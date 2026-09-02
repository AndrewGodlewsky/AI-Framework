# Digest: The AI-Native SDLC Playbook (Anthropic Academy)

**Digest date:** 2026-09-02
**Ticket:** [#20 Digest the AI-Native SDLC Playbook](https://github.com/AndrewGodlewsky/AI-Framework/issues/20)
**Source:** Compiled transcript of the Anthropic Academy course *The AI-Native SDLC Playbook*
(14 lessons, academy.claude.com, retrieved 2026-09-02, content © Anthropic). Reference copy:
`reference/ai-native-sdlc-playbook.html`, committed at the owner's decision (2026-09-02) with
its compilation notice and © attribution intact. Quotes here are short and attributed.

**Evidence tier for everything in this file: vendor.** Anthropic describing its own product and
its Applied AI team's recommended practice ("inspired by working with our customers"). The course
publishes **no measurements**: every play defines leading and lagging indicators and reports no
values against them — an exemplary measurement framework and a non-existent result, the same
shape the corpus recorded for Dropbox.

---

## 1. What the playbook is, in this project's terms

Fourteen lessons across six SDLC stages (Plan → Design → Build → Test → Deploy → Maintain),
each play structured as What changes / Getting started / How to execute / Governance
considerations / How to measure. The organizing thesis is the corpus's own: *"The bottleneck
moves to the stages on either side of the build phase"* and *"The controls stop matching reality…
Reviewing each line by hand made sense when a person had written it, but it can't keep up once
agents write most of the diff"* (L1).

**The archetype verdict.** The playbook's recommended end state is a **Workspace ceiling in auto
mode for the build phase, a Contributor ceiling at the repository, and a Committer-shaped
pre-authorisation only for rehearsed runbooks** — with the production gate explicitly withheld:
*"the agent may act up to the production gate and cannot pass it"* (L12). Nowhere does the vendor
recommend granting merge rights on the agent's judgment or an unattended path to production. The
platform's own structural pin (branch protection; *"anything the agent writes arrives as a PR…
the agent has no route to push to main"*, L12) is presented as the governing principle, not a
limitation to engineer around. This is the fullest single vendor artifact organizing an entire
SDLC around the spectrum's near-middle, and it corroborates the corpus's Contributor finding: the
archetype the tool market ships.

## 2. Play inventory, mapped to the spectrum

| Lesson | Play | Stage | Archetype it assumes or pushes toward |
|---|---|---|---|
| L1 | Introduction | — | The spine's premise, vendor-stated: per-line human reading does not scale past Autocomplete |
| L2 | Capture as intent.md | Plan | Pre-archetype (non-engineers, claude.ai/Cowork); begins the committed-artifact provenance chain |
| L3 | Requirements and design | Design | **Contributor** once automated: a non-interactive job fires on the intent merge and *commits spec.md as a pull request* |
| L4 | Plan mode as the default start | Build | **Workspace**, gated (plan mode "can read the codebase without changing anything"); the *auto mode* subsection recommends moving oversight within Workspace — "away from watching the agent make edits… toward the review of artifacts after longer autonomous sessions" — as guardrails mature |
| L5 | The CLAUDE.md | Build | Context engineering as a reviewable artifact; knowledge, not a control |
| L6 | Skills as institutional knowledge (+ build-time hooks) | Build | Workspace; **the advisory/deterministic split stated by the vendor** (§3.1) |
| L7 | Parallel sessions and subagents | Build | Workspace parallelism via worktrees; reviewer attention named as the ceiling — "add sessions only while review is keeping up" |
| L8 | Give Claude a feedback loop | Test | The corpus's "single enabling condition" (a test suite the agent cannot lie to), plus engineered anti-suppression (§3.2) |
| L9 | Continuous evals in CI | Test | Eval regression testing for agent configuration (CLAUDE.md, skills, hooks), gated as a merge check (§3.3) |
| L10 | AI in the PR review loop | Deploy | **Contributor**: findings "do not approve or block a PR on their own"; code-owner approval via branch protection; agent addresses comments and "babysits" its PRs to green |
| L11 | Hooks as approval gates (+ managed settings) | Deploy | The **administrator-flippable ceiling, documented as a product control plane** (§4.1, §3.4) |
| L12 | CI/CD integration and deployment | Deploy | Agent in the pipeline up to a withheld production gate; per-environment tiers — "In development, the agent deploys freely" (ceiling is per-scope, as `CONTEXT.md` defines) |
| L13 | Closing the loop on metrics (+ Claude Tag) | Maintain | Autonomous loop with deterministic detection and tiered response bands (§4.2); acts only via the PR gate or a **pre-approved runbook** — the pre-authorisation shape again |
| L14 | Closing thoughts and resources | — | The admin/control-plane documentation inventory |

## 3. Corroborations — the vendor stating what the corpus found

1. **Instruction files are advisory; controls are deterministic** (L6): *"A skill is a control,
   though an advisory one… nothing forces a session to comply with it. A policy that must always
   hold needs something deterministic behind the skill… The skill makes violations rare and the
   hook makes them close to impossible."* The course-form restatement of
   `tooling-agentic-cli.md` finding 9 ("permission rules are enforced by Claude Code, not by the
   model").
2. **Anti-suppression is engineered, not assumed** (L8): *"an agent fixing code must not be able
   to weaken the check on that code"* — a hook blocks test-file edits during a fix; the failing
   test is committed *before* the fix and the agent may not edit it. The vendor prescribing the
   defense to the exact evasion secunet measured (`pragma Assume` → `SPARK_Mode => Off`;
   `verification-gates.md` finding 5). Also: *"never skip or delete a failing test… If a test
   fails, fix the code, not the test."*
3. **Evals as live, decaying suites** (L9): *"cases that once discriminated stop doing so, and
   new ones must be added"*; configuration changes to CLAUDE.md/skills/hooks get "the regression
   testing that code gets", gated on pass rate; every production incident becomes a permanent
   eval. The prescription for precisely the decay `verification-infrastructure.md` found
   unattended in practice (Cline's silently lost workflow).
4. **The reviewer cannot gate, by design** (L10): *"Findings do not approve or block a PR on
   their own, and branch protection still requires approval from a code owner"*; a platform
   engineer who wants to gate on findings must build it from the check run's *"machine-readable
   tally"*. Course-form confirmation of `verification-gates.md` finding 1 (the always-neutral
   check), including the build-the-gate-yourself instruction.
5. **Self-approval forbidden** (L10): *"the agent that wrote the code has no way to approve it"* —
   the near-universal withholding `practitioner-exemplars.md` recorded.
6. **Deterministic/probabilistic split** (L13): *"detection stays entirely deterministic, with no
   model involved"* — the Spotify boundary, restated as design guidance.
7. **The pre-authorisation shape** (L12/L13): at 3σ the agent may act *"only by opening a PR into
   the review gate or triggering a pre-approved runbook"*; rollback is *"a single command…
   exercised regularly in staging"*, proven in advance. A human authorises the path; execution is
   unattended — the exact far-end mechanism shape `tooling-landscape.md` found everywhere.
8. **Reviewer attention as the throughput ceiling** (L7): *"The practical ceiling is how many
   streams one person can review properly."*

## 4. What is genuinely new to the corpus

1. **The managed-settings control inventory as a deployable ceiling artifact** (L11). A complete,
   MDM-deployed managed configuration where *"Engineers cannot edit or override any of the
   settings"*: `disableBypassPermissionsMode` + `allowManagedPermissionRulesOnly` (no engineer,
   project file, or flag can widen the rules), sandbox as a *precondition* (`failIfUnavailable`,
   `allowUnsandboxedCommands: false` — refuses to start unsandboxed, no retry outside), a
   `credentials` block denying `~/.ssh` / `~/.aws` reads and stripping named env vars from
   sandboxed commands, `allowManagedHooksOnly` (only managed hooks run — closing the
   hook-tamper vector), `disableSideloadFlags` + `strictKnownMarketplaces` (supply-chain
   allowlist for skills/agents/hooks/MCP), `allowManagedMcpServersOnly`, and
   `requiredMinimumVersion`. The corpus had found five administrator-pinnable constraints
   scattered across eleven CLIs; this is the vendor assembling them into one enforced enterprise
   posture — **the ceiling as a single reviewable file**.
2. **The committed-artifact provenance chain** (L1–L4): intent.md → spec.md → plan.md → diff and
   tests → PR with findings → incident record, each committed with author and timestamp — *"The
   chain of commits is also the audit trail: who asked for what, what the agent produced, and who
   approved it."* This is a **repository-hosted** provenance answer, notable against
   `governance-provenance-audit.md`'s finding that surviving attribution is platform-hosted; it
   answers "who asked for it" where the corpus's question was "which lines did a human write."
3. **Tiered response bands wiring a verification signal to an autonomy tier** (L13):
   1σ log / 2σ diagnose read-only (tool-scoped) / 3σ propose via PR or pre-approved runbook, in
   version-controlled config. The corpus found exactly one artifact tying a verification floor to
   an autonomy level; this is a second, and it is the closest published thing to the "missing
   wire" — though it keys tiers to a *production signal*, still not to authorship.
4. **Eval-per-incident** as a standing rule (L9/L13), and **legacy-system source-of-truth
   patterns** (L4: repo-as-truth / legacy-as-truth / linkage-as-minimum) for regulated
   coexistence.
5. **Claude Tag as on-call first responder** (L13) — incident response entering the loop through
   chat channels under the agent's own identity.

## 5. Tensions with the corpus — cite in both directions

1. **Hooks as approval gates vs. the server-side-gate test.** L11 makes hooks the release gates;
   `verification-gates.md`'s test says gates belong in CI and branch protection, *outside the
   agent's reach*, and Anthropic's own docs record harness-side stops as overridable by the
   harness. The playbook partially answers itself — `allowManagedHooksOnly` closes local
   tampering, and L12 re-grounds the real boundary in branch protection — but a hook remains an
   agent-side control, and any page citing L11 should carry the distinction.
2. **The shifts-table rhetoric outruns the plays' controls.** L1's table promises *"human review
   reserved for regulated and critical code"* — a Committer-shaped claim — while the plays
   themselves keep code-owner approval on every PR (L10). Cite the plays, not the table.
3. **Auto mode as the default for routine work** (L4) sits against the corpus's
   classifier-is-not-a-boundary findings (adaptive attacks >90%; a published attack on the
   auto-mode classifier) — and alongside the vendor's own telemetry that automated checking
   catches 13.6%-vs-89% more dangerous commands than human prompt review. Both halves are the
   same vendor; state both.
4. **Expectations, not measurements.** Every quantified improvement is an expectation (*"fall
   from a multi-week elicitation and refinement cycle to hours"*) or a metric definition. No
   play reports a value. Nothing in this file may be cited as an outcome.

## 6. Citation key

Cite as: *AI-Native SDLC Playbook, Anthropic Academy, L\<n\> "\<heading\>", retrieved 2026-09-02*
(tier: **vendor**). Lessons: L1 Introduction · L2 Capture as intent.md · L3 Requirements and
design · L4 Plan mode as the default start (subsections: Claude Code in auto mode; Legacy systems
and the source of truth) · L5 The CLAUDE.md · L6 Skills as institutional knowledge (subsection:
Hooks as build-time guardrails) · L7 Parallel sessions and subagents · L8 Give Claude a feedback
loop · L9 Continuous evals in CI · L10 AI in the PR review loop · L11 Hooks as approval gates
(subsection: Managed settings for a regulated enterprise) · L12 CI/CD integration and
deployment · L13 Closing the loop on metrics (subsection: Claude on call with Claude Tag) ·
L14 Closing thoughts and resources.
