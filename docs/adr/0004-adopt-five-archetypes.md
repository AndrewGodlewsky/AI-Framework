# Adopt the five-archetype taxonomy: Autocomplete, Workspace, Contributor, Committer, Operator

Archetype Taxonomy (issue #8) resolved the root decision of the map: how many archetypes the
spectrum has, what each is called, and what makes a boundary real. The taxonomy was produced in a
grilling session against the research corpus and then independently reviewed against that corpus
([the review record](../archetype-taxonomy-review.md), which carries the full reasoning and the
review's amendments). This ADR records the amended result — the contract every subsequent document
is written against.

## The five archetypes

| Archetype | The agent's output can reach | Gained at this boundary | Fits a team that believes |
|---|---|---|---|
| **Autocomplete** | the open file; a human accepts every edit | — (the fixed low extreme) | reading every line is non-negotiable, and anything reducing what a human reads costs more than it saves |
| **Workspace** | the working tree, locally | file-write and shell tool surfaces | risk is bounded by what the agent can reach, not by who is watching it |
| **Contributor** | the shared repository; a human merges | a push credential | review is the load-bearing control and should stay human — and an agent's work should come through the same front door as anyone else's |
| **Committer** | trunk, unread; a human gates release | merge rights | trust should be earned by change class rather than by author — and where a class can be checked mechanically, a human reading it adds cost without adding safety |
| **Operator** | running production | a pre-authorised path to production | engineered verification can be made a stronger check than a human in the path — and the honest route there is to narrow what qualifies, never to widen who may act |

## The boundary criterion

**A boundary is crossed when the agent's output can reach the next surface — open file, working
tree, shared repository, trunk, production — with no human action in between.** The usual mechanism
is a credential or tool surface, held by the agent or pre-authorised on its behalf: a CD pipeline
that carries an agent's unread merge to production unattended holds the deploy credential on the
agent's behalf, so a team is Operator whether the agent holds deploy credentials or its trunk is
pre-authorised. Credentials and tool surfaces are enumerable and binary per item, which is what
makes the boundaries discontinuities rather than arbitrary cuts in a continuum — the ticket's
explicit requirement.

The criterion is grounded in **the independence rule** (`CONTEXT.md`): containment and human
oversight move independently, and the spectrum orders only containment. This is what forced the
choice. Defining boundaries by what the human stops gating would order oversight instead — filing
Armin Ronacher (minimal reach, zero supervision) at the far end and a team that grants production
credentials but approves every command at the near end, exactly the conflation this project exists
to break — and it would make the map's central claim ("further along means replacing human
verification with engineered verification") circular rather than a demand.

## Scope of the ceiling

An archetype names a team's **ceiling for model-generated changes**, attached to the configured
scope where the settings actually live. Deterministic automation with no model involved sits
outside the spectrum: Spotify's 2.5M auto-merged scripted transforms and Meta's RADAR (automated
*review* of risk-scored diffs) are the precedent the far-end pattern inherits from, not instances
of it. The genuinely agent-authored cases of unreviewed merge as stated policy number three
(Razorpay/Slash; JetBrains/IdeaVim changelog PRs; salvobase), every one a narrow carve-out. Hence
the far end's standing description: **Operator is reachable per change-class and observed as no
team's ceiling** — teams reach it by narrowing what qualifies, never by widening who may act.

## Considered options

- **Boundary = what the human stops gating** (the session's original recommendation). Rejected:
  orders oversight, misfiles the Ronacher case, and collapses the independence rule into
  circularity. See above.
- **Boundary = what verification replaced the human.** Rejected: ticket #5 found no published
  mechanism anywhere gates a change *because* it is agent-authored, so this would classify teams
  by something almost none of them have.
- **Four archetypes, merge as the last real gate.** Rejected: files a trunk-based team that merges
  unread but gates its release train together with an agent holding deploy credentials — very
  different risk postures, both real.
- **Four archetypes, buffer and workspace collapsed.** Rejected: the low extreme was fixed by the
  owner as "inline AI edits with nothing else about the process changing"; a workspace agent
  changes the process substantially.
- **Archetype = the typical (modal) change.** Rejected: unmeasurable from outside and drifts as
  volume shifts between change types.
- **Two formal axes.** Rejected: the spectrum stays one axis (containment) with oversight named
  alongside; every archetype document states reach, what a human still gates, and what
  verification must replace them, separately.
- **"Pair" as the second archetype's name** (the session's original choice). Rejected on review:
  it encodes oversight — a human present and watching — violating the session's own constraint
  that names encode reach. Its exemplar (Ronacher, unsupervised) and its own posture line ("not by
  who is watching it") both contradict it. Renamed **Workspace**, the literal reach name.
- **Human-role names (Author / Reviewer / Auditor).** Rejected: naming archetypes by what the
  human does re-fuses the two axes in the reader's head.
- **Literal reach names throughout; coinage names.** Viable and not disqualified. The middle three
  keep the OSS-governance intuition — a contributor opens PRs someone else merges; a committer
  holds merge rights — which developers already hold precisely, and which is descriptive rather
  than evaluative per ADR-0003.

## Consequences

- **The five names are ubiquitous language.** No document may drift to a synonym. Qualify on first
  use — "the Contributor archetype" — bare thereafter, mirroring the `CONTEXT.md` convention for
  *agent harness*; this also defuses collision with human contributors and committers.
- **"Committer" carries a standing note.** The Linux kernel forbids agents adding `Signed-off-by`
  — only humans certify the DCO, and merging an agent's PR is adoption, not authorship. The name
  describes the team's ceiling, never the agent's standing, and the Committer archetype document
  must say so explicitly rather than relying on readers to be told.
- **The FCA's Mills Review is named, not mapped.** It also has five positions, but it orders
  autonomy and this spectrum orders containment — independent axes. Cite it by name and date per
  ADR-0002, note the one rough correspondence (its L4 sits near Committer), and warn against
  mapping the rest. ADR-0002 is not amended; a commissioned review is not a standard.
- **Do not cite** "no exemplar describes itself by what it gates" in support of the boundary
  criterion — the review found it false (antirez and Hashimoto describe themselves entirely by
  what they gate). The criterion rests on the independence rule, not on how practitioners phrase
  themselves.
- Applied to `CONTEXT.md` (`Ceiling` and `Spectrum` amended). The per-archetype writing tickets
  and the exemplar document (issue #10) are written against this contract.
