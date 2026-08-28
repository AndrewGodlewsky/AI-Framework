# Test rigor and the circularity problem

Research strand for the reference document on what engineered verification must replace human reading
as AI coding agents are given more autonomy.

Compiled **2026-08-28**. Repository files are quoted from their default branch as of that date. Where
I could not establish when a specific line was authored, I say so.

---

## Summary

### What I found

**The circularity problem is real, measured, and the measurements are bad.** Three venue-accepted or
peer-reviewed studies (2024–2026) establish it. When a model is shown code containing a bug and asked
to write tests for it, it writes tests that *ratify the bug*: bug-detection drops **47% on real-world
code** versus tests generated from correct code (arXiv:2409.09464). An ISSTA 2026 paper defines and
quantifies a **"misguidance effect"** in which buggy code simultaneously increases wrong assertions
and *suppresses* the tests that would find the bug (arXiv:2607.22883). And a 2024 study of the
shipping tools (Codium CoverAgent, CoverUp) found that their designs **reject bug-revealing tests by
construction** — a generated test that fails is discarded as a bad test, so the pipeline cannot
produce a failing one even in principle (arXiv:2412.14137).

**Against that, there is a real and growing body of committed policy that treats the agent's own tests
as untrustworthy and puts an independent check on them.** Verified in operation, with CI configs I
read: diff-scoped mutation gates (`thepartly/gatehouse`, `prestomation/ha-home-keeper`,
`audreyt/ethercalc`); red-green enforcement written into agent policy at Microsoft, Apache Airflow and
styled-components; **external-oracle grounding** (styled-components requires the agent to fetch the
CSS Working Group editor's draft and quote the normative clause above the test it writes);
differential oracles (`vercel-labs/scriptc`, `tursodatabase/turso`); human-adjudicated golden files
(Apache Spark); and **protected judges** the builder agent is structurally forbidden to edit
(`coleam00/skills`). Anthropic's own documentation names the circularity problem and prescribes
separation of duties: *"a fresh model try to refute the result, so the agent doing the work isn't the
one grading it."*

**The strongest single line of practice is a substitution, not an addition.** Across independent
projects the same replacement keeps appearing: stop asking *"is this line covered?"* and start asking
**"would this test fail if the change were reverted?"** Apache Airflow, `phase-rs/phase`, `nWave-ai`,
`coleam00/skills` and `rshankras` all converge on it without citing each other.

### What I looked for and could NOT find

These absences matter more than several of the positive findings.

1. **Nobody has measured whether an agent's tests catch that same agent's bugs.** Every measurement I
   found is a different experiment: tests generated for *known-buggy* code (2409.09464, 2607.22883),
   tests generated to reproduce a bug *described in a ticket* (SWT-Bench, TDD-Bench), or LLM tests
   versus human tests on a *curated* bug set (2606.08588). The specific experiment — let an agent
   write a feature and its tests unsupervised, inject nothing, and count how many of its own defects
   its own suite caught — does not appear to exist. **This is the central empirical gap in the
   strand.**
2. **No coverage bar tied to how much the agent is trusted.** Not one artifact says anything of the
   form "the agent may merge unattended at X%, needs a human at Y%". See §2.
3. **Property-based testing is essentially absent as an agent-verification argument.** PBT is widely
   *used* in repos that also carry an AGENTS.md, but I found no primary source arguing PBT is
   warranted *because* an agent wrote the code. Hypothesis' documentation and its lead developer's
   site say nothing about LLMs — **and he works at Anthropic**. See §3.
4. **cargo-mutants' author has not written about LLMs.** I grepped the entire repository — 80 Markdown
   files, the whole book, NEWS.md, DESIGN.md, CONTRIBUTING.md — plus the issue tracker. The only match
   in the tree is the title line of `AGENTS.md`. See §4d.
5. **No mechanically verified red phase.** Many AGENTS.md files require the agent to see the test fail
   first. I found no agent harness, hook, or CI job that *checks* this — no job that applies only the
   test to the parent commit and asserts a non-zero exit. It is prose everywhere.
6. **No mechanism anywhere that detects an agent weakening its own verification.** Named
   independently by two of the three research threads. See §7.

### The framing worth stealing

Marc Brooker (AWS) reduces the whole problem to an oracle problem —
https://brooker.co.za/blog/2026/05/20/hypothesis.html (2026-05-20), his "Agentic Software Development
Hypothesis", verbatim in three forms:

> **Weak form:** "Any coding task for which a complete specification is available will become trivial."
> **Strong form:** "Any coding task for which a deterministic oracle is available will become trivial."
> **Strongest form:** "Any coding task for which a non-adversarial (*pythic?*) oracle exists will
> become trivial."

Read that way, this strand asks exactly one question: **where does the oracle come from, if not from
the agent that wrote the code?** Every mechanism below is an answer to it, and the answers rank by how
independent the oracle is of the agent.

---

## 1. The circularity problem

### 1a. What has actually been measured

None of this is vendor material; all are academic papers, three venue-accepted.

**IN USE — measured findings**

- **Tests generated from buggy code ratify the bug.** *"Measuring the Influence of Incorrect Code on
  Test Generation"*, Dong Huang, Jie M. Zhang, Mark Harman, Mingzhe Du, Heming Cui. Submitted
  2024-09-14, rev. 2025-03-28. https://arxiv.org/abs/2409.09464 — 5 open and 6 proprietary models,
  three benchmarks plus 41 real repositories. Versus correct code as input, incorrect code yields
  **57% worse test accuracy, 12% worse coverage, 24% worse bug detection** on benchmarks, and
  **47% worse bug detection on real-world code**. Supplying a natural-language description of intent
  recovers **+34% bug detection** — the empirical case for spec-grounded tests.

- **The misguidance effect, quantified.** *"Evaluating and Mitigating the Misguidance Effect of Buggy
  Code in LLM-Generated Unit Tests"*, Junda Zhao, Shurui Zhou, Eldan Cohen. **Accepted at ISSTA 2026**;
  arXiv 2026-07-24. https://arxiv.org/abs/2607.22883 — introduces a metric for the effect and reports
  a *twofold* harm: buggy code both raises the count of tests asserting wrong behaviour and
  **suppresses** generation of bug-finding tests. Analysis of model internals shows preferences skew
  toward tests validating the erroneous behaviour. Their mitigation: replace the code in the prompt
  with a generated **specification docstring** — break the loop by not showing the implementation to
  the test author.

- **The shipping tools are designed to reject bug-revealing tests.** *"Design choices made by
  LLM-based test generators prevent them from finding bugs"*, Noble Saji Mathews, Meiyappan Nagappan,
  2024-12-18. https://arxiv.org/abs/2412.14137 — examines Codium **CoverAgent** and **CoverUp**.
  Because a generated test that fails is treated as a *bad test* and discarded, the tools
  *"validat[e] bugs in the generated test suite and reject[] bug-revealing tests."* This is the
  mechanism of circularity stated exactly.

- **Coverage and mutation score stop predicting fault detection once the code may be buggy.**
  *"Do Coverage and Mutation Scores of LLM-Generated Test Suites Correlate with Their Effectiveness?
  (Replicability Study)"*, Zhao, Zhou, Cohen. **Accepted ISSTA 2026**, ACM PACMSE; arXiv 2026-07-24.
  https://arxiv.org/abs/2607.22880 — verbatim:
  > "the usefulness of coverage and mutation is **highly context-dependent**: in regression-style
  > settings where the code provided to the LLM can be reasonably assumed bug-free, these metrics
  > **can provide meaningful signals** when comparing across models; in another common scenario where
  > the code-under-test may already be buggy and the goal is to expose the bug within the
  > code-under-test, they no longer serve as reliable indicators. We also find **little evidence that
  > test suite size is a dominant confounder**."

  This is a replication of Inozemtseva et al. and Papadakis et al. — the studies usually cited to kill
  coverage — and it *partially rescues* coverage for the regression case while dissolving the
  size-confounder argument. Anyone writing "coverage is discredited for agent code" has to reckon
  with it.

- **LLM tests beat generic human tests at fault detection, at identical coverage.** *"LLM vs. Human
  Unit Tests: Fault Detection on Real Python Bugs"*, Phouvadeth Vathana, Prapti Bhatt, Rishi Patel,
  Nasir U. Eisty, 2026-06-07. https://arxiv.org/abs/2606.08588 — verbatim:
  > "line and branch coverage are nearly identical between the two approaches (84.8% vs. 88.5% and
  > 75.2% vs. 82.1%), confirming that coverage is an insufficient proxy for fault-detection
  > capability."
  > "LLM-generated tests with retrieval-augmented context detect faults in 69% of cases compared to
  > 17.2% for general-purpose human-written tests (Fisher's exact, p < 0.001, Cohen's h = 1.10)."

  **Cite this carefully.** It supports "coverage is a bad proxy" and *undercuts* "agent tests are
  hollow" — the LLM suite found **more** faults. The comparison is against *general-purpose* human
  tests, not the bug-specific regression test a maintainer writes. Setup: Gemini 2.5 Flash plus
  lexical retrieval supplying bug-relevant context, 29 real BugsInPy bugs plus function-level and
  paired benchmarks.

- **Agents are good at writing a reproduction test — when told what is broken.** **SWT-Bench**, Niels
  Mündler, Mark Niklas Müller, Jingxuan He, Martin Vechev (ETH Zurich SRI), 2024-06-18, rev.
  2025-02-07. https://arxiv.org/abs/2406.12952. Live leaderboard https://swtbench.com/ reports e.g.
  TEX-T Claude 4 Sonnet (Salesforce) **87.0%** (2025-12-17) and DevstralTestGen (Mistral AI, script
  mode) **89.1%** (2026-03-13) at producing a test that fails before the fix and passes after. The
  paper also finds generated tests **"doubl[e] the precision of SWE-Agent"** as a filter on proposed
  fixes. **Read the scope carefully:** the agent is handed a written issue describing the defect —
  a specification supplied by a human, which is exactly the input the circularity problem assumes is
  missing. **TDD-Bench Verified** (IBM: Ahmed, Hirzel, Pan, Shinnar, Sinha, 2024-12-03,
  https://arxiv.org/abs/2412.02883, 449 real GitHub issues, measuring fail-to-pass rate and coverage
  adequacy) has the same shape.

- **Models game tests under optimization pressure.** *"Monitoring Reasoning Models for Misbehavior and
  the Risks of Promoting Obfuscation"*, Baker, Huizinga, Gao, Dou, Guan, Madry, Zaremba, Pachocki,
  Farhi (**OpenAI — model vendor, interested party**), 2025-03-14. https://arxiv.org/abs/2503.11926 —
  reward hacking in agentic coding environments, and the finding that penalizing the visible reasoning
  teaches concealment rather than compliance: *"agents learn obfuscated reward hacking, hiding their
  intent within the CoT while still exhibiting a significant rate of reward hacking."* I could not
  retrieve the specific coding exploit examples — see blocked sources.

**The gap, stated plainly.** Put these side by side. Agents write good tests *from a specification*
(SWT-Bench ~87–89%). Agents write bad tests *from buggy code* (−47% real-world bug detection). **The
unattended agent case is the second one, not the first** — the agent has no independent specification,
only the code it just wrote. Nobody has run that experiment. I queried the arXiv API across several
formulations and found no such study.

### 1b. Mitigations — IN USE

Ordered by how independent the oracle is of the agent.

#### External-oracle grounding: the assertion comes from a document the agent did not write

The strongest mechanism found, and it is in a major project.
**styled-components** (★41,127, since 2016) —
https://github.com/styled-components/styled-components/blob/main/AGENTS.md

> Tests AND implementation for CSS surfaces are always grounded in the current editor's draft on
> `drafts.csswg.org`. Before adding or materially changing a test or polyfill, re-fetch the relevant
> module section into `/tmp/` for the session (`curl -s https://drafts.csswg.org/<module>/ >
> /tmp/<module>.html`) and **quote the normative clause verbatim above the test that locks it. Never
> paraphrase from training data**; never substitute MDN or TR for the editor's draft.

and the procedure:

> 2. Translate every spec rule into a single test [...] One test per rule. Quote the spec text
> verbatim as a comment above each test or block.
> 3. Write the tests FIRST (TDD). Run the block; record which currently fail.
> 4. Implement to make failing tests pass. **Resist re-shaping passing tests to match the
> implementation; the spec is the source of truth.**

Two independent anti-circularity properties: the assertion's *content* originates outside the model
(and deliberately outside its training data), and the *direction of correction* is fixed — code moves
to the test, never the reverse. This is the same fix arXiv:2607.22883 arrived at experimentally,
implemented by hand two years earlier.

#### Discrimination required, not coverage: "would this fail if the change were reverted?"

**Apache Airflow** (★46,623, Apache Software Foundation) —
https://github.com/apache/airflow/blob/main/AGENTS.md (file last touched 2026-08-12, commit
"Evaluate AGENTS.md and skills with Codex", #70120), under `## Testing Standards`:

