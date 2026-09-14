# The AI Usage Spectrum

A reference set describing how professional development teams work with AI, from inline
autocomplete to unattended delivery into production. Five **archetypes**, ordered by what the
agent's output can reach with no human action in between, each written up end to end with every
claim cited and its evidence tier stated. The documents **describe rather than recommend**: each
archetype ends with "this fits a team that believes X", and none is presented as the goal state.
Choosing an archetype is a separate conversation this project deliberately does not have for you.

Everything rests on a research corpus of ~29,000 lines across 25 files, built against primary
sources, with every figure carrying a source, a date and a tier.

---

## Start here

**To read it:** open [`pdf/ai-usage-spectrum-2026-09.pdf`](pdf/ai-usage-spectrum-2026-09.pdf)
(the whole set under one cover, 45 pages, live internal links, bookmarks) or open
[`index.html`](index.html) in a browser. Nothing needs building.

**Ten minutes:** the hub page — the spectrum strip and the five summary cards. Then read the
posture line at the bottom of each card and notice which one your team already believes.

**One hour:** the hub, then [`contributor.html`](contributor.html) (where nearly every named
organisation actually sits) and [`operator.html`](operator.html) (the far end, where the evidence
is thinnest and the demands are heaviest). Those two pages carry the project's argument between
them.

**Everything:** the five archetype pages in order, then the glossary, then dip into `research/`
using the guide below.

---

## The core ideas

### Five archetypes, ordered by reach

An *archetype* is a grouping of teams that work with AI the same way. Its name is the team's
**configured ceiling** for model-generated changes — what the settings and policies permit, not what
any individual change receives.

| Archetype | The agent's output can reach | Gained at this boundary | Fits a team that believes |
|---|---|---|---|
| **Autocomplete** | the open file; a human accepts every edit | — (the fixed low extreme) | reading every line is non-negotiable, and anything reducing what a human reads costs more than it saves |
| **Workspace** | the working tree, locally; nothing leaves without a human | file-write and shell tool surfaces | risk is bounded by what the agent can reach, not by who is watching it |
| **Contributor** | the shared repository; a human merges every change | a push credential | review is the load-bearing control and should stay human, and an agent's work should come through the same front door as anyone else's |
| **Committer** | trunk, unread, for a defined class of change; a human gates release | merge rights | trust should be earned by change class rather than by author; where a class can be checked mechanically, a human reading it adds cost without adding safety |
| **Operator** | running production; the path is pre-authorised | a pre-authorised path to production | engineered verification can be made a stronger check than a human in the path, and the honest route there is to narrow what qualifies, never to widen who may act |

### Three rules that make it hold together

All recorded in [ADR-0004](docs/adr/0004-adopt-five-archetypes.md):

- **An archetype is a ceiling, not a behaviour.** It names the maximum delegation a team's settings
  *permit* for model-generated changes. It is what an administrator flips, and what vendor contracts
  key liability to (Cursor's terms make the customer "solely responsible" the moment auto-execution
  is enabled). A team is not further along the spectrum because one change was auto-merged, only
  because auto-merging was permitted.
- **Boundaries are capabilities, not degrees.** A boundary is crossed when the agent's output can
  reach the next surface — open file, working tree, shared repository, trunk, production — with no
  human action in between. Credentials are binary, which makes the boundaries real discontinuities
  rather than arbitrary cuts in a continuum.
- **The independence rule.** Containment (what the agent *can* reach) and human oversight (what a
  human actually gates) move independently; the spectrum orders only containment. A team can grant
  an agent very little reach and supervise none of it (Armin Ronacher runs Claude Code with all
  permission checks off, contained by Docker), or grant production reach and gate every action.
  Every archetype page therefore states three things separately: what the agent can reach, what a
  human still gates, and what verification must replace them.

### The spine

Moving further along the spectrum does **not** mean relaxing discipline. It means replacing
human-in-the-loop verification with *engineered* verification: tests the agent cannot weaken, gates
that live server-side outside the agent's reach, canaries, auto-revert, evals. Archetypes further
along demand **more** rigor, not less.

The research established that this is a **requirement, not a description of practice**. The
machinery exists, and mostly predates agents, but it is almost never wired to autonomy: no adopted
mechanism anywhere gates, canaries or auto-reverts a change *because it was agent-authored*. So the
documents write the demand and never the claim that teams meet it.

### The grammar

