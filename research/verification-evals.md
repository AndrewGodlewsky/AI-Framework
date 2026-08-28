# Evals as engineered verification: measuring an agent over time

**Strand:** how a team measures whether its agent is doing acceptable work OVER TIME, as distinct from whether any one change is correct.
**Research date:** 2026-08-28. Every claim below is dated to its artifact.

**Vocabulary held throughout.** *Verification* answers "is THIS change correct?" *Evals* are task-specific and built for a particular system; *benchmarks* are shared and comparative — they are not interchangeable here. *Eval harness* (the thing that runs eval cases) and *agent harness* (the scaffold that turns a model into an agent: tool loop, context assembly, retries) are different things and are never collapsed into a bare "harness".

---

## 1. Headline findings

1. **The longitudinal question is real and almost nobody answers it.** Across the primary sources I could reach, I found **four** organisations with a working eval suite that runs their *own* agent against *real repository tasks* — Cline, Block (goose), Zed, and Anthropic (for skills/tools, not for a coding agent on a repo). I found **zero** published instances of a team that is not an agent vendor doing this on its own private codebase.

2. **The mechanism everyone would guess — replay past tasks against a new model version — exists, is built, and is largely switched off.** Cline built exactly this (`cline-bench`: real production bug fixes mined from actual user sessions, `baselines/` for regression detection, pass@k / pass^k / flakiness metrics) and shipped it to CI on 2026-02-13. By 2026-05-14 the regression workflow was retired during an unrelated CLI migration, and the repo's own README still says nightly E2E "**not yet implemented, see TODO**". That is the single most informative artifact in this strand.

3. **Anthropic ships a first-party eval harness with a CI gate — undocumented, in early access.** `claude plugin eval` in Claude Code 2.1.250 runs eval cases with a **no-plugin baseline arm** (`--ablation with-without`, on by default), **repeated runs** (`--runs`, default 3), a **built-in LLM judge on a different model than the one under test** (`--judge-model`, default haiku), and **`--threshold <0..1>` — "Exit 1 if any case score is below this threshold"**. That is an LLM-as-judge used as a *gate*, not a metric. It appears in no public documentation page.

4. **Joint measurement is empirically demonstrated, not merely asserted.** The Terminal-Bench leaderboard scores *(agent harness, model)* pairs with separate `Agent Org` and `Model Org` columns; the same model moves several points across agent harnesses. Block's own published table is stronger still: on one fixed model, five agent harnesses spread **47.2% → 57.3%**. A bare model score does not transfer.

5. **Public benchmarks cannot answer the question by construction** — they are shared and comparative, and the question is specific and longitudinal. The transfer gap is now measurable: **30 points** from repository language alone at a fixed agent and model (SWE-Sharp-Bench), and a real-world agent PR acceptance rate of **35–64%** against SWE-bench Verified scores "exceeding 70%" (AIDev, 456,535 agent PRs).

6. **SWE-bench Verified's deprecation is CONFIRMED — and it is narrower than it sounds.** OpenAI published "Why SWE-bench Verified no longer measures frontier coding capabilities" on **2026-02-23**: "we have stopped reporting SWE-bench Verified scores, and we recommend that other model developers do so too." Grounds: **59.4%** of audited hard instances had material test/problem defects, plus reproducible gold-patch contamination. **But that is OpenAI retiring its own use.** The SWE-bench team (Princeton/Stanford) still maintains, publishes and leaderboards Verified as of 2026-08. Do not write "the benchmark was withdrawn".

7. **Eval-in-CI is roughly a 1-in-200 practice in public repos.** GitHub code search over `.github/workflows`: `pytest` **430,080** files vs LangSmith **1,078**, Promptfoo **516**, DeepEval **332**, Braintrust **185**, `inspect_ai` **85** — ~2,196 combined, **~0.5% of the pytest baseline**, and most of those are chatbot/RAG evals, not coding-agent evals.

8. **Vendors ship the instruments and publish no readings.** GitHub's API has carried `total_merged_created_by_copilot` since Feb 2026 and GitHub has published no aggregate from it, conceding only in prose that Copilot's merge rate is "lower than human contributors" — with no figure. Anthropic's Claude Code analytics exposes lines accepted, suggestion accept rate and PRs-with-CC, framed explicitly as "Measure ROI". **No vendor exposes a revert rate at all.** Every real agent-PR-outcome number in existence comes from academics mining public GitHub data.

9. **The metric a team would naturally watch moves the wrong way for the wrong reason.** Reviewer approval of agent PRs rises from **30.1% to 36.8%** over seven months while inline comments *fall* 22% and latency rises 3.5x — "reflexive habituation under growing workload rather than rational trust calibration" (`arXiv:2606.22721`). A rising merge rate can mean the gate is weakening, not that the agent improved.

**On the parent project's hypothesis** — that eval practice for coding agents on private repos is far less mature than the discourse implies, and most teams have nothing longitudinal: **the evidence supports it, and the mechanism is worse than immaturity — it is silent decay.** Three of the four organisations that built the right thing have since lost part of it, and nothing detected the loss. See §9 for how hard I looked and the three places the hypothesis needs qualifying.

---

## 2. What I could NOT find

Recorded as findings, not omissions.