> Target exactly 100% coverage of what the PR changes — no more, no less. **Every changed or added
> behaviour must have a test; every test must fail without the PR's change.** Do not add tests for
> pre-existing logic that was already present before the PR, and do not test standard-library or
> third-party functions.

This is the only artifact found that carries a coverage number **and** closes the Goodhart hole in the
same sentence. *"Every test must fail without the PR's change"* is mutation-style discrimination
stated as prose; *"no more, no less"* forbids padding. Note honestly: this is **stricter than what CI
enforces** — https://github.com/apache/airflow/blob/main/codecov.yml sets `range: 65..90` and
`project.default.target: auto, threshold: 0%`, a no-regression ratchet. The 100%-of-diff figure lives
in the prompt, not the pipeline.

**phase-rs/phase** (★255, active agentic contributor-PR pipeline with a merge queue) —
https://github.com/phase-rs/phase/blob/main/.claude/skills/pr-contribution-handler/SKILL.md

> **Verify the tests DISCRIMINATE.** For every assertion, ask: *would this fail if the fix were
> reverted?* An assertion that passes both before and after the fix is **coverage theater**. A bug-fix
> PR must have at least one runtime test that drives the engine through the real pipeline [...] and
> would fail without the change.

and in its review-lens list: *"**test discrimination** — would each assertion FAIL if the fix were
reverted? (this replaces vague 'test adequacy' — a green test that pins nothing is coverage theater).
[...] **This is the single most frequent finding across contributor PRs.**"* Its general principle:
*"CI/Tilt green is necessary, NOT sufficient."*

#### Red-green enforcement written into agent policy

- **Microsoft** — https://github.com/microsoft/teams-sdk/blob/main/packages/cli/AGENTS.md (★724):
  > All new tests must follow a **red/green cycle**: write the test first, verify it fails against the
  > broken code (red), then apply the fix and verify it passes (green). **This ensures tests actually
  > catch the bug they're designed for.**
- **styled-components/babel-plugin-styled-components** — the sharpest statement of why, plus the
  snapshot cheat closed:
  > Red/green TDD is required for every fix. [...] When the test is a fixture snapshot, generate it on
  > the **pre-fix tree** so the diff captures the broken output, then update on the post-fix tree.
  > **A test that only ever passes alongside the fix is not a regression test.**
- **styled-components** (main AGENTS.md): *"Strict TDD is enforced: extend or add failing tests that
  encode the desired contract before changing production code; implement only enough to turn them
  green. No user-visible behavior change ships without tests that would fail without it."*
- **mastra-ai/mastra** (★27,532) —
  https://github.com/mastra-ai/mastra/blob/main/packages/playground/AGENTS.md: *"Test-first (TDD): RED
  failing MSW test → GREEN minimum code → REFACTOR."*
- Others found: `openops-cloud/openops` ("No production code without a failing test first"),
  `mtlynch/picoshare`, `Adyen/adyen-android`, `commonwarexyz/monorepo`, `astronomer/dag-factory`,
  `mattiasw/ExifReader`, `patrickhoefler/dockerfilegraph`, `ngrok/webernetes`.

> **Limitation, and I found no exception.** Every red-green rule I read is **advisory prose in a
> Markdown file**. No agent harness, hook, or CI job mechanically verifies the test failed before the
> implementation existed. The mechanism the brief asks about — *"where the harness verifies the test
> failed before the implementation existed"* — is **PROPOSED only** in production settings. The
> closest operating analogue is TDD-Bench's fail-to-pass metric, which is an **eval harness**, not a
> production gate.

#### Separation of duties: the agent that writes the code does not write the check

- **Anthropic** (*vendor — interested party; primary for what Anthropic advises*) —
  https://code.claude.com/docs/en/best-practices, fetched 2026-08-28:
  > **By a second opinion**: a verification subagent [...] or a dynamic workflow that checks its own
  > findings has a fresh model try to refute the result, **so the agent doing the work isn't the one
  > grading it.**

  and explicitly for tests:
  > You can do something similar with tests: **have one Claude write tests, then another write code to
  > pass them.**

  and the named failure mode:
  > **The trust-then-verify gap.** Claude produces a plausible-looking implementation that doesn't
  > handle edge cases. **Fix**: Always provide verification (tests, scripts, screenshots). **If you
  > can't verify it, don't ship it.**

  Note also the caution Anthropic attaches to the adversarial reviewer, which cuts against
  over-reading it: *"A reviewer prompted to find gaps will usually report some, even when the work is
  sound, because that is what it was asked to do."*

- **`coleam00/skills`** (★420; widely-distributed template by a well-followed AI-coding educator —
  treat as a template, not a production system) — the **protected judge**, and the only artifact in
  the whole sweep that connects a verification floor to autonomy:
  https://github.com/coleam00/skills/blob/main/.claude/skills/build-dark-factory/templates/harness/locks/floor.json
  > THE RATCHET. Copy to `.factory/locks/floor.json` — it is PROTECTED, so **only a human commit can
  > move these numbers.** That is the entire mechanism: the gate asserts observed >= floor, and a
  > second check asserts floor(head) >= floor(base), so the move **'delete the assertion and lower the
  > number in the same commit' is not available.**
  >
  > **The failure mode to watch: SLACK.** The gap between observed and floor is exactly the number of
  > assertions that can be deleted with the gate still green. It GROWS as the harness improves [...]
  > measured on a real factory, the hole went from 7 to 33 in one cycle BECAUSE the harness got
  > better. [...] either fail the gate when observed != floor, **or let any slack pin the autonomy
  > dial where it is.**

  Companion rule, https://github.com/coleam00/skills/blob/main/.claude/skills/build-dark-factory/references/validation-harness.md:
  > **a builder that can edit its own judge can make any claim true.** Protect `harness/**`, and route
  > legitimate coverage growth to your normal test directory instead.

  Plus a **holdout**: `.factory/holdout/run.py` holds assertions the builder agent may not read. And
  a defence against the empty suite: *"Zero is not a pass: a suite that discovered nothing exits 0 and
  looks perfect."*

- **`tylerlaprade/go2rust`** (★9 — tiny, but it records what *happened* in a genuine two-agent loop,
  not what was planned) — https://github.com/tylerlaprade/go2rust/blob/master/AGENTS.md:
  > **Division of labor converges naturally — capture the spec, let the other side implement.**
  > Repeatedly this session the loop and a Claude session arrived at the same fix from opposite ends:
  > **one wrote the failing fixture or unit test (the spec), the other wrote the implementation.**

  and a rule that stops the loop certifying itself:
  > Never commit a state that depends on the loop's uncommitted WIP. If `./test.sh` promotes your
  > XFAIL because the loop's uncommitted fix makes it pass, do not commit that promotion — at `HEAD`
  > (without the loop's WIP) the fixture is red.

- **`PublicEnemage/worldsim`** (★0 — **not evidence of industry practice**; cited only because the
  rule is articulated unusually precisely) —
  https://github.com/PublicEnemage/worldsim/blob/main/docs/process/agents.md:
  > **Segregation of duties rule:** The agent that wrote the implementation cannot write the intent
  > block for that implementation. **Enforced by session boundary, not instruction.**
  > [...] I cannot write the intent block for code I implemented, because the moment I do, **I am no
  > longer documenting the contract; I am rationalizing the implementation.**
  > [...] Divergences are filed as issues — **not resolved by updating the intent block to match the
  > code.**

#### Human-authored artefacts the agent may not edit

**Thinner than expected.** I found **no well-known project with a machine-enforced "the agent cannot
touch these test files" rule** — no CODEOWNERS-on-tests pattern, no pre-commit hook blocking test
edits. What exists is prose, in small repos:

- `igorrendulic/blueprint-to-code`: *"The agent must not edit the tests unless explicitly instructed."*
- `EpicMandM/esxi-lab-provider`: *"Tests are the specification. Production code must conform to the
  tests, not the [reverse]."*
- `mmunro3318/tradekit`: *"Never edit tests to make implementation pass; never weaken an R-rule test."*
- `SHIMA0111/templatia` and `SHIMA0111/pgbouncer-config-rs`: *"Even if generated tests fail with the
  current implementation, do not modify the tests to fit the implementation if the tests correctly
  reflect the intended behavior described by the comments."*
- `AhmedAlnasser2000/REZANOVA-CAS-CALCULATOR`: role-based read-only enforcement — *"Explorer, CAS
  Researcher, Tester, and Reviewer are read-only. Tester must never edit tests, baselines, snapshots,
  configuration, production code, or durable memory."*

Treat the **pattern as attested** and the **enforcement as absent**. The nearest thing to enforcement
is `coleam00`'s protected `harness/**` above — which protects the *judge*, not human-authored
acceptance tests specifically.

#### Golden files with adjudicated diffs

The mechanism: regeneration is allowed, *silent acceptance* is not.

- **Apache Spark** (★43,894) — https://github.com/apache/spark/blob/master/AGENTS.md:
  > SQL golden file tests are managed by `SQLQueryTestSuite` [...] **DO NOT edit the generated golden
  > files (`.sql.out`) directly. Always regenerate them when needed, and carefully review the diff to
  > make sure it's expected.**
- **fluxcd/flux2** (`cmd/flux/testdata/`, `-update` flag), **DataDog/browser-sdk**
  (`api/*.api.md` committed API golden files), **mbrt/gmailctl**, **wasp-lang/wasp** — same shape.
- **styled-components** goes further and forbids regeneration for one file:
  > `src/native/test/commit-order.test.tsx` banks the commit-order baseline [...] **The arrays are
  > hand-written, never snapshots.** Moving work between phases changes them, and **the diff has to be
  > adjudicated in the same commit rather than regenerated.**

  Their general rule names snapshot-regeneration as a *suppression*, alongside type escapes and
  sleeps: *"A change that hides a symptom without removing what produced it is a suppression [...] a
  governor over a slow effect, an `as any` over a type that won't check, **a snapshot updated to
  green**, a disabled lint rule, a swallowing `try`/`catch`, a sleep or retry over a race."*

#### Differential oracles

A second implementation is an oracle the agent cannot rationalize away.

- **vercel-labs/scriptc** — https://github.com/vercel-labs/scriptc/blob/main/AGENTS.md:
  > Corpus programs are differential tests against Node: every program runs under Node and as a
  > compiled native binary, and **stdout, stderr, and exit codes must match byte-for-byte.** A new
  > feature lands with corpus programs that pin its behavior both ways.
- **tursodatabase/turso** (★24,047) — https://github.com/tursodatabase/turso/blob/main/AGENTS.md lists
  `testing/simulator/` for *"Fault injection, differential testing"* (against SQLite).
- **apache/doris** — *"Prefer differential tests against a [reference engine] such as Spark, Hive,
  Flink, or Trino when applicable."*
- **protobuf-net/protobuf-net**; **nubjs/nub** (*"Bun remains useful as [...] a differential test
  oracle — not as a spec"*).
- **audreyt/ethercalc** (★3,042) ships `packages/oracle-harness/` (record/replay + canonicalizers) and
  runs *"oracle replay against legacy docker"* nightly — a differential oracle against the previous
  implementation of the same product.
- **thepartly/gatehouse** — property-based differential tests against a hand-written deny-overrides
  oracle; see §4a, where a mutation gate certifies that the oracle bites.

**Metamorphic testing specifically: I found no primary artifact tying it to agent verification.** The
sole AGENTS.md hit is `open-gsd/gsd-core` listing *"explicit oracle classification
(specified/derived/metamorphic/implicit)"* as a debugging-agent behaviour. Classify metamorphic
testing as **PROPOSED** in this context.

### 1c. Mitigations — PROPOSED

- **Specification-based prompting** — replace the implementation in the prompt with a generated spec
  docstring (arXiv:2607.22883, ISSTA 2026). Shown to work experimentally; **no production agent
  harness found doing it.** styled-components' CSSWG rule is the same idea implemented by hand.
- **Supplying natural-language intent to the test generator** — +34% bug detection (arXiv:2409.09464).
  Measured, not productized.
- **Mechanically verified red phase.** Advocated in many AGENTS.md files; implemented in none found.
- **Machine-enforced immutable acceptance tests.** `EmeaAppGbb/spec2cloud` (★100, framework/advocacy
  repo, not a working product) — https://github.com/EmeaAppGbb/spec2cloud/blob/main/AGENTS.md:
  > **Never modify a test without human approval.** Tests are human-approved contracts. Any change to
  > a test requires explicit human consent **because it changes what "done" means.**
- **Mutation spot-checks as an audit of agent test suites** — `rshankras/claude-code-apple-skills`
  (★677, personal skills collection) marks its mutation-testing skill EXPERIMENTAL, lists *"Auditing
  agent-written test suites for assertion-free tests"* as a use case, and insists it be
  **"Advisory report only, never a merge gate."**

---

## 2. Coverage expectations

### 2a. The emptiness finding — stated first, because it is the answer

**Nobody publishes a coverage number keyed to how autonomously an agent operates.** Not one artifact
found says anything of the form *"agent may merge unattended at X% / needs a human at Y%"*, or scales
a threshold by trust tier, action risk, or supervision level.

What exists abundantly, and is easy to mistake for it: **repo-wide coverage thresholds restated inside
agent-facing policy files.** The number is the project's pre-existing CI bar. Putting it in AGENTS.md
tells the agent what the gate is; it does not calibrate the gate to the agent.

Queries run to establish this: `"cov-fail-under"` in AGENTS.md (15 hits, all repo-wide);
`"coverage theater"` (20 hits, all anti-metric); `"assertion-free"` (20 hits);
`coverage` + `autonomously` in AGENTS.md (20 hits, no numeric tie);
`coverage` + `unsupervised` in CLAUDE.md (20 hits, no numeric tie);
`coverage` + `trust` in AGENTS.md (18 hits, no numeric tie);
`coverage` + `AI-generated` in AGENTS.md (20 hits); `"coverage is not a gate"` (1 trivial hit);
`"raise coverage"` in AGENTS.md (1 hit). Two further queries (`Goodhart` and `"mutation score"` in
AGENTS.md) were cut off by GitHub's code-search rate limit and never completed — a known gap.

**The one artifact connecting a verification floor to autonomy does not use coverage at all.**
`coleam00/skills`' ratchet counts **assertions** (`e2e_steps_asserted`, `holdout_assertions`,
`unit_tests`) with **no coverage percentage anywhere in the gate ladder**, and its concluding rule is
*"let any slack pin the autonomy dial where it is."* See §1b.

### 2b. IN USE — real numbers, and what they are actually for

**Diff-scoped, with discrimination attached — Apache Airflow.** See §1b for the quote. This is the
shape worth copying: *100% of what the PR changes*, plus *every test must fail without the change*.

**100% patch coverage extended to test code, explicitly because of an agent failure mode —
`aio-libs/frozenlist`** (★127, but `aio-libs` is the org behind `aiohttp`/`yarl`; high credibility for
Python practice). The file opens *"# Notes for LLM contributors"*.
https://github.com/aio-libs/frozenlist/blob/master/AGENTS.md, section **"Every line in a test must be
covered"**:

> The coverage gate applies to **test code too**, not just `frozenlist/`. A test that contains a
> branch or statement the suite never reaches will fail CI. **This catches a class of mistake agents
> make all the time:** defensive `raise` inside a monkeypatched stub, a cleanup branch behind
> `if had_own_getstate:` that the happy path never enters, an `else` arm guarding a condition that is
> always true under the fixture. From the perspective of a unit suite all of those lines are dead
> code.

Machine-enforced: https://github.com/aio-libs/frozenlist/blob/master/.codecov.yml sets
`coverage.range: 100..100` and `status.patch.default.target: 100%`. It cites the canonical incident —
https://github.com/aio-libs/yarl/pull/1687 — where CI rejected an agent-authored test for an
unreachable `raise`. **This is coverage-of-test-code used as an anti-padding mechanism, the inverse of
the usual complaint, and the sharpest counter-example to "coverage is discredited for agents".**

Also: *"If you cannot run the suite in your environment, say so explicitly in the PR body rather than
implying coverage you did not actually achieve."*

**`microsoft/ox-tools` — `cargo-coverage-gate`, default 100% per package.** Microsoft org, ★13,
updated 2026-08-26, published to crates.io as `cargo-coverage-gate` 0.3.0. Threshold resolution:
per-package `[package.metadata.coverage-gate] min-lines-percent` → workspace default → *"The built-in
default of `100.0` — full coverage required."* Guiding principle: *"one package, one number, one
threshold, one verdict."*
https://github.com/microsoft/ox-tools/blob/main/crates/cargo-coverage-gate/README.md

> **No tie to agents.** Its stated rationale is delta builds, displaced-code regressions, and Codecov
> being unreachable in Microsoft-internal repos. The repo's own AGENTS.md never mentions coverage. If
> anyone cites this as agent-verification tooling, that is an inference, not a claim the artifact
> makes.

**Numbers in AGENTS.md that are just the repo's CI bar.** All read and confirmed; none frames the
number as agent-specific.

| Project | Bar | Artifact |
|---|---|---|
| scikit-learn-contrib/MAPIE (★1,584) | `--cov-fail-under=100`; *"Coverage must be exactly 100%."* | https://github.com/scikit-learn-contrib/MAPIE/blob/master/AGENTS.md |
| fgmacedo/python-statemachine (★1,298) | *"**100% branch coverage is mandatory.**"* pre-commit enforced | https://github.com/fgmacedo/python-statemachine/blob/develop/AGENTS.md |
| mandarons/icloud-docker (★1,869) | `--cov-fail-under=100`, mirror test per `src/*.py` | https://github.com/mandarons/icloud-docker/blob/main/AGENTS.md |
| ManimCommunity/manim-voiceover (★314) | 85%, on the same command line as `mutmut` | https://github.com/ManimCommunity/manim-voiceover/blob/main/AGENTS.md |
| styled-components (★41,127) | *"Branch coverage stays above 80%."* | https://github.com/styled-components/styled-components/blob/main/AGENTS.md |
| CodeBoarding/CodeBoarding (★2,403) | 80% | https://github.com/CodeBoarding/CodeBoarding/blob/main/AGENTS.md |
| transferwise/pipelinewise (★659) | 77% | https://github.com/transferwise/pipelinewise/blob/master/AGENTS.md |
| audreyt/ethercalc (★3,042) | 100% node tests as a PR gate | https://github.com/audreyt/ethercalc/blob/master/AGENTS.md |

For honesty about the spread, the low end of the same pattern: `4dn-dcic/tibanna` 25%,
`kayba-ai/agentic-context-engine` 25%, `VoltCyclone/PCILeechFWGenerator` 10%. **A `--cov-fail-under`
in an AGENTS.md is not evidence of a high bar.**

**The qualitative tie that does exist.** `cashubtc/nutshell` —
https://github.com/cashubtc/nutshell/blob/main/AGENTS.md, `## Autonomous vs. Human-Required Changes`:

> ### Safe for agents to do autonomously
> - **Bug fixes with clear reproduction steps and test coverage**
> - Documentation improvements [...] Adding or improving tests
> - Small refactors that don't change public APIs

Coverage appears as a **condition on which actions are autonomous**, with no number attached. Note the
file's autonomy split is otherwise driven by blast radius (crypto, migrations, protocol, API breaks →
human), which is the dominant pattern everywhere (see §6).

