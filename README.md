# The AI Usage Spectrum

A reference work in progress: a set of fully-cited HTML documents defining the full spectrum of
how professional development teams work with AI — from minimal inline assistance to fully
autonomous delivery to production. The documents **describe rather than recommend**: each position
gets a "this fits a team that believes X" characterisation, and none is presented as the goal
state. The team's actual choice of position is a separate discussion this project deliberately
does not touch.

Everything is grounded in a ~29,000-line research corpus built against primary sources, with every
figure carrying a source, a date, and an evidence tier.

## The core ideas

**Five archetypes, ordered by reach.** An *archetype* is a grouping of teams that work with AI the
same way. The five, with what the agent's output can reach:

| Archetype | The agent's output can reach | Gained at this boundary |
|---|---|---|
| **Autocomplete** | the open file; a human accepts every edit | — (the fixed low extreme) |
| **Workspace** | the working tree, locally | file-write and shell tool surfaces |
| **Contributor** | the shared repository; a human merges | a push credential |
| **Committer** | trunk, unread; a human gates release | merge rights |
| **Operator** | running production | a pre-authorised path to production |

Three decisions make the taxonomy hold together (all recorded in [ADR-0004](docs/adr/0004-adopt-five-archetypes.md)):

- **An archetype is a ceiling, not a behaviour.** It names the maximum delegation a team's settings
  and policies *permit* for model-generated changes — not what any individual change receives.
  What an administrator flips, and what vendor contracts key liability to.
- **Boundaries are capabilities, not degrees.** A boundary is crossed when the agent's output can
  reach the next surface with no human action in between. Credentials are binary per item, which
  makes the boundaries real discontinuities rather than arbitrary cuts in a continuum.
- **The independence rule.** Containment (what the agent *can* reach) and human oversight (what a
  human actually gates) move independently; the spectrum orders only containment. A team can grant
  little reach and supervise none of it, or grant production reach and gate every action.

The spine of the whole work: moving further along the spectrum does **not** mean relaxing
discipline — it means replacing human-in-the-loop verification with *engineered* verification.
The research established this is a **requirement, not a description of practice** (the machinery
exists but is almost never wired to autonomy), so the documents write the demand, never the claim
that teams meet it.

Archetypes are **kinds, not ranks**. House grammar follows: "further along the spectrum," never
"higher"; never "tier," "level," "maturity," or a bare "L3 autonomy."

## How the project works

Work is charted as a **wayfinder map** — a planning method where a large, foggy effort becomes a
single map issue with child tickets, worked one decision at a time:

- **The map:** [#1 Map: The AI Usage Spectrum](https://github.com/AndrewGodlewsky/AI-Framework/issues/1)
  — destination, standing notes, an index of every decision made so far, and the "not yet
  specified" fog. Read it first in any session.
- **Tickets** are GitHub sub-issues of the map, each labelled `wayfinder:<type>`
  (`research` / `grilling` / `prototype` / `task`) and each carrying a `## Skills` section naming
  the skills that drive it — that section is authoritative for how the ticket gets resolved.
  Blocking uses GitHub's native issue dependencies, so the frontier (open, unblocked, unclaimed)
  is visible in the GitHub UI. A session claims a ticket by self-assigning before any work.
- **Resolutions** are posted as a comment on the ticket, the ticket is closed, and a one-line
  pointer is appended to the map's *Decisions so far*. Decisions that shape the architecture of
  the work become ADRs in `docs/adr/`; vocabulary rulings land in `CONTEXT.md`.

**Evidence standards** (binding on every document): every number carries a source and date; the
evidence tier — hard survey / controlled study / vendor-reported metric / practitioner anecdote —
is stated *with* the claim, never as a blanket disclaimer; contrarian and negative findings are
included; if nobody practises an archetype, the documents say so rather than inventing
practitioners; unverifiable quotes are dropped, not softened. Known citation traps are catalogued
in `research/evidence-base.md`. One research sub-strand once fabricated content and disclosed it —
the retraction, rewrites, and integrity notices are preserved in place as part of the record
(see the notice at the head of `research/governance-compliance.md`).

`CONTEXT.md` is the **ruling vocabulary**. Its `_Avoid_` lines are binding on every document;
read it before writing anything.

## Where everything is

```
CONTEXT.md                      The ruling vocabulary — terms, definitions, binding _Avoid_ lines
CLAUDE.md                       Agent instructions: tracker, labels, wayfinder ticket rules
README.md                       This file

style.css                       The shared stylesheet every page links (design system, ticket #9)
archetype-template.html         The archetype page template — the 8-section contract, with the
                                "you are here" spectrum diagram (Committer specimen content)
prototype-hub-visual.html       Throwaway demo of the hub spectrum visual with expandable
                                per-archetype cards; absorbed into index.html later, then deleted

docs/
  adr/                          Architecture decision records — the project's settled decisions
    0001  Retire "graph engineering" (use agent orchestration / flow engineering)
    0002  Define our own archetype set (no autonomy-levels standard exists)
    0003  Call the groupings "archetypes" (kinds, not ranks; ordinal grammar banned)
    0004  Adopt the five-archetype taxonomy (the contract for every document)
  agents/                       How agent sessions use this repo: issue tracker conventions,
                                triage labels, domain docs
  archetype-taxonomy-review.md  The taxonomy's full decision record: seven decisions, the
                                independent review, and the six amendments adopted (§9)

research/                       The evidence corpus, ~24 files. Highlights:
  evidence-base.md              Adoption/efficacy evidence + the citation-trap catalogue
  practitioner-exemplars.md     ~57 named exemplars; the far-end count ("three cases")
  vocabulary-and-disciplines.md Terminology against primary sources (feeds CONTEXT.md)
  verification-*.md             Gates, evals, isolation, observability, tests, infrastructure
  governance-*.md               Legal, IP, compliance, accountability, provenance, licensing
  tooling-*.md                  The tool landscape: CLIs, IDEs, background agents, orchestration
  refusal-policies-primary-sources.md  Verbatim text of ~25 restriction regimes (Debian GR
                                result, Fedora's ratified policy, CMORG guidance, …)
```

**The destination** (not yet written): `index.html` — the hub with the spectrum visual and
expandable archetype cards; one page per archetype following the template contract;
`glossary.html`. All committed to this repo with relative links.

## Status and what's next

Done: six research tickets, the archetype taxonomy (reviewed and amended), the design system, and
the blocked-source verification pass. Open on the map:

- **[Exemplar Archetype Document #10](https://github.com/AndrewGodlewsky/AI-Framework/issues/10)**
  — unblocked, next up: write one complete archetype document (the hardest one the research
  supports) end to end, to prove the template survives real content. Its approval is the gate
  that unlocks batched writing of the remaining four.
- **[Blocked-Source Remainder #12](https://github.com/AndrewGodlewsky/AI-Framework/issues/12)** —
  the verification items that genuinely remain (two need an owner decision first); does not block
  the exemplar.

Still in the fog: the four remaining archetype documents (graduate once the exemplar settles which
archetype it takes), the hub and glossary pages, and a final cross-linking pass.