Archetypes are **kinds, not ranks**. The documents say "further along the spectrum", never
"higher"; never "tier", "level", "maturity", "ladder", or a bare "L3 autonomy". The full ruling
vocabulary, with the reasons behind each avoided term, is [`CONTEXT.md`](CONTEXT.md) and the
reader-facing [`glossary.html`](glossary.html).

---

## The documents

Seven HTML pages, one shared stylesheet, all relative links. Every archetype page follows the same
eight-section contract, so the pages can be read side by side:

> 01 What this archetype is · 02 The boundary crossed · 03 What a human still gates ·
> 04 Who works this way · 05 What it gains you, what it costs · 06 What it demands of verification ·
> 07 Governance implications · 08 The posture that fits · Sources

Every claim carries an inline citation chip with source, date and an evidence-tier dot, pointing at
a numbered sources entry at the foot of the page.

| Page | What it is | The load-bearing point |
|---|---|---|
| [`index.html`](index.html) | The hub: the spectrum strip with expandable per-archetype cards | The whole taxonomy on one screen; each card gives "made of", "demands first", gains and costs, and the posture line |
| [`autocomplete.html`](autocomplete.html) | The fixed low extreme | The only archetype whose ceiling is architectural rather than configured: completion has no tool surface, and the crossing to anything that *acts* is one keypress (VS Code's terminal **Run** control). The only region with clean randomised-trial support |
| [`workspace.html`](workspace.html) | File-write and shell locally, no push credential | Carries the independence rule's flagship case (Ronacher: minimal reach, minimal oversight). The last boundary crossed by adopting a tool rather than granting a credential. Liability first attaches to a setting here |
| [`contributor.html`](contributor.html) | Push credential; a human merges every change | The archetype the tool market *ships* and the only boundary the *platform* enforces (no product merges its own PR). The large middle: Stripe, Monzo, Dropbox, Uber, Microsoft's `dotnet/runtime`. Reviewer habituation under agent volume is now measured, so what must be engineered here is **protection of the review** |
| [`committer.html`](committer.html) | A defined change class reaches trunk unread; a human gates release | Every genuine occupant grants this to a narrow, mechanically identified class — changelog updates, forward-merges, low-severity fixes — never to the agent in general. No study anywhere compares unread agent merges against reviewed ones |
| [`operator.html`](operator.html) | Nothing human between the change and running production | Reachable per change class; observed as **no team's ceiling** — searched for, not merely unobserved. Meta's RADAR is the delivery-end anchor (331k+ diffs, no human reviewer, on a subset selected for low risk). The exemplar page: written first, and the template held unchanged through all five |
| [`glossary.html`](glossary.html) | The ruling vocabulary, as the pages use it | Definitions, the avoided terms and why, the citation tiers, and a note on why external autonomy scales are not mapped onto this spectrum |

The compiled PDF also has a cover page listing all seven.

---

## What the research found

The headline findings, by theme, with the file to open for the evidence. Every file is dated, and
every figure in it carries its source.

**Adoption and efficacy** — `research/evidence-base.md`
Headline adoption numbers are unusable: four instruments ask four different questions (75/84/90/90%).
Code-quality evidence is a standoff that splits cleanly by tier — vendor metrics say degrading,
academic studies say not. METR walked back its own "AI slows developers" study; the durable finding
is the **perception gap** (developers believe they are much faster than they measurably are). The
far end is practised but unevaluated: unreviewed agent merges happen at measurable volume, and no
study compares them with reviewed ones. The file also catalogues the **citation traps** — retracted,
mislabelled or modelled figures still in wide circulation.

**Who actually works where** — `research/practitioner-exemplars.md`, `research/refusal-policies-primary-sources.md`
About 57 named organisations and individuals, each with the claimant's stake recorded. The far end
is three cases, none of which is what "agents ship to production" implies; four widely cited far-end
exemplars did not survive inspection. **No company anywhere restricts AI code on quality grounds** —
every verified restriction is cost, security, jurisdiction or vendor competition. Refusal more than
doubles across the delegation axis. The companion file holds verbatim primary text for ~25
restriction policies and shows the press consistently reports nuanced authorship policies as flat
bans (Debian's General Resolution: "Responsible Use of Generative AI" won; the ban failed decisively).

**Verification** — `research/verification-infrastructure.md` (summary) plus `verification-gates.md`, `verification-tests.md`, `verification-evals.md`, `verification-isolation.md`, `verification-observability.md`
The spine tested. The vendors built their AI code reviewers so they **cannot gate** (Copilot leaves a
non-counting comment; Anthropic's check run always reports neutral, which GitHub counts as passing),
and six of eight have no published accuracy figure. Checks are targets: handed a proof obligation it
could not pass, an agent silenced failures, then excluded the code from proof, so anti-suppression
must be engineered. Evals decay silently (one vendor lost its regression workflow in an unrelated
refactor with nothing noticing). Rubber-stamping is measured: approval of agent PRs rising, inline
comments down 22%, latency up 3.5×. Nothing in NIST SSDF, SLSA or ISO 26262 requires a human to
read code; SLSA grants "trusted robots" a perpetual review exception.

**Tooling** — `research/tooling-landscape.md` (summary) plus `tooling-inline-and-chat.md`, `tooling-agentic-ide.md`, `tooling-agentic-cli.md`, `tooling-background-agents.md`, `tooling-orchestration.md`, `tooling-openclaw.md`
The six product categories are a product taxonomy, not six regions of the spectrum. Only three
boundaries matter, and only one is a tool boundary: **propose-vs-act** (architectural, one keypress
wide), **approval** (configurable everywhere; no product structurally refuses to hand over the last
approval, and three CLIs ship with it already gone), and **merge** (platform-enforced). So "the human
approves each change" is a configuration, not a property of any product, and the far end is reached
by an administrator changing a policy, not by buying a tool. Eight of eleven agentic CLIs ship no
OS-level containment; command allowlists have a five-product CVE record; no tool couples permission
to a verification outcome ("allow `git push` only if the tests passed" cannot be expressed anywhere).

**Governance, legal and IP** — `research/governance-legal-ip.md` (summary) plus `governance-compliance.md`, `governance-accountability.md`, `governance-ip-copyright.md`, `governance-licensing-indemnity.md`, `governance-provenance-audit.md`, `governance-data.md`
**Nothing in law or standards requires a human to read source code** — verified across SOC 2,
ISO 27001, ISO/IEC 42001, the EU AI Act, DORA, the CRA, NIST SSDF, SLSA, HIPAA and DO-178C. So
compliance is not what stops teams delegating; every archetype can be compliant with a documented,
followed process. What varies is a setting, and one vendor attaches liability to it contractually.
All six providers disclaim defect liability outright. Merging an agent's PR is *adoption*, not
authorship, so the operative provenance question is "which lines did a human write" — and the
attribution that answers it survives on GitHub by undocumented behaviour and dies in plain git under
a squash merge. The EU AI Act's 2026 amendment puts developer-performance analytics, not coding
assistants, in the high-risk category.

**Vocabulary** — `research/vocabulary-and-disciplines.md`
Terminology established against primary sources. "Graph engineering" is not a term of art and was
retired; "harness engineering" is real and about as load-bearing as model choice; no autonomy-levels
standard exists anywhere, so the project defines its own archetypes and says so. Human-in-the-loop
cannot bear its reassurance weight: the vendor holding the telemetry reports ~93% of permission
prompts approved, and human review catching 13.6% of dangerous commands against 89% for automated
checking.

**The vendor's own playbook** — `research/ai-native-sdlc-playbook.md`
A digest of Anthropic Academy's *AI-Native SDLC Playbook*, cited across the archetype pages at
vendor tier. Its recommended end state is Workspace-in-auto-mode plus Contributor, with the
production gate explicitly withheld ("the agent may act up to the production gate and cannot pass
it") — the Contributor thesis corroborated from the vendor's own mouth. It publishes no measurements.
The transcript it digests is committed at `reference/ai-native-sdlc-playbook.html` with its
© Anthropic attribution intact.

---

## Evidence standards

Binding on every document:

- Every number carries a source and a date. Named companies, teams or individuals per archetype,
  not abstractions.
- The **evidence tier** is stated *with* the claim, never as a blanket disclaimer:
  hard survey data · controlled study or verified primary artifact · vendor-reported metric ·
  practitioner anecdote. Each cited practitioner's stake is recorded.
- Contrarian and negative findings are included, not filtered. If nobody practises an archetype, the
  documents say so rather than inventing practitioners.
- Unverifiable quotes are dropped, not softened. Sources behind paywalls or licence walls were never
  circumvented; what could not be read first-party is marked as such and not quoted.
- Agent benchmark scores are joint measurements of model plus harness and are never reported bare.
  SWE-bench Verified is not cited at all: its publisher deprecated it in 2026 for training
  contamination.

One research sub-strand fabricated a section (UK legislation) and disclosed it after its ticket
closed. It was retracted in full; the rewrite, the integrity notices and the correction trail are
preserved in place rather than erased — see the notice at the head of
`research/governance-compliance.md`.

---

## Repository map

```
README.md                       This guide
CONTEXT.md                      The ruling vocabulary: terms, definitions, binding "avoid" lines
CLAUDE.md / AGENTS.md           Instructions for agent sessions working in this repo

index.html                      The hub: spectrum strip and expandable archetype cards
autocomplete.html               Archetype 1 of 5
workspace.html                  Archetype 2 of 5
contributor.html                Archetype 3 of 5
committer.html                  Archetype 4 of 5
operator.html                   Archetype 5 of 5 (the exemplar, written first)
glossary.html                   The ruling vocabulary, reader-facing
style.css                       The shared stylesheet: design tokens, the citation-chip convention,
                                the spectrum SVG styling, and the @media print pass for the PDFs
archetype-template.html         The eight-section contract as a template (specimen copy only)

pdf/
  ai-usage-spectrum-2026-09.pdf The whole set under one cover, in reading order
  index-2026-09.pdf … glossary-2026-09.pdf   Each page on its own
scripts/
  build-pdf.py                  Regenerates pdf/ from the HTML — see "The PDF versions"

docs/
  adr/
    0001-retire-graph-engineering.md        Use "agent orchestration" / "flow engineering"
    0002-define-our-own-archetype-set.md    No autonomy-levels standard exists; define our own
    0003-call-them-archetypes.md            Not "framework", "tier" or "model": kinds, not ranks
    0004-adopt-five-archetypes.md           The five-archetype contract every document follows
  archetype-taxonomy-review.md  The taxonomy's full decision record: seven decisions, an
                                independent second-model review, and the six amendments adopted
  agents/                       How agent sessions use this repo: issue tracker, labels, domain docs

research/                       The evidence corpus — 25 files, ~29,000 lines, all dated
  evidence-base.md              Adoption and efficacy evidence; the citation-trap catalogue
  practitioner-exemplars.md     ~57 named exemplars with stake recorded; the far-end count
  refusal-policies-primary-sources.md   Verbatim text of ~25 restriction policies
  vocabulary-and-disciplines.md Terminology against primary sources (feeds CONTEXT.md)
  verification-infrastructure.md        Summary of the verification strands
    verification-gates.md       Checks between a change and production; the server-side-gate test
    verification-tests.md       Test rigor and the circularity problem
    verification-evals.md       Evals as engineered verification over time
    verification-isolation.md   Sandboxes, containment, blast radius
    verification-observability.md Detection, provenance and reversal when nobody read the diff
  tooling-landscape.md          Summary of the tooling strands
    tooling-inline-and-chat.md  Completion and in-editor chat; the propose-vs-act boundary
    tooling-agentic-ide.md      Agentic IDE modes; the allowlist CVE record
    tooling-agentic-cli.md      Eleven agentic CLIs: defaults, sandboxes, approval switches
    tooling-background-agents.md  Cloud and background agents; the merge boundary
    tooling-orchestration.md    Multi-agent orchestration frameworks
    tooling-openclaw.md         The far-end anchor examined (it anchors containment, not delivery)
  governance-legal-ip.md        Summary of the governance strands
    governance-compliance.md    What each regime actually requires (with the correction notice)
    governance-accountability.md  Who is answerable for a defect nobody read
    governance-ip-copyright.md  Authorship vs adoption; registration and disclaimers
    governance-licensing-indemnity.md  Provider indemnities and what voids them
    governance-provenance-audit.md     Reconstructing who wrote what, after the fact
    governance-data.md          What leaves the building when code becomes context
  ai-native-sdlc-playbook.md    Digest of the Anthropic Academy course (vendor tier)

reference/
  ai-native-sdlc-playbook.html  Compiled transcript of the course, © Anthropic, attribution intact
```

---

## The decisions record

Decisions that shape the work are recorded as architecture decision records in `docs/adr/`, each
with the options considered and why the others were rejected:

1. **Retire "graph engineering."** Not a term of art anywhere; collides with knowledge-graph
   engineering. Use *agent orchestration*, or *flow engineering* for the narrow sense.
2. **Define our own archetype set.** Verified negatively against NIST AI RMF, ISO/IEC 22989,
   IEEE P3394, SAE and the EU AI Act: no autonomy-levels standard exists, and the leading proposals
   contradict each other. The FCA's Mills Review (2026) publishes an L1–L5 scale about writing code;
   the glossary names it and explains why it is a different axis.
3. **Call the groupings "archetypes."** "Framework" means React to this audience; "tier" ranks;
   "model" reads as language model.
4. **Adopt the five-archetype taxonomy.** The contract above. Produced in a structured
   questioning session against the corpus, then independently reviewed by a second model, which
   upheld all seven decisions with six amendments (the full record is
   `docs/archetype-taxonomy-review.md`).

Vocabulary rulings land in `CONTEXT.md`. Everything else — every research finding, every design
choice, every correction — is indexed on the map issue described next.

---

## How the work was done

The project was run as a **wayfinder map**: one GitHub issue holds the destination, the standing
notes, and an index of every decision made; child issues are the tickets, worked one decision per
session. The whole trail is public and readable end to end:

- **The map:** [#1 Map: The AI Usage Spectrum](https://github.com/AndrewGodlewsky/AI-Framework/issues/1).
  Its *Decisions so far* section is a one-paragraph gist of every closed ticket, each linking to
  the ticket's resolution comment with the full reasoning.
- **Tickets** were labelled by type (`research`, `grilling`, `prototype`, `task`) and blocked with
  GitHub's native issue dependencies, so what was workable was always visible in the GitHub UI.
  Six research tickets ran first and in parallel; the taxonomy and design system were decided
  against their findings; one exemplar document proved the template; the remaining four were
  written against the settled pattern with zero template revisions; a consistency pass closed the
  HTML destination on 2026-09-02; the playbook digest and the PDFs completed the extended
  destination on 2026-09-13.
- **Corrections are part of the record.** Two verification tickets re-read every blocked or
  secondary-sourced quote first-party; figures that did not survive were withdrawn from the pages
  and the withdrawal noted where they had stood.

The agent-facing conventions (tracker operations, labels, where domain docs live) are in
`docs/agents/`.

---

## The PDF versions

`pdf/` holds the set as PDFs: `ai-usage-spectrum-YYYY-MM.pdf` compiles all seven documents under a
cover page in reading order, with live internal links and a heading outline; each page is also cut
on its own. Regenerate them after any change to the HTML:

```
python scripts/build-pdf.py
```

Requires Google Chrome (or Chromium/Edge) and `pip install pypdf`; nothing else and no network.
The script compiles the pages into one HTML document, prints it with headless Chrome under the
`@media print` rules in `style.css` (A4 — change `@page` there for Letter), and stamps a running
footer with page numbers. Embedded fonts are whatever the build machine resolves the stylesheet's
system font stacks to.

---

## Presenting this to a team

The set was written to be handed over, not argued from. A walkthrough that has worked on paper:

1. **The strip** (hub page, 5 minutes). Five surfaces, four gates. Say the ordering rule aloud:
   *what the agent's output can reach with no human in between.* Then the independence rule, because
   it is the thing people get wrong first — a team is not "less careful" for being further along.
2. **The posture lines** (10 minutes). Read the five "fits a team that believes…" lines and ask
   which one the room already believes. That usually locates the team without anyone arguing about
   tools.
3. **The spine** (5 minutes). Further along means *more* engineered verification, and the research
   says almost nobody has built it yet. This reframes "should we let the agent do more" as "what
   would we have to build first".
4. **Where the field actually is** (10 minutes). Contributor is what the market ships and the
   platform enforces; the far end is three narrow cases; no team observed sets Operator as its
   ceiling. The honest numbers: reviewers habituate under agent volume, the perception gap is large
   and one-directional, and no study anywhere tests unread agent merges against reviewed ones.
5. **Stop there.** The documents end at the boundary of the decision. What archetype the team
   chooses — per repository, since the ceiling is a property of where the settings live — is the
   team's conversation, with these pages as the shared reference.

For a hand-out, use the compiled PDF; for a room, open `index.html` and expand the cards live.

---

## Status

The destination, as extended by the owner, was reached on 2026-09-13: every archetype document
exists, every claim is sourced, the set cross-links cleanly, the vendor playbook is digested and
cited, and the PDF versions are in `pdf/`.

One optional ticket remains open on the map:
[Owner-gated source verifications #19](https://github.com/AndrewGodlewsky/AI-Framework/issues/19)
— two compliance quotes (SOC 2 CC8.1, PCI DSS 6.2.3.1) behind registration or licence walls. The
owner has decided not to register; the ticket verifies from freely accessible first-party material
only, and anything that stays walled ends as a permanent pending marker in the research files. It
blocks nothing, and no document quotes either artifact.
