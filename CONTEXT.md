# AI Usage Spectrum

The vocabulary of this project: the terms used across every document describing how professional
development teams work with AI, from minimal inline assistance to fully autonomous delivery.

Terms and verdicts here are grounded in [research/vocabulary-and-disciplines.md](./research/vocabulary-and-disciplines.md),
which carries the primary sources and dates. This file is the ruling; that file is the evidence.

Established 2026-08-27. This vocabulary moves at roughly one major new term per quarter — carry a
dated "as of" in any document that uses it.

## Language

### The spectrum

**Archetype**:
A grouping of teams that work with AI in the same way, defined by what the human stops doing and
what engineered verification replaces them with. Archetypes are kinds, not ranks — none is the
goal state, and no archetype is "higher" than another.
_Avoid_: tier and level (imply ranking), framework (means React/Django to this audience), model
(reads as *language model*), stage and maturity level (imply progression)

**Spectrum**:
The set of archetypes ordered by degree of delegation, from minimal AI assistance to unsupervised
autonomous delivery. Ordering is by delegation only, never by desirability.
_Avoid_: maturity model, adoption curve, ladder (all imply higher is better). Write "further along
the spectrum", never "higher up" — the ordinal grammar reintroduces the ranking the noun removes.

**Posture**:
The set of beliefs and constraints — about trust, risk and what AI should touch — that lands a
team in a particular archetype.
_Avoid_: maturity, sophistication, readiness

### Disciplines

**Context engineering**:
The discipline of assembling what an agent sees: instructions, retrieved code, tool results,
history, and what is deliberately excluded. Retrieval, codebase indexing and code graphs sit
inside it.
_Avoid_: prompt engineering as the name of the discipline — it is now a subset, meaning the
wording of instructions specifically

**Agent harness**:
Everything around the model that makes it an agent: the agent loop, tool surfaces, permission
modes, hooks, sandboxes, and feedback loops. Always qualify as "agent harness" on first use in any
document that also discusses evaluation.
_Avoid_: bare "harness" where eval harnesses are also discussed

**Harness engineering**:
The discipline of designing an agent harness. Established vocabulary as of 2026, and measurably
load-bearing: harness choice moves benchmark results about as much as model choice.
_Avoid_: scaffolding (the 2024 name for the same thing — near-synonym, not a distinction to
build an argument on)

**Eval harness**:
The evaluation infrastructure that runs a benchmark and scores results. A different thing from an
agent harness; conflating them corrupts benchmark numbers.
_Avoid_: bare "harness"

**Agent orchestration**:
The discipline of structuring work across multiple agent steps or agents: subagent fan-out,
pipelines, gates, checkpoints, handoffs.
_Avoid_: **graph engineering** — not a term of art anywhere in this field, and it collides with
the unrelated, established "knowledge graph engineering"

**Flow engineering**:
The narrower practice of encoding the control flow explicitly rather than leaving the sequence to
the agent's judgement. A technique within agent orchestration, not a synonym for it.

**Agent Skill**:
A packaged, model-invoked instruction module following the SKILL.md specification. Capitalise and
qualify on first use — bare "skill" has at least four competing senses.
_Avoid_: bare lowercase "skill" for the artifact; "industry standard" for the specification (it is
openly published with broad adoption, but has no neutral governance body)

**Evals**:
Task-specific, purpose-built measurements of whether a system does acceptable work. Distinct in
practice from public benchmarks, though that distinction has no authoritative source.
_Avoid_: treating evals and benchmarks as interchangeable

**Agentic engineering**:
Professional software development where agents do substantial work under engineered constraint.
The current name for the practice this project's later archetypes describe.
_Avoid_: vibe coding (means prototypes where the diffs go unread — a category error applied to
disciplined work); vibe engineering (retired by its own author)

### Autonomy and oversight

**Autonomy**:
A per-action property — what this agent may do without approval, in this context. Describe it by
naming what the human approves and when.
_Avoid_: "L3 autonomy" or any bare level reference; no standards body has published a scale, and
the two leading proposals contradict each other

**Human oversight**:
What a human actually gates, named specifically. The registerial default: regulators use this
phrase, never the loop vocabulary.
_Avoid_: "human-in-the-loop" as a reassurance claim — approval rates on permission prompts run
around 93%, so the mechanism does not imply the outcome

**Containment**:
Restricting what an agent *can* do — sandboxes, egress controls, least-privilege tool scopes —
rather than approving what it does. The field's structural answer to the limits of supervision.
_Avoid_: guardrails as a load-bearing noun; name the mechanism instead (validation, allowlist,
sandbox, classifier, tripwire, permission rule, hook)

**Perception gap**:
The measured difference between how much faster developers believe AI makes them and how much
faster they measurably are. Consistently large and consistently in one direction — belief exceeds
measurement.
_Avoid_: presenting it as proof that AI makes developers slower. The gap is well-evidenced; the
slowdown is not

**Lethal trifecta**:
The combination of private data access, exposure to untrusted content, and the ability to
externally communicate — the configuration under which prompt injection becomes exfiltration.

**Verification**:
The engineered machinery that establishes a change is acceptable when a human has not read it:
tests, gates, static analysis, canaries, rollback, evals.
_Avoid_: using "review" for both human reading and automated checking — they are the two things
this project most needs to keep apart

### Protocols and formats

**MCP (Model Context Protocol)**:
An open, foundation-governed protocol for connecting agents to tools and data.
_Avoid_: "the USB-C of AI" and similar analogies — they obscure both the governance question and
the unresolved prompt-injection threat model

**AGENTS.md**:
A foundation-governed open standard for repository-level agent instructions. The cleanest example
of an actual open standard in this space.

### Citation hygiene

**Evidence tier**:
The classification every cited figure carries — hard survey data, controlled study, vendor-reported
metric, or practitioner anecdote. Stated with the claim itself, never as a blanket disclaimer at the
foot of a page.

**Joint measurement**:
An agent benchmark score, which reflects model and harness together. Always report as
"model X + harness Y resolves N%", never as a property of the model alone.
_Avoid_: any bare agent benchmark score; SWE-bench Verified scores entirely, deprecated by their
own publisher in February 2026 for training contamination