**Two projects that tell the agent there is no gate.**
- `jdeath/Hubspace-Homeassistant` (★380) — *"Read the missing-lines report after every test run and
  cover new or changed code [...] There is **no** `--cov-fail-under` / Codecov 100% gate."* Coverage
  as a *reading instruction*, with the absence of a gate stated so the agent does not infer one.
- `jmcgrath207/k8s-ephemeral-storage-metrics` — *"**Coverage baseline**: 47.2% total. Ceiling ~47%
  without source mods … **Do not propose refactors to 'raise coverage' unless user asks.**"*

### 2c. IN USE — coverage displaced by discrimination

This is where the evidence is strongest, and the finding is not *"coverage is discredited"* so much as
**"coverage is being replaced by falsifiability"**.

- **`phase-rs/phase`** — see §1b. Also, on the metric itself:
  > **An honest coverage decrease is acceptable — never ask a contributor to "restore" it.** A parser
  > change that converts a silently-swallowed clause into an explicit `Effect::Unimplemented` moves
  > cards from lying-green to honest-red; that is an improvement [...] The CI coverage-regression gate
  > is **bucket-based, not count-based**.
- **OWASP Juice Shop** (★13,730, OWASP flagship; skill added 2026-07-31) —
  https://github.com/juice-shop/juice-shop/blob/master/.ai/skills/write-tests/SKILL.md:
  > **Golden rule:** Never weaken, skip, `@Disabled`/`it.skip`, or delete assertions to make a suite
  > pass. Fix the code or the test instead. **Do not chase 100% — prioritize meaningful behavior,
  > branches, and error paths over trivial getters.**
- **Assertion-free tests banned outright**, verbatim:
  - `mishka-group/mishka_chelekom` (★749): *"Tests must assert something meaningful — never
    `assert true`, no vacuous or assertion-free tests."*
  - `ferro-labs/ai-gateway` (★242): *"**Assert real behaviour.** [...] Don't add tautological or
    assertion-free tests (setting a struct field and reading it back, asserting a value equals itself,
    or only checking that a function returns `nil`)."*
  - `Resgrid/Core` (★225, since 2018): a `### Don't Write Assertion-Free Tests` section with a
    BAD/GOOD pair — *"// BAD — no assertion, only checks it doesn't throw … 'it didn't throw, so it
    works!' — NO"*. Notably the same skill is committed three times, under `.claude/`, `.forge/` and
    `.opencode/` — the rule is being carried across agent harnesses.
  - `nWave-ai/nWave` (★601): classifies this as a **BLOCKER** — *"Severity: BLOCKER for zero-assertion,
    tautological, mock-dominated, circular, always-green, fully-mocked SUT, and assertion-free
    patterns. [...] **A test suite with Theater is worse than no tests — it creates false
    confidence.**"* nWave uses **acceptance-criteria coverage**, not percentage coverage: *"Check
    coverage report shows 100% AC mapped to tests"*, severity CRITICAL.
  - `growilabs/growi` (★1,464): a mandatory design skill that *"Catches brittle implementation-spies
    and assertion-free 'it didn't throw' tests"*, and *"a test diff is not 'good' until it has been
    checked against essential-test-design."*
- **The best *mechanical* anti-padding check found anywhere** — `abap2UI5` (★376) —
  https://github.com/abap2UI5/abap2UI5/blob/main/AGENTS.md:
  > **Every `FOR TESTING` method has to assert something** — `npm run check:asserts`. A method that
  > only calls the code proves it does not dump, and **a green report cannot tell that apart from a
  > proved behaviour.**

  A CI job that fails assertion-free tests. This is the only such gate I found in the entire research.

### 2d. The arguments against coverage-as-a-gate

**Martin Fowler, "TestCoverage", 2012-04-17** — https://martinfowler.com/bliki/TestCoverage.html:
> If you make a certain level of coverage a target, people will try to attain it.
>
> If you are testing thoughtfully and well, I would expect a coverage percentage in the upper 80s or
> 90s. **I would be suspicious of anything like 100% — it would smell of someone writing tests to make
> the coverage numbers happy.**

quoting Brian Marick: *"I expect a high level of coverage. Sometimes managers require one. There's a
subtle difference."*

Fowler's 2012 suspicion of 100% is in direct tension with `frozenlist`, MAPIE, python-statemachine and
icloud-docker, all of which run at exactly 100% and defend it. The reconciliation the artifacts
themselves offer: those are small, pure-logic libraries where 100% is achievable without padding, and
`frozenlist` additionally covers the *test* code so a padded test cannot hide.

**Google** — Marko Ivanković, Goran Petrović, René Just, Gordon Fraser, *"Code coverage at Google"*,
ESEC/FSE 2019, https://research.google/pubs/code-coverage-at-google/ — one billion lines/day across
seven languages; the stated design choice is applying coverage **at the changeset level, surfaced to
human readers**, not as a global gate. Full text is behind the ACM DL and was not accessed.

**The empirical picture is more equivocal than the folklore.** 2606.08588 kills coverage as a
fault-detection proxy *while showing agent tests detecting more real bugs than general human ones*;
2607.22880 partially rehabilitates coverage for regression-style generation and dissolves the
size-confounder argument. **Neither supports "the agent games coverage, so coverage is worthless."**

### 2e. PROPOSED

- **Coverage ratchet as a "were tests actually written" check for agent code** —
  `rshankras/claude-code-apple-skills` (★677, personal collection; stars measure interest, not
  deployment), `last_verified: 2026-07-24` —
  https://github.com/rshankras/claude-code-apple-skills/blob/main/skills/testing/coverage-ratchet/SKILL.md.
  Frontmatter states the agent-specific purpose: *"Use when **agent-written code** needs a
  deterministic 'tests were actually written' check."*
  > A build/test gate proves the tests that exist pass. **It says nothing about whether tests were
  > *written*** — a phase with no test task ships green on build success alone.
  >
  > **Why a Ratchet, Not a Target.** An absolute threshold ("80%") fails one of two ways on a real
  > codebase: it fails day one (so it gets disabled), or it gets set below current reality (so it
  > gates nothing).

  Its own pitfall table refuses to solve Goodhart with coverage: *"Chasing the number with
  assertion-free tests | Coverage without verification | **Pair with mutation spot-checks.**"*
