# Tooling Landscape: Background and Cloud Agents

**Research date:** 2026-08-30
**Ticket:** [#6 Tooling Landscape](https://github.com/AndrewGodlewsky/AI-Framework/issues/6) — strand: background and cloud agents
**Question:** When an agent runs on someone else's machine with no human present — triggered by an
issue, a label, a webhook, a schedule or an API call — and reports back with a pull request: what
actually changes about a developer's process, and **can any of these products merge?**

**Method.** Six product clusters worked in parallel against primary sources only: official
documentation, changelogs, API references, open-source repository contents, and first-party
engineering blogs. Vendor landing pages were read but are never cited as evidence of a capability;
where a capability appears only on a landing page, that is reported as the finding. Every claim
carries an inline URL and a date. Every figure carries an evidence tier.

**Scope.** This covers the *unattended* region — agents that start without a human in the moment and
hand back a pull request. Interactive CLI and IDE agents are a different strand. Review-side agents
appear here only where their behaviour bears on the merge question.

---

## Headline findings

### 1. The merge question has a clean answer, and it is not the one the category markets

**No product in this category merges its own pull request on its own judgement.** Across every vendor
examined, the merge action is either absent from the agent's tool surface, structurally forbidden by
the platform, or present only as *a button a human presses* in the vendor's own review UI.

The strongest vendor claim — Cognition's "The full loop, handled for you"
([cognition.com/blog/introducing-devin-2-2](https://cognition.com/blog/introducing-devin-2-2),
2026-02-24, first-party blog) — terminates at a reviewed pull request, and Cognition's own
documentation says so: *"Human engineers review PRs created by Devin before choosing whether to merge
the code changes"* and *"Devin is subject to the exact same branch protections and SDLC policies as
any human engineer"*
([docs.devin.ai/essential-guidelines/sdlc-integration.md](https://docs.devin.ai/essential-guidelines/sdlc-integration.md),
retrieved 2026-08-30).

The one product whose documentation contains a merge verb is **Devin Review** — and the actor is a
person. "Merge — Merge the PR using the repository's configured merge strategy (merge commit, squash,
or rebase)" describes a button in Devin's own web UI
([docs.devin.ai/work-with-devin/devin-review.md](https://docs.devin.ai/work-with-devin/devin-review.md),
retrieved 2026-08-30). What Devin supplies is a *credential* good enough to merge — "Write features
(comments, reviews, merge actions, code changes from chat) require a GitHub App connection installed
on your GitHub organization. PAT-based connections are read-only and cannot post comments, submit
reviews, or perform merge actions" — not an agent that decides to.

### 2. GitHub forbids its own agent in writing, at four separate points

The single most quotable artifact in the strand. GitHub Docs, *Risks and mitigations for GitHub
Copilot cloud agent*
([docs.github.com](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations),
retrieved 2026-08-30), verbatim:

> "Copilot cloud agent cannot mark its pull requests as 'Ready for review' and cannot approve or
> merge a pull request."
>
> "Draft pull requests created by Copilot cloud agent must be reviewed and merged by a human."
>
> "Prevents the user who asked Copilot cloud agent to create a pull request from approving it."
>
> "When Copilot cloud agent opens a pull request under its own app identity, one more approval is
> required before it can be merged, as long as the repository already requires at least one
> approval."

Four distinct mechanisms: the agent cannot call merge; it cannot even mark its own PR ready for
review; the *requester* is disqualified from approving; and the agent's app identity **adds** a
required approval rather than satisfying one. The platform hosting nearly all of the observable
agent-PR population has engineered the far end out of its own product.

The same page constrains the write surface itself: *"Copilot cloud agent only has the ability to push
to a single branch"*, *"Copilot cloud agent can only perform simple push operations"*, *"Only users
with write access to the repository can trigger Copilot cloud agent"*, and — from the responsible-use
page — *"Copilot cannot push directly to your default branch (for example, `main`)"* and *"The cloud
agent does not have access to Actions organization or repository secrets"*
([docs.github.com/en/copilot/responsible-use/agents](https://docs.github.com/en/copilot/responsible-use/agents),
retrieved 2026-08-30).

### 3. The exception nobody expected: Cursor's agent can be granted the power to approve

Cursor documents the opposite posture. On the Automations page
([cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations), retrieved
2026-08-30), verbatim:

> "If you enable approvals, the agent can also approve, request changes, and dismiss reviews.
> Otherwise, it can only post comments."

Cursor's cloud agents act through the **Cursor GitHub App**, not a user's credentials — "agents reach
your code through the Cursor GitHub or GitLab App, not through any single person's credentials"
([cursor.com/docs/integrations/github](https://cursor.com/docs/integrations/github), retrieved
2026-08-30) — and a GitHub App's `APPROVE` review *does* count toward required approvals. An
organisation that enables this creates a documented path by which a required human approval is
satisfied by an agent, and by which existing approvals can be **dismissed** by an agent. Cursor's docs
carry no warning on that sentence, do not say who may enable it, and do not mention branch protection
in that context.

Cursor's automation tool list still contains no merge action — the complete list is "Pull request
creation, Comment on pull request, Request reviewers, Send to Slack, Read Slack channels, MCP server,
Memories, Computer use." So the path is *approve, then GitHub's native auto-merge lands it*, not *the
agent merges*.

**This is the shape of every real far-end mechanism found: not an agent that merges, but a human who
pre-authorises a merge that then happens without them.** Devin's own version is explicit — "Enable or
disable GitHub auto-merge from the merge button dropdown. When enabled, the PR will merge
automatically once all required checks pass"
([docs.devin.ai/work-with-devin/devin-review.md](https://docs.devin.ai/work-with-devin/devin-review.md)).
The authorising act is human and prior, not agentic.

### 4. Where the constraint is a default rather than a law, vendors document how to remove it

Four switches, all documented, all admin-controlled:

- **GitHub's workflow-approval gate is a repository setting.** "Require approval for workflow runs"
  under Settings → Copilot → cloud agent; "You must be a repository administrator to configure these
  settings." GitHub publishes the consequence in its own words: *"Allowing GitHub Actions workflows to
  run without approval may allow unreviewed code written by Copilot to gain write access to your
  repository or access your GitHub Actions secrets."*
  ([docs.github.com](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/configuring-agent-settings),
  retrieved 2026-08-30)
- **Incompatible rulesets can be bypassed rather than obeyed.** *"If you have configured a ruleset or
  branch protection rule that isn't compatible with Copilot cloud agent, access to the agent will be
  blocked. For example, a rule that only allows specific commit authors can prevent Copilot cloud
  agent from creating or updating pull requests"* — remedied by "adding Copilot as a bypass actor to
  enable access"
  ([docs.github.com](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent),
  retrieved 2026-08-30). Note what this does *not* do: bypass-actor status does not give the agent the
  merge call, which is refused at the agent level, above the ruleset layer.
- **Jules' plan approval — widely described as the human gate — is opt-in for programmatic use and
  time-decaying in the UI.** *"By default, sessions created through the API will have their plans
  automatically approved"* ([jules.google/docs/api/reference/](https://jules.google/docs/api/reference/));
  *"If you navigate away, Jules will eventually auto-approve the plan, which is set on a timer"*
  ([jules.google/docs/review-plan/](https://jules.google/docs/review-plan/), both retrieved
  2026-08-30). It is a review affordance, not a structural gate.
- **GitHub's own "authors cannot approve" rule has an Actions-shaped hole that is off by default.**
  "Pull request authors cannot approve their own pull requests"
  ([docs.github.com](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews),
  retrieved 2026-08-30) — but the organisation setting **"Allow GitHub Actions to create and approve
  pull requests"** exists and can be switched on, with GitHub's own warning that *"Allowing workflows,
  or any other automation, to create or approve pull requests could be a security risk if the pull
  request is merged without proper oversight"*
  ([docs.github.com](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization),
  retrieved 2026-08-30). It is a default, not a law.

### 5. The trigger surface is now genuinely unattended, and it is recent

Every major vendor shipped cron and event triggers within roughly the last fifteen months.

- **GitHub Automations** — schedule (hourly/daily/weekly), issue created, PR opened, PR synchronized —
  shipped **2026-06-02**
  ([github.blog](https://github.blog/changelog/2026-06-02-schedule-and-automate-tasks-with-copilot-cloud-agent/));
  comment triggers added **2026-08-03**
  ([github.blog](https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments/)).
  The REST task API shipped **2026-05-13**
  ([github.blog](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api/)).
- **Cursor Automations** — cron, "Pull request opened / pushed / merged", "Push to branch", "CI
  completed", "PR review submitted", Slack message and emoji reaction, generic webhook POST, Linear,
  Sentry and PagerDuty incident events
  ([cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations)).
- **Devin Automations** — Slack, GitHub (issue comment, PR opened/synchronised, review, CI check-run
  `conclusion = failure`, push), Linear, iCalendar RRULE schedules, generic webhooks with bearer-token
  auth added **2026-08-21** ([docs.devin.ai/release-notes/2026.md](https://docs.devin.ai/release-notes/2026.md)) —
  plus a persistent "auto-triage" Devin that "watches the channel 24/7"
  ([docs.devin.ai/product-guides/auto-triage.md](https://docs.devin.ai/product-guides/auto-triage.md)).
- **Codex** — automatic PR reviews with no mention required ("Codex will post a review whenever
  someone opens a new PR for review, without needing an `@codex review` comment"), and via Linear
  triage rules: "Linear assigns new issues that enter triage to Codex automatically"
  ([learn.chatgpt.com/docs/third-party/linear](https://learn.chatgpt.com/docs/third-party/linear),
  retrieved 2026-08-30).
- **Jules** — GitHub issue label `jules` (**2025-06-26**), scheduled tasks (**2025-12-10**), and CI
  failure auto-fix (**2026-02-19**) ([jules.google/docs/changelog/](https://jules.google/docs/changelog/)).

**The material consequence: a PagerDuty incident or a failing CI check can now open a pull request
with no human involved at any point before review.** That is a real change in a developer's process
and it is roughly eighteen months old.

### 6. What the human is left holding is review capacity, and the bottleneck moved rather than disappeared

The strongest public dataset in this category is Microsoft's ten-month account of Copilot coding agent
on `dotnet/runtime` (devblogs.microsoft.com, **2026-03-23**) — ⚠️ **vendor-reported** (Microsoft on a
Microsoft product), but on a *public* repository where the numbers are independently checkable, and it
reports unflattering ones. Agent PRs merged at **67.9%** (535 of 878) against 87.1% for Microsoft
humans; merged agent PRs averaged **16.5 review comments against 12.4**; **52.3%** of agent PRs needed
someone other than the author to push commits, against a 10.3% baseline. The author's own summary:

> "I opened nine PRs… in the span of a few hours. Those PRs need review… That means I quite quickly
> created 5 to 9 hours of review work, spread across team members who have their own
> responsibilities… The bottleneck has moved."

Set against that, *Habituation at the Gate* (arXiv:2606.22721 — **controlled study**, 400 repeat
reviewers, 11,429 reviews) measures approval of agent PRs rising **30.1% → 36.8%** while inline
comments fall **22%** and latency rises **3.5×**, with human-PR approval *declining* over the same
window. The thing the human is left holding is the thing that measurably degrades under load.

Note the framing this forces: what replaces the human is not review by another name. Codex's own docs
draw the line — *"Code review rules guide Codex; they don't replace tests, branch protections, or
required approvals"*
([learn.chatgpt.com/docs/third-party/github](https://learn.chatgpt.com/docs/third-party/github),
retrieved 2026-08-30). Every vendor in this category positions its agent-side checking as advisory and
names the engineered verification layer — tests, branch protection, required approvals — as the thing
that actually enforces.

### 7. Nobody publishes the outcome number, including the party that computes it

GitHub ships an API returning exactly the figure this category should be judged on —
`pull_requests.total_merged_created_by_copilot`, "Number of pull requests created by Copilot cloud
agent that were merged on this specific day"
([github.blog](https://github.blog/changelog/2026-02-19-pull-request-throughput-and-time-to-merge-available-in-copilot-usage-metrics-api/),
**2026-02-19**) — and publishes **no aggregate value of it**.

| Vendor | Published outcome figure | Tier |
|---|---|---|
| GitHub | **None.** Ships the metric API, publishes no aggregate | Emptiness finding |
| Cognition (Devin) | "67% of its PRs are now merged vs 34% last year" — no methodology, denominator or repo mix | Vendor-reported ([2025-11-14](https://cognition.com/blog/devin-annual-performance-review-2025)) |
| OpenAI (Codex) | **No merge rate, no acceptance rate.** Only "Codex reviews 100% of PRs" (coverage, not outcome) and "weekly PR volume has more than doubled since Q4" (no baseline, no attribution) | Vendor-reported / emptiness |
| Cursor | **None.** No merge rate, acceptance rate or autonomy figure in any doc, changelog or launch blog | Emptiness finding |
| Google (Jules) | "over 140,000 code improvements shared publicly" ([2025-08-06](https://blog.google/technology/google-labs/jules-now-available/)) — an activity count, not an acceptance rate | Vendor-reported |
| Amazon Q | "a small team of AWS developers upgraded over 1000 carefully chosen applications" (2024-06-17) — a raw count on a self-selected sample | Vendor-reported |
| Microsoft (`dotnet/runtime`) | **67.9% merge rate, 0.6% revert rate**, with the author's own caveat that "CCA PRs are not randomly sampled" | Vendor-reported, publicly checkable |

The only cross-vendor acceptance figures come from academia, on the open **AIDev** dataset
(arXiv:2507.15003): "OpenAI Codex achieves the highest acceptance rate at 64%, followed by Devin at
49% and GitHub Copilot at 35%." Those are **observational**, on public repositories with ≥100 stars,
and compare populations that were never randomly assigned. The only independent evaluation of a
single product found is Answer.AI's Devin study
([answer.ai, 2025-01-08](https://www.answer.ai/posts/2025-01-08-devin.html)): "Out of 20 tasks we
attempted, we saw 14 failures, 3 inconclusive results, and just 3 successes" — **practitioner
evaluation, n=20, single team, no control arm, and now roughly twenty months and several Devin major
versions stale.**

**The project's prior finding stands: outcomes at high delegation are barely measured, and the parties
holding the telemetry publish least.**

### 8. Two products in the category are dying or dead, and the docs are the evidence

- **Amazon Q Developer is being sunset.** Per the AWS DevOps blog (**2026-04-30**, first-party): new
  signups ended 2026-05-15; "Amazon Q Developer IDE plugins and paid Subscriptions will reach end of
  support on April 30, 2027, giving customers 12 months to transition to Kiro."
- **Windsurf no longer exists as a separate documentation surface.** `docs.windsurf.com/*` 307-redirects
  into `docs.devin.ai/*`; `windsurf.com/changelog` 308-redirects to `docs.devin.ai/desktop/changelog`.
  The Cognition acquisition is complete at the infrastructure level (verified 2026-08-30).
- **GitHub Copilot Workspace is gone from the docs.** The old docs URL
  `docs.github.com/en/copilot/using-github-copilot/using-copilot-workspace` returns **HTTP 404** —
  removal, not a redirect. The only primary transition signal located is a **2024-12-06** entry in
  `githubnext/copilot-workspace-user-manual` `changes.md`: "Copilot Workspace is graduating!" **No
  GitHub changelog post confirming a sunset date was found — stated plainly, unresolved.** Its
  successor, Copilot coding agent, reached GA **2025-09-25**
  ([github.blog](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/)).

**This is the fastest-ageing material in the project.** Between the ticket brief and this research,
Copilot "coding agent" was renamed "cloud agent" (undated in any changelog found), Cursor "Background
Agents" became "Cloud Agents" (Cursor 2.0, **2025-10-29**), and the entire OpenAI Codex documentation
site moved from `developers.openai.com/codex/*` to `learn.chatgpt.com/docs/*` via 308 redirects. Every
URL in the original brief for Codex, Cursor and Windsurf was stale.

---

## The table

Every row from primary documentation, retrieved **2026-08-30**. "Trigger (unattended)" lists only
mechanisms that start work with **no human in the moment** — interactive entry points are omitted.

| Product | Trigger (unattended) | Execution environment | Opens a PR? | **Can it merge?** | What stops it |
|---|---|---|---|---|---|
| **GitHub Copilot cloud agent** | Automations: cron hourly/daily/weekly, issue created, PR opened, PR synchronized, issue/PR comment; REST agent-tasks API | Ephemeral env "powered by GitHub Actions"; Ubuntu x64 or Windows 64-bit runner; default-on firewall with recommended allowlist | Yes — **draft only**, one PR per task | **No.** "cannot approve or merge a pull request" | Agent-level refusal; cannot mark its own PR ready for review; requester disqualified from approving; its app identity *adds* a required approval; workflows need human "Approve and run"; 59-min hard cap |
| **OpenAI Codex cloud** | Automatic PR review on open (no mention needed); Linear triage-rule delegation; GitLab MR open/every push | OpenAI-managed container, `universal` image, HTTP proxy; **agent-phase internet off by default**; secrets removed before agent phase | Human clicks "open a pull request"; agent *can* push to an existing PR branch | **No.** No merge sentence anywhere in 39,237 lines of docs | "branch protections, and required approvals continue to provide hard enforcement"; its own most-automated pipeline "**Never merges the generated change automatically**" |
| **Devin (Cognition)** | Automations: Slack, GitHub events incl. CI check-run failure, Linear assignment/label, RRULE cron, webhooks; 24/7 Slack auto-triage | Linux VM, snapshot-booted, shell + IDE + browser, Cognition AWS; egress allowlist ("All other outbound connections are blocked"); **Outposts** runs execution on customer infra | Yes | **No autonomous merge.** Merge is a **button a human presses** in Devin Review; GitHub auto-merge is a human toggle | Docs: "Human engineers review PRs created by Devin before choosing whether to merge"; no merge or approve endpoint in the API; merge absent from the Security-Profiles privilege ladder |
| **Google Jules** | GitHub issue label `jules`; scheduled tasks; CI-failure auto-fix; REST API; CLI | Short-lived Google Cloud VM, Ubuntu 24.04; **full internet access, no documented egress allowlist** | Yes — human clicks **Publish PR** | **No.** No merge, auto-merge or approve mechanism anywhere; API has no merge method | Publishing is a human action. ⚠️ The plan gate is **not** the constraint: API sessions auto-approve plans by default and the UI timer auto-approves |
| **Cursor cloud agents** | Automations: cron, PR opened/pushed/merged, push to branch, CI completed, PR review submitted, label changed, Slack, webhook POST, Linear, Sentry, PagerDuty | Cursor-managed isolated Ubuntu VMs, `.cursor/environment.json` + Dockerfile; **internet on by default**, three network modes | Yes (`autoCreatePR`), or push direct to the starting ref (`workOnCurrentBranch`) | **No merge action exists** — but **it can be granted the power to approve, request changes, and dismiss reviews** | No merge tool in the automation tool list; Administration scope is **read**-only, "to determine PR mergeability". ⚠️ Nothing stops the approve grant; no warning documented |
| **Claude Code on the web / Routines** | Routines: cron (min 1h), per-routine `/fire` HTTP endpoint with bearer token, GitHub PR and Release events with filters; PR auto-fix on CI failure or review comment | Isolated Anthropic-managed VM (or customer self-hosted); credentials held outside the sandbox behind a proxy; **Trusted** allowlist default, off-list = `403 host_not_allowed` | Yes — human creates the PR from the session | **No.** No merge mechanism documented | Pushes only to `claude/`-prefixed branches unless the target passes three checks (not protected, no one else's open PR, no other author's commits); PR creation is a human step |
| **`claude-code-action`** | `workflow_dispatch`, `schedule`, `issues: [opened, assigned, labeled]`, plus a `prompt` input needing no `@claude` | Customer's own GitHub Actions runner; short-lived repo-scoped token | Pushes commits; acts by updating one comment | **No.** "For security reasons, Claude cannot approve pull requests"; "Cannot merge branches, rebase, or perform other git operations beyond pushing commits" | An explicit published limitations list — the only one in the strand |
| **Factory (Droids)** | Automations: cron / natural-language cadence, Slack, GitHub PR/push/comment/label/check events; Action `label_trigger`, `assignee_trigger`, `allowed_bots` | Customer CI runner, or Factory-managed Droid Computers (4 CPU / 8 GB, iptables inbound restriction, optional relay mode) | Yes | **No merge — but it approves and it blocks.** "Submits an approval when no issues are found"; `security_block_on_critical` submits REQUEST_CHANGES, default `true` | `git push` blocked below `--auto high`; no merge capability on any docs page |
| **Amazon Q Developer** ⚠️ *sunsetting* | GitHub label literally named "Amazon Q development agent"; `/q dev` comment; auto code review on PR open | AWS-hosted, US data processing, three fixed egress IPs; Java transform build is client-side | Yes | **No.** "you can merge the pull request" — links to GitHub's manual merge docs. No "auto-merge" occurrence found | End of support **2027-04-30**; new sign-ups closed **2026-05-15** |
| **GitLab Duo Agent Platform** | Flow triggers per foundational flow; service-account assignment | GitLab hosted runners on GitLab.com; self-managed needs `gitlab--duo`-tagged docker/k8s executor | Yes (MRs), incl. autonomous conflict-resolution pushes | **No merge, no approve documented** | Composite identity: "the merge request is attributed to the human user who triggered the flow"; more restrictive of the two roles applies |
| **Codegen** | Checks Auto-fixer on any failing check; PR Review on all PRs; Linear/Jira assignment; API | Codegen-hosted sandboxes; on-prem option | Yes ("Enable PR Creation" toggle) | **No.** Permissions page has exactly three toggles and none is merge or approve; API has no merge endpoint | The permission surface itself. Auto-fixer capped at 3 attempts per PR |
| **Ellipsis** | `pull_request` (6 actions), `push`, `issue`, `linear_issue`, Sentry `issue_alert` / `metric_alert`, Slack, cron, API, CLI | Per-session sandbox from committed `environment.yaml` | Yes | **No.** No merge, no approve | Credential-level: read-only agents "physically cannot push a commit"; "GitHub refuses with a 403" |
| **Qodo Merge / PR-Agent** | PR events (hosted); GitHub Action / webhook (OSS) | Hosted, or self-hosted Action | No (review-side) | Hosted: **no**. OSS: **yes, it approves** — `create_review(event="APPROVE")` behind `enable_auto_approval`, a key absent from the shipped config | Opt-in only, and **undocumented in the user-facing docs**. No merge function in the provider at all |
| **CodeRabbit** | Automatic review on PR open | CodeRabbit-hosted; self-hosted option | No (review-side) | **No merge — but the most explicit approve-and-block authority found.** `request_changes_workflow` (default `false`) auto-approves; pre-merge checks in `error` mode "block merges until resolved or manually overridden" | Approval is off by default; overrides configurable via `override_requested_reviewers_only` |
| **Sweep** ⚠️ *dead* | — | — | — | — | No code push since **2025-09-18**; README is a forwarding address to a JetBrains plugin |
| **Renovate** *(not an agent — the control case)* | cron / scheduled dependency scan | Self-hosted or Mend-hosted | Yes | **YES.** `automerge`: "Whether to automerge branches/PRs automatically, **without human intervention**"; `automergeType: "branch"` skips the PR entirely | Nothing, once enabled — the diffs are deterministic and CI-checkable |

**Read the last two rows together.** The only bot in this landscape whose documentation authorises it
to merge its own pull request is the one whose output a machine can fully check.

---

## Product detail

### GitHub Copilot cloud agent (formerly "coding agent")

**Naming, dated.** Public preview **2025-05-19**; GA **2025-09-25** — "Copilot coding agent, our
asynchronous, autonomous developer agent, is now generally available for all paid Copilot subscribers"
([github.blog](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/)).
Current documentation renders it as "Copilot **cloud** agent" throughout; **no changelog post dating
that rename was found.**

**Trigger surface.** Documented entry points: "GitHub — issues, agents tab, dashboard, Copilot Chat,
new repositories, and failing GitHub Actions runs", GitHub Mobile, VS Code / JetBrains / Eclipse /
Visual Studio 2026, REST API, GitHub CLI, GitHub MCP Server, Jira, Slack, Microsoft Teams, Azure
Boards, Linear, Raycast
([docs.github.com](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions),
retrieved 2026-08-30). The unattended path is **Automations**: "On a schedule: the automation runs at a
recurring interval—hourly, daily, or weekly", "When an issue is created", "When a pull request is
opened", "When a pull request is synchronized"
([docs.github.com](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations)),
plus issue-comment and PR-comment triggers added **2026-08-03**. Automations are configured per-tool:
"the tools available to the agent, such as 'create pull request' or 'update issue labels', so you have
full control over what your automation can do" — **"merge pull request" is not among the tools named
in either the changelog or the docs.** Automations are also not versioned with the repository:
"Automations are stored separately from your repository's contents. They are not committed to Git."

**Execution environment.** "Copilot has access to its own ephemeral development environment, powered
by GitHub Actions, where it can explore your code, make changes, execute automated tests and linters
and more." Runners: "only compatible with Ubuntu x64 Linux and Windows 64-bit runners." Customised via
`.github/workflows/copilot-setup-steps.yml`, whose "steps in this job will be executed in GitHub
Actions before Copilot starts working"
([docs.github.com](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment),
retrieved 2026-08-30). Billing: "Copilot cloud agent uses GitHub Actions minutes and AI credits."

**Firewall / egress.** "By default, Copilot's access to the internet is limited by a firewall." The
recommended allowlist covers OS package repositories, container registries, language package
registries, certificate authorities, and "Hosts used to download web browsers for the Playwright MCP
server." Administrators can enable, disable or delegate both the firewall and the recommended
allowlist at organisation and repository level, and add custom domain or URL-with-path entries.
GitHub's own warning: **"Disabling the firewall will allow Copilot to connect to any host, increasing
risks of exfiltration of code or other sensitive information."**
([docs.github.com](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall),
retrieved 2026-08-30)

**Can it merge? No — refused at the agent level.** See headline finding 2 for the four verbatim
constraints. Supporting mechanisms from the same page:

- Workflow gate: "By default, GitHub Actions workflows will not run automatically when Copilot pushes
  changes to a pull request"; a human with write access clicks **"Approve and run workflows"**. The
  gate is a repository setting an administrator can disable, with GitHub's published warning
  (headline 4).
- Chain-breaking: "An issue or pull request opened by an automation could trigger another
  automation… GitHub Actions workflows don't run on a pull request until a user with write access
  approves them, which prevents workflows from running automatically as part of such a chain."
- Untrusted-actor default: "Automations ignore events triggered by users without write access by
  default."
- Provenance: "Copilot cloud agent's commits are signed, so they appear as 'Verified'."

**Copilot code review is comment-only by construction** — "Copilot always leaves a 'Comment' review,
not an 'Approve' review or a 'Request changes' review. This means that Copilot's reviews do not count
toward required approvals for the pull request, and Copilot's reviews will not block merging changes"
([docs.github.com](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review),
retrieved 2026-08-30).

**"Agent merge" — the one place GitHub ships an agent that merges, and what it actually is.** The
GitHub Copilot **desktop** app (GA **2026-06-17**, macOS/Windows/Linux —
[github.blog](https://github.blog/changelog/2026-06-17-github-copilot-app-generally-available/))
documents:

> "When you want to merge a pull request, you can enable **agent merge** at the top of the app. Agent
> merge will prompt the workspace's Copilot session to read your pull request, fix what is blocking
> it, and merge it as soon as GitHub allows. It runs in the background, survives app restarts, and
> turns itself off once your pull request is merged."
> — [docs.github.com](https://docs.github.com/en/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests), retrieved 2026-08-30

Read forensically, this does not contradict "the cloud agent cannot merge." It is a **different
identity and a different trigger**: a local desktop session, switched on deliberately by a signed-in
user for one specific pull request, and bounded by "as soon as GitHub allows" — the same required
checks and approvals as any human merge. The app's own GA note frames it identically: sessions "open a
pull request that uses your team's existing checks and merge requirements." *Inference, labelled: the
docs do not state which identity performs the merge call. The desktop context and the phrase "as soon
as GitHub allows" are the basis for reading it as the user's authority delegated to a local agent,
not as new authority granted to the agent.*

**Confidence-gated automation, and its scope limit.** GitHub ships one of the very few documented
mechanisms tying an action gate to a confidence rating: "For each supported action, the automation
rates its confidence as high, medium, or low… Your repository has an automation level that sets the
confidence threshold: changes rated below it are held as suggestions, and changes at or above it apply
automatically", with "Cautious" as the default and "Full automation" available
([docs.github.com](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automation-rationale-and-approvals),
retrieved 2026-08-30). **Scope limit, stated plainly: this governs *issue* actions — labels, fields,
triage — not code merges.** It is not a counter-example to headline finding 1, and it should not be
cited as one.

**What it cannot do.** "Each Copilot cloud agent session has a maximum execution time of 59 minutes.
This is a hard limit that cannot be extended or bypassed." "Copilot can only work on one branch at a
time and can open exactly one pull request to address each task it is assigned." "Copilot can only
make changes in the repository specified when you start a task." "The cloud agent does not have access
to Actions organization or repository secrets." From a real deployment: "CCA runs on Linux only… CCA
can write code that targets Windows, but it can't compile or test it", and "**CCA cannot open PRs on
its own** — every CCA PR was created at the explicit request of a human with maintainer rights to the
repository" (devblogs.microsoft.com, **2026-03-23**).

---

### OpenAI Codex — cloud / web agent

⚠️ **Documentation relocation, established 2026-08-30.** Every `developers.openai.com/codex/*` URL
returns **HTTP 308** to `learn.chatgpt.com/docs/*`; the Codex docs are now folded into the ChatGPT
docs. Those pages carry **no publication or last-updated dates**, so every doc claim below is cited
"retrieved 2026-08-30" rather than given a doc date. A machine-readable condensed manual exists at
`learn.chatgpt.com/docs/codex-manual.md` (~2.1 MB, 39,237 lines) and was grepped in full for the merge
analysis.

**Trigger surface.** Web UI (`chatgpt.com/codex`). GitHub: `@codex review`, `@codex <anything else>`
(starts a cloud chat with the PR as context), `@codex security review`, and — the unattended one —
"Codex will post a review whenever someone opens a new PR for review, without needing an `@codex
review` comment"
([learn.chatgpt.com/docs/third-party/github](https://learn.chatgpt.com/docs/third-party/github)).
GitLab (Beta, **2026-08-19**) is richer: tasks from **issues** or merge requests via `@codex`, plus
automatic MR review on open, on every push, and an experimental "Smart Trigger". Linear is the most
fully unattended path: "In Triage rules, create a rule and choose Delegate > Codex… Linear assigns new
issues that enter triage to Codex automatically." Slack `@Codex`. CLI `codex cloud exec`, marked
**experimental**.

**Negative finding: there is no GitHub issue-assignment trigger and no REST API for cloud tasks.** A
full grep of the condensed manual found no page documenting assigning a GitHub issue to Codex, a label
trigger, or a webhook. The Codex SDK is explicitly local ("start, continue, and resume **local** Codex
threads"), and `openai/codex-action@v1` runs the local CLI on a runner (`codex exec`), not a cloud
task. **Worth recording as the category's characteristic failure mode: the Developers landing page
says the GitHub integration lets you "Assign work, review changes, and move toward a pull request",
while the GitHub documentation page itself documents only PR-comment triggers.**

**Execution environment.** Documented five-step lifecycle: container created and repository checked out
at the selected branch or SHA; setup script runs; internet-access settings applied; agent loop runs
terminal commands and reads `AGENTS.md` for project lint and test commands; agent presents an answer
and a diff. Default container image `universal`, with a published reference Dockerfile at
`github.com/openai/codex-universal` whose README concedes it is "not an identical environment but
should help for debugging and development". Container state cached "for up to 12 hours", invalidated
on script, environment-variable or secret change; on Business and Enterprise "caches are shared across
all users who have access to the environment." Setup scripts "run in a separate Bash session from the
agent, so commands like `export` do not persist into the agent phase." **No per-task duration cap is
documented anywhere** — the 12-hour figure is cache lifetime, not task length.

**Network policy — the specifics.** Verified directly at
[learn.chatgpt.com/docs/cloud/internet-access](https://learn.chatgpt.com/docs/cloud/internet-access),
retrieved 2026-08-30:

> "By default, Codex blocks internet access during the agent phase. Setup scripts still run with
> internet access so you can install dependencies."

> "For extra protection, restrict network requests to `GET`, `HEAD`, and `OPTIONS`. Requests using
> other methods (`POST`, `PUT`, `PATCH`, `DELETE`, and others) are blocked."

Allowlist presets: **None**, **Common dependencies** (73 published domains including `github.com`,
`pypi.org`, `npmjs.com`, `crates.io`, `docker.io`, `ghcr.io`), **All (unrestricted)**. All traffic
passes through an HTTP/HTTPS proxy. **Secrets are structurally withheld from the agent:** secrets "are
only available to setup scripts. For security reasons, secrets are removed before the agent phase
starts." Environment variables, by contrast, persist for the whole chat.

OpenAI publishes the risk in full, with a worked exfiltration example: enabling agent internet access
carries "Prompt injection from untrusted web content, Code or secret exfiltration, Downloading malware
or vulnerable dependencies, Pulling in content with license restrictions", illustrated by a hidden
instruction planted in a GitHub issue that pipes `git show HEAD` into a POST to an attacker host, and
closing "**Point Codex only to trusted resources and keep internet access as limited as possible.**"
Note the residual shape: the GET/HEAD/OPTIONS restriction that would defeat that exact example is
**opt-in**, not default-on once internet access is enabled.

**Can it merge? No, and OpenAI says so twice.**

> "Code review rules guide Codex; they don't replace tests, branch protections, or required approvals."
> — [learn.chatgpt.com/docs/third-party/github](https://learn.chatgpt.com/docs/third-party/github)

> "Codex Code Review is still an additional reviewer; tests, branch protections, and required approvals
> continue to provide hard enforcement."
> — `developers.openai.com/blog/custom-code-review-rules-for-codex` (OpenAI engineering blog, undated)

A full grep for `merge|merged|merging` in pull-request context found **no sentence describing Codex
merging a pull request**. Opening the PR is a human step in the web UI ("Review the summary and diff…
**or open a pull request** when the work is ready") and in Linear ("Codex… posts a summary and a link
to the completed chat **so you can create a pull request**"). The one autonomous write path is
appending commits to an already-open PR branch: Codex "can push a fix back to the branch when it has
permission to do so."

**The most automated pipeline OpenAI documents hard-codes the human merge gate.** Codex Security's
GitLab CI remediation flow: "every generated change stays a **draft until a human reviews and merges
it**"; "Opens a draft merge request… **Never merges the generated change automatically**"; "Generated
changes always require human review before merge"
([learn.chatgpt.com/docs/security/cli/ci/gitlab](https://learn.chatgpt.com/docs/security/cli/ci/gitlab)).

**Identity is under-documented on GitHub and explicit on GitLab.** The GitHub bot handle appears only
in screenshot alt text (`chatgpt-codex-connector`), and the public GitHub App listing does not publish
its permission set. GitLab, by contrast, documents a personal access token with `api` scope at
Developer access, acting as a "ChatGPT Codex Connector instance service account". **Stated plainly:
the GitHub-side scopes could not be established from primary sources.**

**Rate limits as an unattended-operation constraint.** "On ChatGPT plans, local messages and cloud
chats share a five-hour rolling window", and "Cloud chats on ChatGPT plans use GPT-5.6 Sol and may use
more of your allowance than local messages"
([learn.chatgpt.com/docs/pricing](https://learn.chatgpt.com/docs/pricing)). An unattended trigger loop
draws on a shared rolling budget on the most expensive model, with **no documented per-task time cap
to bound a runaway task**.

---

### Devin (Cognition)

**Trigger surface.** The authoritative surface is **Automations** — "event-driven workflows that start
Devin sessions from Slack, GitHub, Linear, schedules, and webhooks"
([docs.devin.ai/product-guides/automations.md](https://docs.devin.ai/product-guides/automations.md),
retrieved 2026-08-30). GitHub events include issue comments, PR opened/synchronised, PR review, review
comment, push, and **CI check-run `conclusion = failure`**. Linear assignment is fully unattended:
"Assign the ticket to Devin directly in Linear. Devin will use the default playbook… to start working
on the ticket"; label triggers `!plan`, `!implement`, `!triage`, `!review`. Webhooks gained
bearer-token auth **2026-08-21**. Scheduled sessions use standard cron expressions. The API is
`POST https://api.devin.ai/v3/organizations/{ORG_ID}/sessions`, authenticated with `cog_`-prefixed
service users or PATs, with `create_as_user_id` to attribute a session to another team member. The most
autonomous surface is **auto-triage**: "a persistent Devin that monitors your Slack channel", which
"watches the channel 24/7" and "spawns focused child sub-devins".

**Negative finding:** GitHub *issue assignment* is **not** documented as a trigger. GitHub entry is via
Automations conditions or a `/devin` comment. This is a real difference from Jules and Copilot.

**Execution environment.** "Devin's environment is… a Linux-based virtual machine with your
repositories cloned, tools installed, dependencies resolved, environment variables set"
([docs.devin.ai/onboard-devin/environment.md](https://docs.devin.ai/onboard-devin/environment.md)).
Snapshot-based: sessions boot from "a frozen, bootable image", and "Session changes don't persist back
to the snapshot." Tooling is Shell + IDE + Browser; the browser lets Devin "browse through
documentation, test web applications it builds, download/upload information." Hosted in "Cognition's
AWS cloud environment". **Devin Outposts** (shipped **2026-07-22**, "disabled by default") moves
execution on-premises: "Devin's agent loop (inference and planning) continues to run in Devin's cloud,
while all command execution, file edits, and repository access happen on machines you operate"
([docs.devin.ai/cloud/outposts/overview.md](https://docs.devin.ai/cloud/outposts/overview.md)). Egress
is governed by Security Profiles allowlists — "All other outbound connections are blocked" — alongside
AI Guardrails that "detect prompt injection, data exfiltration attempts, and policy violations" with
`log_only` / `warn_user` / `block_message` enforcement.

**Can it merge? The credential can; the agent is not documented to decide to.** Devin Review's merge
control is a UI button: "Merge — Merge the PR using the repository's configured merge strategy (merge
commit, squash, or rebase)", alongside "Enable or disable GitHub auto-merge from the merge button
dropdown. When enabled, the PR will merge automatically once all required checks pass." The write
ceiling is set by connection type: "Write features (comments, reviews, merge actions, code changes from
chat) require a GitHub App connection installed on your GitHub organization. PAT-based connections are
read-only and cannot post comments, submit reviews, or perform merge actions"
([docs.devin.ai/work-with-devin/devin-review.md](https://docs.devin.ai/work-with-devin/devin-review.md),
retrieved 2026-08-30).

**The docs contain one sentence that presupposes agent merging, and it is a security recommendation
rather than a capability statement:** "We recommend enabling branch protection rules on your main
branch to ensure all required checks pass **before Devin can merge changes**"
([docs.devin.ai/integrations/gh.md](https://docs.devin.ai/integrations/gh.md)). Set against it, two
explicit statements in the SDLC guide: "Human engineers review PRs created by Devin before choosing
whether to merge the code changes" and "Devin is subject to the exact same branch protections and SDLC
policies as any human engineer." The API index carries **no merge endpoint and no approve endpoint**;
the session tool list (Shell, IDE, Browser, Side Chats, Progress Tab) contains no PR-merge tool; and
Security Profiles' maximum git privilege is push plus PR opening, with merge absent from the ladder.
**Devin Review does not approve PRs** — it posts findings as comments, with no documented `APPROVE`
submission.

**Stacked PRs are the one place Devin owns merge machinery.** "Merging a PR in the stack also merges
every open PR below it, atomically, in a single operation"; "stacked PRs cannot be merged through
GitHub's regular merge flow; they merge through the stack merge"
([docs.devin.ai/work-with-devin/stacked-prs.md](https://docs.devin.ai/work-with-devin/stacked-prs.md)).
The trigger is a human in Devin Review; Devin executes the cascade.

**Verdict on "end to end".** Cognition's blog claim — "Devin doesn't just write code and hand it off.
It plans, codes, reviews its own output, catches issues, and fixes them" / "The full loop, handled for
you" ([cognition.com/blog/introducing-devin-2-2](https://cognition.com/blog/introducing-devin-2-2),
**2026-02-24**) — describes a loop terminating at a reviewed PR. The constraint that makes "end to end"
false is in Cognition's own documentation: a human chooses whether to merge. The documented path to
unattended landing is GitHub's native auto-merge, toggled by a human in advance.

**Commercial model as an operational constraint.** ⚠️ **The ACU definition is no longer publicly
documented** — `docs.devin.ai/product-guides/acu-usage` returns **HTTP 404**. Surviving text describes
consumption only qualitatively: usage accrues from "Number and complexity of actions Devin takes
(planning, context gathering, task execution, browser actions, code execution, and so on)" plus VM time
and bandwidth ([docs.devin.ai/admin/billing/usage.md](https://docs.devin.ai/admin/billing/usage.md)).
No minutes-per-ACU or dollars-per-ACU conversion appears in current public docs. Self-serve pricing:
Free; Pro $20/month; Max $200/month; Teams $80/month minimum, $40/month per full seat. "There are no
concurrent session limits"; Devin "typically sleeps automatically after roughly 0.1 ACUs of inactivity";
session-level ACU hard caps shipped **2026-04-03**.

**What it cannot do.** There is **no explicit "Devin cannot" list** — a notable absence for a product
marketed on autonomy. Hard limits found: sessions "can't be continued after 30 days". Deployment is the
clearest prohibition — only "static frontends, served from `devinapps.com`" and "FastAPI backends,
deployed to Fly.io"; "Devin is not equipped to deploy pre-existing applications to Cognition-hosted
infrastructure"; deployment requires explicit user approval per deploy and is **disabled entirely for
enterprise organizations**
([docs.devin.ai/product-guides/deployment-capabilities.md](https://docs.devin.ai/product-guides/deployment-capabilities.md)).
Also: "For iOS apps, Devin doesn't have access to a phone emulator." And an honest first-party
admission: "Devin can still experience hallucinations, introduce bugs into code, or suggest insecure
code" ([docs.devin.ai/admin/security.md](https://docs.devin.ai/admin/security.md)).

---

### Google Jules

**Trigger surface.** GitHub issue label — "You can start a task from a GitHub issue by applying the
label 'jules' (case insensitive)"
([jules.google/docs/running-tasks/](https://jules.google/docs/running-tasks/)), shipped **2025-06-26**.
REST API `POST https://jules.googleapis.com/v1alpha/sessions`, `X-Goog-Api-Key` auth, max three keys
per account, shipped **2025-10-03**. CLI `jules remote new --repo … --parallel <n>`, **2025-10-02**.
Scheduled tasks **2025-12-10**. PR-comment response **2025-09-23**. CI-failure auto-fix **2026-02-19**
— Jules detects GitHub Actions failures, analyses logs and resubmits fixes. Render deploy-failure
fixes **2025-12-10**. All dates from
[jules.google/docs/changelog/](https://jules.google/docs/changelog/), retrieved 2026-08-30.

**Execution environment.** "Jules runs each task inside a secure, short-lived virtual machine (VM).
This lets it clone your repository, install dependencies, and run tests"
([jules.google/docs/environment/](https://jules.google/docs/environment/)). Ubuntu 24.04 LTS base with
Node, Bun, Python, Go, Java, Rust, C/C++, Docker, git, curl, jq, make. **Full internet access, with no
documented egress allowlist** — "a secure, cloud-based virtual machine (VM) with internet access"
([jules.google/docs/faq/](https://jules.google/docs/faq/)). That is the sharpest environmental contrast
in the strand: Copilot, Codex and Devin all restrict egress by default; Jules documents none. `AGENTS.md`
is supported. Setup scripts plus "Run and Snapshot" produce reusable environment snapshots
(**2025-08-05**); MCP is restricted to allowlisted servers (**2026-02-02**).

**Can it merge? Unambiguously no.** "Click **Publish branch** or **Publish PR** to push Jules' changes
to GitHub" ([jules.google/docs/code/](https://jules.google/docs/code/)); after publishing you can "send
it for review, or merge the PR into your codebase" — second person, human actor. Identity: "Jules will
appear as a commit author on the branch"; "When publishing a PR, Jules will appear as the creator of
the PR." Access is via the **Google Labs Jules** GitHub App, scoped per repository: "Jules can only
access repositories you explicitly allow through GitHub". **No merge, auto-merge or PR-approval
mechanism appears anywhere in Jules' docs, changelog or API reference, and the API has no merge
method.**

**The plan gate is weaker than commonly claimed** — see headline finding 4. Two documented escapes: a
UI timer that auto-approves ("If you navigate away, Jules will eventually auto-approve the plan, which
is set on a timer" — duration undocumented), and an API default of no approval ("By default, sessions
created through the API will have their plans automatically approved"), with `requirePlanApproval` and
`automationMode` fields and an explicit `:approvePlan` endpoint for when approval *is* required.

**What it cannot do.** Cannot "run long-lived processes like dev servers"; watch scripts unsupported in
setup. Documented failure modes: incomplete setup scripts, "prompts that are too vague or overly
broad", "repos with unusual or nonstandard build systems"
([jules.google/docs/errors/](https://jules.google/docs/errors/)). Hard quotas
([jules.google/docs/usage-limits/](https://jules.google/docs/usage-limits/)): daily tasks Free **15** /
Pro **100** / Ultra **300**; concurrent tasks **3** / **15** / **60**; "task limits are not shared or
pooled." No documented session-duration or repository-size cap.

**Security posture is markedly thinner than its peers.** No SOC 2 statement, no data-residency
statement, no VPC or self-hosted option, and no egress allowlist in the docs. What exists: "Jules does
not train on private repository content"; per-repository GitHub App scoping; integration keys
"encrypted and stored securely". The documented posture is largely a liability transfer: **"You are
responsible for the code you run."** Jules also never documents its GitHub App scopes, so its write
ceiling cannot be established from primary sources.

---

### Cursor cloud agents (formerly "background agents")

**Renamed** in Cursor 2.0, **2025-10-29**. Background agents shipped in early preview **2025-05-15**
(Cursor 0.50), GA with Bugbot **2025-06-04** (Cursor 1.0), Slack **2025-06-12**, web/mobile
**2025-06-30**, Linear **2025-08-21**, SDK **2026-04-29**. `docs.cursor.com/*` now 308-redirects to
`cursor.com/docs/*`.

**Trigger surface.** Cursor Desktop, Cursor Web (`cursor.com/agents`), Cursor iOS, Slack `@cursor`,
GitHub/Bitbucket `@cursor` comment on PRs or issues, Linear, and the API. The unattended surface is
**Automations**: cron; SCM events "Draft opened", "Pull request opened", "Pull request pushed", "Pull
request merged", "Push to branch", "Comment added"; GitHub-specific "Pull request label changed",
"Issue label changed", "CI completed", "PR review submitted", "Workflow run completed"; Slack message
and emoji reaction; generic webhook POST; Linear; Sentry issue events; PagerDuty incident events
([cursor.com/docs/cloud-agent/automations](https://cursor.com/docs/cloud-agent/automations), retrieved
2026-08-30).

The **Cloud Agents API** carries `POST /v1/agents`, `POST /v1/agents/{id}/runs`, run streaming and
cancel. Two request fields are load-bearing: **`autoCreatePR`** (open a PR on completion) and
**`workOnCurrentBranch`** (push to the starting ref rather than a new branch) — the second is a
documented direct-push-to-branch path. Cursor's own webhooks are **report-only**: the sole event is
`statusChange`, HMAC-SHA256 signed; they cannot start agents.

**Execution environment.** "Cloud agents run on isolated Ubuntu machines" and "Cursor manages VM
provisioning, isolation, snapshots, startup, artifacts, and capacity for every Cloud Agent"
([cursor.com/docs/cloud-agent/setup](https://cursor.com/docs/cloud-agent/setup)). Configuration is
`.cursor/environment.json` with `build`, `install`, `snapshot`, `start` and `terminals`. "You configure
the environment with a Dockerfile; you do not get direct access to the remote machine." There is **no
self-serve BYO-compute**; what exists is AWS IAM role assumption for permissions
(`CURSOR_AWS_ASSUME_IAM_ROLE_ARN`, STS credentials expiring after one hour). Secrets: "Encrypted secret
storage, redacted runtime secrets kept out of the model, build-only secrets scoped to the Docker
build", using "AES-256, with per-agent keys". VM snapshots retained 90 days.

**Security posture — Cursor is unusually blunt, and worth quoting in full**
([cursor.com/docs/cloud-agent/security](https://cursor.com/docs/cloud-agent/security), retrieved
2026-08-30):

> "Cloud Agents auto-run terminal commands so they can iterate on tests without stopping for approval
> on every step. **This is more autonomous than the foreground agent, and it changes the risk model.**"

> "The agent has internet access by default."

> "Auto-running introduces data exfiltration risk: attackers could execute prompt injection attacks,
> tricking the agent to upload code to malicious websites"

> Run Modes are "**best-effort guardrails rather than a hard security boundary**."

Three network modes exist — allow all, default plus allowlist, allowlist-only — and enterprise
administrators can lock the choice organisation-wide. Cursor's own worked example notes that a wildcard
S3 allowlist entry "opens egress to every bucket in the region and creates an exfiltration path for a
prompt-injected agent."

**Can it merge? No — but it can be granted the power to approve.** See headline finding 3. The GitHub
App permission grid is instructive: "Administration" is requested to "**Read** branch protection and
required check rules to determine PR mergeability" — read, to *determine* mergeability, not to effect
it. "Pull requests" is scoped to "Create PRs and leave review comments". Access is inherited: "A Cloud
Agent can only reach repositories the triggering user could already reach."

The capabilities page says cloud agents "open a PR, then respond to review comments and CI failures
until it merges" — parse carefully: the agent iterates *until the PR merges*, it is not the merging
party.

**Bugbot is comment-only and non-blocking by default.** It "analyzes PR diffs and leaves comments with
explanations and fix suggestions", posting a check named `Cursor Bugbot` with conclusions `success`,
`neutral` and `failure`; critically, "**Requiring the status alone does not block merges on findings
because findings default to `neutral`**"
([cursor.com/docs/bugbot](https://cursor.com/docs/bugbot), retrieved 2026-08-30). It does not submit a
formal review, so it cannot count as an approval. Making it block requires opt-in fail-on-unresolved.

**What it cannot do.** No auto-fix on human commits; a maximum of 10 CI-failure follow-ups per PR;
SSE and `mcp-remote` unsupported; long-running unavailable for multi-repository environments; computer
use is enterprise-only. **No documented cap on concurrency, session length, or spend** — a genuine gap
for unattended operation. The best-practices page contains **no statement requiring human review before
merge**; its only framing is "Think of the agent as a smart, but low-context human developer."

---

### Amazon Q Developer — and its announced end of life

⚠️ **Being sunset.** Per the AWS DevOps blog (**2026-04-30**, first-party): new sign-ups ended
**2026-05-15**; "Amazon Q Developer IDE plugins and paid Subscriptions will reach end of support on
**April 30, 2027**, giving customers 12 months to transition to Kiro." Code transformation is
explicitly included.

**Trigger surface.** The GitHub trigger is a label whose name is exact: the label "must be named as
**Amazon Q development agent** in order for it to be recognized"
([docs.aws.amazon.com](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/github-feature-development.html),
retrieved 2026-08-30). Also `/q dev` as an issue comment; code review triggers automatically "when a
new pull request is created or a closed pull request is reopened", or via `/q review`. GitLab Duo quick
actions (`/q dev`, `/q review`, `/q test`, `/q transform`) reached GA **2025-04-17**; the GitHub
integration preview was announced **2025-05-05**.

**Execution environment.** No architecture page was found. The available evidence is three fixed egress
IPs published for allowlisting and "The Amazon Q Developer integration with GitHub processes data in
the United States" — implying AWS-hosted rather than customer-account or Actions runners. Notably, **no
AWS account is required** at the free tier. For Java transformation the build is client-side: "the
initial and validation builds use the client-side environment."

**Can it merge? No.** "When Amazon Q Developer finishes generating code changes for the feature
development, it comments on the issue and opens a pull request… If you're satisfied with the suggested
code changes, **you can merge the pull request**" — linking out to GitHub's own manual-merge
documentation. A targeted grep for "auto-merge" returned **no occurrence in any fetched Amazon Q
Developer page**. GitLab Duo mirrors this: "The agent will automatically open up a merge request for me
to review."

**Documented limits — the most explicit in the strand.** Java transform is Maven-only, Java 8/11/17/21
→ 17/21, build must finish in **≤55 minutes**, no VPC or on-premises access during build. .NET:
1,000,000 LOC/month Pro against 1,000 for BuilderID; concurrency 10 against 1. Pro transform 4,000
LOC/month pooled; 1,000 agentic requests/month. CodeCatalyst dev agent: 30 invocations/month/user.

⚠️ **Research-integrity note.** Four unrelated AWS documentation pages each returned an identical
trailing block instructing the reader to run an `aws agent-toolkit search-skills` command, styled as
documentation content. Verbatim repetition of a command-promotion snippet across unrelated pages is
inconsistent with AWS doc authoring and resembles injected content in the fetch pipeline. **The command
was not run and the content was treated as untrusted.** Recorded rather than acted on.

---

### Anthropic — Claude Code on the web, Routines, and `claude-code-action`

Anthropic's unattended surface is three separate products with three different identity models, and the
differences matter more than the similarities.

**Claude Code on the web** — "in research preview for Pro, Max, and Team users, and for Enterprise
users with premium seats or Chat + Claude Code seats". It "runs tasks on Anthropic-managed cloud
infrastructure at claude.ai/code, or on your organization's self-hosted environment when routed there"
([code.claude.com/docs/en/claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web),
retrieved 2026-08-30). Sessions run in "an isolated, Anthropic-managed VM"; "git credentials and
signing keys stay outside the sandbox, and a proxy authenticates on the session's behalf with scoped
credentials." Parallel sessions are explicit — each `claude --cloud` invocation "creates its own cloud
session that runs independently" — and `--teleport` pulls a cloud session and its branch into a local
terminal.

**Routines are the unattended trigger surface, and Anthropic states the autonomy plainly.** A routine
is "a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors",
with three trigger types — **Scheduled** (hourly/daily/weekdays/weekly, custom cron via
`/schedule update`, minimum interval one hour), **API** (`POST
https://api.anthropic.com/v1/claude_code/routines/{id}/fire` with a per-routine bearer token, behind
the `experimental-cc-routine-2026-04-01` beta header), and **GitHub** (Pull request and Release event
categories, with filters on author, title, body, base branch, head branch, labels, draft state and
merged state) ([code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines), retrieved
2026-08-30; research preview). Verbatim:

> "Routines run autonomously as full Claude Code cloud sessions: **there is no permission-mode picker
> and no approval prompts during a run.**"

> "Anything a routine does through your connected GitHub identity or connectors appears as you:
> **commits and pull requests carry your GitHub user**, and Slack messages, Linear tickets, or other
> connector actions use your linked accounts for those services."

> "Claude can use every tool from an included connector, **including writes, without asking for
> permission during a run**."

**Can it merge? No — and the push-side constraint is unusually specific.** Nothing in the Claude Code
on the web or Routines documentation describes merging a pull request; PR creation is a human action
in the session UI ("review changes, create a pull request"). The branch constraint is worth quoting in
full, because it is a mechanism rather than a policy:

> "Claude pushes its work to branches prefixed with `claude/`, which are always accepted. When your
> prompt directs Claude to push to another branch, Claude Code checks the push first and rejects it if
> any of the following is true: The branch is protected on GitHub; Someone else has an open pull
> request from that branch; The branch carries commits authored by someone other than you."
> — [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines), retrieved 2026-08-30

**Network policy.** Cloud environments carry an access level; the **Default** environment uses
**Trusted** — "allows only the default allowlist of package registries, cloud provider APIs, container
registries, and common development domains through the session's network", with off-allowlist requests
failing with "`403` and `x-deny-reason: host_not_allowed`". The alternatives are **Custom** (own
allowlist, optionally plus the default list) and **Full** (unrestricted). MCP connector traffic routes
through Anthropic's servers rather than the session's network path, so connectors work without
allowlist changes — a design that also means connector egress is not governed by the environment's
network policy at all. Anthropic states the residual candidly: "When running with network access
disabled, Claude Code can still communicate with the Anthropic API, **which may allow data to exit the
VM**."

**Prompt-injection handling is architectural rather than advisory.** Text supplied to a routine's
`/fire` endpoint "arrives wrapped in a `<routine-fire-payload>` block that labels it as untrusted data
and tells Claude not to follow instructions inside it unless the routine's own prompt says to… Anyone
holding the bearer token can send `text`, so the wrapper makes fire text from a leaked token arrive
labeled as untrusted data rather than as direct instructions to your routine." And on the trigger
itself: "The trigger attests only that the prompt was stored ahead of time by an authorized session on
your account, so **the fired prompt is not live user input and can't act as approval or consent for
actions during the run.**"

**Auto-fix pull requests — the sharpest unattended-write surface, and it carries a warning worth
reproducing.** With auto-fix on, "Claude subscribes to GitHub activity on the PR, and when a check
fails or a reviewer leaves a comment, Claude investigates and pushes a fix if one is clear." Identity
again: "Claude may reply to review comment threads on GitHub as part of resolving them. **These replies
are posted using your GitHub account, so they appear under your username**, but each reply is labeled
as coming from Claude Code." Then, verbatim:

> "If your repository uses comment-triggered automation such as Atlantis, Terraform Cloud, or custom
> GitHub Actions that run on `issue_comment` events, be aware that **Claude can reply on your behalf,
> which can trigger those workflows.** Review your repository's automation before enabling auto-fix,
> and consider disabling auto-fix for repositories where a PR comment can deploy infrastructure or run
> privileged operations."

That is the clearest published statement anywhere in this strand of the second-order risk of
unattended agents: not that the agent merges, but that an agent writing a comment under a human's
identity can reach automation that does something irreversible.

**`claude-code-action` — the only product in the strand with an explicit published "cannot" list.**
From [`docs/capabilities-and-limitations.md`](https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/capabilities-and-limitations.md)
(retrieved 2026-08-30), verbatim:

> "Claude cannot submit formal GitHub PR reviews"
>
> "For security reasons, Claude cannot approve pull requests"
>
> "Cannot merge branches, rebase, or perform other git operations beyond pushing commits"
>
> "Claude only acts by updating its initial comment"
>
> "Claude only has access to the repository and PR/issue context it's triggered in"
>
> "Claude cannot execute Bash commands unless explicitly allowed using the `allowed_tools`
> configuration"

Note the contrast this sets up. Cursor's agent can be granted the power to approve and to *dismiss*
reviews; Anthropic's Action states flatly that it cannot approve, "for security reasons," and cannot
even submit a formal review of any kind. Both are documented positions; they point in opposite
directions.

**Triggers and access control for the Action.** The documented workflow subscribes to:

```yaml
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  issues:
    types: [opened, assigned, labeled]
  pull_request_review:
    types: [submitted]
```

plus a `prompt` input that runs "without requiring an `@claude` mention, allowing for scheduled or
automatic invocations". Access control, verbatim: "**The action can only be triggered by users with
write access to the repository**" — but "**Scheduled and dispatch events bypass this check**, since
GitHub itself requires write access to dispatch." Bots are blocked by default and can be allowed via
`allowed_bots`, with the caveat that "**Allowed bots are not checked for repository permissions.**" The
relaxation switch is `allowed_non_write_users`, which the docs mark as "**a significant security risk
and should only be used for workflows with extremely limited permissions**". The token is "a short-lived
token scoped specifically to the repository it's operating in" with no cross-repository access, and
GitHub App commits are automatically verified.

**Anthropic Code Review is built so it cannot gate.** Verbatim from
[code.claude.com/docs/en/code-review](https://code.claude.com/docs/en/code-review) (verified in this
project 2026-08-28):

> "Findings are tagged by severity and don't approve or block your PR, so existing review workflows
> stay intact."
>
> "The check run always completes with a **neutral** conclusion so it never blocks merging through
> branch protection rules. If you want to gate merges on Code Review findings, read the severity
> breakdown from the check run output in your own CI."

GitHub counts a `neutral` conclusion as passing, so a repository can require the check and still merge
with findings outstanding. Anthropic then documents the exact recipe for building the gate it declined
to ship.

**Headless mode and the sandbox — the containment story is weaker than it reads.** From the settings
reference (retrieved 2026-08-30): `sandbox.enabled` **defaults to `false`**; the sandbox **fails
open** — "if the sandbox cannot start because dependencies are missing or the platform is unsupported,
Claude Code shows a warning and runs commands without sandboxing" (hard failure requires
`sandbox.failIfUnavailable: true`); and `sandbox.network.strictAllowlist` **also defaults to `false`**,
under which an off-allowlist host is resolved by permission mode — denied in `dontAsk` mode, **allowed
in bypass-permissions mode**. **Net effect: the permission-skipping flag plus the built-in sandbox, at
default settings, gives no egress containment.** Anthropic's own scope statement: "The sandboxed Bash
tool on its own constrains only Bash, so it is not sufficient for fully unattended runs in either
mode"; Read/Edit/Write use the permission system directly, and "MCP servers and hooks are separate
processes that run unconstrained on the host." Linux enforcement is bubblewrap plus an optional seccomp
filter — **Landlock is not used and appears nowhere in the docs.** There is no TLS inspection by
default, so "code running inside the sandbox can potentially use domain fronting or similar techniques
to reach hosts outside the allowlist."

The docs state the consequence directly, and it is the cleanest containment sentence found in the
strand:

> "With no prompts to catch mistakes, **the isolation boundary you choose is what protects your
> system.** Always run `--dangerously-skip-permissions` sessions inside a container, a VM, or the
> sandbox runtime, so that file tools, MCP servers, and hooks are also inside the boundary."

and, drawing the distinction this project needs kept: "**The classifier is a per-action control, not
an isolation boundary.**"

Two further items bearing on unattended operation: `--max-turns` has "**No limit by default**", so an
unbounded agent loop is the default posture with `--max-budget-usd` as the only other stop; and the
`PermissionRequest` hook is the purpose-built unattended gate — "In sessions that can't show a prompt,
such as background subagents in non-interactive mode, Claude Code still runs these hooks, and **if no
hook returns a decision, it denies the tool call.**"

⚠️ **A concrete defect in the reference containment artifact.** The repository's devcontainer firewall
allowlist (last modified **2026-06-30**) omits `claude.ai`, `platform.claude.com`,
`downloads.claude.ai`, `mcp-proxy.anthropic.com` and `code.claude.com` — all listed as required in the
network-config documentation. **OAuth and subscription login therefore cannot complete inside the
reference container; it is effectively API-key-only.** The docs also disclaim it: "The firewall script
and these capabilities are **not required** for Claude Code itself."

**First-party outcome data: none for the unattended surfaces.** Anthropic publishes no merge rate,
acceptance rate, or PR-throughput figure for Claude Code on the web, Routines, or `claude-code-action`.
The frequently cited ">80% of Anthropic's code written by Claude" style claim is an *authorship*
measure, not an autonomy or outcome measure, and the accompanying first-party text says human code
review "has become a new bottleneck" — a statement about the same relocation Microsoft measured.

---

### The long tail — Factory, Codegen, Ellipsis, Qodo, CodeRabbit, GitLab Duo, Sweep

The frontier of *documented* authority in this tail is the **review event**, not the merge event.
Three products are documented to submit a GitHub `APPROVE` review; two are documented to submit
`REQUEST_CHANGES`; none is documented to merge.

**Factory (Droids) — alive, and the strongest PR-side authority found.** Newest changelog entry "CLI
v0.208.1 · Desktop v0.165.1 (August 29, 2026)"
([docs.factory.ai/changelog/release-notes.md](https://docs.factory.ai/changelog/release-notes.md)) —
one day before this research. Custom Automations take three trigger types: **Scheduled** ("Natural-
language cadence or cron schedule"), **Slack**, and **GitHub** ("pull requests, pushes, comments,
labels, or checks"), with run targets "a computer, Slack channel, or GitHub workflow"
([docs.factory.ai/software-factory/automations.md](https://docs.factory.ai/software-factory/automations.md)).
The GitHub Action (`Factory-AI/droid-action`, `action.yml` read at source) exposes `trigger_phrase`
(default `@droid`), `assignee_trigger`, `label_trigger` (default `droid`), and `allowed_bots`
("Comma-separated list of allowed bot usernames, or '\*' to allow all bots"). Execution is on the
customer's own CI runner, with egress pinnable via `experimental_allowed_domains`; the alternative is
Factory-managed **Droid Computers** (4 CPU, 8 GB RAM, "iptables rules to restrict inbound traffic to
the daemon port only", optional relay mode blocking all public traffic).

**Can it merge? It approves and it blocks. It does not merge.** Verbatim, from the docs — not a
landing page:

> "Submits an approval when no issues are found."
> — [docs.factory.ai/software-factory/code-review-ci.md](https://docs.factory.ai/software-factory/code-review-ci.md), retrieved 2026-08-30

and the inverse, as documented action inputs: `security_block_on_critical` — "Submit REQUEST_CHANGES
on critical findings", **default `true`**; `security_block_on_high` — same, default `false`. Push
authority is graduated through `droid exec --auto`: default read-only; `--auto low` allows low-risk
file edits; `--auto medium` adds "trusted package installs, builds, tests, `git commit`, `git
checkout`, and `git pull`" while **blocking `git push`**; `--auto high` enables "remote writes,
deployments, database migrations" including `git push`. The word "merge" does not appear as a
capability on the automations, Droid Control, or Release pages.

Note where that approval sentence lives: **one line buried in a CI setup guide.** A capability that
can satisfy a required-approvals rule is documented less prominently than the trigger phrase.

**Codegen — alive, and the clearest documented negative in the sweep**, because its permissions page
enumerates the whole surface. Exactly three toggles: "Enable PR Creation", "Enable Rules Detection",
"Enforce Organization-wide Signed Commits"
([docs.codegen.com/settings/agent-permissions.md](https://docs.codegen.com/settings/agent-permissions.md),
retrieved 2026-08-30). No merge permission, no approve permission, no protected-branch permission. The
API surface confirms the ceiling — *Edit Pull Request*, *Remove Codegen From Pr*, *Ban All Checks For
Agent Run* — **and no merge endpoint**. Two triggers run with no human at all: "Checks Auto-fixer -
Automatically fixes failing CI checks on agent PRs" (capped at "Default: 3 attempts per PR") and "PR
Review - Provides instant code review feedback on all PRs". ⚠️ **Docs-versus-docs conflict:** the
overview page says the agent can "review PRs, suggest changes, comment on issues, create branches,
commit code, and **manage repositories**" — loose prose that the concrete permissions page contradicts.
Whether the PR Review Agent posts `APPROVE` or `COMMENT` is **not stated anywhere** — unresolved.

**Ellipsis — alive, and substantially re-platformed** from a PR reviewer into a cloud-agent runtime
(`docs.ellipsis.dev` 301-redirects to `www.ellipsis.dev/docs`). Its trigger surface is the richest in
the tail: `pull_request` (`opened`, `pushed`, `merged`, `closed`, `review_submitted`, `commented`),
`push`, `issue`, `linear_issue`, `sentry` (`issue_alert`, `metric_alert`), `slack_channel`, cron,
`@ellipsis` mentions, API and CLI
([www.ellipsis.dev/docs/cloud-agents/triggers](https://www.ellipsis.dev/docs/cloud-agents/triggers)).
Sessions run in per-session sandboxes defined by a committed `environment.yaml`. **Can it merge? No —
and push is hard-gated at the credential**: the permissions page enumerates exact GitHub App scopes and
states, for read-only agents, "The agent can read anything in its repositories and write nothing: it
physically cannot push a commit, open a pull request, or edit an issue" and "if anything in that
sandbox attempts `git push`, GitHub refuses with a 403". Its "Gatekeeper" component sounds like a merge
gate and is not — "the last stage before anything reaches your pull request, and its job is
subtraction… It is not a second reviewer and goes looking for nothing of its own."

**Qodo / PR-Agent — the hosted product cannot approve; the open-source project can, in code, and
does not document it.** `qodo-merge-docs.qodo.ai` now 301-redirects to `docs.qodo.ai/code-review`,
which documents Code Review, Chat, Remediate Findings, committable suggestions, Rule Miner and Review
Standards — **no auto-approval, no merge, no `auto_approve` key anywhere.** The open-source repo is
live (`pushed_at: 2026-08-30`, 12,770 stars) and contains, in
[`pr_agent/git_providers/github_provider.py`](https://raw.githubusercontent.com/qodo-ai/pr-agent/main/pr_agent/git_providers/github_provider.py):

```python
def auto_approve(self) -> bool:
    res = self.pr.create_review(event="APPROVE")
```

gated in `pr_reviewer.py` by `if get_settings().config.enable_auto_approval:` — a key **not present in
the shipped `configuration.toml`**, so the operator must add it, which reads as deliberate opt-in-only
design. There is **no merge function**; the provider makes no call to the merge endpoint. ⚠️ **The
documentation gap is itself the finding:** `docs/docs/tools/review.md` and
`usage-guide/additional_configurations.md` contain **no auto-approval section at all**. A capability
that posts a binding GitHub approval exists in the code and the config surface and is absent from the
pages a user would read.

**CodeRabbit — the most explicit approve-and-block authority in the category, and still no merge.**
The setting, quoted identically from the docs and the machine-readable schema
(`request_changes_workflow`, boolean, **default `false`**):

> "Automatically approve when CodeRabbit's comments are resolved, the latest commit has been reviewed,
> and no pre-merge checks are failing. Note: In GitLab, all discussions must be resolved."
> — [docs.coderabbit.ai/reference/configuration](https://docs.coderabbit.ai/reference/configuration)
> and `schema.v2.json`, retrieved 2026-08-30

On-demand: "`@coderabbitai approve` only submits an approval when `reviews.request_changes_workflow` is
enabled. Without that setting, CodeRabbit resolves its review threads but reports that approval is
disabled" ([docs.coderabbit.ai/guides/commands.md](https://docs.coderabbit.ai/guides/commands.md)). The
blocking half, on pre-merge checks in `error` mode: "When paired with Request Changes Workflow, block
merges until resolved or manually overridden", with `override_requested_reviewers_only` restricting who
may override. **Post-Merge Actions do not merge** — they "run automated follow-up work after a pull
request is merged", only on the default branch, and can "open a follow-up pull request". A human
merges; CodeRabbit reacts.

**Gitlab Duo Agent Platform — creates merge requests, cannot merge them, and its identity model makes
approval structurally awkward.** Flows run under a **composite identity** — human user plus service
account — such that "any activities authored by the GitLab Duo Agent Platform are attributed to the
human user, while preventing privilege escalation by either the human user or the service account",
the more restrictive of the two roles applies, and "When a flow creates a merge request, the merge
request is attributed to the human user who triggered the flow instead of the service account"
([docs.gitlab.com/user/duo_agent_platform/security/](https://docs.gitlab.com/user/duo_agent_platform/security/),
retrieved 2026-08-30). It writes to the MR extensively — "Autonomously analyze merge conflicts, edit
conflicting files, and push a resolution commit"; "Autonomously analyze a review discussion, push the
requested changes, and resolve the thread" — and stops short of the merge button every time. On
GitLab.com "flows use hosted runners, which GitLab provides"; self-managed requires runners tagged
`gitlab--duo` with a `docker`, `docker-autoscaler`, or `kubernetes` executor. GitLab's approval-rules
docs say "Merge request authors do not count as eligible approvers on their own merge requests by
default" but **do not address bots or service accounts explicitly** — so whether attribution-to-the-
human would collide with the author rule is an **inference, not a documented statement**, and is
flagged as such.

**Sweep — dead as a GitHub PR bot, and GitHub does not say so.** `archived: false`, 7,706 stars, an
active-looking Marketplace listing — and `pushed_at: 2025-09-18T06:10:59Z`, **no code push in eleven
and a half months** as of 2026-08-30
([api.github.com/repos/sweepai/sweep](https://api.github.com/repos/sweepai/sweep)). The README's entire
content is a forwarding address: "Thank you for all of the support on Sweep. We're now building an AI
coding assistant for JetBrains." The Marketplace listing has been **repurposed** to advertise the
JetBrains plugin with no deprecation notice. The pivot date could not be established from primary
sources — `blog.sweep.dev` and `docs.sweep.dev` both return **HTTP 402**. Bounding evidence: the
notice was in place no later than **2025-09-18**.

---

### The one bot documented to merge its own pull request — and it is not an agent

**Renovate** ([docs.renovatebot.com/configuration-options/#automerge](https://docs.renovatebot.com/configuration-options/#automerge),
retrieved 2026-08-30):

> `automerge` — "Whether to automerge branches/PRs automatically, without human intervention." —
> default `false`
> `automergeType` — "How to automerge, if enabled." — default `"pr"`, allowed `"branch"`, `"pr"`,
> `"pr-comment"`
> `automergeStrategy` — "The merge strategy to use when automerging PRs."

That is the shape of documentation that authorises a bot to merge its own pull request, and it belongs
to a **deterministic dependency updater** whose diffs are machine-generated, narrow, and checkable by
CI alone. `automergeType: "branch"` even bypasses the pull request entirely, committing to the base
branch when checks pass.

**The contrast is the finding.** Merge authority in this ecosystem sits with the class of bot whose
output is verifiable without reading it. Every LLM agent surveyed stops at the review event. That is
not a coincidence of product maturity — it is the same line the project's verification work already
drew: the machinery that licenses removing the human reader is engineered checking, and a narrow
deterministic diff is the only case where the existing checking is sufficient.

---

## What this changes about a developer's process

The ticket asks what the human is left holding. Four things, and only the first is the one the
category advertises.

**1. Reviewing a finished pull request, in volume, without having watched it being made.** This is the
advertised change and it is real. But every primary source that measures it says the same thing: the
work does not disappear, it relocates and concentrates. Microsoft's `dotnet/runtime` account is the
only public dataset with both sides of the ledger — merged agent PRs need **16.5 review comments
against 12.4** for human PRs, the median agent PR needs **43% more** review comments, **24.5%** need
21 or more comments against 15.5% of human PRs, and **52.3%** need someone other than the author to
push commits against a 10.3% baseline (devblogs.microsoft.com, **2026-03-23**, vendor-reported on a
public repo). The team's response was explicitly not to lower the bar: *"we cannot compromise on review
quality… If PR generation outpaces review capacity, we either: 1. Slow down PR generation… 2. Speed up
review (somehow) 3. Reduce .NET runtime quality (unacceptable). Option 2 is the only sustainable path."*

**2. Deciding what to trigger, which is now a configuration file rather than a decision.** The
trigger surfaces documented above — cron, Sentry metric alerts, PagerDuty incidents, CI check-run
failures, issue creation, label changes — move the "should an agent work on this?" judgement from the
moment of work to the moment of configuration. GitHub's automations make this concrete and add a
wrinkle: *"Automations are stored separately from your repository's contents. They are not committed to
Git."* The rule that decides what an agent starts working on is not in the repository, not in code
review, and not in the history.

**3. Holding the credential.** Every product in this category resolves the merge question the same
way: the *agent* is not authorised, and a *human's* prior authorisation is. Devin's auto-merge toggle,
GitHub's "agent merge" in the desktop app, Cursor's optional approvals, and GitHub's native auto-merge
are all the same mechanism — a person deciding in advance that a merge may happen without them. That
decision is now the load-bearing one, and it is made once, in a settings page, rather than per change.

**4. Noticing when the gate has quietly stopped working.** The switches enumerated in headline finding
4 are all documented, all admin-controlled, and none of them is visible in a diff. A repository where
"Require approval for workflow runs" was turned off, or where Copilot was added as a ruleset bypass
actor, or where `request_changes_workflow` was enabled, looks identical in a pull request to one where
it was not.

**What it explicitly does not change: the verification layer.** Every vendor in this category
positions its own agent-side checking as advisory and names the engineered machinery as the thing that
enforces. OpenAI: *"Code review rules guide Codex; they don't replace tests, branch protections, or
required approvals."* GitHub: Copilot code review *"will not block merging changes."* Cursor: Bugbot
findings *"default to `neutral`"*, so requiring the check does not block. Anthropic: the Code Review
check run *"always completes with a neutral conclusion so it never blocks merging through branch
protection rules."* Read together, these are four vendors declining, in writing, to let their own
agent be the gate — which is a coherent position and worth reporting as such rather than as a defect.

---

## What these products cannot do — the structural limits, collected

| Limit | Products where it is documented |
|---|---|
| **Hard session cap** | Copilot cloud agent **59 minutes**, "a hard limit that cannot be extended or bypassed". Devin sessions "can't be continued after 30 days". **Codex documents no per-task cap at all** (the 12-hour figure is container cache lifetime). Cursor documents no session cap. |
| **Single repository** | Copilot: "can only make changes in the repository specified when you start a task"; GitHub automations "can only take action in the single repository it is scoped to". Copilot responsible-use: the agent "cannot access other repositories". |
| **Single branch, one PR** | Copilot: "can only work on one branch at a time and can open exactly one pull request to address each task it is assigned"; "can only perform simple push operations". |
| **Cannot reach the default branch** | Copilot: "Copilot cannot push directly to your default branch (for example, `main`)." |
| **No access to CI secrets** | Copilot: "The cloud agent does not have access to Actions organization or repository secrets." Codex: secrets "are only available to setup scripts… removed before the agent phase starts." |
| **Platform-bound** | Copilot cloud agent "only works with repositories hosted on GitHub"; Ubuntu x64 and Windows 64-bit runners only. In practice on `dotnet/runtime`: "CCA runs on Linux only… it can't compile or test" Windows targets. |
| **Concurrency and quota** | Jules: 15/100/300 tasks per rolling 24h by tier, 3/15/60 concurrent, "task limits are not shared or pooled". Codex: local and cloud share "a five-hour rolling window". Amazon Q: 30 CodeCatalyst invocations/month/user, 1,000 agentic requests/month Pro. Devin: "there are no concurrent session limits". |
| **No interactive debugging** | Universal. Every product surveyed hands back a diff or a PR; none documents a mechanism for a human to step into a running unattended session, except Cursor and Devin's "take over" surfaces which end the unattended mode. |
| **Ambiguity is not escalated, it is guessed** | Codex environment selection "falls back to the environment you used most recently" — a silent-wrong-repository hazard. Jules lists "prompts that are too vague or overly broad" as a documented failure mode, not an escalation path. **No product surveyed documents a mechanism by which an unattended agent halts and asks a human for clarification** — the closest is Jules' plan approval, and headline finding 4 shows that decays. |
| **Deployment is fenced off** | Devin, the most autonomy-marketed product, restricts deployment to "static frontends, served from `devinapps.com`" and "FastAPI backends, deployed to Fly.io", requires per-deploy approval, and disables deployment **entirely for enterprise organizations**. |

---

## Sources

All retrieved **2026-08-30** unless a publication date is given. Grouped by tier.

### Primary — platform and product documentation

**GitHub**
- [Risks and mitigations for GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations) — **the load-bearing document for this strand**
- [About GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent) — limitations, ruleset compatibility, 59-minute cap, cost model
- [Responsible use of Copilot agents](https://docs.github.com/en/copilot/responsible-use/agents) — default-branch and secrets constraints
- [About Copilot automations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automations) — trigger list, repository scoping, not-committed-to-Git
- [About rationale, confidence, and approvals for issues](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-automation-rationale-and-approvals) — confidence thresholds, "Cautious" / "Full automation"
- [Configuring settings for Copilot cloud agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/configuring-agent-settings) — "Require approval for workflow runs" and its warning
- [Customize the agent firewall](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall)
- [Customize the agent environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment) — `copilot-setup-steps.yml`, runner constraints
- [Starting Copilot sessions](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions) — full entry-point list
- [Managing issues and pull requests with the GitHub Copilot app](https://docs.github.com/en/copilot/how-tos/github-copilot-app/managing-issues-and-pull-requests) — **agent merge**
- [Using Copilot code review](https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review) — "always leaves a 'Comment' review"
- [Approving a pull request with required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews) — "Pull request authors cannot approve their own pull requests"
- [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) — "approved by someone other than the person who pushed it"; the admin-bypass default
- [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization) — "Allow GitHub Actions to create and approve pull requests"
- [GITHUB_TOKEN concepts](https://docs.github.com/en/actions/concepts/security/github_token) — approval-required workflow runs; recursive-run prevention

**GitHub changelog** (dated posts) — [coding agent GA 2025-09-25](https://github.blog/changelog/2025-09-25-copilot-coding-agent-is-now-generally-available/) · [PR throughput & time-to-merge metrics 2026-02-19](https://github.blog/changelog/2026-02-19-pull-request-throughput-and-time-to-merge-available-in-copilot-usage-metrics-api/) · [agent tasks REST API 2026-05-13](https://github.blog/changelog/2026-05-13-start-copilot-cloud-agent-tasks-via-the-rest-api/) · [automations 2026-06-02](https://github.blog/changelog/2026-06-02-schedule-and-automate-tasks-with-copilot-cloud-agent/) · [Copilot app GA 2026-06-17](https://github.blog/changelog/2026-06-17-github-copilot-app-generally-available/) · [comment-triggered automations 2026-08-03](https://github.blog/changelog/2026-08-03-trigger-copilot-automations-with-comments/)

**OpenAI** — [Codex cloud](https://learn.chatgpt.com/docs/cloud) · [cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environment) · [internet access](https://learn.chatgpt.com/docs/cloud/internet-access) · [GitHub integration](https://learn.chatgpt.com/docs/third-party/github) · [GitLab integration](https://learn.chatgpt.com/docs/third-party/gitlab) · [Linear integration](https://learn.chatgpt.com/docs/third-party/linear) · [Codex Security GitLab CI](https://learn.chatgpt.com/docs/security/cli/ci/gitlab) · [pricing](https://learn.chatgpt.com/docs/pricing) · [`openai/codex-universal`](https://github.com/openai/codex-universal)

**Cognition / Devin** — [SDLC integration](https://docs.devin.ai/essential-guidelines/sdlc-integration.md) · [Devin Review](https://docs.devin.ai/work-with-devin/devin-review.md) · [GitHub integration](https://docs.devin.ai/integrations/gh.md) · [automations](https://docs.devin.ai/product-guides/automations.md) · [auto-triage](https://docs.devin.ai/product-guides/auto-triage.md) · [environment](https://docs.devin.ai/onboard-devin/environment.md) · [Outposts](https://docs.devin.ai/cloud/outposts/overview.md) · [security profiles](https://docs.devin.ai/product-guides/security-profiles.md) · [stacked PRs](https://docs.devin.ai/work-with-devin/stacked-prs.md) · [deployment capabilities](https://docs.devin.ai/product-guides/deployment-capabilities.md) · [billing/usage](https://docs.devin.ai/admin/billing/usage.md)

**Google Jules** — [running tasks](https://jules.google/docs/running-tasks/) · [environment](https://jules.google/docs/environment/) · [code / publishing](https://jules.google/docs/code/) · [review plan](https://jules.google/docs/review-plan/) · [API reference](https://jules.google/docs/api/reference/) · [usage limits](https://jules.google/docs/usage-limits/) · [changelog](https://jules.google/docs/changelog/) · [FAQ](https://jules.google/docs/faq/)

**Cursor** — [cloud agent](https://cursor.com/docs/cloud-agent) · [automations](https://cursor.com/docs/cloud-agent/automations) · [setup](https://cursor.com/docs/cloud-agent/setup) · [security](https://cursor.com/docs/cloud-agent/security) · [API endpoints](https://cursor.com/docs/cloud-agent/api/endpoints) · [GitHub integration](https://cursor.com/docs/integrations/github) · [Bugbot](https://cursor.com/docs/bugbot) · changelog entries [0-50](https://cursor.com/changelog/0-50), [1-0](https://cursor.com/changelog/1-0)

**Anthropic** — [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web) · [routines](https://code.claude.com/docs/en/routines) · [cloud environments](https://code.claude.com/docs/en/cloud-environments) · [code review](https://code.claude.com/docs/en/code-review) · [`claude-code-action` capabilities and limitations](https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/capabilities-and-limitations.md) · [`claude-code-action` security](https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/security.md) · [`claude-code-action` usage](https://raw.githubusercontent.com/anthropics/claude-code-action/main/docs/usage.md)

**Long tail** — [Factory code review CI](https://docs.factory.ai/software-factory/code-review-ci.md) · [Factory automations](https://docs.factory.ai/software-factory/automations.md) · [`Factory-AI/droid-action` action.yml](https://raw.githubusercontent.com/Factory-AI/droid-action/main/action.yml) · [Codegen agent permissions](https://docs.codegen.com/settings/agent-permissions.md) · [Ellipsis permissions](https://www.ellipsis.dev/docs/cloud-agents/permissions) · [Ellipsis triggers](https://www.ellipsis.dev/docs/cloud-agents/triggers) · [PR-Agent `github_provider.py`](https://raw.githubusercontent.com/qodo-ai/pr-agent/main/pr_agent/git_providers/github_provider.py) · [CodeRabbit configuration reference](https://docs.coderabbit.ai/reference/configuration) · [CodeRabbit commands](https://docs.coderabbit.ai/guides/commands.md) · [CodeRabbit pre-merge checks](https://docs.coderabbit.ai/pr-reviews/pre-merge-checks.md) · [GitLab Duo security](https://docs.gitlab.com/user/duo_agent_platform/security/) · [`sweepai/sweep` repo API](https://api.github.com/repos/sweepai/sweep) · [Renovate automerge options](https://docs.renovatebot.com/configuration-options/#automerge)

### Vendor-reported outcome data (interested parties)

- Microsoft / Stephen Toub, "Ten months with Copilot coding agent in dotnet/runtime", devblogs.microsoft.com, **2026-03-23** — 67.9% merge rate, 0.6% revert rate, review-load figures, and the author's own sampling caveat
- Cognition, "Devin annual performance review 2025", [cognition.com](https://cognition.com/blog/devin-annual-performance-review-2025), **2025-11-14** — 67% merge rate, no methodology
- Cognition, "Introducing Devin 2.2", [cognition.com](https://cognition.com/blog/introducing-devin-2-2), **2026-02-24** — the "full loop, handled for you" claim
- Google, "Jules now available", [blog.google](https://blog.google/technology/google-labs/jules-now-available/), **2025-08-06** — 140,000 code improvements (activity count)
- AWS DevOps blog, **2026-04-30** — Amazon Q Developer end-of-support timeline

### Independent measurement

- Li, Zhang & Hassan et al., "The Rise of AI Teammates in SE 3.0", **arXiv:2507.15003** — the open AIDev dataset; Codex 64% / Devin 49% / Copilot 35% acceptance. **Observational**, public repos ≥100 stars
- "Habituation at the Gate", **arXiv:2606.22721** — **controlled study**, 400 repeat reviewers, 11,429 reviews; approval 30.1% → 36.8%, inline comments −22%, latency +3.5×
- Duma et al., **arXiv:2605.02273** (EASE 2026) — 33,596 agent PRs; 61.38% with no *recorded* review, with the authors' own caveat that a silent approval is invisible to the instrument
- Xia & Miller, **arXiv:2607.09902** — post-merge fate of agentic code; higher corrective-maintenance rates
- Husain, Flath & Whitaker (Answer.AI), **2025-01-08**, [answer.ai](https://www.answer.ai/posts/2025-01-08-devin.html) — **practitioner evaluation, n=20**, 3 successes

---

## Confidence and gaps

**High confidence.**
- The merge answer for GitHub Copilot cloud agent. Four verbatim sentences on a page whose entire
  purpose is enumerating what the agent cannot do. This is as strong as documentary evidence gets.
- The merge answer for Codex, Jules, Amazon Q, Codegen and Ellipsis — each supported by an exhaustive
  enumeration (a full-manual grep, a complete API surface, a complete permissions page) rather than by
  the absence of a search hit.
- Cursor's approve capability, Factory's approve-and-block behaviour, CodeRabbit's
  `request_changes_workflow`, and PR-Agent's `auto_approve()` — all quoted from docs or read from
  source.
- The trigger surfaces and their dates, which come from dated changelog posts.

**Medium confidence.**
- **The GitHub "agent merge" identity model.** The docs do not state which identity performs the merge
  call. The reading offered — a local desktop session using the signed-in user's authority — rests on
  the desktop context and the phrase "as soon as GitHub allows". Marked as inference in the text and
  should be re-verified.
- **Devin's merge posture.** Two documentation pages pull in opposite directions: one presupposes
  "before Devin can merge changes", the other says humans choose whether to merge. The resolution
  offered — the merge button is a human UI action executed under Devin's GitHub App credential — is
  consistent with every page read, but Cognition has not stated it in one place.
- **Whether a GitHub App's `APPROVE` review satisfies a required-reviewers rule.** This is the hinge
  under Cursor's, Factory's, CodeRabbit's and PR-Agent's approve capabilities, and **GitHub's own
  protected-branches documentation does not address GitHub Apps, bots, or machine accounts at all.**
  That is a real documentation void at exactly the point where it matters. Reported as a void rather
  than resolved by inference.

**Known gaps, stated plainly.**
- **Identity and scopes are under-documented across the board.** Codex's GitHub App permission set is
  not published; Jules never documents its GitHub App scopes; Amazon Q's app permissions were not
  retrievable anonymously. In each case the write *ceiling* cannot be established from primary
  sources — only what the product docs claim it does.
- **Copilot Workspace's sunset date is unresolved.** The docs URL 404s, which evidences removal, but no
  GitHub changelog post confirming a date was found.
- **The Copilot "cloud agent" rename is undated.** No changelog post announcing it was located.
- **Devin's ACU is no longer publicly defined** — the definition page 404s, so the unit Cognition bills
  on cannot be quantified from current primary sources.
- **Sweep's pivot date could not be established** — both `blog.sweep.dev` and `docs.sweep.dev` return
  HTTP 402.
- **Nothing here establishes what teams actually *do* with these switches.** Every relaxation
  documented in headline finding 4 is a capability, not a measured practice. Whether organisations
  disable the workflow-approval gate, add Copilot as a ruleset bypass actor, or enable Cursor's
  approvals is unmeasured — by the vendors and by anyone else. The project's prior far-end census found
  three cases and none was what the phrase implies; nothing found in this strand changes that count.
- **This strand covers documented capability, not deployed behaviour.** Private repositories are
  invisible to every method used. Absence of published evidence is not evidence of absence and is not
  written as such anywhere above.

**Ageing risk — high, and higher than any other strand in this ticket.** In the fifteen months before
this research: Copilot "coding agent" became "cloud agent"; Cursor "Background Agents" became "Cloud
Agents"; the entire Codex documentation site moved hosts; Windsurf's docs were absorbed into Devin's;
Amazon Q Developer entered a two-year sunset; and Copilot Workspace was removed from the docs
entirely. **Every URL supplied in the original research brief for Codex, Cursor and Windsurf was
stale.** Anything built on this document should carry the 2026-08-30 date visibly and be re-verified
before reuse.

---

## Blocked or unavailable sources

Logged, never circumvented. No security control was worked around; no paywall, login wall or bot
challenge was bypassed.

| URL | Block type | Consequence |
|---|---|---|
| `help.openai.com/en/articles/11096431-openai-codex` | **HTTP 403** (bot challenge) | Not retrieved |
| `openai.com/index/introducing-codex/` | **HTTP 403** | Codex launch-date history below 2026-08 unestablished |
| `learn.chatgpt.com/docs/changelog` | Renderer truncates at ~2026-08-10; `.md` variant 404s | Ship dates for Codex cloud, GitHub code review, and the internet-access default could not be pinned |
| `blog.sweep.dev` / `docs.sweep.dev` | **HTTP 402 Payment Required** | Sweep pivot date unestablished |
| `docs.greptile.com` | **ECONNREFUSED** | Greptile not covered |
| `github.com/apps/chatgpt-codex-connector` | Fetched; GitHub publishes no permission set on public App listings | Codex's GitHub scopes unestablished |
| `github.com/marketplace/amazon-q-developer` | Same — no permissions grid exposed anonymously | Amazon Q's contents/PR write scopes unconfirmed |
| `docs.github.com/en/copilot/using-github-copilot/using-copilot-workspace` | **HTTP 404** | Evidentiary — removal, not redirect |
| `docs.devin.ai/product-guides/acu-usage` | **HTTP 404** | ACU definition unestablished |
| `githubnext.com/projects/copilot-workspace/` | HTTP 200 but JS-shell thin | Status label unconfirmable |
| `docs.aws.amazon.com/.../software-dev.html` and `.../security_iam_service-with-iam.html` | Fetched twice; returned title only | Amazon Q `/dev` and IAM specifics unconfirmed |
| `raw.githubusercontent.com/qodo-ai/pr-agent/main/mkdocs.yml` | **HTTP 404** | Could not fully enumerate PR-Agent doc nav to confirm auto-approval is undocumented everywhere |
| `raw.githubusercontent.com/anthropics/claude-code-action/main/README.md` | Fetched; content is a nav stub | Limitations and permissions read from `docs/` files instead |
| `docs.claude.com/en/api/agent-sdk/*.md` | HTTP 200 serving the SPA shell | Worked around by using `code.claude.com/docs/en/agent-sdk/*.md` — a different published host for the same docs, not a circumvention |
| PR-Agent `configuration.toml` full-file dump | Fetch summariser declined a verbatim full-file reproduction on fair-use grounds | Narrow key-by-key queries used instead |

**Redirects recorded as findings rather than blocks:** `developers.openai.com/codex/*` → 308 →
`learn.chatgpt.com/docs/*`; `docs.cursor.com/*` → 308 → `cursor.com/docs/*`; `docs.windsurf.com/*` →
307 → `docs.devin.ai/*`; `windsurf.com/changelog` → 308 → `docs.devin.ai/desktop/changelog`;
`cognition.ai` → 301 → `cognition.com`; `qodo-merge-docs.qodo.ai` → 301 →
`docs.qodo.ai/code-review`; `docs.ellipsis.dev` → 301 → `www.ellipsis.dev/docs`.

⚠️ **One anomaly recorded rather than acted on.** Four unrelated AWS documentation pages each returned
an identical trailing block instructing the reader to run an `aws agent-toolkit search-skills` command,
styled as documentation content. Verbatim repetition of a command-promotion snippet across unrelated
pages is inconsistent with AWS documentation authoring and resembles content injected somewhere in the
fetch pipeline. **The command was not run and the text was treated as untrusted data.**
