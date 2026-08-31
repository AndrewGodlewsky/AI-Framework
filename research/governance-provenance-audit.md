# Provenance and audit: reconstructing who wrote what, after the fact

**Research date:** 2026-08-30
**Ticket:** [Governance, Legal & IP by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/7)
**Question:** How is agent-authored change attributed, and what does an auditor or an incident review
actually need to reconstruct afterwards?

> **This is research, not legal advice.** Nothing here is a legal opinion, and nothing here should be
> relied on as one. Where this document reads a licence, a certificate of origin, or an audit
> criterion, it reports **what the text says and does not say** — never what a court, an auditor, or a
> regulator would conclude from it. Retention obligations, contributor-licence questions, and audit
> scope are jurisdiction- and contract-specific. Take them to counsel and to your auditor.

**What this strand is for.** Two prior tickets covered adjacent ground and this document builds on
them rather than re-deriving them.

- [`verification-observability.md`](./verification-observability.md) (ticket #5) established that **the
  provenance layer and the delivery layer have never been connected** — no published mechanism gated or
  reverted a change *because* it was agent-authored.
- [`tooling-landscape.md`](./tooling-landscape.md) (ticket #6) narrowed that: `agent-approval-check`
  (merged 2026-06-30) **does** gate on agent authorship, by demanding N human approvals; and **no tool
  couples permission to work state**.

Neither asked the governance question. This one does: not *does a mechanism exist*, but **what does it
record, is it trustworthy, and would it satisfy someone reconstructing an incident or an audit?**

**Method and evidence tiers.** Four strands against primary sources — specification text, standards
documents, tool source code, platform documentation. Every claim below carries a tier:

| Tier | Meaning |
|---|---|
| **[PRIMARY]** | Specification, standard, official documentation, or source code, read directly. Stake noted where the publisher is an interested party. |
| **[DIRECT MEASUREMENT]** | Behaviour I executed and observed in this session — git 2.55.0.windows.3 in a disposable repository, and the GitHub REST API against live public repositories. Commands and outputs are reproducible; the observation date is 2026-08-30. |
| **[PLATFORM DATA]** | Counts returned by the GitHub search API. **Unstable** — see §6.2. |
| **[ARCHIVED]** | Primary text retrieved from the Internet Archive because the live URL is now gated. Version differences flagged at the point of use. |

**Vocabulary.** Per [`CONTEXT.md`](../CONTEXT.md): *archetype*, never tier or level; *further along the
spectrum*, never higher up; and **review** (a human reading a change) is kept strictly apart from
**verification** (engineered checking). That distinction turns out to be load-bearing here — §4.1 finds
an audit criterion that cannot tell the two apart, which is exactly why an agent workflow can satisfy
it while producing nothing an incident reviewer could use.

---

## Headline findings

1. **Attribution survives an ordinary GitHub squash-merge — and the reason is a GitHub-specific
   behaviour that no documentation I could find describes.** When GitHub squashes a pull request under
   its default message setting, it appends a `---------` separator and then a **deduplicated,
   aggregated `Co-authored-by:` block** naming every distinct author of the squashed commits. Git's own
   trailer parser reads that block correctly. Across 62 agent-authored merged pull requests in five
   repositories, **61 kept a machine-readable agent attribution and 1 lost it.** *([DIRECT
   MEASUREMENT], §2.3. Read the selection bias in §6.1 before quoting the ratio.)*

2. **But that survival is a repository setting, and two of its three values destroy the record.**
   GitHub's REST API documents `squash_merge_commit_message` as `PR_BODY` | `COMMIT_MESSAGES` | `BLANK`.
   Only `COMMIT_MESSAGES` carries the constituent commit messages — and every trailer in them — into the
   squash. `PR_BODY` substitutes the pull-request description; `BLANK` writes nothing. **An
   administrator flipping one enum value silently converts agent-authored history into
   human-attributed history, for every future merge, with no warning and no error.** *([PRIMARY],
   §2.3.)*

3. **Plain `git` is far more destructive than GitHub, and the difference is invisible.** Measured
   directly: `git merge --squash` produces a message whose trailers git's own parser **cannot read at
   all — 0 of 3 distinct co-authors recovered**. An interactive `rebase -i` squash recovers **1 of 3** —
   only the last commit's trailer block sits in trailer position; the earlier ones become body text.
   `git shortlog --group=trailer:co-authored-by` confirms both results independently. The trailers are
   still *visible* to a human reading the message; they are gone from every machine that counts them.
   **A team that squashes locally and pushes gets a materially worse record than one that clicks
   GitHub's button, and nothing tells them so.** *([DIRECT MEASUREMENT], §2.2.)*

4. **`git blame` never identified an agent, before or after any squash — it has no concept of a
   co-author.** Measured: `git blame --porcelain` emits `author`, `author-mail`, `committer`,
   `committer-mail`, `summary`, `filename`. There is no trailer field, and `git blame` has no
   trailer option. Lines co-authored by three different people all blamed to the single commit author.
   **So the answer to "at what point does `git blame` stop identifying anyone who read the line" is:
   at the first commit.** Blame reads the author field, and in the dominant workflow — a human running
   an agent locally — the human is always in the author field. Blame was never the mechanism. *([DIRECT
   MEASUREMENT], §5.1.)*

5. **Every attribution mechanism that says something about *people* is an unverified assertion in free
   text. The only cryptographic facts available are about *bytes* and *keys*.** A commit signature
   covers the whole commit object — tree, parents, author, committer, and the entire message including
   every trailer ([`gitformat-signature`](https://git-scm.com/docs/signature-format), verified
   2026-08-30). So signing a commit that reads `Co-authored-by: Claude` proves someone holding a key
   committed exactly those characters. It proves nothing about whether a model was involved, whether
   the named party consented, or whether any human read a line. **Signing makes an assertion
   tamper-evident and non-repudiable while leaving its truth entirely untouched.** *([PRIMARY], §1.3.)*

6. **⚠️ Signatures do not survive normal git workflow at all — a much harder negative than the trailer
   result.** Measured: `git rebase` took commits from `%G? = G` (good signature) to `N` (none);
   `git commit --amend` without `-S` stripped the `gpgsig` header entirely; an interactive squash of two
   signed commits produced an unsigned commit. This is structural, not a bug — the payload includes
   `parent` and `committer`, so a rewritten object cannot carry the old signature. Git says so for the
   analogous case: *"It is by definition impossible to preserve signatures… signatures will always be
   removed, buyer beware"* ([`git-filter-branch`](https://git-scm.com/docs/git-filter-branch)). GitHub
   states the consequence in its own words: *"When using the **Rebase and Merge** option on a pull
   request… the commits in the head branch are added to the base branch **without commit signature
   verification**."* **Where a signature does appear after a rewrite, it is the rewriter's — attesting
   bytes that name people the rewriter never spoke to.** *([DIRECT MEASUREMENT] + [PRIMARY], §2.4.)*

7. **⚠️ The provenance that survives a squash on GitHub survives *on GitHub*, not in the repository.**
   In the one loss case I found, the erased pre-squash commit — carrying both `Co-Authored-By: Claude
   Opus 4.8` and a `Claude-Session:` URL — **is still retrievable from GitHub by SHA today**, and
   `refs/pull/54/head` still resolves on the remote. But it is reachable from **zero branches**, and
   git's default fetch refspec is `+refs/heads/*:refs/remotes/origin/*` — **`refs/pull/*` is not
   fetched**. So a clone, a mirror, a fork, an air-gapped copy, or a vendor doing due diligence on the
   source sees nothing. **The audit trail is platform-hosted, and it does not travel with the code.**
   *([DIRECT MEASUREMENT], §2.5.)*

8. **⚠️ The one published mechanism that gates on agent authorship does not read the agent-authorship
   trailer.** `agent-approval-check`'s own source is explicit: *"A commit is agent-authored if its
   committer email is in `agent_emails`"* — it reads `commit.committer.email` and **never parses the
   commit message**. Its default is `noreply@anthropic.com`. That works when the agent commits under
   its own git identity (Copilot coding agent, cloud agents). It **does not fire at all** for the
   dominant case: a developer running Claude Code or Cursor locally, committing as themselves, with the
   agent named only in a `Co-authored-by:` trailer. **The field the gate reads and the field the
   ecosystem writes are not the same field.** *([PRIMARY], source read 2026-08-30, §2.6.)*

9. **The gate's own evidence does not survive the merge it gates.** `agent-approval-check` posts a
   commit status, and its README notes *"Commit statuses attach to a SHA, not a PR."* A squash merge
   produces a new SHA with no status. **The record that "this change was agent-authored and therefore
   required two human approvals" exists only against a commit that is not in the default branch's
   history.** Its threat model is equally frank about forgeability: *"an actor who can push workflow
   changes to the default branch can spoof any required status check, including this one."* *([PRIMARY],
   §2.6.)*

10. **No supply-chain or SBOM standard has a field meaning "this source was written by an AI" — and the
    near-misses all point the wrong way.** SPDX 3.0.1's AI profile models **AI systems as artifacts to
    be inventoried** (`energyConsumption`, `safetyRiskAssessment`, `informationAboutTraining`,
    `modelExplainability`); CycloneDX's ML-BOM `modelCard` is *"must not be specified for other
    component types"* than `machine-learning-model`; NIST SP 800-218A is about *"AI model development"*.
    **Every one treats AI as a thing to inventory, never as a producer whose output needs marking.**
    Anyone citing "SPDX has an AI profile" as coverage of AI-authored code has the arrow backwards.
    *([PRIMARY], §3.)*

11. **⚠️ Ticket #5's SLSA "robot exception" claim is confirmed but needs four corrections, and one of
    them matters a lot.** The text is real: *"An organization MAY choose to grant a Trusted Robot a
    perpetual exception to a policy (e.g. a bot may be able to merge a change that has not been reviewed
    by two parties)."* But: it is **Level 4 only**; **SLSA does not grant it — an organization may**;
    and *Trusted Robot* is a gated term defined as automation whose *"identity and codebase **cannot be
    unilaterally influenced**"*, with Dependabot and import bots as the named examples. **A
    prompt-steered coding agent is hard to reconcile with that clause. The exception was drafted for
    Dependabot, not for an LLM.** Meanwhile SLSA requires reviewers to be *"trusted persons"*, defined
    as *"A human"*. **SLSA draws the human/machine line for approval, and never for authorship.**
    *([PRIMARY], §3.1.)*

12. **The gap was named inside a standards body three years ago and is still open.** in-toto issue
    #244, *"Attestation for AI-assisted code"*, opened **2023-06-03**, untouched since 2023-07-10, still
    open: *"marking which dependencies use AI-assisted code in SBOMs… doesn't solve the whole problem,
    because it doesn't say **which bits of the code were AI-assisted or not**."* Meanwhile **eight
    AI-related predicates were proposed to in-toto in 2026 alone** — every one about *runtime agent
    behaviour* (tool calls, decisions, threat scans, evals), none about authorship. **The community is
    actively building AI attestation. It is building it for what agents do, not for what agents wrote.**
    *([PRIMARY], §3.2.)*

13. **⚠️ SOC 2's change-management criterion is satisfiable by a pipeline that retains nothing.** CC8.1
    and its twelve points of focus require that *processes exist* to authorize, document, track, test
    and approve changes — *"A process is in place to approve system changes prior to implementation."*
    Machine-checked against the full criteria text: **`traceab*` appears 0 times; `evidence` appears 0
    times.** The criterion never requires that the authorizer or approver be *identifiable*, or that the
    reasoning behind a change be *recoverable*. **The finding is not that agent tooling fails SOC 2; it
    is that SOC 2 as written does not detect the failure.** NIST SP 800-53 does: AU-3(f) demands
    *"Identity of any individuals, subjects, or objects/entities associated with the event"* and AU-2(d)
    demands logging *"adequate to support after-the-fact investigations of incidents."* *([ARCHIVED] +
    [PRIMARY], §4.1–4.2.)*

14. **The record that explains *why* an agent made a change has a 30-day half-life and, in the richest
    case, no export path at all.** Claude Code keeps the most complete transcript of any tool surveyed —
    *"every message, tool call, and tool result"* — locally, in plaintext JSONL, **30 days by default**.
    It ships **no documented export command**: `export` and `transcript` each appear **zero times** in
    the slash-commands documentation, and the CLI's only transcript verbs are `purge` and `resume`.
    OpenAI has the inverse: a genuine append-only Compliance API with official download scripts, aimed
    at a source window OpenAI itself documents as **30 days** while telling customers *"Don't assume the
    source retention window replaces your organization's retention policy."* GitHub's audit log runs
    **180 days** and *"does not include client session data, such as the prompts a user sends to Copilot
    locally"*; its coding-agent **session** logs have **no published retention at all**. Cursor states
    the requirement in its own opening line — *"Compliance requires visibility into who did what, when,
    and why"* — then declines it: *"We do not log agent responses or generated code content."* **In no
    product surveyed does the retention of the explanatory record match the retention of the change it
    explains. The commit is permanent.** *([PRIMARY, vendor documentation], §4.5.)*

15. **Blamelessness is being quietly conflated with unreconstructability, and the postmortem template is
    where it shows.** Google's SRE Workbook separates **Root cause** from **Trigger** as distinct
    required fields, and its worked trigger reads *"When the Cluster Turnup team manually started
    another run of the workflow for `a12bcd34`, this action triggered the `admin_server` bug"* — an
    actor, an action, a latent defect. Blameless practice removes *indictment*, not *identification*:
    the doctrine assumes everyone *"did the right thing with the information they had"*, which is only
    checkable if you can recover what information they had. **A diff can never fill that sentence. Only
    a transcript can, and the transcript is the artifact the tooling is least likely to have kept.**
    *([PRIMARY], §4.4.)*

16. **The one product that got the shape right has it switched off in exactly the autonomous case that
    needs it.** Cursor derives AI authorship at *line* granularity from diff signatures, and Cursor
    Blame surfaces *"which lines came from AI assistance, which models were used, and the conversations
    that produced them"*, with conversation summaries on hover. It is also **off by default at team
    level**, on-device only, and — in Cursor's own words — *"has not been implemented for Background
    Agents, or the Cursor CLI yet."* **Line-level provenance exists and is absent from precisely the
    further-along-the-spectrum workflows it was needed for.** *([PRIMARY, vendor documentation], §4.5.)*

### What I could not find

- **No registry of commit trailers exists, for AI disclosure or anything else.** Git defines trailer
  *syntax* (`key`: ASCII alphanumerics and hyphens, colon, arbitrary value) and never a vocabulary. Its
  own list is explicitly local and extensible — *"you can also create your own trailer"*, *"Other
  projects might regularly refer to other kinds of data"*. There is no authority to forge against.
- **No standards body has an authorship predicate.** Re-confirmed against the in-toto vetted list, SLSA
  (both release branches and the draft), SPDX 3.0.1's full 308-file model, and the CycloneDX 1.6 and
  1.7 JSON schemas. `grep -oiE "artificial intelligence|generative|LLM|AI-generated|coding assistant"`
  over `bom-1.7.schema.json` returns **0 matches**; the same sweep over every SLSA spec file returns
  **0 matches**.
- **No documentation from GitHub describing its squash co-author aggregation.** The behaviour is
  demonstrable in the artifact (§2.3) and absent from *About pull request merges*, *Creating a commit
  with multiple authors*, and *Configuring commit squashing* — all fetched 2026-08-30. **Finding 1 rests
  on measurement, not on a documented guarantee, and an undocumented behaviour is one a platform may
  change without notice.**
- **No published retention period for GitHub Copilot coding-agent session logs.** Three surfaces
  checked, including all nine endpoints of the coding-agent management REST API — every one is policy
  and permission management. None returns a session log.
- **ISO/IEC 27001:2022 Annex A control text.** `iso.org` returned **HTTP 403** on both the standard page
  and the Online Browsing Platform. Not circumvented, not sourced second-hand. **Do not cite ISO clause
  text from this document.**

---

## The table this ticket asked for

| Mechanism | What it asserts | Assertion or cryptographic fact | Who can forge it | Survives squash-merge? |
|---|---|---|---|---|
| **`Co-authored-by:` trailer** | A named party co-authored this commit | **Assertion**, free text. GitHub's only check is that the email maps to an account, and that is for the contribution graph | Anyone with commit access, for any name, in one line | **On GitHub, usually yes** — aggregated and deduplicated under `squash_merge_commit_message: COMMIT_MESSAGES`. **In plain git, no** — `merge --squash` recovers 0 of 3; `rebase -i` squash recovers 1 of 3. Lost entirely under `PR_BODY` / `BLANK` or a hand-edited message |
| **`Assisted-by:` (Linux kernel)** | A coding assistant was used, with tools named | **Assertion**, mandatory by policy, **validated by nothing** — the kernel documents no check | Anyone; the realistic failure is omission, not forgery | Same trailer mechanics as above. The kernel does not squash-merge; this is a mailing-list workflow |
| **`Claude-Session:` (observed emitter)** | A pointer to the session that produced the commit | **Assertion**, and the only trailer found that links a commit to a record of *how* it was produced | Anyone | Same mechanics — and it is the trailer whose loss costs the most (§2.5) |
| **`Signed-off-by:` / DCO 1.1** | Certification of **origin and licensing authority**. The words *read*, *review*, *understand*, *inspect* and *correct* **do not appear in the DCO** | **Assertion.** Git: *"The meaning of a signoff depends on the project"* | Anyone with commit access, for any name. Git ships `verify-commit` and `verify-tag`; there is **no** `verify-signoff` | Yes, as a trailer — with the same squash mechanics. But the sign-off after a squash certifies a commit object that did not exist when it was made |
| **Author / committer fields** | Identity, per `user.*` config | **Assertion**, one `git config` away from anything | Anyone, trivially | **Author survives** — GitHub sets the squash author from the pull-request author, so an agent that commits under its own identity stays named. **Committer becomes GitHub** |
| **GPG / SSH / X.509 signature** | This key signed **these exact bytes**: tree, parents, author, committer, full message including every trailer | **Cryptographic fact — but a narrow one.** Says nothing about authorship, consent, or comprehension | Not without the private key. But the key-holder may sign arbitrary field and trailer values | **No.** Measured: `G` → `N` across rebase, amend, and interactive squash. Structurally impossible — the payload covers `parent` and `committer` |
| **GitHub `Verified` (local key)** | A signature GitHub checked **once, at push time** | Cryptographic fact, **cached as a platform assertion**: *"GitHub will not re-verify previously signed commits"* after revocation | Key compromise | n/a — the squash commit is a new object, signed by GitHub (below) |
| **GitHub-signed web/API/bot commit** | GitHub's `web-flow` key signed an object GitHub constructed | **Platform assertion sealed with GitHub's key.** The user contributed a session, not a key. GitHub's setup doc: *"The email address does not need to be valid"* | **Anyone who can authenticate as the user** — stolen token, OAuth app, or an agent holding repo scope | This *is* the squash commit. Verified `true` on a commit whose author field GitHub set from pull-request metadata |
| **GitHub `Partially verified`** | GitHub's own disclosure of the gap: *"the commit signature doesn't guarantee the consent of the author"* | Platform assertion, honestly scoped | n/a | Only visible under vigilant mode, which is opt-in |
| **`on-behalf-of:` (GitHub)** | Attribution to an organization | **Assertion + out-of-band verification** — requires org membership, a signed commit, and domain-verified emails | Requires org and domain control | The counterexample that proves the rest were left unverified **by choice** |
| **Sigstore / gitsign** | An OIDC issuer vouched for this subject; Fulcio issued a short-lived cert; **Rekor witnessed it** | **Cryptographic fact, strongest identity binding in the survey.** `gitsign.matchCommitter` binds signer to claimed committer — and is **off by default** | OIDC compromise, or control of the CI workflow at that ref — **but the forgery is logged in a public append-only ledger** | No — it is a signature (above). Its SAN URI names the **workflow**, not the agent, model, or prompt |
| **SLSA build provenance** | What platform built this artifact from what inputs | Cryptographic fact **about the build** | Compromise of the build platform | n/a — attests artifacts, not commits. **Says nothing about who wrote the source** |
| **`agent-approval-check` status** | N humans with write access approved a PR containing an agent-committed commit | **Platform assertion**, SHA-scoped | Its own threat model: *"an actor who can push workflow changes to the default branch can spoof any required status check, including this one"* | **No.** Statuses attach to a SHA; the squash creates a new one. The gate's evidence does not enter the branch it gates |

---

# 1. What each mechanism actually asserts

## 1.1 The substrate: git validates nothing, and there is no vocabulary

**[PRIMARY]** [`git-interpret-trailers`](https://git-scm.com/docs/git-interpret-trailers), verified
2026-08-30. Ticket #5 established the parsing rule; the governance-relevant half is what is *absent*.

The spec defines a trailer by **position and shape**:

> "Existing trailers are extracted from the input by looking for a group of one or more lines that (i)
> is all trailers, or (ii) contains at least one Git-generated or user-configured trailer and consists
> of at least 25% trailers. The group must be preceded by one or more empty (or whitespace-only) lines.
> The group must either be at the end of the input or be the last non-whitespace lines before a line
> that starts with `---`"

and the key by character class alone:

> "A _trailer_ in its simplest form is a key-value pair with a colon as a separator. The _key_ consists
> of ASCII alphanumeric characters and hyphens (`-`)."

**That is the entire constraint.** No registry, no schema, no signature over the trailer, no check that
a named party exists or consented.

**[PRIMARY]** [`Documentation/SubmittingPatches`](https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches),
verified 2026-08-30, is the git project's own trailer list — `Reported-by:`, `Acked-by:`,
`Reviewed-by:`, `Tested-by:`, `Co-authored-by:`, `Based-on-patch-by:`, `Helped-by:`, `Mentored-by:`,
`Suggested-by:` — and it closes with the two sentences that settle the registry question:

> "While you can also create your own trailer if the situation warrants it, we encourage you to instead
> use one of the common trailers in this project highlighted above."

> "Other projects might regularly refer to other kinds of data, like `Fixes:` and `Link:` in the Linux
> Kernel project, but these ones in particular are not used in this project."

**Two consequences worth carrying forward.** First, **trailer vocabularies are per-project convention
negotiated in each project's contributing docs** — there is nothing to standardise against and nothing
to forge against. Second, **no AI-related trailer appears in git's list at all**, and git's own gloss on
`Co-authored-by:` is *"used to indicate that people exchanged drafts of a patch before submitting it"* —
a description of human collaboration that an agent does not fit.

**[PRIMARY]** GitHub, [Creating a commit with multiple authors](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors),
verified 2026-08-30. Syntax `Co-authored-by: NAME <NAME@EXAMPLE.COM>`, after the description, separated
by a blank line. The only stated check: *"For the commit to count as a contribution, use an email
address associated with their account on GitHub.com"* — and that is for the contribution graph.
**Fetched in full, the page documents no identity verification of a named co-author, and says nothing
about what happens to the trailer when a pull request is merged.**

**The proof that this was a choice, not an oversight.** The same GitHub page documents a second trailer
that *is* verified: *"Add an `on-behalf-of:` trailer to a signed commit to attribute it to an
organization. To use the trailer, you must be a member of the organization, and both your commit email
and the organization email must be in a domain verified by the organization."* **Where GitHub wanted a
trailer to be a fact, it added out-of-band verification. It did not do so for `Co-authored-by:`.**

## 1.2 The DCO: what a sign-off certifies, and what it conspicuously does not

**[PRIMARY]** [Developer Certificate of Origin 1.1](https://developercertificate.org/), verified
2026-08-30. The instrument is short enough to reason about exactly:

> **(a)** "The contribution was created in whole or in part by me and I have the right to submit it
> under the open source license indicated in the file; or
> **(b)** The contribution is based upon previous work that, to the best of my knowledge, is covered
> under an appropriate open source license and I have the right under that license to submit that work
> with modifications, whether created in whole or in part by me, under the same open source license
> (unless I am permitted to submit under a different license), as indicated in the file; or
> **(c)** The contribution was provided directly to me by some other person who certified (a), (b) or
> (c) and I have not modified it.
> **(d)** I understand and agree that this project and the contribution are public and that a record of
> the contribution (including all personal information I submit with it, including my sign-off) is
> maintained indefinitely and may be redistributed consistent with this project or the open source
> license(s) involved."

**The sharp question, answered strictly from the text: the DCO does not require the signer to have read
or understood the code.** The words *read*, *review*, *understand*, *inspect*, *test* and *correct* do
not appear anywhere in the document. Every clause is about **provenance and licensing authority**.
Clause (b)'s *"to the best of my knowledge"* is the document's only nod to the signer's epistemic state,
and it is scoped to the licence status of the antecedent work — not to the code's correctness, and not
to the signer's comprehension of it.

**Applied to a commit an agent wrote and a human did not read, the ambiguity is locatable precisely.**

1. **Clause (a) turns entirely on the undefined word "created."** If directing, prompting, configuring
   and accepting an agent's output counts as creating *"in part"*, (a) is satisfied on its face. If
   "created" requires having composed or at minimum comprehended the text, it is not. **The instrument
   supplies no test either way. This is a gap in the DCO, not a question it answers badly.**
2. **Clause (c) does not rescue the case.** It requires the contribution to have been *"provided
   directly to me by some other person who certified (a), (b) or (c)"*. An agent is not a person and
   issues no certification, so (c) is unavailable by its own terms.
3. **Clause (b) is orthogonal.** It concerns derivation from *identified* prior work under a *known*
   licence. The DCO has no clause covering "the provenance of the inputs is unknown to me."
4. **Clause (d) applies regardless and is permanent.** *"maintained indefinitely."* Whatever (a) meant
   at the moment of signing, the assertion outlives every record of the circumstances in which it was
   made — which is §4.5's finding stated from the other end.

**So: the DCO neither prohibits nor authorises signing off on unread code. It asks a question about
origin that unread agent output does not cleanly answer.** *(Again — a reading of the text, not a legal
opinion.)*

### Git's own position is the sharpest primary text in this corpus

**[PRIMARY]** [`gitfaq`](https://git-scm.com/docs/gitfaq), verified 2026-08-30, on why git refuses to
ship a `commit.signoff` setting:

> "Git intentionally does not (and will not) provide a configuration variable, such as
> `commit.signoff`, to automatically add `--signoff` by default. The reason is to protect the legal and
> intentional significance of a sign-off. If there were more automated and widely publicized ways for
> sign-offs to be appended, **it would become easier for someone to argue later that a "Signed-off-by"
> trailer was just added out of habit or by automation, without the committer's full awareness or
> intent to certify their agreement with the Developer Certificate of Origin**… This could undermine
> the sign-off's credibility in legal or contractual situations."

**The Git project's position is that a sign-off's entire value rests on the committer's "full awareness
or intent", and that automating its insertion degrades it.** Note the asymmetry with signing: git
*does* ship `commit.gpgSign` to sign everything automatically. **Git treats a signature as a mechanical
operation safe to automate, and a sign-off as an act of will that must not be.**

### And GitHub ships exactly what git refused to build

**[PRIMARY]** GitHub, [Managing the commit signoff policy for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-commit-signoff-policy-for-your-repository),
verified 2026-08-30:

> "Once compulsory commit signoffs are enabled for a repository, **every commit made to that repository
> through your instance's web interface will automatically be signed off on by the commit author**" —
> described as *"a seamless part of the commit process."*

**Git: automation makes it arguable the sign-off was "added out of habit or by automation." GitHub: a
repository setting that adds it to every web commit, marketed as seamless.** The two positions cannot
both be right, and a governance document should not cite "we require DCO sign-off" without saying which
one is in force.

### The kernel writes the missing requirement down separately — which proves it is missing

**[PRIMARY]** [`Documentation/process/coding-assistants.rst`](https://docs.kernel.org/process/coding-assistants.html),
verified 2026-08-30:

> "**AI agents MUST NOT add Signed-off-by tags. Only humans can legally certify the Developer
> Certificate of Origin (DCO).** The human submitter is responsible for:
> * Reviewing all AI-generated code
> * Ensuring compliance with licensing requirements
> * Adding their own Signed-off-by tag to certify the DCO
> * Taking full responsibility for the contribution"

with the disclosure trailer specified as `Assisted-by: LLM [TOOL1] [TOOL2]`, and made mandatory by
`submitting-patches.rst`: *"If you used any sort of advanced coding tool in the creation of your patch,
you need to acknowledge that use by adding an Assisted-by tag. Failure to do so may impede the
acceptance of your work."*

**[PRIMARY]** [`Documentation/process/generated-content.rst`](https://docs.kernel.org/process/generated-content.html),
verified 2026-08-30, is where the kernel supplies what the DCO does not:

> "**Ensure that you understand your entire submission and are prepared to respond to review
> comments.**"

> "As with the output of any tooling, the result may be incorrect or inappropriate. **You are expected
> to understand and to be able to defend everything you submit. If you are unable to do so, then do not
> submit the resulting changes.** If you do so anyway, maintainers are entitled to reject your series
> without detailed review."

**The largest DCO-using project in the world found it necessary to write a comprehension requirement in
a separate document, because the DCO does not contain one.** That is the strongest available evidence
that §1.2's reading is not a quibble.

**And note the structural reason an agent cannot be a kernel co-author.** `submitting-patches.rst`:
*"Since Co-developed-by: denotes authorship, every Co-developed-by: must be immediately followed by a
Signed-off-by: of the associated co-author."* Authorship trailers demand a DCO sign-off; no agent can
give one; therefore no agent can be an author. **The kernel closed that door by construction, before it
ever named AI.** The industry convention of writing an agent into `Co-authored-by:` asserts exactly what
the kernel's design forbids — and nothing anywhere validates either form.

## 1.3 Signing: a real cryptographic fact, and a narrow one

**[PRIMARY]** [`gitformat-signature`](https://git-scm.com/docs/signature-format), verified 2026-08-30.
Its worked example shows the signed payload in full — `tree`, `parent`, `author` (name, email,
timestamp), `committer`, and the entire message — with the signature living in a `gpgsig` object header
excluded from its own payload.

**[DIRECT MEASUREMENT]** Confirmed by inspection. An SSH-signed commit created in this session:

```
tree 62e8e652ac0047522396ae309faca9694cdb4cdb
parent 18635966906c12822603b924bb5fbbaa4e5fd1a4
author Human Dev <test@example.com> 1788144825 -0400
committer Human Dev <test@example.com> 1788144825 -0400
gpgsig -----BEGIN SSH SIGNATURE-----
 …
signed commit B
```

**Because the message is covered in its entirety, every trailer is inside the signed bytes.** Which
gives the precise answer to "does a signature make a `Co-authored-by:` trailer true":

**No. It makes a false one non-repudiable.** The chain, each link from spec text: the payload is the
commit object, so the trailer is signed; trailer values are unconstrained free text
(`git commit --trailer` accepts any key-value pair); git provides no verification of trailer contents
anywhere — `git verify-commit` *"Validates the GPG signature created by `git commit -S`"*, and nothing
else. **Signing raises the integrity guarantee of a claim without touching its truth value.**

GitHub says this itself, about the `author` field — which is a *first-class field* of the payload, so
the point applies *a fortiori* to a free-text trailer. From the vigilant-mode status table:

> "**Partially verified** | The commit is signed, and the signature was successfully verified, but the
> commit has an author who: a) is not the committer and b) has enabled vigilant mode. In this case,
> **the commit signature doesn't guarantee the consent of the author**, so the commit is only partially
> verified."

**That is the platform naming the gap between signature and consent, and pricing it into the badge.**

### Sigstore/gitsign is the only mechanism that treats a machine as a first-class signer

**[PRIMARY]** [`sigstore/gitsign`](https://raw.githubusercontent.com/sigstore/gitsign/main/README.md)
and [`docs/committer-verification.md`](https://raw.githubusercontent.com/sigstore/gitsign/main/docs/committer-verification.md),
verified 2026-08-30. Three properties nothing else in this survey has:

- **Machine identity has its own documented binding path.** *"An `EmailAddresses` cert value matches the
  committer `user.email`. This should be used for most human committer verification. A `URI` cert value
  matches the committer `user.name`. This should be used for most automated user committer
  verification."* The SAN type itself tells a verifier which kind of principal signed.
- **An opt-in check that the signer matches the claimed committer** — `gitsign.matchCommitter`, the one
  primitive in this survey that closes git's "signer ≠ claimed identity" gap. **It defaults to false.**
- **Forgery leaves evidence by design.** Signing events are witnessed in Rekor, a public append-only
  log: *"Identity owners can monitor the log to verify that their identity is being properly used."*

gitsign is also honest about the limit, and its warning applies to every mechanism above:

> "**NOTE**: `gitsign verify` is preferred over `git verify-commit`… The git commands do not pass
> through any expected identity information to the signing tools, so they only verify cryptographic
> integrity and that the data exists on Rekor, but **not who put the data there**."

**And the limit that matters here:** the workload SAN names a *workflow path*
(`https://myorg/myrepo/path/to/workflow`). **It identifies the CI job that produced the commit, never
the agent, the model, or the prompt inside it.**

---

# 2. Whether attribution survives

**This section is the strand's centre of gravity, and most of it is measurement rather than
citation.** A provenance record that a routine operation erases is not an audit trail. The evidence
below says the situation is worse than the documentation implies and better than the naive git
experiment implies, and the difference between those two is a repository setting nobody looks at.

## 2.1 The experiment

**[DIRECT MEASUREMENT]** git 2.55.0.windows.3, disposable repository, 2026-08-30. A branch of three
commits, each carrying `Co-authored-by:`, `Signed-off-by:` and `Assisted-by:` trailers, plus a
distinct-co-author variant (Alice / Bob / Carol, one per commit) to detect partial loss. Survival was
measured three ways that must agree: `git log --format='%(trailers:only=true)'`,
`git interpret-trailers --parse`, and `git shortlog --group=trailer:co-authored-by`. Signature survival
was measured with `%G?` on SSH-signed commits.

**Why measure rather than cite:** a trailer that is still *visible* in the message but no longer *parsed*
as a trailer looks fine to a human reading `git log` and is invisible to every tool that counts. That
failure mode does not appear in any documentation, and it is the one that actually happens.

## 2.2 Plain git destroys trailers, silently

**[DIRECT MEASUREMENT]** Three commits, three distinct co-authors, three squash methods:

| Operation | Message shape | Co-authors git **parses** | `shortlog --group=trailer:co-authored-by` |
|---|---|---|---|
| *(no squash — baseline)* | three commits | **3 of 3** | Alice 1, Bob 1, Carol 1 |
| `git merge --squash` + commit | nested `commit`/`Author:`/`Date:` blocks, message bodies **indented** | **0 of 3** | *(empty)* |
| `git rebase -i` with `squash` | messages concatenated, unindented | **1 of 3** — Carol only | Carol 1 |
| GitHub's real squash shape (§2.3) | bullets + `---------` + aggregated block | **2 of 2 distinct** | Cursor 1, RESILIENCE 1 |

`git merge --squash`'s output indents every original message by four spaces inside a nested block, so
no line group satisfies the trailer-block rule. `git log --grep='Co-authored-by'` still matches — the
text is there. `git interpret-trailers --parse` returns nothing. **The trailers survive as prose and
die as data.**

`rebase -i` squash is subtler and arguably worse, because it *looks* like it worked: the last commit's
trailer block is in trailer position and parses; every earlier commit's trailers have become body text.
**In a five-commit branch where an agent co-authored the first four and a human hand-fixed the fifth,
the parsed record says the change was entirely human.**

## 2.3 GitHub's squash preserves it — via an undocumented behaviour

**[DIRECT MEASUREMENT]** `anthropics/claude-code-action` PR #1702, three branch commits each carrying
`Co-authored-by: Cursor <cursoragent@cursor.com>`, squash-merged. The resulting commit on `main`
(`2d7a787f`, author `RESILIENCE Agentic Solutions`, committer `GitHub`, `verified: true`):

```
fix: use paths in delete_files prompt example (#1702)

* fix: use paths param in delete_files prompt example
  …
  Co-authored-by: Cursor <cursoragent@cursor.com>

* test: prove delete_files prompt against the live MCP schema
  …
  Co-authored-by: Cursor <cursoragent@cursor.com>

* test: cover delete_files schema edges and the sibling commit_files tool
  …
  Co-authored-by: Cursor <cursoragent@cursor.com>

---------

Co-authored-by: RESILIENCE Agentic Solutions <286555414+WeAreResilience@users.noreply.github.com>
Co-authored-by: Cursor <cursoragent@cursor.com>
```

**GitHub appends a `---------` separator and then a deduplicated, aggregated trailer block naming every
distinct author.** Reproducing that exact message shape locally, git parses **both** trailers correctly
— the `---------` line is precisely what `git-interpret-trailers` permits before a trailing block.

**This behaviour is not in GitHub's documentation.** I fetched *About pull request merges*, *Creating a
commit with multiple authors*, and *Configuring commit squashing for pull requests* on 2026-08-30. The
first two contain **no mention of "co-author" or "Co-authored-by" in the context of merging at all**.
**Finding 1 therefore rests on measurement of the artifact, not on a documented guarantee — and an
undocumented behaviour can change without a changelog entry.**

### The setting that decides it

**[PRIMARY]** GitHub [REST API — Repositories](https://docs.github.com/en/rest/repos/repos), verified
2026-08-30, is the authoritative machine-readable definition:

| Field | Values |
|---|---|
| `squash_merge_commit_title` | `PR_TITLE` — *"default to the pull request's title"* · `COMMIT_OR_PR_TITLE` — *"default to the commit's title (if only one commit) or the pull request's title"* |
| `squash_merge_commit_message` | `PR_BODY` — *"default to the pull request's body"* · `COMMIT_MESSAGES` — *"default to the branch's commit messages"* · `BLANK` — *"default to a blank commit message"* |

Corroborated by the settings page: *"The default commit message presented to contributors when merging
is the commit title and message if the pull request contains only 1 commit, or the pull request title
and list of commits if the pull request contains 2 or more commits."*

**Only `COMMIT_MESSAGES` carries the constituent commit messages — and therefore every trailer in them
— into the squash.** Under `PR_BODY` the message is the pull-request description, which no tool writes
trailers into. Under `BLANK` there is nothing at all. **[DIRECT MEASUREMENT]** committing a
`PR_BODY`-shaped message locally yields **zero parsed trailers**, as expected.

**This is the governance finding, and it is a one-enum-value finding:** an administrator can convert
every future agent-authored merge into human-attributed history by changing a dropdown, with no
warning, no error, and no visible difference in the pull-request UI. It is the same pattern ticket #6
found at the permission layer — *the constraint that appears to hold the record together is an
administrator-flippable default.*

### The measurement

**[DIRECT MEASUREMENT]** Across five repositories, every merged pull request in the most recent 25
whose branch commits carried an agent identity (trailer or committer email), checked against the
resulting commit on the default branch. Merge-commit merges count as surviving because the agent's
commits remain reachable as parents.

| Repository | Agent-authored merged PRs | Attribution survived | Lost |
|---|---|---|---|
| `anthropics/claude-code-action` | 3 | 3 | 0 |
| `iorate/ublacklist` | 9 | 9 | 0 |
| `fol2/roguecardv2` | 20 | 19 | **1** |
| `Yukoval-Dakia/the-learning-project` | 5 | 5 | 0 |
| `time-yide/yide-acompanha` | 25 | 25 | 0 |
| **Total** | **62** | **61** | **1** |

**⚠️ Read the selection bias before quoting this.** These repositories were reached *through* GitHub
commit search for agent trailers — that is, they were selected *because their default branches contain
surviving trailers*. **The sample is drawn from survivors and cannot estimate a population loss rate.**
It establishes that survival is the normal outcome under default settings, and it locates the loss case
precisely. It does not measure how often the loss case occurs.

## 2.4 Signatures do not survive at all

**[DIRECT MEASUREMENT]** SSH-signed commits, verified `%G? = G` before each operation:

| Operation | Signature after | `gpgsig` header | Trailers |
|---|---|---|---|
| `git rebase master` (no `-S`) | **`N` — none** | absent | preserved intact |
| `git commit --amend --no-edit` (no `-S`) | **`N` — none** | absent | preserved |
| `git rebase -i` squash (no `-S`) | **`N` — none** | absent | last block only |

This is structural. The payload includes `parent` and `committer` (§1.3), so a rewritten object has
different bytes and the old detached signature cannot validate against them. Git states the
impossibility for the analogous case — **[PRIMARY]** [`git-filter-branch`](https://git-scm.com/docs/git-filter-branch):
*"It is by definition impossible to preserve signatures… signatures will always be removed, buyer
beware."* And `commit.gpgSign`'s own warning presupposes re-signing: *"Use of this option when doing
operations such as rebase can result in a large number of commits being signed."*

**⚠️ A caveat for anyone citing this:** `git-rebase(1)` contains **no sentence** saying signatures are
dropped. Its only signing content is the `-S/--gpg-sign` option entry. Do not cite `git-rebase` for a
sentence it does not contain — cite the measurement, `git-filter-branch`, or GitHub.

**[PRIMARY]** GitHub states the platform consequence directly, in
[`rebase_and_merge_verification.md`](https://github.com/github/docs/blob/main/data/reusables/pull_requests/rebase_and_merge_verification.md),
verified 2026-08-30:

> "When using the **Rebase and Merge** option on a pull request, it's important to note that the commits
> in the head branch are added to the base branch **without commit signature verification**. When you
> use this option, GitHub creates a modified commit, using the data and content of the original commit.
> This means that GitHub didn't truly create this commit, and can't therefore sign it as a generic
> system user. GitHub doesn't have access to the committer's private signing keys, so it can't sign the
> commit on the user's behalf."

**The governance consequence.** After any rewrite, the signature — where one exists — attests the
**rewriter**, while the author field and every trailer are carried across verbatim and now sit inside a
signature that says nothing about the people they name. **A "Verified" badge on a squashed commit is a
statement about GitHub's platform key and GitHub's access control. It is not a statement about the
person in the author field, and it is not a statement about the agent in the trailer.**

**[DIRECT MEASUREMENT]** confirms the shape. The signed payload of squash commit `2d7a787f`:

```
tree 8c50571a52f596a63fdd2ef8a2220cb60ef60db8
parent b58c16b3256e2622c33d05f085049ab7ce2767de
author RESILIENCE Agentic Solutions <support@we-are-resilience.com> …
committer GitHub <noreply@github.com> …
```

**GitHub signed an object asserting an author identity that GitHub itself populated from pull-request
metadata.** The author contributed no key. Per **[PRIMARY]** GitHub's own web-commit-signing setup
instructions, the signing account's *"email address does not need to be valid."*

## 2.5 The loss case, and where the erased record actually goes

**[DIRECT MEASUREMENT]** The single loss in §2.3 is the whole strand in one artifact.

`fol2/roguecardv2` PR #54, five branch commits. Commit `6320af42` carried:

```
Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_018Mcehz5kmHVehvoTrort8j
```

The commit that landed on the default branch, single parent, author **`James To`** (human), committer
`GitHub`, `verified: true`:

```
feat(combat): SPINE S2+S3 — preview tints, chrome pulses, WebGL stability (#54)

S2: preview-tinted hand numbers, Pixi chrome pulses, dashed aim arc. S3: aim/drag rAF de-thrash,
production context-loss recovery… All change-carrying CI lanes green…
```

**No `Co-Authored-By`. No `Claude-Session`. No `Assisted-by`.** A hand-written summary replaced the
constituent commit messages, and with them every trace of agent authorship. `git blame` on those lines
now returns a human name, on a commit GitHub marks Verified.

**Note precisely what was lost.** Not just the *class* assertion that a model was involved — the
**instance pointer**. `Claude-Session:` is the only trailer found in this project's research that links
a commit to a retrievable record of *how* it was produced. **The one field that would let an incident
reviewer answer "why did the agent do this?" is a line of free text in a commit message, and it is
erased by the same operation that erases everything else.**

### The erased record still exists — on GitHub, not in the repository

**[DIRECT MEASUREMENT]**, all four checks 2026-08-30:

| Check | Result |
|---|---|
| Is `6320af42` still retrievable from GitHub by SHA? | **Yes** — full message, both trailers intact |
| How many branches contain it? | **0** |
| Does `refs/pull/54/head` still resolve on the remote? | **Yes** — `502fef7b…` |
| Does a default clone fetch it? | **No.** Default refspec: `+refs/heads/*:refs/remotes/origin/*` — `refs/pull/*` is not fetched |

**This is the nuance the strand needs.** Provenance erased from git history survives as **platform
data**, addressable by SHA and through `refs/pull/*`, which GitHub retains. It does **not** survive
into any clone, mirror, fork, archive, air-gapped copy, or vendor's due-diligence snapshot.

**So the honest formulation is:** *attribution survives normal git workflow on GitHub, under default
settings, as a GitHub-hosted record — and the code can be separated from that record by any operation
as ordinary as `git clone`.* An organisation whose retention story is "it's in the git history" is
wrong twice: the trailers may not be in the history, and the recoverable copy is in a vendor's
database, governed by that vendor's policy rather than the team's.

## 2.6 The one provenance-gated mechanism reads a different field

Ticket #6 established that `agent-approval-check` (merged 2026-06-30, `anthropics/claude-code-action`)
gates merges on agent authorship. **This strand's question is what it reads.**

**[PRIMARY]** `agent-approval-check/agent_approval_check.py`, 1,828 lines, read 2026-08-30:

```python
def get_committer_email(commit: dict) -> str:
    return commit.get("commit", {}).get("committer", {}).get("email", "")

def is_agent_commit(commit: dict, config: AgentConfig) -> bool:
    email = get_committer_email(commit).lower()
    return email in (e.lower() for e in config.agent_emails)
```

and its own module docstring:

> "**AGENT DETECTION:** A commit is agent-authored if its committer email is in `agent_emails`. A PR is
> agent-authored if its creator login is in `agent_app_logins`."

Default `agent_emails: noreply@anthropic.com`; default `agent_logins: claude[bot],claude-code[bot]`.
**Grepping the full source for `co-author`, `coauthor`, or `trailer` returns zero matches. The commit
message body is never parsed.**

**Why this matters more than it looks.** Two populations of agent-authored commits exist, and this gate
sees only one:

- **The agent commits under its own git identity** — Copilot coding agent
  (`copilot-swe-agent[bot] <198982749+Copilot@users.noreply.github.com>`), claude-code-action, cloud
  agents. The agent is in the author or committer field. **The gate fires.**
- **A human runs an agent locally and commits as themselves** — Claude Code CLI, Cursor, in-editor
  Copilot. The human is author *and* committer; the agent appears only in a `Co-authored-by:` trailer,
  if the tool emits one. **The gate does not fire, and the pull request merges with one approval or
  none.**

**The second population is the larger one, and it is the one this project's spectrum is mostly about.**
**[PLATFORM DATA]** GitHub commit search returns on the order of 10⁶–10⁷ commits containing
`"Co-Authored-By: Claude"` and ~1.5×10⁶ containing `"Co-authored-by: Copilot"` — see §6.2 on why those
figures must be quoted as orders of magnitude. Essentially all of them are trailer-only.

**The field the gate reads and the field the ecosystem writes are not the same field.** That is a
sharper version of ticket #5's "missing wire": the wire exists now, and it is plugged into the wrong
socket for the majority workflow.

### And the gate's evidence does not survive the merge

**[PRIMARY]** the action's own README, read 2026-08-30:

> "**Sibling-PR guard.** Commit statuses attach to a SHA, not a PR."

> "**Tamper-proof triggers.** …This tamper-resistance assumes the workflow file itself is protected: **an
> actor who can push workflow changes to the default branch can spoof any required status check,
> including this one**, so protect `.github/workflows/` via branch protection or CODEOWNERS."

> "**Fail-closed.** Any unhandled error exits non-zero; the required status stays non-success and the PR
> stays blocked. **PRs with >100 commits are treated as agent-authored because the full commit list
> can't be verified.**"

Statuses are SHA-scoped; the squash creates a new SHA. **So the assertion "this change was
agent-authored and therefore required two human approvals" is recorded against a commit that is not in
the default branch's history — recoverable through the pull request on GitHub, and absent from every
clone.** The same platform-not-repository split as §2.5.

**Credit where due:** the fail-closed >100-commit rule and the self-disclosed spoofing path are better
engineering hygiene than most of this corpus. The criticism is of *coverage*, not of care.

---

# 3. Supply-chain provenance: the build, never the author

Ticket #5 concluded the honest answer is *"only build provenance."* This strand re-verified that against
current spec text and can now say something more precise: **the standards are not silent on AI — several
model it explicitly — but every one of them models AI as a thing to inventory rather than as a producer
whose output needs marking.**

## 3.1 SLSA

**[PRIMARY]** slsa.dev, verified 2026-08-30. **Version correction:** v1.1 is not current. **v1.2 is**
(*"Version 1.2 is the current version"*), and `releases/v1.2/spec/source-requirements.md` is
byte-identical to the `main` draft (`sha256 3b8a86e4…`). **The Source Track is released text, not a
draft.**

**Build track: no source authorship.** The only "who" in build provenance is the platform —
`builder.id`, *"URI indicating the transitive closure of the trusted build platform."* Grepping the v1.1
provenance spec for `author|human|person|creator` returns only prose about the document itself.

**Source track: authorship exists, but only as account identity.**

> "**Source Provenance** — Information about how a Source Revision came to exist… and **who the
> contributors were**"

> "The SCS MUST document how actors are identified for the purposes of attribution. Activities conducted
> on the SCS SHOULD be attributed to authenticated identities."

An "actor" is an SCS account. **SLSA never asks whether the entity behind that account was a human
typing or a model generating.**

**The robot exception, verbatim, with ticket #5's claim corrected:**

> "**Two-party review** — Changes in protected branches MUST be agreed to by two or more trusted persons
> prior to submission."
>
> "**[Trusted Robot Contributions]** An organization MAY choose to grant a Trusted Robot a perpetual
> exception to a policy (e.g. a bot may be able to merge a change that has not been reviewed by two
> parties). Examples: Import and migration bots that move code from one repo to another. Dependabot"

Four corrections to *"SLSA grants robots a perpetual two-person-review exception"*:

1. It is **`two-party-review`** by requirement ID, though the rule text says *"trusted persons"*.
2. It is **Level 4 only** — the requirement row carries a checkmark in L4 and nothing at L1–L3. There is
   no two-party requirement at the lower levels to be excepted from.
3. **SLSA does not grant it.** The modal is `MAY` and the subject is *"An organization"*. SLSA declines
   to forbid the practice; it confers nothing.
4. **⚠️ "Trusted Robot" is a gated term with an exclusion that likely disqualifies LLM agents:**

> "**Trusted person** | A human who is authorized by the organization to propose and approve changes to
> the source.
> **Trusted robot** | Automation authorized by the organization to act in explicitly defined contexts.
> **The robot's identity and codebase cannot be unilaterally influenced.**"

**A prompt-steered coding agent, whose behaviour is directed by a mutable context window, is hard to
reconcile with "cannot be unilaterally influenced." The exception was drafted for Dependabot.**

**And the asymmetry that *is* there:** review must be by *"trusted persons"*, defined as *"A human"*.
**SLSA draws the human/machine line for approval and never for authorship** — which is itself the
finding.

**AI: absolute silence.** `grep -rniE "\bAI\b|artificial intelligence|\bLLM\b|machine learning|generative|copilot|autonom"`
across `source-requirements`, `provenance`, `terminology`, `build-requirements`, `tracks`,
`verifying-source`, `future-directions` and `attestation-model`, in the main draft and both release
branches: **0 matches.**

## 3.2 in-toto: architecturally capable, deliberately unfilled

**[PRIMARY]** verified 2026-08-30. The Statement is four fields (`_type`, `subject`, `predicateType`,
`predicate`) taking an arbitrary predicate-type URI — all semantics live in the predicate. The complete
vetted list: CycloneDX, Link, Reference, Release, Runtime Traces, SCAI Report, SLSA Provenance, SLSA
Verification Summary, SPDX2, SPDX3, Simple Verification Result, Test Result, VULNS. **None models source
authorship or AI involvement.** Directory listing (17 entries) matches; most recent commit 2026-07-19.

**The finding is the open issue.** in-toto **#244, "Attestation for AI-assisted code"**, opened
**2023-06-03**, last touched **2023-07-10**, **still open**:

> "AI-assisted source code is probably coming sooner than later… Part of the solution is in marking
> which dependencies use AI-assisted code in SBOMs, but that doesn't solve the whole problem, **because
> it doesn't say which bits of the code were AI-assisted or not.** So I imagine there's room for an
> attestation which gives you this information. Or maybe that should be the job of an SCM commit now,
> I'm not sure."

**That is this document's question, asked inside the standards body three years ago, and never
answered.**

**⚠️ Meanwhile the body is very busy with AI — in a different direction.** Eight AI-related predicates
were proposed in 2026: AI Agent Action (#588), AI Agent Decision (#591), agent-threat-scan (#552),
eval-result (#575), PRML (#587), Adversarial Execution Evidence (#570) and others. #588's own framing:

> "New predicate type for recording AI agent tool invocations as observed by protocol intermediaries…
> Application logs are insufficient for auditing because the entity writing the log is the same entity
> whose behavior needs verification."

That attests **runtime tool calls**, not code authorship. **All are unvetted proposals — cite them as
evidence of live interest, never as standards.** Also open since 2023-01-24: #124, *"A Source Attestation
for recording metadata about source code."*

## 3.3 SPDX 3.0.1: the AI profile models the model, not the code — with one live loophole

**[PRIMARY]** spdx.github.io and the `spdx-3-model` repository, verified 2026-08-30.

> "The AI Profile is designed to provide a standardized way of documenting and sharing information about
> **AI software packages (i.e. systems)**."

> "These artifacts are the tangible outputs of the AI development process, such as **software packages,
> models, and datasets**."

`AIPackage` is `SubclassOf: /Software/Package`. Its **complete** property list: `autonomyType`,
`domain`, `energyConsumption`, `hyperparameter`, `informationAboutApplication`,
`informationAboutTraining`, `limitation`, `metric`, `metricDecisionThreshold`, `modelDataPreprocessing`,
`modelExplainability`, `safetyRiskAssessment`, `standardCompliance`, `typeOfModel`,
`useSensitivePersonalInformation`.

**Every property describes the model. Not one describes anything the model produced.** Even the
tempting `autonomyType` points the other way: *"Indicates whether **the system** can perform a decision
or action without human involvement or guidance."*

### The nuance: SPDX 3 *can* structurally say a software agent originated a file

This is the most interesting result in the standards sweep, and it needs stating carefully.

> **Agent** — "Agent represents anything with the potential to act on a system… This could be a person,
> organization, software agent, etc."
> **Person** — "A Person is an individual human being."
> **SoftwareAgent** — "A SoftwareAgent is **a software program that is given the authority (similar to a
> user's authority) to act on a system.**"

> **originatedBy** — "Identifies from where or whom the Element originally came." — `Range: Agent`
> **createdBy** — "Identifies who or what created the Element…" — `Range: Agent`

The inheritance chain closes: `File → SoftwareArtifact → Core/Artifact`, and `Artifact.originatedBy`
ranges over `Agent`, of which `SoftwareAgent` is a concrete subclass. `Snippet` inherits the same.

**So `File --originatedBy--> SoftwareAgent("Claude Opus 5")` validates today, at file and even snippet
granularity — which is precisely the sub-file granularity in-toto #244 said was missing.**

**⚠️ Qualify this heavily.** It is a capability of the type system, not a modelled concept. No SPDX text
sanctions, names, or explains that use. `SoftwareAgent`'s definition — *"given the authority (similar
to a user's authority) to act on a system"* — reads as CI runners, bots and service accounts; there is
no indication generative authorship was contemplated. **SPDX 3 has no property named `author` at all**
(swept across all 308 model files), and `AnnotationType` has exactly two values, `other` and `review`.
**It is an available hook, not an existing answer.**

## 3.4 CycloneDX: splits manual from automated, and routes automated to a company

**[PRIMARY]** `bom-1.6.schema.json` and `bom-1.7.schema.json` from the CycloneDX specification
repository, verified 2026-08-30. **A 1.7 schema exists.**

> **`authors`** — "The person(s) who created the component. **Authors are common in components created
> through manual processes. Components created through automated means may have `@.manufacturer`
> instead.**"
> **`manufacturer`** — "**The organization that created the component.** Manufacturer is common in
> components created through automated processes."

**This is the closest any standard comes to the distinction this document cares about, and it misses.**
CycloneDX splits manual from automated production and then routes "automated" to an
`organizationalEntity` — a company. **There is no way to name *what* did the automating.**

**ML-BOM is fenced off from code by the schema itself:**

> `modelCard` — "**This object SHOULD be specified for any component of type `machine-learning-model`
> and must not be specified for other component types.**"

**A `modelCard` is legally prohibited from appearing on a `file` or `library` component.**

**Attestations (CDXA) attest the paperwork, not the software:** `declarations` describes *"the
conformance to standards"*; `attestations` *"maps requirements to claims"*. Its `evidence` object does
carry `author` and `reviewer` — *"The author of the evidence"* — which attributes the audit artifact.

**⚠️ New in 1.7 and a genuine near-miss worth flagging:** `citations` — *"A collection of attributions
indicating which entity supplied information for specific fields within the BOM"*, with `attributedTo`
(*"component, service, **tool**, organisational entity, or person"*), `process`, and a JSON Pointer.
**Field-level, tool-granular attribution — structurally exactly the right shape. But its subject is the
BOM's own data.** It answers "which scanner filled in this field", never "who wrote this function."

**AI: silence.** `grep -oiE "artificial intelligence|generative|LLM|AI-generated|coding assistant|copilot"`
over `bom-1.7.schema.json`: **0 matches.**

## 3.5 The verdict to carry to the archetype documents

| | Carries authorship? | Models **AI authorship of source**? | Models **AI systems as artifacts**? |
|---|---|---|---|
| SLSA build track | No — only a *platform* | **No** | No |
| SLSA source track (v1.2) | Yes — account identity, human/robot roles | **No** | No |
| in-toto (vetted) | Only via SLSA/SPDX/CDX predicates | **No** — the gap is a 3-year-old open issue | Partly |
| SPDX 3.0.1 | Yes — `originatedBy` → `Agent` | **No named field.** Structurally expressible via `SoftwareAgent` | **Yes** — that is the AI profile |
| CycloneDX 1.6 / 1.7 | Yes — `authors` (persons) / `manufacturer` (orgs) | **No** | **Yes** — ML-BOM |
| NIST SSDF 800-218 / -218A | No | **No** — 218A covers *"AI model development"* | Securing their development |

**The category error runs through the whole ecosystem.** The entire stack answers *"was this artifact
built from this source by this builder, untampered?"* It does not answer *"who wrote this source, and
did anyone read it?"* — and the one specification reaching toward the source defines its top level as
**two humans agreeing to the change**, i.e. the review this project's further-along archetypes are
built around replacing.

---

# 4. What an auditor or an incident review actually needs

## 4.1 ⚠️ SOC 2's change-management criterion cannot tell review from verification

**[ARCHIVED]** AICPA, *TSP Section 100 — 2017 Trust Services Criteria*, March 2020 revision, retrieved
from the Internet Archive's 2022-09-01 capture of the formerly-public official AICPA URL. **Sourcing
caveat:** the live AICPA download page returns HTTP 200 but no criterion text, with embedded JSON
marking it `"isLocked":"locked"` for `"loggedInRole"` — sign-in gated, not circumvented. **The archived
copy is the March 2020 edition, not the 2022 revised-points-of-focus edition**, and the Wayback
availability API returns the same capture for 2024, 2025 and 2026 probes. Treat the criterion sentence
as stable and the points of focus as *as-of-March-2020*.

> "**CC8.1 Change Management** — The entity authorizes, designs, develops or acquires, configures,
> documents, tests, approves, and implements changes to infrastructure, data, software, and procedures
> to meet its objectives."

Its points of focus include, verbatim:

> "**Authorizes Changes** — **A process is in place** to authorize system changes prior to development."
> "**Documents Changes** — **A process is in place** to document system changes…"
> "**Tracks System Changes** — **A process is in place** to track system changes prior to implementation."
> "**Approves System Changes** — **A process is in place** to approve system changes prior to
> implementation."

**Machine-checked emptiness across the full criteria document:**

| Term | Occurrences |
|---|---|
| `traceab*` | **0** |
| `evidence` | **0** |
| "who performed" / "identity of an individual" in a control context | **0** |

**The criterion demands that a *process exist*. It never demands that the authorizer or approver be
identifiable, or that the reasoning behind a change be recoverable.** CC7.5 does require *"The root
cause of the event is determined"*, and CC7.4 requires understanding *"the method by which the incident
occurred"* — but neither specifies an input record from which that determination must be
reconstructible. Accountability-to-an-individual lives in a different criterion entirely, CC1.5
(*"holds individuals accountable for their internal control responsibilities"*), which is a
governance-structure control disconnected from CC8.1's change record.

**The finding is not that agent tooling fails SOC 2. It is that SOC 2 as written does not detect the
failure.** A control designed around "a process is in place" is satisfiable by a pipeline in which no
human ever saw the reasoning that produced the diff. **This is the clearest instance in the whole
project of the review/verification conflation `CONTEXT.md` warns about: CC8.1 says "approves" without
distinguishing a human reading the change from a check reporting green, so an archetype that has
replaced the first with the second passes the criterion unchanged and produces none of the record an
incident reviewer needs.**

## 4.2 NIST states the requirement in the terms an incident reviewer actually uses

**[PRIMARY]** NIST SP 800-53 Rev. 5, from the NIST-maintained OSCAL catalog (`usnistgov/oscal-content`),
verified 2026-08-30.

> **AU-3 Content of Audit Records** — "Ensure that audit records contain information that establishes
> the following: a. What type of event occurred; b. When the event occurred; c. Where the event
> occurred; d. Source of the event; e. Outcome of the event; and **f. Identity of any individuals,
> subjects, or objects/entities associated with the event.**"

> **AU-2 Event Logging** — "d. **Provide a rationale for why the event types selected for logging are
> deemed to be adequate to support after-the-fact investigations of incidents**"

> **CM-3 Configuration Change Control** — "c. **Document configuration change decisions associated with
> the system;** … e. **Retain records of configuration-controlled changes to the system for
> [Assignment: organization-defined time period]**"

**AU-3(f) is the demand SOC 2 never makes, and AU-2(d) is the sufficiency test.** Note that AU-3(f)
says *"individuals, subjects, or **objects/entities**"* — the wording already accommodates a non-human
actor, which is more than any of the AI-specific standards in §3 manage.

**Recommendation for the archetype documents: frame the auditor's real requirement as AU-3(f) +
CM-3(c)/(e), and treat SOC 2 CC8.1 as a weaker restatement that agent tooling can satisfy vacuously.**

## 4.3 ISO/IEC 27001:2022 — blocked, and not sourced second-hand

Two ISO-owned URLs attempted 2026-08-30: `iso.org/obp/ui/#iso:std:iso-iec:27001:ed-3:v1:en` and
`iso.org/standard/27001`. **Both returned HTTP 403 Forbidden.** Not circumvented; not sourced from a
consultancy summary. **A.8.32, A.8.15 and A.5.28 are unverified. Do not cite ISO clause text or titles
from this document.**

## 4.4 Post-incident review needs an actor slot that a diff cannot fill

**[PRIMARY]** Google, [SRE Book — Postmortem Culture](https://sre.google/sre-book/postmortem-culture/)
and [SRE Workbook](https://sre.google/workbook/postmortem-culture/), verified 2026-08-30.

> "A postmortem is a written record of an incident, its impact, the actions taken to mitigate or resolve
> it, **the root cause(s)**, and the follow-up actions to prevent the incident from recurring."

> "For a postmortem to be truly blameless, it must focus on identifying the contributing causes of the
> incident **without indicting any individual or team** for bad or inappropriate behavior."

with the philosophy resting on the assumption that

> "everyone involved in an incident had good intentions and **did the right thing with the information
> they had**."

The Workbook's template separates **Root Causes** from **Trigger** as distinct required fields, and its
worked trigger reads:

> "When the Cluster Turnup team **manually started another run of the workflow** for `a12bcd34`, this
> action triggered the `admin_server` bug."

**That sentence template has an actor slot: `<actor> did <action>, which activated <latent defect>`.**

**⚠️ The finding here is a conceptual one, and it is easy to get backwards. Blamelessness is not
anonymity.** Google's formulation removes *indictment*, not *identification* — and the assumption that
everyone *"did the right thing with the information they had"* is only checkable if you can recover
**what information they had**. For an agent-authored change, "the information they had" is the session
transcript. **If the transcript is gone, blameless postmortem culture does not degrade gracefully into a
blameless outcome; it degrades into an unreconstructable one.**

**[PRIMARY, vendor practice — PagerDuty sells incident tooling]**
[response.pagerduty.com](https://response.pagerduty.com/after/post_mortem_process/), verified
2026-08-30, shows how reconstruction is actually done:

> "**Go through the history in Slack** to identify the responders and add them to the page"
> "Identify the underlying cause of the incident (**what happened and why did it happen**)"

**The method is archaeological. It presumes a durable, searchable, human-readable interaction log
exists.** For human responders that log is chat. **For an agent it is the session transcript — the
artifact §4.5 shows is least likely to have been kept.**

## 4.5 Agent session transcripts: retained where, how long, exportable?

All rows below are **[PRIMARY, vendor documentation]**, verified 2026-08-30. ⚠️ Every vendor here is
documenting its own product and has a commercial stake; the constraints they disclose run against that
interest, which is why they are worth quoting.

| Tool | Vendor-retained | Locally retained | Customer-exportable | How long |
|---|---|---|---|---|
| **Claude Code** | 30 d commercial; 5 yr consumer opt-in; 5 yr `/feedback`; up to 6 mo survey-shared; ZDR available per-org | **Yes — *"Full conversation transcript: every message, tool call, and tool result"*, plaintext JSONL** | **No documented export.** OTel only, at generation time, gates off by default | 30 d local default (`cleanupPeriodDays`, min 1). `history.jsonl` **kept until deleted** |
| **GitHub Copilot** | Audit log yes; coding-agent session logs yes, period **undocumented** | Local sessions yes (deletable); cloud sessions **archive-only, not deletable** | Audit log **yes** (JSON/CSV, REST + GraphQL). Session logs **no documented export or API** | **180 d** audit; **silent** on session logs |
| **Cursor** | Admin events only — *"We do not log agent responses or generated code content"* | AI line-signatures **on-device only** | Audit log yes (CSV, SIEM/webhook/S3 on request). Agent content: nothing to export | **Not specified on any of four pages checked** |
| **OpenAI Codex** | Yes — Compliance Logs Platform | `codex resume` implies local state; path and retention undocumented | **Yes** — append-only Compliance API, paginated JSONL, official scripts | **30 d**, with explicit "don't rely on it" guidance |
| **Gemini CLI** | Enterprise/Vertex: *"not collected"*. Paid API: *"a limited period of time"* | Not documented | Not documented | **No number for any tier** |
| **Jules** | Not documented | Not documented | Not documented | **Not documented** |

### The quotes that matter

**Claude Code** — the richest record and no way out of it:

> "Claude Code clients store session transcripts locally in plaintext under `~/.claude/projects/` for
> **30 days by default** to enable session resumption. Adjust the period with `cleanupPeriodDays`."

> "`projects/<project>/<session>.jsonl` | **Full conversation transcript: every message, tool call, and
> tool result**"

> "**Transcripts and history are not encrypted at rest. OS file permissions are the only protection.**
> If a tool reads a `.env` file or a command prints a credential, that value is written to
> `projects/<project>/<session>.jsonl`."

**On export: `export` and `transcript` each appear zero times in the slash-commands documentation.** The
CLI's only transcript verbs are destructive or resumptive — `claude project purge` *"Delete all local
Claude Code state for a project: transcripts, task lists, debug logs…"* and `claude rm`. The only
documented egress is OpenTelemetry captured *at generation time*, with `OTEL_LOG_USER_PROMPTS`,
`OTEL_LOG_ASSISTANT_RESPONSES`, `OTEL_LOG_TOOL_DETAILS` and `OTEL_LOG_RAW_API_BODIES` **all disabled by
default**, and spans that *"redact user prompt text, tool input details, and tool content by default."*

**GitHub** — the explicit negative, plus a genuinely useful new field set:

> "The audit log **does not include client session data, such as the prompts a user sends to Copilot
> locally**." · "The audit log retains events for the last **180 days**."

But the agentic audit-log events do carry structured attribution:

> "`actor_is_agent`: Indicates whether the actor is an AI agent"
> "`agent_session_id`: **A unique identifier linking to the specific agent session that generated the
> event**"
> "`user`: The person who initiated the agentic event"

**This is the only field set in the survey that even attempts NIST AU-3(f) for agent actions.** And it
has a hole: **`agent_session_id` is a 180-day pointer aimed at a session store whose retention GitHub
does not publish.** Three surfaces checked, including all nine coding-agent management REST endpoints —
every one is policy and permission management, none returns a session log. **The pointer may well
outlive its target.**

**Cursor** — names the requirement, declines it, hands you a script:

> "**Compliance requires visibility into who did what, when, and why.**"
> "**We do not log agent responses or generated code content.** Instead, we recommend using hooks to log
> prompts and code."
> "**Important:** Be careful logging actual code or prompts. They may contain sensitive information. **Log
> metadata (who, when, what file) rather than content when possible.**"

**OpenAI** — the best export path, aimed at the shortest window:

> "Use the **append-only compliance log stream** for ongoing collection." (with official Bash/PowerShell
> scripts that *"write JSONL to standard output"*)
> "**Compliance Logs Platform records are available for 30 days.**"
> "Schedule continuous collection… **Don't assume the source retention window replaces your
> organization's retention policy.**"

### The one product that got the shape right

**[PRIMARY, vendor documentation]** Cursor, verified 2026-08-30:

> "Cursor keeps a log of the signature of every AI line (Tab or Agent) that is suggested to the user…
> These lines are stored and later compared to the signatures of each line in subsequent git commits…
> **All the AI detection is done on device, and never leaves the user's computer.**"

> "Cursor Blame extends traditional git blame with AI attribution… it retrieves attribution data that
> identifies **which lines came from AI assistance, which models were used, and the conversations that
> produced them**." · "**Hover over AI-attributed lines to see conversation summaries.**"

**This is the only shipped mechanism in the entire corpus that attaches provenance to the code rather
than to a separate log, and links a line to the conversation that produced it — exactly what §5 says is
missing.** Its documented limits are the finding:

> "**Cursor Blame is disabled at the team level by default.**"
> "Diff signatures may be **invalidated if automated code formatting is modifying lines**."
> "**AI Code Tracking has not been implemented for Background Agents, or the Cursor CLI yet.**"
> "The git commit must be scored on the **same machine** as the AI code was authored."

**Line-level provenance exists, it is off by default, it is on-device only, and it is absent from
precisely the further-along-the-spectrum workflows — background agents and CLI — that most need it.
Cite it as proof the record is buildable, not merely as a gap.**

---

# 5. The autonomy axis: where the record breaks

## 5.1 `git blame` was never the mechanism

The brief asked: *at what point does `git blame` stop identifying anyone who read the line?*

**[DIRECT MEASUREMENT]** The answer is **at the first commit**, and the reason is structural rather than
a consequence of delegation.

`git blame --porcelain` emits exactly these identity fields: `author`, `author-mail`, `author-time`,
`author-tz`, `committer`, `committer-mail`, `committer-time`, `committer-tz`, `summary`, `filename`.
**There is no trailer field, and `git blame` has no trailer or co-author option** — `git blame -h`
returns zero matches for either term. In the baseline experiment, three lines contributed by three
distinct `Co-authored-by:` parties all blamed to the single commit **author**.

**So `git blame` reads the author field, and in the dominant agent workflow — a human running Claude
Code or Cursor locally — the human is always in the author field.** Blame has never identified an agent
and never will, regardless of how far along the spectrum a change sits. Squashing degrades blame further
(three distinct commits collapse to one; `-C -C -w` does not recover them), but that is a second-order
loss on a signal that carried no agent provenance to begin with.

**The correct formulation for the archetype documents:** the question is not *when does blame stop
working* but **blame answers a different question than the one governance asks.** Blame answers "which
commit last touched this line." Reconstructing responsibility requires "who read this line, and what did
they know" — and there is exactly one mechanism in this entire corpus that answers it (Cursor Blame,
§4.5), off by default and absent from background agents.

**`git shortlog --group=trailer:co-authored-by` is the one built-in tool that does surface co-authors**,
and it is a reporting command, not an attribution one — and §2.2 shows it returns nothing after a local
squash.

## 5.2 Provenance must be per-change, and almost nothing records it that way

Ticket #4 established, and ticket #6 reinforced, that **position on the spectrum is a per-change
property, not a per-team property**. Provenance must therefore be per-change too. Measured against that
requirement:

| Mechanism | Granularity | Per-change? |
|---|---|---|
| `Co-authored-by:` / `Assisted-by:` trailer | **Per commit** | **Yes** — the only widely-deployed per-change mechanism, and it is unverified free text |
| `Claude-Session:` trailer | **Per commit, pointing at a session** | **Yes**, and uniquely it points at the *reasoning*. Also free text, also erased by §2.5 |
| Committer email (what `agent-approval-check` reads) | Per commit | Yes — but only for agents that commit under their own identity (§2.6) |
| Commit signature | Per commit | Yes — about **bytes and keys**, not authorship (§1.3) |
| Cursor diff signatures / Cursor Blame | **Per line** | **Yes, and the finest granularity found** — off by default, on-device, not for background agents |
| GitHub `agent_session_id` audit event | Per agent action | Yes — 180 d, pointing at a store with no published retention |
| SLSA / in-toto / SBOM | Per artifact or per build | **No** — an SBOM describes a release, not a change |
| OTel metrics (`lines_of_code.count` etc.) | Per session, aggregate | **No** — counts, not attributions |
| Vendor analytics dashboards | Per user / per team | **No** — this is provenance for management reporting, not for incident triage |

**Two things fall out of that table.**

1. **The per-change mechanisms are exactly the unverified ones.** Everything cryptographic is
   per-artifact or per-build; everything per-change is free text. The autonomy spectrum needs per-change
   provenance, and per-change is precisely the layer where nothing is attested.

2. **The further along the spectrum a change sits, the more the record depends on the layer that survives
   worst.** At the near end, a developer typing with completions produces commits whose author field is
   honestly theirs and whose provenance question barely arises. Further along, more of the change came
   from a prompt and less from a hand on the expression — so the interesting record moves from the author
   field (durable, signed, carried through squash) into a trailer (free text, erasable by a dropdown) and
   then into a session transcript (30 days, no export). **Autonomy and durability of the record move in
   opposite directions.**

This is the same shape as ticket #5's copyrightability finding, arrived at from the audit side rather
than the licensing side. The U.S. Copyright Office's test — *"insufficient human control over the
expressive elements"*, assessed *"on a case-by-case basis"* — needs a per-change record of how the change
was produced. **That record is the `Claude-Session:` transcript, and it is the single artifact this
document finds to be simultaneously the most valuable, the most fragile in git, and the shortest-lived
in the vendor's store.**

---

# 6. Method, limits and disclosures

## 6.1 What the measurements can and cannot support

- **The 61-of-62 survival figure is drawn from a sample selected through commit search for agent
  trailers on default branches — i.e. from survivors.** It establishes that survival is the normal
  outcome under default settings and locates the loss case precisely. **It cannot estimate a population
  loss rate, and must not be quoted as one.**
- **The local git experiments are deterministic and reproducible**, and are the strongest evidence in
  this document. They are also *only* about git's behaviour; GitHub's squash does something different
  and better, which is exactly why both had to be measured.
- **GitHub's squash co-author aggregation is undocumented.** Finding 1 rests on the artifact. A
  behaviour with no documented guarantee is one a platform may change silently, and a governance
  document should say so rather than assert a guarantee that does not exist.
- **Merge-commit merges are counted as surviving** because the agent's commits remain reachable as
  parents. That is correct for the repository, and it inherits §2.5's caveat about what a clone carries.

## 6.2 ⚠️ The GitHub commit-search counts are unstable — quote them as orders of magnitude

**[PLATFORM DATA]** Four identical queries for `"Co-Authored-By: Claude"`, issued minutes apart in one
session on 2026-08-30, returned:

| Attempt | `total_count` |
|---|---|
| 1 | 13,684,044 |
| 2 | 6,384,245 |
| 3 | 9,796,098 |
| 4 | 14,889,191 |

— a **2.3× spread on an unchanged query**. `"Co-authored-by: Copilot"` behaved the same way: **1,135,820**
then **1,476,561**.

GitHub's search `total_count` is an estimate over an index, not a count. **Cite these as "on the order
of 10⁷" and "on the order of 10⁶" respectively, never as figures, and never as a ratio between the
two.** They are sufficient to establish that trailer-based agent attribution is a mass phenomenon, which
is all §2.6 needs from them. **A previous version of this analysis nearly quoted attempt 1 as a fact;
the instability was only visible because the query was repeated. Repeat any search-API count before
citing it.**

## 6.3 Ageing

Everything in §4.5 is vendor documentation with no publication date, and every retention number in it is
a policy the vendor can change unilaterally. Ticket #6 found that `docs.claude.com/en/docs/claude-code/*`
had already 301'd to `code.claude.com/docs/en/*` mid-session; this strand found three more URL
reorganisations (§6.5). **Re-verify every retention figure before relying on one, and treat §4.5 as a
snapshot dated 2026-08-30.**

## 6.4 Corrections to prior tickets

- **Ticket #5, finding 2 — "SLSA grants robots a perpetual two-person-review exception."** Confirmed in
  substance, corrected in four particulars (§3.1): it is `two-party-review` by requirement ID; it is
  **Level 4 only**; **an organization** grants it, not SLSA; and *Trusted Robot* is gated by *"cannot be
  unilaterally influenced"*, with Dependabot as the named example. **Do not cite it as evidence SLSA has
  considered AI agents — SLSA contains zero occurrences of AI, LLM, agent or generative across every
  spec file in both release branches and the draft.**
- **Ticket #5, §1.5 — "SLSA Source Track (working draft)."** The Source Track is **released v1.2**, not a
  draft; the release-branch file is byte-identical to the draft.
- **Ticket #5, §1.5 — "no standards body has an authorship predicate."** Still true for *AI* authorship,
  but **SPDX 3.0.1's `SoftwareAgent` + `originatedBy` makes a file- and snippet-level machine-authorship
  statement structurally expressible today** (§3.3). That is a real narrowing of the emptiness finding,
  even though no spec text endorses the use.
- **Ticket #5, §1.4 — Cursor retention "not specified."** Re-checked across four current pages and
  **confirmed still true**, and Cursor now states affirmatively that it *"does not log agent responses or
  generated code content."*
- **Ticket #6 — `agent-approval-check` as a provenance-gated mechanism.** Confirmed and narrowed
  further: it gates on **committer email**, never on a trailer, so it does not fire for the
  human-commits-locally workflow (§2.6); and its status is SHA-scoped, so its evidence does not enter the
  branch it gates.

## 6.5 Tooling note

**WebSearch was not used at any point in this strand**, preserving the budget ticket #5 exhausted. Every
source was reached by direct fetch of a canonical URL, with URL discovery via vendor-published indexes
(`cursor.com/docs/llms.txt`, `learn.chatgpt.com/llms.txt`), GitHub's own docs search API, and the GitHub
REST/GraphQL API. **Where this document says "could not find", read "not found via direct-URL fetching
and API enumeration, with keyword search unused."**

---

# Sources

**Git**
- `git-interpret-trailers` — https://git-scm.com/docs/git-interpret-trailers (2026-08-30)
- `git-commit` (`--signoff`, `-S`, `--trailer`, `--amend`) — https://git-scm.com/docs/git-commit (2026-08-30)
- `gitfaq` (why no `commit.signoff`) — https://git-scm.com/docs/gitfaq (2026-08-30)
- `gitformat-signature` — https://git-scm.com/docs/signature-format (2026-08-30)
- `git-filter-branch` (signature preservation impossible) — https://git-scm.com/docs/git-filter-branch (2026-08-30)
- `git-rebase`, `git-cherry-pick`, `git-config` (`gpg.format`, `user.signingKey`, `commit.gpgSign`, `gpg.ssh.allowedSignersFile`) — git-scm.com (2026-08-30)
- `Documentation/SubmittingPatches` — https://raw.githubusercontent.com/git/git/master/Documentation/SubmittingPatches (2026-08-30)

**DCO and kernel**
- Developer Certificate of Origin 1.1 — https://developercertificate.org/ (2026-08-30)
- `submitting-patches.rst` — https://docs.kernel.org/process/submitting-patches.html (2026-08-30)
- `coding-assistants.rst` — https://docs.kernel.org/process/coding-assistants.html (2026-08-30)
- `generated-content.rst` — https://docs.kernel.org/process/generated-content.html (2026-08-30)

**GitHub**
- About commit signature verification — https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification (2026-08-30)
- Displaying verification statuses (vigilant mode) — same section (2026-08-30)
- `rebase_and_merge_verification.md` — https://github.com/github/docs/blob/main/data/reusables/pull_requests/rebase_and_merge_verification.md (2026-08-30)
- Creating a commit with multiple authors — https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors (2026-08-30)
- About pull request merges — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/about-pull-request-merges (2026-08-30)
- Configuring commit squashing — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/configuring-commit-squashing-for-pull-requests (2026-08-30)
- REST API — Repositories (`squash_merge_commit_message` enum) — https://docs.github.com/en/rest/repos/repos (2026-08-30)
- Commit signoff policy — https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-commit-signoff-policy-for-your-repository (2026-08-30)
- Configuring web commit signing (GHES) — https://docs.github.com/en/admin/configuring-settings/configuring-user-applications-for-your-enterprise/configuring-web-commit-signing (2026-08-30)
- Agentic audit log events — https://docs.github.com/en/copilot/reference/enterprise-administrators/agentic-audit-log-events (2026-08-30)
- Reviewing audit logs for Copilot — https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-enterprise/review-audit-logs (2026-08-30)
- Track Copilot sessions — https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/track-copilot-sessions (2026-08-30)

**Sigstore**
- Sigstore overview — https://docs.sigstore.dev/ (2026-08-30)
- gitsign README — https://raw.githubusercontent.com/sigstore/gitsign/main/README.md (2026-08-30)
- gitsign committer verification — https://raw.githubusercontent.com/sigstore/gitsign/main/docs/committer-verification.md (2026-08-30)

**Standards**
- SLSA source requirements v1.2 — https://slsa.dev/spec/draft/source-requirements and `releases/v1.2` (byte-identical) (2026-08-30)
- SLSA provenance v1.1 — https://raw.githubusercontent.com/slsa-framework/slsa/releases/v1.1/spec/provenance.md (2026-08-30)
- in-toto Statement v1 — https://raw.githubusercontent.com/in-toto/attestation/main/spec/v1/statement.md (2026-08-30)
- in-toto vetted predicates — https://raw.githubusercontent.com/in-toto/attestation/main/spec/predicates/README.md (2026-08-30)
- in-toto issue #244, *Attestation for AI-assisted code*, opened 2023-06-03, open (2026-08-30)
- SPDX 3.0.1 AI profile — https://spdx.github.io/spdx-spec/v3.0.1/model/AI/AI/ and `/Classes/AIPackage/` (2026-08-30)
- SPDX 3.0.1 Core `Agent` / `SoftwareAgent` / `originatedBy` — https://spdx.github.io/spdx-spec/v3.0.1/model/Core/ (2026-08-30)
- CycloneDX `bom-1.6.schema.json` and `bom-1.7.schema.json` — https://github.com/CycloneDX/specification (2026-08-30)
- CycloneDX ML-BOM and Attestations capability pages — https://cyclonedx.org/capabilities/ (2026-08-30)
- NIST SP 800-53 Rev. 5 (AU-2, AU-3, AU-12, CM-3) via OSCAL catalog — https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json (2026-08-30)
- NIST SP 800-218A abstract — https://csrc.nist.gov/pubs/sp/800/218/a/final (2026-08-30)
- AICPA *TSP Section 100 — 2017 Trust Services Criteria*, March 2020 revision — **[ARCHIVED]** http://web.archive.org/web/20220901034236/https://us.aicpa.org/content/dam/aicpa/interestareas/frc/assuranceadvisoryservices/downloadabledocuments/trust-services-criteria.pdf

**Incident review**
- Google SRE Book, Postmortem Culture — https://sre.google/sre-book/postmortem-culture/ (2026-08-30)
- Google SRE Workbook, Postmortem Culture — https://sre.google/workbook/postmortem-culture/ (2026-08-30)
- PagerDuty postmortem process *(vendor practice)* — https://response.pagerduty.com/after/post_mortem_process/ (2026-08-30)

**Vendor documentation (first-party, commercial stake)**
- Claude Code data usage — https://code.claude.com/docs/en/data-usage (2026-08-30)
- Claude Code directory / monitoring / CLI reference / slash commands — https://code.claude.com/docs/en/ (2026-08-30)
- Cursor compliance and monitoring — https://cursor.com/docs/enterprise/compliance-and-monitoring (2026-08-30)
- Cursor analytics, admin API, Cursor Blame — https://cursor.com/docs/ (2026-08-30)
- OpenAI Compliance API — https://learn.chatgpt.com/docs/enterprise/compliance-api.md (2026-08-30)
- OpenAI cloud security / retention — https://learn.chatgpt.com/docs/enterprise/chatgpt-work-cloud-security.md (2026-08-30)
- Gemini CLI ToS and privacy — https://google-gemini.github.io/gemini-cli/docs/tos-privacy.html (2026-08-30)

**Source code and live artifacts**
- `anthropics/claude-code-action`, `agent-approval-check/` — `action.yml`, `README.md`, `agent_approval_check.py` (1,828 lines), read 2026-08-30
- Merged pull requests and resulting commits in `anthropics/claude-code-action`, `fol2/roguecardv2`, `iorate/ublacklist`, `Yukoval-Dakia/the-learning-project`, `time-yide/yide-acompanha`, and Copilot coding-agent PRs across 30 repositories — GitHub REST API, 2026-08-30
- Local git experiments, git 2.55.0.windows.3, 2026-08-30

**Prior tickets**
- [`verification-observability.md`](./verification-observability.md) (#5)
- [`tooling-landscape.md`](./tooling-landscape.md) (#6)
- [`practitioner-exemplars.md`](./practitioner-exemplars.md) (#4, per-change property)

---

# Confidence and gaps

**High confidence.**
- Git's trailer and signature behaviour under squash, rebase, amend and cherry-pick. Deterministic,
  reproducible, cross-checked three ways.
- GitHub's squash co-author aggregation **as observed** — multiple independent artifacts, and the
  message shape reproduces the parse behaviour exactly.
- `squash_merge_commit_message` enum semantics — GitHub's own API reference.
- What the DCO text does and does not say. It is 300 words and the absence is checkable.
- What SLSA, in-toto, SPDX and CycloneDX do and do not model. Multiple greps over full spec corpora.
- Claude Code's absence of a transcript export path — `export` and `transcript` return zero hits in the
  slash-commands documentation.

**Medium confidence.**
- **That GitHub will keep aggregating co-authors on squash.** Undocumented behaviour; no guarantee to
  point at.
- **Retention figures in §4.5.** Vendor documentation with no publication dates, unilaterally changeable.
- **The claim that trailer-only attribution is the dominant population.** Well-supported directionally by
  the commit-search magnitudes and by how the tools are used, but the search counts are unstable (§6.2)
  and I have no measurement of the split.

**Low confidence / open.**
- **How often the loss case actually occurs.** I could not read `squash_merge_commit_message` on any
  repository without admin scope, so the population distribution of that setting is unknown. **This is
  the single most valuable follow-up: a survey of that setting across repositories with agent-authored
  commits would convert finding 2 from a mechanism into a magnitude.**
- **Whether OpenAI compliance records contain prompt or agent-reasoning content.** The contract lives
  behind an authenticated SPA.
- **ISO/IEC 27001 clause text.** Blocked. Unverified.
- **Whether any organisation has actually been asked, in a SOC 2 or ISO audit, to produce evidence of who
  authored an agent-written change.** No primary source found either way. §4.1 establishes that the
  criterion does not require it; it does not establish what auditors do in practice.

**What would change the picture.**
- GitHub documenting — and thereby committing to — its squash co-author aggregation.
- Any of SPDX, CycloneDX or in-toto adopting a source-authorship predicate. SPDX 3's `SoftwareAgent`
  needs no schema change, only a profile that says the words.
- A vendor shipping transcript export as a first-class, retention-configurable feature rather than an
  opt-in telemetry pipeline with four redaction gates.
- `agent-approval-check` — or anything like it — learning to read the commit message.

---

# Blocked or unavailable sources

**No security control, paywall, auth wall, rate limit or robots policy was circumvented.** Itemised:

| Source | Attempted | Outcome | Handling |
|---|---|---|---|
| ISO/IEC 27001:2022 OBP | `iso.org/obp/ui/#iso:std:iso-iec:27001:ed-3:v1:en` | **HTTP 403** | Not circumvented. **A.8.32 / A.8.15 / A.5.28 unverified — not cited** |
| ISO/IEC 27001 standard page | `iso.org/standard/27001` | **HTTP 403** | Not circumvented |
| AICPA TSC, 2022 points-of-focus edition | `aicpa-cima.com/resources/download/…` | HTTP 200, no text; `"isLocked":"locked"`, `"role":"loggedInRole"` | Not circumvented. Substituted the **archived March 2020 official PDF**, version difference flagged at point of use (§4.1) |
| A post-2022 archived TSC capture | Wayback availability API, probes at 2024/2025/2026 | All resolve to the same 2022-09-01 capture | No later archived copy exists |
| Wayback CDX index for AICPA | `web.archive.org/cdx/search/cdx` | **HTTP 504** | Worked around via the availability API |
| OpenAI Admin API reference (event coverage, retention contract) | `chatgpt.com/public/admin/api-reference` | Authenticated SPA | **Whether OpenAI compliance records contain prompt or reasoning content is unverified.** Both public pages defer to this reference |
| GitHub Copilot coding-agent **session-log retention** | `track-copilot-sessions`; all 9 coding-agent management REST endpoints; GitHub docs search | Pages load; retention and export simply absent | **Emptiness finding, three surfaces** |
| GitHub Copilot audit-log page | `…/manage-for-organization/review-audit-logs` | **HTTP 404** — reorganised | Live page located under `manage-for-enterprise` |
| Cursor analytics / privacy pages | `cursor.com/docs/account/teams/analytics`, `/docs/account/privacy` | **Both 404** — reorganised | Current pages located via `cursor.com/docs/llms.txt` |
| OpenAI Codex security page | `developers.openai.com/codex/security` | **308** → `learn.chatgpt.com/docs/security`, which has no retention content | Retention found on `chatgpt-work-cloud-security.md` |
| Jules retention / privacy docs | `jules.google/docs/privacy`, `developers.google.com/jules/docs` | **Both 404**; main docs page has no logging/retention/export content | **Emptiness finding — complete documentation void** |
| Gemini CLI retention period | `google-gemini.github.io/gemini-cli/docs/tos-privacy.html` | Loads; *"a limited period of time"*, **no number for any tier** | **Emptiness finding** |
| Copilot coding-agent commit attribution | `docs.github.com/…/coding-agent/about-coding-agent` | Loads; **no statement about git author/committer identity, co-author trailers, or signing** | Established empirically instead (§2.6) |
| GitHub squash co-author aggregation | *About pull request merges*; *Creating a commit with multiple authors*; *Configuring commit squashing* | All load; **none documents the behaviour** | **Documentation gap.** Established by artifact measurement (§2.3) |
| `Documentation/signature-format.adoc` | raw.githubusercontent | **404** — the file is `gitformat-signature.adoc` | Fetched under the correct name |
| SRE Workbook timeline entry format | `sre.google/workbook/postmortem-culture/` | Elided by Google: *"[The link to our Timeline log has been elided for book publication]"* | Field names quoted; entry formatting not quotable |
| SLSA `releases/v1.1/spec/source-requirements.md` | raw.githubusercontent | **404** — legitimately; Source and Build tracks were not separate files in v1.1 | Not an access failure |
| NIST SP 800-218 / 218A | `csrc.nist.gov/pubs/sp/800/218/final` | Landing pages and abstracts only, per budget | **Weaker negative than the others — flag it if relied on** |
| Repository merge settings on repos without push access | `GET /repos/{o}/{r}` for 12 popular repos | All merge-setting fields return `null` — the fields require admin scope | **Could not survey the population distribution of `squash_merge_commit_message`.** This is the single biggest gap in §2.3 |
| `mcp__github`, `greptile`, `figma-desktop`, `discord`, `firebase` MCP servers | — | Failed to connect at session start (auth/connection errors) | Not needed; `gh` CLI and public HTTPS were sufficient |

