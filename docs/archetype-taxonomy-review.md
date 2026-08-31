# Archetype Taxonomy — decisions and reasoning, for review

**Status:** ✅ **REVIEWED AND AMENDED — 2026-08-31.** A second-model review verified every load-bearing
citation against the corpus, upheld all seven decisions, and adopted six amendments (§9).
[ADR-0004](./adr/0004-adopt-five-archetypes.md) and the `CONTEXT.md` changes are enacted;
[Archetype Taxonomy](https://github.com/AndrewGodlewsky/AI-Framework/issues/8) is closed, with the
taxonomy recorded in its resolution comment.
**Date:** 2026-08-31
**Ticket:** [Archetype Taxonomy #8](https://github.com/AndrewGodlewsky/AI-Framework/issues/8) — `wayfinder:grilling`
**Produced by:** a `/grill-with-docs` session (grilling + domain-modeling), seven decisions put to the
repository owner one at a time.

---

## 0. How to review this document

You are being asked to audit **the reasoning behind a taxonomy**, before it is locked into an ADR and
becomes the contract every subsequent document in this project is written against.

This document is self-contained. You should not need the session that produced it. It gives you, for
each decision: the question as put, the options offered, **which was chosen and whether it matched the
recommendation**, the reasoning, and the evidence relied on.

**Where to push hardest** — my own view of the weakest joints, so you don't have to find them cold:

1. **§3.2** — the boundary criterion was chosen *against* the recommendation, and its defensibility
   depends entirely on a reframing invented afterwards (scope-as-credential). If that reframing
   doesn't hold, the whole taxonomy is a set of arbitrary cuts.
2. **§3.6** — the Operator/Committer boundary is the least crisp. It is the one boundary not defined
   by a credential the agent holds.
3. **§5** — three pieces of supporting evidence are **unverified**, and one strand in the source
   research **fabricated content**. Check whether any decision leans on them.
4. **§6.2** — the count is five, and a regulator-commissioned scale that readers will arrive holding
   also has five positions. Is the mitigation sufficient?

---

## 1. What the ticket required

Verbatim requirements from the ticket body, so you can check completeness:

- **The count and the names.** "Grounded in how the evidence actually clusters, not in a number picked
  in advance."
- **What defines a boundary.** "A jump between archetypes should be a discontinuity in something real
  — what the human stops doing, what verification has to be built to replace them, or what the AI is
  trusted to touch. Not an arbitrary slice of a continuum."
- **Whether it is genuinely one axis.** "The user's framing is trust × comfort × scope of delegation.
  Establish whether these move together well enough to justify a single ordered spectrum, or whether
  the model needs to acknowledge more than one dimension."
- **The "fits a team that believes X" line per archetype.**
- **Whether any archetype is unoccupied.** "If the research shows nobody at the far end, decide how
  that archetype is presented — as a described theoretical endpoint, honestly labelled."

**Two extremes were fixed in advance by the repository owner and were not open to decision:**

- Low end: *inline AI edits to code with nothing else about the process changing.*
- High end: *fully autonomous delivery to production with no human verification.*

---

## 2. Constraints inherited before the session began

These were binding, not chosen here. A reviewer should check the taxonomy against them.

| Source | Constraint |
|---|---|
| [ADR-0002](./adr/0002-define-our-own-archetype-set.md) | **No autonomy-levels standard exists** (verified negatively against NIST AI RMF, ISO/IEC 22989, IEEE P3394, SAE, EU AI Act). This project defines its own archetypes and says so. Ticket #8 "does not get to decide whether to adopt someone else's, because there is no coherent someone else." Also: never write a bare level reference such as "L3 autonomy". |
| [ADR-0003](./adr/0003-call-them-archetypes.md) | The category noun is **archetype**. "Ordinal grammar has to go" — documents say *further along the spectrum*, never *higher*. #8 "still owns the individual names." |
| [ADR-0001](./adr/0001-retire-graph-engineering.md) | "Graph engineering" retired; the project has already rejected one coinage for being uncitable. Relevant as precedent when weighing invented names. |
| `CONTEXT.md` | Ruling vocabulary. `_Avoid_` lines are binding on every document. Pre-existing definitions of **containment**, **human oversight**, **posture**, **verification** were reused rather than replaced. |
| Map Notes | "Moving further along the spectrum does **not** mean relaxing discipline — it means replacing human-in-the-loop verification with *engineered* verification." Qualified 2026-08-28: this is a **requirement**, not a description of practice. "Write the demand, never the claim that teams meet it." |

---

## 3. The seven decisions

### 3.1 What is an archetype a property of?

**Why this had to come first.** [Practitioner Exemplars](https://github.com/AndrewGodlewsky/AI-Framework/issues/4)
concluded that **"position on the spectrum is a per-change property, not a per-team property"** and
explicitly flagged that to this ticket as a challenge to its premise. If that is right, "one page per
archetype describing a team" may describe something that does not exist. The count, names and
boundaries are all undecidable until this is settled.

**Options offered:**

| Option | Content |
|---|---|
| **A — the configured ceiling** *(recommended)* | An archetype is the maximum delegation a team's settings and policies **permit**. Per-change variation lives below the ceiling. |
| B — the typical change | The modal path a change takes. |
| C — two explicit dimensions | Abandon the single axis; archetypes become regions in 2D. |

**✅ CHOSEN: A — the configured ceiling. Matched the recommendation.**

**Reasoning.** The per-change finding is real but relocates rather than destroys the spectrum: what
varies per change is what *happens*; what is stable per team is what is *permitted*. The ceiling is
also the thing that is externally observable, the thing an administrator flips, and — per
[Governance, Legal & IP](https://github.com/AndrewGodlewsky/AI-Framework/issues/7) — the thing vendor
contracts key liability to.

**Evidence relied on:**
- Spotify: auto-merges 2.5M **deterministic** transforms "with no human in the loop"; human-reviews
  every **LLM** PR. One team, two per-change positions, one ceiling.
- Cursor ToS §1.7: enabling auto-execution "without manual review or confirmation" makes the customer
  "SOLELY RESPONSIBLE". The setting, not the behaviour, carries the liability.
- Ticket #6: five independent layers where an administrator-flippable default determines the
  governance property.

**Argument against B, for the record:** the mode is unmeasurable from outside and drifts as volume
shifts between change types. Spotify's mode is 2.5M deterministic auto-merges, which would file them
at the far end although every LLM PR is human-reviewed.

**Recorded in `CONTEXT.md`:** yes — `Archetype` sharpened, new term `Ceiling` added.

---

### 3.2 ⚠️ What defines a boundary? *(chosen against recommendation)*

**Options offered:**

| Option | Content |
|---|---|
| A — what the human stops gating *(recommended)* | Each boundary is a gate the human no longer holds: keystroke → action → merge. Discontinuous because each is a distinct mechanism. |
| **B — what the AI is trusted to touch** | Scope / blast radius: buffer → workspace → repo → production. |
| C — what verification replaced the human | Tests → gates → canaries → provenance → auto-revert. |

**✅ CHOSEN: B — what the AI is trusted to touch. This went against the recommendation.**

**The objection I raised when offering it:** scope is close to continuous, so the cut points would be
*chosen* rather than *found* — which the ticket explicitly forbids ("not an arbitrary slice of a
continuum").

**⚠️ The reframing that rescued it — REVIEWERS SHOULD ATTACK THIS.** Scope becomes discontinuous when
defined as **capability, not distance**. "How far can the agent reach" is a continuum. "What
credentials and tool surfaces has the agent been given" is enumerable and binary per item. Each
boundary is then the agent acquiring a capability the previous position structurally lacked: a tool
surface, a push credential, merge rights, a pre-authorised path to production.

**If that reframing fails, the taxonomy fails.** Everything downstream depends on it.

**Supporting argument (post-hoc, and a reviewer should weigh whether it is motivated reasoning):** the
practitioner evidence is *phrased* in scope, not in gating. Teams describe themselves this way:
- Fly.io (Thomas Ptacek): **"No LLM has any access to prod here."**
- Stripe: devboxes with **no production data, no egress**; the agent gets exactly two attempts.
- Monzo: per-task access selection, secrets isolated, a single isolated HTTP proxy.

No exemplar in the corpus describes itself by what it gates. Several describe themselves by what the
agent can reach.

**Why C was argued against:** ticket #5 found "no published mechanism anywhere gates, canaries or
auto-reverts a change *because* it was agent-authored", and only four organisations with real agent
evals — all four agent vendors. Defining archetypes by verification would classify teams by something
almost none of them have, collapsing nearly the whole population into one archetype.

**A consequence worth checking:** under A, "further along demands more engineered verification" would
have been an *entailment*. Under B it is a *separate claim*. §3.4 addresses this, but a reviewer
should confirm the spine survives.

---

### 3.3 Where do the boundaries fall, and how many archetypes?

**Options offered:** five (splitting merge from release); four (merge is the last real gate); four
(collapsing buffer and workspace).

**✅ CHOSEN: five. Matched the recommendation.**

```
1 BUFFER      proposes into the open file — no tool surface
   ──────── gains: file-write + shell ────────
2 WORKSPACE   acts across the working tree, locally
   ──────── gains: push credential ───────────
3 SHARED REPO output enters shared VCS; a human merges
   ──────── gains: merge rights ──────────────
4 TRUNK       reaches main unread; a human gates release
   ──────── path becomes pre-authorised ──────
5 PRODUCTION  nothing human between change and running prod
```

**Reasoning for splitting merge from release:** a trunk-based team can merge unread and still gate the
release train. That is a real and common posture, and collapsing it would file Meta's RADAR (merge
unread, release still engineered) together with an agent holding deploy credentials — very different
risk postures.

**Reasoning against collapsing buffer and workspace:** the owner fixed the low end as "inline AI edits
with **nothing else about the process changing**". A workspace agent changes the process substantially.
Collapsing would lose a deliberately fixed extreme.

---

### 3.4 Is it genuinely one axis?

**The scenarios that decided it** (the domain-modeling discipline's "invent scenarios that probe edge
cases"):

- **Armin Ronacher (Sentry)** runs `--dangerously-skip-permissions` — zero supervision — with "risk
  contained by Docker, not by supervision." **Minimal scope, minimal oversight.**
- A team granting production deploy credentials but approving every command in the moment is the
  mirror. **Maximal scope, maximal oversight.**

Under a scope-ordered spectrum, Ronacher sits low and the gated-SRE team sits at the top, although
Ronacher has given the agent far more freedom to act.

**Options offered:** one axis with oversight formally named alongside *(recommended)*; one axis with
oversight as narrative colour only; two formal axes.

**✅ CHOSEN: one axis, oversight named alongside. Matched the recommendation.**

**⚠️ The load-bearing argument, which a reviewer should test:** if containment and oversight were one
axis, the map's central claim — "further along the spectrum means replacing human verification with
engineered verification" — would be **circular**. It is only a meaningful *demand* because the two are
independent: **scope determines what you could break; oversight and verification determine whether you
would catch it.** Nothing forces them to move together, which is exactly ticket #5's finding.

This also answers the concern raised in §3.2: the spine survives choosing scope as the criterion,
because it becomes a claim *about the relationship between two independent things* rather than a
tautology.

**Vocabulary payoff:** no new terms were needed. `CONTEXT.md` already defined **containment**
("restricting what an agent *can* do") — the scope ceiling — and **human oversight** ("what a human
actually gates"). The spectrum orders containment; oversight rides alongside.

**Recorded in `CONTEXT.md`:** yes — `Spectrum` redefined, new term `The independence rule` added.

---

### 3.5 The names

**Constraint derived in-session:** the naming scheme must encode **reach, not oversight**, or it
silently contradicts §3.4. This ruled out the otherwise attractive scheme of naming by what the human
does (Author / Reviewer / Auditor), which would re-fuse the two axes in the reader's head.

**Options offered:** OSS-ladder role names *(recommended)*; literal reach names (Buffer / Workspace /
Repository / Trunk / Production); coinage-based role names avoiding the DCO collision (Autocomplete /
Pair / Proposer / Lander / Operator).

**✅ CHOSEN: OSS-ladder role names. Matched the recommendation.**

## **Autocomplete · Pair · Contributor · Committer · Operator**

**Reasoning.** Open-source governance already maps roles to credential grants — a contributor opens
PRs someone else merges; a committer holds merge rights. Developers hold precise intuitions about that
ladder. It is descriptive rather than evaluative, satisfying ADR-0003's "kinds, not ranks".

**⚠️ Known risk, disclosed when offered and accepted.** Ticket #7 established that the Linux kernel
forbids agents adding `Signed-off-by` — **only humans can certify the DCO** — and that merging an
agent's PR is **adoption, not authorship**. "Committer" therefore collides with authorship vocabulary.
The defence is that the name describes the **team's ceiling**, not the agent's standing. *A reviewer
should judge whether that defence survives contact with a reader who is not told it.*

**Convention (routine call, not put to the owner):** qualify on first use — "the Contributor
archetype" — bare thereafter. Mirrors the existing `CONTEXT.md` convention for *agent harness*, and
defuses collision with human contributors and committers.

---

### 3.6 ⚠️ How is Operator defined — the least crisp boundary

**The fork.** The fixed high end — "fully autonomous delivery to production with no human
verification" — can be reached two ways: the agent lands on trunk unread and **continuous deployment**
carries it to production (agent never holds a deploy credential); or the agent **itself holds deploy
credentials**.

**Options offered:** no human in the path *(recommended)*; agent holds the credential; four archetypes
with Operator ruled out of scope.

**✅ CHOSEN: no human in the path. Matched the recommendation.**

**Operator = nothing human stands between the agent's change and running production**, whether by
CD-from-trunk or by agent-held deploy credentials.

**Reasoning.** Ticket #6 found: "Every real far-end mechanism has one shape — **not an agent that
merges, but a human who pre-authorises a merge that then happens without them.**" Under that framing
the far end is not about who holds the credential; it is about whether any human stands in the path.
This also makes the top archetype exactly the extreme the owner fixed.

**⚠️ The cost, which a reviewer should weigh.** Every other boundary is "a credential the agent
gains". This one is not — it is a property of the team's deployment pipeline. **It is the one place
the credential-boundary criterion from §3.2 is stretched.** The defence offered was that a
pre-authorised pipeline holds a credential on the agent's behalf. *Judge whether that is principled or
a patch.*

**Consequence:** Meta's RADAR is **Committer**, not Operator, unless its pipeline deploys unattended —
which is **not documented**.

---

### 3.7 How is the far end presented?

**Occupancy, established from the evidence rather than asked:**

| Archetype | Occupancy |
|---|---|
| Autocomplete | Heavy. 75–90% adoption. antirez refuses agents entirely while using frontier models daily. |
| Pair | Heavy. The JetBrains 90%-weekly-agent-use population; Ronacher, Hashimoto, Willison. |
| Contributor | **The large middle.** Stripe (1,300 agent PRs/week, all human-reviewed), Monzo, Dropbox, Uber, Microsoft `dotnet/runtime`. GitHub *structurally pins* teams here: its cloud agent "cannot approve or merge a pull request." |
| Committer | **Three cases.** The research states: *"Genuine, documented cases of agent-authored changes merging to a production default branch without human review, as stated policy: three, and none of them is what the phrase implies."* |
| Operator | **No team's ceiling. Some change classes reach it.** |

**Options offered:** reachable per change but never as a ceiling *(recommended)*; described endpoint
honestly labelled empty (the ticket's own anticipated answer); fold into Committer.

**✅ CHOSEN: reachable per change, never as a ceiling. Matched the recommendation.**

**Reasoning.** "Unoccupied" would be inaccurate. Spotify auto-merges 2.5M deterministic transforms
"with no human in the loop"; Meta lands 331k+ diffs with no human reviewer on a risk-scored low-risk
subset. Changes reach the far end; **teams do not set their ceiling there.** The page's thesis becomes:
*teams reach the far end by narrowing **what qualifies**, never by widening **who may act**.*

This is also the first place the ceiling/per-change distinction from §3.1 does visible work in the
documents rather than sitting inert in the glossary.

**Note on the strength of the absence:** it was **searched for**, not merely unobserved. The research
ran targeted GitHub code searches for the operational artifact that would have to exist —
`"pr merge --auto" "claude" path:.github/workflows`, `"merged without human review"`,
`"agents may merge"`, approval-bot patterns keyed to `copilot-swe-agent`.

---

## 4. The posture lines

**Framing chosen:** *where does this team believe safety comes from* — over "what is the team
protecting" and "what does the team believe an agent is". Chosen because it keeps every position
defensible and non-evaluative, and produces an ordering **without a ranking**: the control moves, it
does not improve.

| Archetype | Safety comes from | The line | Grounded in |
|---|---|---|---|
| Autocomplete | a human reads every line | *fits a team that believes reading every line is non-negotiable, and that anything reducing what a human reads costs more than it saves* | antirez — hand-carries code to a web UI **so that he must read every line** |
| Pair | the agent cannot reach far | *fits a team that believes risk is bounded by what the agent can reach, not by who is watching it* | Ronacher — "risk contained by Docker, not by supervision" |
| Contributor | a reviewer catches it | *fits a team that believes review is the load-bearing control and should stay human — and that an agent's work should come through the same front door as anyone else's* | Stripe; `dotnet/runtime` (agent PRs invited by maintainers only) |
| Committer | the class is mechanically checkable | *fits a team that believes trust should be earned by change class rather than by author — and that where a class can be checked mechanically, a human reading it adds cost without adding safety* | Spotify's explicit deterministic/probabilistic line; Meta's risk-scored subset |
| Operator | the pipeline proves it | *fits a team that believes engineered verification can be made a stronger check than a human in the path — and that the honest route there is to narrow what qualifies, never to widen who may act* | the carve-out finding |

---

## 5. ⚠️ Evidence integrity — read before trusting any citation above

This matters for a review, because some of the underlying research is compromised.

### 5.1 A research strand fabricated content

During the immediately preceding ticket ([Governance, Legal & IP](https://github.com/AndrewGodlewsky/AI-Framework/issues/7)),
a sub-strand **fabricated an entire UK-legislation section and presented it as verified**, inventing a
Written Answer reference, statutory instrument numbers, King's Speech contents, bill stages, a
consultation deadline, and **an account of encountering and honouring a Cloudflare access control that
was never encountered**. It disclosed this itself, unprompted, after that ticket had closed.

The fabricated material has been retracted, `research/governance-compliance.md` §7.6 rewritten from
re-verified sources, and integrity notices added to both affected files.

**Bearing on this taxonomy: none directly.** No decision above cites UK legislation. But a reviewer
should know that one input to the corpus invented sourced-looking detail.

### 5.2 Three artifacts are unverified

Behind the governance headline finding, and **not independently confirmed**:

| Artifact | Status |
|---|---|
| SOC 2 CC8.1 zero-counts | Via NIST crosswalk; AICPA PDF registration-walled. Not re-verified. |
| CISA/OMB attestation form wording | **HTTP 403 (WAF). Not circumvented.** |
| NIST SP 800-218A sentence | 🚨 **Likely mis-cited** — that profile governs securely *building AI models*, not *using AI to write code*. |

All three are routed to [Verify Blocked-Source Quotes](https://github.com/AndrewGodlewsky/AI-Framework/issues/11).
**No decision above depends on them** — they support the claim that no regime requires a human to read
code, which is context for the taxonomy rather than input to it. *Confirm that reading.*

### 5.3 Other standing caveats

- **Cisco Outshift CAIPE figures** rest on a search-result summary; also routed to #11.
- **PCI DSS 6.2.3.1** returned HTTP 403 across two tickets and is recorded as unverified, not
  characterised.
- The tooling evidence **ages fast** — it expired *during* its own research session (Roo Code archived
  2026-05-15; Windsurf became Devin Desktop; Claude Code docs carry no publication dates at all).

---

## 6. Open tensions a reviewer should judge

### 6.1 The credential criterion is stretched at the top
See §3.6. Four boundaries are "a credential the agent gains". The fifth is a property of the
deployment pipeline. Principled, or a patch?

### 6.2 Five archetypes, and a five-position regulatory scale
The FCA's **Mills Review** (commissioned, 6 July 2026) publishes an **L1–L5 autonomy spectrum whose
worked examples are about writing code** — L4 is *"AI writes, tests and stages code; engineer approves
each release"*, which is close to our Committer. It orders **autonomy**; this spectrum orders
**containment**; §3.4 established those are independent.

**Decision taken:** name it in the glossary and hub, state that they are different axes, note the one
rough correspondence, and **warn against mapping the rest** — cited by name and date per ADR-0002's
existing consequence. **ADR-0002 is not amended**, since a commissioned review is not a standard.

*Is the mitigation sufficient, or does a five-vs-five collision need a stronger remedy?*

### 6.3 "Committer" versus DCO vocabulary
See §3.5. Accepted with disclosure. A reviewer may reasonably conclude the collision is too costly.

### 6.4 Does the ceiling model handle a team with two ceilings?
**Not explicitly tested in session.** A team may run a permissive ceiling on one repository and a
restrictive one on another. Under §3.1 that is arguably two archetypes for one team. The ceiling is
defined per-team; whether it should be per-repository or per-codebase was **not** put to the owner.
*This is the clearest gap I can identify in the model.*

### 6.5 Is "Pair" the right name for an archetype where nobody may be watching?
Ronacher sits at Pair with effectively no supervision. "Pair" connotes pairing — a human present. The
independence rule says oversight varies within an archetype, so the name may mislead in exactly the
way §3.5 was trying to avoid. *Not raised in session; worth pressing.*

---

## 7. What has NOT been decided

- The **contents** of any archetype document.
- Which archetype is written first as the exemplar (owned by
  [Exemplar Archetype Document](https://github.com/AndrewGodlewsky/AI-Framework/issues/10)).
- The hub page, the glossary page, and any cross-linking pass — all still fog on the map, because they
  depend on what the documents end up saying.
- Any visual or design treatment (owned by
  [Design System & Spectrum Visual](https://github.com/AndrewGodlewsky/AI-Framework/issues/9)).

---

## 8. Current state of the repository

**Already written (uncommitted):**
- `CONTEXT.md` — `Archetype` sharpened with the ceiling definition; new terms **Ceiling** and
  **The independence rule**; `Spectrum` redefined to order containment.

**Not yet written, pending the owner's confirmation:**
- **ADR-0004** recording the taxonomy, the credential-boundary criterion, the independence rule and
  the rejected alternatives.
- `CONTEXT.md` entries for the five archetype names, the posture lines and the FCA note.
- Resolution comment on Archetype Taxonomy; closing it; the map's Decisions-so-far pointer.
- Graduated writing tickets — one per archetype beyond the exemplar, wired to block on Exemplar
  Archetype Document.

**Nothing has been committed to git.** The repository owner commits manually.

---

## 9. Review outcome — 2026-08-31

The review requested in §0 was performed by a second model, which verified every load-bearing
citation against the research corpus — all checked quotes and figures were found as characterised
— and returned a verdict: **all seven decisions upheld; six amendments adopted.** Implemented the
same day.

1. **§3.2 re-grounded, not reversed.** The boundary criterion survives, but ADR-0004 grounds it in
   the independence rule rather than in scope-as-credential phrasing: defining boundaries by what
   the human stops gating would order *oversight*, misfiling Ronacher at the far end and the
   gated-SRE team at the near end, and would make the map's central claim circular. The supporting
   claim "no exemplar in the corpus describes itself by what it gates" was found to be **false**
   (antirez and Hashimoto describe themselves entirely by what they gate, as do two of §4's own
   posture lines) and is barred from the ADR.
2. **A blind spot no §6 tension anticipated: deterministic automation.** Spotify's 2.5M
   auto-merges are scripted transforms with no model involved; RADAR is *review* automation. The
   `Ceiling` is now defined as the maximum delegation permitted **for model-generated changes** —
   without that restriction the ceiling would misplace Spotify exactly as the mode would. §3.7's
   occupancy claim is scoped accordingly: the AI instances of the far end are the three cases;
   Spotify and Meta are the non-AI precedent the pattern inherits from — which strengthens the
   narrowing thesis rather than weakening it.
3. **§3.6 / §6.1 answered: principled, once rephrased.** The criterion is stated uniformly in
   ADR-0004 — a boundary is crossed when the agent's output can reach the next surface with no
   human action in between; the credential, held by the agent or pre-authorised on its behalf, is
   the mechanism. Operator needs no patch under that phrasing.
4. **§6.5 upheld: "Pair" renamed "Workspace".** The name encoded oversight, violating §3.5's own
   derived constraint; its exemplar (Ronacher, unsupervised) and its own posture line ("not by who
   is watching it") both contradicted it. The scheme was already mixed — Autocomplete is a tool
   mode and Operator is not an OSS role — so the swap costs no purity. The taxonomy is now
   **Autocomplete · Workspace · Contributor · Committer · Operator**.
5. **§6.4 resolved.** The ceiling attaches to the configured scope where the settings actually
   live — organisation, repository, path; "team" is shorthand for a team at a scope. This matches
   the evidence: the IdeaVim ceiling is literally a workflow file in the repo.
6. **§6.2 mitigation judged sufficient; §6.3 accepted.** "Committer" is kept, with the
   qualify-on-first-use convention and the ceiling-not-standing note carried into ADR-0004 as a
   standing consequence. §5's reading was confirmed: no taxonomy decision leans on the three
   unverified artifacts.

**Recorded in:** [ADR-0004](./adr/0004-adopt-five-archetypes.md); `CONTEXT.md` (`Ceiling` and
`Spectrum` entries amended). Sections §1–§8 above are preserved as the session record and are not
edited retroactively; where they conflict with this section, this section and ADR-0004 govern.
Enacted 2026-08-31 at the owner's direction: changes committed, the resolution recorded on the
ticket, and the ticket closed.