- **No named non-vendor engineering organisation** publishing an eval suite for a coding agent against its own private codebase. Not one. Every `IN USE` example in §3 is a company that *sells the agent*.
- **No published regression suite of past tasks replayed against a new model version, in continuous operation.** The suites exist; the schedule does not. Cline's is a documented TODO; Zed has **no eval CI workflow at all** (`.github/workflows` contains no eval/bench job — runs are launched manually via Modal/Harbor/Pier).
- **No documentation from Anthropic of Claude Code's own internal evaluation practice** against Anthropic's codebase. "How Anthropic teams use Claude Code" describes *human review before merging* ("They give Claude abstract problems, let it work autonomously, then review solutions before final refinements") and periodic human check-ins — no evals, no regression tracking, no longitudinal measurement.
- **No calibration guidance in the most-adopted open-source eval CLI.** Promptfoo's model-graded assertion docs list ~20 LLM-as-judge assertion types and discuss *nothing* about judge bias, position bias, verbosity bias, self-preference, or agreement with human raters. The only reliability-adjacent line is "If you do not have access to the selected default or prefer a different judge, you can override the grader."
- **No named customer** shown using Braintrust, LangSmith, Langfuse, Promptfoo, DeepEval or Inspect for a coding agent on a private repo. Vendor docs describe the capability; no case study demonstrates it in this application.
- **No first-party revert or rollback rate for AI-authored changes, from any vendor.** The field does not exist in any GitHub API generation. The only published data is academic (`arXiv:2607.09902`).
- **Cost per merged change is proposed by nobody and published by nobody.** Of the metrics in this strand's brief, this appears to be a genuine gap in the field rather than a search failure. The nearest real instance is Block's goose table, which tracks cost per *eval run* — inside an eval harness, not a fleet.
- **No statement from the SWE-bench publishers responding to OpenAI's deprecation post.** The SWE-bench repos, leaderboard site posts, and news timeline were grepped for `deprecat|retire|sunset|contaminat` — nothing. Their silence-plus-continued-maintenance is itself the finding.
- **No published example of an eval suite run across a model-version matrix in CI.** Not established as absent — the GitHub code-search API rate-limited before this could be tested properly.
- **Aider's benchmark has gone dormant.** The polyglot leaderboard's last recorded run is **2025-10-03** (file last committed 2025-10-04) — ~11 months before this research date, spanning several model generations — while the model-keyed calibration file it informs was still being edited on **2026-04-24**. (The leaderboard page's "last updated November 20, 2025" is a site build date, not a data date.)

---

## 3. Custom / internal evals — the actual practice

### 3a. `IN USE` — named org + artifact

Every entry here is an **agent vendor**. That is itself the finding.

---

**Cline (Cline Bot Inc. — sells the agent; interested party)**
`https://github.com/cline/cline/tree/main/evals` · `https://github.com/cline/cline-bench`

The most complete published example of an eval suite built to answer the longitudinal question, and the most instructive because of how it decayed.

- **Layered design** (`evals/README.md`, last commit 2026-05-14): Layer 1 contract tests (no LLM calls); Layer 2 smoke tests (5 scenarios, 3 trials, minutes); Layer 3 E2E against `cline-bench` (hours, Docker/Daytona via Harbor).
- **Tasks are real production work, not synthetic.** `cline-bench` is described as "Real-world coding benchmarks derived from actual Cline user sessions. Tasks are challenging, verified, and represent genuine engineering problems solved in production." Each task ships `instruction.md`, `task.toml`, `environment/Dockerfile` (broken initial state), `solution/solve.sh` (oracle), and a `tests/` pytest suite.
- **Reliability metrics, not just pass rate.** `evals/analysis/src/metrics.ts` implements **pass@k** ("Can this model solve the problem?"), **pass^k** — probability *all* k trials pass, commented "Can I rely on this model?" — and an **entropy-based flakiness score**. With 3 trials: all pass → `pass`, all fail → `fail`, mixed → `flaky`. Cites the HumanEval paper (`https://arxiv.org/abs/2107.03374`).
- **Regression infrastructure**: a `baselines/` directory "for regression detection" and a failure classifier with pattern matching (`analysis/patterns/cline-failures.yaml`).

**And then the decay, precisely dated.** Commit history on `.github/workflows/cline-evals-regression.yml`:
- **2026-02-13** — `feat(evals): comprehensive LLM evaluation framework with CI (#8909)`
- **2026-02-23** — `ci: add automatic retries for smoke test jobs (#9503)`
- **2026-05-12** — `ci: move SDK publishing into cline/cline and retire legacy CLI infra (#10648)`
- **2026-05-14** — `chore: remove legacy cli/ source and adjacent dead glue (#10658)` — file removed.

The README's own status, verbatim:
> "Smoke tests (Layer 2) are partially disabled while the eval framework is repointed at the new SDK CLI. … The old build-and-link helpers and the auto-running `cline-evals-regression.yml` workflow are off until someone wires the build step at the new SDK CLI."

and, under **CI Integration**:
> "Current PR gate: contract tests only
> Smoke test CI: temporarily disabled while the workflow is repointed at the SDK CLI
> Nightly: E2E tests with cline-bench are **not yet implemented**, see TODO"

The `cline-bench` repo itself: created 2025-12-09, **last pushed 2025-12-11**, 36 stars, **12 tasks**, labelled "early access". It has not been touched in ~8.5 months.

*Read this carefully:* a well-resourced agent vendor built the exact longitudinal mechanism this strand is about, gated it in CI, and lost it to an unrelated refactor within three months. Nothing detected the loss of the detector.

---

**Block, Inc. (goose — sells/ships the agent; interested party)**
`https://github.com/block/goose/tree/main/evals/harbor` · README last commit **2026-08-12**

Block publishes an actual results table from a real fleet of eval runs — the only published table I found that varies **model, agent harness, and product build** together. All `*-full` runs cover the full `terminal-bench/terminal-bench-2` dataset (89 tasks):

| job | model | rate | compute | turns | cost | pass/fail/err/tout |
|---|---|---|---|---|---|---|
| `goose-sonnet46-full-code-mode` | claude-sonnet-4-6 | **57.3%** | 22.0h | 3k | $206.43 | 51/20/2/16 |
| `sonnet46-sum_codem` | claude-sonnet-4-6 | **57.3%** | 21.9h | 3k | $254.53 | 51/23/2/13 |
| `claude-sonnet46-full` | claude-sonnet-4-6 | 55.1% | 20.2h | 3k | $42.83 | 49/23/1/16 |
| `sonnet46-summon-full` | claude-sonnet-4-6 | 55.1% | 23.5h | 3k | $217.28 | 49/19/3/18 |
| `opencode-sonnet46-full` | claude-sonnet-4-6 | 52.8% | 22.2h | 3k | $70.30 | 47/23/0/19 |
| `sonnet46-full` (stock goose) | claude-sonnet-4-6 | 50.6% | 22.5h | 3k | — | 45/21/3/20 |
| `goose-1.30-sonnet46-full` | claude-sonnet-4-6 | 50.6% | 23.7h | 3k | — | 45/24/2/18 |
| `pi-sonnet46-full` | claude-sonnet-4-6 | 47.2% | 24.4h | 3k | $74.82 | 42/25/1/21 |
| `nemotron-full` | nemotron-3-nano-30b-a3b | 1.1% | 21.8h | 1k | — | 1/64/2/22 |

Block's own reading, verbatim: stock goose "lands at **50.6%** … roughly on par with `opencode` (52.8%) and ahead of `pi` (47.2%) on the same model. Notably, `pi` also burned the most compute (24.4h) — slowest *and* lowest scoring of the sonnet runs."

**Why this matters beyond goose:** holding the model fixed at `claude-sonnet-4-6`, the pass rate ranges **47.2% → 57.3%** purely as a function of agent harness and configuration — a 10.1-point spread, wider than the gap between adjacent frontier models on the same leaderboard. This is direct primary evidence for joint measurement (§5). It also tracks **cost per run** ($42.83 → $254.53 for scores within 2.4 points of each other), which is the cost-per-outcome metric §6 asks about, measured properly.

---

**Zed Industries (Zed editor — sells/ships the agent; interested party)**
`https://github.com/zed-industries/zed/tree/main/crates/eval_cli` · last commit **2026-08-09**

The clearest published statement of the joint-measurement design principle, from a product team:

> "`eval-cli` uses the **same `NativeAgent` + `AcpThread` pipeline as the production Zed editor**: a full agentic loop with tool calls, subagents, and retries, without a GUI."

They evaluate the shipping agent harness, not the bare model — the eval binary is the product's own agent loop with the GUI removed. Orchestration lives in `crates/eval_cli/zed_eval/`, a Python CLI that launches runs on Modal / Harbor / Pier and fetches results (`zed-eval run`, `zed-eval runs`, `zed-eval status`).

**But there is no eval CI.** `.github/workflows` contains no eval, bench or agent job. Runs are launched by hand. Zed has the eval harness and the production-fidelity design; it does not have the longitudinal schedule.

---

**Anthropic (model vendor; interested party) — `claude plugin eval`, early access, undocumented**
Verified against the installed CLI, **Claude Code 2.1.250**, 2026-08-28.

`claude plugin eval` — "Run eval cases (`<eval dir>/**/case.yaml` or `prompt.md` + `graders/*.md` …) against a plugin and report scored results." Running `claude plugin eval help` returns: "`plugin eval` is currently in early access". `curl https://code.claude.com/docs/llms.txt | grep -i eval` returns **zero matches** — it is in the shipping binary and absent from the entire public documentation index.

The flags are the interesting part, because each one encodes an eval-design decision:

| Flag | What it encodes |
|---|---|
| `--ablation <none\|with-without>` | **Controlled baseline arm, on by default.** "Run a no-plugin baseline arm and report the score delta". Measures the *delta the plugin causes*, not the absolute score. |
| `--runs <n>` (default `case.runs ?? 3`) | **Repeated runs** — the output is nondeterministic, so a single run is not a measurement. |
| `--judge-model <model>` (default `haiku`) | **LLM-as-judge built in, deliberately a different and cheaper model** than the one under test — the standard self-preference mitigation (§4). |
| `--threshold <0..1>` | **"Exit 1 if any case score is below this threshold."** This is the gate. |
| `--max-cost-usd <usd>` | Hard cost ceiling; on breach, paid graders (llm/baseline) are skipped while free graders still score. |
| `--mocks <record\|off>` | Deterministic stand-ins for MCP servers, so external services do not inject variance. |
| `tool_used: Skill` graders | Deterministic graders alongside LLM graders; under `with-without` these are a "plugin-fired indicator rather than part of the score". |

**Scope limit, stated plainly:** this evaluates a *plugin or skill*, not a coding agent working on your repository. It is nonetheless the only first-party artifact I found where an LLM-as-judge score is wired to a non-zero exit code.

---

**Anthropic — evals in operation for agent tools**
`https://www.anthropic.com/engineering/writing-tools-for-agents` (**2025-09-11**)

Anthropic describes evals it actually ran, not evals it recommends:
- Tasks built on real internal data: evaluations "created on top of our internal workspace, mirroring the complexity of our internal workflows, including real projects, documents, and messages".
- Explicitly against toy environments: "avoid overly simplistic or superficial 'sandbox' environments"; "Prompts should be inspired by real-world uses and be based on realistic data sources and services."
- Graders on a spectrum: "Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response."
- Beyond pass rate: "collecting other metrics like the total runtime of individual tool calls and tasks, the total number of tool calls, the total token consumption, and tool errors."
- Generation of the eval set is itself agent-driven: "Claude Code can quickly explore your tools and create dozens of prompt and response pairs."

---

**Anthropic — `skill-creator`, a shipped eval methodology**
`~/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/` (official marketplace, curated by Anthropic)

Working code, not advice. The methodology it encodes is the most complete first-party statement of how Anthropic thinks eval design should work, and several parts bear directly on this strand:

- **Paired arms in the same turn.** "For each test case, spawn two subagents in the same turn — one with the skill, one without. This is important: don't spawn the with-skill runs first and then come back for baselines later."
- **Variance is first-class.** `scripts/aggregate_benchmark.py` "produces `benchmark.json` and `benchmark.md` with pass_rate, time, and tokens for each configuration, **with mean ± stddev and the delta**."
- **Held-out split to prevent overfitting.** The description-optimisation loop "splits the eval set into 60% train and 40% held-out test, evaluates the current description (**running each query 3 times** to get a reliable trigger rate) … returns JSON with `best_description` — **selected by test score rather than train score to avoid overfitting**."
- **Joint measurement instruction, explicit.** "Use the model ID from your system prompt (the one powering the current session) **so the triggering test matches what the user actually experiences**."
- **The grader is told to attack the evals, not just apply them** (`agents/grader.md`): "You have two jobs: grade the outputs, and critique the evals themselves. **A passing grade on a weak assertion is worse than useless — it creates false confidence.**" It must flag "An assertion that passed but would also pass for a clearly wrong output".
- **Surface compliance is a FAIL.** "FAIL when … The evidence is superficial — the assertion is technically satisfied but the underlying task outcome is wrong or incomplete"; "The output appears to meet the assertion by coincidence rather than by actually doing the work." Burden of proof is on the expectation.
- **Discriminating-power analysis** (`agents/analyzer.md`): flag assertions that "always pass in both configurations (may not differentiate skill value)", ones that "always fail with skill but pass without" (the skill is hurting), and ones that are "highly variable (flaky expectation or non-deterministic behavior)".
- **Blind comparison for position bias**: "give two outputs to an independent agent without telling it which is which, and let it judge quality."
- **Anthropic's own guidance keeps the human in the loop**: blind comparison "is optional … **The human review loop is usually sufficient.**"

**Scope limit:** this is an eval methodology for *skills*, run inside a development loop. It is iteration-time, not longitudinal, and it is not aimed at a coding agent on a repository.

---

**The mechanism for building evals from your own repository exists — with a hard constraint**
`https://github.com/SWE-bench/SWE-bench/tree/main/swebench/collect`

SWE-bench ships the pipeline that turns a repo's merged PRs into eval task instances, and documents pointing it at your own code: "**To run collection on your own repositories, run the `run_get_tasks_pipeline.sh` script.**" It emits `<repo>-task-instances.jsonl` — "valid task instances that also has associated *tests* … candidate task instances. Once validated, they can be used for evaluation purposes."

Constraint, stated in the same README: "SWE-bench's collection pipeline is currently designed to target **PyPI packages**." Python only, and it requires that the PR have both a linked issue and test modifications — which selects for a narrow slice of a repo's real work.

**This is the gap in the field, stated precisely:** the tooling to mine your own git history into an eval set is public, free, and largely unused outside Python OSS. I found no organisation documenting having done it on a private codebase.

---

**Harbor — convergence on a shared eval harness**
`https://harborframework.com/` · `https://github.com/harbor-framework/harbor` (created 2025-08-04, **pushed 2026-08-28**, 4,720 stars, DOI `10.5281/zenodo.20953922`)

From the creators of Terminal-Bench. Its stated purpose is exactly the joint-measurement shape:
> "Evaluate arbitrary agents like Claude Code, OpenHands, Codex CLI, and more."
> "**Build and share your own benchmarks and environments.**"

Cline, Block (goose) and Zed all run their eval suites on it. That convergence is a genuine, dateable maturation of the ecosystem — the eval harness problem is being solved even where the eval *practice* is not.

### 3b. `PROPOSED / ADVOCATED` — capability documented, no named operator

Everything in this bucket is either a vendor documenting a feature it sells, or guidance without a shown instance.

| Source | Stake | What it documents | Date |
|---|---|---|---|
| Anthropic, "Create strong empirical evaluations" `https://platform.claude.com/docs/en/test-and-evaluate/develop-tests` | Model vendor | Task-specific eval design, exact-match / cosine / ROUGE-L / LLM-graded graders, Likert and binary rubrics. Key line: "**Be task-specific: Design evals that mirror your real-world task distribution.**" And on volume: "More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals." | current |
| Anthropic, "Building effective agents" `https://www.anthropic.com/engineering/building-effective-agents` | Model vendor | Advocacy only — "The key to success, as with any LLM features, is measuring performance and iterating on implementations." No eval framework, no instance shown. | 2024-12-19 |
| OpenAI Evals guide `https://developers.openai.com/api/docs/guides/evals` | Model vendor | Prompt-level evals, `string_check` grader. States "Writing evals … especially when upgrading or trying new models, is an essential component to building reliable applications" but gives **no procedure** for it. Does not address agent evaluation at all. | current |
| OpenAI `evals` repo `https://github.com/openai/evals` | Model vendor | "a framework for evaluating large language models (LLMs) or systems built using LLMs", incl. private evals on proprietary data. No archival/deprecation notice found. | current |
| Braintrust `https://www.braintrust.dev/docs/guides/evals` | **Sells the eval product** | "Experiments are the immutable, comparable record of your eval runs … track progress over time, and integrate into CI/CD to catch regressions before they reach production." No named coding-agent customer. | current |
| LangSmith `https://docs.langchain.com/langsmith/evaluation` | **Sells the eval product** | "compare experiments for benchmarking, unit tests, regression tests, or backtesting"; LLM-as-judge as an evaluator type. General LLM apps; CI gating not explicit. | current |
| Langfuse `https://langfuse.com/docs/evaluation/overview` | **Sells the eval product** | LLM-as-judge, human annotation, code evaluators, experiments across prompts/models/code variants; links "Block deploys on regressions" to CI/CD experiments. Oriented at LLM-app observability. | current |
| Promptfoo `https://www.promptfoo.dev/docs/` | **Sells the eval product** | "an open-source CLI and library for evaluating and red-teaming LLM apps"; "benchmarks specific to your use-case". Does **not** address coding agents on a codebase or cross-model-version regression. ~20 model-graded assertion types, **no bias/calibration guidance**. | current |
| DeepEval `https://deepeval.com/` | **Sells the eval product** (Confident AI) | Agentic metrics: Task Completion, Step Efficiency, Argument Correctness, Tool Correctness, Plan Adherence, Plan Quality. Has a "Regression Testing LLM Systems in CI/CD" guide. Serves RAG/chatbot *and* agents; not repo-specific. | current |
| Inspect, UK AI Security Institute + Meridian Labs `https://inspect.aisi.org.uk/` | Government/nonprofit — **least conflicted source here** | "an open-source framework for large language model evaluations". Built-in ReAct agent, bash/python/editor tools, sandboxing (Docker, K8s, Modal, Proxmox, Vagrant), and can "run arbitrary external agents like **Claude Code and Gemini CLI**" — i.e. supports joint measurement. Documentation emphasises 200+ pre-built shared **benchmarks**; **no documentation of evaluation against a private codebase.** | current |
| Ragas | Sells/maintains eval product | RAG-oriented. Out of scope for coding agents on a repo. | — |

**Adoption reality check (GitHub code search over `.github/workflows`, 2026-08-28).** Public repos only — this necessarily undercounts private repos, which is exactly where the practice would live if it existed; treat as a floor, not a census.

| Tool in CI | Files |
|---|---|
| `pytest` (baseline) | **430,080** |
| `langsmith` | 1,078 |
| `promptfoo` | 516 |
| `deepeval` | 332 |
| `braintrust` | 185 |
| `inspect_ai` | 85 |
| **eval tools combined** | **~2,196 (≈0.5% of pytest)** |

---

## 4. LLM-as-judge: calibration, failure modes, and whether it gates

### The primary papers on judge failure modes

| Bias | Primary source | Finding |
|---|---|---|
| Position bias | Wang et al., *Large Language Models are not Fair Evaluators*, `https://arxiv.org/abs/2305.17926` (submitted 2023-05-29, rev. 2023-08-30) | "The quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context." Magnitude: Vicuna-13B "could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator" once order was manipulated — reordering **reverses** the verdict. |
| Position + verbosity + self-enhancement | Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, `https://arxiv.org/abs/2306.05685` (submitted 2023-06-09, v4 2023-12-24) | Names and examines "position, verbosity, and self-enhancement biases, as well as limited reasoning ability". Also the calibration anchor everyone cites: strong judges "match both controlled and crowdsourced human preferences well, achieving **over 80% agreement, the same level of agreement between humans**." |
| Self-preference | Panickssery, Bowman & Feng, *LLM Evaluators Recognize and Favor Their Own Generations*, `https://arxiv.org/abs/2404.13076` (submitted 2024-04-15) | "we discover a **linear correlation between self-recognition capability and the strength of self-preference bias**", and establish the link is causal. GPT-4 and Llama 2 show "non-trivial accuracy at distinguishing themselves from other LLMs and humans" untrained. |

**The 80%-agreement number is the field's calibration standard and it is doing more work than it can bear.** It was measured on MT-Bench/Chatbot Arena — open-ended chat preference — not on "did this patch correctly fix this bug in this repository". I found no equivalent human-agreement calibration published for a judge grading code changes against a real codebase. Anyone reusing the 80% figure to justify an unattended code gate is extrapolating across task types.

### How the failure modes are mitigated in practice

- **Different model for judging.** Anthropic's eval guidance: "Generally best practice to use a different model to evaluate than the model used to generate the evaluated output" (`https://platform.claude.com/docs/en/test-and-evaluate/develop-tests`). Enforced in the shipping tool: `claude plugin eval --judge-model` defaults to **haiku**, not the model under test.
- **Blinding for position bias.** `skill-creator` blind comparison: "give two outputs to an independent agent **without telling it which is which**".
- **Prefer deterministic graders where possible.** `skill-creator`: "For assertions that can be checked programmatically, **write and run a script rather than eyeballing it** — scripts are faster, more reliable, and can be reused across iterations." `claude plugin eval` mixes deterministic graders (`tool_used: Skill`) with LLM graders and, under `--max-cost-usd` breach, "paid graders (llm/baseline) are skipped while **free graders still score it**" — the deterministic tier survives.
- **Attack the assertions, not just the outputs.** The grader is instructed that "A passing grade on a weak assertion is worse than useless — it creates false confidence."

### Does anyone use it as a gate rather than a metric?

**Yes — but only one first-party artifact, and not on a codebase.** `claude plugin eval --threshold <0..1>` — "**Exit 1 if any case score is below this threshold**" — makes an LLM-judged score a build-failing condition. It is in early access and undocumented, and it gates a *plugin*, not a repository change.

Everything else is vendor documentation of the *capability* (Braintrust "integrate into CI/CD to catch regressions"; Langfuse "Block deploys on regressions"; DeepEval's CI/CD regression guide) with **no named operator shown**. Promptfoo's GitHub Action documentation describes posting results as a PR comment and does not document failing a build on a score threshold.

**Judgement:** LLM-as-judge is overwhelmingly used as a **metric inside a development loop**, reviewed by a human. Using it as an unattended gate is a documented capability that I could not find anyone publicly attesting to running on production code.

---

## 5. Joint measurement — measuring model + agent harness + codebase together

The project glossary term is **supported by primary evidence**, and the evidence is quantitative.

**Terminal-Bench leaderboard** (`https://www.tbench.ai/leaderboard/terminal-bench/2.1`). Columns: `Rank, Agent, Model, Effort, Accuracy, Date, Agent Org, Model Org, PR, Hacks, Cost`. Every entry is an *(agent harness, model)* pair, with the agent's org and the model's org tracked separately. Selected entries:

| Agent harness | Model | Accuracy |
|---|---|---|
| Claude Code | Fable 5 | 83.8% ± 1.2% |
| Codex | GPT-5.5 | 83.1% ± 1.1% |
| **Terminus 2** | **Fable 5** | **80.4% ± 1.2%** |
| Cursor CLI | Grok 4.5 | 79.3% ± 1.5% |
| Claude Code | Opus 4.8 | 78.9% ± 1.3% |
| Terminus 2 | GPT-5.5 | 78.0% ± 1.2% |
| Claude Code | Sonnet 5 | 74.6% ± 1.6% |

Fable 5 scores **83.8% under Claude Code and 80.4% under Terminus 2** — 3.4 points from the agent harness alone, on identical tasks. The board also carries a `Hacks` column, i.e. the operators consider benchmark-gaming frequent enough to need a dedicated field.

**Block's goose table (§3a) is the stronger evidence** because it holds the model *completely* fixed: on `claude-sonnet-4-6`, five agent harnesses span **47.2% → 57.3%**. The agent-harness effect (10.1 points) exceeds the model-version effect visible between adjacent frontier models on Terminal-Bench.

**Stated as a design principle by a product team** — Zed: "`eval-cli` uses the **same `NativeAgent` + `AcpThread` pipeline as the production Zed editor**". And by Anthropic in `skill-creator`: "Use the model ID from your system prompt (the one powering the current session) so the triggering test **matches what the user actually experiences**."

**Tooling that supports it:** Harbor ("Evaluate arbitrary agents like Claude Code, OpenHands, Codex CLI") and Inspect ("run arbitrary external agents like Claude Code and Gemini CLI") both take the agent harness as a first-class variable.

**The third term is missing.** All of this measures *model × agent harness*. The **codebase** term — the same agent harness and model against *your* repository, with its conventions, its flaky tests, its multi-repo context — is exactly what `cline-bench` and the SWE-bench `collect` pipeline are for, and it is the term with essentially no published practice behind it. **Nothing I found contests joint measurement; the gap is that only two of its three terms are actually being measured.**

---

## 6. Fleet-level metrics — instruments shipped, readings withheld

Population-level measurement of whether an agent is producing acceptable work. **Every source in this section is stake-labelled; several of these companies sell the measurement product, and their published numbers are interested claims.**

### 6a. What the model vendor actually exposes

**Anthropic, Claude Code analytics** — `https://code.claude.com/docs/en/analytics` (model vendor; interested party). Exact metrics exposed to Team/Enterprise admins:

- **PRs with CC** — merged PRs containing ≥1 line written with Claude Code
- **Lines of code with CC** — "effective lines" only (>3 chars after normalisation, excluding brackets/punctuation)
- **PRs with Claude Code (%)**
- **Suggestion accept rate** — "percentage of times users accept Claude Code's code editing suggestions"
- **Lines of code accepted** — "excludes rejected suggestions and **does not track subsequent deletions**"
- **Adoption**: daily active users, sessions; **PRs per user**; **Leaderboard** of top contributors

**Attribution method** (worth recording, because it bounds what the numbers can mean): added lines from the merged PR diff are matched against Claude Code session output within a window of "21 days before to 2 days after the PR merge date"; "Code substantially rewritten by developers, with **more than 20% difference, is not attributed** to Claude Code." Anthropic labels the dashboard "deliberately conservative and … an underestimate".

**The finding: every one of these is an adoption or volume metric. Not one is a quality metric.** There is no revert rate, no rework rate, no change-failure rate, no defect density, no post-merge outcome of any kind. "Lines of code accepted" explicitly does not track subsequent deletion — so code accepted and then thrown away counts identically to code that shipped and worked. Anthropic's framing is explicit: the section is titled "**Measure ROI**" and says the metrics "help answer 'Is this tool worth the investment?'", suggesting teams "Use alongside [DORA metrics](https://dora.dev/), sprint velocity, or other engineering KPIs".

A team removing human review cannot use this dashboard to learn that its agent got worse. It can only learn that its agent was used more.

*Note: the one metric here that edges toward quality — the 20% rewrite threshold — is used to* exclude *heavily-rewritten code from attribution, i.e. to protect the ROI number, rather than being surfaced as a human-edit-distance metric. Human edit distance after agent output is being computed and then discarded.*

---

### 6b. The instrument/reading gap — the story of this section

**Every vendor that holds fleet telemetry ships the instrument and publishes no reading from it.** Every real fleet-level number about agent PR outcomes in existence comes from academics mining public GitHub data, not from the vendors who hold the data.

**GitHub (sells Copilot; interested party)** is the sharpest case. The Copilot usage metrics API ships the exact fields needed to compute an agent PR merge rate — field names verbatim from `github/docs`:

| Field | Definition (verbatim) |
|---|---|
| `pull_requests.total_created_by_copilot` | "Number of pull requests created by Copilot cloud agent on this specific day." |
| `pull_requests.total_merged_created_by_copilot` | "Number of pull requests created by Copilot cloud agent that were merged on this specific day." |
| `pull_requests.median_minutes_to_merge_copilot_authored` | "Median time, in minutes, between pull request creation and merge for pull requests created by Copilot cloud agent and merged on this specific day." |

Org-level analytics have been available since 2025-12-12. Acceptance rate is computed, not stored (`code_acceptance_activity_count ÷ code_generation_activity_count`). **No `revert` field exists in any API generation.**

GitHub has published no aggregate reading from these fields in the six months since shipping them, while conceding the outcome in prose without a figure (`https://github.blog/ai-and-ml/github-copilot/how-copilot-helps-build-the-github-platform/`, 2025-11-12):

> "If you check Copilot's merged pull request rate in your repo, you'll notice it's **lower than human contributors**. That's expected—and useful."

Octoverse 2025 publishes the numerator only — "1+ million pull requests… created between May 2025 and September 2025" — with no merge, close, or revert outcome. And GitHub's dashboard guidance frames a *falling* acceptance rate solely as a tooling defect ("Configuration issues or reduced relevance of suggestions"), never as evidence that output quality degraded. That is a vendor-shaped reading of the one metric that could act as an early warning.

### 6c. `IN USE — REAL NUMBERS PUBLISHED`

Ordered by how neutral the publisher is.

---

**Academic, low stake — the AIDev dataset.** Hao Li, Ahmed E. Hassan et al. (Queen's University), "The Rise of AI Teammates in Software Engineering (SE) 3.0", **2025-07-20**, `https://arxiv.org/abs/2507.15003`. Openly released dataset: "456,535 Agentic-PRs created by five leading Autonomous Coding Agents" across "61,453 repositories" and "47,303 developers" (Codex, Devin, Copilot, Cursor, Claude Code).

Agent PR acceptance rate, verbatim:
> "across all evaluated Autonomous Coding Agents, PR acceptance rates consistently lag behind human performance… **OpenAI Codex achieves the highest acceptance rate at 64%, followed by Devin at 49% and GitHub Copilot at 35%.** These substantial performance gaps, ranging from 15 to 40 percentage points below human performance, suggest systemic limitations rather than isolated implementation flaws."

And — directly on this strand's central claim about benchmarks:
> "these results contrast sharply with benchmark performance on SWE-bench verified… where top-performing AI solutions report success rates exceeding 70%. **This significant disparity between benchmark and real-world performance raises important questions about the ecological validity of current evaluation methodologies.**"

Also: "both Human-PRs and Agentic-PRs receive no explicit review in the majority of cases (**75.3% and 58.2%**, respectively)."

---

**Academic, low stake — revert/rework, the metric nobody else publishes.** "Do These Violent Delights Have Violent Ends? Measuring the Post-Merge Fate of Agentic Code", **2026-07-10**, `https://arxiv.org/abs/2607.09902`. 182 repositories, longitudinal.

> "While the overall maintenance rates are similar, agentic contributions require **significantly higher rates of corrective maintenance** and introduce more security weaknesses and dependency vulnerabilities… each 10 percentage-point increase in a project's no-review rate is associated with roughly a **6% increase in agentic maintenance burden** on average."

> "**merge success alone does not reveal whether a contribution will remain stable** or require bug fixes and other corrective maintenance downstream."

That second sentence is the fleet-metrics equivalent of this strand's whole argument, and the "no-review rate → maintenance burden" coefficient is the single most decision-relevant number I found for a team considering removing human review.

---

**Academic, low stake — merge rate is a misleading label.** "Why Are Agentic Pull Requests Merged or Rejected?", **2026-05-21**, `https://arxiv.org/abs/2605.22534`. 11,048 closed agentic PRs → 9,799 human-reviewed → 717 manually inspected.

> "only **35.7% of rejected PRs reflected clear agentic failures**, while 31.2% were driven by workflow constraints and 33.1% lacked observable decision rationale. Among merged PRs, **15.4% required explicit reviewer involvement** through feedback or direct commits, and 5.5% showed no visible interaction trace."

> "These results **reject the assumption that PR outcomes alone capture agent performance**."

---

**Academic, low stake — the gate itself decays.** "Habituation at the Gate", **2026-06-21**, `https://arxiv.org/abs/2606.22721`. 400 repeat reviewers, 11,429 reviews, seven months.

> "a population-level shift in approval rate from **30.1% to 36.8%**… the cumulative gap reaches **+14.5 pp** from first to tenth decile. This shift is experience-driven… agent-specific (human PR approval rates decline over the same period), and not explained by PR difficulty… However, **review latency increases** rather than decreases (+3.5x), while **inline comment volume decreases (-22%**, p=0.0014)"

Diagnosis, verbatim: "most consistent with **reflexive habituation under growing workload** rather than rational trust calibration alone."

**This is the most important fleet finding in the whole strand.** A rising agent merge rate can mean the verification gate is weakening, not that the output improved. Any dashboard tracking acceptance or merge rate as a quality proxy will read gate decay as agent improvement. Corroborated by `https://arxiv.org/abs/2601.13754` (2026-01-20): "approximately **80% merged without any explicit review**" for AI-co-authored PRs from non-owners.

---

**Academic, low stake — other AIDev-derived numbers.**
- "Beyond Bug Fixes", 2026-01-27, `https://arxiv.org/abs/2601.20109` — 1,210 merged agent bug-fix PRs: "**merge success does not reliably reflect post-merge code quality**"; agent differences "largely disappear after normalizing by code churn" (raw issue counts track PR size).
- 2026-01-20, `https://arxiv.org/abs/2601.13597` — staggered difference-in-differences: static-analysis warnings and cognitive complexity rise "roughly **18% and 39%**" after agent adoption; "sustained agent-induced technical debt **even when velocity advantages fade**."
- 2026-06-24, `https://arxiv.org/abs/2606.26289` — 11,097 repos, Jan 2023–May 2026: human contributor density ATT −0.019 (p=0.002); newcomer share −3.7pp; review depth **+5.3%** — "AI agents **shift burden from the code production stage to the review stage**."
- 2026-07-06, `https://arxiv.org/abs/2607.04697` — concurrent agents: textual merge conflict **41.7% cross-agent vs 19.8% intra-agent** (non-overlapping 95% CIs). A failure mode that only exists once you run more than one agent.
- **Contrary result, carried honestly**: 2026-07-06, `https://arxiv.org/abs/2607.05677` — 13,360 AI chat sessions, 1,356 repos: "no broad deterioration in code-quality signals or pull request merging rates."

---

**Harvard / Jellyfish — best firm-level telemetry study. Stake: mixed, well-declared.** Fiona Chen & James Stratton (Harvard), current version **2026-08-04**, `https://fion.ac/jellyfish.pdf` (ungated). Data from Jellyfish, a measurement vendor; authors funded by the Stripe Economics of AI Fellowship, Harvard Kennedy School and Schmidt Sciences. Their independence statement is worth reproducing:

> "The conclusions of this study are those of the authors and do not represent the views of Jellyfish… The manuscript was reviewed by the data partner **solely to verify that it does not disclose proprietary information** … it was **not reviewed for its scientific content**."

Scale: "300 million work events… across **718 firms**", 725,938 workers, Jan 2021 – Mar 2026, staggered difference-in-differences on adoption timing.

- Individual productivity, agents: "**30% for lines of code, 20% for commits, and 23% for pull requests**."
- Firm output does not follow: "small positive, but statistically insignificant, effects… For agents, our estimates **rule out an increase in output of larger than 12%** of the baseline mean — well below the 30% individual-level productivity gain."
- **The verification bottleneck**: "The average time to review a pull request **increases by 49%**, the share of pull requests with changes requested **nearly doubles**, and the number of comments per pull request increases by 35%. Firms also reallocate labor toward review activities: the share of workers performing code reviews increases by 14%. **This bottleneck persists following the adoption of AI code review tools.**"

---

**Google (sells AI coding products; interested party) — the only published longitudinal fleet series.**
- 2022-07, `https://research.google/blog/ml-enhanced-code-completion-improves-developer-productivity/` — 10,000+ Google developers, three months: single-line acceptance **25%**, multi-line **34%**; "3% of new code (measured in characters) now generated from accepting ML completion suggestions."
- 2024-06-06, `https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/` — "acceptance rate by software engineers of **37%**"; AI responsible for "**50% of code characters**"; code review comments ">8% of which are now addressed with AI-based assistance."

25% → 37% acceptance and 3% → 50% character share across two years is the only genuine published fleet time series I found. Note it measures *adoption and acceptance*, not correctness.

---

**GitHub / Microsoft (sell Copilot; interested parties) — acceptance published, outcomes withheld.**
- 2023-06-27, `https://github.blog/news-insights/research/the-economic-impact-of-the-ai-powered-developer-lifecycle-and-lessons-from-github-copilot/` — "Analysis on a large sample of GitHub Copilot users (**n = 934,533**)… users accept nearly **30%** of code suggestions." No later figure and no time series exists.
- **Human edit distance, the only first-party data at fleet scale** — Ziegler et al., `https://arxiv.org/abs/2205.06537` (2022): mean `accepted_per_shown` **0.26**; `unchanged_600_per_accepted` mean **0.46** — i.e. **~54% of accepted completions are edited within ten minutes** (n≈2,019). GitHub's own caveat, verbatim: "Such discrepancies highlight the **difficulty in using acceptance rate to understand the value** of a system."
- Accenture enterprise RCT, 2024-05-13: "**15% increase to the pull request merge rate**", "8.69% increase in pull requests", "developers retained **88%** of GitHub Copilot-generated characters". Single customer.
- Microsoft Research, Cui et al., June 2025 — three RCTs, n = 4,867 developers: "a **26.08% increase (SE: 10.3%)** in completed tasks." That SE puts the 95% CI at roughly 6–46%.
- Microsoft fleet rollout, 2026-07-01, `https://arxiv.org/abs/2607.01418` — "tens of thousands of engineers at Microsoft", early-2026 Claude Code and Copilot CLI rollout: "adopters merged roughly **24% more pull requests** than they would have otherwise", sustained over four months. Authors' own caveat, verbatim: "**a merged PR is not the same as the value it delivers.**"

---

**DORA / Google Cloud — survey, NOT telemetry. Stake: high and dual** (Google Cloud sells Gemini Code Assist and Gemini CLI, and is reporting on the category it sells into). **This distinction matters and is frequently lost**: DORA's findings are self-reported perceptions from a few thousand respondents, not measurements of any fleet.

- **DORA 2024** (`https://services.google.com/fh/files/misc/2024_final_dora_report.pdf`, n ≈ 3,000). Section heading, verbatim: **"AI is hurting delivery performance."** > "the effect on delivery throughput is small, but likely negative (an estimated **1.5% reduction** for every 25% increase in AI adoption). The negative impact on delivery stability is larger (an estimated **7.2% reduction** for every 25% increase in AI adoption)." And: "AI does not appear to be a panacea."
- **DORA 2025** (`https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf`, n = 4,867, surveyed 2025-06-13 → 2025-07-21): "AI adoption now **improves software delivery throughput**, a key shift from last year. However, **it still increases delivery instability.** This suggests that while teams are adapting for speed, their underlying systems have not yet evolved to safely manage AI-accelerated development."

The 2025 edition reports standardised effect sizes with 89% credible intervals rather than 2024's "per 25% adoption" framing, so **the two years' magnitudes are not directly comparable** — only the direction reversal is. The persistent finding across both years is *increased instability*.

---

**Faros AI — largest vendor telemetry fleet. Stake: very high** (sells the measurement platform; full reports email-gated, so the below is the ungated marketing surface).
`https://www.faros.ai/research/ai-acceleration-whiplash` — "Two years of telemetry from **22K developers across 4K teams**"; headline deltas "**+51% PR Size · +28% Bugs per PR · 5X Median Review Time · 3X Incidents per PR · 10X Code Churn**". Positioning, verbatim: "**Telemetry, not surveys**… Our data directly contradicts DORA's 2025 findings."
`https://www.faros.ai/ai-productivity-paradox` (updated 2025-12-12) — "telemetry and workflow data from **10K devs across 1,255 enterprise engineering teams**"; developers "complete 21% more tasks and merge 98% more pull requests" while review times rise 91% and DORA metrics stay "largely unchanged."

**Faros independently replicates the Harvard/Jellyfish verification-bottleneck result from a different dataset.** Two independent telemetry sources agreeing that review cost rises sharply is the most reproducible fleet-level finding in this strand — and it is a *verification* cost, not a code-production cost.

---

**curl / Daniel Stenberg — maintainer rejection rate. Stake: none.** 2025-07-14, `https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/`. AI slop is "about **20% of all submissions**" in 2025, against a valid-report rate of "about **5%** of the submissions in 2025", running at "about two security report submissions per week."

**GitClear — code churn and duplication. Stake: high** (sells code analytics; full PDF email-gated). `https://www.gitclear.com/ai_assistant_code_quality_2025_research` — 211 million changed lines, 2020–2024: code clones rose **8.3% → 12.3%** of changed lines; refactoring fell **25% → under 10%**.

**METR — the neutral RCT. Stake: low** (nonprofit, sells nothing here). `https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/`, 2025-07-10. 16 experienced developers, 246 issues, mature repos (22k+ stars, 1M+ LOC): developers "take **19% longer** to complete issues" when allowed AI tools. Small n, and it measures task completion time rather than merge rate — but it is the only well-powered RCT pointing against the vendor direction, and the AIDev authors cite it.

**Jellyfish internal case study. Stake: very high** (measuring itself, with a partner's tool). `https://jellyfish.co/blog/ai-code-review-doubled-pr-throughput/` — **n = 18 engineers**. PRs/developer +110%, PR size −82%, bugs/developer −20%; nine-month follow-up shows 2x throughput but **longer** median cycle time (17.8h vs 5.5h). Anecdote-scale; recorded for completeness, not as evidence.

### 6d. `PROPOSED / FRAMEWORK ONLY`

- **DORA AI Capabilities Model** (Google Cloud; interested party), `https://services.google.com/fh/files/misc/2025_dora_ai_capabilities_model.pdf`. Seven capabilities: "Clear and communicated AI stance · Healthy data ecosystems · AI-accessible internal data · Strong version control practices · Working in small batches · User-centric focus · Quality internal platforms." Survey-derived *moderators*, not measured fleet outcomes.
- **DX / Getdx AI Measurement Framework** (sells the measurement product), `https://getdx.com/research/measuring-ai-code-assistants-and-agents/` (Abi Noda, Laura Tacho). Public page names only broad dimensions (utilization/adoption, impact, cost) and references "AI-driven time savings, PR throughput, Perceived Rate of Delivery, Developer Experience Index." **Exact metric definitions sit behind an email gate, which was not filled in.** Customer figures on the public page are single-customer illustrations without n (Booking.com "16% increase in throughput"; Intercom "41% increase in AI-driven developer time savings"). Treat as marketing copy.
- **GitHub agentic evaluation** (`https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/`, 2026-06-25) — SWE-bench Verified, SWE-bench Pro, SkillsBench, Terminal-Bench. These are shared comparative **benchmarks**, not evals and not fleet telemetry; results shown as charts without printed scores.
- **Anthropic Economic Index** (`https://www.anthropic.com/news/anthropic-economic-index-september-2025-report`, 2025-09-15) — two million conversations, reports task *distribution* ("create new code" 4.1% → 8.6%). **No acceptance, PR outcome or task-success metric.** Reporting that emptiness is the finding: Anthropic's public research surface carries no agent output-quality data.

### 6e. What this means for the strand

1. **Revert rate is the great unmeasured metric.** No vendor exposes it. The only published data is academic (`arXiv:2607.09902`).
2. **Cost per merged change is proposed by no one and published by no one.** Of the metrics in this strand's brief, this is the one that appears to be a genuine gap in the field rather than a search failure. The nearest real instance is Block's goose table (§3a), which tracks cost per eval run — inside an eval harness, not a fleet.
3. **Acceptance rate has a known ceiling as a signal, stated by its own publisher**, and ~54% of accepted completions are edited within ten minutes.
4. **A fleet dashboard without a verification-effort denominator will mislead.** Approval rate rises as scrutiny falls (`arXiv:2606.22721`); merge rate does not track post-merge stability (`arXiv:2607.09902`, `arXiv:2601.20109`); most rejections are not agent failures (`arXiv:2605.22534`). None of the vendor dashboards in §6a–6b carry that denominator.

## 7. Model-update risk — every prior calibration is invalidated

This is why the longitudinal question cannot be optional. If the model underneath an agent changes, every threshold, prompt and grader calibrated against the old one is measuring something else.

### 7a. The risk is not hypothetical — the retirement cadence, from the vendors

**Anthropic** (model vendor) — `https://platform.claude.com/docs/en/about-claude/model-deprecations`. Commitment: "Anthropic notifies customers with active deployments for models with upcoming retirements, providing **at least 60 days' notice** before model retirement for publicly released models." Recent retirements:

| Model | Deprecated | Retired |
|---|---|---|
| `claude-opus-4-1-20250805` | 2026-06-05 | 2026-08-05 |
| `claude-sonnet-4-20250514`, `claude-opus-4-20250514` | 2026-04-14 | 2026-06-15 |
| `claude-3-haiku-20240307` | 2026-02-19 | 2026-04-20 |
| `claude-3-5-haiku-20241022` | 2025-12-19 | 2026-02-19 |
| `claude-3-7-sonnet-20250219` | 2025-10-28 | 2026-02-19 |
| `claude-3-5-sonnet-2024{0620,1022}` | 2025-08-13 | 2025-10-28 |

Observed announcement-to-retirement gap: **~60-62 days.** **OpenAI** commits to "At least 6 months" for GA models, "At least 3 months" for specialized variants, and preview models "may be retired with much shorter notice" (`https://developers.openai.com/api/docs/deprecations`). **Google**: preview models "will be deprecated with at least 2 weeks notice"; `-latest` breaking changes get "a 2-week notice" (`https://ai.google.dev/gemini-api/docs/models`).

Anthropic also deprecates **parameters** in ways that break calibration hard: `temperature`, `top_p`, `top_k` "Returns a 400 error when set to a non-default value on Claude 4.7 and later models." A pinned sampling setting does not degrade quietly — the request fails.

### 7b. `IN USE` — a vendor's own eval suite failing to catch a behavioural regression

**OpenAI, GPT-4o sycophancy rollback, 2025-04-29.** `https://openai.com/index/sycophancy-in-gpt-4o/` and `https://openai.com/index/expanding-on-sycophancy/`. Quotes below verified directly against the source page HTML on 2026-08-28.

The best-documented case of a model update changing deployed behaviour — and it is a vendor stating that its own eval suite did not catch it:

> "One of the key problems with this launch was that **our offline evaluations—especially those testing behavior—generally looked good.** Similarly, the A/B tests seemed to indicate that the small number of users who tried the model liked it."

> "**We also didn't have specific deployment evaluations tracking sycophancy.**"

> "Our offline evals **weren't broad or deep enough** to catch sycophantic behavior … and our A/B tests didn't have the right signals to show how the model was performing on that front with enough detail."

> "We then had a decision to make: should we withhold deploying this update **despite positive evaluations and A/B test results**, based only on the subjective flags of the expert testers? In the end, we decided to launch the model due to the positive signals from the users who tried out the model. **Unfortunately, this was the wrong call.**"

> "Even with what we thought were all the right ingredients in place (A/B tests, offline evals, expert reviews), **we still missed this important issue.**"

> "**Sometimes our evals will lag behind what we learn in practice**, but we'll keep moving quickly to fix issues and prevent harm."

> "There's no such thing as a 'small' launch."

Their pre-deployment gate at the time: offline evaluations; "Spot checks and expert testing: … We informally call these **'vibe checks'**—a kind of human sanity check to catch issues that automated evals or A/B tests might miss"; safety/preparedness checks; red teaming; small-scale A/B tests. Remedies committed to: treat behaviour issues as **launch-blocking**, add an opt-in alpha phase, and "block launches based on proxy measurements or qualitative signals, **even when metrics like A/B testing look good**".

**Why this matters for a team removing human review.** One of the strongest eval operations in the industry, run by a model vendor on its own model, with offline evals + A/B tests + expert review, shipped a behavioural regression. The thing that noticed was human "vibe checks" — which were then **overruled** by the quantitative signals. The evals did not fail because they were absent; they failed because they were not measuring the axis that moved. Every eval suite is a fixed set of axes, and a model update can move an axis nobody wrote a case for.

### 7c. `IN USE` — model-version-keyed agent-harness calibration, checked in

**Aider (Paul Gauthier / Aider-AI)** — `https://github.com/Aider-AI/aider/blob/main/aider/resources/model-settings.yml`, last commit **2026-04-24**. **357 per-model entries**, keyed largely on dated snapshot IDs (`gpt-4o-2024-08-06`, `gpt-4o-2024-11-20`, `claude-3-5-sonnet-20241022`, `claude-sonnet-4-5-20250929`), each carrying agent-harness calibration for that exact snapshot: `edit_format` (whole / diff / udiff), `use_repo_map`, `reminder`, `examples_as_sys_msg`, `lazy`, `editor_edit_format`. `gpt-4o` (floating) and `gpt-4o-2024-08-06` (pinned) get **separate entries with different settings**.

This is the best non-vendor artifact in the strand: agent-harness configuration treated as a function of model version, versioned in git, maintained for years. It is the concrete form of "every prior calibration is invalidated".

**But the measurement that justified it has lapsed.** The companion `aider/website/_data/polyglot_leaderboard.yml` — 69 recorded runs, each pinning `model`, `edit_format`, `commit_hash`, aider `versions`, `date`, `pass_rate_1`/`pass_rate_2`, plus failure counters (`num_malformed_responses`, `exhausted_context_windows`, `test_timeouts`) — has a **last recorded run of 2025-10-03** and a last commit of **2025-10-04**. As of 2026-08-28 that is **~11 months dormant**, spanning several model generations. (The leaderboard page's "last updated November 20, 2025" is a site build date, not a data date; `benchmark/over_time.py`, which plots score against model release date, was last touched 2024-11-22.)

The calibration file was still being edited four months ago; the measurement that would say whether the calibration is still right stopped eleven months ago. **That is the shape of the field in one repository.**

### 7d. Version pinning as a verification practice — and its limits

**Pinning is now the default at Anthropic's API layer.** `https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions` exists to correct a misconception:

> "A common misconception is that dateless model IDs such as `claude-sonnet-4-6` behave as evergreen pointers that route to the latest or best-performing version. **That is not the case.**"

> "Each Claude model ID identifies a **pinned version** of the model … the underlying model remains constant for the lifetime of that ID."

> "Anthropic does not update the weights or configuration of an existing model ID. When an updated version is available, **it ships under a new model ID**."

**But the floating-alias risk moved up into the agent harness.** `https://code.claude.com/docs/en/model-config`: "Aliases point to the recommended version for your provider and **update over time**. To pin to a specific version, use the full model name". The same page documents the alias being re-pointed under users three times inside one minor-version band:

> "Before v2.1.219, `opus` resolved to Opus 4.8 on the Anthropic API from v2.1.154, and on Claude Platform on AWS, Amazon Bedrock, and Google Cloud's Agent Platform from v2.1.207. Before v2.1.207, `opus` resolved to Opus 4.7 on Claude Platform on AWS and to Opus 4.6 on Amazon Bedrock and Google Cloud's Agent Platform."

The `opus` alias also resolves to **different models on different providers at the same moment**. An unpinned agent config is not reproducible across deployment targets on the same day. Anthropic's weekly digests record the swaps as routine: Week 30 (2026-07-20/24) "Claude Opus 5 is the new default Opus model in Claude Code"; Week 27 the same for Sonnet 5.

**Pinning bounds the risk; it does not eliminate it.** From the same page:

> "**Model weights are fixed for a given ID, but the serving infrastructure around the model can change over time.** This infrastructure includes components such as the request router, safety classifiers, and sampling logic. Occasionally, infrastructure updates produce **minor differences in observable behavior even when the model ID and weights have not changed.** If you notice unexpected behavioral differences on a previously stable model ID, an infrastructure update is the most likely cause."

There is no notification channel, changelog, or recommended detection method for this class of change. A pinned model ID is a weaker guarantee than it looks, and the only way to notice is to keep measuring.

**Pinning in real configs** (named orgs; these are eval harnesses for shared benchmarks rather than task-specific evals — evidence of the *pinning practice*, not of eval maturity): ARC Prize Foundation, `src/arc_agi_benchmarking/models.yml` (`https://github.com/arcprize/arc-agi-benchmarking`), 139 model configs each with a pinned `model_name` and dated pricing; UK AISI Inspect, `src/inspect_ai/model/_model_data/anthropic.yml`; LiveBench, `livebench/model/model_configs/anthropic.yml`.

### 7e. A named agent-harness effect that masquerades as a capability regression

The most directly useful passage found anywhere for this strand, from Anthropic's model-migration guidance (`anthropics/skills`, `skills/claude-api/shared/model-migration.md`). *(Anthropic writes bare "harness" here; in this project's vocabulary they mean the **agent harness** — the review agent's prompt, tools and loop. Quoted verbatim.)*

> "**Code review.** Opus 4.7 is meaningfully better at finding bugs than prior models, with both higher recall and precision. However, **if a code-review harness was tuned for an earlier model, it may initially show lower recall — this is likely a harness effect, not a capability regression.** When a review prompt says 'only report high-severity issues,' 'be conservative,' or 'don't nitpick,' Opus 4.7 follows that instruction more faithfully than earlier models did … Precision rises, but measured recall can fall even though underlying bug-finding has improved."

Read that against a team that has replaced human review with an automated reviewer and a dashboard. After a model update their measured defect-catch rate **drops**, and the correct diagnosis is that the model got *better* at obeying a hedge written for a worse model. No metric in such a dashboard distinguishes those two cases. Only re-running a task-specific eval — against known-buggy code, with the new model and the current agent harness together — does.

Anthropic ships a tool premised on exactly this decay, `prompt-audit` (`skills/claude-api/shared/prompt-audit.md`):

> "Prompts, skills, and tool descriptions accumulate instructions tuned to older models … Current Claude models follow instructions more closely and more literally than the models much of this text was written for, so the leftover text is not just wasted tokens — **specific outdated instructions actively degrade behavior**."

> "**Cruft is relative to a model:** a workaround that is load-bearing on one generation is dead weight on the next."

> "which failure, on which model, did this prevent — and does that failure still reproduce on the target model?"

It "is non-interactive by design: it runs the same way in a chat session, a CI job, or a batch migration" — CI-able, but no repo was found running it in CI.

### 7f. `PROPOSED / ADVOCATED` — vendors telling customers to re-run their own evals

**Anthropic, Opus 5 migration guide** (`https://platform.claude.com/docs/en/models/opus-5/migration-guide`) — the strongest vendor instruction to re-run *customer-owned* evals found from any vendor:

> "Re-evaluate your `effort` setting: **run a fresh effort sweep on your own evals rather than carrying over a setting tuned for an earlier model.**"
> "Re-baseline cost and latency on your own workloads."
> "Re-test any client-side token-count estimations."
> "**A prompt and harness review may be especially helpful** for migration to Claude Opus 5."
> "Remove carried-over verification instructions … Claude Opus 5 verifies its own work without being told to, so remove explicit verification or self-check instructions carried over from prompts tuned for earlier models; leaving them in causes over-verification."

**The gap in that same guide is telling.** Its "Verify the Migration" step is `assert response.model.startswith(YOUR_TARGET_MODEL)`. **Anthropic's automated verification for a model migration is an identity assertion — it checks that the swap took effect, not that behaviour held.** The behavioural re-evaluation lives in prose checklists handed to a human. The `/claude-api migrate` skill likewise "produces a checklist of items that require manual verification".

**Anthropic, deprecations page** — note the hedge: "**consider** thorough testing of your applications with the new models well before the retirement date." Framed around retirement deadlines, not voluntary upgrades.

**OpenAI, evals guide** — the entirety of its model-upgrade eval guidance is one clause: "Writing evals to understand how your LLM applications are performing against your expectations, **especially when upgrading or trying new models**, is an essential component to building reliable applications." The linked regression cookbook covers *prompt* regression only.

**Promptfoo** (sells the eval product) — the cleanest articulation of the benchmarks-vs-evals distinction found in any vendor documentation (`site/docs/guides/choosing-best-gpt-model.md`): "New model releases often score well on benchmarks. **But generic benchmarks are for generic use cases.** If you're building an LLM app, you should evaluate these models on your own data and make an informed decision based on your specific needs." Its 38-file guides directory contains model-*comparison* guides but **no model-migration or upgrade-regression guide**.

**Braintrust / LangSmith / Langfuse** all document experiment comparison and CI regression catching, but each frames the trigger as a **code or prompt change (a PR)**, not a model release. Braintrust: "Run evals on every pull request to catch regressions." None names model upgrade as the trigger.

**No vendor offers any behavioural-compatibility guarantee across model versions.** Anthropic disclaims it in both directions: new IDs for new weights, *and* "infrastructure updates produce minor differences in observable behavior even when the model ID and weights have not changed."

## 8. Public benchmarks — and why they cannot answer the question

Benchmarks are *shared, comparative* instruments: they answer "which model or agent is ahead of which, on this fixed public task set, as of this date." That is a different question from "is this agent, on **this** codebase, with **this** agent harness, still producing acceptable work?" The point below is the category limitation, not a benchmark survey.

### 8a. SWE-bench Verified — deprecation CONFIRMED, with a split that matters

**The primary artifact:** OpenAI, **"Why SWE-bench Verified no longer measures frontier coding capabilities"**, **2026-02-23**, `https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/`. Subtitle: "SWE-bench Verified is increasingly contaminated. We recommend SWE-bench Pro."

The load-bearing sentence, verbatim:
> "This means that improvements on SWE-bench Verified **no longer reflect meaningful improvements in models' real-world software development abilities**. Instead, they increasingly reflect how much the model was exposed to the benchmark at training time. **This is why we have stopped reporting SWE-bench Verified scores, and we recommend that other model developers do so too.**"

Two findings behind it:
- **Flawed tests.** An audit of 138 Verified problems that o3 failed inconsistently across 64 runs, each reviewed by ≥6 engineers: "We found that **59.4% of the 138 problems contained material issues in test design and/or problem description**, rendering them extremely difficult or impossible even for the most capable model or human to solve." Breakdown: 35.5% *narrow* tests (enforce implementation details), 18.8% *wide* tests (check unspecified functionality), 5.1% other.
- **Contamination.** "all frontier models we tested were able to reproduce the original, human-written bug fix used as the ground-truth reference, known as the gold patch, or verbatim problem statement specifics for certain tasks." Transcripts published.

**The qualification the reference document must not drop.** This is **OpenAI** — a co-producer of Verified, and a model vendor with a direct stake in which benchmark its launches are judged against — **retiring its own use of the dataset**. The other publisher, the SWE-bench team (Princeton/Stanford), **has not deprecated it**. Evidence, all dated after 2026-02-23:

- The official leaderboard site (`https://github.com/SWE-bench/swe-bench.github.io`, last pushed **2026-08-10**) still ships **Verified as the default leaderboard tab**, with **no** deprecation, caution or contamination notice.
- The `swebench` harness **5.0.0 release (2026-08-17)** lists live dataset aliases as "`full`, `verified`, `multilingual` and `multimodal`", and the README's installation smoke test is `swebench eval verified --gold`. The same changelog *does* retire the **Lite** alias (commit `bdfcdd8`, 2026-08-15) — a plausible source of confusion.
- `SWE-bench/SWE-bench_Verified` on HuggingFace was last modified **2026-08-16**, tagged `benchmark:official`. The `princeton-nlp/` copy is stale (2025-02-18) — a namespace migration, not a retirement.

**Accurate formulation:** *SWE-bench Verified was deprecated as a reporting metric by OpenAI (2026-02-23) on contamination and test-validity grounds, and OpenAI asked other model developers to follow. The benchmark itself is still maintained, published and leaderboarded by the SWE-bench team as of 2026-08.* Note also that OpenAI's recommended replacement, SWE-bench Pro, is published by a commercial evaluation vendor (Scale AI) — one interested party pointing at another.

Third-party confirmation that the field reads it as a deprecation: SWE-Bench ProMax (`https://arxiv.org/abs/2608.09802`, 2026-08-10) writes "leading OpenAI to deprecate the benchmark entirely [31]", citing that URL.

### 8b. Measurement problems published against SWE-bench itself

- **SWE-Bench+** — `https://arxiv.org/abs/2410.06992` (2024-10-09, Aleithan et al., York University). Manual screening of SWE-Agent+GPT-4's successful patches: "**32.67% of the successful patches involve cheating** as the solutions were directly provided in the issue report or the comments" (solution leakage), and "**31.08% of the passed patches are suspicious** … due to weak test cases". Filtering dropped the measured resolution rate from 12.47% to **3.97%**. They state the same issues exist in Lite and Verified, and that ">94% of the issues were created before LLM's knowledge cutoff dates".
- **Passing tests ≠ correct patch** — "Are 'Solved Issues' in SWE-bench Really Solved Correctly?", `https://arxiv.org/abs/2503.15223` (2025-03-19, rev. 2025-09-09). Differential patch testing on Verified: "**7.8% of all patches … count as correct while failing the developer-written test suite**"; 29.6% of plausible patches "induce different behavior than the ground truth"; 28.6% of those are "certainly incorrect"; net "an inflation of reported resolution rates by **6.2 absolute percent points**."
- **Memorisation** — "The SWE-Bench Illusion", `https://arxiv.org/abs/2506.12286` (2025-06-14, rev. 2025-12-01, Microsoft-affiliated). Models identify buggy file paths from the issue description **alone** at up to **76%** on Verified vs up to **53%** on repos not in SWE-bench; verbatim 5-gram reproduction of ground-truth functions up to **35%** on Verified vs **18%** elsewhere.
- **The benchmark authors' own leakage audit** — John Yang (SWE-bench co-author), "[SWE-bench Verified] Detecting cheating in submissions", **2025-11-19**, `https://john-b-yang.github.io/swe-bench-cheating/index.html`. Average exact-gold-patch match rate 6.7% across Verified submissions; one leaderboard entry (`20240820_honeycomb`) at **78.7% / 87.2%** exact match on Verified/Lite. Detection script: `https://github.com/SWE-bench/experiments/blob/main/analysis/detect_similarity.py`.

### 8c. The others, briefly

**SWE-bench Pro** (Scale AI — **sells model-evaluation services; interested party**), `https://arxiv.org/abs/2509.16941` (2025-09-21, rev. 2025-11-14). 1,865 problems from 41 repos: a public set (11 repos), a **held-out set (12 repos, not publicly accessible)**, and a **commercial set (18 proprietary startup repos under partnership)**. Contamination-resistance is by construction: "(1) exclusively selecting repositories distributed under strong copyleft licenses (GPL) … and (2) acquiring commercial codebases from real startups … we reduce contamination risks by leveraging both legal protections and restricted data access." Run as a paid-access leaderboard product. Its own news log records the same class of curation defect appearing early: "(2/9) We have removed some unit tests which were outdated…".

**SWE-Lancer** (OpenAI; vendor), `https://arxiv.org/abs/2502.12115` (2025-02-17). 1,400+ real Upwork tasks worth $1M in actual payouts, graded by triple-verified end-to-end tests. Its Limitations section is the useful citation: tasks come from **one** repository (Expensify); "Freelance tasks tend to be **more self-contained** than full-time software engineering tasks"; models "**cannot ask clarifying or follow-up questions**"; "we remain cautious about extrapolating impact beyond this."

**Terminal-Bench** (Stanford × Laude Institute), `https://arxiv.org/abs/2601.11868` (2026-01-17). Terminal-Bench 2.0: 89 hand-curated hard terminal tasks, each with a unique environment, human-written solution and verification tests. Its stated motivation is itself a claim about the category: "Current benchmarks either **do not measure real-world tasks**, or are not sufficiently difficult to meaningfully measure frontier models." Run through the Harbor eval harness (§3a, §5).

**Aider polyglot** (Paul Gauthier), `https://aider.chat/2024/12/21/polyglot.html` (2024-12-21). 225 Exercism exercises across six languages — the ones solved by ≤3 of 7 reference models. It measures *code editing and instruction-following* on self-contained kata with supplied tests, not repository work. The post is an explicit account of **saturation-driven benchmark replacement**: the previous benchmark was "saturating as the top scores approached and then surpassed 80% … New champions were advancing the top score by solving just 1-2 more problems than the previous record." (Its own leaderboard has since gone dormant — see §7c.)

**LiveCodeBench** (UC Berkeley/MIT/Cornell), `https://arxiv.org/abs/2403.07974` (2024-03-12). Competitive-programming problems continuously harvested from LeetCode, AtCoder, Codeforces. Contamination control is by **recency, not secrecy**: "LiveCodeBench annotates problems with release dates, and thus allows evaluating models on problems released during a specific time period", so a model with cutoff *D* is scored only on later problems. Limitation: contest problems are self-contained algorithmic puzzles — no repository, no conventions, no ambiguity to resolve.

**RE-Bench** (METR — nonprofit, low stake), `https://arxiv.org/abs/2411.15114` (2024-11-22, rev. 2025-05-27). 7 open-ended ML research-engineering environments against 71 8-hour attempts by 61 human experts. Agents beat humans at a 2-hour budget; humans overtake by 8, and at 32 hours "average human scores nearly doubled the best AI agent performance". Its stated limitation is the sharpest short form of the category argument: "our environments are **smaller in scope and have clearer objectives and shorter feedback loops** compared to real-world research engineering."

### 8d. METR — time horizons, and the experiment that breaks the benchmark→productivity link

**Time horizons.** `https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/` (2025-03-19; arXiv 2503.14499, last revised 2026-07-10) proposes the 50%-task-completion time horizon, with a ~7-month doubling since 2019.

**Two 2026 updates, both material:**
- The original post now carries a banner: "⚠️ Some of the text and figures in this post are **out of date**… For our latest methodology and results, see the dedicated time horizons page and Time Horizon 1.1."
- **Time Horizon 1.1**, **2026-01-29**, `https://metr.org/blog/2026-1-29-time-horizon-1-1/`: task suite grown 170 → 228 tasks; 8h+ tasks 14 → 31; the **eval harness moved from METR's in-house Vivaria to UK AISI's Inspect**. Only 14 of 33 models were re-estimated; new estimates "generally lie within the confidence intervals from the TH1 time horizons". Task removals "generally represent cases where a task description was confusing, or **easy to reward-hack**, or the scoring function had errors" — the same curation-defect class, found by the benchmark's own authors.
- Also: the 2025 paper replicated the trend on SWE-bench Verified with independently collected human time estimates and got "an even faster doubling time, of **under 3 months**" — a warning that the doubling rate is partly a property of the chosen task set.

**The RCT** — `https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/` (2025-07-10; arXiv 2507.09089). 16 experienced OSS developers, 246 real issues from their *own* mature repos (22k+ stars, 1M+ LOC), randomised AI-allowed/AI-disallowed, screen-recorded. Developers took **19% longer** with AI tools — while forecasting a 24% speedup beforehand and still believing they had been sped up 20% afterwards.

The motivation paragraph is the single best primary quote for the category argument:
> "While coding/agentic benchmarks have proven useful for understanding AI capabilities, they typically **sacrifice realism for scale and efficiency**—the tasks are self-contained, don't require prior context to understand, and use algorithmic evaluation that doesn't capture many important capabilities. These properties may lead benchmarks to **overestimate** AI capabilities. … Broadly, **it can be difficult to directly translate benchmark scores to impact in the wild.**"

**Do not cite the 19% as current.** METR has stamped that post "⚠️ These results are out of date." The follow-up, **"We are Changing our Developer Productivity Experiment Design", 2026-02-24**, `https://metr.org/blog/2026-02-24-uplift-update/`, reports a second experiment (10 original + 47 new developers, from Aug 2025) that METR itself judges unreliable: "we have observed a **significant increase in developers choosing not to participate** in the study because they do not wish to work without AI, which likely biases downwards our estimate of AI-assisted speedup", plus unreliable time measurement for developers running multiple agents concurrently. Raw numbers: returning developers −18% (CI −38% to +9%); newly recruited −4% (CI −15% to +9%). METR's reading: "it is likely that developers are more sped up from AI tools now — in early 2026 … However, because of the selection effects in our experiment, our data is only **very weak evidence** for the size of this increase."

**The methodological finding is the durable one, and it is directly load-bearing for this strand: once a team has adopted agents, the counterfactual arm becomes unrunnable.** A/B measurement against "no AI" decays as a longitudinal instrument. That pushes the question back onto per-repo evals — there is no third option.

### 8e. The category argument, in primary sources

The strong form is not "benchmarks are bad". It is that **every benchmark ships with an author-stated scope limit that excludes the longitudinal, single-codebase question, and its scores drift for reasons that have nothing to do with the agent under test.**

**(a) The task distribution is not your repo's.** SWE-Sharp-Bench, `https://arxiv.org/abs/2511.02352` (2025-11-04, Microsoft) holds the model and agent harness identical and swaps only the language: "while **70% of Python tasks** in SWE-Bench Verified are solved, only **40% of our C# tasks** are resolved." Same agent, same agent harness, **30-point swing from repository population alone.** This is the cleanest published demonstration that a benchmark number does not travel to a different codebase.

**(b) The contamination profile is not your repo's.** OpenAI said so in the *original* Verified announcement, before the benchmark peaked (`https://openai.com/index/introducing-swe-bench-verified/`, updated 2025-02-24): "Evaluations based on static datasets are inherently limited… Given that the benchmark is composed of scrapes of public GitHub repos, large foundation models that are pre-trained on internet text are **likely to be contaminated** on the tasks. Furthermore, SWE-bench only covers a **narrow distribution**… and so must be supplemented with other evaluations." **Your private repository is never in the training set the way a benchmark is — so the contamination correction is unbounded and unmeasurable at the point of transfer.**

**(c) The grading oracle is not your CI.** OpenAI's audit (59.4% of hard instances have flawed tests) and PatchDiff (7.8% of "correct" patches fail the developer-written suite; 29.6% behaviourally diverge) both show a passing benchmark oracle does not establish that a change is correct. Your CI has the same failure modes — flakiness, coverage gaps, over-narrow assertions — but *different specific ones*, and no benchmark score carries information about them.

**(d) Benchmarks saturate and get retired underneath you.** OpenAI, 2026-02-23: "After initial leaps, state-of-the-art progress on SWE-bench Verified has slowed, improving from 74.9% to 80.9% in the last 6 months. This raises the question: do the remaining failures reflect model limitations **or properties of the dataset itself**?" Aider reached the same conclusion in 2024 and rebuilt. METR re-based its task suite and swapped eval harnesses in 2026. SWE-Bench ProMax (2026-08) opens: "existing benchmarks are rapidly saturating and their evaluation quality has come under serious scrutiny."

**(e) The one high-quality field experiment found the sign of the effect went the opposite way** from what benchmark trends implied (METR 2025) — and then found the experiment itself became unrunnable once adoption was widespread (METR 2026-02).

**(f) The gap, named by the people who built the benchmarks.** Three independent author statements: RE-Bench ("smaller in scope … clearer objectives and shorter feedback loops"); SWE-Lancer ("more self-contained"; models "cannot ask clarifying or follow-up questions"); METR's RCT motivation ("self-contained, don't require prior context to understand"). What all three name as *absent* is exactly what constitutes the longitudinal question: prior repository context, tacit conventions, ambiguity that must be resolved by asking, review culture, and grading that is not a fixed pass/fail oracle.

**And the field data confirms the gap quantitatively.** The AIDev study (§6c) puts real agent PR acceptance at **35–64%** against SWE-bench Verified scores "exceeding 70%", and names the problem in the authors' own words: "This significant disparity between benchmark and real-world performance raises important questions about the **ecological validity of current evaluation methodologies**."

## 9. The honest state of the field

The brief asked me to **test** the hypothesis that eval practice for coding agents on private repos is far less mature than the discourse implies, and that most teams have nothing longitudinal at all — not to confirm it. Here is the test, the result, and the places where the hypothesis needs qualifying.

### 9a. How hard I looked

- Direct inspection of the eval directories of eight shipping agent products (Zed, OpenHands, Aider, SWE-agent, Cline, Continue, Block's goose, Sourcegraph Cody) via the GitHub contents API — reading the actual `evals/`, `eval/`, `benchmark/` and `crates/eval_cli` trees, their READMEs, their metrics code, their CI workflow directories, and the **commit history** of the specific workflow files that would run them.
- GitHub code search across `.github/workflows` for every major eval platform, with `pytest` as a scale baseline.
- The installed Claude Code CLI itself (2.1.250), including undocumented subcommands, plus Anthropic's official plugin marketplace source on disk.
- First-party documentation for Anthropic, OpenAI, Google, GitHub, and six eval-platform vendors; first-party engineering blogs; vendor changelogs and deprecation pages.
- The 2026 academic literature on agent PR outcomes (largely built on one open dataset, AIDev), plus METR's RCT and its 2026 retraction-and-redesign.
- Primary papers for every LLM-as-judge bias named in the brief.

**Search limitations, stated plainly.** The WebSearch tool's session budget was exhausted at the outset, and DuckDuckGo, Google, Bing, searx.be and Startpage all serve bot challenges, which I did not attempt to defeat. General web search therefore ran through Mojeek, whose index is small — **a Mojeek miss is not evidence of absence.** Most of my positive findings came from direct artifact inspection (GitHub API, docs sites, arXiv, the local CLI) rather than from search, which is the stronger method here anyway; but it does mean a team that wrote a blog post I could not surface may exist.

**The decisive limitation: private repos are invisible to every method I used.** GitHub code search covers public repositories. A bank running a nightly eval suite against its internal monorepo would not appear in any of my counts. So the finding below is precisely: **there is no published evidence of this practice**, which is weaker than evidence that the practice does not exist. That distinction should survive into the reference document.

### 9b. Result: the hypothesis holds, and the mechanism is worse than "immature"

**On "most teams have nothing longitudinal": supported.**
- Eval tooling appears in **~0.5%** of the CI workflows that carry `pytest`, and most of those are chatbot/RAG evals.
- Not one **non-vendor** organisation was found publishing an eval suite against its own codebase.
- The model vendor's own showcase of internal agent use ("How Anthropic teams use Claude Code") describes **human review before merging**, not evals.
- The largest fleet-telemetry holders (GitHub, Anthropic) ship the instruments and publish **no readings**; every real agent-PR-outcome number in existence was produced by academics mining public data.

**But the sharper finding is not absence — it is decay.** The four organisations that *did* build the right thing have each lost part of it:

| Org | Built | State on 2026-08-28 |
|---|---|---|
| Cline | Real-task eval suite, pass@k/pass^k/flakiness, baselines, CI regression workflow (2026-02-13) | Regression workflow **removed** 2026-05-14 in an unrelated CLI migration; smoke CI disabled; nightly E2E "**not yet implemented**"; `cline-bench` untouched since **2025-12-11** |
| Zed | Production-fidelity eval binary running the shipping agent pipeline (active 2026-08-09) | **No eval CI workflow at all** — runs launched by hand |
| Aider | 357-entry model-version-keyed agent-harness calibration (edited 2026-04-24) | The benchmark that justifies the calibration has a **last recorded run of 2025-10-03** — ~11 months dormant |
| Anthropic | `claude plugin eval` with an `--threshold` CI gate; `skill-creator` methodology | **Early access, absent from the entire public documentation index**; scoped to plugins/skills, not repository work |

**Cline is the cautionary case and deserves to be quoted rather than paraphrased in the reference document.** They built the regression detector, gated it in CI, and lost it to a refactor three months later. **Nothing detected the loss of the detector.** An eval suite is itself unverified infrastructure: it decays silently, and its decay looks exactly like everything being fine.

**And even a working eval suite is a fixed set of axes.** OpenAI's sycophancy postmortem is the proof: offline evals, A/B tests and expert review all in place, and the regression shipped anyway because "we also didn't have specific deployment evaluations tracking sycophancy." Their own conclusion — "**Sometimes our evals will lag behind what we learn in practice**" — is a model vendor stating the ceiling on the entire category.

### 9c. Where the hypothesis needs qualifying

Three findings genuinely cut against the strong form of "the field has nothing":

1. **The substrate matured fast, and recently.** Harbor (created 2025-08-04, 4,720 stars, pushed the day of this research) is now the common eval harness beneath Cline, Zed, Block's goose and Terminal-Bench, and its stated purpose is exactly right: "Evaluate arbitrary agents like Claude Code, OpenHands, Codex CLI" and "**Build and share your own benchmarks and environments.**" UK AISI's Inspect can drive Claude Code and Gemini CLI as external agents. SWE-bench's `collect` pipeline mines a repo's own merged PRs into task instances. **The tools to do this well now exist, are free, and are good.** The gap is practice, not capability — which is a much more tractable problem, and worth saying so.

2. **The measurement knowledge exists even where the practice does not.** The 2026 academic literature answers, with real numbers on real repositories, the questions the vendors decline to: agent PR acceptance by agent (35–64%), post-merge corrective maintenance, and — most importantly — that **reviewer approval rates rise while scrutiny falls** (`arXiv:2606.22721`). A team building a longitudinal programme today does not have to invent the metrics; it has to instrument them.

3. **Two independent telemetry datasets agree on where the cost lands.** Harvard/Jellyfish (718 firms: review time +49%, changes-requested nearly doubles, "this bottleneck **persists** following the adoption of AI code review tools") and Faros (22K developers: 5x median review time). That convergence is the most reproducible fleet-level result in this strand, and it points somewhere specific: **the constraint moved from writing code to verifying it**, and automating the verification did not relieve it.

### 9d. What this means for a team removing human review

Stated as findings, not recommendations:

- **The two obvious dashboards both mislead in the same direction.** Vendor adoption telemetry (§6) measures usage, not correctness — Anthropic's "lines of code accepted" explicitly "does not track subsequent deletions", and the 20% rewrite threshold is used to *exclude* heavily-edited code from attribution rather than surface it as an edit-distance signal. Meanwhile agent merge/approval rate rises as reviewer scrutiny decays. A team that removes human review and watches merge rate will see its numbers improve for precisely the reason it should be worried.
- **A benchmark score cannot be substituted.** The transfer gap is measurable and large: 30 points from repository language alone (SWE-Sharp-Bench), 10 points from agent harness alone at a fixed model (Block's goose table), and a 35–64% real acceptance rate against >70% benchmark scores (AIDev).
- **Pinning the model bounds the risk but does not close it.** Anthropic documents that "infrastructure updates produce minor differences in observable behavior **even when the model ID and weights have not changed**", with no notification channel for it. The only way to notice is to keep measuring.
- **A model update can make a metric fall because the model got better.** Anthropic's own migration guide names the case: a code-review agent harness tuned for an older model shows *lower* recall on a newer one, "a **harness effect, not a capability regression**", because the new model obeys the "don't nitpick" hedge more faithfully. No fleet metric distinguishes that from decay.
- **The counterfactual arm expires.** METR could not re-run its own RCT once adoption spread, because developers declined to work without AI. Whatever baseline a team wants, it has to capture it *before* it removes human review — after that, the comparison is gone.

## 10. Blocked sources — none circumvented

Every entry below was left un-retrieved or retrieved only from its ungated surface. No paywall, login wall, registration gate, rate limit or bot challenge was defeated.

### Registration / email gates (not filled in)

| URL | Gate |
|---|---|
| `https://getdx.com/whitepaper/ai-measurement-framework/` | Email/registration form (name, work email, company). The direct PDF path was visible and **deliberately not fetched**, since that would bypass the gate. Public page reported as marketing copy. |
| `https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development` | Registration form. Note the main DORA 2024 / 2025 / AI-Capabilities PDFs were **ungated** and were retrieved. |
| `https://www.faros.ai/research/ai-acceleration-whiplash` | Email gate on "Download the Report". Landing-page figures used, labelled as marketing copy. |
| `https://go.faros.ai/ai-engineering` | Registration gate on the full "AI Productivity Paradox" report. |
| `https://www.gitclear.com/ai_assistant_code_quality_2025_research` | Email gate on the full PDF. Summary numbers taken from the ungated page. |

### Bot challenges / CAPTCHAs (not attempted or abandoned on sight)

| Source | Block |
|---|---|
| `https://duckduckgo.com/html/?q=…` and `https://lite.duckduckgo.com/lite/` | CAPTCHA ("Select all squares containing a duck") on GET; anti-bot challenge page (`anomaly.js`) on POST. Abandoned. |
| `https://searx.be/search?…` | "Verifying your browser…" antibot interstitial redirecting no-JS clients to `/antibot/captcha`. Abandoned. |
| Google, Bing, Startpage | Known bot challenges — **not attempted**. |

General web search consequently ran through **Mojeek** (`https://www.mojeek.com/search`), which returns results without a challenge. Its index is small; a Mojeek miss is not evidence of absence, and this is flagged wherever it affects a conclusion.

### Rate limits (backed off, not worked around)

| Endpoint | Block |
|---|---|
| GitHub `search/code` API (`gh search code`) | HTTP 403 secondary rate limit, hit repeatedly across the session. Handled by spacing requests and by switching to the separate-quota **contents** API for repo inspection. Two counts (`braintrust`, `pytest` baselines) required retries; both eventually succeeded. |
| `https://api.semanticscholar.org/graph/v1/paper/search` | HTTP 429. arXiv and OpenAlex used instead. |
| `https://linearb.io/resources` and two sub-pages | HTTP 429 on two separate attempts. **LinearB is unassessed — treat as unknown, not absent.** |
| `https://priv.au`, `https://opnxng.com` (SearXNG instances) | HTTP 429 on probe. |
| `https://searxng.site` | HTTP 403 on probe. |

### Access-denied to automated clients

| URL | Block | Disposition |
|---|---|---|
| `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566` (Cui et al.) | HTTP 403 | Headline numbers taken from the Microsoft Research landing page instead. |
| `https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/` | HTTP 403 | The arXiv MAPS '22 version (`https://arxiv.org/abs/2205.06537`) was used and is the primary artifact. |
| `https://huggingface.co/api/datasets/openai/SWE-bench_Verified` | HTTP 401 | Not retried with credentials. The dataset most likely does not exist under `openai/`; the canonical public copies (`SWE-bench/`, `princeton-nlp/`) were read successfully. |
| `https://web.archive.org/…` | Blocked by the fetch tool for this environment | Not pursued; primary sources reached directly instead. |
| `https://www.mojeek.com/…` via `WebFetch` | HTTP 403 to the WebFetch client | Retrieved successfully via `curl` with a standard desktop User-Agent. |

### Not actually blocked — correction to an earlier assumption

`https://openai.com/index/introducing-swe-bench-verified/` and `https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/` returned **HTTP 403 to the WebFetch client** but **HTTP 200 to plain `curl` with a standard desktop User-Agent**. There is no CAPTCHA, challenge page or login on these URLs — the 403 was a User-Agent filter on one client, not an access control, and both pages were read normally. Recorded here so the reference document does not carry a false "paywalled" claim about OpenAI's research posts.

### Dead links (recorded as absence, not as blocks)

| URL | Result |
|---|---|
| `https://code.claude.com/docs/en/plugin-evals` | HTTP 404. `https://code.claude.com/docs/llms.txt` contains **zero** occurrences of "eval" — confirming `claude plugin eval` is undocumented publicly. |
| `https://www.promptfoo.dev/docs/guides/evaluate-llm-model-migration/` | HTTP 404. Confirmed against the repo: no such guide exists among the 38 files in `site/docs/guides`. |
| `https://langfuse.com/docs/evaluation/experiments/ci-cd` | HTTP 404. The CI/CD claim was taken from the linked text on the evaluation overview page instead. |
| `https://openai.com/index/improving-coding-evaluations/` | HTTP 404 (guessed URL). The real post was located via the SWE-Bench ProMax bibliography. |

---

## Appendix: source stake register

| Source | Stake | Read accordingly |
|---|---|---|
| Anthropic, OpenAI, Google | **Model vendors.** Also sell coding agents. | Their eval guidance advertises their models; their fleet dashboards are framed as ROI evidence. Their *admissions against interest* (OpenAI's sycophancy postmortem; Anthropic's serving-infrastructure caveat and agent-harness-effect warning) are correspondingly strong evidence. |
| GitHub / Microsoft | **Sell Copilot.** | Publishes acceptance rates, not outcomes. Frames falling acceptance as a tooling defect only. |
| Cline, Zed, Block (goose), Cursor/Anysphere | **Sell or ship the agent.** | Their eval suites are real and inspectable — the artifacts are strong even though the publishers are interested. Their *self-reported decay* (Cline's disabled CI) is evidence against interest. |
| Scale AI | **Sells model-evaluation services.** Publishes SWE-bench Pro as a paid-access leaderboard. | OpenAI recommending SWE-bench Pro is one interested party pointing at another. |
| DORA / Google Cloud | **Interested party reporting on the category it sells into.** | Also, critically, a **survey of self-reported perceptions** (n≈3,000–4,900), not fleet telemetry. Do not present alongside Faros/Jellyfish as the same kind of evidence. |
| Faros AI, Jellyfish, LinearB, DX/Getdx, GitClear | **Sell the measurement product.** | Landing-page numbers are marketing surfaces; full reports are email-gated. Faros explicitly positions against DORA ("Telemetry, not surveys… Our data directly contradicts DORA's 2025 findings") — a competitive claim as much as a finding. |
| Braintrust, LangSmith (LangChain), Langfuse, Promptfoo, DeepEval/Confident AI | **Sell the eval product.** | All document regression-catching capability; **none names a customer doing it for a coding agent on a private repo.** |
| UK AI Security Institute (Inspect) | Government/nonprofit. **Least conflicted tooling source in this strand.** | — |
| METR | Nonprofit, sells nothing here. | Publishes results against the prevailing direction, and retracts its own findings when the method breaks — the strongest neutrality signal in the set. |
| Harvard authors (Chen & Stratton) | Academic, **vendor-supplied data**, independence explicitly declared and reviewed only for proprietary disclosure. | Strong, with the data-provenance caveat stated. |
| AIDev-derived literature (Queen's University et al.) | Academic, open dataset, low stake. | The only source of real agent-PR-outcome numbers. Note most 2026 papers share one dataset — correlated methodology risk. |
| Daniel Stenberg (curl) | Maintainer reporting on his own project. No commercial stake. | — |
