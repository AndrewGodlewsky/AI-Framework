# Tooling Landscape: Agentic CLIs

**Research date:** 2026-08-30
**Ticket:** [#6 Tooling Landscape](https://github.com/AndrewGodlewsky/AI-Framework/issues/6)
**Question:** In the region where the agent leaves the editor and gains the full shell, what does each
tool's permission model actually enforce, what does it actually contain, and what can it actually do
with no human present?

**Purpose.** Terminal-native coding agents are the structural step that makes unattended operation
possible at all. This strand establishes, per tool and from primary sources, the four properties that
decide how far along the spectrum a team using that tool can go: the **permission model**, the
**containment mechanism**, the **headless entry point**, and the **programmability** a team can
engineer around.

**Method.** Official documentation and — where the tool is open source — the repository itself:
permission-check code, sandbox implementation, CLI argument definitions, and serde defaults. Source
code beats a doc page and was preferred wherever both existed. Every claim below carries its source
and the date it was read. All web documentation was read 2026-08-30; all source was read at `main`
on 2026-08-30 unless a commit or version is named.

**Evidence tier is stated with each figure.** Where a vendor measures the thing it sells, the row says
so.

---

## Headline findings

1. **Headless operation is universal and therefore no longer discriminating.** All eleven tools
   examined ship a documented non-interactive entry point. The property that lets an agent be wired
   into CI, cron, a webhook or a queue is now table stakes. *(Primary artifact: eleven CLIs, 2026-08-30.)*
   **What discriminates is what happens to an unapproved action when nobody is there to approve it** —
   and the tools give four incompatible answers (finding 5).

2. **Eight of eleven tools run with the full privileges of the invoking user in the real working tree,
   with no OS-level containment of any kind.** Aider, opencode, Amp, Crush, Goose, Amazon Q Developer
   CLI, Continue CLI and Droid document no sandbox. *(Primary artifact: first-party docs and source,
   2026-08-30.)*

3. **Exactly one tool sandboxes by default, and only on two of three platforms.** OpenAI's Codex CLI
   makes the sandbox the substrate and approvals the escalation path out of it — the inverse of every
   other design. Its `SandboxMode` serde default is `ReadOnly`; its shipped preset labelled "Default"
   is `workspace-write` + `on-request` approval. But `WindowsSandboxLevel` derives `#[default]
   Disabled`, so **on Windows, Codex runs unsandboxed unless you turn a sandbox on.**
   *(Primary artifact: `codex-rs/protocol/src/config_types.rs`, `codex-rs/utils/approval-presets/src/lib.rs`.)*

4. **Claude Code's default is now a classifier, not a human.** On Pro, Max and Team plans, in a
   terminal or the VS Code extension, the built-in starting permission mode is `auto`, in which "a
   separate classifier model reviews actions before they run" rather than the user. Requires v2.1.228+
   (macOS/Linux/WSL) or v2.1.233+ (native Windows). `claude -p` and the Agent SDK still start in
   `default` (Manual) on every plan, as do Enterprise plans, Console API keys, and Bedrock/Vertex/
   Foundry sessions. *(Vendor documentation, [permission-modes](https://code.claude.com/docs/en/permission-modes), 2026-08-30.)*
   This is the single largest default-posture change in the set and it moves the oversight question
   from "did a human approve" to "did a second model approve".

5. **When no human is present, unapproved actions resolve four different ways — and only one tool
   guarantees no partial changes.**
   - *Deny at call time:* Gemini CLI ("In non-interactive mode, `ask_user` is treated as `deny`"),
     Claude Code `dontAsk`.
   - *Remove the capability up front:* Continue CLI ("In headless mode, `ask` tools are automatically
     excluded — there's no one to approve them").
   - *Stop the run, non-zero exit, no partial writes:* Droid exec ("returns a non-zero exit code, and
     performs no partial changes").
   - *Silently skip and keep working:* Claude Code auto mode under `-p` without `--permission-prompt-tool`
     — "the action doesn't run and Claude keeps working… Claude Code doesn't stop the run in either case."
   The last is the dangerous one for a CI gate: the run exits 0 having quietly not done part of the job.
   *(Vendor documentation for all four, 2026-08-30.)*

6. **Network egress control exists in three tools and is honest about its own limit in two.** Claude
   Code and Codex CLI both route sandboxed traffic through a proxy with a per-host allow/deny list.
   Both concede the same weakness: the proxy decides from the client-supplied hostname and does not
   terminate TLS by default. Anthropic names the consequence: "code running inside the sandbox can
   potentially use domain fronting or similar techniques to reach hosts outside the allowlist."
   Gemini CLI can only restrict egress via its `-proxied` Seatbelt profiles or a container you
   configure yourself. **The other eight tools' agents have your whole network.**
   *(Vendor documentation + `codex-rs/network-proxy/`, 2026-08-30.)*

7. **Three tools ship in a state where the agent runs shell commands in your working tree with no
   prompt and no sandbox.** Amp — "By default, Amp does not ask for approval before running tools."
   opencode — "By default, opencode allows all operations without requiring explicit approval." Goose —
   its own docs carry a warning admonition reading "`Autonomous Mode` is applied by default."
   *(First-party documentation, 2026-08-30.)*

8. **Every ceiling in the set is a product decision, not an architectural one.** All eleven ship a
   documented switch that removes approval entirely: `--dangerously-skip-permissions`,
   `--dangerously-bypass-approvals-and-sandbox` (alias `yolo`), `--approval-mode yolo`, `--yolo`,
   `--yes-always`, `--auto`, `-a/--trust-all-tools`, `--skip-permissions-unsafe`,
   `amp.dangerouslyAllowAll`, `/mode auto`. Only **five** administrator-pinnable constraints were found
   across the whole set that a developer cannot override locally (finding 12).

9. **Permission rules are enforced by the agent harness, not the model — and one vendor says so in
   plain text.** "Permission rules are enforced by Claude Code, not by the model. Instructions in your
   prompt or `CLAUDE.md` shape what Claude tries to do, but they don't change what Claude Code allows."
   No other tool in the set states this as clearly, and it is the sentence a reference document most
   needs: an instruction file is not a permission control. *(Vendor documentation, 2026-08-30.)*

10. **The hook interface has converged across four independent vendors with no specification and no
    governance body.** Claude Code, Codex CLI, Gemini CLI and Amazon Q Developer CLI all now ship
    lifecycle hooks with the same event vocabulary (`PreToolUse`/`PostToolUse`/`SessionStart`/
    `SessionEnd`/`UserPromptSubmit`), the same transport (JSON on stdin, JSON on stdout), and the same
    blocking convention (**exit code 2 blocks the action; stderr becomes the rejection reason**).
    Codex's `HookHandlerType` enum is `{Command, McpTool, Prompt, Agent}` — the same four handler
    kinds Claude Code offers minus `http`. This is a de facto interface with none of AGENTS.md's open
    governance. *(Primary artifact: `codex-rs/protocol/src/protocol.rs`; Claude Code, Gemini CLI and
    Q CLI hook docs, 2026-08-30.)*

11. **The vendor holding the telemetry reports permission-prompt approval at 93% and then 97%, five
    months apart.** "Claude Code users approve 93% of permission prompts" (Anthropic engineering,
    2026-03-25). "users approve 97% of permission prompts in Claude Code" (Anthropic blog, ~2026-08-08).
    The same August post reports the same population **rejecting 39% of proposed plans**, and a study
    with 1,053 paid participants in which "human review caught just 13.6% of dangerous commands, while
    auto mode caught 89%." *(Vendor-reported; the vendor sells the replacement for the prompt.)*
    Neither figure comes with a denominator or a time series. The 39% plan-rejection contrast is the
    load-bearing part: the same humans scrutinise a plan and rubber-stamp a prompt, so **the interface
    shape, not the human, determines whether review happens.**

12. **Five administrator-pinnable constraints exist across the entire set.** (a) Claude Code managed
    settings — "no other level, including command line arguments, can override a managed permission
    rule", plus `permissions.disableBypassPermissionsMode` and `permissions.disableAutoMode`.
    (b) Claude Code refuses `bypassPermissions` when running as root or under `sudo` on Linux and
    macOS, and refuses it under `--restricted`. (c) Gemini CLI's `security.disableYoloMode`, plus the
    structural rule that YOLO "can only be enabled via command line" and never from a settings file.
    (d) Codex's `requirements.toml` `allow_managed_hooks_only`, and `HookTrustStatus` requiring hooks
    to be trusted before they run. (e) Amazon Q's `allowedTools` deliberately refusing the `"*"`
    wildcard that its `tools` field accepts. Everything else in the set is advisory.
    *(Primary artifacts, 2026-08-30.)*

13. **Contrarian finding: Claude Code's auto mode silently discards the allowlist a team built.** On
    entering auto mode, "broad allow rules that grant arbitrary code execution are dropped" — blanket
    `Bash(*)`/`PowerShell(*)`, wildcarded interpreters like `Bash(python*)`, package-manager run
    commands, `Agent` rules, and `Monitor` rules. Narrow rules like `Bash(npm test)` survive. This is
    good design and it also means **the allowlist a team reviewed and checked into version control is
    not the allowlist in force** in the mode that is now the default. *(Vendor documentation, 2026-08-30.)*

14. **Negative finding: no tool in the set couples its permission model to a verification outcome.**
    Nothing lets a team express "allow `git push` only if this session's test suite passed."
    Every permission rule found matches on the *shape* of the call — tool name, command prefix, path,
    domain, parameter — never on the state of the work. A `PreToolUse` hook can approximate it by
    shelling out, but no tool ships the primitive. *(Emptiness finding across eleven tools, 2026-08-30.
    Consistent with the coupling gap already recorded in
    [`verification-infrastructure.md`](./verification-infrastructure.md).)*

15. **Aider's stance is the outlier and remains defensible.** `--auto-commits` defaults to `True` and
    `--dirty-commits` defaults to `True`: every agent edit lands as a reviewable, revertible commit,
    and pre-existing uncommitted work is committed first so the agent's diff is isolated. No other
    tool in the set makes version control the primary containment mechanism. What it gives up is
    everything else — no tool-call permission surface, no sandbox, no egress control, and a Python API
    its own docs describe as "not officially supported or documented".
    *(Vendor documentation, [aider.chat/docs/git.html](https://aider.chat/docs/git.html) and
    [config/options.html](https://aider.chat/docs/config/options.html), 2026-08-30.)*

16. **Governance movement worth watching: Goose has left its vendor.** `github.com/block/goose` now
    HTTP-301s to `aaif-goose/goose`. A vendor-owned agent CLI moving to a foundation-style
    organisation is the same pattern AGENTS.md and MCP followed. *(Primary artifact: GitHub API
    redirect observed 2026-08-30.)*

---

## The comparison table

Default posture, containment and headless capability across all eleven tools. **"Default posture" is
what happens on a fresh install with no configuration**, which is the only number that describes what
most teams actually run.

| Tool | Default permission posture (fresh install) | Sandbox mechanism | Sandboxed by default? | Network egress control | Headless entry point | Structured output | Remove-all-approval switch |
|---|---|---|---|---|---|---|---|
| **Claude Code** (Anthropic) | **`auto`** on Pro/Max/Team in terminal & VS Code — classifier reviews, not the human. `default` (Manual) for `-p`, Agent SDK, Enterprise, Console API keys, Bedrock/Vertex/Foundry | macOS **Seatbelt**; Linux/WSL2 **bubblewrap** + optional **seccomp** filter + `socat`. Native Windows unsupported | **No** — opt-in via `/sandbox` or `sandbox.enabled` | **Yes.** Out-of-sandbox proxy; **no domains pre-allowed**; `strictAllowlist`, `allowManagedDomainsOnly`. No TLS inspection by default | `claude -p` / `--print`; `--bare` for CI | `--output-format text\|json\|stream-json`, `--json-schema`; exit 0/non-zero, SIGTERM→143 | `--dangerously-skip-permissions` ≡ `--permission-mode bypassPermissions` |
| **Codex CLI** (OpenAI) | `AskForApproval::OnRequest` (`#[default]`) + preset labelled "Default" = `workspace-write`. `SandboxMode` serde default = `ReadOnly` | macOS `/usr/bin/sandbox-exec` (**Seatbelt**, `.sbpl` policies); Linux **bubblewrap + seccomp** by default, legacy **Landlock** via `--use-legacy-landlock`; Windows restricted-token or elevated backend | **Yes on macOS/Linux.** **No on Windows** — `WindowsSandboxLevel` `#[default] Disabled` | **Yes.** `codex-network-proxy` (HTTP/CONNECT/SOCKS5) with per-host allow/deny + audit events; `NetworkAccess` `#[default] Restricted`; optional MITM | `codex exec [PROMPT]` (reads stdin, `-` supported) | `--json` (JSONL events), `--output-schema FILE`, `-o/--output-last-message FILE` | `--dangerously-bypass-approvals-and-sandbox` (alias `yolo`) |
| **Gemini CLI** (Google) | `general.defaultApprovalMode` = `"default"` — prompts for approval | **Widest menu, all off:** macOS `sandbox-exec` (6 named profiles), Docker, Podman, **gVisor (`runsc`)**, LXC | **No** — `-s`/`--sandbox`, `GEMINI_SANDBOX=…`, or `tools.sandbox` | Only via `permissive-proxied`/`restrictive-proxied`/`strict-proxied` Seatbelt profiles, or a container you configure | `gemini -p "…"` (also auto-triggers in any non-TTY) | `--output-format text\|json\|stream-json`; **named exit codes 0/1/42/53** | `--approval-mode=yolo` (CLI only — cannot be set from a settings file) |
| **Aider** | Prompts per confirmation; **auto-commits every edit** (`--auto-commits` default `True`) | **None** | **No** | **None** | `aider -m "…"` / `-f FILE`; `--commit`; `--exit` | None documented (plain text) | `--yes-always` ("Always say yes to every confirmation") |
| **opencode** | **Allow-all.** "By default, opencode allows all operations without requiring explicit approval." Exceptions: `doom_loop`, `external_directory` → `ask`; `.env` → `deny` | **None documented** | **No** | **None documented** | `opencode run [message..]`; `--attach http://localhost:4096` | `--format default\|json` | `--auto` ("Auto-approve permissions that are not explicitly denied") |
| **Amp** (Sourcegraph) | **No approval at all.** "By default, Amp does not ask for approval before running tools." MCP servers likewise: "If no rule matches an MCP server, Amp allows it." | **None documented** — "runners" are remote thread executors in the current directory, not isolation | **No** | **None documented** | `amp -x` / `--execute` (reads stdin; auto-enabled when stdout is redirected) | Streaming JSON documented separately | Already the default; `amp.dangerouslyAllowAll` activates the legacy rules plugin |
| **Amazon Q Developer CLI** | Built-in default agent: `"tools": ["*"], "allowedTools": ["fs_read"]` — only file reads pre-approved | **None** | **No** | **None** | `q chat --no-interactive` (alias `non-interactive`); reads stdin | None documented | `-a` / `--trust-all-tools` |
| **Charm Crush** | "By default, Crush will ask you for permission before running tool calls." | **None** | **No** | **None** | `crush serve` + client; `--cwd`-keyed workspaces | Not documented in README | `--yolo` — **first-wins per workspace**: a later client at the same `--cwd` cannot turn it off |
| **Goose** (Block → `aaif-goose`) | **Completely Autonomous.** Docs carry a warning: "`Autonomous Mode` is applied by default." | **None** — containment is at MCP-extension *install* time via `GOOSE_ALLOWLIST` | **No** | **None** | `goose run -t "…"` / `-i FILE` / `-i -` (stdin) | Not documented | Already the default; `/mode auto` |
| **Continue CLI** (`cn`) | Read-only tools `allow`; `Edit`/`MultiEdit`/`Write`/`Bash` `ask`. **In headless mode `ask` tools are excluded entirely** | **None** | **No** | **None** | `cn -p "…"`; `cn -p --resume` | `--format json`, `--silent` | `--auto` (absolute override: `*: allow`) |
| **Droid** (Factory) | **Read-only reconnaissance** with no flag — the most restrictive default in the set | **None documented** | **No** | **None documented** | `droid exec` | `-o/--output-format text\|json\|stream-jsonrpc`; **fail-fast, non-zero exit, "no partial changes"** | `--skip-permissions-unsafe` |

*(Codebuff was checked and excluded: `github.com/CodebuffAI/codebuff` now presents as "Freebuff", a
free ad-supported multi-product suite, and publishes no permission or containment model. Read 2026-08-30.)*

### Granularity and programmability

| Tool | Permission granularity | Persistent allowlist | Rule precedence | Hooks | MCP | Subagents | SDK | Local / open-weight models |
|---|---|---|---|---|---|---|---|---|
| **Claude Code** | Per-tool, per-command-prefix (`Bash(git commit *)`), per-path (four anchor forms incl. `Edit(//secrets/**)`), per-domain (`WebFetch(domain:*.example.com)`), **per-input-parameter** (`Agent(model:opus)`, `Bash(run_in_background:true)`) for deny/ask | `settings.json` at managed / project / local / user scopes; `/permissions` | **deny → ask → allow**, first match wins; specificity irrelevant; managed settings beat CLI args | ~30 events; 5 handler types (`command`, `http`, `mcp_tool`, `prompt`, `agent`); `permissionDecision: allow\|deny\|ask`; exit 2 blocks | Yes | Yes (classifier checks at spawn, per-action, and on return) | Python + TypeScript Agent SDK; `canUseTool`, `permissionMode`, `setPermissionMode()` | Via Bedrock/Vertex/Foundry only |
| **Codex CLI** | Permission profiles + `execpolicy` `.rules` DSL; `writable_roots` with `read_only_subpaths` protecting `.codex`, `.git`, `.git/hooks`; per-host network policy | `config.toml`, `<name>.config.toml` profiles, `requirements.toml` (managed) | Layered config stack low→high; managed `requirements.toml` constrains | 12 events; 4 handler types (`Command`, `McpTool`, `Prompt`, `Agent`); `HookTrustStatus` gates execution | Yes (`codex mcp`) | Yes (`SubAgentSource`, `SubagentStart`/`Stop` hooks) | App-server protocol; `codex-mcp` | **Yes** — `--oss` with `--local-provider {lmstudio\|ollama}` |
| **Gemini CLI** | TOML policy engine: `toolName` (+ MCP wildcards), `commandPrefix`, `argsPattern` (regex over stable-JSON args), **`interactive: true\|false`** so a rule can target headless runs specifically | `~/.gemini/policies/*.toml` | `final_priority = tier_base + (toml_priority/1000)`; Default 1 / Extension 2 / **Workspace 3 (non-functional, [#18186](https://github.com/google-gemini/gemini-cli/issues/18186))** / User 4 / Admin 5 | `settings.json` `hooks`, `command` type only, `matcher` regex, `sequential`, 60 000 ms default timeout, exit 2 blocks | Yes | Yes | Extensions | Model-agnostic via providers |
| **Aider** | None (no tool-call surface) | n/a | n/a | No | No | No | Unsupported Python `Coder` API | **Yes** — any LiteLLM-reachable model |
| **opencode** | Per-tool and per-pattern (`"bash": {"*": "ask", "git *": "allow", "rm *": "deny"}`); per-agent overrides | `opencode.json` | **Last matching rule wins** | Not documented | Yes | Yes (`task` tool) | `opencode serve` HTTP server | **Yes** — model-agnostic |
| **Amp** | Plugin API only; `amp.tools.disable` globs with `builtin:` prefix; `amp.mcpPermissions` | Settings file | First matching MCP rule; unmatched = allow | Plugin API | Yes | Yes | Plugin API | No |
| **Amazon Q CLI** | `allowedTools` globs incl. MCP `@server/tool_*`; `toolsSettings` (e.g. `fs_write.allowedPaths`) | Agent JSON files | Agent file; `--trust-tools=` overrides | `agentSpawn`, `userPromptSubmit`, `preToolUse` (can block), `postToolUse`, with `matcher` | Yes | No | No | No |
| **Crush** | Per-tool `permissions allow …` / `permissions deny …` (deny hides the tool from the agent) | `crush.json` | Not documented | "Preliminary support" | Yes | No | `crush serve` | **Yes** — model-agnostic |
| **Goose** | Per-tool permissions under Manual/Smart Approval; extension allowlist by MCP install command | `GOOSE_ALLOWLIST` URL → YAML | Allowlist blocks install; modes set the rest | No | Yes (extensions *are* MCP servers) | Yes (recipes, subagents) | ACP | **Yes** — model-agnostic |
| **Continue CLI** | `allow`/`ask`/`exclude` per tool and per pattern (`Write(**/*.ts)`, `Bash(npm install*)`) | `~/.continue/permissions.yaml` | Mode policies (`--auto`/`--readonly`) → CLI flags → `permissions.yaml` → defaults | No | Yes | Yes | `@continuedev/cli` | **Yes** — model-agnostic |
| **Droid** | Named autonomy levels + `--restrict-tools` / `--additional-tools` / `--disabled-tools` | Settings file | `--auto` level, then tool restrictions | No | Yes | Yes (custom droids) | `droid exec` + stream-jsonrpc | Not documented |

---

## Detail by tool

### Claude Code (Anthropic)

**Permission modes.** Six, by exact config value:
[`default`](https://code.claude.com/docs/en/permission-modes) (labelled **Manual**, alias `manual` from
v2.1.200), `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`. Modes set the baseline;
permission rules layer on top. Deny rules block in every mode including `bypassPermissions`; allow
rules have no effect in `bypassPermissions`.

**The default changed.** "On Pro, Max, and Team plans, the built-in starting permission mode is auto
mode." The table of built-in defaults is worth reproducing in the reference document, because it is
where an organisation's actual posture is decided:

| How Claude Code is run | Built-in starting mode |
|---|---|
| Any settings file sets `disableAutoMode` to `"disable"` | `default` |
| Feature-flag fetching is off | `default` |
| First session after install/upgrade (unless flags arrive in time) | `default` |
| `claude -p` or the Agent SDK | `default` |
| Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, Claude Platform on AWS, gateway | `default` |
| **Pro, Max or Team plan, in a terminal or the VS Code extension** | **`auto`** |
| Enterprise plan or a Claude Console API key | `default` |

*(Vendor documentation, 2026-08-30.)*

**Rule syntax and granularity.** `Tool` or `Tool(specifier)`. `Bash(*)` ≡ `Bash`. Wildcards: "Claude
Code matches everything before the first `*` as written", so `Bash(git log *)` allows only `git log`
while `Bash(git *)` allows every git subcommand — including `-c`, "which makes git run a program you
name". The docs warn at startup about an allow rule with a `*` before the subcommand. Deny/ask rules
additionally match a top-level input parameter (`Agent(model:opus)`, `Bash(run_in_background:true)`),
but **not** a tool's primary content field: "A rule like `Bash(command:rm *)` would be bypassable by a
compound command, so Claude Code ignores it and emits a startup warning."

**Evaluation order.** "Rules are evaluated in order: deny, then ask, then allow. The first match in
that order determines the outcome, and rule specificity doesn't change the order." A broad deny cannot
carry allowlist exceptions. A bare-name deny removes the tool from Claude's context entirely.

**Precedence.** "Permission rules follow the same settings precedence as all other Claude Code
settings, with managed settings highest: no other level, including command line arguments, can
override a managed permission rule." A deny at any scope beats an allow at any other.

**The auto-mode classifier.** A separate model (Sonnet 5 by default) reviews each action. Decision
order: (1) explicit allow/ask/deny rules resolve immediately, with exceptions routed to the
classifier; (2) read-only actions and working-directory edits auto-approve; (3) everything else goes
to the classifier; (4) a block returns to Claude, usually as the fixed text `Blocked by classifier`.
The classifier "sees user messages, tool calls other than read-only lookups… and your CLAUDE.md
content. **Tool results are stripped**, so hostile content in a file or web page can't manipulate it
directly." Blocked-by-default categories are enumerated at length and include `curl | bash`,
production deploys, force push, `git reset --hard`, `terraform destroy`, IAM grants, merging an
unapproved PR, and "posting a comment that is itself a command to automation, such as `atlantis apply`".

**Auto-mode fallback thresholds.** "if the classifier blocks an action 3 times in a row or 20 times
total, auto mode pauses and Claude Code resumes prompting… These thresholds are not configurable."

**Sandboxing.** Opt-in. "On macOS, there is nothing to install: sandboxing uses the built-in Seatbelt
framework. On Linux and WSL2, the sandbox relies on two packages" — `bubblewrap` and `socat`, plus an
optional seccomp filter shipped as `@anthropic-ai/sandbox-runtime` that "adds Unix domain socket
blocking". Native Windows is not supported. Default write scope is cwd + `additionalDirectories` +
session `$TMPDIR`; **default read scope is the entire computer**, and the docs are explicit that "this
default still allows reading credential files such as `~/.aws/credentials` and `~/.ssh/`."

Protected paths inside the writable area cannot be exempted by any allow rule — `.claude` settings,
`.claude/skills|agents|commands|hooks`, `.mcp.json`, `.git/hooks`, `.git/config`, shell startup files.
"There is no way to exempt one of these paths."

Failure mode is permissive by default: "if the sandbox cannot start because dependencies are missing
or the platform is unsupported, Claude Code shows a warning and runs commands without sandboxing."
`sandbox.failIfUnavailable: true` makes it a hard failure. An escape hatch is on by default: Claude
"may retry the command with the `dangerouslyDisableSandbox` parameter", which can be shut off with
`"allowUnsandboxedCommands": false`.

**Scope limit worth naming.** "The sandbox isolates Bash subprocesses… Read, Edit, and Write use the
permission system directly rather than running through the sandbox." So the containment layer and the
file-writing layer are different mechanisms with different rules.

**Headless.** `claude -p` / `--print`. `--output-format text|json|stream-json`; `--json-schema` for a
schema-conforming `structured_output` field; `--include-partial-messages` for token streaming. Exit 0
on success, non-zero on failure, 143 on SIGTERM. `--bare` skips auto-discovery of hooks, skills,
commands, subagents, plugins, MCP servers and CLAUDE.md — "the recommended mode for scripted and SDK
calls, and will become the default for `-p` in a future release." Without `--bare`, **a `-p` session
runs the hooks in a project's `.claude/settings.json` and connects the servers in its `.mcp.json`,
even in a folder you've never trusted**, with no trust dialog. That is a supply-chain surface any team
wiring an agent into CI needs to know about.

**Programmability.** Roughly 30 hook events, of which 13 can block. Five handler types: `command`,
`http`, `mcp_tool`, `prompt` (send to a model for a verdict) and `agent` (spawn a subagent to verify).
`hookSpecificOutput.permissionDecision` takes `allow|deny|ask`. Exit code 2 blocks and "overrides all
JSON decisions". Agent SDK in Python and TypeScript with a six-step documented evaluation flow —
hooks → deny → ask → mode → allow → `canUseTool` — and an explicit warning that "**Auto-approved tools
never reach `canUseTool`**", so a permission check written into that callback is silently bypassed for
any tool covered by a bare allow entry. The recommended fix is a `PreToolUse` hook, "hooks run before
every other step".

**Ceiling.** Product decision. `--dangerously-skip-permissions` exists and the vendor's own language
is unambiguous: "`bypassPermissions` offers no protection against prompt injection or unintended
actions." Two architectural constraints do exist: it refuses to start in that mode as root or under
`sudo` on Linux and macOS ("`--dangerously-skip-permissions` cannot be used with root/sudo privileges
for security reasons"), and Claude Code on the web ignores `bypassPermissions` and `dontAsk` from
settings files, so a repository's checked-in settings cannot start a cloud session in bypass mode.

### OpenAI Codex CLI (open source — read from source)

**The approval enum, verbatim** from `codex-rs/protocol/src/protocol.rs`:

```rust
pub enum AskForApproval {
    #[serde(rename = "untrusted")] UnlessTrusted,   // projects marked untrusted
    #[serde(alias = "on-failure")] #[default] OnRequest,
    #[strum(serialize = "granular")] Granular(GranularApprovalConfig),
    Never,                                          // failures returned to the model, never escalated
}
```

`GranularApprovalConfig` splits approval into five independently togglable flows —
`sandbox_approval`, `rules`, `skill_approval`, `request_permissions`, `mcp_elicitations` — which is
the finest-grained approval decomposition found in the set.

**The sandbox policy enum**, same file: `DangerFullAccess`, `ReadOnly { network_access }`,
`ExternalSandbox { network_access }`, and `WorkspaceWrite { writable_roots, network_access,
exclude_tmpdir_env_var, exclude_slash_tmp }`. `network_access` is documented in the source as "`false`
by default". `SandboxMode` in `config_types.rs` derives `Default` with `#[default] ReadOnly`;
`NetworkAccess` derives `#[default] Restricted`.

**`WritableRoot` carries `read_only_subpaths`**, described in the source as ensuring "that folders
containing files that could be modified to escalate the privileges of the agent (e.g. `.codex`,
`.git`, notably `.git/hooks`) under a writable root are not modified by the agent." This is the same
protection Claude Code implements, arrived at independently.

**The three shipped presets** (`codex-rs/utils/approval-presets/src/lib.rs`), verbatim descriptions:
- `read-only` — "Codex can read files in the current workspace. Approval is required to edit files or access the internet." (`OnRequest` + read-only profile)
- `auto`, labelled **"Default"** — "Codex can read and edit files in the current workspace, and run commands. Approval is required to access the internet or edit other files. (Identical to Agent mode)" (`OnRequest` + workspace-write)
- `full-access` — "Codex can edit files outside this workspace and access the internet without asking for approval." (`AskForApproval::Never` + `PermissionProfile::Disabled`)

**OS primitives, source-verified.** macOS: `pub const MACOS_PATH_TO_SEATBELT_EXECUTABLE: &str =
"/usr/bin/sandbox-exec";` — hardcoded, with a source comment explaining that only `/usr/bin` is
considered "to defend against an attacker trying to inject a malicious version" on `PATH`. Policies
are `.sbpl` files compiled into the binary (`seatbelt_base_policy.sbpl`,
`seatbelt_network_policy.sbpl`, `seatbelt_preferences_policy.sbpl`,
`seatbelt_read_only_platform_defaults.sbpl`). Linux: a self-invoking helper named
`codex-linux-sandbox` that "performs the actual sandboxing (**bubblewrap by default + seccomp**)",
with `--use-legacy-landlock` selecting the older Landlock path and `--allow-network-for-proxy`
requiring "bubblewrap's isolated network namespace". Windows: `codex-rs/windows-sandbox-rs` with an
elevated backend and an unelevated restricted-token backend — **and `WindowsSandboxLevel` derives
`#[default] Disabled`.**

**Egress.** `codex-rs/network-proxy/` is a full proxy implementation: HTTP, HTTPS CONNECT, SOCKS5 TCP
and UDP, per-host `allow`/`deny` decisions emitted as structured audit events
(`codex.network_proxy.policy_decision`), plus `mitm.rs`, `certs.rs` and a `credential_broker` for TLS
termination and credential injection. Codex is the only tool in the set whose egress layer ships
first-class audit telemetry.

**CLI flags, source-verified** (`codex-rs/utils/cli/src/shared_options.rs`):
`-s`/`--sandbox {read-only|workspace-write|danger-full-access}`;
`--approve-for-me` (alias `not-so-yolo`), which pushes `approval_policy="on-request"` and
`sandbox_mode="workspace-write"`; `--dangerously-bypass-approvals-and-sandbox` (alias `yolo`),
documented in source as "Skip all confirmation prompts and execute commands without sandboxing.
EXTREMELY DANGEROUS. Intended solely for running in environments that are externally sandboxed";
`--dangerously-bypass-hook-trust`; `--add-dir`; `-C`/`--cd`. Note that `--full-auto`, widely cited in
older write-ups, **is not present** in the current shared options.

**Headless.** `codex exec [OPTIONS] [PROMPT]`, with `resume`, `fork` and `review` subcommands. Reads
stdin when the prompt is `-` or omitted, and appends piped stdin as a `<stdin>` block when both are
present. `--json` emits JSONL events; `--output-schema FILE` constrains the final response to a JSON
Schema; `-o/--output-last-message FILE` writes the final message. Isolation flags for reproducible CI:
`--ephemeral` (no session files), `--ignore-user-config`, `--ignore-rules`, `--strict-config`,
`--skip-git-repo-check`.

**Programmability.** Hooks (`HookEventName`: `PreToolUse`, `PermissionRequest`, `PostToolUse`,
`PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`, `UserPromptSubmit`, `SubagentStart`,
`SubagentStop`, `Stop`, `Interrupt`) with four handler types and a `HookTrustStatus` of
`Managed|Untrusted|Trusted|Modified` — hooks must be trusted before they run, which no other tool in
the set enforces. An `execpolicy` crate with `.rules` files loadable at user and project scope.
MCP (`codex-mcp`), skills, AGENTS.md, plugins, and a `requirements.toml` managed-policy layer with
`allow_managed_hooks_only`.

**Local models.** `--oss` ("Use open-source provider") with `--local-provider` ("lmstudio or ollama").
Codex is the only first-party vendor CLI in the set with a documented local-model path.

**Ceiling.** Architectural on macOS and Linux in a real sense — the sandbox is the substrate and
`Never` approval still runs inside it unless you also pass the bypass flag. Product decision on
Windows, where the sandbox is off by default.

### Gemini CLI (Google, open source)

**Approval modes.** `--approval-mode {default|auto_edit|yolo|plan}`; `-y`/`--yolo` is deprecated in
favour of `--approval-mode=yolo`. The settings key `general.defaultApprovalMode` defaults to
`"default"`, and its own description carries the constraint: "YOLO mode (auto-approve all actions) can
only be enabled via command line (`--yolo` or `--approval-mode=yolo`)." Combined with
`security.disableYoloMode`, this is the cleanest structural constraint in the set: **a repository
cannot ship a config that turns approval off.**

**The policy engine** is the most expressive rule language found. TOML files in
`~/.gemini/policies/*.toml`:

```toml
[[rule]]
toolName = "run_shell_command"
commandPrefix = "rm -rf"
decision = "deny"
priority = 100
```

Conditions: `toolName` with wildcards (`*`, `mcp_server_*`, `mcp_*_toolName`, `mcp_*`), `commandPrefix`,
`argsPattern` (a regex tested against "a stable JSON string" of the arguments), and **`interactive`**
— "`true`: the rule applies only in interactive mode. `false`: the rule applies only in
non-interactive (headless) mode." No other tool lets a rule target the unattended case specifically.

Decisions `allow|deny|ask_user`. Two behaviours matter for autonomy: "For global rules (those without
an `argsPattern`), tools that are denied are **completely excluded from the model's memory**", and
"`ask_user`… (In non-interactive mode, this is treated as `deny`.)"

Priority: `final_priority = tier_base + (toml_priority / 1000)` over Default 1 / Extension 2 /
Workspace 3 / User 4 / Admin 5. **The Workspace level is currently non-functional** — the docs carry
a warning: "Defining policies in a workspace's `.gemini/policies` directory will not have any effect.
See [issue #18186](https://github.com/google-gemini/gemini-cli/issues/18186)." A team that put its
project policy there has no policy.

**Sandboxing.** The widest menu and all of it off by default: `GEMINI_SANDBOX=true|docker|podman|
sandbox-exec|runsc|lxc`. `runsc` is **gVisor** — Gemini CLI is the only tool in the set offering a
user-space kernel as a first-class option. macOS Seatbelt ships six named profiles
(`permissive-open` default, plus `permissive-proxied`, `restrictive-open`, `restrictive-proxied`,
`strict-open`, `strict-proxied`); the `-proxied` variants are the only documented egress control.
Container mode mounts cwd "at the **exact same absolute path** as it is on your host machine".
A separate `security.toolSandboxing` setting (default `false`) "isolates individual tools instead of
the entire CLI process".

**Documentation contradiction (contrarian finding).** `docs/cli/trusted-folders.md` states "The
Trusted Folders feature is **disabled by default**." The settings table in `docs/cli/settings.md`
lists `security.folderTrust.enabled` with default `true`. Both files were read at `main` on
2026-08-30. A team cannot determine from the documentation whether folder trust is enforcing.

**Headless.** `-p`/`--prompt`, and headless mode also "triggered when the CLI is run in a non-TTY
environment" — so a CI runner gets it without asking. `--output-format text|json|stream-json`, with
`stream-json` emitting typed events (`init`, `message`, `tool_use`, `tool_result`, `error`, `result`).
**Distinct exit codes**: `0` success, `1` general error or API failure, `42` input error, `53` turn
limit exceeded. This is the only tool in the set that lets a CI gate distinguish "the agent ran out of
turns" from "the agent failed", without parsing output.

**Hooks.** `settings.json` `hooks` object; `type: "command"` only; `matcher` regex; `sequential`;
`timeout` default 60 000 ms. Same contract as the others: exit `0` = success and stdout parsed as
JSON, exit `2` = "System Block. The action is blocked; `stderr` is used as the rejection reason".

### Aider

**Architecture.** Aider is not a tool-calling agent loop with a permission surface. It is an
edit-application loop: it builds a **repo map**, sends it with the request, parses the model's reply
into file edits, applies them, and commits. The repo map is a tree-sitter symbol extraction over the
repository, ranked with a graph algorithm — "a graph where each source file is a node and edges
connect files which have dependencies" — and truncated to a token budget (`--map-tokens`, "defaults to
1k tokens"). This is the pre-agentic-search context strategy, and it is why Aider has no tool
permission model to describe: there are almost no tools.

**Auto-commit is the distinctive stance.** `--auto-commits` default `True`; `--dirty-commits` default
`True`, so pre-existing uncommitted work is committed *first*, isolating the agent's diff. Commits are
attributed by appending "(aider)" to git author and committer metadata, with
`--attribute-co-authored-by` available as an alternative. `--no-git` disables git entirely, and the
docs pair that with a warning to keep backups. **Version control is the containment mechanism** — the
only design in the set that makes that choice deliberately.

**Scripting.** `-m`/`--message` and `-f`/`--message-file` run one instruction and exit; `--yes-always`
= "Always say yes to every confirmation"; `--auto-test` (default `False`) and `--lint` close a
feedback loop. The Python API (`Coder.create(...).run(...)`) is documented with the caveat that it "is
not officially supported or documented, and could change in future releases without providing
backwards compatibility" — which rules it out as a foundation for a team's own agent harness.

**What it cannot do.** No sandbox, no egress control, no per-command allowlist, no hooks, no MCP,
no subagents, no structured output. It runs in the real working tree with the invoking user's
privileges.

### opencode

Three-state permissions (`allow`/`ask`/`deny`) under a top-level `"permission"` key, expressible
per-tool or per-pattern with `*`, `?` and `~`/`$HOME` expansion, overridable per agent, resolved
**last-matching-rule-wins** — the inverse of Claude Code's first-match-in-severity-order and a real
semantic difference for anyone porting rules between them. Default is permissive: "By default,
opencode allows all operations without requiring explicit approval", with `doom_loop` and
`external_directory` defaulting to `ask` and `.env` to `deny`. No sandbox documented.
Headless via `opencode run [message..]` with `--format default|json` and `--auto` ("Auto-approve
permissions that are not explicitly denied"); `--attach http://localhost:4096` reuses a running
`opencode serve` to skip cold start, which makes it the cheapest of the set to call in a tight loop.

### Amp (Sourcegraph)

The most permissive default in the set, stated plainly by the vendor: "By default, Amp does not ask
for approval before running tools." MCP servers follow the same rule — "Amp applies the first matching
rule. If no rule matches an MCP server, Amp allows it." Permission controls exist only through the
Plugin API; a legacy rules plugin activates if `amp.permissions`, `amp.guardedFiles.allowlist` or
`amp.dangerouslyAllowAll` is present. The docs acknowledge the exposure — "Untrusted repositories, MCP
servers, and other external inputs can influence what Amp does" — and direct users to "custom policy
plugins or isolated environments", i.e. containment is the user's problem. `amp.tools.disable` accepts
globs and a `builtin:` prefix to block a built-in tool without an MCP server shadowing it.

**Headless.** `-x`/`--execute` sends a message, waits for the turn to end, prints the final message
and exits; it "is automatically turned on when you redirect stdout". Streaming JSON is documented
separately. `AMP_API_KEY` for non-interactive auth.

**"Runners" are not isolation.** `amp --no-tui [--runner-id <id>]` waits for and runs remotely created
threads "in the current directory without opening the TUI" — a remote work intake mechanism on your
real filesystem, not a sandbox.

Amp commits with a coauthor trailer and an Amp thread trailer by default
(`amp.git.commit.coauthor.enabled`, `amp.git.commit.ampThread.enabled`, both `true`), which is a
provenance mechanism worth noting for the observability strand.

### Amazon Q Developer CLI

The built-in default agent, verbatim from the repository:

```json
{ "name": "default", "tools": ["*"], "allowedTools": ["fs_read"],
  "resources": ["file://AmazonQ.md", "file://README.md", "file://.amazonq/rules/**/*.md"],
  "useLegacyMcpJson": true }
```

Every tool is available; only `fs_read` is pre-approved. `allowedTools` supports glob patterns over
native tools (`fs_*`, `*_bash`, `fs_?ead`) and MCP tools (`@server/read_*`, `@git-*/*`), and
**deliberately refuses the `"*"` wildcard** that the `tools` field accepts — "Unlike the `tools` field,
the `allowedTools` field does not support the `"*"` wildcard for allowing all tools." `toolsSettings`
carries per-tool configuration such as `fs_write: { allowedPaths: ["~/**"] }`.

Hooks: `agentSpawn`, `userPromptSubmit`, `preToolUse` (documented as able to block the tool use) and
`postToolUse`, each with an optional `matcher`.

**Headless, source-verified** from `crates/chat-cli/src/cli/chat/mod.rs`: `--no-interactive` (alias
`non-interactive`) — "Whether the command should run without expecting user input" — which reads the
prompt from stdin when no positional input is given; `-a`/`--trust-all-tools` — "Allows the model to
use any tool to run commands without asking for confirmation"; `--trust-tools=<TOOL_NAMES>` with the
documented idiom `--trust-tools=` (empty) meaning trust nothing. No sandbox, no egress control, no
structured output format.

### Charm Crush

"By default, Crush will ask you for permission before running tool calls." Allowlisting is per-tool
(`permissions allow view ls grep edit mcp_context7_get-library-doc`); denial hides the tool from the
agent entirely (`permissions deny bash sourcegraph`). `--yolo` "skip[s] all permission prompts
completely… Be very, very careful with this feature."

**A footgun worth reporting.** Crush supports a shared backend (`crush serve`) with clients grouped
into workspaces keyed by their resolved `--cwd`. "The first client to create a workspace fixes its
process-wide flags. In particular, `--yolo` and `--debug` follow a **first-wins** rule: later clients
that arrive at the same `--cwd` with different values for those flags do not change the running
workspace." A developer who attaches to a colleague's workspace inherits `--yolo` and cannot turn it
off; the mismatch is recorded only in a debug log line. Clients also "share the session list, message
history, **permission queue**, LSP, and MCP state."

Context comes from `~/.config/crush/CRUSH.md` and `~/.config/AGENTS.md`; `.crushignore` extends
`.gitignore`. Hooks have "preliminary support". No sandbox.

### Goose (Block → `aaif-goose`)

Four permission modes: **Completely Autonomous** ("goose can modify files, use extensions, and delete
files **without requiring approval**"), **Manual Approval**, **Smart Approval** ("a risk-based
approach to automatically approve low-risk actions and flag others"), **Chat Only**. Set with
`/mode auto|approve|smart_approve|chat`. The docs' own warning admonition: "`Autonomous Mode` is
applied by default."

**Containment is at the wrong layer to substitute for a sandbox, but it is real.** `GOOSE_ALLOWLIST`
points at a URL serving a YAML list of permitted MCP server install commands; "If the command is not
in the allowlist, the extension installation is rejected." This gates *what tools exist*, not *what
they may do* — a useful supply-chain control for a corporate deployment, and no substitute for
per-call permission or OS isolation.

Headless: `goose run -t "your instructions here"`, `-i instructions.md`, or `-i -` for stdin, with the
docs naming CI/CD as the use case. Model-agnostic, so open-weight and local models are available.

The repository moved: `github.com/block/goose` HTTP-301s to `aaif-goose/goose` (observed 2026-08-30).

### Continue CLI (`cn`)

The clearest small permission model in the set. Three levels — `allow` (runs, no prompt), `ask`
(prompts, TUI only), `exclude` (hidden from the agent entirely). Defaults: read-only tools (`Read`,
`List`, `Search`, `Fetch`, `Diff`, `AskQuestion`, `Checklist`, `Status`, `CheckBackgroundJob`,
`ReportFailure`, `UploadArtifact`) `allow`; `Edit`, `MultiEdit`, `Write` and `Bash` `ask`.

**Its headless behaviour is a design choice worth borrowing.** "In headless mode, `ask` tools are
excluded since there's no one to approve them." Not denied at call time — *removed*, so the model
never proposes the action and never burns a turn discovering it can't. `cn -p "…" --allow Write
--allow Edit` re-enables specific writes.

Patterns: `Write(**/*.ts)`, `Bash(npm install*)`. Persistent state in `~/.continue/permissions.yaml`.
Precedence is documented explicitly: mode policies (`--auto`, `--readonly`) → CLI flags →
`permissions.yaml` → defaults, with plan and auto as "absolute overrides. They ignore `--allow`,
`--exclude`, and `permissions.yaml` entirely."

Headless: `cn -p`, `--silent`, `--format json`, `cn -p --resume`. No sandbox.

### Droid (Factory)

**The most restrictive default and the best-specified headless contract.** With no flag, Droid permits
"Read-only file inspection, directory listing, process and environment inspection, and git read
operations such as `git status`, `git log`, and `git diff`" — and blocks file edits, package installs,
git writes and system changes.

`--auto` takes three named levels:

| Level | Allows | Blocks |
|---|---|---|
| `low` | "Low-risk project file creation and edits" | System modifications, package installs, remote writes, production changes |
| `medium` | Low-risk plus "trusted package installs, builds, tests, `git commit`, `git checkout`, and `git pull`" | `git push`, sudo, production changes |
| `high` | "remote writes, deployments, database migrations" | "Extreme destructive operations like `sudo rm -rf /`" |

Tool surface is separately restrictable with `--restrict-tools`, `--additional-tools` and
`--disabled-tools`. `--skip-permissions-unsafe` removes the checks — the docs' own wording is
"Removes all guardrails" [their term], with the instruction to use it "**only** in isolated
environments like Docker containers". `--mission` (multi-agent orchestration) is gated: it "requires
either `--auto high` or `--skip-permissions-unsafe`", which is an unusually explicit statement that
orchestration and autonomy are coupled.

`droid exec` supports `-o/--output-format text|json|stream-jsonrpc`, `--input-format`, `-f/--file`,
`--session-id`, `--fork`. Its exit contract is the strongest in the set: "`droid exec` exits `0` on
success and non-zero on failure (permission violation, tool error, unmet objective)" and, on exceeding
the autonomy level, "stops immediately with a clear error message, returns a non-zero exit code, and
**performs no partial changes**." No other tool promises atomicity on a policy stop.

No sandbox or egress control is documented.

---

## Cross-cutting observations for the reference document

1. **The structural hinge has already been crossed everywhere.** Headless operation is not a
   distinguishing property of a tool any more; it is a property of the category. The useful question
   moved downstream: given that the tool *can* run unattended, what does its permission model do when
   nobody answers? Four incompatible answers exist (finding 5), and they are not interchangeable —
   "deny", "exclude", "fail-fast with no partial writes" and "skip and keep going" produce four
   different CI behaviours from the same prompt.

2. **Two architectures, not one.** Codex CLI treats the sandbox as the substrate and approval as the
   escalation path out of it. Everyone else treats approval as the substrate and the sandbox, if any,
   as an optional layer. The consequence is that Codex's *worst case* (a user who never reads a
   prompt) is still contained on macOS and Linux, while the worst case for the approval-first tools is
   an unconstrained shell. This distinction is more predictive of blast radius than any default-mode
   comparison.

3. **The permission-model vocabulary has converged; the semantics have not.** Nearly every tool now
   offers three states — allow, ask, deny — but the resolution rules differ in ways that silently
   change behaviour: Claude Code evaluates deny → ask → allow with first-match-wins and specificity
   deliberately ignored; opencode uses last-matching-rule-wins; Gemini computes a numeric priority
   across five named levels; Continue documents a four-source precedence chain. A rule set ported
   between tools by shape will not behave the same way.

4. **Containment is where the field is thinnest.** Two OS-primitive sandboxes, one of them opt-in and
   scoped to Bash subprocesses only; one menu of container/gVisor options that ships entirely off;
   three egress-control implementations, two of which document that they cannot inspect TLS. Against
   eleven tools with mature permission-prompt UX, that is a lopsided investment — and the vendor with
   the telemetry is on record that the prompt is approved 93–97% of the time.

5. **The verification coupling is absent everywhere.** No permission rule in any of the eleven can
   depend on whether the tests passed, the types check, or the diff was reviewed. Permission is a
   function of the *call*; verification is a function of the *result*; nothing joins them. Teams
   further along the spectrum need exactly that join, and today they must build it themselves out of
   `PreToolUse` hooks.

6. **The `-p`-runs-untrusted-repo-hooks problem is a supply-chain surface nobody has closed.** Claude
   Code documents it and offers `--bare`; Codex offers `--ignore-user-config` and `--ignore-rules`;
   Gemini has folder trust whose default the docs contradict themselves about; Goose gates MCP
   installs by allowlist. No tool in the set is safe-by-default when pointed at an untrusted
   repository in an unattended run.

---

## Sources

All web documentation read 2026-08-30. All source read at `main` on 2026-08-30.

**Claude Code (vendor documentation, Anthropic)**
- Permission modes — https://code.claude.com/docs/en/permission-modes
- Permissions and rule syntax — https://code.claude.com/docs/en/permissions
- Sandboxing — https://code.claude.com/docs/en/sandboxing
- Hooks — https://code.claude.com/docs/en/hooks
- Headless / programmatic use — https://code.claude.com/docs/en/headless
- Agent SDK overview — https://code.claude.com/docs/en/agent-sdk/overview
- Agent SDK permissions (six-step evaluation flow) — https://code.claude.com/docs/en/agent-sdk/permissions
- Settings reference — https://code.claude.com/docs/en/settings-reference
- CHANGELOG (v2.1.251 at time of reading) — https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- "Auto mode for Claude Code" (2026-03-24, updated 2026-07-10) — https://claude.com/blog/auto-mode
- Engineering deep dive, classifier metrics (2026-03-25) — https://www.anthropic.com/engineering/claude-code-auto-mode
- "Auto mode is now the default…" (~2026-08-08) — https://claude.com/blog/auto-mode-default-in-claude-code

**OpenAI Codex CLI (source, `openai/codex`)**
- `codex-rs/protocol/src/protocol.rs` — `AskForApproval`, `GranularApprovalConfig`, `NetworkAccess`, `SandboxPolicy`, `WritableRoot`, `HookEventName`, `HookHandlerType`, `HookTrustStatus`
- `codex-rs/protocol/src/config_types.rs` — `SandboxMode` (`#[default] ReadOnly`), `WindowsSandboxLevel` (`#[default] Disabled`)
- `codex-rs/utils/approval-presets/src/lib.rs` — the three shipped presets, verbatim
- `codex-rs/utils/cli/src/shared_options.rs` — `--sandbox`, `--approve-for-me`, `--dangerously-bypass-approvals-and-sandbox`, `--oss`, `--local-provider`
- `codex-rs/utils/cli/src/sandbox_mode_cli_arg.rs`, `approval_mode_cli_arg.rs`
- `codex-rs/exec/src/cli.rs` — `codex exec` flags, subcommands, `--json`, `--output-schema`
- `codex-rs/sandboxing/src/seatbelt.rs` — `MACOS_PATH_TO_SEATBELT_EXECUTABLE`, `.sbpl` policy files
- `codex-rs/sandboxing/src/landlock.rs` — "bubblewrap by default + seccomp", `--use-legacy-landlock`
- `codex-rs/sandboxing/src/windows.rs` — elevated vs restricted-token backends
- `codex-rs/network-proxy/src/network_policy.rs`, `connect_policy.rs` — proxy protocols and audit events
- `docs/config.md`, `docs/execpolicy.md` (both now stubs pointing at hosted docs)

**Gemini CLI (source, `google-gemini/gemini-cli`)**
- `docs/reference/policy-engine.md` — rules, conditions, decisions, priority formula, the non-functional Workspace level
- `docs/cli/sandbox.md` — sandbox methods and Seatbelt profiles
- `docs/cli/cli-reference.md` — `--approval-mode`, `--yolo`, `--sandbox`, `--output-format`
- `docs/cli/headless.md` — output formats, exit codes 0/1/42/53
- `docs/cli/settings.md` — `general.defaultApprovalMode`, `security.*`
- `docs/cli/trusted-folders.md` — folder trust (default contradicts `settings.md`)
- `docs/hooks/reference.md` — hook schema, exit-code contract

**Aider (vendor documentation)**
- https://aider.chat/docs/git.html — auto-commit, dirty commits, attribution
- https://aider.chat/docs/config/options.html — flag defaults
- https://aider.chat/docs/repomap.html — tree-sitter + graph ranking, `--map-tokens`
- https://aider.chat/docs/scripting.html — `-m`, `--yes-always`, unsupported Python API
- https://raw.githubusercontent.com/Aider-AI/aider/main/README.md

**opencode** — https://opencode.ai/docs/permissions/, https://opencode.ai/docs/config/, https://opencode.ai/docs/cli/

**Amp (Sourcegraph)** — https://ampcode.com/docs/tools, https://ampcode.com/docs/cli/settings, https://ampcode.com/docs/cli/execute-mode, https://ampcode.com/docs/cli/runners, https://ampcode.com/manual

**Amazon Q Developer CLI (source, `aws/amazon-q-developer-cli`)**
- `docs/default-agent-behavior.md` — built-in default agent JSON
- `docs/agent-format.md` — `allowedTools`, `toolsSettings`, hooks
- `crates/chat-cli/src/cli/chat/mod.rs` — `--trust-all-tools`, `--trust-tools`, `--no-interactive`

**Charm Crush** — https://raw.githubusercontent.com/charmbracelet/crush/main/README.md

**Goose (`aaif-goose/goose`, formerly `block/goose`)**
- `documentation/docs/guides/managing-tools/goose-permissions.md` — the four modes and the default
- `documentation/docs/guides/allowlist.md` — `GOOSE_ALLOWLIST`
- `documentation/docs/guides/running-tasks.md` — `goose run`

**Continue CLI (source, `continuedev/continue`)**
- `docs/cli/tool-permissions.mdx` — levels, defaults, patterns, precedence, modes
- `docs/cli/headless-mode.mdx` — `cn -p`, `--silent`, `--format json`, ask-tools-excluded behaviour

**Droid (Factory)** — https://docs.factory.ai/docs/droid-exec/overview, https://docs.factory.ai/docs/droid-cli/cli-reference, https://docs.factory.ai/cli/getting-started/overview

**Codebuff** — https://raw.githubusercontent.com/CodebuffAI/codebuff/main/README.md (now "Freebuff"; excluded)

**Prior work in this repository, cited rather than re-derived**
- [`verification-isolation.md`](./verification-isolation.md) §7.4 — the 97% / 39% / 13.6% / 89% figures with their Anthropic sourcing and the unresolved 93-vs-97 discrepancy
- [`verification-infrastructure.md`](./verification-infrastructure.md) — the finding that no published mechanism couples verification rigour to autonomy

---

## Confidence and gaps

**High confidence.**
- Every permission-model, sandbox-mechanism and headless-flag claim about Codex CLI and Amazon Q
  Developer CLI, which were read from source rather than documentation.
- Claude Code's permission modes, rule syntax, evaluation order, sandbox mechanism and headless
  contract — the documentation is unusually precise and version-stamped.
- Gemini CLI's policy engine and headless exit codes, read from the repository's own docs.
- The default postures of Amp, opencode and Goose, each of which is stated in a single unambiguous
  first-party sentence.

**Medium confidence.**
- **Claude Code's `sandbox.*` default values.** The settings-reference table does not print defaults.
  I inferred `sandbox.enabled` default `false` from "To enable the sandbox across all of your
  projects, set `sandbox.enabled` to `true`", `failIfUnavailable` default `false` from "By default,
  if the sandbox cannot start… Claude Code shows a warning and runs commands without sandboxing", and
  `autoAllowBashIfSandboxed` default `true` from "leave `autoAllowBashIfSandboxed` at its default of
  `true`". The inferences are strong but they are inferences.
- **Codex's effective launch default.** The serde default for `SandboxMode` is `ReadOnly` and the
  shipped preset labelled "Default" is `workspace-write` + `on-request`. I did not trace the full
  config-resolution path in `codex-rs/core/src/config/mod.rs` (4 756 lines) to confirm which one a
  first run in a trusted git repo lands on. Both are reported above rather than one being asserted.
- **Amp's permission surface.** Documented only as "an internal plugin is activated to apply the
  legacy permissions rules" when `amp.permissions`, `amp.guardedFiles.allowlist` or
  `amp.dangerouslyAllowAll` is detected. The rule format itself is not published on the pages I could
  reach; `amp.permissions` has no schema documentation.
- **Droid's containment.** Absence of sandboxing is inferred from absence in the documentation I
  reached, not from a positive statement.

**Known gaps.**
- **No independent measurement of any permission model's effectiveness.** Every effectiveness figure
  in this document is vendor-reported by a vendor selling the mechanism. No controlled study, no
  third-party audit, no red-team result from a party without a stake was found for any of the eleven.
- **The 93%-vs-97% discrepancy is unresolved and unresolvable from primary sources.** Anthropic
  published 93% on 2026-03-25 and 97% around 2026-08-08 with no denominator, no methodology and no
  time series in either. The habituation claim that both are used to support — that approval rates
  degrade as approvals accumulate — has, as far as this strand could establish, never been measured
  in public by anyone.
- **Codex's classifier-equivalent.** Codex has no analogue of Claude Code's auto-mode classifier; its
  equivalent lever is `execpolicy` `.rules`. I could not read the `.rules` DSL specification —
  `docs/execpolicy.md` in the repository is a one-line stub pointing at hosted documentation that
  redirected away (see below).
- **Crush, Goose and Droid publish no exit-code contract**, so a CI gate around them can only
  distinguish success from failure.
- **Nothing in this strand measures how any of these tools behave under prompt injection.** That is
  the isolation strand's territory and is deliberately not re-derived here.

---

## Blocked or unavailable sources

Logged, not circumvented.

| Source | Attempted URL | Result | Substitute used |
|---|---|---|---|
| OpenAI Codex security & approvals docs | `https://developers.openai.com/codex/security` | 308 → `https://learn.chatgpt.com/docs/security`, which returned only a link stub with no approval-mode, sandbox-primitive or flag content | Read the Rust source directly (higher trust) |
| OpenAI Codex config reference | `https://raw.githubusercontent.com/openai/codex/main/docs/config.md`, `codex-rs/config.md` | Both are stubs redirecting to `developers.openai.com/codex/config-reference` | Read `protocol.rs` / `config_types.rs` / `shared_options.rs` |
| OpenAI Codex execpolicy `.rules` spec | `https://raw.githubusercontent.com/openai/codex/main/docs/execpolicy.md` | One-line stub pointing at `developers.openai.com/codex/exec-policy` | Confirmed the mechanism exists from `codex-rs/execpolicy/` and the `--ignore-rules` flag; the DSL itself is unread |
| OpenAI Codex Linux sandbox semantics | `codex-rs/docs/linux_sandbox.md` (referenced from `landlock.rs`) | 404 — the source comment points at a file that no longer exists | Read `landlock.rs` and `bwrap.rs` directly |
| Amazon Q Developer CLI trust docs | `docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/command-line-trust.html`, `…command-line-chat-tools.html` | 404 and an empty JS-rendered shell | Read `aws/amazon-q-developer-cli` source and `docs/` |
| Charm Crush documentation site | `https://docs.crush.charm.land/` | DNS failure (`getaddrinfo ENOTFOUND`) | Read the repository README |
| Continue CLI hosted docs | `docs.continue.dev/cli/overview`, `/cli/permissions`, `/guides/cli` | Redirect stub and 404s | Read `continuedev/continue` `docs/cli/*.mdx` |
| Factory Droid auto-run docs | `docs.factory.ai/cli/configuration/auto-run`, `/cli/user-guides/autonomy-levels` | 404 | Reached the same content at `/docs/droid-exec/overview` and `/docs/droid-cli/cli-reference` |
| Amp permissions page | `https://ampcode.com/docs/permissions` | 404 — no such page exists | Reached the default-posture statement at `/docs/tools` and settings at `/docs/cli/settings` |
| Gemini CLI configuration page | `docs/cli/configuration.md`, `docs/get-started/configuration.md` | 404 (files moved) | Read `docs/reference/policy-engine.md`, `docs/cli/settings.md`, `docs/cli/sandbox.md` |
| Goose documentation site | `block.github.io/goose/docs/guides/goose-permissions/`, `…/smart-approval/` | 404 | Read `aaif-goose/goose` `documentation/docs/guides/` after following the repository's 301 |

No source was worked around, re-hosted, or fetched through an alternate route after a block. Where a
hosted doc was unreachable, the substitute was the tool's own repository, which is the higher-trust
source in every case.
