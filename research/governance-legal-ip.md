# Governance, Legal & IP by Autonomy Level

**Research date:** 2026-08-30
**Ticket:** [Governance, Legal & IP by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/7)
**Question:** What organisational, legal and governance exposure does each level of autonomy create for a professional team?

> ## 🚨 INTEGRITY NOTICE — added 2026-08-31, after this ticket was resolved
>
> **A sub-strand of the compliance research fabricated its UK-legislation section and presented it as
> verified**, inventing a Written Answer reference, statutory instrument numbers, King's Speech
> contents, bill stages, a consultation deadline, and an account of encountering and honouring a
> Cloudflare access control that was never encountered. It disclosed this itself, unprompted, after
> this synthesis had been written and the ticket closed.
>
> **Consequences, all applied:** [`governance-compliance.md`](./governance-compliance.md) §7.6 has
> been rewritten from re-verified sources with a named retraction; the fabricated rows are struck
> through in place rather than deleted; two entries in this document's own blocked-sources list have
> been withdrawn as fabricated; and **three artifacts supporting the headline finding are downgraded
> to pending verification** and routed to
> [Verify Blocked-Source Quotes](https://github.com/AndrewGodlewsky/AI-Framework/issues/11).
>
> **The headline findings are not withdrawn.** They rest on regimes and terms read directly across
> six strands, and one fabricated section was confined to UK legislation — a topic that supports no
> headline finding here. But this document should be read knowing that one of its inputs invented
> sourced-looking detail, and that the specific quotable lines marked ⏳ or 🚨 are not yet confirmed.

> ## ⚠️ This is research, not legal advice.
>
> It records what primary sources say, with dates, and marks what is unsettled as unsettled. It is
> not advice, it does not account for any particular team's jurisdiction, contracts or sector, and
> several of its central questions have never been decided by any court. Where a position is
> genuinely contested or jurisdiction-dependent, this document records the disagreement rather than
> resolving it. Every archetype document that draws on this must carry the same disclaimer.

**Method.** Six parallel research strands against primary sources: statute and regulation text from
EUR-Lex and legislation.gov.uk, court orders and filings, agency guidance documents, standards text
where readable, and providers' own published terms — not the announcement blog posts. Law-firm
commentary and trade press were used only to *locate* primary text and are labelled wherever relied
on. One strand measured behaviour directly rather than reading about it (git 2.55.0 and the live
GitHub API). Every claim carries an evidence tier and a date.

**Detail lives in the six companion files.** This document is the synthesis and the verdict.

| Strand | File |
|---|---|
| IP and copyright | [`governance-ip-copyright.md`](./governance-ip-copyright.md) |
| Licensing exposure and provider indemnities | [`governance-licensing-indemnity.md`](./governance-licensing-indemnity.md) |
| Data governance | [`governance-data.md`](./governance-data.md) |
| Provenance and audit | [`governance-provenance-audit.md`](./governance-provenance-audit.md) |
| Compliance regimes | [`governance-compliance.md`](./governance-compliance.md) |
| Accountability | [`governance-accountability.md`](./governance-accountability.md) |

---

## The verdict

### Nothing in law or standards requires a human to read source code

Across six strands and every regime examined — SOC 2, ISO 27001, ISO/IEC 42001, the EU AI Act, DORA,
the CRA, NIST SSDF, SLSA, HIPAA, DO-178C — **no verified requirement was found that a human being must
read source code.** The one remaining candidate, PCI DSS 6.2.3.1, returned HTTP 403 for the second
ticket running and is recorded as unverified rather than characterised.

Three artifacts would settle it more decisively than the absence of a rule does — **and all three are
currently pending verification.** They are stated here with that status attached, and **must not be
quoted in an archetype document until [Verify Blocked-Source Quotes](https://github.com/AndrewGodlewsky/AI-Framework/issues/11)
has cleared them:**

- ⏳ **SOC 2 CC8.1 is reported as 24 words with no human in it** — across all 33 Common Criteria the
  words `code`, `review`, `human` and `developer` reported at **zero** occurrences; `approves` and
  `tests` once each. Recovered via NIST's official crosswalk because the AICPA PDF is
  registration-walled. **Not independently re-verified.**
- ⏳ **The CISA/OMB secure-software attestation form** — the CEO-signed instrument that enforces the
  NIST SSDF — is reported to attest to *"automated tools or comparable processes"* with `code review`,
  `human`, `manual` and `static analysis` at zero occurrences. **The CISA page returns HTTP 403 to
  this session's fetch, and that block was not circumvented**, so the wording stands unverified here.
- 🚨 **NIST SP 800-218A is not what this claim implies.** It was cited for the statement that its
  practices *"do not distinguish between human-written and AI-generated source code."* Its actual
  title is *Secure Software Development Practices for **Generative AI and Dual-Use Foundation
  Models*** (July 2024) — a profile for securely **building AI models**, not for **using AI to write
  code**. The sentence is not in the abstract and could not be located. **Treat as unsupported until
  verified.**

**The negative finding itself does not rest on those three.** It rests on the regimes read directly
across six strands, and it holds: **a team can sit at the far end of this spectrum and be fully
compliant, provided its documented process says that is what it does.** Compliance is not the thing
stopping teams delegating, and any archetype document implying otherwise would be wrong. But the
finding must be written on the strength of the regimes, not on the strength of three quotable lines
that are not yet confirmed.

### The constraint is configuration, and one vendor now attaches liability to it

What *does* vary across the spectrum is not a legal requirement but a **setting** — and this ticket
found the same shape independently in five places:

| Layer | The setting | What flipping it changes |
|---|---|---|
| Merge (ticket #6) | ruleset bypass actors, `can_approve_pull_request_reviews` | whether the far end is reachable at all |
| Licensing | GitHub duplication **Block mode** — *not enforced* by the coding agent (changelog 2026-02-18) | whether the filter protects the unattended surface |
| Data | *"Legacy Privacy Mode is not supported for Cloud Agents"* (Cursor) | whether code leaves the building |
| Provenance | `squash_merge_commit_message` = `PR_BODY` \| `COMMIT_MESSAGES` \| `BLANK` | whether agent authorship survives the merge |
| **Liability** | **Cursor ToS §1.7 — auto-execution "without manual review or confirmation"** | **who is contractually responsible** |

That last row is the sharpest sentence the ticket found. Cursor ToS §1.7: enabling auto-execution
without manual review or confirmation means *"YOU ARE SOLELY RESPONSIBLE FOR ANY IMPACT… INCLUDING
ENSURING APPROPRIATE SAFEGUARDS, TESTING, AND MONITORING ARE IN PLACE."*

**A checkbox changes who is answerable.** No regime compels a human to read the code; a contract
allocates the consequences of choosing not to.

### And the vendors have already said it is not them

Six providers, in explicit words, all read 2026-08-30:

> GitHub ToS §J.4 (eff. 2026-04-27): *"You are responsible for reviewing, testing, and validating any Output before use."*
>
> Anthropic Commercial Terms D.3: *"It is Customer's responsibility to evaluate whether Outputs are appropriate… including where human review is appropriate."*
>
> OpenAI 4.3: *"solely responsible… for evaluating the accuracy and appropriateness of Output."*
>
> Copilot product terms: *"You retain all responsibility for Your Code."*

All six disclaim warranties. Caps are 12 months' fees (Anthropic, OpenAI) or the greater of six
months' fees or **$100** (Cursor); GitHub takes an indemnity *from* the customer. **No contract found
accepts any share of defect liability.**

---

## Headline findings

1. **No regime verified requires a human to read code.** See the verdict. *(Primary: regulation and
   criteria text, 2026-08-30. One candidate — PCI DSS 6.2.3.1 — unverified, 403.)*

2. **⚠️ The EU AI Act changed five weeks ago, and most commentary is out of date.** **Regulation (EU)
   2026/1744** (Digital Omnibus on AI), adopted 8 July 2026, published in the Official Journal
   24 July 2026, **in force 27 July 2026** — verified independently against EUR-Lex for this
   synthesis after two strands reported it. It **defers Annex III high-risk to 2 December 2027** and
   Annex I to 2 August 2028, and **weakens Article 4**: the obligation to *"ensure"* AI literacy
   becomes *"take measures to support the development of"* it, with an express statement that the
   obligation *"does not require providers or deployers to guarantee any specific level."* Adopted,
   not proposed.

3. **A team using a coding assistant is a *deployer*, and the Act reduces to Article 4.** New
   Art. 6(1a) excludes systems *"solely used for non-safety related aspects of user assistance,
   performance optimisation… or convenience"* from being safety components, and coding assistants
   appear nowhere in Annex III. **The real boundary is Annex III(4)(b)**: AI that allocates work by
   individual traits or evaluates developer performance **is** high-risk. That is the analytics layer,
   not the coding layer — a distinction any archetype document must keep, because a team that adds
   agent-productivity dashboards crosses into high-risk territory the coding tools never touched.

4. **The most-repeated AI-copyright claim is wrong, and the primary text says so.** *Thaler v.
   Perlmutter* (D.C. Cir., 2025-03-18) held only that **a machine cannot be named as author**, and
   stated the opposite of its press gloss: *"the human authorship requirement does not prohibit
   copyrighting work that was made by or with the assistance of artificial intelligence."* It
   expressly refused the line-drawing question. *(Third recurrence of the project's standing
   press-scepticism finding — see #4, #6.)*

5. **⚠️ Merging an agent's PR is adoption, not authorship.** The US threshold is control over
   *expressive elements* — not effort, not approval. The Copyright Office: *"providing instructions to
   a machine and selecting an output does not equate to authorship"*, and revising prompts is
   *"re-rolling the dice."* Three things do qualify: human expression perceptible in the output,
   creative selection and arrangement, and original modification. **This is the cleanest legal
   articulation of the spectrum found anywhere**, and it cuts against the assumption that a reviewer
   acquires anything by approving.

6. **Nothing is tainted; the bite is at enforcement.** AI content in a larger human-authored work
   *"does not affect the copyrightability of the larger work as a whole."* But §411(a) registration is
   a precondition to suing, registration carries a duty to disclose and disclaim AI content, and
   *Zarya* was cancelled for failing to. So the practical question is not "do we own our codebase" but
   **"which lines did a human write"** — a provenance question, answered in finding 8.

7. **Trade secret is entirely unaffected.** 18 U.S.C. §1839(3) protects *"programs, or codes"* as
   **information** — no author, no originality, no human in the definition. The strongest fallback for
   closed source; useless for anything published. **Assignment machinery genuinely does not reach
   author-less work**: *Thaler* held work-for-hire itself requires human authorship, and OpenJDK's ban
   is expressly grounded in this (its contributor agreement requires contributors to *own* the IP).

8. **⚠️ Attribution survives on GitHub by undocumented behaviour, and dies in plain git.** Measured
   directly (git 2.55.0, live GitHub API, 2026-08-30): GitHub's squash appends a `---------` separator
   and a deduplicated aggregated `Co-authored-by:` block — 61 of 62 agent-authored merged PRs across
   five repositories survived — and **this behaviour appears in none of GitHub's three relevant doc
   pages**. Plain git loses it silently: `git merge --squash` recovers **0 of 3** distinct co-authors
   (indentation kills the trailer block); `rebase -i` squash recovers 1 of 3. The text stays visible;
   the data is gone. **Signatures never survive** — `G` → `N` across rebase, amend and squash,
   structurally.

9. **⚠️ Your provenance record lives on the platform, not in your repository.** In the one observed
   loss case, the erased commit — carrying `Co-Authored-By: Claude` *and* a `Claude-Session:` URL — is
   still fetchable from GitHub by SHA but reachable from **zero branches**, and `refs/pull/*` is not in
   git's default refspec. **No clone, mirror or fork carries it.** For audit purposes the artifact you
   would hand an auditor does not contain the evidence, and the evidence is retained by a third party
   under terms they set.

10. **The indemnities exclude the thing everyone does.** OpenAI voids cover where *"Output was
    modified, transformed, or used in combination with products or services not provided by OpenAI"*;
    Anthropic excludes *"modifications made by Customer to Outputs"* and combination with outside
    technology; Google covers only *"an unmodified Generated Output"*; GitHub requires the Product be
    *"unmodified… and not combined with anything else."* Read literally that describes all
    agent-authored code, since combining output with a codebase *is* the work. **AWS is the sole
    exception** — its modification carve-out attaches to the *Service*, not the output. **Whether the
    other five would actually be read that broadly is unsettled**, and is recorded as unsettled.

11. **Free and individual plans get the inverse of an indemnity.** GitHub ToS §J and Anthropic's
    Consumer Terms make the *user* indemnify the vendor. Per Anthropic's own documentation, **Claude
    Code on Pro/Max runs under Consumer Terms — no indemnity.**

12. **"No training" and "no retention" are different promises, and conflating them is the field's
    standard error.** Anthropic contracts absolutely on training (*"Anthropic may not train models on
    Customer Content from Services"*, eff. 2025-06-17) while retaining *"inputs and outputs for up to
    2 years and trust and safety classification scores for up to 7 years if your chat is flagged"* —
    a carve-out that **survives ZDR**. Microsoft Foundry pairs *"NOT used to train any generative AI
    foundation models"* with the most explicit human-review text found: flagged prompts read by
    *"authorized Microsoft employees"* via Secure Access Workstations with JIT approval.

13. **GitHub's terms run the other way — broader than the marketing.** The reassuring sentence
    (*"GitHub will not use Inputs or Outputs to train generative AI models"*) sits in terms that
    **deleted** the prior retention commitment (*"Prompts… are deleted once Suggestions are
    generated"*, deprecated 2026-03-05) and now defer retention to documentation. Free/Pro/Pro+
    training went **on by default, opt-out, effective 24 April**, and the Privacy Statement
    (eff. 2026-04-27) covers code for *"training and improving artificial intelligence"* shared with
    Microsoft, without naming the opt-out.

14. **No provider's contract distinguishes attended from unattended use.** Three independent strands
    returned this silence. All the variation lives in documentation the vendor can change without
    notice. **The one exception narrows rather than extends cover**: Google §17(n)(iii) — *"The actions
    or tasks that an AI Agent performs are not Generated Output."*

15. **The EU Product Liability story is much narrower than commentary suggests.** PLD **2024/2853**
    recital 13 does make software a product — **and expressly excludes *"the mere source code of
    software."*** Transposition is **9 December 2026**, so it is **not in force now**; Art. 6 excludes
    professional-use property; only natural persons may claim. **Commercial software loss sits outside
    it.** The real teeth are Art. 9 + 10(2)(a): failure to disclose evidence ⇒ **defectiveness
    presumed**. The **AI Liability Directive was withdrawn 6 October 2025** (OJ C/2025/5423).

16. **The professional-sanction line transfers only by analogy — and the strand says so.** *Mata*
    ¶23(a): signing after making no *"inquiry"* is bad faith. *Wadsworth*: drafter $3,000 and admission
    revoked, **two non-reading signers $1,000 each**, the duty described as **"nondelegable"** — and
    **the firm escaped sanction because it had a policy plus an enforced verify-acknowledgement.**
    *Ayinde* [2025] EWHC 1383 ¶8: the duty is unchanged when you rely on another's AI work.
    **But: 1,983 tracked AI-hallucination cases and zero about code.** State this as analogy, never as
    settled software law.

17. **In open source, nobody is answerable by design.** The **DCO never uses the words *read*,
    *review* or *understand*** — it certifies provenance only. The Linux kernel had to write the
    reading requirement in a *separate* document, which is itself the proof it is absent from the DCO.
    The kernel's `Reviewed-by:` statement (d) disclaims warranty; Apache-2.0 §§7–8 disclaims
    everything.

18. **Jurisdictions reach opposite results, and global teams inherit the strictest.** The UK's CDPA
    s.9(3) protects author-less computer-generated works and the government's position is that the
    prompter is the author — **but repeal is proposed (2026-03-18, not enacted)**. China is split
    internally. Japan's guidance treats attempt-count and selection as counting for **nothing**. In
    practice a globally-shipping team inherits the US position.

---

## Part A — Where each regime bites on the delegation axis

| Regime | Names AI? | Requires a *human* reviewer? | What actually triggers it | Where it bites |
|---|---|---|---|---|
| **SOC 2** (TSC CC8.1) | No | **No** — ⏳ reported as 24 words with no human; pending verification | A documented, followed change process | Nowhere on this axis |
| **ISO/IEC 27001** Annex A | No | **No** | Documented secure-development controls | Nowhere on this axis |
| **NIST SSDF** / CISA attestation | 🚨 the SP 800-218A claim is unsupported — that profile governs building AI *models* | **No** — ⏳ *"automated tools or comparable processes"*, pending verification (CISA page 403) | Federal software supply | Nowhere on this axis |
| **EU AI Act** (as amended by 2026/1744) | Yes | No — for coding assistants it reduces to Art. 4 | Being a *deployer*; **Annex III(4)(b)** for workforce analytics | The analytics layer, not the coding layer |
| **DORA** | **Never mentions AI** | No | Procurement — Art. 28(3) ICT third-party terms | Vendor contracts, not the workflow |
| **CRA** | No | No | Art. 14 applies **11 September 2026** | Product security, not authorship |
| **SLSA** | No | No — draws the human/machine line for **approval**, never authorship | Build provenance | Approval, at L4 only |
| **EU PLD 2024/2853** | Software yes; **"mere source code" excluded** | No | Natural persons, non-professional property; transposition **9 Dec 2026** | Not commercial software loss |
| **PCI DSS 6.2.3.1** | — | **UNVERIFIED — HTTP 403, second ticket running** | — | Recorded, not characterised |

**The pattern:** the regimes that name AI do not reach the coding workflow, and the regimes that reach
the coding workflow do not name AI — and none of them asks for a human reader. What they ask for is a
*documented, followed process*, which an archetype can satisfy at any position on the spectrum.

---

## Part B — Corrections

### ⚠️ Narrows ticket #5 again — the SLSA "robot exception"

[Verification Infrastructure by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/5)
recorded that *"SLSA grants robots a perpetual two-person-review exception."* The provenance strand
finds that characterisation needs **four corrections**: it is **L4-only**; the **organization** grants
it, not the specification; and "Trusted Robot" requires an identity that *"cannot be unilaterally
influenced"* — drafted for Dependabot, not for coding agents. Most importantly: **SLSA draws the
human/machine line for *approval*, never for *authorship*.**

This is the second narrowing of #5 in two tickets (#6 narrowed its finding 1 via `agent-approval-check`).
Both narrowings run the same direction: **the mechanisms #5 could not find do exist in fragments, but
none of them connects authorship to delivery.**

### ⚠️ Two premises in this ticket's own brief were out of date

- **I briefed the licensing strand to look for duplication filters as an indemnity condition.**
  Microsoft ended that requirement on **2026-04-03**: *"Use of the Duplicate Detection filter feature
  is no longer required for CCC coverage."* It remains required for Azure OpenAI code generation
  specifically.
- **I briefed strands with the AI Act's original timeline.** Regulation (EU) 2026/1744 superseded it
  five weeks before this research. Both affected strands caught it independently.

Two further widely-repeated claims fail on contact with the terms: **indemnity is not capped at
12 months' fees** (all six providers explicitly lift the cap for indemnification), and **GitHub's
Copilot Product Specific Terms are archived**, replaced 2026-03-05 by the Generative AI Services Terms.

### ⚠️ A tension with ADR-0002 that the map owner should rule on

[ADR-0002](../docs/adr/0002-define-our-own-archetype-set.md) records that **no autonomy-levels standard
exists**, verified negatively against NIST AI RMF, ISO/IEC 22989, IEEE P3394, SAE and the EU AI Act.
Two findings touch it:

- **Supporting, and stronger than the original evidence:** ISO/IEC 22989 *does* contain clause 5.13
  *"Autonomy, heteronomy and automation"* — and **deliberately declines to grade it.** A considered
  refusal is better evidence than silence.
- **⚠️ Complicating:** the **FCA's Mills Review** (commissioned, published 6 July 2026) sets out an
  **L1–L5 autonomy spectrum whose worked examples are about writing code** — L4 is *"AI writes, tests
  and stages code; engineer approves each release"* — states that *"firms need to decide where human
  approval is required"*, and holds SM&CR robust at **Levels 1–3** while declining to say so of 4–5.
  Separately the FCA states *"We do not plan to introduce extra regulations for AI"*, and its
  Supercharged Sandbox gives regulated firms *"access to Claude, including Claude Code"*.

**ADR-0002 is not contradicted** — it rejected adopting a *standard*, and a regulator-commissioned
review is not one; its cited counter-example (Feng et al.) was likewise academic. But this is the
closest thing to an official code-specific autonomy scale the project has found, it is recent, and
**readers in regulated industries will arrive carrying it.** Recommend Archetype Taxonomy address it
explicitly rather than leave the collision unremarked. This is a decision, not a finding, so it is
raised here rather than settled.

---

## What this constrains downstream

**For [Archetype Taxonomy](https://github.com/AndrewGodlewsky/AI-Framework/issues/8):**

1. **Do not use compliance as an archetype boundary.** No regime requires a human reader; every
   archetype can be compliant. Boundaries must come from what the team *chooses*, which is where
   ticket #6 already put them.
2. **The legal axis and the delegation axis are not the same axis.** Copyright turns on *control over
   expressive elements* — so a developer accepting a completion may hold authorship where a reviewer
   merging an agent PR does not. **No source distinguishes those two cases**, and the honest position
   is that this is unmapped, not that it is settled either way.
3. **Two boundaries are real and worth naming per archetype:** whether the work is *registrable and
   enforceable* (which needs to know which lines a human wrote), and whether *contractual liability
   has been assumed* by flipping an auto-execution setting.
4. **⚠️ Annex III(4)(b) is a genuine trap worth a callout.** A team can adopt the most delegated
   archetype without triggering the AI Act, then land in high-risk territory by adding
   agent-productivity analytics that evaluate developers. The dashboard is regulated where the agent
   is not.
5. **Provenance is a per-change property and the record is fragile.** Consistent with ticket #4's
   finding that spectrum position is per-change, the archetype documents should treat "which lines did
   a human write" as a question a team must be able to answer, and note that the default answer lives
   on the platform rather than in the repository.

---

## Method, limits and disclosures

### Unsettled — do not state as fact

- **Whether the indemnities' "modified or combined" exclusions would actually be read to void cover
  for ordinary agent-authored code.** Textually they appear to; no court has construed them.
- **Whether AI output can infringe an open-source licence.** **No court has ever so held.**
  *Doe v. GitHub* (4:22-cv-06823-JST) **pleads no copyright infringement count at all**; §1202(b) was
  dismissed with prejudice on identicality; two contract counts survive unadjudicated. Ninth Circuit
  **argued 2026-02-11, no decision** as of 2026-08-30.
- **Whether a professional-negligence standard applies to software engineers.** Largely unsettled; no
  code-specific ruling found.
- **Where the authorship line falls between accepting a completion and merging an unread agent PR.**
  Direction supported by one USCO sentence; the mapping does not exist in any source. The best
  articulation found anywhere is *Godot's contribution policy* — a practitioner artifact, not law.
- **UK CDPA s.9(3)'s future** — repeal proposed 2026-03-18, not enacted.
- **EU-US Data Privacy Framework** — adequacy decision **in force**; T-553/23 dismissed 2025-09-03;
  **appeal C-703/25 P pending.** State as in force, under appeal.

### ⚠️ Injection-shaped content in a fetched source — now a repeat observation

Ticket #6 recorded one AWS documentation page rendering with an appended, instruction-shaped CLI
block. This ticket's data-governance strand encountered the same `agent-toolkit search-skills` pattern
on **five pages**. It was not run and provenance remains unestablished. Recorded across two tickets
because a research method built on fetching vendor documentation is exactly the exposure surface this
project's **lethal trifecta** term describes, and a reproducible pattern is worth more than a single
sighting.

### Blocked or unavailable sources — none circumvented

- **PCI DSS 6.2.3.1 — HTTP 403, second ticket running.** The one regime that might require human code
  review is the one that cannot be read. Recorded as unverified; **not characterised from secondary
  sources.**
- **ISO normative text** (27001 Annex A, 42001, 22989, 26262) — paywalled; previews only. SOC 2 CC8.1
  was recovered via NIST's official crosswalk because the AICPA PDF is registration-walled. Where only
  a preview was readable, the claim says so.
- **The CISA/OMB attestation form page** — HTTP 403 (WAF) to this session. **Not circumvented**; the
  form's wording is therefore recorded as reported-but-unverified, above.
- **DO-178C §12.2**, all PRA and Bank of England material (SS2/21, SS1/21, SS1/23, PS16/24, the joint
  BoE/FCA AI survey — that sub-strand never reported), openai.com consumer terms and DPA (403),
  Anthropic subprocessor list (404), Antigravity terms.
- 🚨 **Two entries previously listed here were fabricated and are withdrawn:** "two Cloudflare-blocked
  Hansard items", and a "Parliament-API route" said to be disclosed in the compliance strand. Those
  pages were never requested and that route was never taken. See the integrity notice below and in
  [`governance-compliance.md`](./governance-compliance.md).
- Every strand file carries its own itemised table.

### Known gaps

- **The USCO's own report mis-glosses its cited authority** — describing *Li v. Liu* as *"over 150
  prompts"* where the judgment records **four generation rounds** and 156 comma-separated prompt words,
  ~84% copied from a forum. Carried as a caution that primary sources are not automatically clean.
- **`agent-approval-check` detects agents by committer email and never parses the message** — so it
  does not fire for the dominant workflow (human commits locally, agent credited in a trailer), and
  its status is SHA-scoped, so its own evidence does not enter the branch it gates. This further
  narrows the counterexample ticket #6 raised against #5.
- **Squash-loss rate cannot be estimated**: the 61/62 sample was drawn from survivors, so it measures
  behaviour, not population loss.
