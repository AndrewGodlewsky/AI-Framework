# Tooling Landscape

**Research date:** 2026-08-30
**Ticket:** [Tooling Landscape](https://github.com/AndrewGodlewsky/AI-Framework/issues/6)
**Question:** What tools occupy each region of the spectrum, and what can each one actually do?

**Purpose.** This ticket supplies the tooling substrate for every archetype document, and it is the
last open blocker on [Archetype Taxonomy](https://github.com/AndrewGodlewsky/AI-Framework/issues/8).
The ticket asked for six categories to be mapped as six regions of the spectrum. **They are not six
regions**, and establishing what they actually are is this document's main result.

**Method.** Six parallel research strands against primary sources: official documentation read as raw
Markdown where the vendor serves it, source code read directly from repositories, settings schemas,
CVE advisories with reproduction steps, GitHub's REST API, and first-party engineering blogs. Vendor
marketing pages were excluded as capability evidence and labelled where they were the only source.
Every capability claim carries an "as of" date, because the ticket correctly predicted this is the
fastest-ageing material in the project — see [§ Ageing](#ageing-this-document-began-expiring-during-the-session).

**Detail lives in the six companion files.** This document is the synthesis and the verdict.

| Strand | File |
|---|---|
| Inline completion, in-editor chat and edit | [`tooling-inline-and-chat.md`](./tooling-inline-and-chat.md) |
| Agentic IDE modes | [`tooling-agentic-ide.md`](./tooling-agentic-ide.md) |
| Agentic CLIs | [`tooling-agentic-cli.md`](./tooling-agentic-cli.md) |
| Background and cloud agents | [`tooling-background-agents.md`](./tooling-background-agents.md) |
| Multi-agent orchestration | [`tooling-orchestration.md`](./tooling-orchestration.md) |
| OpenClaw, the far-end anchor | [`tooling-openclaw.md`](./tooling-openclaw.md) |

---

## The verdict: three boundaries, and only one of them is a tool boundary

The six categories in the ticket describe a **product taxonomy**. The spectrum this project is
charting has a different shape, and the tooling evidence resolves it into exactly three boundaries.

### Boundary 1 — propose vs. act. Architectural, real, and one keypress wide.

The only place in the entire survey where a tool *structurally* cannot do the next thing. Across
fourteen completion products, not one documents an engine that executes a command, writes to a file
the developer is not editing, or makes any outbound call beyond the inference request. There is no
tool surface to grant.

The crossing point is not a product but a control: VS Code's terminal inline chat offers **Run
(⌘Enter)**. Everything before it proposes text; everything after it can act.

**This is the one boundary a team gets for free.** It holds without configuration, policy, or
discipline.

### Boundary 2 — approval. Configurable everywhere. No product refuses to let you cross it.

Every product examined past Boundary 1 ships a named mode that removes approval entirely:

> VS Code *Bypass Approvals* / *Autopilot* · Cursor *Run Everything* · Windsurf/Devin *Turbo* ·
> JetBrains Junie *Brave Mode* · Cline and Kilo *YOLO* · Zed `tool_permissions.default: "allow"` ·
> and across eleven CLIs: `--dangerously-skip-permissions`,
> `--dangerously-bypass-approvals-and-sandbox`, `--approval-mode yolo`, `--yolo`, `--yes-always`,
> `--auto`, `-a/--trust-all-tools`, `--skip-permissions-unsafe`, `amp.dangerouslyAllowAll`, `/mode auto`

**There is no product in this survey that structurally refuses to hand over the last approval.**
Three CLIs ship with it already gone — Amp (*"By default, Amp does not ask for approval before
running tools"*), opencode (*"allows all operations without requiring explicit approval"*), and Goose
(its own docs warn *"`Autonomous Mode` is applied by default"*).

Consequently: **"the human approves each change" is a configuration, not a property of a category.**
An archetype cannot be defined by naming a product. It must name the settings that hold the position
in place — and name who can change them.

### Boundary 3 — merge. Platform-enforced, and the only boundary the tools consistently respect.

**No product in this survey merges its own pull request on its own judgement.** The merge action is
absent from the agent's tool surface, structurally forbidden by the platform, or present only as a
button a human presses.

GitHub forbids its own agent in writing, at four separate points ([docs.github.com, *Risks and
mitigations for GitHub Copilot cloud agent*](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations),
retrieved 2026-08-30):

> "Copilot cloud agent cannot mark its pull requests as 'Ready for review' and cannot approve or merge a pull request."
>
> "Draft pull requests created by Copilot cloud agent must be reviewed and merged by a human."
>
> "Prevents the user who asked Copilot cloud agent to create a pull request from approving it."
>
> "When Copilot cloud agent opens a pull request under its own app identity, one more approval is required before it can be merged, as long as the repository already requires at least one approval."

Four distinct mechanisms — the agent cannot call merge; cannot mark its own PR ready; the *requester*
is disqualified from approving; and the app identity **adds** a required approval rather than
satisfying one. The platform hosting nearly all of the observable agent-PR population has engineered
the far end out of its own product.

**So the headline result of this ticket is this:** the far-end archetype is not something a tool
delivers. **Every real far-end mechanism found has the same shape — not an agent that merges, but a
human who pre-authorises a merge that then happens without them.** Devin's auto-merge dropdown,
GitHub's native auto-merge behind Cursor's approval, ClawSweeper's per-PR `/clawsweeper automerge`
comment. The decision is human and prior; only the execution is unattended.

The far end of this spectrum is reached by **a repository administrator changing a policy**, not by
buying a tool. That is a governance act, which routes it to
[Governance, Legal & IP by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/7).

---

## Headline findings

1. **Inline completion permits no autonomy at all — verified across fourteen products, not assumed.**
   The architecture forecloses it. *(Vendor documentation, fourteen products, read 2026-08-30.)*

2. **Edit acceptance has an off switch; completion acceptance does not.** VS Code ships
   `chat.editing.autoAcceptDelay` — *"a delay after which suggested edits are automatically
   accepted"*, default `0`. The moment a team moves from completion to in-editor edit, diff review
   becomes a countdown timer. *(VS Code AI settings reference, dated 2026-08-26.)*

3. **The command allowlist is not a security boundary, and there is a five-product CVE record proving
   it.** Zed shipped three bypasses on one day — environment-variable prefixing (CVE-2026-44463),
   arithmetic expansion (CVE-2026-44466), `${var@P}` chaining (CVE-2026-44462), all 2026-05-08.
   Also Cursor CVE-2026-22708; Roo CVE-2025-57771 and CVE-2025-58370 (Roo shipped `npm install` as a
   *default* allow); VS Code CVE-2026-45482. **Every product that built a regex allowlist over a shell
   had it defeated by shell syntax.** VS Code concedes it in its own source: the defaults *"do not aim
   to provide exhaustive coverage… as that is simply not feasible."* Cursor's wording: allowlists are
   *"best-effort convenience. They are not a security guarantee."*
   *(Vendor security advisories with reproduction steps.)*

4. **The hard floor is vanishingly small, and where it is real it belongs to your employer.** Zed's
   entire un-overridable protection is five regexes matching `rm` against `/`, `~`, `$HOME`, `.`,
   `..`. Junie's Brave Mode explicitly overrides `.aiignore`. Cline's floor for an individual is
   nothing. The floors that do exist are enterprise policies — `ChatToolsAutoApprove`,
   `"yoloModeAllowed": false`, Claude Code managed settings, `security.disableYoloMode`. **Only five
   administrator-pinnable constraints were found across eleven CLIs.**

5. **Checkpoints restore less than developers believe, in documented ways.** Zed's restore runs
   `git restore --worktree` with `git clean` deliberately disabled — **agent-created files survive
   "Restore Checkpoint"** — and excludes files over 2 MB plus `*.db`, `*.sqlite` and images. Kilo
   excludes `.gitignore`d files (so `.env`, `dist/`) and garbage-collects snapshots after seven days.
   **No checkpoint in any product restores terminal side effects, database state, or network calls.**

6. **Headless operation is universal and therefore no longer discriminates.** All eleven CLIs ship a
   documented non-interactive entry point. **What discriminates is what happens to an unapproved
   action when nobody is present, and there are four incompatible answers**: deny at call time
   (Gemini `ask_user`→deny, Claude Code `dontAsk`); remove the capability up front (Continue excludes
   `ask` tools in headless); stop with a non-zero exit and *"performs no partial changes"* (Droid
   exec — the only atomicity promise in the set); or **silently skip and keep working** (Claude Code
   auto mode under `-p` without `--permission-prompt-tool`). The last exits 0 having quietly not done
   part of the job — which makes a green CI run uninterpretable unless a team knows which of the four
   it bought.

7. **Containment thins as delegation increases — the opposite of what the spine demands.** Eight of
   eleven CLIs run with the invoking user's full privileges in the real working tree with no OS-level
   containment (Aider, opencode, Amp, Crush, Goose, Amazon Q CLI, Continue, Droid). Cline, Kilo and
   Junie ship no sandbox. **Exactly one tool inverts this**: Codex CLI makes the sandbox the substrate
   and approval the escalation path out of it (`SandboxMode` serde default `ReadOnly`) — **but
   `WindowsSandboxLevel` derives `#[default] Disabled`, so on Windows Codex runs unsandboxed.**
   VS Code's sandbox is off by default, macOS/Linux/WSL2 only; Cursor documents no Windows support.

8. **The default oversight mechanism is becoming a second model, not a human.** Claude Code's
   built-in starting mode on Pro/Max/Team in a terminal is now `auto`, in which *"a separate
   classifier model reviews actions before they run"* (v2.1.228+). `-p`, the SDK, Enterprise and
   Bedrock/Vertex/Foundry still start Manual. The vendor's own framing of why is the 93%→97%
   permission-prompt approval figure — see finding 9.

9. **The interface shape, not the human, determines whether review happens.** Anthropic reports
   permission-prompt approval at **93%** (engineering, 2026-03-25) and **97%** (blog, ~2026-08-08) —
   and *the same population rejecting 39% of proposed plans*. Same humans, same product, two
   interfaces, opposite behaviour. *(Vendor-reported; the vendor sells the replacement for the
   prompt. Neither figure carries a denominator or a time series.)* This sharpens the project's
   existing **human oversight** ruling: the mechanism does not imply the outcome, and the variable is
   the interface.

10. **Multi-agent orchestration is not a region of this spectrum.** No first-party engineering
    write-up was found in which a general-purpose multi-agent framework writes and ships application
    software. The largest published production software-engineering AI system is **deliberately not
    multi-agent** — Uber's uReview handles *">90%"* of ~65,000 weekly diffs with in-house prompt
    chaining and no framework ([Uber, 2025-08-12](https://www.uber.com/us/en/blog/ureview/),
    vendor-reported). The one independent measurement is negative: **41%–86.7% failure rates** across
    seven open-source multi-agent systems, gains *"often minimal compared to single-agent frameworks
    or simple baselines like best-of-N sampling"* ([arXiv:2503.13657](https://arxiv.org/abs/2503.13657),
    v3 2025-10-26, 1,600+ annotated traces). **Both leading vendors have published against it for
    coding** — Cognition's *"Don't Build Multi-Agents"* (2025-06-12) and Anthropic's *"Most coding
    tasks involve fewer truly parallelizable tasks than research"* (2025-06-13). Anthropic now
    actively suppresses it: on Opus 5 with the `claude_code` preset, the system prompt tells the model
    *not to call the Agent tool unless asked*.

11. **The 2026 convergence is toward flow engineering, and it vindicates ADR-0001.** Devin and Claude
    Code independently shipped orchestration-as-deterministic-script — Devin: *"a deterministic Python
    script that orchestrates a team of Devin agents"*; Claude Code: *"A script the runtime executes"*,
    with the decision of what runs next belonging to *"The script"*. Both **ban non-determinism in the
    orchestration layer**: `Date.now()`, `Math.random()` and no-argument `new Date()` throw. Microsoft
    says the quiet part in its own agent framework's overview: *"If you can write a function to handle
    the task, do that instead of using an AI agent."* The term this project kept on linguistic grounds
    names the field's actual direction of travel.

12. **⚠️ No tool in the survey couples permission to work state.** Every permission rule in every tool
    matches the *shape* of a call — tool, command, path, domain, parameter. **Nothing can express
    "allow `git push` only if the tests passed."** This is the single missing primitive that would let
    a team engineer the map's spine, and it does not exist in any of the eleven CLIs, six IDE
    products, or eight background agents examined. See [§ The missing wire](#the-missing-wire).

---

## Part A — The six categories, as the ticket asked

Each category is given the ticket's three questions: what it changes about a developer's process,
what autonomy it *structurally* permits, and what it cannot do.

### A.1 Inline completion

**Changes:** the developer stops typing tokens they can predict. Nothing else.

**Structurally permits:** no autonomy. No tool surface exists.

**Cannot:** execute, write outside the open buffer, or reach the network beyond inference.

**Note the category description is already stale.** GitHub's Next Edit Suggestions predicts *"both the
location of the next edit you'll want to make and what that edit should be"*, is on by default, and
ships `editor.inlineSuggest.edits.allowCodeShifting` defaulting to `"always"`. Cursor Tab *"predicts
cross-file edits."* Completion now moves the cursor, shifts surrounding code and points across files
— and still cannot commit any of it without a keypress. **"Text at the cursor" is the wrong mental
model; "cannot act without a keypress" is the durable one.**

**Representatives (read 2026-08-30):** GitHub Copilot, Cursor Tab, JetBrains AI Assistant + Full Line,
Tabnine, Zed Zeta, Amazon Q inline, Continue.dev. **Consolidation has removed two and dated a third:**
Codeium→Windsurf→acquired by Cognition [2025-07-14](https://cognition.com/blog/windsurf) (docs now
307 to `docs.devin.ai`); Supermaven→Cursor [2024-11-12](https://supermaven.com/blog/cursor-announcement);
Amazon Q Developer IDE plugins discontinued **2027-04-30**.

**Unique to this region:** it is the only place a team can eliminate the egress question outright.
JetBrains Full Line *"runs entirely on your local device without sending any code over the internet"*;
Tabnine documents a *"completely air-gapped"* deployment.

### A.2 In-editor chat and edit

**Changes:** the developer stops writing the first draft, and starts reading diffs.

**Structurally permits:** as much as the accept control allows — and that control has a timer
(`chat.editing.autoAcceptDelay`).

**Cannot:** survive the editor closing; act without a session.

**The containment gap that matters:** Copilot content exclusion — the one file-scope mechanism GitHub
ships — *"is currently not supported in Edit and Agent modes of Copilot Chat."* It also does not apply
to symlinks or remote filesystems, and *"Copilot may use semantic information from an excluded file if
the information is provided by the IDE indirectly."* A team whose answer to "what can the AI see" is
content exclusion has an answer that covers only the least-delegated surface.

**The read-only mode is now a standard primitive**, enforced by tool scoping rather than instruction:
Cline Plan, Continue Plan, Cursor Ask, VS Code read-only custom agents. **This is the shape an
archetype should specify** — a tool scope, not a trust posture.

### A.3 Agentic IDE modes

**Changes:** the developer stops approving diffs and starts approving *actions* — then, with
auto-approve, stops approving at all and starts supervising a session.

**Structurally permits:** everything the developer's own shell permits. Cline, Kilo and Junie ship no
sandbox; the agent runs with full user privileges.

**Cannot:** run without a human present, or open a PR in most cases. This is what separates it from
A.5.

**The most honest threat model in the category is Zed's**, and it is an admission of defeat at the
workspace boundary: sandboxing covers only Zed Agent's `terminal` and `fetch` tools — not external
agents, language servers, the git client, extensions, or ordinary terminal tabs — and the docs name
three escapes it cannot close (a malicious Rust proc macro run by `rust-analyzer` *"outside the
sandbox"*, an injected `Makefile`, and a submodule whose `core.fsmonitor` runs on every prompt render).

**⚠️ The category is dissolving.** Roo Code's repository was **archived 2026-05-15**, the team pivoting
to a cloud agent whose README opens *"No IDE plugin. No terminal session. No babysitting."* Windsurf
is now Devin Desktop. The convergence is toward **ACP** (Zed's Agent Client Protocol, v1.7.0
2026-08-20) and **VS Code's Agent Host Protocol**, in which the editor hosts a *foreign* agent that
calls `session/request_permission` on the editor. **The editor renders the prompt; the agent decides
what to ask about.** Zed states plainly that its sandbox *"does not sandbox … External Agents."* This
relocates the permission decision out of the tool the developer configured, and it means "agentic IDE
mode" is not a stable unit to build an archetype on.

### A.4 Agentic CLIs

**Changes:** the agent leaves the editor, gains the full shell, and becomes **scriptable**. This is
the step that makes unattended operation possible at all.

**Structurally permits:** anything the shell permits, in every tool. All eleven ship an off switch.

**Cannot:** nothing structural. Every ceiling here is a product decision.

**Two findings a reference document must carry.** First, permission rules are enforced by the agent
harness, not the model, and one vendor states it plainly: *"Permission rules are enforced by Claude
Code, not by the model. Instructions in your prompt or `CLAUDE.md` shape what Claude tries to do, but
they don't change what Claude Code allows."* **An instruction file is not a permission control** —
the sentence this project most needs. Second, the hook interface has converged across four
independent vendors — Claude Code, Codex CLI, Gemini CLI, Amazon Q CLI — on the same event vocabulary
(`PreToolUse`/`PostToolUse`/`SessionStart`/`SessionEnd`/`UserPromptSubmit`), the same transport (JSON
on stdin/stdout) and the same blocking convention (**exit code 2 blocks; stderr becomes the
reason**). It is a de facto interface with none of AGENTS.md's open governance.

**Egress:** three tools can restrict it; two are honest that they cannot inspect TLS. Anthropic names
the consequence — *"code running inside the sandbox can potentially use domain fronting or similar
techniques to reach hosts outside the allowlist."* **The other eight tools' agents have your whole
network.**

### A.5 Background and cloud agents

**Changes:** the human stops operating and starts reviewing a finished PR.

**Structurally permits:** opening a PR, and no further — see Boundary 3.

**Cannot:** merge on its own judgement, anywhere in the survey.

**⚠️ The exception that proves the boundary is a policy, not a law.** Cursor documents the opposite
posture: *"If you enable approvals, the agent can also approve, request changes, and dismiss
reviews."* Cursor's cloud agents act as a **GitHub App**, and an App's `APPROVE` review *does* count
toward required approvals. An organisation that enables this creates a documented path by which a
required human approval is satisfied by an agent, and existing approvals can be **dismissed** by one.
Cursor's docs carry no warning on that sentence and do not say who may enable it. Factory approves by
default on clean reviews; CodeRabbit ships `request_changes_workflow`; PR-Agent has
`create_review(event="APPROVE")` in source, opt-in and undocumented in its user docs.

**The only bot documented to merge its own PR is Renovate — which is deterministic, not an agent.**
That contrast is itself the finding: merge authority currently sits with the class of bot whose output
CI can fully check.

**Outcomes are barely measured, confirming ticket #3.** GitHub ships a merge-rate metric API and
publishes no aggregate. Cursor publishes nothing. The only cross-vendor figures are observational and
academic (AIDev: Codex 64% / Devin 49% / Copilot 35%). The best public case is Microsoft's
`dotnet/runtime` — 67.9% merged, 16.5 vs 12.4 review comments — and its conclusion is *"the bottleneck
has moved."*

### A.6 Multi-agent orchestration

**Not a region of this spectrum.** See headline finding 10. It is a **build-versus-buy axis that
crosses the spectrum**: a team here has taken on maintaining an agent harness alongside its product.

**Durability is the property that separates a demo from unattended operation, and almost nothing has
it.** Only Temporal makes an unconditional crash guarantee (*"the Worker uses the Event History to
replay the code and recreate the state… as if the failure never occurred"*). LangGraph re-runs the
whole node on resume — *"it does not resume from the exact line"*, so side effects *"should (ideally)
be idempotent"*. The OpenAI Agents SDK persists **conversation history only** — no execution state, no
crash recovery.

**Cost, vendor-reported:** ~15× chat (≈3.75× a single agent) for Anthropic's research system; **~7×**
for Claude Code agent teams. **No framework author publishes any cost figure at all** — an emptiness
finding. And the vendor's own headline multi-agent result (+90.2%) was measured on an internal
*research* evaluation, not a coding task.

**Conflict handling in the most-documented in-tool peer system is task partitioning by a human:**
*"Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a
different set of files."* No merge, no lock, no conflict detection. That system is experimental and
disabled by default.

---

## Part B — OpenClaw, and the far-end anchor

**The ticket asked whether anyone uses OpenClaw, or anything like it, to push code to production
without human verification. The answer is no, and it is settled mechanically rather than by absence
of evidence.**

The project's own FAQ: *"OpenClaw is an assistant and coordination layer, not an IDE replacement. Use
Claude Code or Codex for the fastest direct coding loop inside a repo."*

- **Its only repository-write tool creates a *draft* PR, and `draft: true` is a hardcoded literal**
  with no parameter to flip (`github-publication-executor.ts:529`). There is **no merge, deploy,
  release or CI-trigger tool anywhere** in `src/agents/tools/`.
- **The ecosystem is not a delivery ecosystem.** Across **1,198 ClawHub skills** enumerated
  2026-08-30, "pull request" appears in 2, "github action" in 1, "terraform" in 1. Top topics are
  Health, Home, Smart Home, finance.
- **Even the adversarial lab study built to make it act autonomously found it did not.** *Agents of
  Chaos* (arXiv:2602.20021v1, 2026-02-23) gave six OpenClaw agents unrestricted shell including
  `sudo` and reports: *"The majority of agent actions during our experiments were initiated by human
  intervention, and most high-level direction was provided by humans."*

**What OpenClaw does anchor is containment, and it anchors it as a warning.** Default posture is
`agents.defaults.sandbox.mode: off`, with the docs stating *"No-approval host exec is the default for
gateway and node (`mode=full`)"* — the **lethal trifecta** with containment switched off by default,
across **30,000+ internet-exposed instances** (Bitsight, 27 Jan–8 Feb 2026), including healthcare and
finance, against **647 published advisories, 14 critical**.

**Recommendation to the map: keep OpenClaw, move its role.** It anchors a real extreme — maximum
delegation of a person's digital life on the widest untrusted surface with the weakest defaults — but
not a *delivery* extreme. The delivery-end anchor already exists in this project's own corpus:
**Meta's RADAR** (331k+ diffs, no human reviewer), recorded in
[`verification-gates.md`](./verification-gates.md) by ticket #5.

**A useful reachable midpoint** for the taxonomy, also from this strand: ClawSweeper's automerge lane
— a maintainer types `/clawsweeper automerge` per PR, and merges pin to a reviewed head SHA behind CI.
The project's own docs are explicit that the bot is not the gate: *"A positive ClawSweeper result is
supporting evidence, not maintainer approval."*

---

## The missing wire

Ticket #5 concluded that the provenance layer and the delivery layer have never been connected. This
ticket finds the same disconnection one level down, at the permission layer:

**Every permission rule in every tool matches the shape of a call — tool, command, path, domain,
parameter. None matches the state of the work.** No tool can express:

> allow `git push` only if the test suite passed
>
> allow `Write` to `src/` only while coverage is above the floor
>
> deny everything after the third consecutive failed build

This is the primitive an archetype further along the spectrum would need in order to replace human
approval with engineered verification *at the point of action* rather than after it. Two independent
strands, examining different layers, found the same wire missing. **That convergence is the
strongest structural finding this ticket produces**, and it is what the archetype documents should
say the field has not yet built.

---

## Corrections to prior tickets

### ⚠️ Ticket #5's headline finding 1 needs narrowing — a counterexample exists

[Verification Infrastructure by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/5)
concluded: *"No published mechanism anywhere gates, canaries, or auto-reverts a change because it was
agent-authored."*

**`agent-approval-check` is a counterexample, and it was verified directly against the repository for
this ticket** (not merely reported): PR #1429 *"Add agent-approval-check composite action"*, **merged
2026-06-30T21:09:58Z**, shipping as a directory at the root of `anthropics/claude-code-action`. Its
README, read 2026-08-30:

> "Require **N human approvals** on any pull request that contains commits authored by an AI agent
> (Claude, Claude Code, or any bot identity you configure). PRs without agent activity are unaffected."
>
> "This is the same gate Anthropic runs internally on every agent-authored PR."
>
> "Mark `agent-approval-check` as a **required status check** on your protected branches and GitHub
> will refuse to merge until it's green."

It scans commits, author and reviews for configured agent identities, counts distinct human approvals
(write-access-verified per user via the collaborators API), and posts a `success`/`pending` commit
status. Default `required_approvals: 2`; fail-closed.

**The correction is a narrowing, not a reversal, and the direction matters:** a mechanism *does* now
gate on agent authorship — but it wires provenance to **more human reading**, not to more engineered
verification. That is the inverse of the direction the map's spine argues for. The honest amended
form: *provenance-gated delivery now exists in exactly one published mechanism, and it responds to
agent authorship by demanding more human review rather than more automated checking.*

**Two negative findings sharpen it.** First, **`anthropics/claude-code-action` does not run this
workflow on itself** — verified 2026-08-30 by listing `.github/workflows` (13 workflows, none uses it;
code search scoped to `path:.github` returns 0). Second, its stablemate cannot gate at all: Anthropic
Code Review's *"check run always completes with a neutral conclusion so it never blocks merging
through branch protection rules"* — and GitHub counts neutral as passing (*"Required status checks
must have a successful, skipped, or neutral status"*). **Anthropic ships one mechanism that can be a
required check and one that is designed never to be.**

### ⚠️ A premise this ticket's own brief carried was wrong

This ticket briefed its background-agents strand with the claim that GitHub Actions' `GITHUB_TOKEN`
*cannot* approve a PR. **That is not what GitHub's documentation says.** It is a **policy setting, off
by default** — *"Allow GitHub Actions to create and approve pull requests"*, REST field
`can_approve_pull_request_reviews`, introduced
[2022-01-14](https://github.blog/changelog/2022-01-14-github-actions-prevent-github-actions-from-approving-pull-requests/)
explicitly *"to protect against a user using Actions to satisfy the 'Required approvals' branch
protection requirement"*, with GitHub's own note that *"Enabling this can be a security risk."*
It is a switch an admin can flip, not a wall. The adjacent claim **is** verified verbatim: *"Pull
request authors cannot approve their own pull requests."*

**This matters beyond the correction:** it is a third instance of the pattern this ticket keeps
finding — the constraint that appears to hold the far end shut is an administrator-flippable default.

### Proposed Notes rewording for the map

> **Far-end anchor.** OpenClaw anchors **containment and the lethal trifecta**, not delivery: its only
> repository-write tool opens a *draft* PR by hardcoded literal, and it ships no merge, deploy or
> release tool at all. The delivery-end anchor is **Meta's RADAR** (331k+ diffs, no human reviewer),
> already in [`verification-gates.md`](./verification-gates.md).

### Confirmations of prior findings

- **Ticket #4's "position is a per-change property, not a per-team property"** is reinforced and
  refined: this ticket finds position is set by **configuration and administrator policy**, which
  *can* be a per-team property — if the team pins it. The five administrator-pinnable constraints
  found across eleven CLIs are the entire mechanism by which an archetype can be made to hold.
- **Ticket #2's ruling on human oversight** is strengthened by the 39%-plan-rejection contrast: the
  variable is the interface, not the human.
- **ADR-0001's retention of *flow engineering*** is vindicated by the 2026 convergence (finding 11).

---

## What this constrains downstream

**For [Archetype Taxonomy](https://github.com/AndrewGodlewsky/AI-Framework/issues/8), which this
ticket unblocks:**

1. **Do not build archetypes on product categories.** Several dissolved during this research — Roo
   archived, Windsurf became Devin Desktop, ACP relocated the permission decision out of the editor.
   Build them on the three boundaries, which are durable.
2. **An archetype must name its settings and its enforcement scope**, because every position past
   Boundary 1 is a configuration. "Which product" is not a distinguishing question; "who can change
   the setting, and can they be stopped" is.
3. **The far end must be described as pre-authorised unattended execution**, not as an agent that
   decides to ship. No product in the survey supports the latter description.
4. **Multi-agent orchestration is an axis, not an archetype.** Placing it as the furthest region
   would state something the evidence contradicts.
5. **The containment inversion is real and should be stated as a demand the field has not met.**
   Delegation increases while containment thins; one tool of eleven inverts it.

---

## Method, limits and disclosures

### Ageing: this document began expiring during the session

The ticket predicted this is the fastest-ageing material in the project. It aged *while being
written*: Windsurf's docs 307 to `docs.devin.ai` mid-strand, Supercomplete is gone from the successor
docs, VS Code has abandoned the ask/edit/agent frame the ticket itself used, and
`docs.claude.com/en/docs/claude-code/*` now 301s to `code.claude.com/docs/en/*` — making every
suggested doc URL in the brief stale. **Claude Code doc pages carry no publication or last-updated
date**; the only timestamp served is a JSON-LD `dateModified` equal to the fetch moment, so those
claims are dated *accessed 2026-08-30* and no more precisely.

**Consequence for the archetype documents: anchor prose on the boundaries and the mechanisms, not on
product mode names.** Every product name in these documents should be readable as an example that may
have been renamed, acquired or archived since.

### ⚠️ Prompt-injection-shaped content encountered in a fetched source

One strand reported that a fetched AWS documentation page rendered with an **appended
instruction-shaped CLI block**. The agent did not act on it and could not establish its provenance.
It is recorded here rather than discarded because a research corpus assembled by fetching vendor pages
is precisely the exposure surface this project's **lethal trifecta** term describes — the method used
to write these documents has the same shape as the risk they document. Separately, the harness
flagged instruction-shaped patterns in one subagent's returned output; that content was treated as
data and its load-bearing claim (`agent-approval-check`) was independently re-verified against the
repository before being used here.

### Items routed to Verify Blocked-Source Quotes (#11)

- **Cisco Outshift CAIPE/JARVIS figures** ("automated around a third of its internal platform
  engineering tasks"; incident response "hours to seconds") came from a **search-result summary**
  because both Outshift blog bodies failed to render. Used in the orchestration strand only with that
  qualification attached, and flagged for verification.

### Blocked or unavailable sources

**No security control, paywall, auth wall or rate limit was circumvented.** Across the six strands the
failures were: one HTTP 429 (Windsurf rename post); roughly fifteen 404s from documentation
reorganisation; several SPA-shell responses served at HTTP 200 (worked around by fetching the raw
Markdown a vendor publishes, which is a higher-trust source, not a circumvention); and four
Anthropic/GitHub doc paths retired or merged. Each strand file carries its own itemised table.

### Known gaps

- **OpenClaw's community talks on Discord**, which is unindexed and was not searched. The strand's
  usage findings rest on the repo, the skill registry and the issue tracker.
- **Whether Cursor's Browser / File-Deletion / External-File protections survive Run Everything** is
  not documented by the vendor.
- **No vendor publishes a merge rate for its background agent.** GitHub ships the metric API and
  publishes no aggregate; Cursor publishes nothing. This is a genuine emptiness finding, consistent
  with ticket #3.
