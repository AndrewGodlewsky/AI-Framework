# Tooling Landscape: Multi-Agent Orchestration Frameworks

**Research date:** 2026-08-30
**Ticket:** [#6 Tooling Landscape](https://github.com/AndrewGodlewsky/AI-Framework/issues/6) — strand: multi-agent orchestration frameworks
**Question:** What does a team take on when it stops using someone else's agent product and builds the agent system itself — and is there any evidence that anyone ships software this way?

**Scope.** This strand covers the region furthest along the spectrum in terms of what a team takes
responsibility for: the team is now writing the agent harness, not just configuring one. Two distinct
things live here and this document keeps them apart throughout, because conflating them is the main
error the category invites:

- **(a) General-purpose agent-building frameworks** — libraries for constructing agent systems of any
  kind, of which coding is one application. LangGraph, CrewAI, AutoGen/AG2, OpenAI Agents SDK,
  Claude Agent SDK, Google ADK, Microsoft Agent Framework, Temporal-backed durable agents,
  LlamaIndex Workflows, Pydantic AI, Mastra, smolagents, DSPy. **Part A.**
- **(b) Multi-agent features inside coding tools** — subagents, orchestrator modes, peer sessions,
  worktree parallelism, script orchestration. Claude Code, Cursor, Devin, Roo Code, Cline, Amp.
  **Part B.**

**Method.** Primary sources only: official documentation, repository READMEs and source, arXiv
papers, first-party engineering blogs. Framework landing pages and customer-story pages are read but
labelled **vendor marketing** wherever cited. Docs pages carry the date they were read (2026-08-30)
where the page itself publishes none.

**Evidence tiers used below:** `[controlled study]`, `[hard survey]`, `[vendor-reported]`,
`[primary artifact]` (source, docs, or config read directly), `[practitioner anecdote]`,
`[emptiness finding]` (a documented absence after a directed search).

---

## The verdict up front

**This is the region of the tooling landscape where the discourse is loudest and the
shipped-software evidence is thinnest.** After a directed search of first-party sources:

1. **No first-party engineering write-up was found in which a general-purpose multi-agent framework
   writes and ships application software in production.** The named production systems built on these
   frameworks are conversational assistants, research assistants, data agents, customer support, and
   *platform/infrastructure* operations. The closest software-engineering case found — Cisco
   Outshift's CAIPE/JARVIS — automates platform-engineering toil, not application code.
2. **The largest published production software-engineering AI system that could be found is
   explicitly not multi-agent.** Uber's uReview processes over 90% of ~65,000 weekly diffs using a
   **prompt-chaining** architecture built in-house, with no third-party orchestration library
   ([Uber, 2025-08-12](https://www.uber.com/us/en/blog/ureview/)).
3. **The two vendors with the most exposure to agentic coding have both published against naive
   multi-agent architectures** — Cognition explicitly, Anthropic by scoping where it works and
   excluding most coding from that scope.
4. **The frameworks and the coding tools are converging on the same answer, and it is not
   multi-agent autonomy — it is flow engineering.** Independently, in 2026, Cognition's Devin and
   Anthropic's Claude Code both shipped a feature in which orchestration is a **deterministic
   script** with recorded, replayable agent calls, and both forbid `Date.now()`/randomness inside it.
   OpenAI, Microsoft, Google and CrewAI all document a code-orchestrated mode alongside the
   agent-decided one, and all four recommend the code-orchestrated one when predictability matters.

So the honest form of the finding is not "multi-agent frameworks do not work." It is:

> **The category's own vendors have quietly moved the interesting part from the agents to the script
> that sequences them. Where multi-agent orchestration is documented in production, it is for
> research, support, and operations — not for writing the software a company sells. And the one
> independent measurement of these frameworks found 41%–86.7% failure rates and gains over
> single-agent baselines that are "often minimal."**

---

## Headline findings

| # | Finding | Figure | Tier | Source & date |
|---|---|---|---|---|
| 1 | First-party engineering write-ups of a general-purpose multi-agent framework **shipping application software** in production | **None found** | Emptiness finding | Directed search, 2026-08-30 |
| 2 | Largest published production code-review AI system, and its architecture | **>90% of ~65,000 weekly diffs**; "prompt-chaining-based architecture… four simpler sub-tasks"; in-house, **no orchestration framework named** | Vendor-reported (Uber, interested party) | [Uber, 2025-08-12](https://www.uber.com/us/en/blog/ureview/) |
| 3 | Measured failure rate of open-source multi-agent systems | **41% to 86.7%** across 7 frameworks; gains over single-agent "often minimal compared to single-agent frameworks or simple baselines like best-of-N sampling" | Controlled study (7 frameworks, 1,600+ annotated traces, 14 failure modes) | [arXiv:2503.13657](https://arxiv.org/abs/2503.13657), v1 2025-03-17, v3 2025-10-26 |
| 4 | Cognition's published position | "Don't Build Multi-Agents." Two principles: **"Share context, and share full agent traces, not just individual messages"**; **"Actions carry implicit decisions, and conflicting decisions carry bad results."** Recommends a **single-threaded linear agent** | First-party position (interested party — sells Devin) | [Walden Yan, Cognition, 2025-06-12](https://cognition.com/blog/dont-build-multi-agents) |
| 5 | Anthropic's published scope limit on multi-agent | **"Most coding tasks involve fewer truly parallelizable tasks than research."** Does not work where tasks require "all agents to share the same context or involve many dependencies between agents" | First-party (interested party — sells Claude) | [Anthropic, 2025-06-13](https://www.anthropic.com/engineering/multi-agent-research-system) |
| 6 | Token multiplication, multi-agent vs chat | **~15× more tokens** than chat; single agents ~**4×** chat (so ≈3.75× a single agent). Requires "tasks where the value of the task is high enough to pay for the increased performance" | Vendor-reported | [Anthropic, 2025-06-13](https://www.anthropic.com/engineering/multi-agent-research-system) |
| 7 | Token multiplication, peer-agent teams vs one session | **"approximately 7x more tokens than standard sessions when teammates run in plan mode"** | Vendor-reported | [Claude Code costs docs](https://code.claude.com/docs/en/costs), read 2026-08-30 |
| 8 | The vendor's own multi-agent performance claim, and what it was measured on | **+90.2%** over single-agent Opus 4 — on **Anthropic's internal *research* evaluation**, not a coding task | Vendor-reported, joint measurement (Opus 4 lead + Sonnet 4 subagents + Anthropic's harness) | [Anthropic, 2025-06-13](https://www.anthropic.com/engineering/multi-agent-research-system) |
| 9 | Convergent move to deterministic script orchestration, two vendors, 2026 | Devin Dynamic Workflows: "a **deterministic Python script** that orchestrates a team of Devin agents." Claude Code Dynamic Workflows: "A **script the runtime executes**"; who decides what runs next = **"The script"** | Primary artifact (both vendors' docs) | [Devin](https://docs.devin.ai/work-with-devin/dynamic-workflows.md), [Claude Code](https://code.claude.com/docs/en/workflows), read 2026-08-30 |
| 10 | Both convergent implementations ban non-determinism in the orchestration layer | Claude Code: "`Date.now()`, `Math.random()`, and a no-argument `new Date()` **throw** inside the script." Devin: logic "must not depend on the current time or date, randomness, generated IDs, environment variables, filesystem state, or network responses" | Primary artifact | Both docs, read 2026-08-30 |
| 11 | The vendor is actively **suppressing** subagent delegation on its newest model | On Opus 5 with the `claude_code` preset, "Claude Code adds a line to its system prompt telling Claude **not to call the Agent tool unless it's asked to**." Guidance: "do **not** use subagents to verify or double-check your own work" | Primary artifact / vendor guidance | [Opus 5 prompting guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5), read 2026-08-30 |
| 12 | Anthropic's framework advice, unchanged since 2024 | **"We suggest that developers start by using LLM APIs directly… If you do use a framework, ensure you understand the underlying code."** Frameworks "often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug" | First-party | [Anthropic, 2024-12-19](https://www.anthropic.com/engineering/building-effective-agents) |
| 13 | Microsoft's framework advice, in its own agent framework's overview | **"If you can write a function to handle the task, do that instead of using an AI agent."** | Primary artifact (Microsoft Learn) | [MAF overview](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview), ms.date 2026-07-29 |
| 14 | Conflicting-edit handling in the most-documented in-tool peer system | **"Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files."** No merge, no lock, no conflict detection — the mitigation is task partitioning by the human | Primary artifact | [Claude Code agent teams](https://code.claude.com/docs/en/agent-teams), read 2026-08-30 |
| 15 | Status of that peer system | **Experimental and disabled by default** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`), with published limitations including **no session resumption** for in-process teammates and task status that "can lag" | Primary artifact | Same, read 2026-08-30 |
| 16 | Framework consolidation, established | **AutoGen is in maintenance mode**, "will not receive new features," directs new users to Microsoft Agent Framework as "the enterprise-ready successor." **Semantic Kernel "is now Microsoft Agent Framework."** MAF is "the direct successor" to both, "created by the same teams," at **1.0 with stable APIs** | Primary artifact (READMEs + Learn docs) | [autogen README](https://raw.githubusercontent.com/microsoft/autogen/main/README.md), [semantic-kernel README](https://raw.githubusercontent.com/microsoft/semantic-kernel/main/README.md), [MAF overview](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview) |
| 17 | AG2 fork status | AG2 is a fork of AutoGen ("modifications and additions made in this fork are licensed under the Apache License, Version 2.0"). **AG2 v1.0 is a rewrite, not a continuation**: "AG2 Classic" moved to `ag2ai/ag2-classic`, and "AG2 v1.0 (`pip install ag2`) is **not** a drop-in upgrade from Classic" | Primary artifact | [ag2 README](https://raw.githubusercontent.com/ag2ai/ag2/main/README.md), read 2026-08-30 |
| 18 | Swarm status | **"Swarm is now replaced by the OpenAI Agents SDK"**; Swarm is "experimental, educational," and "We recommend migrating to the Agents SDK for all production use cases" | Primary artifact | [swarm README](https://raw.githubusercontent.com/openai/swarm/main/README.md), read 2026-08-30 |
| 19 | What OpenAI Agents SDK sessions actually persist | **Conversation history only.** Documented resumption covers *approval* pauses, not crashes: no execution state, no in-flight tool calls, no crash-recovery guarantee | Primary artifact | [Agents SDK sessions](https://openai.github.io/openai-agents-python/sessions/), read 2026-08-30 |
| 20 | LangGraph's resume semantics, stated caveat | On resume after `interrupt()`, **"the runtime restarts the entire node from the beginning — it does not resume from the exact line."** Therefore "side effects called before `interrupt` should (ideally) be idempotent" | Primary artifact | [LangGraph interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts), read 2026-08-30 |
| 21 | The one framework family with a real crash guarantee | Temporal: "If the Worker crashes, the Worker uses the Event History to **replay** the code and recreate the state… **as if the failure never occurred**" | Primary artifact | [Temporal](https://docs.temporal.io/evaluate/understanding-temporal), read 2026-08-30 |
| 22 | Origin of "flow engineering" in this project's vocabulary | AlphaCodium: "a test-based, multi-stage, code-oriented iterative flow." **GPT-4 + direct prompt: 19% pass@5; GPT-4 + AlphaCodium flow: 44% pass@5** on CodeContests validation — a joint model+flow measurement, not a model property | Controlled study (single benchmark, 2024 model) | [arXiv:2401.08500](https://arxiv.org/abs/2401.08500), 2024-01-16, CodiumAI |
| 23 | LangGraph's named users, from its own README | **Klarna, Replit, Elastic** — the README names no system built by any of them, and no dates | Vendor marketing | [langgraph README](https://raw.githubusercontent.com/langchain-ai/langgraph/main/README.md), read 2026-08-30 |
| 24 | LangChain's customer page, screened for software-engineering systems | 11 named customers; **exactly one** (Cisco Outshift's "AI Platform Engineer") is a software/platform-engineering system. The rest are research, support, GTM, clinical, travel, monitoring | Vendor marketing | [langchain.com/customers](https://www.langchain.com/customers), read 2026-08-30 |
| 25 | The best-evidenced multi-agent system doing engineering work in production | Cisco Outshift's **JARVIS → CAIPE**: "automated around a third of its internal platform engineering tasks," incident response "from hours to seconds" — **platform operations, not application code** | Vendor-reported; the article body itself did not render (see Blocked sources) | Outshift/Cisco, search result 2026-08-30; [CAIPE repo](https://github.com/cnoe-io/ai-platform-engineering) Apache-2.0 |

---

## Part A — General-purpose agent-building frameworks

### A.1 What the category actually contains, as of 2026-08-30

The category has consolidated hard since 2024. Establishing the fork-and-merge status matters
because a lot of secondary writing still treats retired projects as live options.

| Project | Status | Established from |
|---|---|---|
| **OpenAI Swarm** | **Retired.** "Swarm is now replaced by the OpenAI Agents SDK, which is a production-ready evolution of Swarm." Kept as "an educational resource" | [swarm README](https://raw.githubusercontent.com/openai/swarm/main/README.md) |
| **OpenAI Agents SDK** | Live. Swarm's primitives (Agents, handoffs) plus sessions, input/output validation, tracing | [Agents SDK docs](https://openai.github.io/openai-agents-python/) |
| **microsoft/autogen** | **Maintenance mode**, community-managed, "will not receive new features or enhancements." Directs new users to Microsoft Agent Framework | [autogen README](https://raw.githubusercontent.com/microsoft/autogen/main/README.md) |
| **AG2** | Community fork of AutoGen. **v1.0 is a rewrite**, protocol-driven; the AutoGen-derived code is now "AG2 Classic" in a separate repo and v1.0 is "**not** a drop-in upgrade" | [ag2 README](https://raw.githubusercontent.com/ag2ai/ag2/main/README.md) |
| **Semantic Kernel** | **Superseded.** "Semantic Kernel is now Microsoft Agent Framework" | [semantic-kernel README](https://raw.githubusercontent.com/microsoft/semantic-kernel/main/README.md) |
| **Microsoft Agent Framework (MAF)** | Live, **1.0, "stable APIs, and a commitment to long-term support."** "Combines AutoGen's simple abstractions… with Semantic Kernel's enterprise-grade features… The Agent Framework is the direct successor, created by the same teams." .NET, Python, Go (Go in public preview) | [MAF overview](https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview), ms.date 2026-07-29, updated 2026-08-25 |
| **LangGraph** | Live. Explicit-graph. Checkpointers, `interrupt()`, time travel | [langgraph docs](https://docs.langchain.com/oss/python/langgraph/persistence) |
| **CrewAI** | Live, and **internally split**: Crews (agent autonomy) vs Flows (explicit control flow) | [crewai docs](https://docs.crewai.com/en/concepts/flows) |
| **Google ADK** | Live. LLM agents plus **template workflow agents** (Sequential, Parallel, Loop) | [adk.dev](https://adk.dev/agents/workflow-agents/) |
| **Claude Agent SDK** | Live. Subagents via `AgentDefinition`, plus a `Workflow` tool for script orchestration | [Agent SDK subagents](https://code.claude.com/docs/en/agent-sdk/subagents) |
| **LlamaIndex Workflows** | Live. Event-driven `@step` functions; "Branches are ordinary `if` statements that return different event types" | [llamaindex docs](https://developers.llamaindex.ai/python/framework/understanding/workflows/) |
| **Pydantic AI** | Live. **Delegates durability to four external engines**: Temporal, DBOS, Prefect, Restate | [pydantic ai](https://pydantic.dev/docs/ai/integrations/durable_execution/overview/) |
| **Mastra** | Live. TypeScript; `.then()`/`.commit()` chaining, `resumeStream`, restart "from the last active step" | [mastra docs](https://mastra.ai/docs/workflows/overview) |
| **smolagents** | Live, deliberately minimal — "the main code in `agents.py` has <1,000 lines of code." Core claim: actions as executable Python rather than JSON tool calls, **"30% fewer steps (thus 30% fewer LLM calls)"** `[vendor-reported]` | [smolagents README](https://raw.githubusercontent.com/huggingface/smolagents/main/README.md) |
| **DSPy** | **Not in this category.** "The framework for *programming—rather than prompting—language models*," an optimizer/compiler for LM programs. Its README makes **no mention of multi-agent orchestration**. It is frequently mislabelled as an agent framework | [dspy README](https://raw.githubusercontent.com/stanfordnlp/dspy/main/README.md) |
| **Temporal** | Not an agent framework — a durable execution engine used *underneath* them | [temporal docs](https://docs.temporal.io/evaluate/understanding-temporal) |

### A.2 The control-flow question: three structural families

This is the axis the project's vocabulary already distinguishes. **Agent orchestration** is the
discipline of structuring work across agent steps. **Flow engineering** is the narrower practice of
encoding the control flow explicitly rather than leaving sequencing to the agent's judgement. Sorted
by that axis, the frameworks fall into three families, and *every major vendor now ships both an
agent-decided and a code-decided mode.*

**Family 1 — Explicit graph / explicit script (flow engineering).** The developer writes the
control flow; the model fills in the steps.

- **LangGraph.** Nodes and edges; the graph is the program. State is checkpointed per super-step.
- **Google ADK template workflow agents.** The cleanest statement of the property in any vendor's
  docs: *"Template workflow agents operate based on predefined logic. They determine the execution
  sequence according to their type, such as sequential, parallel, or loop, **without consulting an
  AI model** for assistance with the orchestration. This approach results in **deterministic and
  predictable execution patterns**."*
- **CrewAI Flows.** `@start`, `@listen`, `@router`, `and_()`, `or_()`. The docs frame the split
  explicitly: Flows are "developer-directed orchestration" versus Crews' "agent autonomy."
- **MAF Workflows.** "explicit, inspectable execution paths"; graph API (`WorkflowBuilder`,
  executors, typed edges) and, in Python, a functional API using "native Python (`if`, loops,
  `asyncio.gather`)".
- **LlamaIndex Workflows, Mastra, Shopify's Roast** (Ruby DSL, declarative step composition).
- **Devin Dynamic Workflows and Claude Code Dynamic Workflows** — see A.3 and B.4; these are the
  2026 arrivals and the most consequential ones.

*Structurally permits:* deterministic replay, per-step evaluation, cost bounding, targeted retry,
static inspection of what will happen before it happens.
*Structurally forbids:* the model discovering a plan shape the author did not anticipate. If the
task's shape is genuinely unknown up front, the graph is a guess.

**Family 2 — Role and delegation based.** A manager agent, or a speaker-selection policy, decides
who acts next at runtime.

- **CrewAI Crews.** Two processes: *Sequential* — "Tasks are executed one after another"; and
  *Hierarchical* — "A manager agent coordinates the crew, delegating tasks and validating outcomes
  before proceeding," which requires a `manager_llm` or `manager_agent`. The routing decision is an
  LLM call.
- **AutoGen / AG2 group chat**, and **MAF's Group Chat and Magentic** patterns — MAF describes
  Magentic as "A manager agent **dynamically** coordinates specialized agents."

*Structurally permits:* emergent decomposition; adding a specialist without rewriting a graph.
*Structurally forbids:* knowing in advance how many model calls a run will make, or bounding cost.
This is the family the MAST study measured, and where its "inter-agent misalignment" failure category
lives.

**Family 3 — Handoff based.** Control transfers laterally between peers, and the transfer itself is
a tool call the model chooses.

- **OpenAI Agents SDK.** *"Handoffs are represented as tools to the LLM. So if there's a handoff to
  an agent named `Refund Agent`, the tool would be named `transfer_to_refund_agent`."* By default
  the receiving agent "gets to see the entire previous conversation history"; `input_filter` narrows
  it. **The model decides** — "let the model choose among them."
- **MAF Handoff:** "Agents transfer control to each other based on context."

*Structurally permits:* full context transfer by default, which is precisely what Cognition argues
for; a flat topology with no coordinator to become a bottleneck.
*Structurally forbids:* parallelism (a handoff is a transfer, not a fork), and any static guarantee
about where control ends up.

**The important finding about this taxonomy is that the vendors do not defend it.** OpenAI's own
multi-agent guidance separates "orchestrating via LLM" from "orchestrating via code" and says code
orchestration "makes tasks more deterministic and predictable, **in terms of speed, cost and
performance**"
([Agents SDK](https://openai.github.io/openai-agents-python/multi_agent/), read 2026-08-30).
Google's ADK says the workflow agents avoid "consulting an AI model… for the orchestration."
CrewAI ships Flows alongside Crews. Microsoft's MAF overview goes furthest: *"If you can write a
function to handle the task, do that instead of using an AI agent."*

### A.3 Durability and failure semantics

This is the property that separates a demo from something that can run unattended, and the
frameworks differ far more here than their marketing suggests.

| Framework | What is persisted | What happens on crash mid-run | Determinism constraint |
|---|---|---|---|
| **Temporal** | Event History: "a complete and durable log of everything that has happened in the lifecycle of a Workflow Execution" | **"If the Worker crashes, the Worker uses the Event History to replay the code and recreate the state… It then resumes progress from the point of failure as if the failure never occurred."** | Replay implies workflow code must be deterministic; the *Understanding Temporal* page names the mechanism but does not enumerate the constraints |
| **LangGraph** | Checkpoints per thread, per super-step. `InMemorySaver` (lost on restart), `SqliteSaver`, `PostgresSaver`/`AsyncPostgresSaver` | Resume from the last checkpoint. **But: "the runtime restarts the entire node from the beginning — it does not resume from the exact line where `interrupt` was called."** | Documented consequence: "side effects called before `interrupt` should (ideally) be idempotent"; guidance is to move side effects after the interrupt or into their own node |
| **Pydantic AI** | Delegated: Temporal, DBOS, Prefect, Restate (plus Kitaru, Airflow) | Whatever the chosen engine guarantees. Pydantic AI's own claim is that agents "preserve their progress across transient API failures and application errors or restarts" | Inherited from the backend |
| **MAF** | Checkpoints **at superstep boundaries** (graph API) or per-`@step` result caching (functional API). Human-in-the-loop via `RequestInfoExecutor` / `ctx.request_info()` | Documented as "durability and restartability" and "time-travel debugging"; per-pattern detail lives in the capability pages | Not stated on the concepts page |
| **CrewAI Flows** | `@persist` decorator, `SQLiteFlowPersistence` default; "resume" (same UUID) and "fork" (new state ID) modes | "automatic state recovery after system failures or restarts" via "transaction-based state updates" | Not stated |
| **OpenAI Agents SDK** | **Conversation history only.** Ten session backends (SQLite, Redis, SQLAlchemy, MongoDB, Dapr, OpenAI-hosted, encrypted, compacting…) | **Nothing.** The documented resume path is for *approval* pauses — "If a run pauses for approval, resume it with the same session instance." No crash-recovery guarantee, no in-flight tool-call state | N/A |
| **Claude Agent SDK / Claude Code subagents** | Subagent transcripts persist "in separate files… independently of the main conversation"; resume by `agentId` + `resume: sessionId` | A resumed subagent "retains its full conversation history." An **API error that ends a subagent early "is never delivered as its result"** | N/A |
| **Claude Code Dynamic Workflows** | Every `agent()` result is recorded by the runtime | Replay in start order: completed agents return saved results; **"a failure in the middle of a fan-out reruns work that already finished"** — if A, B, C, D started in that order and B fails, A is cached and B, C, D all run again | **Enforced**: `Date.now()`, `Math.random()`, and no-argument `new Date()` **throw** inside the script |
| **Devin Dynamic Workflows** | "Every agent call is recorded, so a workflow run is observable while it executes and **resumable if it is interrupted**: completed agents replay their recorded results instantly, and only the unfinished work runs again" | As above | **Enforced by rule**: logic "must not depend on the current time or date, randomness, generated IDs, environment variables, filesystem state, or network responses" |
| **Mastra** | Snapshot/persistence referenced; `resumeStream`; restart "from the last active step" | Partial: reconnects a stream, restarts a step | Not stated |

**Three honest conclusions from this table.**

1. **Only Temporal makes an unconditional crash guarantee**, and it makes it because durable
   execution is the whole product rather than a feature bolted onto an agent library. Pydantic AI's
   design decision — to have no durability of its own and integrate four external engines instead —
   is the most intellectually honest position in the category.
2. **"Checkpointing" is not resumption.** LangGraph's node-level replay and Claude Code's fan-out
   replay both re-execute work that already completed. For a *research* agent that is wasteful; for
   a *coding* agent that has already written files, run migrations, or opened a PR, re-execution is
   a correctness problem, and the documented mitigation in both cases is the same: **make the side
   effects idempotent yourself**. That obligation lands on the team building the harness.
3. **Human-in-the-middle interrupts are well supported and structurally distinct from crash
   recovery.** LangGraph's `interrupt()`, MAF's `RequestInfoExecutor`, the Agents SDK's approval
   pause, and CrewAI's persistence all handle *planned* pauses. None of them handle a worker dying.
   Documents that treat these as the same property are wrong.

### A.4 What building the harness buys, and what it costs

**What it buys, on the evidence:**

- **Control flow you can read.** Every code-orchestrated mode in the category exists because
  somebody wanted to see the plan before it ran. Claude Code's own comparison table makes the claim
  concrete: with subagents "Claude, turn by turn" decides what runs next and intermediate results
  live in "Claude's context window"; with a workflow "The script" decides and results live in
  "Script variables," so "Claude's context holds only the final answer."
- **Cost bounding.** `max_budget_usd`, `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`,
  `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`, the 1,000-agents-per-run cap. None of these are available
  to you if the model decides the topology.
- **Repeatability.** Claude Code: "What's repeatable" — for subagents, "The worker definition"; for
  workflows, "**The orchestration itself**."
- **A measured effect when the flow is the point.** AlphaCodium remains the cleanest demonstration:
  GPT-4 + direct prompt reaches 19% pass@5 on CodeContests validation; **GPT-4 + the AlphaCodium
  flow reaches 44%** — same model, different flow. Report it as a joint measurement; it is a
  property of model-plus-flow, on one benchmark, with a 2024 model.

**What it costs, stated plainly:**

- **You now maintain an agent harness alongside your actual product**, and the harness is coupled to
  model behaviour that changes underneath you. The clearest evidence is Anthropic's own migration
  advice for Opus 5: *"If your prompt contains explicit verification instructions… remove them:
  instructions like these cause over-verification on Claude Opus 5… **The same applies to legacy
  harness scaffolding that adds separate verification steps.**"* A harness that was correct for the
  previous model is now a cost centre.
- **You inherit an abstraction you may not be able to debug.** Anthropic's position from 2024-12-19
  has not been retracted: frameworks "often create extra layers of abstraction that can obscure the
  underlying prompts and responses, making them harder to debug," and the recommendation is to start
  with the API directly.
- **You inherit consolidation risk.** In under two years this category retired Swarm, put AutoGen in
  maintenance mode, superseded Semantic Kernel, and forked AG2 twice (fork, then a v1.0 that is "not
  a drop-in upgrade from Classic"). A team that built on any of those in 2024 has migrated or is
  migrating.
- **You inherit the failure modes the framework has.** MAST's taxonomy — specification and system
  design, inter-agent misalignment, task verification and termination — are properties of the
  architecture, and the paper's conclusion is that "identified failures require more sophisticated
  solutions" than prompt or orchestration tweaks. Its own best tactical interventions on ChatDev
  gained **+9.4%** (a CEO final-approval step) and **+15.6%** (high-level objective verification) —
  real, but not the difference between 41%–86.7% failure and working.

---

## Part B — Multi-agent features inside coding tools

The same structural questions, asked of the products rather than the libraries. The important
observation is that **the coding tools are not, mostly, multi-agent systems in the (a) sense.** Most
of what is marketed as multi-agent in a coding tool is *context isolation with a summary return* —
a single orchestrator, fan-out workers, no peer communication.

### B.1 Subagents: context isolation, not collaboration

| Tool | Own context window | What returns to parent | Nesting | Peer communication |
|---|---|---|---|---|
| **Claude Code** | Yes — "starts with a fresh, isolated context window. It doesn't see your conversation history, the skills you've already invoked, or the files Claude has already read." A *fork* is the exception: it "inherits the entire conversation so far" | **Only the final message**, as the Agent tool result. Since v2.1.210 that message is scanned for instruction-shaped patterns before the parent reads it | Yes, default depth **3**, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | Yes, via `SendMessage` to *named* subagents |
| **Claude Agent SDK** | Same engine; `AgentDefinition` with `tools`, `model`, `skills`, `maxTurns`, `permissionMode`, `background` | Same | Same | Same |
| **Amp** | "Each subagent has its own context window and access to tools." Five specialists (Review, Search, Oracle, Librarian, Read Thread) | "The main agent only receives their final summary rather than monitoring their step-by-step work" | Not documented | **No** — "they work in isolation, so they can't communicate with each other" |
| **Devin CLI** | "operates in its own conversation chain — it does not inherit the parent's conversation history" (but shares tools and codebase context) | "You do not see the subagent's raw output directly… the parent agent reads the result and summarizes" | **No by default** — "only the root agent can" spawn | Not documented |
| **Roo Code (Boomerang / Orchestrator mode)** | "Each subtask operates in complete isolation with its own conversation history. It does not automatically inherit the parent's context" | "a concise summary" only | Not documented | Not documented |

Amp is explicit about the trade-off subagents make: you "cannot guide them mid-task, and they start
with the instructions and context the main agent gives them rather than the full conversation."
That is exactly the property Cognition's argument targets.

**Cline is not in this table, and should not be.** Plan mode and Act mode are two modes of one agent:
"The conversation history carries over when you switch modes." A different model can be configured
per mode, but there is one context and one thread. Calling it multi-agent is a category error.

### B.2 Peer sessions: the only genuinely multi-agent feature in a mainstream coding tool

**Claude Code agent teams** are the one in-tool feature where agents message each other directly and
claim work from a shared list rather than reporting to an orchestrator. It is also, by a wide margin,
the most candid vendor document found in this entire strand:

- **Experimental and off by default.** Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.
- **When not to use it:** "Agent teams add coordination overhead and use significantly more tokens
  than a single session… For **sequential tasks, same-file edits, or work with many dependencies**,
  a single session or subagents are more effective."
- **Conflicting edits are unsolved:** "Two teammates editing the same file leads to overwrites.
  Break the work so each teammate owns a different set of files."
- **Diminishing returns are acknowledged:** "beyond a certain point, additional teammates don't speed
  up work proportionally." Recommended team size: **3–5**.
- **Start with work that isn't code:** "If you're new to agent teams, start with tasks that have
  clear boundaries and don't require writing code: reviewing a PR, researching a library, or
  investigating a bug. These tasks show the value of parallel exploration **without the coordination
  challenges that come with parallel implementation**."
- **Unattended running is discouraged:** "Letting a team run unattended for too long increases the
  risk of wasted effort."
- **A human-oversight gap worth naming:** when a teammate finishes planning, "Claude Code approves
  the plan in the lead's session as soon as the request arrives, **without the lead reviewing it**."
  Tool permission prompts still surface to the human; plan approval does not.
- **Published limitations include:** no session resumption for in-process teammates; task status
  "can lag," blocking dependent tasks; no nested teams; permissions fixed at spawn.

Architecture is a JSON mailbox per agent under `~/.claude/teams/{team}/inboxes/`, plus a shared task
list with **file locking** for claim races. Messages between agents are treated as untrusted: "a
teammate can't approve a permission prompt or supply consent on your behalf, and a teammate that was
denied an action can't relay it to another teammate to bypass the check."

**Cursor** offers parallel agents with the isolation mechanism named: "Parallel agents: run many
parallel agents in the cloud"; "Worktrees: run agents in isolated Git checkouts so each task has its
own files and changes." The docs found state the mechanism but publish no limits, merge strategy, or
conflict semantics.

### B.3 Worktrees: the field's actual answer to conflicting edits

Across every tool that runs agents in parallel on one repository, the isolation mechanism is the
same and it is not new: **a separate git working directory per agent**. Cursor uses worktrees for
parallel agents. Claude Code has `--worktree`, `EnterWorktree`/`ExitWorktree` tools, and
`isolation: worktree` frontmatter on a subagent definition.

What is notable in Claude Code's implementation is that isolation is **enforced by the harness, not
by convention** — four checks block a worktree-isolated session from touching the main checkout:
file edits targeting it, commands whose working directory resolves to it, git redirects
(`git -C`, `--git-dir`, `GIT_DIR`, `GIT_WORK_TREE`, or a `cd` before git), and commands whose shape
the harness cannot verify (brace expansion, heredocs with unquoted delimiters). "You can't turn this
check off."

The limit of the mechanism is equally clear: **worktrees isolate file edits and nothing else.** They
do not merge, they do not detect semantic conflict, and the branches still have to be reconciled by
something. Nothing in any vendor's documentation claims otherwise.

### B.4 The 2026 convergence: orchestration as a deterministic script

This is the most significant finding in Part B, and it is a convergence between two vendors who
disagree publicly about multi-agent architecture.

**Cognition — the company that published "Don't Build Multi-Agents" — now ships multi-agent
orchestration in Devin.** But: "a dynamic workflow is a **deterministic Python script** that
orchestrates a team of Devin agents." Primitives: `agent()`, `pipeline()`, `parallel()`,
`register_workflow()`. Determinism is mandatory. Every agent call is recorded and replayed on resume.
Devin writes the script; the *script*, not an agent, then decides the sequence.

**Anthropic ships the same shape in Claude Code and the Agent SDK.** "A dynamic workflow is a
JavaScript script that orchestrates many subagents at once." Primitives: `agent()`, `pipeline()`,
`parallel()`, plus `phase()` and `log()`. Determinism is enforced by making `Date.now()`,
`Math.random()` and `new Date()` throw. Runtime caps: **16 concurrent agents**, **4,096 items per
`parallel()`/`pipeline()` call**, **1,000 agents per run**, with a `Large workflow` warning at
**>25 agents or >1.5M projected tokens**.

The two implementations arrived independently at the same primitive names, the same determinism ban,
and the same record-and-replay resumption. That is strong convergent evidence about where the
category's working answer actually is — and the shared answer is **flow engineering**, not agent
autonomy.

Anthropic states the reason for the shape directly: "A workflow moves the plan into code. With
subagents, skills, and agent teams, Claude is the orchestrator: it decides turn by turn what to spawn
or assign next, and every result lands in a context window. A workflow script holds the loop, the
branching, and the intermediate results itself."

---

## Part C — The reality check

### C.1 What was found

**Production systems built on multi-agent frameworks, named, with a named system:**

- **Cisco Outshift — JARVIS, now open-sourced as CAIPE** (Community AI Platform Engineering,
  Apache-2.0, `cnoe-io/ai-platform-engineering`, under the CNOE Agentic AI Community). LangGraph-
  based multi-agent system for platform engineering: Jira, CI/CD bootstrap, Kubernetes config, a
  Backstage chat assistant. Reported: **"automated around a third of its internal platform
  engineering tasks"**, incident response "from hours to seconds." `[vendor-reported]` This is
  **platform and infrastructure operations, not writing the software Cisco sells.**
- **Uber — Genie (on-call copilot, agentic RAG) and Finch (conversational financial data agent)**,
  both stated to use LangGraph; plus an internal agent platform built in early 2025 that is
  "orchestration-framework agnostic" and "has been adopted by thousands of internal agents"
  ([Uber, 2026-05-21](https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/)). The one
  multi-agent example given in that post is **incident response**: an Oncall Agent delegating to an
  Investigation Agent which coordinates with a Monitoring Agent to change alert thresholds via a
  pull request. Again: operations, adjacent to software but not shipping it.
- **LangGraph's own README** names **Klarna, Replit, Elastic** with no system named for any of them.
  `[vendor marketing]`

**Production software-engineering AI at the largest published scale, and what it is not:**

**Uber's uReview** is the single most quantified production software-engineering AI system found in
this strand — and it is a deliberate counterexample to the multi-agent thesis:

- Architecture: **"Its prompt-chaining-based architecture breaks down the code-review task into four
  simpler sub-tasks… comment generation, filtering, validation, and deduplication."**
- Framework: **in-house.** No LangGraph, no CrewAI, no orchestration library named.
- Scale: processes **over 90% of ~65,000 weekly diffs**; **75%** of comments marked useful; **65%**
  of posted comments addressed in the same changeset; median 4 minutes per commit; ~1,500 developer
  hours saved weekly. `[vendor-reported — Uber is an interested party]`
- The authors' own conclusion about what mattered: **"Prompt design helped, but system architecture,
  and post-processing were even more critical."**

That is flow engineering with an aggressive verification stage, built without a framework, at a scale
none of the framework case studies approach.

**A first-party artifact from a company that ships software, built for its own code work:**
**Shopify's Roast** — "a Ruby-based domain-specific language for creating structured AI workflows,"
composing "cogs" in declarative sequence (`cmd(:recent_changes)` → `agent(:review)` →
`chat(:summary)`). Explicit developer-defined control flow. `[primary artifact]` The README publishes
no production figures and no philosophy statement, so it evidences the *shape* of what a software
company builds, not its results.

### C.2 What was not found — the emptiness findings

Each of these is the result of a directed search, not an absence of looking.

1. **No first-party engineering write-up in which LangGraph, CrewAI, AutoGen/AG2, the OpenAI Agents
   SDK, MAF, or ADK writes and ships application software in production.** The named systems are
   support, research, GTM, clinical, monitoring, travel, financial Q&A, incident response, and
   platform operations.
2. **No published postmortem of a multi-agent coding system.** Nothing first-party was found. The
   nearest published incident material lives in secondary and practitioner blogs, which this strand
   excludes.
3. **No head-to-head production comparison of a multi-agent framework against a single-agent
   baseline on a software-engineering workload by anyone.** The only rigorous comparison found is
   MAST's, which is on benchmarks, and its finding is negative.
4. **No framework publishes a cost figure for its own multi-agent mode.** Every token multiplier in
   this document comes from a *model vendor* (Anthropic), not from LangChain, CrewAI, Microsoft,
   Google, or OpenAI. The frameworks that most encourage fan-out publish nothing about what fan-out
   costs.
5. **No framework publishes an accuracy or reliability figure for its orchestration layer.**

### C.3 First-party evidence *against* multi-agent architectures

This is the part of the record most often omitted from writing about this category.

**Cognition, 2025-06-12, "Don't Build Multi-Agents" (Walden Yan).** Two principles, quoted:

> 1. "Share context, and share full agent traces, not just individual messages"
> 2. "Actions carry implicit decisions, and conflicting decisions carry bad results"

The argument names OpenAI's Swarm and Microsoft's AutoGen as promoters of the pattern it rejects.
The worked example: two subagents build incompatible halves of a Flappy Bird clone because each
resolves an ambiguity in the shared task differently, and no coordinator can reconcile the result
afterwards. The recommendation is "a single-threaded linear agent," with an LLM "history compressor"
for long tasks — and the caveat that "this is hard to get right." The post cites Claude Code's
sequential (non-parallel) subtask agents approvingly. Its own conclusion is that multi-agent
collaboration was premature in 2025, "awaiting better cross-agent communication capabilities."

**Anthropic, 2025-06-13, "How we built our multi-agent research system."** The pro-multi-agent post
in the record — and it draws the boundary itself. Multi-agent is for "heavy parallelization,
information that exceeds single context windows, and interfacing with numerous complex tools." It is
**not** for tasks requiring "all agents to share the same context or involve many dependencies
between agents," and the coding statement is explicit: **"Most coding tasks involve fewer truly
parallelizable tasks than research."** Documented failure modes include spawning 50+ subagents for
simple queries, duplicated work from poorly defined task boundaries, and "agent distraction through
excessive mutual updates."

**Anthropic, 2026, Opus 5 guidance.** The most recent and most pointed signal. Delegation "multiplies
cost and time when applied to small tasks." The recommended prompt text: *"Delegate to a subagent
only for large tasks that are genuinely independent and parallelizable… **Do not delegate work you
can finish yourself in a handful of tool calls, and do not use subagents to verify or double-check
your own work.** If one subagent can complete the task, use one rather than several."* And Claude
Code, on Opus 5 with its own system-prompt preset, "adds a line to its system prompt telling Claude
**not to call the Agent tool unless it's asked to.**" The same guide's positive multi-agent claim —
"Claude Opus 5 coordinates teams of subagents well, with effective writer-verifier patterns and few
cases of agents overwriting each other's work" — carries **no figure**, so treat it as an
unquantified vendor claim.

**arXiv:2503.13657, "Why Do Multi-Agent LLM Systems Fail?" (Cemri, Pan, Yang, Agrawal, Chopra,
Tiwari, Keutzer, Parameswaran, Klein, Ramchandran, Zaharia, Gonzalez, Stoica; UC Berkeley et al.;
v1 2025-03-17, v3 2025-10-26).** `[controlled study]` The strongest independent evidence in this
strand. Seven open-source multi-agent systems — **ChatDev, MetaGPT, HyperAgent, AppWorld, AG2
(MathChat), Magentic-One, OpenManus** — three of which are software-engineering systems. 1,600+
annotated traces, 150 analysed to build a taxonomy of **14 failure modes** in **3 categories**
(system design, inter-agent misalignment, task verification). Findings:

- **"41% to 86.7% failure rate on 7 state-of-the-art open-source MAS."**
- **"their performance gains often remain minimal compared to single-agent frameworks or simple
  baselines like best-of-N sampling."**
- Best tactical interventions on ChatDev: **+9.4%** and **+15.6%** — and the paper's own conclusion
  is that "identified failures require more sophisticated solutions."

**Two structural cautions on citing this study:** it is a 2025 study on 2025-era models, and the
systems studied are open-source research artifacts rather than the commercial harnesses this document
covers elsewhere. It is the best available independent measurement, not the last word.

---

## Part D — What this category structurally cannot do

Each item is grounded in a vendor's own documentation, not inferred.

1. **Share context between agents without paying for it twice.** Isolation is the point — Claude
   Code: "starts with a fresh, isolated context window"; Roo Code: "complete isolation"; Amp: "they
   work in isolation, so they can't communicate with each other"; Devin CLI: "does not inherit the
   parent's conversation history." Everything the subagent needs must be restated in its prompt, and
   everything it learned comes back as one summary. Cognition's principle 1 is precisely the claim
   that this loses the information that mattered.
2. **Resolve conflicting edits.** No vendor claims to. The published mitigations are *partition the
   work by file* (Claude Code agent teams) and *isolate the filesystem* (worktrees, everywhere). Both
   push the reconciliation onto a human or onto git.
3. **Bound cost without an explicit cap.** "Once you include `Agent` in `allowedTools`, Claude
   decides on its own when to spawn a subagent and how many to spawn… **one prompt can grow into a
   tree of agents.**" The caps exist because the topology is otherwise unbounded.
4. **Give you a debuggable trace by default.** Anthropic's 2024 warning about frameworks obscuring
   "the underlying prompts and responses" is why every 2026 script-orchestration feature writes its
   script to a readable file and exposes a per-agent progress view. Debuggability had to be
   engineered back in.
5. **Be deterministic while the orchestration is model-decided.** This is definitional, and both
   2026 script-orchestration implementations resolve it by *removing the model from the
   orchestration layer* and banning non-determinism in the script.
6. **Be evaluated as a unit.** No framework in this strand publishes an eval story for its
   orchestration layer. MAST had to build a human-annotated taxonomy from 1,600 traces precisely
   because no such measurement existed. Note the vocabulary distinction: this is an **eval harness**
   gap, and it is separate from the **agent harness** the team is building.
7. **Survive a crash mid-run without idempotent side effects.** LangGraph re-runs the whole node;
   Claude Code re-runs everything after a failed fan-out member; the OpenAI Agents SDK persists no
   execution state at all. For a coding agent, "re-run" means re-editing files.

---

## Part E — Cost and token multiplication

Every first-party published figure found. **All are vendor-reported by the model vendor**; no
framework author publishes any.

| Figure | Comparison | Source & date |
|---|---|---|
| **~15×** | Multi-agent system vs standard chat | [Anthropic, 2025-06-13](https://www.anthropic.com/engineering/multi-agent-research-system) |
| **~4×** | Single agent vs standard chat (implying multi-agent ≈ **3.75×** a single agent) | Same |
| **~7×** | Claude Code agent teams vs a standard session, "when teammates run in plan mode" | [Claude Code costs](https://code.claude.com/docs/en/costs), read 2026-08-30 |
| **Linear in team size** | "Token costs scale linearly: each teammate has its own context window and consumes tokens independently"; "token usage is roughly proportional to team size" | [Claude Code agent teams](https://code.claude.com/docs/en/agent-teams) |
| **>25 agents or >1.5M projected tokens** | Threshold at which Claude Code shows a `Large workflow` warning (advisory only — "it doesn't pause or limit the run") | [Claude Code workflows](https://code.claude.com/docs/en/workflows) |
| **16 / 4,096 / 1,000** | Concurrent agents / items per `parallel()` or `pipeline()` call / agents per workflow run | Same |
| **20 / depth 3** | Default concurrent subagent limit / default subagent nesting depth | [Agent SDK subagents](https://code.claude.com/docs/en/agent-sdk/subagents) |
| **$13/dev/active day, $150–250/dev/month** | Baseline single-agent coding cost across enterprise deployments — the denominator any multiplier applies to | [Claude Code costs](https://code.claude.com/docs/en/costs) |
| **"cost scales with the number of subagents"** | Devin CLI, no figure: "Subagents run as their own agent sessions, each with its own context window and inference calls, so they consume cost independently of the parent" | [Devin CLI subagents](https://docs.devin.ai/cli/subagents.md) |
| **30% fewer LLM calls** | smolagents' code-actions claim vs JSON tool calls — an efficiency claim *within* one agent, not a multi-agent figure | [smolagents README](https://raw.githubusercontent.com/huggingface/smolagents/main/README.md) |

**One partial mitigation worth recording**, because it is the only published mechanism that makes
fan-out cheaper rather than just bounded: agents in the same Claude Code workflow run "can read each
other's prompt cache" when they share model, effort, agent type, tools, output schema and working
directory, and the runtime deliberately staggers a fan-out (default 5,000 ms,
`CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS`) so siblings read the first agent's cached prefix instead of
each processing it uncached. Subagent caches also fall outside the main conversation's TTL bucket —
**five minutes by default**, an hour only if `subagentPromptCacheTtl` is set to `1h`, which the API
bills at a higher write rate.

**The economic conclusion the sources support:** multi-agent is a way of *buying* wall-clock time and
context headroom with tokens. Anthropic states the condition for that trade being worth it —
"tasks where the value of the task is high enough to pay for the increased performance" — and its
own coding guidance says most coding tasks do not meet it.

---

## Sources

**First-party positions and engineering write-ups**

- Cognition (Walden Yan), *Don't Build Multi-Agents*, 2025-06-12 — https://cognition.com/blog/dont-build-multi-agents
- Anthropic, *How we built our multi-agent research system*, 2025-06-13 — https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic, *Building effective agents*, 2024-12-19 — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, *Effective context engineering for AI agents*, 2025-09-29 — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Uber, *uReview: Scalable, Trustworthy GenAI for Code Review*, 2025-08-12 — https://www.uber.com/us/en/blog/ureview/
- Uber, *Solving the Identity Crisis for AI Agents*, 2026-05-21 — https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/

**Peer-reviewed / preprint**

- Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, arXiv:2503.13657, v1 2025-03-17 / v3 2025-10-26 — https://arxiv.org/abs/2503.13657
- Ridnik, Kredo, Friedman (CodiumAI), *Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering*, arXiv:2401.08500, 2024-01-16 — https://arxiv.org/abs/2401.08500

**(a) Framework documentation and source, all read 2026-08-30**

- LangGraph persistence — https://docs.langchain.com/oss/python/langgraph/persistence
- LangGraph interrupts — https://docs.langchain.com/oss/python/langgraph/interrupts
- LangGraph README — https://raw.githubusercontent.com/langchain-ai/langgraph/main/README.md
- OpenAI Agents SDK, handoffs — https://openai.github.io/openai-agents-python/handoffs/
- OpenAI Agents SDK, sessions — https://openai.github.io/openai-agents-python/sessions/
- OpenAI Agents SDK, multi-agent orchestration — https://openai.github.io/openai-agents-python/multi_agent/
- OpenAI Swarm README — https://raw.githubusercontent.com/openai/swarm/main/README.md
- microsoft/autogen README — https://raw.githubusercontent.com/microsoft/autogen/main/README.md
- microsoft/semantic-kernel README — https://raw.githubusercontent.com/microsoft/semantic-kernel/main/README.md
- microsoft/agent-framework README — https://raw.githubusercontent.com/microsoft/agent-framework/main/README.md
- Microsoft Agent Framework overview (ms.date 2026-07-29, updated 2026-08-25) — https://learn.microsoft.com/en-us/agent-framework/overview/agent-framework-overview
- MAF workflow concepts (ms.date 2026-07-30) — https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/
- MAF orchestrations (ms.date 2026-02-12) — https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/
- ag2ai/ag2 README — https://raw.githubusercontent.com/ag2ai/ag2/main/README.md
- CrewAI Crews — https://docs.crewai.com/en/concepts/crews
- CrewAI Flows — https://docs.crewai.com/en/concepts/flows
- Google ADK workflow agents — https://adk.dev/agents/workflow-agents/
- LlamaIndex Workflows — https://developers.llamaindex.ai/python/framework/understanding/workflows/
- Pydantic AI durable execution — https://pydantic.dev/docs/ai/integrations/durable_execution/overview/
- Mastra workflows — https://mastra.ai/docs/workflows/overview
- smolagents README — https://raw.githubusercontent.com/huggingface/smolagents/main/README.md
- DSPy README — https://raw.githubusercontent.com/stanfordnlp/dspy/main/README.md
- Temporal, *Understanding Temporal* — https://docs.temporal.io/evaluate/understanding-temporal
- Temporal, use cases and design patterns — https://docs.temporal.io/evaluate/use-cases-design-patterns/
- Shopify/roast README — https://raw.githubusercontent.com/Shopify/roast/main/README.md
- cnoe-io/ai-platform-engineering (CAIPE) README — https://raw.githubusercontent.com/cnoe-io/ai-platform-engineering/main/README.md

**(b) Coding-tool documentation, all read 2026-08-30**

- Claude Code subagents — https://code.claude.com/docs/en/sub-agents
- Claude Agent SDK subagents — https://code.claude.com/docs/en/agent-sdk/subagents
- Claude Code dynamic workflows — https://code.claude.com/docs/en/workflows
- Claude Code agent teams — https://code.claude.com/docs/en/agent-teams
- Claude Code worktrees — https://code.claude.com/docs/en/worktrees
- Claude Code costs — https://code.claude.com/docs/en/costs
- Prompting Claude Opus 5 — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Devin dynamic workflows — https://docs.devin.ai/work-with-devin/dynamic-workflows.md
- Devin CLI subagents — https://docs.devin.ai/cli/subagents.md
- Devin, when to use Devin — https://docs.devin.ai/essential-guidelines/when-to-use-devin.md
- Cursor Agents window — https://cursor.com/docs/agent/agents-window
- Roo Code Boomerang tasks — https://roocodeinc.github.io/Roo-Code/features/boomerang-tasks
- Cline plan and act — https://docs.cline.bot/features/plan-and-act
- Amp models and subagents — https://ampcode.com/docs/models-and-subagents

**Vendor marketing, cited as such**

- LangChain customers — https://www.langchain.com/customers
- Outshift by Cisco, JARVIS and CAIPE posts (titles and search-surfaced claims only; bodies did not render — see below)

---

## Confidence and gaps

**High confidence**

- The fork/merge/retirement status of every framework in A.1. All established from the projects' own
  READMEs and Microsoft Learn, not from secondary reporting.
- The control-flow taxonomy in A.2, and the finding that every major vendor now ships a
  code-orchestrated mode and recommends it for predictability. Multiple independent primary sources
  say the same thing in their own words.
- The durability table in A.3. Every row is a direct quotation or a direct reading of the vendor's
  own page.
- The 2026 convergence on deterministic script orchestration (B.4). Two independent vendors, same
  primitives, same determinism ban, same replay semantics.
- The token multipliers in Part E, as *vendor-reported figures*. That they are vendor-reported is
  itself a finding — no framework publishes any.

**Medium confidence**

- **The central emptiness finding (no multi-agent framework shipping application software in
  production, first-party).** This is a negative established by directed search over vendor case
  studies, framework READMEs, and the engineering blogs of the companies most likely to have such a
  system. A private first-party write-up, a conference talk not indexed, or a case study published
  after 2026-08-30 could falsify it. It should be re-checked before publication and carried with an
  explicit "as of 2026-08-30."
- ✅ **Resolved 2026-09-02 (ticket #12): the CAIPE blog body renders in a real browser** (the page
  is client-rendered; automated fetch got only the shell). Verified verbatim from
  `outshift.cisco.com/blog/inside-outshift/caipe-building-open-source-multi-agent-systems-for-platform-engineering`:
  *"By using CAIPE, Outshift's team has automated around a third of its internal platform
  engineering tasks. They've reduced the average incident response time from hours to seconds."*
  Both figures are now vendor-primary (Cisco on Cisco — the interested-party caveat stands). The
  10× figure was **not** on this page; it remains sourced to the CAIPE white paper / LangChain
  customer post only.
- **The Cisco Outshift / CAIPE figures.** The blog bodies did not render (see below); the "one third
  of internal platform engineering tasks" and "hours to seconds" figures come from a search-engine
  summary of Cisco's own pages, not from a page this strand read directly. **Verify against the
  rendered article before quoting.** The repository and its Apache-2.0 licence were confirmed
  directly; the architecture details were not.

**Low confidence / not established**

- **Whether the negative result generalises past 2026-08.** Anthropic's Opus 5 guidance claims better
  multi-agent coordination "with… few cases of agents overwriting each other's work" and carries no
  figure. If a vendor publishes a measured coding result for a multi-agent configuration, the
  headline verdict changes and this file needs revisiting. This is the fastest-ageing material in
  the strand.
- **LangGraph's durability modes.** The `"exit"` / `"async"` / `"sync"` durability settings could not
  be confirmed from a rendered primary page in this session; the LangChain docs site moved and
  several concept pages returned redirect stubs. The `interrupt()` re-execution semantics *were*
  confirmed and are the more consequential fact, but the durability-mode detail is unverified and
  should not be asserted.
- **Cursor's parallel-agent limits and merge semantics.** Confirmed that parallel agents and worktree
  isolation exist; no published limit, merge strategy, or conflict behaviour was found.
- **Whether MAST's 2025 findings hold on 2026 models.** Almost certainly the absolute failure rates
  have moved. Whether the *architectural* failure categories have is unknown, and no one has
  re-run it.
- **Devin's published limits.** The "when to use Devin" page frames constraints as task-sizing advice
  ("if a task would take you three hours or less…") rather than as a limitations list; no negative
  capability statement was found.

**A note on vocabulary for downstream documents.** Per ADR-0001, the retired term is not used
anywhere in this file. The distinction that carries the analysis is **agent orchestration** (the
discipline) versus **flow engineering** (encoding the control flow explicitly). The 2026 convergence
described in B.4 is best characterised as *the coding-agent vendors moving from agent orchestration
to flow engineering for anything above a handful of delegated tasks*, and that sentence is
defensible from the primary sources cited. Where a benchmark appears (AlphaCodium, MAST) it is
reported as a **joint measurement** of model plus flow or model plus framework, never as a model
property. No score from the benchmark deprecated by its publisher in February 2026 appears anywhere
in this document.

---

## Blocked or unavailable sources

Logged, not circumvented.

| Source | What happened |
|---|---|
| `outshift.cisco.com/blog/inside-outshift/caipe-building-open-source-multi-agent-systems-for-platform-engineering` | Fetched successfully but the page returned only the title/heading — body appears to be client-rendered. Figures for CAIPE therefore rest on a search-result summary, not a read page. **Flagged for verification.** |
| `outshift.cisco.com/blog/JARVIS-agentic-platform-engineering-Outshift` | Same: returned footer navigation only, no article body. |
| `langchain-ai.github.io/langgraph/concepts/persistence/` | Returned a "Redirecting…" stub with no content. Superseded by `docs.langchain.com`, which was used instead. |
| `docs.langchain.com/oss/python/langgraph/durability` | HTTP 404. |
| `raw.githubusercontent.com/langchain-ai/langgraph/main/docs/docs/concepts/durable_execution.md` | HTTP 404 — the docs path has moved in-repo. Durability modes remain unverified as a result. |
| `docs.temporal.io/evaluate/use-cases-design-patterns/agentic-ai` | HTTP 404. Temporal's agentic-AI page has moved; `understanding-temporal` was used for the durability mechanics instead. |
| `temporal.io/blog/what-is-durable-execution-for-ai-agents` | HTTP 404. |
| `cursor.com/docs/agent/parallel-agents` | HTTP 404. Parallel-agent detail was recovered from `agents-window` instead, which is thinner. |
| `docs.devin.ai/essential-guidelines/multi-devin`, `docs.devin.ai/product-guides/parallel-devin` | HTTP 404 both. Multi-session detail recovered from `llms.txt` → `dynamic-workflows.md` and `cli/subagents.md`. |
| `blog.replit.com/three`, `blog.replit.com/agent-3`, `replit.com/blog/three` | 301 then HTTP 404. Replit's own account of Agent 3's architecture could not be read, so Replit appears in this document only as a name in LangGraph's README. |
| `raw.githubusercontent.com/Shopify/roast/main/docs/PHILOSOPHY.md` | HTTP 404. Roast's design rationale could not be established from a primary source. |
| `github`, `greptile`, `firebase`, `discord`, `figma-desktop` MCP servers | Failed to connect at session start (auth header rejected, timeout, connection closed). Not used; no finding depends on them. |