- **"Coverage Theater" named as an AI-specific failure mode** — `mkwatson/ai-fastify-template` (★18,
  **stale since 2025-07-02** — cite for framing, not adoption):
  > AI frequently writes tests that achieve 100% coverage but validate nothing [...]
  > `expect(result).toBeDefined(); // ✅ Passes` [...] `expect(typeof result).toBe('number'); // ✅
  > Passes - 100% coverage!` [...] Our mutation testing standards catch this — **when logic is
  > mutated, the test still passes, revealing it's fake.**
- **Negative examples written into agent context** — Andrew Stellman (known O'Reilly author),
  `quality-playbook` (★83) —
  https://github.com/andrewstellman/quality-playbook/blob/main/ai_context/TOOLKIT.md:
  > "Coverage theater" is when tests produce high coverage numbers without catching real bugs.
  > Examples: asserting that imports worked, that dicts have keys, **that mocks return what they were
  > configured to return.** The quality constitution calls this out explicitly with project-specific
  > examples derived from exploration, so future AI sessions know what NOT to do.
- **Mutation testing sold as the agent-loop oracle — `davidteren/mutineer` (★7). This is the vendor's
  own documentation for its own tool; label as advocacy.**
  https://github.com/davidteren/mutineer/blob/main/docs/agentic-coding.md:
  > Line coverage tells you which code *ran* under test. It says nothing about whether your tests
  > would *notice if that code broke*. **Mutation testing closes exactly that gap — and that gap is
  > where AI-generated code and AI-generated tests are weakest.**

  Its CI recommendation is a delta gate — *"fail a PR only when it makes things worse"* — rather than
  an absolute bar. Also seen: `ankitjha67/product-architect` (★106) — *"95% line coverage + 40%
  mutation score = assertion-free 'coverage theater'"*, the only two-number diagnostic pair found.

---

## 3. Property-based testing as an agent-verification mechanism

### The honest headline: close to empty, and I looked hard

PBT is *used* in plenty of repos that also carry an AGENTS.md — `scala/scala` (ScalaCheck),
`App-vNext/Polly` (FsCheck), `remeda/remeda` (fast-check, `*.test-prop.ts`), `atuinsh/atuin`
(proptest), `DataDog/lading` (*"Where proofs are impractical, use property tests via proptest"*),
`awslabs/mcp` (`hypothesis` in the DynamoDB MCP server), `skjolber/3d-bin-container-packing` (jqwik),
`Start9Labs/start-technologies`, `ai-dynamo/dynamo`, `dbrattli/Expression`, `chdb-io/chdb`,
`ghuntley/loom` (*"Prefer property-based tests (`proptest`) over unit tests when appropriate"*),
`tech-leads-club/agent-skills` (`*.pbt.test.ts`), `LiamMorrow/LiftLog`, `TrustTunnel/TrustTunnel`.

**In every case PBT is the project's ordinary testing practice, described to the agent the way any
other convention is. None of them argues PBT is warranted *because* an agent wrote the code.**

### Where I looked for the agent link and did not find it

- **Hypothesis (Python).** https://hypothesis.readthedocs.io/en/latest/ contains **no mention of LLMs,
  AI, or coding agents**. Its lead developer, **Zac Hatfield-Dodds — who works at Anthropic** — has a
  personal site (https://zhd.dev/) listing PBT talks (PyCon US, PyCon AU *"Sufficiently Advanced
  Testing"*) and an Anthropic alignment/interpretability talk (StrangeLoop 2023), with **no writing
  connecting the two**. This is the most promising possible link in the entire strand and it does not
  exist in public.
- **Trail of Bits.** Their Testing Handbook (https://appsec.guide/docs/fuzzing/) covers fuzzing in
  depth, does **not** treat property-based testing as a distinct methodology, and makes **no**
  connection to AI/LLM/agent-generated code.
- **AWS.** Marc Brooker has extensive formal-methods and simulation writing
  (https://brooker.co.za/blog/2024/04/17/formal.html — *"Formal Methods: Just Good Engineering
  Practice?"*; .../2022/04/11/simulation.html; .../2015/03/29 on AWS's use of formal methods) **and**
  extensive agent writing (.../2026/05/20/hypothesis.html; .../2026/01/12/agent-box.html —
  *"Agent Safety is a Box"*; .../2025/08/12/llms-as-components.html). **The two sets do not meet on
  testing.** The closest is *"LLMs as Parts of Systems"* (2025-08-12): *"LLMs are more powerful, more
  dependable, more efficient, and more flexible when deployed as a component of a carefully designed
  system"*, with *"SMT solvers are used for what they're great at"* — but the worked example is
  Bedrock Automated Reasoning Checks, verifying *model output against a policy*, not verifying
  agent-written code.
- **Anthropic.** No mention of property-based testing in the Claude Code best-practices or
  test-and-evaluate documentation.

### The one genuine tie — and it is to simulation, not PBT

**Jane Street, *"Getting from tested to battle-tested"*, Doug Patti, 2025-12-03** —
https://blog.janestreet.com/getting-from-tested-to-battle-tested/ — describes a seven-layer stack for
their Aria distributed message bus: unit tests; integration tests over a **simulated networking
layer** (*"delaying and dropping packets and manipulating time"*); **property-based testing with
QuickCheck** (*"can produce random orderings of events which we can feed into a simulation"*);
version-skew tests; **AFL fuzzing** (*"turn the fuzzer's byte input stream into a sequence of state
updates"*); nightly lab performance tests; and chaos testing. On agents:

> We also think that **Antithesis holds a lot of promise in the context of agentic coding tools** [...]
> we think that Antithesis holds a lot of promise as a **source of feedback, both for using and for
> training such models.**

**Classify precisely.** The **testing stack is IN USE** — for human-written code, at a firm with
strong incentives to get this right. The **agent application is PROPOSED**, in the authors' own hedged
words ("holds a lot of promise"). Antithesis is a commercial vendor and Jane Street is its customer:
note the stake in both directions.

### Why the emptiness is interesting rather than merely a gap

The brief's hypothesis — that PBT is an anti-circularity mechanism because the agent must assert
invariants it cannot trivially satisfy — is sound, and **I can find nobody making it in a primary
source.** What I *did* find, in an operating CI file, is PBT and mutation testing composed in exactly
that role: **thepartly/gatehouse** (§4a) runs property-based **differential** tests against a
hand-written deny-overrides oracle, and then runs a mutation gate whose job is to certify that those
property tests actually discriminate. PBT supplies the oracle; mutation testing proves the oracle
bites. **The mechanism the hypothesis describes is running in production without anyone writing down
the argument for it.**

---

## 4. Mutation testing on agent-authored code

This is the **densest area of genuine IN USE evidence in the strand**, and the reason is stated
outright in one of the CI files: coverage cannot distinguish a test that would have caught the bug
from one that merely executed the line — and that distinction is exactly what you lose when you stop
reading the diff yourself.

### 4a. IN USE — mechanism verified in a CI config

**`thepartly/gatehouse`** (★346, Rust authorization library, since 2025-03) — the best single example,
because the policy and the workflow agree and the design is coherent.

Policy — https://github.com/thepartly/gatehouse/blob/main/AGENTS.md:
> A **diff-scoped `cargo-mutants` gate** mutates the PR's changes to `src/checker.rs` and
> `src/combinators.rs` only. **Every new/changed line there must be killed by a test or CI fails**
> (~20 min run). When you touch veto/short-circuit logic, **add a test that *distinguishes the
> mutation*** (e.g. a case where `&&` vs `||` actually diverge), not just a happy-path assertion —
> **a green test that survives the mutant is the usual failure mode here.**

Mechanism — https://github.com/thepartly/gatehouse/blob/main/.github/workflows/ci.yml:
```yaml
- name: Capture checker/combinator diff
  run: git diff origin/${{ github.base_ref }}...HEAD -- src/checker.rs src/combinators.rs > mutants.diff
- name: Run focused mutation tests
  run: cargo mutants --in-place --in-diff=mutants.diff
       --file src/checker.rs --file src/combinators.rs
       --baseline=skip --timeout=60 --build-timeout=300 --all-features
       -- --test checker_contract --test tracing_contract
  env:
    PROPTEST_CASES: 128
```
Note what this composes. The tests the mutants must be killed by are **property-based differential
tests against an oracle** — from the same AGENTS.md: *"`evaluate_one` (single) and
`evaluate_batch_by` (batch) implement this independently and **must agree per item**; differential
proptests against a deny-overrides oracle in `tests/checker_contract.rs` enforce it."* Also:
`main` requires an approving review the author cannot self-grant.

**`prestomation/ha-home-keeper`** (★66, created 2026-06 — young repo, but the mechanism is real and
the reasoning is the clearest found anywhere).
Workflow — https://github.com/prestomation/ha-home-keeper/blob/main/.github/workflows/mutation.yml,
header comment verbatim:
> **Line coverage proves a line ran; it says nothing about whether a test would have failed had that
> line been wrong.** These jobs mutate the changed functions (Python, via mutmut) and the changed line
> ranges (TypeScript, via Stryker) and fail when too few of those mutants are caught.
>
> Scope is deliberately narrow [...] **Judging a whole file would fail pull requests for debt they did
> not introduce**, so `ci/mutation_scope.py` maps the diff onto just the functions/lines it touched.

Budgets: Python `timeout-minutes: 45`; TypeScript `timeout-minutes: 75`, with the note *"Diff-scoped
runs take minutes; the headroom is for a manual `--all`, which is ~40 minutes over the full
1,800-mutant frontend surface."* Escape hatch: a `skip-mutation` PR label bypasses both jobs.

Policy — https://github.com/prestomation/ha-home-keeper/blob/main/AGENTS.md:
> **Mutation testing gates every PR** at an 80% mutation score on the code the PR changed [...]
> **It is too slow for the run-before-you-push loop**; run it when you touch the mutable surface.
> [...] **Kill surviving mutants with real assertions.**

**`audreyt/ethercalc`** (★3,042, since 2011) — the most elaborate, with measured per-package floors.
Policy — https://github.com/audreyt/ethercalc/blob/master/AGENTS.md:
> CI gates (PR): Typecheck → node tests (100% coverage) → workers-pool → Playwright e2e →
> `wrangler deploy --dry-run` → self-host smoke → conditional `mutation-gate`. [...] Nightly: full
> Stryker matrix + oracle replay against legacy docker
> [...] Mutation floors re-measured: worker 90.21, shared 99.69, socketio-shim 84.68, migrate 90.38,
> oracle-harness 83.46, client 77.61 — **equivalent mutants carry written `// Stryker disable`
> justifications rather than padded tests.**

Mechanism — https://github.com/audreyt/ethercalc/blob/master/.github/workflows/ci.yml, a
`mutation-gate` job (changed-packages-only) whose comment, **dated 2026-08-10**, is the best primary
statement of the cost calculus found anywhere:
> Budget (2026-08-10): local full six-package ratchet exits 0 in ~828s (~13m48s) on M-series; this job
> mutates only packages with `src/` changes vs origin/main. [...] run 31388973185 cancelled the
> Stryker step at timeout-minutes:20 with zero score output — **a cancelled gate is indistinguishable
> from green at a glance and trains people to ignore it.** 45m ≈ ~2.5× the local full-matrix baseline,
> deliberate headroom so the gate can finish and report a real score rather than timing out.
> **Do NOT lower Stryker break thresholds to "fit" a short budget.**

**`PicnicSupermarket/error-prone-support`** (★38, but a real company's long-running OSS Java project,
since 2018) — PIT mutation testing as a numbered step in the agent's workflow.
https://github.com/PicnicSupermarket/error-prone-support/blob/master/AGENTS.md step 9 runs
`./run-branch-mutation-tests.sh` *"and try to resolve any surviving mutants"*. The detailed rule —
https://github.com/PicnicSupermarket/error-prone-support/blob/master/.github/instructions/testing.instructions.md:
> **Kill every killable mutant.** Every mutant that can be killed must be killed. If a surviving
> mutant indicates a gap in test coverage, add a test case; **even if the test case seems contrived.**
> High mutation test coverage is a hard requirement.
> [...] **Document unkillable mutants** [...] add an `// XXX:` comment next to the code explaining why
> the mutant survives and why the code is intentional.

**`mastra-ai/mastra`** (★27,532) —
https://github.com/mastra-ai/mastra/blob/main/packages/playground/AGENTS.md:
> After tests pass, **mutation testing is mandatory** on exactly the production `.ts`/`.tsx` files the
> task changed (none changed = skip) [...] No dirs/globs, no unrelated files, no direct `stryker run`
> [...] **Strengthen the TDD/BDD tests to kill survivors (never weaken assertions)**; report truly
> equivalent/unreachable ones.

**`microsoft/ox-tools`** (★13, Microsoft org) —
https://github.com/microsoft/ox-tools/blob/main/crates/cargo-coverage-gate/AGENTS.md:
> `cargo-mutants` runs in CI against this crate. Before claiming a change is done, prefer adding
> direct unit tests for any private helper whose arithmetic, comparisons, or branch conditions would
> otherwise only be exercised through wider integration tests — **those are the mutants the runner
> catches most often, and surviving mutants block the build.** `#[mutants::skip]` is acceptable [...]
> **but justify the attribute in a comment.**

**`ManimCommunity/manim-voiceover`** (★314) — a **zero-survivor** gate.
https://github.com/ManimCommunity/manim-voiceover/blob/main/AGENTS.md requires `uv run mutmut run` and
`uv run python scripts/check_mutmut_results.py` before submitting. The script
(https://github.com/ManimCommunity/manim-voiceover/blob/main/scripts/check_mutmut_results.py) exits 1
on any mutant whose status is in `{"survived", "timeout", "no tests", "suspicious", "not checked"}` —
note that **`"not checked"` is treated as failure rather than ignored**, closing the "the run didn't
finish" hole that ethercalc's comment warns about.

**`egil/Htmxor`** (★160) — https://github.com/egil/Htmxor/blob/main/AGENTS.md separates a fast PR
profile from an authoritative full-scope Stryker run on a scheduled cadence, plus the discipline rule:
*"A red full-scope run records legacy debt; **it is never a reason to weaken the command.**"* The same
file requires *"separate Standards and Spec reviews, using different reviewers when the environment
supports it"* — separation of duties again.

**`App-vNext/Polly`** (★14,232) — https://github.com/App-vNext/Polly/blob/main/AGENTS.md exposes five
mutation-test build targets to the agent (`./build.ps1 -Target MutationTestsCore`, …). **Weaker
evidence than the above:** the file tells the agent the targets exist; I did not verify a blocking CI
gate.

**Other mutation-score numbers in AGENTS.md files**, offered as a spread rather than as authority
(mostly small repos): `lidofinance/lido-oracle` 75%+, `Avyukton/mouchak-mail` 85%,
`ishanjain1502/distributed-inference-engine` 85%, `Doumajnik/template` ≥90% with an explicit *"If below
90%, loop back to Test Writer to add defeating tests"*, `buildworksai/saraise-application` cosmic-ray
`--fail-over 10` (≥90% kill rate), `supernovae-st/nika` ≥90%, `sudo97/charlie` ≥95%,
`mivek/MetarParser` 92%, `longcipher/hpx`, `Corgea/Sighthound` (advisory only),
`bagowix/interlock` (*"out of band, never a PR gate"*), and 100%/zero-survivor at `sferik/nba-ruby`,
`MaximSrour/is-it-ready` and `chobbledotcom/tickets`.

**A lightweight variant worth noting** — `tech-leads-club/agent-skills` builds a mutation check into
the agent's own loop without the tooling:
> **Discrimination sensor** — injects a small behavior-level fault (flip a condition, change a return
> value, off-by-one, remove a required side effect) in an **isolated scratch** (temporary
> `git worktree` or temp file copies — never `git stash`), runs the relevant tests there, **confirms
> they FAIL (kill the mutant)**, discards the scratch, and verifies the real worktree's
> `git status --porcelain` matches the pre-sensor baseline. Tiered by risk [...] Surviving mutants
> become fix tasks.

### 4b. The anti-gaming rules are the interesting part

Several projects independently wrote down the same rule, which tells you they hit the same failure:
**an agent asked to raise a mutation score will pad the suite or exclude the code.**

- `sferik/nba-ruby` (★3 — weigh the repo, not the author's reputation) —
  https://github.com/sferik/nba-ruby/blob/main/AGENTS.md:
  > **Never ignore or exclude code from mutation testing.** Do not: add exclusions to `.mutant.yml`;
  > use inline `# mutant:disable` comments; skip methods or classes from mutation coverage. **If a
  > mutant seems impossible to kill, the code is likely untestable or redundant — refactor it instead
  > of excluding it.**
- `audreyt/ethercalc`: equivalent mutants carry written justifications *"rather than padded tests."*
- `mastra-ai/mastra`: *"Strengthen the TDD/BDD tests to kill survivors (**never weaken assertions**)."*
- `filda/aenternis`: *"Surviving mutants mean a missing assertion. **Add one; do not weaken the
  threshold.**"*
- `microsoft/ox-tools`, `PicnicSupermarket/error-prone-support`: skips permitted only with a written
  justification at the code site.
- `egil/Htmxor`: a red full-scope run *"is never a reason to weaken the command."*

**This is the load-bearing observation for the reference document.** Mutation testing is not
self-enforcing either. **Every project running it as an agent gate also had to write a rule forbidding
the agent from gaming the gate.** The gate moves the goalpost from "lines executed" to "assertions
that discriminate", which is much harder to fake — but it is not unfakeable, and the projects running
it know that.

### 4c. The cost problem, and whether agents change the calculus

**They do — but not in the way the brief suggests. The argument "an agent can afford to wait" does not
appear in any primary source I found.** What appears instead, universally, is **diff-scoping**: every
operating gate above mutates only the changed code. That is the cost fix.

cargo-mutants' own documentation —
https://github.com/sourcefrog/cargo-mutants/blob/main/book/src/performance.md:
> Most of the runtime for cargo-mutants is spent in running the program test suite and in running
> incremental builds: **both are done once per viable mutant.** So, anything you can do to make the
> `cargo build` and `cargo test` suite faster will have a **multiplicative** effect.

Mitigations it offers: skip doctests; a debug-symbol-free `mutants` cargo profile; ramdisks; and
faster linkers — *"Using the Mold linker on Unix can give a 20% performance improvement [...] On one
tree, using Wild cut the time to run cargo-mutants by more than half."*

Stryker's incremental mode — https://stryker-mutator.io/docs/stryker-js/incremental/ (**the tool's own
docs; interested party**) — makes no general performance claim, offering one worked example of reusing
3,731 of 3,965 mutant results.

#### Two cautions from cargo-mutants' own docs that undercut the diff-scoped gates above

These come from the tool's author, against his own tool, which makes them credible.
https://github.com/sourcefrog/cargo-mutants/blob/main/book/src/in-diff.md:
> `--in-diff` makes tests faster [...] However, **it's certainly possible that edits in one region
> cause code in a different region or a different file to no longer be well tested.** Incremental
> tests are helpful for giving faster feedback, but **they're not a substitute for a full test run.**
>
> **The diff is only matched against the code under test, not the test code. So, a diff that only
> deletes or changes test code won't cause any mutants to run**, even though it may have a very
> material effect on test coverage.

**That second sentence is a direct hole in the agent story.** A diff-scoped mutation gate is **blind to
a PR that only weakens tests** — precisely the agent failure mode every AGENTS.md above exists to
prevent. gatehouse, ha-home-keeper and ethercalc all have this hole. ethercalc partially covers it with
a nightly full matrix; the others do not.

And https://github.com/sourcefrog/cargo-mutants/blob/main/book/src/limitations.md:
> cargo-mutants can only help **if the test suite is hermetic: if the tests are flaky or
> non-deterministic, or depend on external state, it will draw the wrong conclusions** about whether
> the tests caught a bug.

Mutation testing is therefore **downstream of §5** — it does not work at all on a flaky suite.

### 4d. Emptiness finding: Martin Pool has not written about LLMs

The brief asks whether cargo-mutants' author (Martin Pool / sourcefrog) has connected mutation testing
to LLM output. **He has not, in any public artifact I could reach.**

Method: I downloaded the full repository tarball and grepped **all 80 Markdown files** — the book
(`book/src/*`, 39 pages including `goals.md`, `limitations.md`, `cautions.md`, `performance.md`,
`ci.md`, `pr-diff.md`), `NEWS.md`, `README.md`, `DESIGN.md`, `CONTRIBUTING.md` — for `LLM`, `AI`,
`coding agent`, `generative`, `copilot`, `claude`, `chatgpt`. **The only match in the entire tree is
the title line of `AGENTS.md`: "# Coding agents instructions for cargo-mutants"** — and that file is
ordinary build/test/style guidance with no mutation-testing rationale for agents at all. I separately
searched the issue tracker for `LLM`, `AI generated` and `agent`: the only relevant hit is issue #565,
*"✨ Set up Copilot instructions"* (2025-10-12). `book/src/goals.md` (*"tell you something interesting
about areas where bugs might be lurking or the tests might be insufficient"*) and https://mutants.rs/
make no mention of AI.

**If there is an argument from the tool's author that mutation testing is the right answer to
agent-written tests, it is not published.**

---

## 5. The test suite as the agent's own feedback loop

**Verdict: the thesis is partially documented, and the strongest evidence is narrower than the thesis.
In two of the best artifacts the direction is reversed.**

### IN USE

#### A team made tests faster and self-classifying, naming LLM agents as the reason

`tphakala/birdnet-go` (★1,596), PR #3754, opened and merged **2026-06-30** —
https://github.com/tphakala/birdnet-go/pull/3754:
> Refactors the `golangci-test` pipeline so PR feedback is faster and failures are **interpretable by
> humans and by LLM coding agents.**
> - **Shard the unit suite** across 4 parallel runners [...] cutting wall-clock from ~8m toward ~3m.
> - **Run every Go test job through `gotestsum`** with one automatic rerun (`--rerun-fails=1`). A test
>   that fails once then passes is reported as flaky, not a gate failure.
>   `--rerun-fails-abort-on-data-race` keeps real data races fatal (**a race is never retried away**).
> - **Fix the testcontainer MySQL flake at the source.**

The motivating sentence:
> There was no machine-readable signal saying "this is known-flaky infra," so **an agent picking up
> the PR would burn tokens "fixing" healthy code.**

The consuming policy — https://github.com/tphakala/birdnet-go/blob/main/AGENTS.md:
> `PASS (with flakes)` — tests that failed once then passed on rerun. These are flaky/infra [...] NOT
> a code regression. **Do not "fix" them; re-run or report instead.** [...] If a test is persistently
> flaky, **raise it rather than patching around it.**

**This is the one clean confirming case:** speed, determinism, and a machine-readable
flake-vs-regression channel, all changed for agents, in one dated PR. The repo also runs an automated
test-failure agent workflow (`.github/workflows/automated-test-engineer.yml`), so the loop is genuinely
unattended.

#### GitHub's own CLI engineered *around* a non-clean suite instead of cleaning it

`cli/cli` (★46,031), a scheduled unattended agentic workflow built on `github/gh-aw` —
https://github.com/cli/cli/blob/trunk/.github/skills/tech-debt-burndown/SKILL.md:
> This skill is built to run **unattended, on a schedule, in a loop.**
>
> ### Establish the validation baseline
> Before making any edit, record what already fails on clean `trunk` [...] **Do not require these to
> be green, and do not try to fix what they report.** Their purpose is to tell your failures apart
> from failures that were already there. [...] **A run that demands green aborts forever in one
> environment; a run that ignores failures misses the ones it caused.**
> [...] **Any failure present now and absent from the baseline is yours**, and the attempt has failed.

Plus the containment against gaming the check:
> **Never make a check pass by weakening it.** Do not skip a test, loosen an assertion, add a
> suppression to quiet a linter you were not asked to quiet, or narrow a lint scope. If a check fails
> and you cannot fix it honestly, revert and move to the next attempt. **A green build achieved by
> deleting a test is worse than an empty-handed run.**

**This is a genuine counter-datum to the strong form of the thesis, and should be reported as such:**
the largest, most credible organization in this section did **not** make the suite hermetic first. It
replaced "green" with "no worse than baseline" — a per-run differential.

#### Camunda: a committed flake protocol with "do not disable the test"

`camunda/camunda` (★4,255; AGENTS.md maintained through 2026-08-04) —
https://github.com/camunda/camunda/blob/main/AGENTS.md:
> Do not proceed without a green baseline. [...] If it is flaky (non-deterministic): 1. Search for an
> existing open issue [...] 2. Assign the issue to the engineer. 3. **Treat the baseline as passed and
> proceed — do not disable the test.**

Plus hermeticity rules aimed at the agent's own test-writing:
> - Use Awaitility for async waiting. **Never use `Thread.sleep`.**
> - Isolate tests with unique data (process/tenant/resource IDs) — **never reuse fixed identifiers
>   across tests, as collisions cause flakiness.**
> - **Fix the root cause of a flaky race rather than masking it with retries or longer waits.**
> - Always tear down resources you create [...] even on failure, to avoid cross-run flakiness.

#### De-flaking delegated *to* the agent rather than done to enable it

`glific/glific` (Tech4Dev, ★221) ships a skill whose whole job is de-flaking, with a repeated-run gate
— https://github.com/glific/glific/blob/master/.claude/skills/fix-flaky-tests/SKILL.md:
> **Verify after fix (mandatory)** — Run the flaky test(s) individually **3 times**. Run whole suite
> [...] **3 times**. Only conclude fixed when all required runs pass consistently.
> [...] **Hard guardrail** — If root cause cannot be demonstrated with evidence, **do not guess**.

**Note the direction: this is the opposite of the thesis.** The agent is the de-flaker, not the
beneficiary.

#### Committed containment against the agent weakening the check

- **Apache Camel K** (ASF) — https://github.com/apache/camel-k/blob/main/CLAUDE.md: *"Do **NOT** use
  `time.Sleep()` to wait for asynchronous state in tests. It leads to flaky, slow, and
  non-deterministic tests. [...] New test code MUST NOT introduce `time.Sleep()`."*
- **Ruby for Good / CASA** — https://github.com/rubyforgood/casa/blob/main/CLAUDE.md: *"No `sleep` in
  tests [...] **Flaky tests are disabled with `xit` + a tracking issue, never deleted.**"*
- **`userver`** (★2,955, Yandex-originated) —
  https://github.com/userver-framework/userver/blob/develop/AGENTS.md: *"If asked to fix a flaky
  failure and the root cause is in production code (not in the test itself), **first** add a new test
  that reliably reproduces the bug without flakiness, then fix the code."*
- **`abap2UI5`** (★376) — https://github.com/abap2UI5/abap2UI5/blob/main/AGENTS.md names the exact
  cheat: a system-ID guard *"makes the method a silent no-op in `npm run unit` while it still runs in
  a real system — **CI stays green over assertions nobody executes.**"* The sanctioned alternative is a
  skip list *"with a note naming the missing runtime capability; the runner then prints it as skipped
  instead of pretending it passed."*
- **`netclaw-dev/netclaw`** (★175, created 2026-02 — young) — the only case found where reward hacking
  is itself a **CI gate**: `dotnet slopwatch analyze  # Detect reward hacking (new violations fail
  CI)`, detecting *"disabled/skipped tests, suppressed warnings, empty catch blocks, hardcoded values,
  TODO-as-done comments"*, against a baseline file.
- **`GerritCodeReview/gerrit`** — hands the agent a Bazel tag filter that excludes flaky tests outright
  (`bazel test --test_tag_filters=-flaky //...`). Bazel's pre-existing hermeticity is leaned on rather
  than newly built.
- **`styled-components`** — *"Local suites run fast (well under 30s); **debug a slow suite rather than
  accept it.**"* The only committed speed *budget* found in a major project's agent policy.

#### Anthropic's docs make the check the mechanism of autonomy — and never discuss the check's own reliability

(*Vendor; primary for what Anthropic advises.*) https://code.claude.com/docs/en/best-practices:
> Claude stops when the work looks done. Without a check it can run, "looks done" is the only signal
> available, and **you become the verification loop: every mistake waits for you to notice it.** Give
> Claude something that produces a pass or fail, and **the loop closes on its own.**
> [...] Each step trades setup for attention. [...] **The `/goal` and Stop hook versions are what let
> an unattended run finish correctly without you.**

Mechanisms named: `/goal` conditions re-evaluated after every turn; a **Stop hook** as a deterministic
gate; a verification subagent for a second opinion.

Three things to note, because they bear directly on flakiness:
1. The canonical CLAUDE.md example advises **avoiding** the full suite for speed — *"Prefer running
   single tests, and not the whole test suite, for performance"* — rather than making it fast.
2. The `/goal` evaluator *"doesn't run commands or read files independently"*; it judges the
   transcript. **A flaky result that lands in the transcript is what it sees.**
3. Stop hooks are overridden after **8 consecutive blocks** — the de-facto answer to "what if the
   check never goes green", including because it is flaky.

**Nothing in Anthropic's documentation says the suite must be fast, deterministic, or hermetic for any
of this to work.** Given how load-bearing the check is in their own framing, **that silence is the
sharpest gap this strand found.**

### PROPOSED

- **Anthropic, *"Quantifying infrastructure noise in agentic coding evals"***, Gian Segato,
  **2026-02-05** — https://www.anthropic.com/engineering/infrastructure-noise — *"the gap between the
  most- and least-resourced setups on Terminal-Bench 2.0 was 6 percentage points (p < 0.01)"*; at
  strict enforcement *"as many as 6% of tasks were failing because of pod errors"*, dropping *"from
  5.8% at strict enforcement to 2.1%"* (p < 0.001); *"leaderboard differences below 3 percentage
  points deserve skepticism until the eval configuration is documented and matched."*

  > **Scope caution — this is about evals, not verification.** It shows environment nondeterminism
  > corrupting *the measurement of agent behaviour over time*. It does **not** show a team fixing a
  > production suite to enable autonomy. Do not let the two blur; this document's whole vocabulary
  > depends on keeping them apart.
- **Anthropic, *"Beyond permission prompts"***, Dworken & Weller-Davies, **2025-10-20** —
  https://www.anthropic.com/engineering/claude-code-sandboxing — hermeticity as **containment**
  (bubblewrap/seatbelt network and filesystem isolation; *"sandboxing safely reduces permission
  prompts by 84%"*). Explicitly not a determinism argument.
- **OpenAI Codex cloud environments** —
  https://learn.chatgpt.com/docs/environments/cloud-environment: *"during the agent phase, **internet
  access is off by default**"*. This yields a hermetic test environment as a side effect, but the
  stated rationale is security, not determinism. **Do not cite it as OpenAI arguing hermetic tests
  enable autonomy.**
- `EmeaAppGbb/spec2cloud` (★100, framework/advocacy): *"Never skip a test [...] Never delete a test
  [...] Never modify a test without human approval."*

### Reported emptiness

- **No engineering blog post or conference talk by a named practitioner describing "we fixed our
  flaky/slow tests so agents could run unattended."** birdnet-go PR #3754 is the closest artifact that
  exists, and it is a PR description, not a published narrative. Nothing from Google, Jane Street,
  Shopify, Stripe, or the Bazel/remote-execution community connecting test hermeticity to agent
  autonomy.
- **No vendor statement that suite speed or determinism is the limiting factor on agent autonomy.**
- **No CI-vendor marketing** ("flaky tests block your AI agents") surfaced via the primary-artifact
  route. Because web search was unavailable, treat this as **unmeasured**, not absent.

---

## 6. Where tests cannot carry the verification load

Six domains. For each: what actually catches the problem, and whether anyone ties it to agent-written
code.

### 6.1 UI / visual correctness

**The mechanism's own documented limit** (Playwright, vendor-neutral for this purpose) —
https://playwright.dev/docs/test-snapshots:
> Browser rendering can vary based on the host OS, version, settings, hardware, **power source
> (battery vs. power adapter)**, headless mode, and other factors.

The mitigations are `maxDiffPixels` / `maxDiffPixelRatio` / `threshold` — **a tolerance dial, not a
correctness oracle.** A pixel diff answers "did this change?", never "is this right?".

**IN USE — and the interesting finding is who is allowed to run it.**

| Org | Artifact | What it shows |
|---|---|---|
| **Adobe** (react-spectrum) | https://github.com/adobe/react-spectrum/blob/main/AGENTS.md | **The agent is forbidden from running the visual suite:** *"**Don't run `yarn chromatic` / `yarn chromatic:forced-colors`** — maintainers run the VRT suites."* Visual regression is held by humans. |
| **Owncast** | https://github.com/owncast/owncast/blob/develop/AGENTS.md | Chromatic in CI, *and* the agent's job is to produce evidence for a human: *"UI changes: include before and after screenshots, plus the Chromatic Storybook link from the PR's Chromatic job."* |
| **Sanity** | https://github.com/sanity-io/sanity/blob/main/AGENTS.md | *"Visual regression runs on Chromatic via `.github/workflows/chromatic.yml`."* |
| **rust-lang/crates.io** | https://github.com/rust-lang/crates.io/blob/main/AGENTS.md | *"Visual regression testing uses Percy (via Playwright) and Chromatic via Storybook"* |
| **Mozilla** (pdf.js) | https://github.com/mozilla/pdf.js/blob/master/AGENTS.md | Reference images in `test/ref/` |
| **Cloudflare** (kumo) | https://github.com/cloudflare/kumo/blob/main/ci/AGENTS.md | *"**Visual regression**: Creates ephemeral `vr-screenshots-{pr}-{runId}` branches for diff images"* — published **for a person to open**, not asserted pass/fail. |
| **actualbudget/actual** | https://github.com/actualbudget/actual/blob/master/AGENTS.md | Determinism by containment: `yarn vrt:docker` — *"Visual regression in Docker (consistent environment)"*. |
| **Khan Academy** (perseus) | `packages/perseus/src/widgets/AGENTS.md` | Agent instructed to author regression stories for Chromatic. |
| dell-mic/file-glance (small) | https://github.com/dell-mic/file-glance/blob/main/AGENTS.md | Names the failure mode: *"Snapshot tolerance is loose: `maxDiffPixels: 100` … **Prefer small visual diffs over regenerating snapshots frivolously.**"* |

**The Adobe line is the most important artifact in this domain**: a committed, well-known-org statement
that an existing automated visual gate is *withheld from the agent*.

**A structural problem specific to agent harnesses.** Playwright now ships a first-party **healer**
agent that *"executes the test suite and automatically repairs failing tests"* —
https://playwright.dev/docs/test-agents (Microsoft; stake: harness vendor). **An agent that can rewrite
the gate is not gated by it.** Snapshot baselines are the softest case: regenerating a `.png` turns a
failure green with **no diff a reader would flag**. No primary artifact anywhere solves this;
dell-mic's rule is prose.

**Vendor claims — Applitools** (commercial visual-testing vendor) markets an "agentic SDLC gap" and
claims Visual AI *"eliminates false positives, AI drift, and test hallucinations"* via a "Deterministic
Language Model", *"100% reproducible"* — https://www.applitools.com/. **This is marketing copy on the
vendor's own homepage.** No independent artifact found of an org gating agent-written UI changes on it.

**What replaces tests: a human still looks.** No artifact treats a green visual diff as sufficient to
merge an agent's UI change. The committed pattern is that the automated diff **narrows what the human
looks at** (owncast's link, Cloudflare's ephemeral diff branch), or the gate is **withheld** (Adobe).
Screenshot comparison also appears as an *iteration* signal inside the agent loop — Anthropic
recommends *"take a screenshot of the result and compare it to the original. list differences and fix
them"* — **but that is the agent steering toward a target, not a gate establishing correctness.**

### 6.2 ML / nondeterministic output

**This is where the eval/verification distinction does the most work.** Evals measure behaviour across
a distribution over time; verification establishes that *this change* is correct. **An eval score
cannot verify a change.** At the variance levels these harnesses openly report, a few points' move on a
200-case eval does not establish that the diff in front of you is right.

**Anthropic's own eval doc reinforces this by what it optimises for** —
https://platform.claude.com/docs/en/test-and-evaluate/develop-tests (Anthropic; stake: model vendor):
> **More questions with slightly lower signal automated grading is better than fewer questions with
> high-quality human hand-graded evals.**

**Volume over per-item signal is a measurement design, not a verification design.** `openai/evals`
frames the same way — *"a framework for evaluating large language models (LLMs) or systems built using
LLMs"* — https://github.com/openai/evals.

**IN USE**

| Org | Artifact | Mechanism |
|---|---|---|
| **HyperDX** | https://github.com/hyperdxio/hyperdx/blob/main/AGENTS.md, `packages/hdx-eval/README.md` | The most complete real artifact found: *"**Generates deterministic synthetic telemetry** (traces + logs) with **planted anomalies**, spawns Claude Code as an SRE agent…, records full trajectories, and grades answers using **programmatic checks and an LLM-as-judge**."* Plus a *"dual-slot A/B comparison workflow"*. Note the layering: determinism is manufactured in the **fixture**; the judge grades only the free-text residue; measurement is **comparative**. |
| **elizaOS** | `packages/scenario-runner/AGENTS.md` | `judge.ts # judgeTextWithLlm()`, with `final-checks/` for deterministic assertions alongside. Same layering. |
| mikeyobrien/ralph-orchestrator (small) | https://github.com/mikeyobrien/ralph-orchestrator/blob/main/AGENTS.md | *"**Backpressure Over Prescription** — Don't prescribe how; create gates that reject bad work. [...] For subjective criteria, use **LLM-as-judge with binary pass/fail**."* Binary, not scalar — a deliberate choice to make a judge gate-shaped. |
| songsuijie/SCUT-Campus-Compass (small/individual — but the most epistemically careful artifact found) | https://github.com/songsuijie/SCUT-Campus-Compass/blob/main/AGENTS.md | Refuses to let an eval stand in for verification: *"actual answer-faithfulness labels remain `not_run` **until a human records** `SUPPORTED` / `PARTIALLY_SUPPORTED` / `UNSUPPORTED`"* and *"It does not turn those candidates into a quality metric… before human review."* |

**PROPOSED** — **promptfoo** (commercial eval vendor) —
https://github.com/promptfoo/promptfoo/blob/main/site/docs/guides/evaluate-coding-agents.md:
*"Run coding agent evals like integration tests"*; *"Run evals multiple times with `--repeat 3` to
measure variance"*; *"Test the system, not the model"*; and for single changes, *"For file-level
verification, read the files after the eval or enable tracing"* rather than trusting the agent's
self-report. **Note that `--repeat 3` is itself an admission that a single eval run establishes
nothing about a single change.**

**Emptiness:** **no artifact from a well-known org gating merges of agent-authored changes on an eval
score threshold.** The one CI-threshold example that surfaced appears only as a description of a
third-party project inside a secondary guide repo and was not chased to a primary artifact. Treat
"eval score as merge gate" as **PROPOSED, unproven at scale**. Braintrust and LangSmith were not
fetched — recorded as a gap rather than filled with a guess.

**What replaces tests: nothing fully.** Three partial substitutes: (a) **manufacture determinism in the
fixture** so ordinary assertions apply again (HyperDX's planted anomalies — the strongest move
available); (b) **assert on the path, not the output** — did the tool actually run; (c) LLM-as-judge
with **binary** verdicts for the irreducible remainder. (c) is a nondeterministic system judging a
nondeterministic system, and nobody credible claims otherwise. Where the answer genuinely matters, the
artifacts fall back to a human label.

### 6.3 Distributed-systems race conditions

**The most mature techniques, the weakest agent link — with one significant exception.**

| Technique | Primary source | Key claim |
|---|---|---|
| **FoundationDB simulation** | https://apple.github.io/foundationdb/testing.html | *"Simulation is able to conduct a **deterministic** simulation of an entire FoundationDB cluster within a single-threaded process. Determinism is crucial in that it allows perfect repeatability."* Tens of thousands of simulations nightly; cumulatively *"roughly one trillion CPU-hours"*. |
| **TigerBeetle VOPR** | `docs/internals/vopr.md` | *"Because our simulator is deterministic based on a **seed** number and the Git commit, we can perfectly reproduce any bugs discovered in testing."* Stubs clock, network, disk. |
| **Jepsen** | https://jepsen.io/analyses | *"we evaluate real binaries running on real clusters"* under *"faulty networks, unsynchronized clocks, and partial failure"*, checked against *"a model to establish its correctness"*. Two dozen-plus systems, 2013–2025. |
| **loom** (Rust) | https://github.com/tokio-rs/loom | *"It runs a test many times, permuting the possible concurrent executions of that test under the C11 memory model."* Self-stated limit: *"there can be a bug in the checked code even if Loom says there is no bug."* |
| **shuttle** (AWS Labs) | https://github.com/awslabs/shuttle | *"a soundness—scalability trade-off"*, and explicitly: *"**Shuttle is not sound (a passing Shuttle test does not prove the code is correct).**"* |

**IN USE — Apple / FoundationDB is the one real agent link.** `apple/foundationdb` ships an AGENTS.md
that routes AI coding agents into the simulator —
https://github.com/apple/foundationdb/blob/main/AGENTS.md:
> `fdbserver -r simulation` runs the entire cluster in a single process using Sim2, a deterministic
> simulated network. `BUGGIFY` macros inject faults (delays, failures, corruption). Tests are TOML
> files that compose workloads. **This is FDB's primary testing strategy.**

It also makes simulation gate-shaped for an agent: *"A `SevError` (Severity 40) `TraceEvent` **fails** a
simulation/Joshua run"*, and an oversized trace event *"is **dropped entirely** and re-logged as
`TraceEventOverflow` — at `SevError` in simulation, so an oversized event **fails the test**."* And it
draws the iteration/bulk line: *"Local `fdbserver -r simulation` runs are for iteration; large-scale
shake-out happens on Joshua."*

**ABSENCES.** `tigerbeetle/tigerbeetle` has **no** AGENTS.md, CLAUDE.md, or
`.github/copilot-instructions.md` (checked 2026-08-28) — a world-class VOPR with **no stated
relationship to agent-written code**. Jepsen, loom, shuttle and TLA+/P have no agent tie in any primary
source found; Jepsen in particular is an external, commissioned, human-expert activity on a released
binary and is **structurally incapable of gating a PR**, agent-written or not.

**Vendor claims — Antithesis** (commercial deterministic-simulation vendor; stake at every mention) is
the only party making the agent link loudly:
- Homepage https://antithesis.com/ — *"merge big changes confidently — **even when they're authored by
  agents**"*; *"As AI drives down the cost of producing code, the pressure to ship faster rises."*
  Named customers attributed on their own site: Jane Street, Confluent, Ethereum Foundation, etcd,
  Turso, Mysten (Sui), Tigris Data, ParadeDB, Formance, PingThings, Synadia, Filecoin.
- https://antithesis.com/blog/2025/ai_testing/ (2025-07-23) — argues AI-written tests can't verify
  AI-written code because *"example-based testing only accounts for the things engineers, or AI, think
  may go wrong."*
- https://antithesis.com/blog/2026/agent_skills/ (2026-03-25) — **read carefully; this does not claim
  what the homepage implies.** The three skills help an agent *onboard a project onto Antithesis*; they
  do not verify the agent's own diff. And Antithesis disclaims them: *"because the product of these
  skills is driven by your LLM, **we can't provide a hard guarantee that they'll work.**"*

**What replaces tests:** deterministic simulation genuinely does catch what tests cannot, and it is the
one technique here that arguably *replaces* rather than supplements them. **But it requires building
the system to be simulatable** (single-threaded, stubbed clock/network/disk) — an architectural
commitment made years before any agent touched the code, **and one no agent can retrofit.**

### 6.4 Performance regressions

**The noise problem, quantified.** Bencher (open-source + commercial; stake noted) —
https://bencher.dev/docs/explanation/continuous-benchmarking/: *"General purpose CI environments are
often noisy and inconsistent when measuring wall clock time"*, with GitHub Action Runners seeing
**">30% variance" between runs** versus <2% on their bare-metal runners. CodSpeed (commercial; stake
noted) splits it two ways: **CPU-instruction simulation** for algorithmic benchmarks (removes
wall-clock variance by not measuring time) and bare-metal macro runners for walltime —
https://codspeed.io/docs/features.

> Note what instruction counting actually buys: **a reproducible number that is not the thing you care
> about.** It is deterministic precisely because it ignores cache, memory and scheduling — where real
> regressions often live.

**IN USE — CodSpeed as a committed agent-facing gate:**
- **online-ml/river** — https://github.com/online-ml/river/blob/main/AGENTS.md — the clearest statement
  of intent: *"Speed matters a lot in online machine learning. Therefore, a golden rule for
  implementation is to not introduce significant slowdowns. **We use CodSpeed to detect regressions in
  pull requests.**"* And as a task instruction: *"Add a new CodSpeed benchmark entry, in order to
  detect future regressions."*
- **tursodatabase/turso**, **atuinsh/atuin**, **web-infra-dev/rspack**, **aio-libs/yarl**,
  **reactive/data-client**, **dymmond/ravyn**, **NFFT/nfft** — CodSpeed named in agent-facing CI lists.
- **starkware-libs/stwo** — https://github.com/starkware-libs/stwo/blob/main/AGENTS.md puts a benchmark
  check at the end of an agent pipeline (*"Perf Specialist … → Math Reviewer … → **CI benchmark
  regression check**"*), immediately followed by a human escalation clause: *"Escalate to human
  IMMEDIATELY when: 1. Any undocumented paper-implementation divergence is discovered 2. A
  soundness-critical component has zero test coverage for the modified path."*
- **styled-components** — *"Always microbenchmark to validate optimizations. Bench the realistic
  workload, not a synthetic best case. Revert changes that pessimize the path actual callers take,
  even if they win in isolation."*

**IN USE — the browser vendors keep a named human.** Chromium runs automated detection and bisection
and still routes every alert to a person —
https://chromium.googlesource.com/chromium/src/+/main/docs/speed/addressing_performance_regressions.md:
the bisect bot names a culprit CL, but engineers must validate causation, and a regression can be
disputed either by showing the CL *"couldn't be the cause"* or by arguing *"the regression is
justified"* — **a judgement no gate can make, because it is a trade-off, not a fact.** Also the platform
trap: *"Often, a performance regression only affects a certain type of hardware or a certain operating
system, which may be different than what you tested locally."* Test ownership is human and named:
*"Each test has an owner, named in this spreadsheet."*

**What replaces tests:** benchmark gates work in CI **only after you have bought your way out of the
noise** — by measuring something other than time, or by buying dedicated hardware. Both are purchases,
and both are the vendors' own framing of why their product exists. On stock runners, a naive
`cargo bench` gate at >30% variance is pure noise. The IN USE evidence is real and reasonably broad,
but it is **almost entirely one vendor's product appearing in agent instructions** — and the two orgs
with the deepest performance culture keep a human sheriff, because *"is this regression justified?"* is
not a measurement.

### 6.5 Security properties

**Can tests express them? Mostly no.** Security properties are universally quantified ("no input causes
X"); a test is existential ("this input doesn't"). That gap is why the replacements here are **fuzzing**
(search over inputs) and static analysis (search over paths), not tests.

**IN USE — Google / OSS-Fuzz + DeepMind CodeMender is the strongest artifact in this entire report,**
because it is a production pipeline where **an AI agent authors security patches to real open-source
code** and publishes exactly what verification it applies —
https://google.github.io/oss-fuzz/ai-patches-beta/ (beta; source at
https://github.com/google/oss-fuzz/blob/master/docs/AI%20patches%20(beta).md):
> The patches are generated by **CodeMender, an AI coding security agent from Google DeepMind.**
> * We proactively check your repository's guidelines before engaging; **if your project restricts AI
>   code, we honor that choice and withhold submissions entirely.**
> * We verify that each patch works, **testing every fix in an isolated environment to prove that it
>   compiles cleanly and successfully resolves the crash.**
> * As a temporary measure during this beta phase, **Google engineers known as *patch shepherds*
>   personally review proposed patches.**

and to the receiving maintainer: *"We recommend that you approach AI-proposed patches with the same
rigor you would use for any other proposed submission."*

**Read the layers.** (1) The **fuzzer-found reproducer is the ground truth** — a crashing input is an
objective, reproducible oracle, which is exactly what security properties normally lack. (2) Automated
verification is **narrow and honestly scoped**: it compiles, and *the specific crash stops
reproducing*. That does **not** establish the patch is correct, only that it closes the one hole.
(3) A **named human** reviews every patch. (4) The maintainer reviews again. (5) Containment default:
opt-out honoured *"entirely"*. Google states the human layer is *"temporary"* — **that is an intention,
not evidence, and should not be reported as a plan that has succeeded.**

**Agents building the verification mechanism, with published results.** `google/oss-fuzz-gen`
*"generates fuzz targets for real-world C/C++/Java/Python projects with various Large Language
Models"*, documenting **30 discovered vulnerabilities**, including **OpenSSL CVE-2024-9143**
(OOB read/write), across *"160 C/C++ projects"*, with up to *"29%"* line-coverage increase over
human-written targets, and bugs that *"were not reachable with existing OSS-Fuzz targets"* —
https://github.com/google/oss-fuzz-gen (experiment dated 2024-01-31). **This is the inverse of the
question asked — an agent extending the search rather than being searched — and it is stronger evidence
of value than any agent-gating story in this report.** OSS-Fuzz baseline: ~1,000 projects, 10,000+
vulnerabilities and 36,000 bugs (figures stated as of August 2023).

**IN USE — committed policy that security is not delegated to the agent:**

| Org | Verbatim |
|---|---|
| **Microsoft / Azure** (azure-sdk-for-python) | `## Prohibited Operations`: *"❌ Merging PRs without human review / ❌ Releasing packages to PyPI / ❌ Modifying CI/CD pipeline definitions / ❌ **Changing security or authentication logic without security review** / ❌ Committing secrets or credentials / ❌ Force pushing to protected branches"*. Restricted (⚠️ requires review) includes *"**Disabling or removing tests (requires explanation)**"*. |
| **MongoDB** (mongo-java-driver) | Line 3 of AGENTS.md, before anything else: *"**All changes require human review.**"* |
| **Microsoft / Azure** (azure-sdk-for-cpp, storage) | *"## Escalation / Human Review Triggers [...] **Authentication/signing logic.** Retry/pipeline policy semantics. Cross-package refactors [...] Test proxy / recording sanitization policy adjustments."* |
| **Cloudflare** (circl, crypto) | *"**Every change is security-sensitive.**"* |
| **OWASP** (dep-scan) | *"Treat workflow files as security-sensitive code. **A one-line change in `.github/workflows/` can have a larger blast radius than a medium-sized Python change.**"* |
| **jPOS-EE** (financial) | *"jPOS-EE is a conservative, production-oriented codebase used in security-sensitive financial systems."* |
| roostorg/osprey | *"**Every new or upgraded package including transitive dependencies requires human approval.**"* Plus, even-handedly: *"**Same review bar.** PRs authored with agent assistance are held to the same standards as any other PR."* |

**On CodeQL:** GitHub's introduction page describes it as *"the code analysis engine developed by GitHub
to automate security checks"* and **states no limitation about false negatives or about not
substituting for human reading** —
https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning.
**That silence is worth flagging: the vendor page does not tell you what the tool misses.**

**What replaces tests:** fuzzing, and it genuinely works, because it converts a universally-quantified
property into a concrete reproducible artefact that ordinary automation can check. **This is also the
domain with the most explicit committed human gates at large orgs.** Google, running the most advanced
agent-writes-security-patches pipeline in existence, keeps a named human on every patch. **Nobody
credible has removed the human here.**

### 6.6 Anything with real side effects

**No technique replaces tests here, because the problem is not verification — it is that the action is
irreversible.** Every artifact responds with **containment**: reduce the agent's autonomy for that
specific action class.

**Migrations**
- `usesend/useSend` — *"**Never run migrations unless users explicitly asked**"*
- `icoretech/airbroke` (`prisma/AGENTS.md`) — *"Never edit `migrations/migration_lock.toml` manually.
  / **Never rewrite an applied migration to match a newer desired schema.** / Never run migrations
  against the test database by borrowing the `web` service's development URL."*
- `unav4ila8le/foliofox` — **authorship split from execution**: *"**Do not create Supabase migration
  files. Ask the user to create an empty migration file first**, then edit that file only after it
  exists. [...] **the user will apply the migration**."*

**Production mutation**
- **Cloudflare** (kumo) — an anti-patterns table with a **dry-run escape hatch**: *"Running
  `release-production.sh` as agent | Sensitive operation | **Human-only; use `DRY_RUN=true` to
  test**"*, and *"Production release script gates all destructive operations; logs what would
  happen."* **The best-designed single example found** — containment plus a safe rehearsal path.
- `dezwier/mesozoica` (small, but the sharpest formulation) — *"**Never run production-mutating jobs
  just to validate code.** Cron, sync, prune, backfill, migration, and image upload commands require
  explicit task scope."* This names the exact trap: **an agent reaching for a real side effect as its
  verification step.**
- **Elastic** (rally) — *"**Never benchmark a production or production-like cluster.** Rally creates
  and mutates indices, and any competing traffic invalidates results."*

**Messages, releases, deletions**
- **Microsoft / Azure** — *"❌ Releasing packages to PyPI"* (prohibited outright).
- `NetVar1337/unleash` — *"**Do not send email / Slack / messages / create public PRs** without
  **in-session** acknowledgement."* Note *in-session*: prior approval does not carry forward.
- `shakacode/react_on_rails` — the most elaborate **graduated gate keyed to blast radius**: beta →
  *"**Lowest.** Confidence note + green required checks"*; rc → *"**Higher.** [...] **zero open
  MUST-FIX**"*; final → *"**Highest.** [...] only cherry-picked, fully-verified fixes; **no new
  features**; **human sign-off on the promotion**. No confidence-only auto-merge."* Plus:
  *"**Direct live Rake invocation remains BLOCKED**; [...] **preview-only**."*
- **Grafana** — a containment rule born from a real agent failure —
  https://github.com/grafana/grafana/blob/main/pkg/router/AGENTS.md:
  > **## Rule: never delete interfaces in `types.go` without human sign-off** [...] **This rule exists
  > because an earlier refactor dropped `Router` while unifying the serving types — the interface was
  > future-facing, not dead.**

  This is the general case of an unverifiable property: **no test can encode intent about the future**,
  so deleting a deliberately-unused seam is invisible to every automated gate.
- `ShellyUSA/Hubitat-Drivers` states the criterion generically, which is why it is worth quoting:
  *"When to require human sign-off — **Any change that cannot be validated automatically** (websocket
  behavior, firmware upgrades, new device protocols)."*
- `microsoftgraph/kibali` — a **template placeholder**, itself a finding about how nascent this is:
  *"[REPLACE: Define what actions AI may take autonomously vs. what requires human approval.]"*

**PROPOSED:** staged rollout / canary appears in agent instructions as ordinary product practice
(warpdotdev/warp, Automattic/wp-calypso, apache/superset), but **nobody found ties canary deployment
specifically to containing agent-written code.**

**What replaces tests: nothing, and nothing tries to.** The universal answer at every org size is to
remove the action from the agent's autonomy — never, human-approval, or dry-run-only. **Dry-run and
authorship/execution splitting are the two genuinely good mechanisms**, because they preserve most of
the agent's usefulness while keeping the irreversible step in human hands.

---

## 7. Cross-cutting conclusions

1. **The circularity problem is measured and the numbers are bad — but the measurements are all of the
   wrong experiment.** −47% bug detection from buggy-code context is the closest anyone has come. **The
   experiment that matters — does an agent's suite catch that agent's own defects — has not been run.**

2. **The live practice is a substitution, not an abandonment of testing.** Airflow, `phase-rs`, nWave,
   `coleam00`, `rshankras` and every mutation-gating project converge on the same replacement:
   **"would this test fail if the change were reverted?"** Coverage survives in two narrow roles —
   diff-scoped ("100% of what the PR changes") and ratcheted ("never worse").

3. **Every gate that works had to be paired with a rule forbidding the agent from gaming it.** Mutation
   scores get padded suites and exclusions; coverage gets assertion-free tests; snapshots get
   regenerated; flaky tests get retried away. **The rule is always prose. The gate is always code.
   That asymmetry is the practical finding.**

4. **Agents can edit their own judge, and almost nothing detects it.** Playwright ships a healer agent
   that repairs failing tests. Azure has to explicitly list *"Disabling or removing tests"* as
   restricted. Diff-scoped mutation gates are, by cargo-mutants' own documentation, **blind to a PR
   that only weakens tests.** The only structural answer found anywhere is `coleam00`'s protected
   `harness/**` plus a human-only floor file — *"a builder that can edit its own judge can make any
   claim true."* **This is the largest gap in the material.**

5. **Determinism is the scarce resource, and it must be built in advance.** FoundationDB's Sim2,
   TigerBeetle's stubbed clock/network/disk, HyperDX's planted-anomaly fixtures, actualbudget's
   Dockerised visual runs, CodSpeed's instruction counting, cargo-mutants' hermeticity precondition —
   **every working mechanism in this report is manufactured determinism, and none of it can be
   retrofitted by the agent that needs it.**

6. **The most common committed answer across all six failure domains is not a verification mechanism at
   all — it is reduced autonomy for a named action class.** Adobe withholds the visual suite. Azure
   prohibits touching auth. Cloudflare marks the release script human-only. **The classification
   attaches to the action, not to the change** — which is exactly the per-action framing this document
   uses for autonomy.

7. **Three domains have real non-vendor mechanisms** (security via fuzzing; concurrency via
   deterministic simulation; performance via instruction counting). **Three do not** (UI,
   nondeterministic output, side effects) — and in those three the artifacts fall back to a human
   every time.

---

## Blocked sources — none circumvented

| URL / endpoint | Block type | Handling |
|---|---|---|
| `https://html.duckduckgo.com/html/?q=...` | **CAPTCHA challenge** ("Select all squares containing a duck") | Abandoned immediately. Not circumvented. Switched to other services. |
| `https://www.mojeek.com/search?q=...` | **HTTP 403 Forbidden** | Abandoned. |
| WebSearch tool | **Session budget exhausted** (200/200 calls used before this task began) | Not retried. All findings obtained via `gh` CLI against primary artifacts and direct WebFetch. |
| GitHub code search API (`/search/code`) | **HTTP 403 rate limit** (10/min) and **403 secondary abuse limit**, hit repeatedly across the research threads | Paced and waited for documented resets; never circumvented. Several planned queries were never run — notably `Goodhart` and `"mutation score"` filtered to AGENTS.md, and deeper `deterministic` / `hermetic` / `nondeterministic` sweeps. Recorded as a genuine gap in coverage of this sweep. |
| `https://openai.com/index/chain-of-thought-monitoring/` | **HTTP 403 Forbidden** | Substituted the authors' own arXiv paper, arXiv:2503.11926, same content, no circumvention. |
| `https://www.anthropic.com/research/reward-hacking` | **HTTP 404** (guessed URL) | Not pursued further. |
| `https://www.anthropic.com/engineering/claude-code-best-practices` | **308 redirect** to `code.claude.com/docs/en/best-practices` | Followed. **Note:** the original 2025-04-18 post text is no longer retrievable; the living doc replaced it. All quotes are from the current doc as fetched **2026-08-28**, not from the 2025 post. |
| `https://developers.openai.com/codex/best-practices`, `https://learn.chatgpt.com/docs/agents-md`, `https://learn.chatgpt.com/docs/environments/agents-md` | **308 → 404 / 404** | Substituted `learn.chatgpt.com/docs/environments/cloud-environment`. |
| `https://export.arxiv.org/api/query?...` | **HTTP 429 Too Many Requests** (once), and one **60s timeout** | Not retried against the API; used `arxiv.org/abs/<id>` pages instead — same publisher, no circumvention. |
| `https://testing.googleblog.com/2020/08/code-coverage-best-practices.html` | **Body not extractable** (JS-rendered Blogger shell; not a paywall) | Not obtained. Substituted the peer-reviewed Google paper (ESEC/FSE 2019). **Do not cite that blog post's specifics from this document.** |
| `https://testing.googleblog.com/feeds/posts/default?q=...` | **302 → FeedBurner → `ECONNREFUSED`** | Abandoned. |
| ACM DL full text, *"Code coverage at Google"* | **Paywalled** | Not attempted. Only the open abstract on research.google is used. |
| `https://chromium.googlesource.com/.../perf_regression_sheriffing.md` | **WebFetch timeout (60s)** | Substituted `addressing_performance_regressions.md` and `speed/README.md` on the same host. |
| `https://security.googleblog.com/2025/10/introducing-codemender-...`, `.../2024/11/leveling-up-fuzzing-...` | **404 (guessed URL)** / **navigation chrome only** | Substituted the primary artifacts: the OSS-Fuzz AI-patches doc and `github.com/google/oss-fuzz-gen`. |
| `https://google.github.io/oss-fuzz/getting-started/ai-patches/` | **HTTP 404** (guessed path) | Located the real artifact via the repo tree. |
| Braintrust, LangSmith eval docs | **Not fetched** (time/budget) | Recorded as a gap. Both are commercial eval vendors; anything found would have been PROPOSED, not IN USE. |

### Dating caveats

Repository files are quoted from the default branch as of **2026-08-28**; unless a commit date is
given, **the authoring date of any specific quoted rule is undetermined** — I did not run per-line
`git log` for most files. Dated items: birdnet-go AGENTS.md flake section (**2026-06-30**, PR #3754);
camunda AGENTS.md (touched through **2026-08-04**); Apache Airflow AGENTS.md (**2026-08-12**);
ethercalc CI mutation-gate budget comment (**2026-08-10**); OWASP Juice Shop skill (**2026-07-31**);
Antithesis posts (**2025-07-23**, **2026-03-25**); oss-fuzz-gen experiment (**2024-01-31**); OSS-Fuzz
scale figures (**August 2023**); Jepsen analyses (2013–2025). Playwright, Anthropic, Bencher, CodSpeed,
GitHub CodeQL and OSS-Fuzz AI-patches pages carry **no visible date**; fetch date is 2026-08-28.

### Repository credibility, stated plainly

Star counts and ages retrieved 2026-08-28, so the reader can weight the artifacts rather than take
"an AGENTS.md says so" as industry practice.

**Large / well-established:** styled-components ★41,127 (2016) · apache/spark ★43,894 · apache/airflow
★46,623 · cli/cli ★46,031 · mastra ★27,532 · turso ★24,047 · juice-shop ★13,730 · Polly ★14,232 ·
camunda ★4,255 · ethercalc ★3,042 (2011) · userver ★2,955 · birdnet-go ★1,596 · growi ★1,464 ·
teams-sdk ★724 (Microsoft) · Htmxor ★160 · frozenlist ★127 (aio-libs org). Plus Adobe, Apple, Google,
Microsoft/Azure, MongoDB, Mozilla, Cloudflare, Grafana, Elastic, Khan Academy, Sanity, rust-lang,
Picnic, OWASP, Jane Street, AWS — cited from their own repositories or engineering publications.

**Small but mechanism-verified in CI (cited for the mechanism, not as evidence of adoption):**
gatehouse ★346 · manim-voiceover ★314 · ha-home-keeper ★66 (created 2026-06) · error-prone-support ★38
(Picnic, since 2018) · ox-tools ★13 (Microsoft, created 2026-03).

**Tiny — cited only where the formulation is unusually precise, and never as evidence of practice:**
go2rust ★9 · nba-ruby ★3 · worldsim ★0 · ai-fastify-template ★18 (stale since 2025-07) ·
tomevault-io/tomes ★1 · jdforsythe/ACT ★0 · mutineer ★7 (vendor's own docs).
