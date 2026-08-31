# Tooling Landscape: Inline Completion, and In-Editor Chat/Edit

**Research date:** 2026-08-30
**Ticket:** [#6 Tooling Landscape](https://github.com/AndrewGodlewsky/AI-Framework/issues/6) — strand 1 of 6
**Question:** For the two least-delegated regions of the spectrum — ghost-text completion, and chat/edit
surfaces where a human still accepts every diff — what does the architecture make impossible regardless
of trust, what exactly does the human approve, and can that approval be turned off?

**Method.** Primary sources only: official product documentation, first-party engineering blogs,
published settings references, the GitHub REST API OpenAPI description read directly, and the GitHub
API for repository state. Vendor landing pages were used for exactly one fact and are labelled as such
in place. Every capability claim below carries an "as of" date and a URL. Where a documentation page
moved or died between the ticket being written and this research being run, that move is recorded as a
finding rather than silently corrected.

**A durability warning, stated first.** This is the fastest-ageing material in the project. Between
2024 and this research date, one of the two categories lost its vendor vocabulary entirely: the
"ask / edit / agent" mode taxonomy that framed this strand's brief is no longer how either GitHub or
VS Code documents its own product. The findings below are therefore written around **the acceptance
boundary** — what the human approves, and whether that approval has an off switch — because that is the
part that has held still. Product mode names have not.

---

## Headline findings

Evidence tier is stated with each claim, never as a footer.

1. **Inline completion structurally permits no autonomy at all, and this is the sharpest structural
   line on the whole spectrum.** Across the completion products examined, not one documents a
   completion engine that executes a command, writes to a file the developer is not editing, or makes
   any outbound call beyond the inference request itself. The architecture forecloses it: the surface
   is a text decoration in an editor buffer, and the only committing action is a keypress. *(Tier:
   vendor documentation, fourteen products, read 2026-08-30.)*

2. **The one place this category crosses into acting is not completion — it is inline chat.** VS Code's
   terminal inline chat offers a **Run (⌘Enter)** control that executes the suggested command
   ([VS Code docs, page dated 2026-08-26](https://code.visualstudio.com/docs/copilot/chat/inline-chat)).
   That single control is the category boundary. Everything on the completion side of it proposes text;
   everything on the other side can act.

3. **Completion acceptance cannot be batched or automated anywhere in this survey. Edit acceptance
   can.** No vendor documents an auto-accept for ghost text. But VS Code ships
   **`chat.editing.autoAcceptDelay`** — *"Configure a delay after which suggested edits are
   automatically accepted"*, default `0` (off) — which converts diff review into a countdown timer
   ([VS Code AI settings reference, dated 2026-08-26](https://code.visualstudio.com/docs/agents/reference/ai-settings)).
   This is the single most decision-relevant fact in the strand: the moment a team moves from
   completion to in-editor edit, the approval step acquires an off switch.

4. **"Text at the cursor" is already an out-of-date description of the completion category.** GitHub's
   Next Edit Suggestions predicts *"both the location of the next edit you'll want to make and what
   that edit should be"*, is enabled by default (`github.copilot.nextEditSuggestions.enabled`, default
   `true`), and ships `editor.inlineSuggest.edits.allowCodeShifting` — *"Configure if NES is able to
   shift your code to show a suggestion"* — defaulting to `"always"`. Cursor Tab *"predicts cross-file
   edits when changes in one file need updates in another."* Completion now moves the cursor, shifts
   surrounding code, and points across file boundaries. It still cannot commit any of it without a
   keypress. *(Tier: vendor documentation, 2026-08-26 / 2026-08-30.)*

5. **The one file-scope containment mechanism GitHub ships stops working exactly where the tool starts
   writing.** Copilot content exclusion suppresses inline suggestions in excluded files — and
   *"Content exclusion is currently not supported in Edit and Agent modes of Copilot Chat."* It also
   does not apply to symlinks or remote filesystems, and *"Copilot may use semantic information from an
   excluded file if the information is provided by the IDE indirectly."*
   ([GitHub docs, read 2026-08-30](https://docs.github.com/en/copilot/concepts/content-exclusion).)
   A team that adopts content exclusion as its answer to "what can the AI see" has an answer that
   covers only the least-delegated surface.

6. **The two most-quoted completion figures in the industry are vendor-reported, both are years old,
   and the vendor that collected the more famous one no longer exposes the field.** Google published
   **37% acceptance rate** and **50% of code characters** completed by AI on
   [2024-06-06](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/)
   *(vendor-reported: Google measuring Google)*. GitHub published *"an average of 46% of a developers'
   code"* on [2023-02-14](https://github.blog/news-insights/product-news/github-copilot-now-has-a-better-ai-model-and-new-capabilities/)
   *(vendor-reported)*. As of 2026-08-30, GitHub's REST API exposes **no completion acceptance field at
   all** — verified by reading the OpenAPI description directly (see §1.7).

7. **Acceptance rate measures satisfaction, not output.** GitHub's own researchers found *"the rate
   with which shown suggestions are accepted, rather than more specific metrics regarding the
   persistence of completions in the code over time, drives developers' perception of productivity"*
   ([Ziegler et al., arXiv:2205.06537, 2022-05-13](https://arxiv.org/abs/2205.06537) — *tier:
   observational study, vendor-authored*). Any archetype document that cites an acceptance rate as a
   productivity figure is citing a perception proxy. This is the perception gap appearing at the least
   delegated end of the spectrum, where it is usually assumed not to apply.

8. **The read-only mode has become a standard product primitive, and it is enforced by tool scoping
   rather than by instruction.** Cline Plan mode *"can read your codebase, run searches, and discuss
   strategy, but cannot modify any files or execute commands"*; Continue Plan mode has *"Read-only
   tools for safe exploration and planning"*; Cursor Ask mode is *"a read-only mode… without making any
   edits"*; VS Code custom agents can be defined with a read-only tool set. This is the cleanest
   structural expression of "chat that cannot write", and it is the shape an archetype should specify
   rather than a trust posture. *(Tier: vendor documentation, read 2026-08-30.)*

9. **A completion product that sends nothing over the network is shipped by a mainstream vendor
   today.** JetBrains Full Line Code Completion *"runs entirely on your local device without sending
   any code over the internet"*
   ([JetBrains docs, read 2026-08-30](https://www.jetbrains.com/help/idea/full-line-code-completion.html)).
   Tabnine documents a *"completely air-gapped"* deployment. This is the only region of the spectrum
   where a team can eliminate the egress question outright rather than manage it.

10. **Consolidation has removed two of the named completion vendors as independent products, and a
    third has an announced death date.** Codeium became Windsurf, Windsurf was acquired by Cognition on
    [2025-07-14](https://cognition.com/blog/windsurf), and as of 2026-08-30 `docs.windsurf.com`
    HTTP-307s to `docs.devin.ai/desktop/…`. Supermaven joined Cursor on
    [2024-11-12](https://supermaven.com/blog/cursor-announcement). AWS states: *"On April 30, 2027, AWS
    will discontinue support for Amazon Q Developer IDE plugins."* The FauxPilot lineage is dormant —
    the repository is unarchived but its last push was **2024-04-09** (GitHub API, 2026-08-30).

---

## Part 1 — Inline completion

### 1.1 What the category is, structurally

A completion product renders a *decoration* into an editor buffer. It is not an edit until the
developer commits it with a keypress. Every product surveyed shares this shape:

- a request is made from the editor to a model (local or remote) carrying cursor context,
- a candidate string comes back,
- it is drawn as dimmed "ghost text" or an inline diff overlay,
- **Tab** commits it, **Escape** or continued typing discards it.

VS Code documents the canonical form: Copilot offers *"dimmed ghost text suggestions as you type:
sometimes the completion of the current line, sometimes a whole new block of code"*
([VS Code, 2026-08-26](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions)). Cursor:
*"Tab suggests code as you type, based on your recent edits, surrounding code, and linter errors"*
([Cursor help, read 2026-08-30](https://cursor.com/help/ai-features/tab)). Zed: *"As you type, Zed
requests predictions from the edit prediction provider, which returns individual or multi-line
suggestions you accept by pressing `tab`"*
([Zed docs, read 2026-08-30](https://zed.dev/docs/ai/edit-prediction)).

### 1.2 What it changes about a developer's process

**Concretely, the step the human stops doing is typing the characters — and nothing else.** The
developer still decides what to build, still reads what appears, still decides whether it is right, and
still runs it. Reading is not removed; it is moved earlier and made continuous. The verification burden
is unchanged in kind and is discharged by the same person in the same second.

That is the honest description, and it is a finding in its own right: **this category does markedly
less than its reputation.** The 46%- and 50%-of-code figures (finding 6) describe *character
provenance*, not delegated decisions. Nothing about the process changes hands.

One real second-order change is documented rather than inferred: the JetBrains and Zed docs both make
completion a *navigation* device as well as a text device (accept-to-word-boundary,
accept-to-line-boundary, jump-to-next-edit). The developer's cursor movement partially becomes a thing
the tool proposes.

### 1.3 What degree of autonomy it structurally permits: none, and where that stops being true

**None.** No surveyed completion product can:

- run a shell command,
- write to a file other than the buffer the developer has open at the cursor,
- read a file the editor has not already supplied as context,
- make a network call other than its own inference request,
- persist anything after the editor closes.

The architecture forecloses these, not a policy setting. A completion engine has no tool surface. There
is nothing to grant it.

**Three places where the "only text at the cursor" description gets thinner, all verified:**

| Boundary case | What actually happens | Still gated on a keypress? |
|---|---|---|
| **Cursor Tab cross-file prediction** | *"Tab predicts cross-file edits when changes in one file need updates in another. When a jump to another file is available, a portal window appears at the bottom of the editor."* ([Cursor help](https://cursor.com/help/ai-features/tab), 2026-08-30) | **Yes.** The portal is an offer to navigate; the edit in the other file is still accepted by Tab. |
| **Copilot NES code shifting** | `editor.inlineSuggest.edits.allowCodeShifting`, default `"always"` — *"Configure if NES is able to shift your code to show a suggestion"* ([VS Code settings ref](https://code.visualstudio.com/docs/agents/reference/ai-settings), 2026-08-26) | **Yes**, for the committed edit. But the *display* mutates the buffer layout before acceptance. |
| **Ghost text is generated from context the developer did not choose** | Copilot content exclusion notes *"Copilot may use semantic information from an excluded file if the information is provided by the IDE indirectly"* ([GitHub docs](https://docs.github.com/en/copilot/concepts/content-exclusion), 2026-08-30) | N/A — this is an *input* boundary, not an action boundary, and it leaks. |

**Network egress is the one genuinely non-zero risk surface of the category**, and it is unavoidable
for every cloud product: Zed states plainly that *"Each keystroke can send local editing context to the
selected provider"* ([Zed privacy docs](https://zed.dev/docs/ai/privacy-and-security), 2026-08-30).
Cursor: *"Cursor sends prompts and code context to model providers like OpenAI, Anthropic, and
Google"*; Privacy Mode *"ensures your code is never used for training by Cursor or other AI model
providers"* — it does not stop the transmission
([Cursor privacy help](https://cursor.com/help/security-and-privacy/privacy), 2026-08-30).

The exceptions are §1.6's local lane: JetBrains Full Line, Tabnine air-gapped, Tabby, llama.vscode /
llama.vim, and Continue configured against Ollama.

### 1.4 The acceptance boundary — completion

**What the human approves:** one candidate string, at one cursor position, at the moment it is shown.

**Can it be batched?** No. Nothing in this survey batches completion acceptance.

**Can it be turned off?** No — but the *offering* can be, at three granularities, and every product
ships all three or a subset:

| Product | Global off | Per-language / per-filetype off | Per-directory / temporary |
|---|---|---|---|
| Copilot (VS Code) | `github.copilot.enable: {"*": false}` | yes, per-language map; default `{"*": true, "plaintext": false, "markdown": false, "scminput": false}` | Status Bar snooze |
| Cursor Tab | Tab status indicator → Disable globally | *"Turn Tab off for certain file types"* | Snooze |
| Zed | yes | *"For Specific Languages"* | *"In Specific Directories"* |
| JetBrains | uncheck "Enable inline code completion" / disable the plugin | yes | — |
| Amazon Q | Pause Auto-Suggestions per IDE | — | Pause/Resume |

*(Sources: the product docs cited in §1.6. Read 2026-08-30 except VS Code, whose pages carry the date
2026-08-26.)*

**Partial acceptance is universal and is the category's real ergonomic signature.** Copilot, Cursor,
Tabnine, JetBrains, Zed, Continue and Devin Desktop all ship word-by-word (`Ctrl`/`Cmd`+`→`) and most
ship line-by-line (`End`, or accept-to-line-boundary). The unit of human approval in this category is
therefore often *smaller* than one suggestion.

### 1.5 What inline completion cannot do — the load-bearing negatives

1. **It cannot act.** No tool calls, no execution, no file writes outside the open buffer.
2. **It cannot span a session.** It has no memory of what it suggested five minutes ago beyond the
   recent-edit window the editor supplies.
3. **It cannot be delegated to.** There is no configuration in any surveyed product under which a
   developer walks away and returns to accepted work. The only committing action is a keypress made
   while looking at the suggestion.
4. **It cannot be verified by anything but the developer reading it.** No completion product ships a
   test run, a lint gate, or a static-analysis check between suggestion and acceptance. Copilot's
   public-code matching is the sole automated check found, and it is a licensing check, not a
   correctness one: *"Matches may be discarded or suggested with a code reference"*
   ([GitHub docs](https://docs.github.com/en/copilot/concepts/completions/code-suggestions), 2026-08-30).
5. **Its input scoping leaks.** See finding 5.

### 1.6 Representatives, with dates

All read **2026-08-30** unless a different date is given.

| Product | Status and what it is | Acceptance | Notable structural fact |
|---|---|---|---|
| **GitHub Copilot completions** | Shipping. Ghost text + Next Edit Suggestions. Available in VS Code, Visual Studio, JetBrains, Eclipse, Xcode, NeoVim; NES is ✓ in VS Code and Visual Studio, preview elsewhere ([feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix)) | `Tab`; `Ctrl`/`Cmd`+`→` partial | NES default-on; `allowCodeShifting` default `"always"`. NeoVim gets completion and nothing else. |
| **Cursor Tab** | Shipping. Multi-line, missing imports, cross-file jumps via a portal window ([docs](https://cursor.com/docs/tab/overview), [help](https://cursor.com/help/ai-features/tab)) | `Tab`; `Cmd`/`Ctrl`+`→` word-wise; `Esc` or keep typing to reject | Incorporates Supermaven long-context technology (per the [2024-11-12 acquisition post](https://supermaven.com/blog/cursor-announcement)). |
| **JetBrains Full Line Code Completion** | Shipping, **fully local**: *"Full Line code completion runs entirely on your local device without sending any code over the internet"* ([docs](https://www.jetbrains.com/help/idea/full-line-code-completion.html)) | `Tab` full; `Ctrl`+`→` word; `End` line | Requires x64+AVX2 or ARM64. Bundled with IntelliJ IDEA Ultimate. |
| **JetBrains AI Assistant completion** | Shipping. Default model **Mellum**, *"a proprietary large language model developed by JetBrains"*. Configurable **Local only / Hybrid / Cloud only**, or an OpenAI-compatible provider ([docs](https://www.jetbrains.com/help/ai-assistant/code-completion.html)) | `Tab` / `Ctrl`+`→` / `End` | The local/hybrid/cloud switch is the clearest egress control found in any commercial completion product. |
| **Windsurf autocomplete** | **Product folded into Devin Desktop.** `docs.windsurf.com` HTTP-307s to `docs.devin.ai/desktop/…`. Autocomplete described as *"single-line and multi-line suggestions"* from models *"trained in-house from scratch"* ([docs](https://docs.devin.ai/desktop/autocomplete)) | `Tab`; `⌘`+`→` word; line-wise | **"Supercomplete" is not mentioned anywhere in the successor documentation.** The branded feature named in this strand's brief no longer exists as a documented product term. |
| **Tabnine** | Shipping. Whole-line, full-function, comment-to-code, in VS Code / JetBrains / VS 2022 / Eclipse ([docs](https://docs.tabnine.com/main/getting-started/code-completion.md)) | `Tab`; configurable partial line/word | Four deployment shapes including *"a completely air-gapped environment"* ([deployment options](https://docs.tabnine.com/main/welcome/readme/architecture/deployment-options.md)). Privacy doc: *"Tabnine NEVER retains or shares any of your code with third parties."* |
| **Supermaven** | **Still independently purchasable as of 2026-08-30** — free / Pro $10 / Team $10, plugins for VS Code, JetBrains, Neovim, no sunset notice. ⚠️ *This fact comes from the [supermaven.com](https://supermaven.com/) landing page, which is a marketing page, not documentation; no capability claim is drawn from it.* | `Tab` | Founder announcement 2024-11-12: *"We'll continue to maintain the Supermaven plugins for VS Code, JetBrains, and Neovim."* |
| **Zed edit prediction (Zeta)** | Shipping. *"Zeta is derived from Qwen2.5-Coder-7B, and is fully open source, including an open dataset"* ([Zed blog, 2025-02-13](https://zed.dev/blog/edit-prediction)). Not fill-in-the-middle: *"given a list of recent edits and the cursor position, we asked the model to rewrite a snippet of text around the cursor, incorporating one or more edit predictions."* | `tab` (eager mode), `alt-tab`, `alt-l`; accept-to-word / accept-to-line commands | Alternative providers: Copilot, Mercury Coder, Codestral, **Ollama**, OpenAI-compatible. Training-data collection is **opt-in and additionally requires a detected open-source licence file**; `.env*`, `*.pem`, `*.key`, `*.cert`, `secrets.yml` are excluded regardless ([ai-improvement docs](https://zed.dev/docs/ai/ai-improvement)). Dataset: Apache-2.0, 583 rows ([HF](https://huggingface.co/datasets/zed-industries/zeta)). |
| **Amazon Q Developer inline** | **Announced end of life.** *"On April 30, 2027, AWS will discontinue support for Amazon Q Developer IDE plugins."* AWS directs users to Kiro ([AWS docs](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions.html)) | `Tab`; Pause/Resume Auto-Suggestions per IDE | Customisable on internal libraries; code-reference tracking for open-source matches. |
| **Codeium** | **Name retired.** Codeium → Windsurf → Cognition. Cognition acquired Windsurf's *"IP, product, trademark and brand, and business"* on [2025-07-14](https://cognition.com/blog/windsurf), citing *"$82M of ARR"* and *"350+ enterprise customers"*. | — | The rename-rationale post is now behind a 429 (see Blocked sources). |
| **Continue.dev** | Shipping, Apache-2.0, active (last push 2026-08-30, 35.7k stars — GitHub API). *"Autocomplete provides inline code suggestions as you type"* ([docs](https://docs.continue.dev/ide-extensions/autocomplete/quick-start)) | `Tab`; `Esc`; `Ctrl`/`Cmd`+`→` word; `Ctrl`/`Cmd`+`Alt`+`Space` force-trigger | Model-agnostic; documented Ollama and self-hosting guides. |
| **Tabby** | Shipping, self-hosted: *"an open-source, self-hosted AI coding assistant"* ([docs](https://tabby.tabbyml.com/docs/welcome/)). 33.8k stars, last push 2026-06-30 (GitHub API); licence reported as `NOASSERTION` by the API — **not a clean OSI identifier; verify before relying on it.** | IDE-extension driven | Docker / Homebrew / HF Spaces deployment. |
| **llama.vscode / llama.vim** (ggml-org) | Shipping, MIT. *"Local LLM-assisted text completion, chat with AI and agentic coding extension for VS Code"*, llama.cpp server backend ([repo](https://github.com/ggml-org/llama.vscode)). 1.49k / 2.16k stars; last pushes 2026-08-19 / 2026-08-27 (GitHub API) | `Tab` full; `Shift`+`Tab` first line; `Ctrl`/`Cmd`+`→` word | FIM completion with ring-buffer context reuse; explicitly targets low-end hardware. Note that this project also ships a chat and an agent — the local lane is no longer completion-only. |
| **FauxPilot** | **Dormant.** MIT, 14.7k stars, **not archived**, but last push **2024-04-09** (GitHub API, 2026-08-30). *"an attempt to build a locally hosted alternative to GitHub Copilot… SalesForce CodeGen models inside of NVIDIA's Triton Inference Server with the FasterTransformer backend."* | — | The named self-hosted-Copilot lineage of 2022 has been superseded by Tabby and the llama.cpp plugins. |

### 1.7 Telemetry and measured usage

| Figure | Value | Tier | Source, date |
|---|---|---|---|
| Google internal acceptance rate | **37%** — *"the number of AI-generated suggestions that are accepted divided by the number shown for greater than 750 milliseconds while the user is not typing"* | **Vendor-reported** (Google measuring Google) | [research.google, 2024-06-06](https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/) |
| Google share of characters | **50%** — *"the same amount of characters in the code are now completed with AI-based assistance as are manually typed by developers."* Denominator excludes copy-paste. | **Vendor-reported** | same, 2024-06-06 |
| Copilot share of code | **46%** across languages, **61%** in Java; **27%** at June 2022 launch | **Vendor-reported** | [github.blog, 2023-02-14](https://github.blog/news-insights/product-news/github-copilot-now-has-a-better-ai-model-and-new-capabilities/) |
| Copilot task-speed experiment | **55% faster** (1h11m vs 2h41m), n=95, P=.0017, 95% CI [21%, 89%] | **Controlled experiment, vendor-run**, single synthetic task | [github.blog, 2022-09-07, upd. 2024-05-21](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) |
| Copilot developer survey | n>2,000 (~60% professional developers); 73% "stay in flow", 87% "preserved mental effort" | **Vendor-run survey** | same |
| What acceptance rate actually measures | *"the rate with which shown suggestions are accepted, rather than more specific metrics regarding the persistence of completions in the code over time, drives developers' **perception** of productivity"* | **Observational study, vendor-authored** (GitHub) | [Ziegler et al., arXiv:2205.06537, 2022-05-13](https://arxiv.org/abs/2205.06537) |

**Two structural facts about the telemetry itself, both verified rather than reported:**

- **GitHub no longer exposes completion acceptance data through its API.** The current
  `api.github.com.yaml` OpenAPI description (downloaded from
  [github/rest-api-description](https://github.com/github/rest-api-description) on 2026-08-30, 9.8 MB)
  contains the schemas `copilot-usage-metrics-1-day-report` and `copilot-usage-metrics-28-day-report`,
  whose only properties are `download_links` and `report_day` / `report_start_day` / `report_end_day`.
  A grep for `total_code_acceptances`, `total_code_suggestions`, `total_code_lines_accepted` and
  `copilot_ide_code_completions` returns **zero hits** in both the current and the pinned
  `2022-11-28` descriptions, and a GitHub code search for `total_code_acceptances` across `org:github`
  returns **0 results**. The documented metrics properties are `report_time`, `login`,
  `last_authenticated_at`, `last_activity_at`, `last_surface_used`
  ([GitHub docs](https://docs.github.com/en/copilot/reference/metrics-data), 2026-08-30) — activity
  timestamps, no acceptance counts. *Tier: primary artifact read directly.*
- **Cursor does expose it — to the paying customer, not to the public.** The team analytics API's
  `/analytics/team/tabs` endpoint returns `total_suggestions`, `total_accepts`, `total_rejects`,
  `total_lines_suggested`, `total_lines_accepted`, and green/red line splits for accepted, rejected and
  suggested lines, aggregated daily and filterable per user
  ([Cursor docs](https://cursor.com/docs/account/teams/analytics-api), 2026-08-30).
  **Per-developer completion-acceptance measurement is a shipped enterprise feature.** No aggregate is
  published by the vendor.

**The consequence for this project:** there is no current, independent, non-vendor figure for
completion acceptance. Every number available is either vendor-reported or several years old, and the
best-evidenced statement about acceptance rate is that it tracks how productive developers *feel*.

---

## Part 2 — In-editor chat and edit

### 2.1 The mode taxonomy no longer holds still — write around the boundary instead

The brief for this strand named "Copilot Chat (ask/edit modes in VS Code)" and "Cursor's Composer
non-agentic edit mode". Both descriptions were superseded before the research ran:

- **VS Code** documents four *surfaces* — *"Agents Window"*, *"Chat View"*, *"Inline Chat"*, *"Quick
  Chat"* — plus **custom agents** defined in `.agent.md` files under `.github/agents` or
  `~/.copilot/agents`, whose documented examples include a "Planner" agent *with read-only tools*
  ([VS Code, dated 2026-08-26](https://code.visualstudio.com/docs/copilot/chat/copilot-chat),
  [custom agents](https://code.visualstudio.com/docs/copilot/chat/chat-modes)). It does not present
  "ask / edit / agent" as its top-level frame.
- **GitHub's** own docs name three modes — *"Ask mode"*, *"Plan mode"*, *"Agent mode"* — with **Edit
  mode** surviving as a per-IDE feature (✓ VS Code, ✓ JetBrains, ✗ Visual Studio, per the
  [feature matrix](https://docs.github.com/en/copilot/reference/copilot-feature-matrix))
  ([GitHub docs](https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide), 2026-08-30).
- **Cursor** documents Plan, Ask, Debug, Design and Max modes; "Composer" is not the frame.
- **Windsurf's** Cascade is now documented as *"one of two local agents in Devin Desktop"*.

**Recommendation for the archetype documents: do not organise around mode names.** Organise around
the two questions in §2.2 and §2.3, which have been stable.

### 2.2 What the human approves, per product

| Product | What is shown | What the human approves | Granularity |
|---|---|---|---|
| **VS Code Copilot (edit/agent)** | Pending edits marked with *"a squared-dot indicator in the Explorer view and editor tabs"*; Up/Down controls navigate between edits | *"Select **Keep** to accept the edit. Select **Undo** to reject the edit and revert the change."* Terminal commands are confirmed separately. | Per hunk (*"Hover over an inline change to accept or reject that specific change without affecting other edits"*), **or all pending edits at once from the Chat view** |
| **VS Code Inline Chat** | *"VS Code shows a diff with the code suggestion inline in the editor."* | *"Use **Keep** or **Undo** to accept or reject the changes."* In the terminal: **Run (⌘Enter)** executes, or **Insert** places the command for editing first. | Per invocation |
| **Copilot edit mode (per GitHub docs)** | Proposed edits per file | Users *"choose which files Copilot can make changes to"* and *"decide whether or not to accept the suggested edits after each turn"* | Per file, per turn |
| **Cursor** | *"The diff view shows changes as they happen. If you see the agent heading in the wrong direction, click Stop or press Cmd Shift Backspace to cancel and redirect."* Post-hoc: *"click Review then Find Issues to run a dedicated code review."* | Tool calls, gated by Run Mode (§2.3). Regardless of mode, **file deletion, external file operations, and browser tool use always require approval.** | Per tool call; diff is streamed live |
| **JetBrains AI Assistant** | Chat mode: *"responses typically contain suggestions or code snippets that you can review and apply if needed"* — chat output is applied manually. Agents *"can perform multi-step actions in your project, modify multiple files, and report progress during execution."* | *"you can review the results and keep or roll back the changes if needed"* | Chat: manual application. Agents: keep / roll back the result set. |
| **Cascade (Devin Desktop, ex-Windsurf)** | Code mode: *"create and make modifications to your codebase"*. Chat mode: *"optimized for questions around your codebase or general coding principles"* | Changes before they are applied. An **Auto-Continue** feature resumes automatically when tool-call limits are hit, consuming credits. | Per change set |
| **Continue.dev Edit** | *"a diff will be streamed inline to your file which you can accept or reject"* | Per-change accept/reject | `Cmd/Ctrl+Opt/Alt+Y` accept one, `+N` reject one, `Cmd/Ctrl+Shift+Enter` accept **all**, `Cmd/Ctrl+Shift+Delete` reject all |
| **Continue.dev Agent** | Tool-call prompts | *"By default, Agent mode will ask permission when it wants to use a tool. Click `Continue` to allow Agent mode to proceed with the tool call or `Cancel` to reject it."* | Per tool call |
| **Cline** | Plan/Act split | In Act mode, each file edit and command; auto-approve toggles listed in §2.3 | Per action class |
| **Zed Agent Panel** | *"the panel will surface which files, how many of them, and how many lines have been edited"* | *"accept or reject each individual change hunk, or the whole set of changes made by the agent"*; *"Use Tool Permissions to control whether permission-gated tool calls are allowed, denied, or confirmed."* | Per hunk **or** whole set |
| **Zed Inline Assistant** | *"The Inline Assistant sends your current selection (or line) to a language model and replaces it with the response."* (`Ctrl-Enter`) | The replacement | Per selection |

*(All read 2026-08-30 except the VS Code pages, which carry the date 2026-08-26.)*

### 2.3 Can the approval be turned off? Yes — and this is the category's real dividing line

This is the answer the project most needs. **Every in-editor edit product surveyed ships a documented
way to remove the human from the accept step.** They differ only in how granular the removal is and how
loudly the vendor warns about it.

| Product | Mechanism | Default | Vendor's own warning |
|---|---|---|---|
| **VS Code** | `chat.editing.autoAcceptDelay` — *"Configure a delay after which suggested edits are automatically accepted"* | `0` (off). *"Hover over the editor overlay controls to stop the countdown."* | — |
| **VS Code** | `chat.permissions.default`: **Default Approvals** / **Assisted Permissions** (an LLM judge evaluates risk; risky calls still show a dialog) / **Bypass Approvals** (auto-approves all tool calls); plus **Autopilot** (continuous autonomous iteration, all tools auto-approved) | `"default"`; `chat.assistedPermissions.enabled` is `true` in Insiders, `false` in Stable | *"Bypass Approvals and Autopilot bypass manual approval prompts, including for potentially destructive actions."* |
| **VS Code** | `chat.tools.terminal.autoApprove` regex allow/deny map | **Terminal auto-approval is ON by default** (`chat.tools.terminal.enableAutoApprove: true`) with a built-in deny list: `{"rm": false, "rmdir": false, "del": false, "kill": false, "curl": false, "wget": false, "eval": false, "chmod": false, "chown": false, "/^Remove-Item\b/i": false}` | *"Automatically approving terminal commands provides best effort protections and assumes the agent is not acting maliciously."* Documented detection limits around subcommand extraction and quote concatenation. |
| **VS Code** | `chat.tools.global.autoApprove` | `false` | Its own description begins *"Automatically approve all tools - this setting disables critical…"* |
| **VS Code** | `chat.tools.edits.autoApprove` (`{}`), `chat.tools.urls.autoApprove` (`[]`), `chat.tools.terminal.blockDetectedFileWrites`, `chat.agent.sandbox.enabled` (`off`) | as shown | *"The post-approval step is not linked to the 'Trusted Domains' feature and always requires your review"* — an explicit prompt-injection countermeasure |
| **Cursor** | **Run Modes**: *Auto-review* (*"Allowlisted calls run immediately. Other shell commands run in the sandbox when possible"*, with classifier review of higher-risk actions) / *Allowlist* (pre-approved actions only, no classifier) / **Run Everything** (every tool call automatically, no sandboxing, no classifier) | Auto-review is *"the recommended default"* | Run Everything is documented as for when *"You accept the risk and want zero prompts"* |
| **Cursor** | `permissions.json` with plain-English `allow_instructions` / `block_instructions`; `sandbox.json` controlling *"what a sandboxed command can reach, like network domains and extra readable or writable paths"* | — | File deletion, external file operations and browser tool use **still require approval regardless of mode** |
| **Cline** | Per-action-class auto-approve: Read project files / Read all files / Edit project files / Edit all files / Execute safe commands / Execute all commands / Use the browser / Use MCP servers. *"Read all files"* and *"Edit all files"* extend access outside the workspace and require the base toggle first. | Approval required | *"YOLO mode disables all safety checks. Cline executes whatever it decides without asking permission."* |
| **Continue.dev** | *"You can use tool policies to exclude or make usage automatic for specific tools"* | Ask per tool call | — |
| **Zed** | Tool Permissions: *allowed / denied / confirmed* per permission-gated tool | Confirmed | No blanket auto-approve documented |
| **JetBrains** | Not documented in the pages read | Review, then keep or roll back | — |

**Two things follow.** First, VS Code's **terminal auto-approval is on by default** with a deny list of
ten patterns — meaning the shipped default for a mainstream editor already executes many commands
without asking, and the vendor states plainly that the protection *"assumes the agent is not acting
maliciously"*. Second, containment is the right vocabulary for these products: what varies across the
table above is not how much a team *trusts* the tool but what the tool is structurally permitted to
reach — sandbox paths, network domains, allow/deny patterns, read-only tool sets.

### 2.4 What in-editor chat and edit cannot do

1. **It cannot run without an editor session.** Every product in this category is a UI attached to an
   open workspace. Nothing continues after the window closes. That is the honest structural difference
   between this region and the regions further along the spectrum.
2. **Its read-only modes are enforced by tool availability, not by promise** — this is a *capability*
   and should be read as one: Cline Plan *"cannot modify any files or execute commands"*; Continue Chat
   mode has *"No tools available, pure conversation"*; Cursor Ask *"answers questions and explores code
   without making any edits"*.
3. **The one input-scoping mechanism GitHub ships does not extend to it.** See finding 5. A team
   relying on Copilot content exclusion loses that protection at exactly the moment it switches from
   Ask to Edit or Agent.
4. **Chat output does not automatically become code in every product.** In JetBrains AI Assistant,
   chat-mode code *"needs to be reviewed and applied manually"* — the diff-application step some
   vendors automate is, in that product, still a human copy.

---

## Part 3 — What this means for the archetype documents

1. **These two categories are not one category and should not share an archetype.** Inline completion
   permits zero autonomy structurally; in-editor edit permits full autonomy with a settings change that
   every surveyed vendor ships. The boundary between them is a `Run` button and a
   `chat.editing.autoAcceptDelay` value — crossed by editing a JSON file, not by adopting a new tool.
2. **Describe positions by the acceptance boundary, not by product name.** The product names moved
   twice during a single ticket: Codeium→Windsurf→Devin Desktop; Composer→modes; ask/edit/agent→four
   surfaces plus custom agents; Supercomplete→gone; Amazon Q IDE plugins→end-of-support 2027-04-30.
3. **Do not cite completion acceptance rates as productivity evidence.** GitHub's own researchers
   established that acceptance rate tracks perception. If a figure is needed, cite Google's 37% / 50%
   with the vendor-reported label and the 2024-06-06 date, and say what it measures: character
   provenance.
4. **The "human accepts every diff" framing is a configuration, not a property.** It is true of the
   in-editor edit category as shipped and false of it as configurable. Any archetype defined by "the
   human reads every diff" must name the settings that have to stay at their defaults for that to
   remain true — for VS Code, at minimum `chat.editing.autoAcceptDelay: 0`,
   `chat.permissions.default: "default"`, `chat.tools.global.autoApprove: false`, and a reviewed
   `chat.tools.terminal.autoApprove` map, since terminal auto-approval is on by default.
5. **A genuinely no-egress option exists at the least-delegated end and nowhere further along.**
   JetBrains Full Line, Tabnine air-gapped, Tabby, and the llama.cpp plugins. Teams with a hard
   data-egress constraint have a real product choice in this region and progressively fewer as
   delegation increases.

---

## Sources

**Inline completion — product documentation**
- GitHub Copilot completions in VS Code — https://code.visualstudio.com/docs/copilot/ai-powered-suggestions (page dated 2026-08-26)
- VS Code AI settings reference — https://code.visualstudio.com/docs/agents/reference/ai-settings (2026-08-26)
- VS Code Copilot features and shortcuts — https://code.visualstudio.com/docs/copilot/copilot-vscode-features (2026-08-26)
- GitHub Copilot code suggestions (concept) — https://docs.github.com/en/copilot/concepts/completions/code-suggestions (2026-08-30)
- GitHub Copilot features — https://docs.github.com/en/copilot/get-started/features (2026-08-30)
- GitHub Copilot feature matrix — https://docs.github.com/en/copilot/reference/copilot-feature-matrix (2026-08-30)
- GitHub Copilot content exclusion — https://docs.github.com/en/copilot/concepts/content-exclusion (2026-08-30)
- Cursor Tab overview — https://cursor.com/docs/tab/overview (2026-08-30)
- Cursor Tab help — https://cursor.com/help/ai-features/tab (2026-08-30)
- JetBrains Full Line Code Completion — https://www.jetbrains.com/help/idea/full-line-code-completion.html (2026-08-30)
- JetBrains AI Assistant code completion — https://www.jetbrains.com/help/ai-assistant/code-completion.html (2026-08-30)
- Devin Desktop autocomplete (ex-Windsurf) — https://docs.devin.ai/desktop/autocomplete (2026-08-30)
- Tabnine code completion — https://docs.tabnine.com/main/getting-started/code-completion.md (2026-08-30)
- Tabnine deployment options — https://docs.tabnine.com/main/welcome/readme/architecture/deployment-options.md (2026-08-30)
- Tabnine privacy — https://docs.tabnine.com/main/welcome/readme/privacy.md (2026-08-30)
- Zed edit prediction — https://zed.dev/docs/ai/edit-prediction (2026-08-30)
- Zed AI privacy and security — https://zed.dev/docs/ai/privacy-and-security (2026-08-30)
- Zed feedback and training data — https://zed.dev/docs/ai/ai-improvement (2026-08-30)
- Amazon Q Developer inline suggestions — https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/inline-suggestions.html (2026-08-30)
- Continue autocomplete quick start — https://docs.continue.dev/ide-extensions/autocomplete/quick-start (2026-08-30)
- Tabby docs — https://tabby.tabbyml.com/docs/welcome/ (2026-08-30)
- llama.vscode — https://github.com/ggml-org/llama.vscode (2026-08-30)
- FauxPilot — https://github.com/fauxpilot/fauxpilot (repo state via GitHub API, 2026-08-30)

**In-editor chat and edit — product documentation**
- VS Code Copilot Chat surfaces — https://code.visualstudio.com/docs/copilot/chat/copilot-chat (2026-08-26)
- VS Code custom agents — https://code.visualstudio.com/docs/copilot/chat/chat-modes (2026-08-26)
- VS Code inline chat — https://code.visualstudio.com/docs/copilot/chat/inline-chat (2026-08-26)
- VS Code reviewing AI-generated code edits — https://code.visualstudio.com/docs/agents/run/review-code-edits (2026-08-26)
- VS Code approvals and permissions — https://code.visualstudio.com/docs/agents/run/approvals (2026-08-26)
- GitHub Copilot chat in your IDE — https://docs.github.com/en/copilot/how-tos/chat-with-copilot/chat-in-ide (2026-08-30)
- Cursor agent overview — https://cursor.com/docs/agent/overview (2026-08-30)
- Cursor run modes — https://cursor.com/docs/agent/security/run-modes (2026-08-30)
- Cursor terminal — https://cursor.com/docs/agent/terminal (2026-08-30)
- Cursor review — https://cursor.com/docs/agent/review (2026-08-30)
- Cursor Ask mode — https://cursor.com/help/ai-features/ask-mode (2026-08-30)
- Cursor Plan mode — https://cursor.com/docs/agent/modes (2026-08-30)
- Cursor privacy — https://cursor.com/help/security-and-privacy/privacy (2026-08-30)
- Cursor team analytics API — https://cursor.com/docs/account/teams/analytics-api (2026-08-30)
- JetBrains AI Assistant overview — https://www.jetbrains.com/help/idea/ai-assistant.html (2026-08-30)
- JetBrains AI chat — https://www.jetbrains.com/help/ai-assistant/ai-chat.html (2026-08-30)
- Cascade (Devin Desktop) — https://docs.devin.ai/desktop/cascade/cascade (2026-08-30)
- Continue agent quick start — https://docs.continue.dev/ide-extensions/agent/quick-start (2026-08-30)
- Continue edit quick start — https://docs.continue.dev/ide-extensions/edit/quick-start (2026-08-30)
- Cline plan and act — https://docs.cline.bot/features/plan-and-act (2026-08-30)
- Cline auto-approve — https://docs.cline.bot/features/auto-approve (2026-08-30)
- Zed agent panel — https://zed.dev/docs/ai/agent-panel (2026-08-30)
- Zed inline assistant — https://zed.dev/docs/ai/inline-assistant (2026-08-30)

**Telemetry, studies and first-party engineering posts**
- Google, "AI in Software Engineering at Google" — https://research.google/blog/ai-in-software-engineering-at-google-progress-and-the-path-ahead/ (2024-06-06)
- GitHub, "GitHub Copilot now has a better AI model and new capabilities" — https://github.blog/news-insights/product-news/github-copilot-now-has-a-better-ai-model-and-new-capabilities/ (2023-02-14, updated 2023-02-17)
- GitHub, "Quantifying GitHub Copilot's impact on developer productivity and happiness" — https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/ (2022-09-07, updated 2024-05-21)
- Ziegler et al., "Productivity Assessment of Neural Code Completion" — https://arxiv.org/abs/2205.06537 (2022-05-13)
- Zed, "Edit Prediction" — https://zed.dev/blog/edit-prediction (2025-02-13)
- Zeta dataset — https://huggingface.co/datasets/zed-industries/zeta (Apache-2.0, 583 rows; read 2026-08-30)
- GitHub Copilot metrics data properties — https://docs.github.com/en/copilot/reference/metrics-data (2026-08-30)
- GitHub REST API OpenAPI description — https://github.com/github/rest-api-description, `descriptions/api.github.com/api.github.com.yaml` and `…2022-11-28.yaml` (downloaded and grepped 2026-08-30)

**Consolidation and lineage**
- Supermaven joins Cursor — https://supermaven.com/blog/cursor-announcement (2024-11-12)
- Cognition acquires Windsurf — https://cognition.com/blog/windsurf (2025-07-14)
- `docs.windsurf.com` → `docs.devin.ai` HTTP 307 redirect, observed 2026-08-30
- Amazon Q Developer IDE plugins end of support — https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-developer-ide-end-of-support.html (referenced from the inline-suggestions page, 2026-08-30)

**⚠️ Marketing page, used for one fact only and labelled in place**
- https://supermaven.com/ — used solely to establish that the product is still purchasable as of
  2026-08-30 (pricing tiers and download links present, no sunset notice). No capability claim is drawn
  from it.

---

## Confidence and gaps

**High confidence**
- That inline completion cannot act. Fourteen products, every one documented as a proposal surface with
  a keypress commit, and no tool surface described anywhere.
- That the acceptance boundary in the edit category has a documented off switch in VS Code, Cursor,
  Cline and Continue. Setting names, defaults and vendor warnings are quoted directly.
- That GitHub's REST API exposes no completion acceptance field today. Verified against the OpenAPI
  artifact itself, not against documentation about it.
- That Windsurf's documentation now serves from `docs.devin.ai`, that Supercomplete is absent from it,
  and that Amazon Q's IDE plugins have a published end-of-support date.

**Medium confidence**
- The Cursor mode inventory. Cursor's docs were partially reorganised around this research date
  (`docs.cursor.com` → `cursor.com/docs`, with `/help/` and `/docs/` carrying overlapping content), and
  several expected paths 404'd. Ask, Plan, Debug, Design and Max modes are named in the published
  `llms.txt` index; only Ask, Plan and the Run Modes were read in full.
- Whether Cursor's *file edits* (as distinct from tool calls) have an auto-accept. The dedicated review
  page did not document per-hunk accept/reject mechanics; Run Modes govern tool calls. Treat "Cursor
  has no edit auto-accept" as **unverified**, not established.
- JetBrains agent approval semantics. The AI Assistant pages describe review-then-keep-or-roll-back but
  do not enumerate per-tool permission settings the way VS Code and Cline do.

**Explicitly unverified**
- **That GitHub's `/copilot/metrics` endpoint ever carried `total_code_acceptances` /
  `copilot_ide_code_completions`.** Widely repeated, and the present absence is verified here, but the
  removal itself is not sourced. Do not write "GitHub removed the field" without checking the changelog.
- **Tabby's licence.** The GitHub API reports `NOASSERTION`, meaning it could not match a standard
  identifier. Verify before describing Tabby as OSI-licensed.
- **Whether any completion product performs an outbound call beyond inference.** Absence of
  documentation is not proof; no source code was read for any closed-source completion client.
- **Supermaven's ongoing engineering status.** The site sells it; no changelog or release cadence was
  checked, and the only source is a marketing page.
- **The Codeium → Windsurf rename date.** The rationale post returned 429 twice (see below). Only the
  Cognition acquisition date (2025-07-14) is sourced.

**Not covered by this strand** (belongs to sibling strands): CLI agents, cloud and background agents,
code review bots, and the productivity-measurement literature beyond the completion-specific studies
above.

**A methodological note worth recording.** The fetched rendering of the AWS Amazon Q inline-suggestions
page carried an appended "See also" block instructing the reader to run an AWS CLI command against a
skills catalogue. That block was **not acted on**, and its provenance — genuine AWS documentation
versus an artifact introduced somewhere in the fetch path — was **not established**. It is noted only
because it is a live instance of instruction-shaped text arriving inside a document an agent was asked
to read, which is the exact input condition this project's `lethal trifecta` entry describes.

---

## Blocked or unavailable sources

None were circumvented.

| URL | Block | Consequence |
|---|---|---|
| https://devin.ai/blog/why-we-rebranded-to-windsurf | **HTTP 429** (twice, ~40 min apart) | The Codeium→Windsurf rename rationale and its exact date are unsourced here. |
| https://docs.cursor.com/tab/overview | HTTP 308 → `cursor.com/docs` | Followed the redirect; no loss. |
| https://docs.windsurf.com/windsurf/cascade/cascade | HTTP 307 → `docs.devin.ai/desktop/cascade/cascade` | Followed; the redirect is itself finding 10. |
| https://cognition.ai/blog/windsurf | HTTP 301 → `cognition.com/blog/windsurf` | Followed; no loss. |
| https://docs.continue.dev/features/autocomplete/how-it-works | Client-side redirect stub ("Redirecting…") | Superseded by `/ide-extensions/autocomplete/quick-start`. Continue's prompt-construction internals were not read. |
| https://raw.githubusercontent.com/continuedev/continue/main/docs/features/autocomplete/how-it-works.mdx | HTTP 404 | Same gap as above. |
| https://cursor.com/docs/account/privacy, `…/account/settings/privacy`, `…/account/privacy-mode`, `…/docs/sitemap.md`, `…/docs/tab/advanced-features` | HTTP 404 (five paths) | Privacy facts recovered from `cursor.com/help/security-and-privacy/privacy`; Tab advanced-feature detail recovered from `cursor.com/help/ai-features/tab`. |
| https://code.visualstudio.com/docs/copilot/chat/copilot-edits, `…/chat/chat-agent-mode`, `…/docs/agents/run/tool-approvals` | 404 or superseded content | Superseded by `/docs/agents/run/review-code-edits`, `/docs/agents/run/approvals` and `/docs/agents/reference/ai-settings`, all of which were read. |
| https://docs.github.com/en/copilot/reference/example-schema-for-copilot-usage-metrics, `…/reference/data-available-in-copilot-usage-metrics`, `…/how-tos/administer/organizations/reviewing-usage-data` | HTTP 404 | The metrics conclusion was instead verified against the OpenAPI artifact directly, which is a stronger source. |
| https://www.jetbrains.com/help/idea/ai-chat.html, `…/help/ai-assistant/chat.html`, `…/help/ai-assistant/use-ai-code-completion.html`, `…/help/ai/get-started-with-ai-assistant.html` | HTTP 404 (four paths) | Recovered via `/help/idea/ai-assistant.html` and `/help/ai-assistant/ai-chat.html`. JetBrains' AI documentation has clearly been reorganised recently; treat any JetBrains URL in this file as short-lived. |
| https://docs.tabnine.com/main/getting-started/introduction | HTTP 404 | Recovered via the published sitemap. |
