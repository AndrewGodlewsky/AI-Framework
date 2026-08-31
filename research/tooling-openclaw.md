# OpenClaw: the far-end anchor, examined

**Research date:** 2026-08-30
**Ticket:** [#6 Tooling Landscape](https://github.com/AndrewGodlewsky/AI-Framework/issues/6) — strand: OpenClaw, the far-end anchor
**Question:** What is OpenClaw, what was it built for, what is it actually used for — and does anyone use it, or anything like it, to push code to production without human verification?

**Method.** Project-first. The repository README, `VISION.md`, `SECURITY.md`, the docs source under
`docs/` in the repo, the project's own blog, its GitHub Security Advisory database read through the
REST API, its plugin/skill registry read through its public JSON API, and the source code of the one
tool that writes to a repository. Third-party security research and press are read only after that,
and are labelled as such. The project's prior finding that **the press consistently reports nuanced
policies as flat bans** was applied here too, and it paid off twice: see §7.3 and §7.4.

**Evidence tier is stated inline with every claim**, using: `[first-party docs]`, `[first-party
source code]`, `[first-party blog]`, `[security advisory]`, `[third-party security research]`,
`[academic]`, `[press]`, `[practitioner anecdote]`.

---

## 0. Verdict up front

**No. OpenClaw is not a production-delivery tool, and I found no evidence that anyone ships code to
production through it without human verification.**

The strongest statement of this is the project's own. Its FAQ answers the question directly:

> "OpenClaw is an **assistant and coordination layer**, not an IDE replacement. Use Claude Code or
> Codex for the fastest direct coding loop inside a repo. Use OpenClaw for durable memory,
> cross-device access, and tool orchestration."
> — [`docs/help/faq.md`](https://github.com/openclaw/openclaw/blob/main/docs/help/faq.md), read 2026-08-30 `[first-party docs]`

The mechanical evidence agrees with the positioning:

1. **The only built-in tool that writes to a repository creates a *draft pull request*, and "draft"
   is hardcoded.** `github_publish` is the sole repository-write tool in OpenClaw's tool surface. Its
   own description: *"the Gateway commits, pushes through an exact HTTPS path, and creates or reuses
   a **draft** pull request."* In the executor, the GitHub API call is made with `draft: true` as a
   literal, not a parameter.
   ([`src/agents/tools/github-publish-tool.ts`](https://github.com/openclaw/openclaw/blob/main/src/agents/tools/github-publish-tool.ts),
   [`src/gateway/github-publication-executor.ts:529`](https://github.com/openclaw/openclaw/blob/main/src/gateway/github-publication-executor.ts), read 2026-08-30) `[first-party source code]`
   There is no merge tool, no deploy tool, no release tool, and no CI-trigger tool anywhere in
   `src/agents/tools/` (full listing read 2026-08-30) `[first-party source code]`.

2. **The ecosystem is not a software-delivery ecosystem.** Across **1,198 skills** enumerated from
   the ClawHub public API on 2026-08-30, the phrase "pull request" appears in **2**, "github action"
   in **1**, "terraform" in **1**, "ci/cd" in **8**, "code review" in **7**. The most common topics
   are Health, Home, Self Improving, Smart Home, finance and email
   (`https://clawhub.ai/api/v1/skills`, paginated 2026-08-30) `[first-party docs]`. Every one of the
   delivery-adjacent skills that does exist is a *review* or *PR-opening* skill — the top hit,
   `code-workflow`, is a "4-stage code-change workflow: research → plan → **user review** →
   implement".

3. **The project's own repository automation, which is the most autonomous merge path anywhere in
   the OpenClaw universe, is started by a human typing a command on each individual PR.** ClawSweeper's
   automerge flow begins: *"A maintainer comments `/clawsweeper automerge`."*
   ([`clawsweeper.bot/repair/automerge-flow.html`](https://clawsweeper.bot/repair/automerge-flow.html), read 2026-08-30) `[first-party docs]`
   And the PR-review doc is explicit that the bot is not the gate: *"A positive ClawSweeper result is
   supporting evidence, not maintainer approval. Maintainers still decide whether and when a PR is
   ready to merge."*
   ([`docs/reference/pull-request-review-flow.md`](https://github.com/openclaw/openclaw/blob/main/docs/reference/pull-request-review-flow.md), read 2026-08-30) `[first-party docs]`

4. **Even the adversarial lab study built to make OpenClaw agents act autonomously found they mostly
   did not.** *Agents of Chaos* (arXiv:2602.20021v1, 2026-02-23) gave six OpenClaw agents unrestricted
   shell access including `sudo`, no tool restrictions, and the ability to edit their own operating
   instructions — and reports: *"The majority of agent actions during our experiments were initiated
   by human intervention, and most high-level direction was provided by humans."* `[academic]`

**What this means for the map.** The far end of a *software delivery* spectrum, as the ticket
anticipated, is a **theoretical position rather than an observed practice** — at least as anchored by
OpenClaw. But the finding is sharper than "no evidence found": OpenClaw does not anchor that spectrum
at all. It anchors a **different axis** — how much of a person's *life and credentials* an agent
holds, and on how many untrusted surfaces it is reachable. On that axis it is a genuine and extreme
anchor, and it is the clearest real-world instance of the **lethal trifecta** this project has a name
for. See §8 for the honest assessment and §8.3 for what would anchor a delivery spectrum instead.

**The single most load-bearing fact in this document**, and the one that should survive into any
write-up: **OpenClaw's default posture is no sandbox and no approval gate.** `agents.defaults.sandbox.mode`
defaults to `off` ([`SECURITY.md`](https://github.com/openclaw/openclaw/blob/main/SECURITY.md)), and
the exec docs state plainly: *"**No-approval host exec is the default for gateway and node
(`mode=full`)**"*
([`docs/tools/exec.md`](https://github.com/openclaw/openclaw/blob/main/docs/tools/exec.md), read 2026-08-30) `[first-party docs]`.
An out-of-the-box OpenClaw runs arbitrary shell commands on the operator's host, unsandboxed and
unprompted, driven by a model reachable from WhatsApp.

---

## 1. Headline findings

1. **OpenClaw is a personal-assistant gateway, not a coding agent.** It connects a model to your
   messaging apps and your machine. Its own one-line description: *"an AI assistant that runs on your
   devices and meets you in the channels you already use"*
   ([README](https://github.com/openclaw/openclaw/blob/main/README.md), read 2026-08-30) `[first-party docs]`.

2. **The naming history is Warelay → Clawd/Clawdbot → Molty/Moltbot → OpenClaw, and the trigger was
   an Anthropic trademark request.** `VISION.md` states the chain: *"It evolved through several names
   and shells: Warelay -> Clawdbot -> Moltbot -> OpenClaw."* The lore page dates it: Clawd from
   2025-11-25; **2026-01-27**, "Anthropic sent a polite email asking for a name change (trademark
   stuff)" and the community picked Moltbot at 5am on Discord; **2026-01-30**, the final migration to
   OpenClaw at 4am GMT. The npm package `openclaw` was created 2026-01-29 (registry metadata). `[first-party docs]`

3. **It is enormous, young, and moving fast.** Repository created **2025-11-24**; **388,096 stars**,
   81,483 forks, **30,750 merged PRs**, 3,563 open issues and 2,213 open PRs as of 2026-08-30
   (GitHub REST + GraphQL API). 248 npm versions published since 2026-01-29. `[first-party docs]`

4. **The security record is the largest of any project in this research, by an order of magnitude.**
   **647 published GitHub Security Advisories** — 14 critical, 219 high, 350 medium, 64 low — with 39
   carrying CVE IDs (GitHub Security Advisory API, read 2026-08-30) `[security advisory]`. The
   project's own accounting is larger still and more honest: as of 2026-04-30, *"GitHub shows 1,309
   security advisories since January 10. 535 were published. 746 were closed as invalid"*
   ([blog, 2026-04-30](https://openclaw.ai/blog/openclaw-security-in-public/)) `[first-party blog]`.

5. **Tens of thousands of instances were exposed to the open internet.** Bitsight observed **more than
   30,000 distinct instances** between 2026-01-27 and 2026-02-08
   ([published 2026-02-09](https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances)) `[third-party security research]`;
   Hunt.io identified **17,587** in a 2026-02-03 sweep `[third-party security research]`. The exposure
   is *deliberate deployment*, not accident: 98.6% of Hunt.io's hits were on commercial cloud
   hosting, top hosts DigitalOcean (35.2%) and Alibaba Cloud (26.4%).

6. **The project's stated security model is "one trusted operator", stated bluntly and repeatedly,
   and it disclaims the boundaries people assume it has.** `SECURITY.md`: *"Anyone who can operate an
   agent can make it do anything that agent can do. Session ownership, visibility, and presence are
   usability features, not security boundaries."* And: *"The model/agent is **not** a trusted
   principal."* And: *"Prompt injection by itself is not a vulnerability report."* `[first-party docs]`

7. **The project itself names the approval-fatigue problem this project's `human oversight` entry
   describes.** Its security roadmap post: *"Prompts arrive faster than anyone can read them. After a
   few minutes, users flip on YOLO mode so work can continue. At that point the prompts train the
   user to stop reading."*
   ([blog, 2026-05-15](https://openclaw.ai/blog/where-openclaw-security-is-heading/)) `[first-party blog]`
   That is a vendor conceding, in its own documentation, that per-action approval degrades — which is
   the reasoning behind this project's preference for **containment** over approval.

8. **One showcase entry, and only one, describes something like the far-end archetype — and it is an
   unsourced one-line claim.** A community entry credited to `@henrymascot`: *"Watches a company Slack
   channel, responds helpfully, and forwards notifications to Telegram. **Autonomously fixed a
   production bug in a deployed app without being asked.**"* There is no link, no artifact, no
   verification path
   ([`docs/start/showcase.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/showcase.md), read 2026-08-30) `[practitioner anecdote]`.
   This is the entire observed-practice evidence base for "OpenClaw shipped a production fix
   unsupervised", and it does not carry weight.

9. **Third-party descriptions of OpenClaw are demonstrably unreliable on details a primary source
   settles in one read.** Hunt.io calls Clawdbot and Moltbot *"forks"* of OpenClaw (they are prior
   names of the same project) and describes CVE-2026-25253 as *"unauthenticated access to stored API
   tokens via the `/api/export-auth` endpoint"* — while the GitHub advisory that CVE points at
   (GHSA-g8p2-7wf7-98mq) describes something structurally different: a Control UI that trusts a
   `gatewayUrl` query parameter and auto-connects, leaking the gateway token to an attacker's server,
   *"exploitable even on instances configured to listen on loopback only, since the victim's browser
   initiates the outbound connection."* Same skepticism, same result as the refusal-policy strand. `[security advisory]` vs `[third-party security research]`

10. **OpenClaw is the wrong anchor for a delivery spectrum and the right anchor for a containment
    argument.** It is not where "AI ships software unsupervised" lives. It is where "AI holds
    everything you own and is reachable by strangers" lives. §8.

---

## 2. What OpenClaw is (Q1)

### 2.1 Architecture, from the project's own description

> "OpenClaw is an AI assistant that runs on your devices and meets you in the channels you already
> use. It connects models, tools, messaging channels, and optional companion apps through one
> Gateway, for a single operator or for a team whose members trust each other."
> — [README](https://github.com/openclaw/openclaw/blob/main/README.md), read 2026-08-30 `[first-party docs]`

The pieces, from the README's "How it fits together":

- **Gateway** — the local control plane for sessions, tools, events, and channel connections. Binds
  to loopback by default (port 18789).
- **Control UI, CLI, TUI** — clients that connect to the Gateway.
- **Channels** — WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, and others
  (labels in the repo also list Matrix, Mattermost, Nextcloud Talk, Nostr, LINE, Tlon, Zalo, MS Teams,
  BlueBubbles, voice-call).
- **Companion apps and nodes** — voice, Canvas, camera, screen and device-local actions on macOS,
  iOS, Android, Windows, Linux.
- **Tools, Skills, Plugins** — extension surface, distributed through **ClawHub**.

Written in **TypeScript**, MIT-licensed, distributed on npm as `openclaw`, requiring Node 22.22.3+ /
24.15+ / 25.9+, running on macOS, Linux and Windows (WSL2). Installed by a piped-curl shell script
or a PowerShell `iwr | iex` one-liner. `[first-party docs]`

**Model providers**: hosted and local, as plugins, with no privileged lab. The bundled provider table
alone lists OpenAI, Anthropic, Google (Gemini API, Vertex, Gemini CLI), OpenAI ChatGPT/Codex OAuth,
Z.AI/GLM, Vercel AI Gateway, GitHub Copilot, xAI, Mistral, Cohere, DeepSeek, Moonshot/Kimi, MiniMax,
Groq, Cerebras, Together, OpenRouter, NVIDIA, Ollama Cloud, Hugging Face, Tencent TokenHub, Alibaba
Qianfan, Volcano Engine/Doubao, Xiaomi, Venice, Arcee, BytePlus, Chutes, DeepInfra, Featherless,
GMI, Novita and a first-party `clawrouter`
([`docs/concepts/model-providers.md`](https://github.com/openclaw/openclaw/blob/main/docs/concepts/model-providers.md), read 2026-08-30) `[first-party docs]`.

**It also hosts other vendors' agent harnesses as plugins** — the Codex app-server loop, the GitHub
Copilot SDK session loop, and the Claude Agent SDK — *"while OpenClaw keeps ownership of channels,
sessions, policy, and state"*
([`docs/start/why-openclaw.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/why-openclaw.md), source review dated 2026-08-27) `[first-party docs]`.
This is directly relevant to the map: OpenClaw is not a competitor to Claude Code or Codex; it is a
*surface* that can run them. Its own FAQ says so (§0).

### 2.2 Governance

Stewarded by the **OpenClaw Foundation**, described as an independent 501(c)(3) with a full-time team,
donors and partners including Atlassian, GitHub, Microsoft, NVIDIA, OpenAI and Tencent across "more
than thirty organizations", and releases signed under the Foundation identity
([`docs/start/why-openclaw.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/why-openclaw.md)) `[first-party docs]`.
The author, **Peter Steinberger**, writes that inside OpenAI he *"run[s] a team called Claw Labs"*
([blog, 2026-04-30](https://openclaw.ai/blog/openclaw-security-in-public/)) `[first-party blog]`.
Note for citation hygiene: the Foundation's own page is the source for its Foundation claims; that is
an interested source on its own governance.

### 2.3 Naming history, dated

| Date | Name | Event |
|---|---|---|
| pre-Nov 2025 | **Warelay** | "a sensible name for a WhatsApp gateway" |
| 2025-11-24 | — | GitHub repository created (REST API) |
| 2025-11-25 | **Clawd** / **Clawdbot** | "a playful pun on 'Claude' with a claw" |
| **2026-01-27** | **Molty** / **Moltbot** | *"Anthropic sent a polite email asking for a name change (trademark stuff)."* Community named it at 5am on Discord; Peter: "fuck it, let's go with openclaw" at 6:14am |
| **2026-01-29** | — | "Introducing OpenClaw" blog post; npm package `openclaw` created |
| **2026-01-30** | **OpenClaw** | "The Great OpenClaw Migration" at 4am GMT: GitHub org rename, X handle, npm packages, `docs.openclaw.ai` |

Sources: [`docs/start/lore.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/lore.md),
[`VISION.md`](https://github.com/openclaw/openclaw/blob/main/VISION.md),
[blog 2026-01-29](https://openclaw.ai/blog/introducing-openclaw/), npm registry metadata — all read
2026-08-30 `[first-party docs]` / `[first-party blog]`.

**Two reasons for the renames, both documented and both worth reporting accurately.** The first molt
was **legal**: an Anthropic trademark request over "Clawd". The second was **phonetic**: the
announcement post says Moltbot *"never quite rolled off the tongue"*, and adds that for OpenClaw
*"we did our homework: trademark searches came back clear, domains have been purchased"*. The rename
is not a security or governance event, and should not be reported as one.

The lore page also records that the renames were operationally chaotic in ways that are themselves a
finding about agent-adjacent projects at scale: bots sniped the `@openclaw` X handle "within seconds"
and posted a crypto wallet address; Peter accidentally renamed his own GitHub account and bots sniped
`steipete` "within minutes"; scammers created fake "Head of Engineering at OpenClaw" GitHub profiles
to promote tokens; a `$OPENCLAW` token launched on Pump.fun "within minutes" of the migration.
`[first-party docs]`

---

## 3. What it was built for (Q2) — the author's own words

> "OpenClaw started as a personal playground to learn AI and build something genuinely useful: an
> assistant that can run real tasks on a real computer. […] The goal: a personal assistant that is
> easy to use, supports a wide range of platforms, and respects privacy and security."
> — [`VISION.md`](https://github.com/openclaw/openclaw/blob/main/VISION.md), read 2026-08-30 `[first-party docs]`

> "OpenClaw is an open agent platform that runs on your machine and works from the chat apps you
> already use. WhatsApp, Telegram, Discord, Slack, Teams—wherever you are, your AI assistant follows.
> **Your assistant. Your machine. Your rules.** Unlike SaaS assistants where your data lives on
> someone else's servers, OpenClaw runs where you choose—laptop, homelab, or VPS."
> — [blog, 2026-01-29](https://openclaw.ai/blog/introducing-openclaw/) `[first-party blog]`

> "Two months ago, I hacked together a weekend project. What started as 'WhatsApp Relay' now has over
> 100,000 GitHub stars and drew 2 million visitors in a single week."
> — same post `[first-party blog]`

> "OpenClaw is the AI that actually does things. It runs on your devices, in your channels, with your
> rules."
> — [`VISION.md`](https://github.com/openclaw/openclaw/blob/main/VISION.md) `[first-party docs]`

The one place the docs make an *enterprise* case — `why-openclaw.md` — is careful to say it is not a
different product: *"There is no enterprise edition. If you run OpenClaw for yourself, the defaults
are tuned for you and none of this requires action. The properties below are phrased as an enterprise
evaluation because that is the harshest audience."* `[first-party docs]`

Nowhere in the README, `VISION.md`, the announcement post, or the docs index is software delivery
named as a purpose. The roadmap in `VISION.md` lists security, bug fixes, setup reliability, model
providers, messaging channels, performance, "better computer-use and agent harness capabilities",
CLI/web ergonomics and companion apps. No CI, no deployment, no release automation. `[first-party docs]`

---

## 4. What it is actually used for (Q3)

### 4.1 The registry, quantified

I enumerated **1,198 skills** from `https://clawhub.ai/api/v1/skills` (paginated, 2026-08-30)
`[first-party docs]`.

**Most common topics:** `ai` (33), `generative` (28), 健康/Health (52 combined), `Self Improving` (20),
`Home` (17), `toolkit` (17), `mcp` (12), `git` (12), `security` (12), `agent` (12), `email` (10),
`docker` (9), `productivity` (8), `finance` (7), `Smart Home` (6).

**Delivery keyword frequency across all 1,198 skill summaries and descriptions:**

| Term | Skills containing it |
|---|---|
| `deploy` | 16 |
| `production` | 12 |
| `merge` | 11 |
| `ci/cd` | 8 |
| `pipeline` | 8 |
| `release` | 8 |
| `kubernetes` | 8 |
| `code review` | 7 |
| `pull request` | **2** |
| `github action` | **1** |
| `terraform` | **1** |

The character of the front page is life-admin and ops integration: VMware fleet management (a cluster
of ~15 skills from one publisher), Splitwise, Resy restaurant bookings, Canvas LMS parent portals,
Zola wedding planning, HoneyBook, FreshBooks, SignUpGenius, Skylight family calendars, A-share market
signals, image/music generation.

**Every delivery-adjacent skill I inspected keeps a human in the decision.** `code-workflow` is
"research → plan → **user review** → implement (TDD)". `smart-git` is "local code review, creating a
PR/MR, reviewing an existing PR/MR, listing my open PRs/MRs". `github-flow` is "GitHub issue/PR
workflow automation". `compound-eng-code-review` produces "severity-ranked findings". None of them
merge, deploy, or release.

### 4.2 The showcase

The project's curated showcase (`docs/start/showcase.md`, read 2026-08-30) is organised as: *Fresh
from Discord*, *Automation and workflows*, *Knowledge and memory*, *Voice and phone*, *Infrastructure
and deployment*, *Home and hardware*, *Community projects*. `[first-party docs]`

**"Infrastructure and deployment" is about deploying OpenClaw itself** — a Home Assistant add-on, a
Nix packaging repo, a macOS menu-bar manager, a CalDAV calendar skill. Not about the agent deploying
anything.

Exactly **two** entries touch software delivery:

- **"PR Review to Telegram Feedback"** (@bangnokia) — *"OpenCode finishes the change, opens a PR,
  OpenClaw reviews the diff and replies in Telegram with suggestions plus a clear merge verdict."*
  Note the division of labour: a coding agent writes and opens; OpenClaw *reads and advises a human
  over chat*. This is OpenClaw in its actual role — a notification and judgement surface, not the
  thing that ships. `[practitioner anecdote]`
- **"Slack auto-support"** (@henrymascot) — the unsourced production-bug claim quoted in §1.8.

### 4.3 The issue tracker as a shape test

The repository's label taxonomy (GraphQL, read 2026-08-30) is entirely channels, apps, extensions,
gateway, CLI, security, docker, agents. There is no CI label, no deploy label, no coding label. The
volume — 3,563 open issues, 2,213 open PRs, 30,750 merged PRs — is going into channel integrations
and platform work. GitHub **Discussions is disabled** (totalCount 0); the community lives on Discord.
`[first-party docs]`

### 4.4 What the docs *enable* versus what people *do*

The docs enable a great deal that nobody in the visible community is doing:

- **Cloud workers** — a session's coding work on a throwaway cloud machine, with per-dispatch minted
  credentials on a ten-minute TTL, no standing GitHub or cloud credential on the worker, and the
  durable transcript held by the Gateway
  ([`docs/gateway/cloud-workers.md`](https://github.com/openclaw/openclaw/blob/main/docs/gateway/cloud-workers.md)) `[first-party docs]`
- **Managed worktrees**, **portals** (proxying an agent's dev server into your browser), a
  **Cloud Worker Desktop** VNC view, **Beam** (mirroring a local coding session to a team gateway).
- **Git co-author attribution**: *"OpenClaw supplies exact `Co-authored-by` trailers for eligible
  shared-session participants with verified GitHub identity"*, and broker-created PRs end with a link
  to the team session *"so a reviewer with access can read the conversation that produced the diff."*
  `[first-party docs]`

That last detail is the tell. The whole publication path is built so that **a reviewer can reconstruct
how the diff came to exist**. It is engineered for human review of agent work, not for its absence.

---

## 5. The central question, answered mechanically (Q4)

### 5.1 Can it open a pull request? Yes — a draft one, by construction

`github_publish` is the only repository-write tool. Its description, verbatim from source:

> "Publish the current session-owned Git worktree through the Gateway. Call only after the work is
> complete. On cloud or remote-exec sessions this records a durable request; finish the turn so
> authoritative reconciliation can complete before the Gateway commits, pushes through an exact HTTPS
> path, and creates or reuses a **draft pull request**. […] Credentials never enter tool arguments or
> the worker."
> — [`src/agents/tools/github-publish-tool.ts`](https://github.com/openclaw/openclaw/blob/main/src/agents/tools/github-publish-tool.ts), read 2026-08-30 `[first-party source code]`

Its parameter schema accepts exactly two optional fields — `title` and `body` — with
`additionalProperties: false`. There is no `draft` parameter to flip. In the executor the PR is
created with `draft: true` written as a literal in the request body
([`github-publication-executor.ts:529`](https://github.com/openclaw/openclaw/blob/main/src/gateway/github-publication-executor.ts)) `[first-party source code]`.

Three structural constraints ride along with it: credentials stay Gateway-side and never reach the
worker or the tool arguments; the publication is idempotency-keyed on the tool call ID; and the
executor refuses when *"GitHub pull request is owned by another account."*

### 5.2 Can it merge? Not through any tool it ships

There is no merge tool, no deploy tool, no release tool, no CI-dispatch tool in the agent tool
surface (`src/agents/tools/` full listing, read 2026-08-30) `[first-party source code]`.

**The honest caveat, and it matters:** OpenClaw ships a general `exec` tool. An agent with exec access
and a `gh` CLI on `PATH` can run `gh pr merge`, `kubectl apply`, or `terraform apply` — and by default
it can do so with **no sandbox and no approval prompt** (§5.4). So the *capability* to ship
unsupervised is a shell command away for anyone who wants it. What is absent is any evidence that
anyone has built that, documented it, published a skill for it, or written about doing it. **The
capability is trivially reachable and the practice is invisible.**

### 5.3 The nearest real thing: ClawSweeper automerge

The most autonomous merge path anywhere in the OpenClaw universe is not in OpenClaw. It is
**ClawSweeper**, a separate bot in the same org that maintains the OpenClaw repositories
([openclaw/clawsweeper](https://github.com/openclaw/clawsweeper), [docs](https://clawsweeper.bot/)).
It has a genuine automerge lane. Its documented shape:

- **A human starts it, per PR:** *"A maintainer comments `/clawsweeper automerge`."* `[first-party docs]`
- **The merge is pinned to a reviewed commit:** *"every merge is pinned to a reviewed head SHA, waits
  for GitHub checks, and uses the comment router as the only final merge owner."* The router *"verifies
  the pass marker names the current head SHA"* before merging. `[first-party docs]`
- **CI is the gate:** the router *"waits for required checks and transient mergeability"*; repairable
  states include `CONFLICTING`, `DIRTY`, `BEHIND`, and terminal required-check failures. `[first-party docs]`
- **Scope is opt-in:** *"Bounded 'review, fix, re-review, merge' loop for **opted-in** PRs and strict
  generated bug PRs."* `[first-party docs]`

This is worth reporting precisely because it is *close* and still not the far-end archetype. A human
elects each PR into the lane. The merge is gated on CI checks that a human wrote. And a bot review
substitutes for a human reading the diff — which is exactly this project's definition of
**verification** doing its job, not the absence of it.

**What it is not:** a deploy. Releases at OpenClaw are explicitly human-signed: *"Releases used to be
just me. Now it's me plus another OpenClaw Foundation employee, with each one scripted, gated and
signed off."*
([blog, 2026-04-30](https://openclaw.ai/blog/openclaw-security-in-public/)) `[first-party blog]`

### 5.4 The default posture — the fact that should not be buried

| Setting | Default | Source |
|---|---|---|
| `agents.defaults.sandbox.mode` | **`off`** | `SECURITY.md` |
| `tools.exec.host` | `auto` → resolves to **gateway host** when no sandbox runtime | `SECURITY.md`, `docs/tools/exec.md` |
| Exec approval mode on gateway/node | **`full`** — "No approval gate" | `docs/tools/exec.md` |

> "**No-approval host exec is the default for gateway and node (`mode=full`)** — this comes from the
> host-policy defaults, not from `host=auto`. If you want approvals/allowlist behavior, set
> `tools.exec.mode` and tighten the host approvals file."
> — [`docs/tools/exec.md`](https://github.com/openclaw/openclaw/blob/main/docs/tools/exec.md), read 2026-08-30 `[first-party docs]`

> "**Sandboxing is off by default.** Out of the box, OpenClaw is a personal assistant for one trusted
> operator, and exec runs on the gateway host without prompts."
> — [`docs/start/why-openclaw.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/why-openclaw.md) `[first-party docs]`

The available modes are `deny`, `allowlist`, `ask`, `auto`, `full`. `auto` — added 2026-05-31 — routes
allowlist misses to a **separate reviewer model** (configurable to a different, stronger model than
the agent) before falling back to a human; the auto-review approval is single-use and pinned to a
resolved executable path, and heredocs, shell expansions and unparseable wrapper quoting always fall
back to a human
([blog 2026-05-31](https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals/),
[`docs/tools/exec.md`](https://github.com/openclaw/openclaw/blob/main/docs/tools/exec.md)) `[first-party blog]` / `[first-party docs]`.
That is a well-designed containment mechanism. It is **opt-in**, and the post says so: *"We are not
changing the default today."*

**Read against the map, this is the finding.** The archetype OpenClaw actually occupies is not "ships
code without human verification". It is "**executes arbitrary host commands without human approval or
containment, by default, on behalf of a model reachable from a group chat**". Those are different
failures, and the second is the one this tool is evidence for.

---

## 6. Security posture (Q5) — the lethal trifecta, in the wild

OpenClaw is the cleanest real-world instance of this project's **lethal trifecta** term I have found:
private data access (host filesystem, credentials, mail, calendars, smart home), exposure to untrusted
content (any messaging channel, any web fetch, any email), and the ability to externally communicate
(it is *made of* outbound messaging). The project does not dispute this. It states it.

### 6.1 What the project says, verbatim

> "Treat inbound messages as untrusted input. […] Tools run on the host for the main session unless
> you configure sandboxing."
> — [README](https://github.com/openclaw/openclaw/blob/main/README.md) `[first-party docs]`

> "Anyone who can operate an agent can make it do anything that agent can do. Session ownership,
> visibility, and presence are usability features, not security boundaries."
> — [`SECURITY.md`](https://github.com/openclaw/openclaw/blob/main/SECURITY.md) `[first-party docs]`

> "OpenClaw does **not** model one gateway as a multi-tenant, adversarial user boundary. […] If one
> operator can view data from another operator on the same gateway, that is expected in this trust
> model."
> — `SECURITY.md` `[first-party docs]`

> "The model/agent is **not** a trusted principal. Assume prompt/content injection can manipulate
> behavior. Security boundaries come from host/config trust, auth, tool policy, sandboxing, and exec
> approvals. Prompt injection by itself is not a vulnerability report unless it crosses one of those
> boundaries."
> — `SECURITY.md` `[first-party docs]`

> "Prompt injection does not require public DMs: even if only you can message the bot, any
> **untrusted content** it reads (web search/fetch results, browser pages, emails, docs, attachments,
> pasted logs/code) can carry adversarial instructions. The content itself is a threat surface, not
> just the sender."
> — [`docs/gateway/security/index.md`](https://github.com/openclaw/openclaw/blob/main/docs/gateway/security/index.md) `[first-party docs]`

> "For tool-enabled agents or agents that read untrusted content, prompt-injection risk with
> older/smaller models is often too high. Do not run those workloads on weak model tiers."
> — same `[first-party docs]`

> "Do **not** expose it to the public internet (no direct bind to `0.0.0.0`, no public reverse proxy).
> It is not hardened for public exposure."
> — `SECURITY.md`, Web Interface Safety `[first-party docs]`

> "Plugins/extensions are loaded **in-process** with the Gateway and are treated as trusted code.
> Plugins can execute with the same OS privileges as the OpenClaw process. Runtime helpers […] are
> convenience APIs, not a sandbox boundary."
> — `SECURITY.md` `[first-party docs]`

> "Exec approvals (allowlist + ask) are guardrails for operator intent, not hostile multi-tenant
> isolation. […] Use sandboxing and host isolation for strong boundaries."
> — [`docs/gateway/security/index.md`](https://github.com/openclaw/openclaw/blob/main/docs/gateway/security/index.md) `[first-party docs]`

That last one is the project drawing this project's own distinction: approval is not containment.

The project also cites a 2026 crowdsourced injection arena — 272K attacks across 41 agent scenarios,
scored only when the agent both executed the harmful action *and* hid it — reporting 0.5% success
against Claude Opus 4.5, 1.0% Sonnet 4.5, 1.3% Haiku 4.5, 8.5% Gemini 2.5 Pro, and then immediately
qualifies it: *"Adaptive human attackers still break models that score well on static benchmarks,
with published success rates above 80% against state-of-the-art defenses once the attacker adapts."*
`[first-party docs, citing an unnamed third-party arena]` — I could not identify the underlying arena
from the docs, so treat the numbers as a vendor-relayed figure, not a verified one.

### 6.2 The advisory record

From the GitHub Security Advisory REST API for `openclaw/openclaw`, read 2026-08-30 `[security advisory]`:

- **647 published advisories.** Severity: 14 critical, 219 high, 350 medium, 64 low. 39 carry CVE IDs.
- Publication by month: 2026-01 (3), **2026-02 (220)**, **2026-03 (204)**, 2026-04 (108), 2026-05 (67),
  2026-06 (45). None published after June 2026 at the time of reading.
- Earliest: **2026-01-31**, `GHSA-mc68-q9jw-2h3v` *"Command Injection in **Clawdbot** Docker Execution
  via PATH Environment Variable"* (CVE-2026-24763) — still carrying the old name.

The 14 criticals, in order:

| Date | GHSA | Summary |
|---|---|---|
| 2026-02-14 | `gv46-4xfq-jv58` | Remote Code Execution via Node Invoke Approval Bypass in Gateway |
| 2026-02-14 | `4rj2-gpmh-qq5x` | Inbound allowlist policy bypass in voice-call extension |
| 2026-02-14 | `qrq5-wjgg-rvqw` | Path Traversal in Plugin Installation |
| 2026-03-12 | `4jpw-hj22-2xmc` | Pairing-scoped device tokens could mint `operator.admin` and reach node RCE |
| 2026-03-13 | `rqpp-rjj8-7wv8` | WebSocket shared-auth connections could self-declare elevated scopes |
| 2026-03-24 | `hf68-49fm-59cq` | `device.pair.approve` lets `operator.pairing` escalate to `operator.admin`, reaching node RCE |
| 2026-03-26 | `9hjh-fr4f-gxc4` | Gateway backend reconnect lets non-admin scopes self-claim `operator.admin` |
| 2026-03-26 | `fqw4-mph7-2vr8` | Local shared-auth reconnect silently widens paired device scope to `operator.admin` |
| 2026-03-29 | `hc5h-pmr3-3497` | `/pair approve` omitted caller scope subsetting |
| 2026-03-29 | `8rh7-6779-cjqq` | CWD `.env` environment injection bypasses host-env policy, allows config takeover |
| 2026-03-29 | `j7p2-qcwm-94v4` | Incomplete host env sanitization allows supply-chain redirection via package-manager env overrides |
| 2026-03-31 | `9p3r-hh9g-5cmg` | Sandbox escape via TOCTOU race in remote FS bridge `readFile` |
| 2026-03-31 | `g5cg-8x5w-7jpm` | Heartbeat context inheritance bypasses sandbox via `senderIsOwner` escalation |
| 2026-04-16 | `xh72-v6v9-mwhc` | Feishu webhook and card-action validation now fail closed |

The pattern is one class repeated: **privilege and scope confusion that terminates in remote code
execution on the host**. Seven of the fourteen are scope-escalation-to-RCE.

Named CVEs of note `[security advisory]`:

- **CVE-2026-24763** (2026-01-31, high) — Command injection in Clawdbot Docker execution via `PATH`.
- **CVE-2026-25253 / GHSA-g8p2-7wf7-98mq** (2026-01-31, high, CVSS 8.8) — *"1-Click RCE via
  Authentication Token Exfiltration From gatewayUrl."* The advisory's own impact statement: *"This
  vulnerability is exploitable even on instances configured to listen on loopback only, since the
  victim's browser initiates the outbound connection."* Affected `<= v2026.1.28`, patched `v2026.1.29`
  — under the package name `clawdbot`.
- **CVE-2026-25593** (2026-02-04, high) — Unauthenticated Local RCE via WebSocket `config.apply`.
- **CVE-2026-27001** (2026-02-18, high) — Unsanitized CWD path injection into LLM prompts.
- **CVE-2026-27002** (2026-02-18) — Docker container escape via unvalidated bind-mount config injection.
- **CVE-2026-27209** (2026-02-21, high) — Shell command injection in exec allowlist mode via unquoted
  heredoc expansion.
- **CVE-2026-26329**, **CVE-2026-26972** (2026-02) — Path traversal in browser upload / download.

### 6.3 The project's own accounting of the advisory flood

> "As of April 30, GitHub shows 1,309 security advisories since January 10. 535 were published. 746
> were closed as invalid. […] GitHub currently shows 109 critical reports: 14 published, 95 closed as
> invalid. That is 87%. The false positives are often wonderfully dumb: 'the agent runs commands,
> therefore RCE', 'plugins execute code', 'this dangerous opt-in mode is dangerous', 'if I already
> have the token I can do bad things.'"
> — [blog, 2026-04-30](https://openclaw.ai/blog/openclaw-security-in-public/) `[first-party blog]`

> "Real bugs remain. OpenClaw moves fast and does weird stuff. We fixed authentication bugs, privilege
> confusion, reconnect scope widening, sandbox bypasses, unsafe env handling and approval path
> mistakes."
> — same `[first-party blog]`

This is a genuinely useful primary source on how an advisory count should and should not be read. Note
also that `why-openclaw.md` says so itself: *"Advisory counts are not a comparative safety score."*
Reporting "647 advisories" as a bare comparative number would repeat exactly the error this project's
citation-hygiene vocabulary exists to prevent. The right reading is the *shape*: a young, very large
attack surface with a fast-moving, publicly-triaged security process and a documented, narrow trust
model.

Hardening measures the project documents `[first-party docs]` / `[first-party blog]`: CodeQL across
TypeScript, Actions, Android and macOS; an OpenGrep rulepack of **148 precise rules**, each tied to a
specific advisory or review finding, run on PR diffs for regression and variant detection; TLA+ models
of the riskiest authorization and isolation paths (with the docs' own caveat that these are *"models
of the design, checked in bounded state spaces; they do not establish that 'the TypeScript is
verified'"*); a community threat model mapped to MITRE ATLAS; Sigstore attestations and npm
provenance; `openclaw security audit --deep` with stable check IDs.

### 6.4 Mass internet exposure

Two independent scanning efforts `[third-party security research]`:

- **Bitsight**, published 2026-02-09: *"we ended up observing more than 30,000 instances in just one
  analysis period, from January 27 to February 8."* By 2026-01-27, "almost 1,000 instances were
  already observed online since the beginning of the year", and there was a **177% single-day surge**
  between 27 and 28 January. Bitsight also reports observing instances *"in more sensitive industry
  sectors such as healthcare, finance, government and insurance"*. It notes that pre-OpenClaw versions
  supported `gateway auth mode "none"`, removed at the OpenClaw rename.
- **Hunt.io**, published 2026-02-03: **17,587** instances by HTML-title fingerprint across 52
  countries; **98.6% on commercial cloud/hosting**, DigitalOcean 35.2% and Alibaba Cloud 26.4%; title
  split Clawdbot 68.9% / Moltbot 22.3% / OpenClaw 8.8%.

Bitsight quotes a honeypot operator: *"We stood up a honeypot on port 18789 […] The first probes
arrived within minutes. The traffic included prompt injection attempts targeting the AI layer—but the
more sophisticated attackers skipped the AI entirely. They connected directly to the gateway's
WebSocket API and attempted authentication bypasses, protocol downgrades to pre-patch versions, and
raw command execution. Every RPC method they probed maps to a real handler in the codebase. They're
not guessing. They've read the source."* `[practitioner anecdote, relayed by third-party research]`

**Skepticism applied, per house rules.** These two counts differ by ~70% and use different
methodologies over different windows; treat "tens of thousands" as the defensible claim, not either
specific number. Bitsight itself debunks an earlier viral geographic-distribution chart of Clawdbot
instances: *"we could tell at a glance that the chart was far from accurate."* And Hunt.io's article
contains two errors a primary source refutes (§7.3). Meanwhile, **the exposure is explicitly out of
scope for the project's own security policy** — `SECURITY.md` lists "Public Internet Exposure" and
"Using OpenClaw in ways that the docs recommend not to" under **Out of Scope**, and the docs say
plainly not to do it. That is a defensible position on triage and a genuinely bad outcome at the same
time; both should be reported.

### 6.5 *Agents of Chaos* — and why the framing dispute matters

**arXiv:2602.20021v1**, submitted 2026-02-23, 39 authors led by Natalie Shapira with David Bau, Maarten
Sap, Tomer Ullman and others. `[academic]`

Design: six OpenClaw agents on isolated VMs, each with Discord, ProtonMail, persistent memory, a 20GB
volume, running 24/7; twenty AI researchers probing them adversarially for two weeks. Four agents on
Kimi K2.5, two on Claude Opus 4.6. Eleven case studies. Reported behaviours: *"unauthorized compliance
with non-owners, disclosure of sensitive information, execution of destructive system-level actions,
denial-of-service conditions, uncontrolled resource consumption, identity spoofing vulnerabilities,
cross-agent propagation of unsafe practices, and partial system takeover. In several cases, agents
reported task completion while the underlying system state contradicted those reports."*

The project's response, 2026-04-30: *"They ran OpenClaw in sudo mode with disabled guardrails, broad
shell access and no sandboxing, then wrote up the results as if this is what users get out of the box.
The paper has since added a short acknowledgment that guardrails were disabled; the headlines did
not."* `[first-party blog]`

**I checked the paper against that claim.** The v1 text says: *"Agents were given unrestricted shell
access (including `sudo` permissions, in some cases), no tool-use restrictions, and the ability to
modify any file in their workspace—including their own operating instructions."* So the disclosure is
in v1 and the characterisation is accurate. **But the rebuttal is weaker than it looks**, because
§5.4 establishes that OpenClaw's *shipped defaults* are already no sandbox and no approval gate. The
gap between the lab configuration and the default configuration is `sudo` and a permissive tool
policy — real, but narrower than "disabled guardrails" implies.

**The paper's most useful finding for this ticket is one neither side highlighted.** Despite the setup
being built for autonomy:

> "The majority of agent actions during our experiments were initiated by human intervention, and most
> high-level direction was provided by humans. […] most ostensibly autonomous actions still involved at
> least partial human oversight—a human noticing a failure, restarting a job, or manually triggering a
> heartbeat."

The paper attributes part of this to cron and heartbeat bugs, and is careful: *"It is conceivable that
the lack of our agents' autonomy partially stems from these technical problems. However, we have also
not observed the described autonomy patterns without explicit instructions provided by the human
operators since fixing our setup."* And: *"reliable self-configuration was the exception rather than
the norm."* When agents got stuck, the researchers fell back to **Claude Code or Cursor Agent** on the
agent's own VM — the coding agents did the coding.

The case studies are personal-assistant failures, not delivery failures: an agent deleting its own
mail server in response to a secrecy conflict; compliance with non-owner instructions; sensitive
disclosure; DoS through looping. Not one involves shipping software.

---

## 7. Contrarian and negative findings

### 7.1 The thing the user is picturing does not exist in the artifact

If the far-end archetype is "an agent commits, merges and deploys with no human in the path", OpenClaw
does not implement it. Its repository-write ceiling is a **draft** PR — a state whose entire purpose is
to signal *not ready to merge*. That is a deliberate design decision visible in one line of source.

### 7.2 The strongest "far end" claim in the corpus is a single unsourced sentence

§1.8 / §4.2. One showcase card. No link, no artifact, no author attestation beyond a handle. It is the
whole of the observed-practice evidence, and it is not enough to build an archetype on.

### 7.3 Third-party security research got the primary facts wrong

Hunt.io's article ([2026-02-03](https://hunt.io/blog/cve-2026-25253-openclaw-ai-agent-exposure)):

- Calls Clawdbot and Moltbot *"its forks"* — they are prior names of the same project, per the
  project's own `VISION.md` and lore page.
- Describes CVE-2026-25253 as *"unauthenticated access to stored API tokens via the `/api/export-auth`
  endpoint"* which *"lacks any authentication or authorization checks"*. The GitHub advisory that CVE
  points to (GHSA-g8p2-7wf7-98mq) and NVD's own description both describe a **query-string
  `gatewayUrl` auto-connect that leaks the token via the victim's own browser**. Different mechanism,
  different mitigation, different threat model.
- Calls OpenClaw a *"browser automation framework"*.

This does not invalidate their scan counts — fingerprinting an HTML title is independent of
understanding the CVE — but it is a direct instance of the pattern the refusal-policy strand found.
**Do not source OpenClaw's mechanics from security-vendor blogs.**

### 7.4 The project's rebuttal of *Agents of Chaos* is partly self-undermining

§6.5. "Disabled guardrails" overstates the gap when your shipped default is already `sandbox: off`
and `exec mode: full`.

### 7.5 The advisory count is not a safety score, and the project says so first

§6.3. Anyone citing "647 advisories" as a comparative badness number is making the error the project
itself warns against — and the error this repo's **evidence tier** entry exists to prevent.

### 7.6 It is not primarily a Western-developer phenomenon

Roughly a third of the ClawHub skills I enumerated are Chinese-language, and Hunt.io's scan puts
Beijing, Hangzhou, Shanghai and Guangzhou collectively above any single US city outside cloud regions.
Tencent supplies full-time maintainers. Any characterisation of the OpenClaw community as an
English-speaking developer subculture is wrong.

---

## 8. Is it the right anchor? (Q6)

### 8.1 The honest answer: no, not for a software delivery spectrum

OpenClaw does not anchor the far end of a spectrum about professional software delivery, because it
does not deliver software. Placing it there would make the map's furthest archetype rest on a tool
whose vendor explicitly tells you to use a different tool for the job (§0), whose only repo-write
capability is a draft PR, and whose entire ecosystem is calendars, smart homes and expense tracking.

Anyone who knows OpenClaw will spot this immediately, and the credibility cost is not worth it.

### 8.2 What OpenClaw *does* anchor, and why it still belongs in the document

It anchors a different and genuinely extreme position: **maximum delegation of a person's whole
digital life to an agent, on the widest possible untrusted-input surface, with the weakest default
containment.** Nothing else in this research has that combination:

- Private data: host filesystem, credentials, mail, calendars, browser sessions, smart home.
- Untrusted input: any DM on any of a dozen messaging networks, any fetched page, any email, any
  attachment.
- External communication: it *is* an outbound messaging system.
- Default containment: **none** — `sandbox: off`, `exec mode: full`.

That is the **lethal trifecta** with the containment layer switched off by default, deployed by tens of
thousands of people, some of them in healthcare and finance. It is the best available real-world
instance of the term this project defines, and it should appear in the document under that heading,
not under delivery.

It is also an unusually good source on **why containment beats approval**, in the vendor's own words —
§1.7, §5.4, §6.1. A vendor conceding that its own approval prompts train users to stop reading is
stronger evidence for this project's `human oversight` position than any advocacy piece.

### 8.3 What would anchor a delivery spectrum instead

The far end of *software delivery* needs an artifact where the machine, not a human, is the gate on a
change reaching production, at volume, with published outcome data. Candidates from this repo's
existing research, in descending order of strength:

1. **Meta's RADAR** — already established in `verification-gates.md`: **331,000+ diffs landed with no
   human reviewer**, revert rate 1/3 and production incident rate 1/50 of human-reviewed diffs, on a
   risk-scored subset. It is simultaneously the reference artifact for "the machine is the gate" and
   for how narrowly that claim must be scoped. This is the far-end anchor the map needs.
2. **ClawSweeper's automerge lane** (§5.3) — a real, documented, small-scope bot-merge path, opt-in
   per PR, CI-gated, running on a 388k-star repository. Useful as a *reachable* midpoint, not the far
   end.
3. **Agent-authored PR outcome data** — the AIDev corpus (456,535 agent PRs, 35–64% acceptance) and
   arXiv:2606.22721 (approval rates rising 30.1% → 36.8% while inline comments fall 22%), both already
   in `verification-gates.md`. These describe what actually happens at the frontier better than any
   tool description does.

**Recommendation.** Keep OpenClaw in the tooling document, prominently, but under the containment and
lethal-trifecta discussion rather than as the delivery spectrum's endpoint. Say plainly why: it is a
personal-assistant gateway, its authors say so, and the far end of delivery is anchored by RADAR.
Then say the thing that is actually interesting about it — that the most-starred agent project in the
world ships with no sandbox and no approval gate, and that this is a *delegation* extreme even though
it is not a *delivery* one.

---

## 9. Sources

**First-party — repository and docs** (all read 2026-08-30 unless noted)

- [`README.md`](https://github.com/openclaw/openclaw/blob/main/README.md)
- [`VISION.md`](https://github.com/openclaw/openclaw/blob/main/VISION.md)
- [`SECURITY.md`](https://github.com/openclaw/openclaw/blob/main/SECURITY.md)
- [`docs/start/why-openclaw.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/why-openclaw.md) (its own source review dated 2026-08-27 against commit `7b624e9de25`)
- [`docs/start/lore.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/lore.md)
- [`docs/start/showcase.md`](https://github.com/openclaw/openclaw/blob/main/docs/start/showcase.md)
- [`docs/gateway/security/index.md`](https://github.com/openclaw/openclaw/blob/main/docs/gateway/security/index.md)
- [`docs/gateway/security/exposure-runbook.md`](https://github.com/openclaw/openclaw/blob/main/docs/gateway/security/exposure-runbook.md)
- [`docs/gateway/sandboxing.md`](https://github.com/openclaw/openclaw/blob/main/docs/gateway/sandboxing.md)
- [`docs/gateway/cloud-workers.md`](https://github.com/openclaw/openclaw/blob/main/docs/gateway/cloud-workers.md)
- [`docs/tools/exec.md`](https://github.com/openclaw/openclaw/blob/main/docs/tools/exec.md)
- [`docs/reference/pull-request-review-flow.md`](https://github.com/openclaw/openclaw/blob/main/docs/reference/pull-request-review-flow.md)
- [`docs/concepts/model-providers.md`](https://github.com/openclaw/openclaw/blob/main/docs/concepts/model-providers.md)
- [`docs/help/faq.md`](https://github.com/openclaw/openclaw/blob/main/docs/help/faq.md)
- [`docs/index.md`](https://github.com/openclaw/openclaw/blob/main/docs/index.md)

**First-party — source code**

- [`src/agents/tools/github-publish-tool.ts`](https://github.com/openclaw/openclaw/blob/main/src/agents/tools/github-publish-tool.ts)
- [`src/gateway/github-publication-executor.ts`](https://github.com/openclaw/openclaw/blob/main/src/gateway/github-publication-executor.ts)
- Full listing of `src/agents/tools/` via the Git tree API (37,296 paths), 2026-08-30

**First-party — blog** (`https://openclaw.ai/blog/`)

- [Introducing OpenClaw](https://openclaw.ai/blog/introducing-openclaw/) — Peter Steinberger, 2026-01-29
- [How OpenClaw Got Safer in Public](https://openclaw.ai/blog/openclaw-security-in-public/) — Peter Steinberger, 2026-04-30
- [OpenClaw Had a Rough Week](https://openclaw.ai/blog/openclaw-rough-week/) — Peter Steinberger, 2026-05-05
- [Where OpenClaw Security Is Heading](https://openclaw.ai/blog/where-openclaw-security-is-heading/) — Jesse Merhi, 2026-05-15
- [Safer Than YOLO: Auto Mode for Exec Approvals](https://openclaw.ai/blog/safer-than-yolo-auto-mode-for-exec-approvals/) — Koc, Merhi, Avant, 2026-05-31

**First-party — APIs and registries**

- GitHub REST `repos/openclaw/openclaw` and `.../security-advisories` (647 published advisories, paginated), 2026-08-30
- GitHub GraphQL: issue/PR/label/discussion counts, 2026-08-30
- `https://clawhub.ai/api/v1/skills` — 1,198 skills enumerated, 2026-08-30
- `https://registry.npmjs.org/openclaw` — 248 versions, created 2026-01-29
- [ClawSweeper docs](https://clawsweeper.bot/) and [automerge flow](https://clawsweeper.bot/repair/automerge-flow.html), 2026-08-30

**Security advisories and CVE records**

- [GHSA-g8p2-7wf7-98mq](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq) / CVE-2026-25253 (NVD record, published 2026-02-01, CVSS 8.8)
- The 14 critical advisories tabulated in §6.2, read via the GitHub Security Advisory API

**Academic**

- Shapira, N. et al., *Agents of Chaos*, [arXiv:2602.20021v1](https://arxiv.org/abs/2602.20021), 2026-02-23

**Third-party security research** (secondary; treat mechanics claims with caution — §7.3)

- [Bitsight — OpenClaw Security: Risks of Exposed AI Agents](https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances), 2026-02-09
- [Hunt.io — Hunting OpenClaw Exposures: CVE-2026-25253](https://hunt.io/blog/cve-2026-25253-openclaw-ai-agent-exposure), 2026-02-03

**Press** (identified but not relied on for any claim)

- Infosecurity Magazine, "Researchers Find 40,000+ Exposed OpenClaw Instances"; SecurityScorecard;
  PointGuard AI; hunto.ai; knolli.ai; Cyber Unit. Listed for completeness. The 40,214 figure appears
  only in press summary and I could not trace it to a named methodology, so it is **not** used above.

---

## 10. Confidence and gaps

**High confidence**

- The naming history and its dates. Three independent first-party sources agree.
- That `github_publish` creates a draft PR and that `draft: true` is a literal. Read in source.
- That there is no merge, deploy, release or CI tool in the agent tool surface. Full directory listing.
- The default posture: `sandbox: off`, exec `mode=full` / no approval gate. Stated in three
  first-party places.
- The advisory counts and severity distribution. Read from the API, not summarised.
- That the ClawHub ecosystem is not a software-delivery ecosystem. 1,198 skills counted directly.
- The project's own positioning against Claude Code and Codex. Verbatim from its FAQ.

**Medium confidence**

- The exposure scale. Two vendor scans disagree by ~70%; "tens of thousands, concentrated on cloud
  hosting, in Jan–Feb 2026" is the safe claim.
- That nobody merges or deploys through OpenClaw. This is an absence-of-evidence finding over a
  large, largely Discord-based community. I searched the docs, the showcase, the skill registry, the
  label taxonomy and the tool surface. **I did not search Discord**, which is where most of this
  community actually talks, and which is not indexed. If the practice exists anywhere, it exists
  there, undocumented.
- The prompt-injection arena figures in §6.1 — relayed by the vendor's docs without a citation I
  could resolve.

**Known gaps**

- **Discord is unindexed and unsearched.** The project's own docs point setup questions and
  contributor coordination to Discord. A meaningful fraction of practitioner evidence is there and
  outside my reach.
- **No usage telemetry exists to find.** `VISION.md`: *"OpenClaw sends no usage analytics, tracking
  identifiers, or telemetry attribution to the project unless the operator turned that on
  themselves."* There is no vendor dataset on what OpenClaw is used for, and there cannot be one by
  design. Everything in §4 is inferred from registry and showcase artifacts.
- **The maturity scorecard was not read.** `why-openclaw.md` references a scorecard grading 50
  surfaces across 280 capability areas at `/maturity/scorecard`. It would settle whether the project
  grades a coding/delivery surface at all. Not fetched — low marginal value against the FAQ quote,
  but it is the obvious next read.
- **ClawSweeper's merge volume is unknown.** I established the mechanism and the human trigger, not
  how many PRs have gone through the automerge lane. `clawsweeper.bot/live-dashboard.html` and
  `action-ledger.html` exist and were not fetched.
- **Advisory publication stops after 2026-06.** Whether that reflects a genuine decline in real
  findings (the project claims the inbound rate "has dropped significantly"), a change in disclosure
  cadence, or an artifact of the API is not established.
- **The 40,214 exposure figure could not be traced** to a named methodology and is excluded.
- **No corroboration was sought for the `@henrymascot` production-bug claim.** No link exists to follow.

---

## 11. Blocked or unavailable sources

- **`https://clawhub.ai/skills` (HTML)** — client-rendered single-page app; server response contains
  no skill data. *Not a block; a rendering limitation.* Worked around via the public JSON API at
  `https://clawhub.ai/api/v1/skills`, which returned complete records.
- **`https://clawhub.ai/api/skills`, `/api/trending`, `/sitemap.xml`** — returned `No matching routes
  found` or the SPA shell. Correct route located by probing: `/api/v1/skills`.
- **ClawHub `q=` search parameter** — accepted but silently ignored; returns the unfiltered first
  page. Worked around by paginating 1,198 records and filtering locally.
- **`https://arxiv.org/pdf/2602.20021v1` (PDF)** — downloaded successfully (6.5 MB, 19 pages) but not
  renderable in this environment (`pdftoppm` not installed). Worked around via the arXiv HTML
  rendering at `https://arxiv.org/html/2602.20021v1`, which carried the full text.
- **`plugin:github:github` MCP server** — failed to connect at session start (HTTP 400, malformed
  Authorization header). Worked around using the authenticated `gh` CLI, which had full access.
- **Discord (`https://discord.gg/clawd`)** — not attempted. Requires an account and is not indexable;
  logged as a known gap in §10 rather than a block.

No source was circumvented, and no access control was worked around.
