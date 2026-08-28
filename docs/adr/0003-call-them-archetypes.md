# Call each grouping on the spectrum an "archetype"

The commissioning brief called each position on the spectrum a **framework**; the initial map drifted
to **tier**. Both are compromised for this audience: "framework" means React, Django or Spring to a
professional developer and has to be actively suppressed on every occurrence, while "tier" implies
ranking, which this project explicitly refuses — the documents describe groupings without declaring
any of them the goal state. We call each grouping an **archetype**: a grouping of teams that work
with AI in the same way. It is descriptive rather than evaluative, which matches the project's
reference-not-verdict stance, and it carries no collision with existing software vocabulary.

## Considered options

- **Framework** (the brief's word). Rejected: unavoidable collision with software frameworks.
- **Tier**. Rejected: tier lists rank, and ranking is the one thing these documents must not do.
- **Model** (as in "operating model"). Rejected outright: in a document about AI, "the Supervised
  Agent model" reads as a language model.
- **Stage / level / rung / maturity level**. Rejected: all imply a direction of travel and a
  destination, reintroducing the ranking through the back door.
- **Band**, **mode**, **profile**. All viable and none disqualified. "Band" inherits the spectrum
  metaphor but reads oddly in a standalone document title; "mode" implies something you switch
  rather than somewhere you sit; "profile" is precise but dry. Archetype was chosen because the
  commissioning question was "where do we feel comfortable being" — an identity, not a setting.

## Consequences

- **Ordinal grammar has to go.** "Archetype" does not support "higher", "moving up" or "upper".
  Documents say **further along the spectrum**. This is the decision doing its work: the old
  wording smuggled ranking in through the grammar even where the noun was neutral.
- **Archetype Taxonomy (issue #8) still owns the individual names** — how many archetypes there are
  and what each is called. This ADR fixes only the category noun.
- Applied retroactively across the map, all nine tickets, `CONTEXT.md` and ADR-0002. Issues #8 and
  #10 were renamed to *Archetype Taxonomy* and *Exemplar Archetype Document*.
