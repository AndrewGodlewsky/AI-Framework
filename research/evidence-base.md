# Evidence Base: Adoption and Efficacy of AI in Professional Software Development

**Research date:** 2026-08-27
**Purpose:** Establish a primary-sourced, tier-classified evidence base for (a) how many developers and teams use AI and at what *depth*, and (b) whether it works — for a set of documents describing the spectrum from minimal inline assistance to unsupervised autonomous delivery.
**Method:** Live web research against published survey reports, peer-reviewable papers, and vendor telemetry disclosures. Journalism and secondary summaries are labelled `[SECONDARY]` inline and were used only where a primary artifact could not be reached.
**Scope note:** Per the constraints inherited from the vocabulary ticket, **no SWE-bench Verified scores appear in this document** (deprecated by OpenAI 23 Feb 2026 for contamination; UTBoost/ACL 2025 found 24.4% of leaderboard entries affected by mislabelled patches). No bare agent-benchmark scores appear at all, because any such score is a joint model+harness measurement.

---

## Headline findings

Every row carries its evidence tier, sample size, and date. **Read the conflicts column** — several of these numbers contradict each other, and that is the point.

| # | Finding | Figure | Tier | N | Source & date | Conflicts with |
|---|---|---|---|---|---|---|
| 1 | Professional developers using AI tools at all | **75% – 90%** depending on survey | Hard survey | 4,867 – 49,000 | Four surveys, Q1 2025 – Jul 2026 | Itself — see §1.1. A 15-point spread on the single most-quoted number in the field |
| 2 | Professional developers using AI **daily** | **51%** | Hard survey | ~26.5k–33.7k per question | Stack Overflow Dev Survey 2025 (fielded May–Aug 2025) | JetBrains May–Jul 2026: 68% use *agents* daily |
| 3 | Median time per day spent working with AI | **2 hours** | Hard survey | ~5,000 | DORA, *State of AI-assisted Software Development 2025* | — |
| 4 | Developers using AI **agents** (agent edits files / runs commands) | **~31% any use; 14.1% daily; 37.9% no plans** | Hard survey | ~26.5k–33.7k | Stack Overflow 2025 | JetBrains 2026: **90% weekly, 68% daily**. Repository traces: **22–29% of projects**. See §1.2 — the largest conflict in this document |
| 5 | Share of developers who are heavy agent users | **~31% "Agentic Coders"** (avg. 84% of their code agent-generated); ~47% AI-assisted; ~23% manual | Hard survey | >15,000 | JetBrains *Developer Ecosystem Survey 2026*, fielded May–Jul 2026 | Self-report only; no telemetry corroboration at this granularity |
| 6 | Coding-agent adoption measured from **repository traces** rather than self-report | **22.20% – 28.66% of projects** | Semi-controlled study (observational mining) | 128,018 projects | Robbes et al., arXiv:2601.18341, as of 21 Feb 2026 | Rows 4 and 5 |
| 7 | Developers who **highly trust** AI output accuracy | **3.1%** (2.7% among professionals) | Hard survey | ~26.5k–33.7k | Stack Overflow 2025 | Sonar Jan 2026: 96% "don't fully trust" — different question, same direction |
| 8 | **The perceived-vs-actual gap.** Experienced devs on their own mature repos | **+19% completion time** (i.e. slower) while self-estimating **−20%** | Controlled study (RCT) | 16 devs / 246 tasks | METR, arXiv:2507.09089, tools of Feb–Jun 2025 | Rows 9–12, and METR's own Feb 2026 walk-back (row 13) |
| 9 | Field RCTs, GitHub Copilot inline completion | **+26.08% tasks completed** (SE 10.3%) | Controlled study (3 field RCTs) | 4,867 devs | Cui, Demirer, Jaffe, Musolff, Peng & Salz, *Management Science*, pub. 27 Feb 2026 | Row 8 |
| 10 | Lab RCT inside Google, enterprise-grade task | **~21% faster**; authors state "our confidence interval is large" | Controlled study (RCT) | 96 Google engineers | Paradis et al., arXiv:2410.12944, Oct 2024 | Row 8 |
| 11 | CLI coding agents (Claude Code, Copilot CLI) rolled out at Microsoft | **+24% merged PRs** vs counterfactual | Semi-controlled study (observational, self-selected adopters) | tens of thousands of engineers, 4 months, early 2026 | Murphy-Hill, Butler & Savelieva, arXiv:2607.01418 | Row 8 (different era, different tools) |
| 12 | Enterprise "2× productivity" mandate, longitudinal | **2.09× per-capita throughput** by Apr 2026; reviewer workload **~doubled**; automated review **exceeded human review by volume**; merge and revert rates **stable** | Semi-controlled study (staggered difference-in-differences) | 802 devs / 196,212 PRs, Jan 2024 – Apr 2026 | He, Agarwal, Denisov-Blanch, Azaletskiy, Koyejo & Vasilescu, arXiv:2607.01904 | Rows 15–17 on quality |
| 13 | **METR's own follow-up walked the headline back** | Late-2025 rerun: **−18%** (CI −38% to +9%) for 10 returning devs; **−4%** (CI −15% to +9%) for 47 new devs. METR: "our data is only very weak evidence" | Controlled study (RCT, design abandoned) | 57 devs | METR, 24 Feb 2026 | Row 8 — same team, same instrument |
| 14 | Delivery stability under AI adoption | AI's association with **throughput turned positive** in 2025 (was negative in 2024) but its association with **instability remained negative** | Hard survey | ~5,000 | DORA 2025 | Faros telemetry (row 15) explicitly contradicts DORA's protective-foundations claim |
| 15 | Production incidents and rework at high AI adoption | **Incidents-per-PR +242.7%**, bugs/dev **+54%**, code churn **+861%**, time in review **+199.6%**, PRs merged **without any review +31.3%**, throughput **+33.7%** | Vendor-reported metric | 22,000 devs / 4,000 teams, 2 yrs telemetry | Faros AI, *The Acceleration Whiplash*, Mar 2026 | Rows 12, 16 |
| 16 | Downstream **maintainability** of AI-assisted code, measured by a second cohort maintaining it | **No significant difference** in completion time or code quality; "no consistent warning signs of degraded code-level maintainability" | Controlled study (two-phase RCT) | 151 participants, 95% professional | Borg et al., arXiv:2507.00788 (v3 Feb 2026) | Rows 15, 17 — the sharpest quality conflict in this document |
| 17 | Longitudinal code-structure signals across the industry | Block duplication **+81%** since 2023 (40.3 → 73.0 per M changed lines); moved/refactored code **21% (2022) → 3.8% (2026)**; copy/paste **15.7%** of changed lines | Vendor-reported metric | 623M analysed code changes, 2023–2026 | GitClear, *The Maintainability Gap*, 2026 | Row 16 |
| 18 | Security of model-generated code | **~55% security pass rate**, flat for two years, while syntax pass rate rose ~50% → 95%+ | Vendor-reported metric | 80 tasks × 4 languages × 4 CWEs, 150+ models | Veracode, Spring 2026 GenAI Code Security update | — (tests unprompted generation only) |
| 19 | Skill formation under AI assistance | AI group scored **50%** vs **67%** hand-coding on a comprehension quiz (Cohen's d = 0.738, p = 0.01); time gains not significant | Controlled study (RCT) | 52 mostly-junior engineers | Shen & Tamkin (Anthropic), arXiv:2601.20245, 3 Feb 2026 | — |
| 20 | Human review of agent-authored PRs | **Most AI-generated PRs receive no reviews at all**; where review occurs it is "automation-mediated" | Semi-controlled study (mining AIDev) | AIDev corpus (932,791 agentic PRs / 116,211 repos) | Duma et al., EASE 2026, arXiv:2605.02273 | GitLab survey: 85% say the bottleneck moved *to* review |
| 21 | Agent PR acceptance and review latency | AI-assisted PRs accepted **32.7%** vs **84.5%** unassisted; agentic PRs wait **5.3×** longer for reviewer pickup (1,055 vs 201 min); AI PRs ~**154%** larger | Vendor-reported metric | 8.1M PRs / 4,800 teams / 42 countries | LinearB, *2026 Software Engineering Benchmarks*, May 2026 | Mazloomzadeh et al. (arXiv:2607.21832) measure agent merge rates of **43.0%–84.3%** on open source |
| 22 | Share of an AI lab's own merged code authored by its agent | **>80%** as of May 2026 (from "low single digits" pre-Feb 2025) | Vendor-reported metric | Anthropic's own codebase | Anthropic Institute, *When AI builds itself*, 4 Jun 2026 | Self-caveated: LOC-based, "imperfect measure," attribution pipeline has "gaps" |
| 23 | Merging without a human in the loop, at one company | **>1/3 of PRs merged with no human in the loop** | Practitioner anecdote (single-company engineering blog) | one company | Razorpay engineering, Jun 2026 | Nothing to compare it against — see §2.5 |

---

## Part A — Adoption

### 1.1 The headline number is not one number

Four credible instruments, four different answers, all published within 14 months of each other. **This is the single most important thing a reader should take from the adoption section: "developers use AI" has no agreed value.**

| Source | Figure | Question actually asked | Tier | N | Fielded | Population & selection |
|---|---|---|---|---|---|---|
| **Stack Overflow Developer Survey 2025** | **84%** use or plan to use AI tools in development (up from 76%); **51%** of professional developers use daily | Use *or plan to use* — a deliberately broad frame that inflates relative to "currently use" | Hard survey | 49,000+ respondents, 177 countries; per-question N 26,564–33,662 | May–Aug 2025 | Opt-in, recruited through Stack Overflow's own channels. Self-selects toward people who still visit Stack Overflow — a population under active disruption from the thing being measured |
| **DORA, State of AI-assisted Software Development 2025** | **90%** use AI at work (+14 points YoY); median **2 h/day**; **>80%** perceive a productivity increase; **30%** report little or no trust | "Using AI within your job function" — broader than coding | Hard survey | ~5,000 technology professionals + 100+ hours qualitative | 2025 | Opt-in, Google-affiliated recruitment. Includes non-developer technology roles |
| **JetBrains, AI Pulse Jan 2026** | **90%** regularly used ≥1 AI tool at work for coding; **74%** used specialised AI tools (assistants/editors/agents) rather than only chatbots | Explicitly framed as "tools you use for work," AI not mentioned in the framing — a genuine methodological improvement | Hard survey | 10,000+ professional developers | Jan 2026 | Recruited partly via Instagram/Zhihu ads, ~16% from JetBrains' own research panel; raked on region, experience, JetBrains familiarity. **The weighting variable "JetBrains familiarity" is itself an AI-tooling proxy** |
| **SlashData, Developer Nation Q1 2026** | **75%** of professional developers use AI-assisted tools (up from 61% in Q1 2024); **12%** report no AI usage (down from 28%) | Splits "using AI tools" from "building AI features" — the cleanest construct of the four | Hard survey | 12,400+ valid responses, 95 countries | Q1 2026 | Opt-in global omnibus; the most demographically balanced of the four but the least developer-community-specific |

**What would resolve it:** the four instruments ask four different questions of four different populations. SlashData's 75% is the most conservative *and* the most recent, and it decomposes cleanly (53% use external chatbots, 42% use IDE-integrated tools, 25% use AI for assets). Stack Overflow's 84% includes "plan to use." DORA's 90% includes non-developer roles. JetBrains' 90% is weighted on a variable correlated with the outcome. **A reader should quote the range 75–90% and name the instrument, never a single figure.**

⚠️ **Self-selection warning that applies to all four.** Every one of these is opt-in. Developers who have rejected AI have less reason to complete an AI-heavy survey; developers whose employer bans AI tools may not be reached at all. All four numbers are plausibly biased upward, and **none of the four publishes a non-response analysis.**

### 1.2 Depth of usage — the axis this project is built on

This is where the evidence gets genuinely interesting and genuinely contradictory.

#### The four-level ladder, as the sources actually measure it

Almost no instrument measures the full ladder. Here is what each level has, and what it lacks.

**Level 1 — inline completion.** Best-measured level, and the only one with clean RCT evidence (Peng et al. 2023; Cui et al. 2026). Stack Overflow 2025 finds **13.8% of respondents prefer copilot/autocomplete mode exclusively** — the only direct measurement of "inline only" I could locate anywhere.

**Level 2 — chat.** Poorly separated from Level 1 in most instruments. SlashData is the exception: **53% use external AI chatbots/agents outside the coding environment** vs **42% using IDE-integrated tools**, i.e. chat is still the more common surface. Stack Overflow 2025 has ChatGPT at **81.7%** and GitHub Copilot at **67.9%** among AI users, consistent with chat-first.

**Level 3 — agentic (the agent edits files and runs commands).** Three instruments, wildly different answers:

| Source | Agent adoption | Instrument | N | Date |
|---|---|---|---|---|
| Stack Overflow 2025 | **14.1% daily, 9% weekly, 7.8% monthly (~31% any); 37.9% no plans** | Self-report survey | ~26.5k–33.7k | May–Aug 2025 |
| Sonar, *State of Code* | **64% use autonomous AI agents** | Self-report survey | 1,149 | pub. Jan 2026 |
| JetBrains, Dev Ecosystem 2026 | **90% weekly, 68% daily** | Self-report survey | 15,000+ | May–Jul 2026 |
| Robbes et al., arXiv:2601.18341 | **22.20% – 28.66% of projects** | Repository-trace mining (co-authoring markers on commits/PRs) | 128,018 projects | to 21 Feb 2026 |

**This is the sharpest and most consequential conflict in the document.** In roughly twelve months, self-reported weekly agent use goes from ~31% to 90% — while independent trace mining of 128,018 GitHub projects finds agent traces in only 22–29% of them.

*What would resolve it, honestly stated:*

- The two are not measuring the same unit. JetBrains measures **developers**; Robbes et al. measure **projects**. A developer can use an agent daily on one repo and leave no trace on twenty others.
- Trace mining under-counts by construction: it detects only agents that leave explicit co-authoring markers. Locally-run agents whose output the developer commits under their own name are invisible. The authors flag this.
- Self-report over-counts by construction: "using an agent" is now socially and professionally desirable (JetBrains 2025: **68% expect employers to require AI proficiency**), and "agent" has no shared definition — a chat sidebar that can edit a file qualifies for some respondents.
- **The measurement that does not exist:** nobody has published a study that instruments a fixed developer cohort and compares what they say they do against what their tooling logs show. Until someone does, the 31%-vs-90%-vs-25% spread is unresolved.

**Level 4 — autonomous (the agent works unsupervised).** Essentially unmeasured as a population statistic. See §2.5.

#### The best available depth breakdown

**JetBrains, *How Much Code Do Developers Really Let Agents Write?* (Aug 2026; N>15,000 professional developers; fielded May–Jul 2026; 8 languages; raked on region, employment status, language, JetBrains familiarity).** Tier: hard survey. This is the most granular published depth measurement in existence and the closest thing the field has to a map of the spectrum:

- **~31% "Agentic Coders"** — ~84% of their code fully agent-generated, 15% AI-assisted, 6% manual
- **~47% "AI-Assisted Coders"** — ~40% agent-generated, 60% AI-assisted, 20% manual
- **~23% "Manual Coders"** — ~10% agent-generated, 25% AI-assisted, 75% manual
- **Over half of all developers now write less than 20% of their code manually**
- **One in five writes literally zero code without AI help**

⚠️ **Three caveats that matter.** (i) These are self-reported percentage estimates, and JetBrains had to discard responses whose buckets summed outside 80–150% — an explicit admission that respondents cannot estimate this reliably. (ii) Segment averages sum above 100% because they are bucketed midpoints. (iii) The weighting variable includes JetBrains product familiarity.

**Breakdowns available from the same instrument:**

- **By seniority:** senior developers lead heavy agent use — roughly a quarter generate >80% of code via agents, more than juniors, who skew toward AI-assisted rather than agentic workflows. **This inverts the pattern in the efficacy literature**, where Cui et al. (2026) and Sonar both find *less* experienced developers gain more. Seniors adopt the deeper mode; juniors get the bigger measured lift.
- **By geography:** East Asia (China, Japan, South Korea) **32–35%** generate >80% of code via agents, vs **~16%** in Europe/UK — roughly twice the rate.
- **By language:** Go/JavaScript/TypeScript **54–55%** agent-generated; Java/Python 48–51%; C/C++ lowest (38% of code still written manually).
- **By company size** (JetBrains Jan 2026): GitHub Copilot reaches **40% adoption at companies with 5,000+ employees** vs 29% overall — the only *primary-sourced* company-size datum found. Everything else on enterprise-vs-startup depth traces to content-farm aggregation and is **not** cited here.

#### Agentic autonomy measured from the product side

**Anthropic Economic Index, June 2026 report ("Cadences").** Tier: vendor-reported metric. Methodology: privacy-preserving classifiers (transcripts read only by another instance of Claude), hourly sampling across Claude.ai, Desktop, Claude Code and the first-party API, 10 Apr – 10 Jun 2026; ~9,700 survey respondents linked to usage; users with <5 sessions excluded.

- Autonomy measured on a **1–5 scale** (how far Claude must make independent judgments vs execute a specified task).
- **Claude Code sessions score higher on autonomy for 26 of 31 output types**, averaging **+0.37** points; the gap persists at constant model (Sonnet-to-Sonnet: +0.26), so **the product surface, not the model, drives the autonomy difference**.
- **~2/3 of the autonomy difference comes from users delegating the same task more fully** on Claude Code — median blog post: 13 chat turns vs 1 Claude Code prompt.
- "Directive" conversations (complete task delegation, minimal interaction) rose from **27% to 39%**.

⚠️ **Survivorship, stated plainly.** This is telemetry from people who chose Claude Code and kept using it. It cannot tell you what share of developers delegate; it tells you that among those who adopted an agentic surface, delegation deepened. Anthropic itself notes the respondent base skews heavily to computer/mathematical occupations (30% vs 4% of employment) and that selection bias cannot be ruled out.

**Scale corroboration.** Liu et al., arXiv:2608.00101 (30 Jul 2026) characterise sampled GitHub Copilot traces from June 2026: **3.2M users, 13M sessions, 761M LLM calls, 95T tokens**, and describe the modal shape as "sparse user-initiated turns, each unfolding into an autonomous agent loop of LLM calls almost always coupled with tool execution." The paper is a systems paper, not an adoption paper, but the session structure is direct evidence that agentic (not completion) is now the dominant interaction shape on that platform.

### 1.3 Where teams sit versus where the discourse claims they sit

Five independent pieces of evidence that the gap is real:

1. **Vibe coding is a minority practice among professionals.** Stack Overflow 2025: **72.2% do not engage in vibe coding**; 14.7% do; 5.3% emphatically reject it. Consistent across all age groups. Tier: hard survey, N ~26.5k–33.7k.

2. **Observed behaviour contradicts the delegation narrative.** Huang, Reyna, Lerner, Xia & Hempel, arXiv:2512.14012 (v2 18 Aug 2026), *"Professional Software Developers Don't Vibe, They Control."* Field observations N=13 plus qualitative survey N=99. Finding: experienced developers "retain their agency in software design and implementation out of insistence on fundamental software quality attributes" and deploy explicit "strategies for controlling agent behavior." Tier: controlled study (observational, small-N qualitative).

3. **Trace mining finds a quarter of projects, not nine-tenths.** §1.2 above.

4. **Adoption is broad but shallow by the tools' own users' account.** JetBrains 2025: **85% use AI regularly but only 44% report AI is fully or partially integrated into their workflows** — a 41-point gap between "I use it" and "it is part of how we work." Tier: hard survey, N=24,534, fielded Apr–Jun 2025.

5. **Where AI is *not* used is as informative as where it is.** Stack Overflow 2025 asked which tasks developers **"Don't Plan to Use AI for This Task"** — forward-looking, task-level intent, *not* current abstention.

   > ⚠️ **CORRECTED 2026-08-27** by the practitioner-exemplars strand. The raw figures first recorded here (deployment/monitoring 75.8%, project planning 69.2%, committing and reviewing code 58.7%, predictive analytics 65.6%) are **within-series percentages of a 25,349-person subset, not percentages of all developers** — the "Don't Plan" column sums to 371%. Reconstructing per-task denominators (~29,700) gives **≈65%** for deployment/monitoring and **≈50%** for committing and reviewing code. Note also that "committing *and* reviewing code" is a compound category, not code review alone. The monotonic workflow gradient survives intact and is cleaner once properly denominated; the magnitudes do not. Full arithmetic in `practitioner-exemplars.md`, *Where refusal concentrates, and who is doing it*. **Use the corrected figures.**

   Refusal concentrates at the operations end of the lifecycle — the part of the spectrum that unsupervised autonomy would have to cross. A second, independent correction from the same strand: **Stack Overflow's results blog contradicts its own microsite** (trust reported at 29% where the microsite totals give 32.7%, and two frustration figures transposed). The erroneous 29% has propagated downstream — cite the microsite.

⚠️ **A live example of narrative contamination, found during this research.** Multiple 2026 blogs (byteiota, 11 Jun 2026; cadence.withremote.ai; several aggregators) publish articles headlined *"Stack Overflow Dev Survey **2026**"* reporting 84% adoption, 3% trust, 49,000 respondents, 177 countries. **These are the 2025 figures.** The 2026 Stack Overflow Developer Survey opened on **23 June 2026** and, as of this research date (27 Aug 2026), **has published no results**. byteiota's own body text links to `survey.stackoverflow.co/2025`. Any document in this project citing a "2026 Stack Overflow survey" is citing a mislabelled 2025 survey. This is a concrete instance of the discourse running ahead of the data.

---

## Part B — Efficacy

### 2.1 What the controlled evidence actually says

Ordered by date, because the era of the tools is the dominant moderator.

| Study | Design | N | Tools / era | Effect | Tier |
|---|---|---|---|---|---|
| **Peng, Kalliamvakou, Cihon & Demirer**, arXiv:2302.06590, 13 Feb 2023 | RCT, single synthetic task (implement an HTTP server in JavaScript) | 95 professional developers | GitHub Copilot, inline completion | **55.8% faster** | Controlled study |
| **Paradis et al.**, arXiv:2410.12944, Oct 2024 | RCT, one complex enterprise-grade task, three AI features | 96 full-time Google engineers | Google-internal, summer 2024 | **~21% faster**; authors: "our confidence interval is large" and "we cannot assume that the effect size obtained in our lab study will necessarily apply more broadly" | Controlled study |
| **Cui, Demirer, Jaffe, Musolff, Peng & Salz**, *Management Science*, online 27 Feb 2026; pre-registered AEARCTR-0014530 | Three field RCTs at Microsoft, Accenture, and an unnamed Fortune 100 firm | 4,867 developers | GitHub Copilot, inline completion | **+26.08% completed tasks (SE 10.3%)**; less-experienced developers adopted more and gained more; authors note "each experiment is noisy and results vary across experiments" | Controlled study — **the strongest single piece of positive evidence in the field**, peer-reviewed and pre-registered |
| **METR (Becker, Rush, Barnes & Rein)**, arXiv:2507.09089, Jul 2025 | RCT, real issues in the developers' own mature repos (avg. 22k+ stars, 1M+ LOC), randomised per task | 16 developers / 246 tasks | Cursor Pro + Claude 3.5/3.7 Sonnet, Feb–Jun 2025 | **+19% completion time (slower)**; forecast −24%, self-estimate after −20% | Controlled study — see §2.2 |
| **Borg, Hewett, Hagatulah, Couderc, Söderberg, Graham, Kini & Farley**, arXiv:2507.00788 (v3 26 Feb 2026) | Two-phase controlled experiment: phase 1 build with/without AI, phase 2 *different* people evolve those solutions without AI | 151 participants, 95% professional | Java web application | Phase 1: **−30.7% median completion time** (habitual users ~−55.9%). Phase 2: **no significant difference** in completion time or code quality — "no consistent warning signs of degraded code-level maintainability" | Controlled study — **the only proper downstream-maintainability RCT located** |
| **Chen, Talwalkar, Brennan & Neubig**, arXiv:2507.08149 (v2 13 Sep 2025) | First controlled study of developer interaction with **coding agents vs copilots** | not stated in the abstract; participants recruited as regular copilot users | two leading copilot and agentic assistants | Agents "surpass copilots (e.g., completing tasks humans may not have accomplished) and reduce the effort required to finish tasks"; challenges remain "ensuring users adequately understand agent behaviors" | Controlled study — **the only controlled study on the copilot/agent axis specifically**, and it reports no headline effect size |
| **Shen & Tamkin (Anthropic)**, arXiv:2601.20245, 3 Feb 2026 | RCT: learn an unfamiliar Python library (Trio), then comprehension quiz | 52 mostly-junior engineers | AI sidebar able to generate correct code | **Quiz 50% (AI) vs 67% (hand-coded)**, d=0.738, p=0.01. Time gains modest and **not statistically significant**. Six interaction patterns; the three low-scoring ones are delegation-shaped, the three high-scoring ones are explanation-shaped | Controlled study |
| **Murphy-Hill, Butler & Savelieva**, arXiv:2607.01418, 1 Jul 2026 | Observational, four-month rollout, adopters vs counterfactual | tens of thousands of Microsoft engineers | Claude Code and GitHub Copilot CLI, early 2026 | **+24% merged PRs**. First use spread through social networks; engineering activity level (not demographics) predicted retention. Authors: "a merged PR is not the same as the value it delivers" | Semi-controlled study (self-selected adopters) |
| **He, Agarwal, Denisov-Blanch, Azaletskiy, Koyejo & Vasilescu**, arXiv:2607.01904, 2 Jul 2026 | Longitudinal case study of an enterprise "2× productivity" mandate; staggered difference-in-differences | 802 developers / 196,212 PRs, Jan 2024 – Apr 2026 | mixed | **Per-capita throughput reached 2.09× baseline** by Apr 2026; gains broadly shared across seniority but **concentrated in newer code**; reviewer workloads **~doubled**; **automated review surpassed human review in volume**; **merge and revert rates remained stable**. Authors: adoption is "a catalyst rather than a direct driver," and because adoption was not randomly assigned this implicates "an adoption-and-use channel rather than exact causal attribution" | Semi-controlled study |
| **Agarwal, He & Vasilescu**, arXiv:2601.13597, Jan 2026 | Staggered DiD with matched controls on open-source repos adopting agents | AIDev-derived repository panel | coding agents | Velocity gains **only where agents were the first AI tool**; repos already using IDE assistants saw minimal/temporary throughput gain. **Static-analysis warnings +~18%; cognitive complexity +~39%**, persisting after velocity gains faded | Semi-controlled study |
| **Afroz, Feng, Menezes, Kimura, Trinkenreich, Steinmacher & Sarma**, arXiv:2510.24265 (v2 5 Apr 2026), *"The Fast and Spurious"* | SPACE-framework survey | 415 practitioners | — | Faster completion and higher output for frequent users, but **effort redistribution**: increased review demand, cognitive strain from verification, stagnant collaboration. "Perceived productivity gains may be spurious — surface-level acceleration, often accompanied by redistributed effort and hidden costs" | Hard survey |

### 2.2 Negative and contrarian findings

#### The METR RCT, in full, including its own retraction of emphasis

**Becker, Rush, Barnes & Rein, arXiv:2507.09089** (submitted 12 Jul 2025, revised 25 Jul 2025). Tier: **controlled study**.

*Methodology, exactly.* 16 experienced open-source developers, recruited from repositories they had contributed to for years (average 5 years' prior experience on that codebase; repos averaging 22,000+ stars and 1M+ lines). 246 real issues from those repos, each ~2 hours. Each issue randomly assigned AI-allowed or AI-disallowed. Screen recordings plus self-reported implementation times. Paid $150/hour. When allowed, developers used mainly Cursor Pro with Claude 3.5/3.7 Sonnet.

*Result.* Developers forecast a **24% reduction** in completion time before starting; estimated a **20% reduction** afterward; **actually took 19% longer**. Expert forecasters were worse still (economists 39% shorter, ML researchers 38% shorter). METR evaluated **20 candidate explanatory properties** of the setting and concluded that "although the influence of experimental artifacts cannot be entirely ruled out, the robustness of the slowdown effect across our analyses suggests it is unlikely to primarily be a function of our experimental design."

*What METR explicitly says the result does NOT show* (their own list): that AI does not speed up many or most developers; anything outside software development; anything about future AI trajectories; anything about alternative prompting strategies or fine-tuning. They state results "don't generalize beyond their specific setting."

*Credible limitations, several of which METR raises itself:*

- **N=16 developers.** 246 tasks give statistical power, but developer-level clustering is thin and the population is unusual: expert maintainers of large, high-standard, high-implicit-requirement codebases.
- **Tool era.** Cursor + Claude 3.5/3.7 Sonnet, Feb–Jun 2025. Two generations of coding agent have shipped since.
- **Learning effects.** Participants had only dozens of hours with Cursor. METR tested this — breaking results down by prior AI experience and by Cursor hours showed no difference, and developers did not get faster over the study — but concedes that effects appearing only after several hundred hours would be invisible to them.
- **Quality-standard confound.** METR suggests AI may underperform "in settings with very high quality standards, or with many implicit requirements relating to documentation, testing coverage, or linting/formatting."
- **Self-reported time** on screen-recorded sessions.

*⚠️ **The rebuttal that matters most came from METR itself.*** On **24 Feb 2026** METR published *"We are Changing our Developer Productivity Experiment Design."* A late-2025 rerun (57 developers) estimated **−18% speedup (CI −38% to +9%)** for the 10 returning developers and **−4% (CI −15% to +9%)** for 47 newly recruited ones. Both intervals cross zero. METR then declared the data unusable:

> "we believe that the data from our new experiment gives us an unreliable signal of the current productivity effect"

Selection effects they identified: developers increasingly refused to participate at all rather than work without AI; **"30% to 50% of developers told us that they were choosing not to submit some tasks because they did not want to do them without AI"**; task types differed by condition; code quality and documentation differed by condition; some AI-disallowed tasks were simply skipped; and concurrent multi-agent use made time tracking unreliable. Their current position:

> "it is likely that developers are more sped up from AI tools now — in early 2026 — compared to our estimates from early 2025 … because of the selection effects in our experiment, our data is only very weak evidence for the size of this increase."

**How to present METR, honestly.** The 2025 result is real, well-executed, and the perception gap it documents (a 39-point divergence between belief and measurement) is its most durable contribution. The **−19% figure is not a current estimate of anything**, and its own authors no longer defend it as one. Anyone citing "AI makes developers 19% slower" in 2026 without the February 2026 update is misrepresenting the source. Anyone citing the February 2026 update as proof AI works is *also* misrepresenting it — those intervals cross zero and METR says the data is weak.

#### Other negative findings

- **Skill formation** (Shen & Tamkin, N=52, RCT): −17 percentage points on comprehension, largest deficits under full delegation, worst in debugging, and **no significant time saving to trade against it**. The three lowest-scoring interaction patterns are AI delegation (copy-paste without reading), progressive AI reliance, and iterative AI debugging; the three highest-scoring involve asking for explanations or conceptual questions. Small N, junior-skewed, immediate post-test only — the authors flag all three.
- **Cognitive shape** (Bari/Copenhagen biometrics study, arXiv:2606.20598, 19 May 2026; within-subjects crossover; EEG, eye-tracking, EDA, HRV, NASA-TLX): lower EEG θ/α ratio and higher blink rate with AI, indicating "reduced cognitive engagement when developers offload generative effort to the model," and the conclusion that "AI-assisted programming is not a faster version of solo coding but a cognitively distinct activity." University participants; no productivity outcome.
- **Agent failure modes at scale** (Tang et al., arXiv:2605.29442, 28 May 2026): 20,574 real agent sessions across 1,639 repositories. **90.50% of misalignment episodes cost effort and trust rather than causing irreversible damage — but 91.49% of visible resolutions required explicit user correction.** Agents rarely self-resolve. Overall failure rates declined over time, but **constraint violations and inaccurate self-reporting grew as a share**. That second trend is the one that matters for autonomy: the failures that remain are precisely the ones an unsupervised setup cannot catch.
- **Agent PR rejection** (Abujadallah, Arabat & Sayagh, MSR '26, arXiv:2606.13468): **~46.41% of agent-proposed fixes rejected**; qualitative and quantitative analysis of 306 non-merged PRs; four categories — incorrect implementation, CI/test failures, unable to complete, low priority.
- **Security is flat** (Veracode, Spring 2026; vendor): ~55% security pass rate, **essentially unchanged over two years** (45–55% band) while syntax correctness went from ~50% to 95%+. Java worst (29%), Python best (62%); XSS pass rate 15%, SQL injection 82%. Limitation stated by Veracode: tests out-of-the-box generation with no security prompting, four CWE types only. Vendor incentive is obvious and should be stated when citing.

### 2.3 Code quality and maintainability over time — a genuine standoff

**Position A: measurable structural degradation.**

- **GitClear, *The Maintainability Gap* (2026).** Tier: vendor-reported metric. 623M analysed code changes, 2023–2026. Reuse signals down (cross-file function connectivity −35% since 2023; legacy-code updates −74%; moved/refactored code 21% in 2022 → 3.8% in 2026). Risk signals up (block duplication 40.3 → 73.0 per million changed lines, +81%; copy/paste to 15.7% of changed lines; error-masking constructs +47%; two-week churn +15%). Earlier waves: churn 3.3% pre-AI → 5.7% (2024) → 7.1% (2025); 2024 was the first year on record where within-commit copy/paste exceeded moved code.
  ⚠️ **Weaknesses.** GitClear presents this as correlational ("as AI authorship has scaled … the structural habits have eroded") and does **not** claim causation. It publishes **no methodological limitations section**, does not disclose repository count or composition, and does not normalise for the changing population of repos in its dataset. GitClear sells code analytics. And GitClear's own founder has written that treating churn as a process defect is "inherently flawed" because "churn only exists relative to a developer's commit habits."
- **Faros AI, *The Acceleration Whiplash* (Mar 2026).** Tier: vendor-reported metric. Two years of telemetry, 22,000 developers, 4,000+ teams, comparing each organisation's own lowest- and highest-AI-adoption periods. PR size +51%, bugs per PR +28%, bugs per developer +54%, incidents-to-PR ratio +242.7%, monthly production incidents +57.9%, code churn +861%, median time to first review +156.6%, average time in review +199.6%, PRs merged without any review +31.3%, deployments per week −11.7% — against epics +66.2%, task throughput +33.7%, PR merge rate +16.2%.
  ⚠️ **Weaknesses.** Within-organisation before/after with **no numeric threshold published** for "low" vs "high" adoption; no control for calendar-time confounds (2024→2026 also contains layoffs, reorgs and tooling migrations); Faros sells the platform that measures this and benefits commercially from a governance narrative. To its credit Faros states its own limits ("may not reflect every team's experience") and states its disagreement with DORA openly rather than eliding it.
- **Agarwal, He & Vasilescu, arXiv:2601.13597.** Tier: semi-controlled study — and **the only one of the three degradation findings with a causal design** (staggered DiD, matched controls). Static-analysis warnings **+~18%**, cognitive complexity **+~39%**, persisting after velocity gains faded. Open-source repositories only.

**Position B: no detectable maintainability harm.**

- **Borg et al., arXiv:2507.00788, N=151, 95% professionals.** Two-phase RCT: cohort 1 builds features with or without AI; cohort 2 (fresh participants, no AI) then evolves cohort 1's code. **No significant difference in completion time or code quality in phase 2.** "No consistent warning signs of degraded code-level maintainability." The authors are careful — they flag code bloat and cognitive debt as untested — but this is a direct experimental test of the exact claim Position A makes observationally, and it comes out negative.
- **Mazloomzadeh, Morovati & Khomh, arXiv:2607.21832 (23 Jul 2026).** AIDev-based; 2,275 merged agentic PRs matched against 2,275 human PRs. **"Agentic PRs show comparable or lower defect proneness than human PRs, with mostly non-significant differences."** Most structural differences between agentic and human PRs are "limited in practical magnitude." Merge rates: Claude 84.3%, Codex 73.5%, Cursor 63.9%, Copilot 59.6%, Devin 43.0%, against human PRs at ~84–86%. Agentic contributions concentrate in documentation, dependency management, testing, refactoring and CI; mergeability is ≥0.80 for documentation/dependencies/testing/CI and ≤0.60 for LLM integration, model evaluation and function implementation. Limitations the authors state: Python repos only, >100 stars only, data ends 10 Aug 2025, heuristic agent detection.
- **He et al., arXiv:2607.01904** found **merge and revert rates remained stable** through a doubling of throughput at one enterprise.

**What would resolve this standoff.** The two positions are measuring different things and neither is wrong on its own terms. Position A measures *structural properties of the code corpus* (duplication, complexity, churn) and *operational outcomes* (incidents). Position B measures *the cost to a human of subsequently changing the code* and *defect proneness of merged units*. It is entirely coherent for duplication to rise 81% while a maintainer's task time is unchanged — for a while. The resolving study does not exist: **nobody has run a long-horizon (12+ month) controlled comparison of maintenance cost on AI-authored versus human-authored subsystems in the same production codebase.** Until that exists, present both and say so.

⚠️ **Note the tier asymmetry.** Every "quality is degrading" finding at industry scale is a **vendor-reported metric** from a company selling remediation. Every "quality is fine" finding is a **controlled or semi-controlled academic study** with a small or narrow sample. Neither asymmetry is decisive, but a reader should see it.

### 2.4 Does AI shift the bottleneck to review?

**Evidence that it does:**

- **He et al., arXiv:2607.01904** (802 devs, 196,212 PRs, DiD): reviewer workloads **approximately doubled**; **automated review surpassed human review in volume**. This is the best-designed evidence on the question.
- **Faros AI** (vendor telemetry, 22,000 devs): median time to first review **+156.6%**, average time in code review **+199.6%**, daily PR contexts per developer **+67.4%**.
- **LinearB, 2026 Software Engineering Benchmarks** (vendor; 8.1M PRs, 4,800 teams, 42 countries, pub. 4 May 2026): agentic PRs wait **5.3× longer for reviewer pickup** (1,055 vs 201 minutes); AI-assisted PRs are ~**154%** larger (at the 75th percentile 400+ vs 157 lines); AI-assisted PR acceptance **32.7%** vs **84.5%** unassisted; refactoring share in AI-assisted PRs near **zero** at the 75th percentile vs 37% unassisted. LinearB classifies PRs into unassisted / AI-assisted / agentic but **does not publish the classifier**.
- **Sonar, *State of Code* (N=1,149, pub. Jan 2026):** **96%** do not fully trust AI-generated code to be functionally correct; only **48%** always verify before committing; **38%** say reviewing AI code takes more effort than reviewing a colleague's. AI accounts for **42%** of committed code today, projected 65% by 2027. **64%** use autonomous agents; average team uses **4** AI coding tools; **35%** access AI tools through personal, non-sanctioned accounts; **40%** of juniors report the highest productivity gains.
- **GitLab, *2026 AI Accountability Report*** (Harris Poll, **1,528** developers and technology buyers, six countries, 23 Jun 2026): **85%** agree AI has shifted the bottleneck from writing to reviewing; 80% say adoption outran policy; 92% report governance challenges; 91% use ≥2 AI coding tools and 54% use three or more; 78% say developers commit code faster; 73% concerned about maintainability; 82% say it risks new technical debt; **43% cannot reliably distinguish AI-generated from human-written code in their own codebase**.

**Evidence that it does not — or that the framing is wrong:**

- **The New Stack, "AI hasn't shifted the bottleneck from coding to code review"** `[SECONDARY]` — the article body would not extract; the argument, per its headline and search summarisation, is that if work accumulates *after* review then review is not the constraint, and the real queue is downstream deployment batching. Consistent with Faros's own **−11.7% deployments per week** alongside +33.7% throughput. **Flagged as secondary, and as argument rather than measurement.**
- **He et al.** found merge and revert rates **stable** while throughput doubled — the review system absorbed the load without a quality collapse at that company.
- **GitHub Octoverse 2025** (platform telemetry + interviews): **72.6% of developers who use Copilot code review said it improved their effectiveness** — the review capacity itself is being augmented.

**What would resolve it.** The disagreement is partly definitional (is "the bottleneck" the longest queue, or the stage where WIP accumulates?) and partly a measurement gap: the survey evidence (85% agree) is *perception*, and perception in this field has a documented 39-point error bar (§2.2). **A study that measures end-to-end value-stream constraint location before and after agent adoption, rather than asking people where they think it is, does not exist.**

### 2.5 Outcomes at high autonomy — the honest answer is that this is barely measured

**This is the thinnest part of the entire evidence base, and it is thin in a specific way: there is a growing amount of data on *how much* unsupervised agent work is happening, and essentially none on *whether it works*.**

What exists:

| Evidence | What it shows | Tier | What it cannot tell you |
|---|---|---|---|
| **Duma, Wróblewski, Bobińska, Winiarska & Przymus**, EASE 2026, arXiv:2605.02273 (4 May 2026) | **Most AI-generated PRs receive no reviews whatsoever.** Where review occurs it is "automation-mediated"; human involvement typically takes the form of *agent steering* rather than independent assessment. Human-authored PRs attract substantially more direct human feedback | Semi-controlled study (mining the AIDev corpus) | Nothing about outcomes. The authors' own framing is a warning to researchers that "review metrics may not accurately represent human oversight levels" in agentic environments |
| **Faros AI** | PRs merged **without any review up 31.3%** at high AI adoption | Vendor-reported metric | Not linked to outcome at the PR level — the incident figures are org-level, not attributed to unreviewed PRs specifically |
| **Anthropic Institute**, *When AI builds itself*, 4 Jun 2026 | **>80% of code merged into Anthropic's codebase authored by Claude** as of May 2026, from "low single digits" before Claude Code's Feb 2025 preview | Vendor-reported metric | Anthropic's own caveats: LOC "is an imperfect measure, as it measures quantity over quality"; the attribution pipeline has "gaps"; it excludes auto-generated artifacts (making it conservative). Crucially, **"merged" here still means after review** — this is not a claim about unsupervised merging |
| **Razorpay engineering**, Jun 2026 | Thousands of PRs merged monthly through an internal agentic system ("Slash"); **over a third merged with no human in the loop**; low-severity PRs auto-approved; review performed by specialised sub-agents (bug detection, security, code quality, design system, i18n, pre-mortem) with an AI false-positive filter; every change still passes the same checks as a human-authored one | **Practitioner anecdote** | One company, self-published, no outcome data, no control period, no defect or incident comparison |
| **He et al.**, arXiv:2607.01904 | **Automated review surpassed human review in volume** while merge and revert rates stayed stable | Semi-controlled study | One enterprise; revert rate is a coarse proxy for "was this safe" |
| **Tang et al.**, arXiv:2605.29442 | **91.49% of visible agent-misalignment resolutions required explicit user correction**; constraint violations and inaccurate self-reporting are a *growing share* of remaining failures | Semi-controlled study | Measures agent failure with a human present. Says nothing directly about outcomes when no human is present — but it is the strongest indirect evidence that removing the human removes the resolution mechanism |

**What does not exist, stated plainly:**

1. **No controlled or quasi-controlled study compares outcomes for agent-authored changes merged with human review against agent-authored changes merged without it.** Not one. This is the central empirical question for the top of the autonomy spectrum and nobody has published an answer.
2. **No population statistic** for what fraction of professional teams operate agents with reduced human review. Faros's +31.3% is a *change*, not a level. Duma et al.'s "most" is over an open-source corpus, not professional teams.
3. **No published telemetry from Cursor or any AI-IDE vendor** on the completion/chat/agent/autonomous split. Searched specifically; Cursor publishes engineering blogs but not usage telemetry. Anthropic's Economic Index is the only vendor autonomy telemetry in existence, and it measures conversational autonomy, not merge autonomy.
4. **No incident or defect data attributable to unsupervised merges.** The industry-scale incident figures (Faros) cannot be decomposed by review status.

**How to write about this section of the spectrum:** describe the practices, cite the volume evidence, and state that the efficacy evidence is absent. Do not let the availability of adoption numbers at the high-autonomy end substitute for outcome numbers, which do not exist.

### 2.6 The one number the field agrees on

Amid all the conflict, one finding replicates across every instrument and every tier: **people cannot estimate their own AI-assisted productivity.**

- **METR:** 39-point gap between self-estimate (−20%) and measurement (+19%).
- **Afroz et al.** (N=415, SPACE framework): "perceived productivity gains may be spurious — surface-level acceleration, often accompanied by redistributed effort and hidden costs."
- **DORA 2025:** >80% perceive increased productivity, while the same survey finds AI's association with delivery instability remains negative.
- **Murphy-Hill et al.** (Microsoft): a documented divergence between developer sentiment and measured output — Copilot CLI adopters showed a **larger PR lift** than Claude Code adopters, despite Claude Code being the more highly rated tool in early-2026 comparisons.
- **Sonar:** 96% don't fully trust the code, 48% always verify it — a 48-point gap between stated belief and stated behaviour.

**Consequence for this project:** any figure in these documents that originates in self-report about productivity should be labelled as *perceived* productivity, not productivity.

---

## 3. Evidence quality

### 3.1 The four tiers, as used here

**Tier 1 — Hard survey data.** A published survey report with a stated sample size and (ideally) a stated methodology. *Systematic weakness:* every developer survey in this document is **opt-in**. None publishes a non-response analysis. Adoption figures are plausibly biased upward across the board, and the bias grows as AI use becomes a professional expectation (JetBrains 2025: 68% expect employers to require AI proficiency). Self-report about one's own productivity is additionally unreliable in a documented, measured way (§2.6).

**Tier 2 — Controlled and semi-controlled study.** Independent, peer-reviewable work with a comparison group or an explicit causal identification strategy. Within this tier:

- *Randomised* (Peng, Paradis, Cui, METR, Borg, Shen & Tamkin, Chen) — strongest.
- *Quasi-experimental with identification* (He et al. and Agarwal et al., both staggered DiD; Murphy-Hill et al., adopter-vs-counterfactual) — strong for direction, weak for magnitude, because adoption is self-selected in all three.
- *Observational repository mining* (AIDev-derived work: Duma, Mazloomzadeh, Abujadallah, Robbes, Tang) — descriptive. No control. Excellent for "what is happening," poor for "what does it cause." Labelled semi-controlled throughout.

**Tier 3 — Vendor-reported metric.** Telemetry or measurement published by a company with a commercial position in the outcome. Includes GitClear, Faros AI, LinearB, Sonar, Veracode, GitLab, GitHub Octoverse, and the Anthropic Economic Index. *Systematic weaknesses:* **survivorship** (telemetry sees only customers who kept the product); **selection** (customers of a developer-analytics platform are not a random sample of engineering organisations); **incentive alignment** (every degradation finding at industry scale comes from a company selling remediation, and every capability finding comes from a company selling capability); and **methodology opacity** — GitClear publishes no limitations section, LinearB does not publish its AI/agentic PR classifier, and Faros does not publish its low/high adoption thresholds.

**Tier 4 — Practitioner anecdote.** Single-company engineering blogs, conference talks, individual reports. Used here only for the Razorpay case, and only because nothing better exists at that point on the spectrum. Never load-bearing.

### 3.2 Which headline numbers are weaker than they look

- **"90% of developers use AI."** Weaker than it looks. Three different surveys produce 75%, 84% and 90% depending on question wording and population; the highest figures use the broadest constructs ("use or plan to use," "within your job function") and the most tool-correlated weighting. **Range, not point estimate.**
- **"90% of developers use AI agents weekly" (JetBrains, May–Jul 2026).** Much weaker than it looks. Self-report, no shared definition of "agent," weighted partly on JetBrains familiarity, and contradicted by roughly a factor of three by repository-trace mining. It is the single most quotable and least corroborated number in this document.
- **"AI makes experienced developers 19% slower."** Weaker than it looks and **no longer defended by its authors** as a current estimate. See §2.2.
- **"Anthropic's code is 80% written by Claude."** Weaker than it looks *for this project's purposes* — not because the measurement is bad (Anthropic caveats it well) but because it is a lines-of-code count at one AI lab with unusual tooling, unusual staff and an unusual codebase, and it describes *authorship*, not *unsupervised merging*. It is routinely repurposed in discourse as evidence about autonomy. It is not.
- **DORA's 2026 ROI figures ($11.6M return on $8.4M, 39% first-year ROI, ~8-month payback, 15% J-curve dip).** Much weaker than they look. **These are modelled, not measured.** The 2026 report (v.2026.1, 22 Apr 2026) is a *value model* built on Google Cloud's Value Realisation practice applied to an illustrative 500-person organisation at $176k fully-loaded salary; the 15% productivity dip is explicitly a placeholder input, not a measurement; the "instability tax" assumes a change failure rate rising 5%→6%. DORA itself writes: "Treat these calculations as a high-uncertainty estimate meant to spark a conversation, rather than a rigid mathematical formula." **There was no new DORA survey wave in 2026** as of this research date — the 2026 publication is an ROI framework, not a second annual dataset. Cite the 2025 survey for data and the 2026 report only for framing.
- **All GitClear percentage changes.** Real measurements over a real corpus, but with an undisclosed and changing repository population, no limitations section, and a strictly correlational claim that is routinely reported as causal.
- **LinearB's "AI PRs accepted 32.7% vs 84.5%."** The gap is large and the corpus is large, but the classifier that decides which PRs are "AI-assisted" is not published, and academic measurement of agent merge rates on open source finds **43.0%–84.3%** depending on agent. The populations differ (enterprise teams vs open-source repos) but the classifier opacity means the conflict cannot be adjudicated.
- **Any figure about the top of the autonomy spectrum.** See §2.5.

---

## 4. Sources

All accessed **2026-08-27** unless noted otherwise.

### Surveys (Tier 1)

- https://survey.stackoverflow.co/2025/ai — Stack Overflow Developer Survey 2025, AI section (fielded May–Aug 2025)
- https://stackoverflow.blog/2026/06/23/the-2026-developer-survey-is-now-open-for-human-developers-only/ — 2026 survey **opened** 23 Jun 2026; **no 2026 results published as of this date**
- https://survey.stackoverflow.co/2026/ and https://survey.stackoverflow.co/2026/ai — **both HTTP 404** (confirming no 2026 results)
- https://dora.dev/dora-report-2025/ — landing page; report content reached via research.google and blog.google
- https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/ — DORA 2025, authors and abstract (~5,000 professionals, 100+ hours qualitative; DeBellis, Storer, Harvey et al.)
- https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/ — DORA 2025 figures (90% adoption, 2h median, trust breakdown: 4% great deal / 20% a lot / 23% a little / 7% not at all)
- https://dora.dev/insights/balancing-ai-tensions/ — DORA insight incl. 1,110 open-ended responses from Google engineers, Q3 2025
- https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/ — N=24,534, 194 countries, fielded Apr–Jun 2025
- https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/ — AI Pulse Jan 2026, N>10,000
- https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ — Dev Ecosystem 2026, N>15,000, fielded May–Jul 2026
- https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/ — same instrument; the depth-of-usage segmentation
- https://www.slashdata.co/post/75-of-professional-developers-are-using-ai-assisted-tools-insights-on-developer-tools-usage-and-me — Developer Nation Q1 2026, N>12,400, 95 countries
- https://www.sonarsource.com/company/press-releases/sonar-data-reveals-critical-verification-gap-in-ai-coding/ — Sonar State of Code, N=1,149, pub. Jan 2026 ⚠️ vendor-commissioned survey
- https://about.gitlab.com/resources/ai-accountability-survey-2026/ — GitLab AI Accountability Report, Harris Poll, N=1,528, six countries, 23 Jun 2026 ⚠️ vendor-commissioned survey

### Controlled and semi-controlled studies (Tier 2)

- https://arxiv.org/abs/2302.06590 — Peng, Kalliamvakou, Cihon & Demirer, 13 Feb 2023, N=95
- https://arxiv.org/abs/2410.12944 — Paradis et al., Oct 2024, N=96 Google engineers
- https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535 — Cui, Demirer, Jaffe, Musolff, Peng & Salz, *Management Science*, online 27 Feb 2026, N=4,867, AEARCTR-0014530
- https://arxiv.org/abs/2507.09089 — Becker, Rush, Barnes & Rein (METR), 12 Jul 2025, N=16 / 246 tasks
- https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ — METR blog version with the 20-property analysis
- https://metr.org/blog/2026-02-24-uplift-update/ — **METR's own design change and walk-back, 24 Feb 2026, N=57**
- https://arxiv.org/abs/2507.00788 — Borg, Hewett, Hagatulah, Couderc, Söderberg, Graham, Kini & Farley, *Echoes of AI*, v3 26 Feb 2026, N=151
- https://arxiv.org/abs/2507.08149 — Chen, Talwalkar, Brennan & Neubig, v2 13 Sep 2025 — copilot vs agent, controlled
- https://arxiv.org/abs/2601.20245 — Shen & Tamkin, *How AI Impacts Skill Formation*, 3 Feb 2026, N=52
- https://www.anthropic.com/research/AI-assistance-coding-skills — Anthropic's own write-up of the above, with effect sizes and the six interaction patterns
- https://arxiv.org/abs/2607.01418 — Murphy-Hill, Butler & Savelieva, 1 Jul 2026, Microsoft CLI agent rollout
- https://arxiv.org/abs/2607.01904 — He, Agarwal, Denisov-Blanch, Azaletskiy, Koyejo & Vasilescu, 2 Jul 2026, N=802 devs / 196,212 PRs
- https://arxiv.org/abs/2601.13597 — Agarwal, He & Vasilescu, Jan 2026, staggered DiD on agent adoption
- https://arxiv.org/abs/2510.24265 — Afroz, Feng, Menezes, Kimura, Trinkenreich, Steinmacher & Sarma, *The Fast and Spurious*, v2 5 Apr 2026, N=415
- https://arxiv.org/abs/2601.18341 — Robbes, Matricon, Degueule, Hora & Zacchiroli, *Agentic Much?*, v2 8 Apr 2026, 128,018 projects
- https://arxiv.org/abs/2602.09185 — Li, Zhang & Hassan, *AIDev*, 9 Feb 2026 — 932,791 agentic PRs, 116,211 repos, 72,189 developers, 5 agents (Codex, Devin, Copilot, Cursor, Claude Code)
- https://arxiv.org/abs/2605.02273 — Duma, Wróblewski, Bobińska, Winiarska & Przymus, EASE 2026, 4 May 2026 — review of agentic PRs
- https://arxiv.org/abs/2606.13468 — Abujadallah, Arabat & Sayagh, MSR '26 — agent fix rejection, 306 non-merged PRs
- https://arxiv.org/abs/2607.21832 — Mazloomzadeh, Morovati & Khomh, 23 Jul 2026 — agentic vs human PR merge rates and defect proneness
- https://arxiv.org/abs/2605.29442 — Tang et al., 28 May 2026 — 20,574 sessions, 1,639 repos, agent misalignment
- https://arxiv.org/abs/2512.14012 — Huang, Reyna, Lerner, Xia & Hempel, v2 18 Aug 2026 — *Professional Software Developers Don't Vibe, They Control*
- https://arxiv.org/abs/2606.20598 — biometrics study of AI-assisted coding performance and perception, 19 May 2026
- https://arxiv.org/abs/2608.00101 — Liu, Qiu, Goiri, Fonseca, Bianchini & Choukse, 30 Jul 2026 — Copilot traces at production scale

### Vendor-reported metrics (Tier 3)

- https://www.gitclear.com/the_ai_code_quality_maintainability_gap — GitClear, *The Maintainability Gap*, 2026, 623M code changes ⚠️ sells code analytics
- https://www.gitclear.com/ai_assistant_code_quality_2025_research — GitClear 2025 wave, 211M lines through 2024
- https://www.faros.ai/research/ai-acceleration-whiplash and https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways — Faros AI, Mar 2026, 22,000 devs / 4,000 teams ⚠️ sells engineering intelligence
- https://linearb.io/blog/8-million-prs-engineering-productivity — LinearB, 4 May 2026, 8.1M PRs / 4,800 teams / 42 countries ⚠️ sells AI code review and workflow automation
- https://www.veracode.com/blog/spring-2026-genai-code-security/ — Veracode Spring 2026, 150+ models, 80 tasks × 4 languages × 4 CWEs ⚠️ sells application security
- https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ — Octoverse 2025; Copilot coding agent 1M+ PRs May–Sep 2025; ~80% of new GitHub developers use Copilot in week one; 72.6% say Copilot code review improved effectiveness; measurement window Sep 2024–Aug 2025 ⚠️ GitHub distinguishes telemetry from survey in the source, and notes selection bias toward established repos
- https://www.anthropic.com/research/economic-index-june-2026-report — Anthropic Economic Index "Cadences," data 10 Apr – 10 Jun 2026, ~9,700 linked survey respondents, 1–5 autonomy scale ⚠️ vendor
- https://www.anthropic.com/institute/recursive-self-improvement — *When AI builds itself*, 4 Jun 2026, the >80% merged-code figure with its footnoted caveats ⚠️ vendor
- https://dora.dev/ai/roi/report/ and https://cloud.google.com/resources/content/dora-roi-of-ai-assisted-software-development — DORA ROI report (v.2026.1, 22 Apr 2026) ⚠️ **modelled, not measured**
- https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/ — InfoQ, 11 May 2026 `[SECONDARY]`, used for the ROI report's methodology and the explicit "high-uncertainty estimate" quote because dora.dev serves only a landing page to automated fetch

### Practitioner anecdote (Tier 4)

- https://razorpay.com/blog/razorpay-engineers-built-slash-slash-builds-the-rest/ — Razorpay, Jun 2026, "Slash" internal agentic system

### Secondary sources used and labelled

- https://thenewstack.io/ai-code-bottleneck-myth/ `[SECONDARY]` — body would not extract; argument summarised from search results only
- https://byteiota.com/stack-overflow-dev-survey-2026-ai-at-84-trust-at-3/ `[SECONDARY]` — cited **as evidence of mislabelling**, not as a source of data (pub. 11 Jun 2026; headlines 2025 figures as "2026"; its own body links to survey.stackoverflow.co/2025)

---

## Confidence and gaps

### High confidence

- **The Stack Overflow 2026 survey has not published results.** Verified three ways: the blog announcing it opened on 23 Jun 2026; `survey.stackoverflow.co/2026` and `/2026/ai` both return HTTP 404; and the "2026" secondary articles link to the 2025 dataset.
- **The Stack Overflow 2025 AI figures**, read directly from the survey site, including the agent-usage breakdown (14.1% daily / 9% weekly / 7.8% monthly / 37.9% no plans / 13.8% copilot-mode-only) and the vibe-coding figures (72.2% do not).
- **The METR RCT design, result, and its authors' February 2026 walk-back**, all from METR's own publications with confidence intervals quoted verbatim.
- **Cui et al. is peer-reviewed and pre-registered** — *Management Science*, online 27 Feb 2026, AEARCTR-0014530, +26.08% (SE 10.3%), N=4,867. This is the strongest positive result in the field and its provenance is clean.
- **DORA's 2026 publication is a value model, not a survey wave.** DORA says so itself and describes its own ROI figures as a high-uncertainty estimate with a placeholder J-curve input.
- **JetBrains' depth segmentation** (31/47/23 across agentic / AI-assisted / manual), read from JetBrains' own August 2026 research post along with its methodology and its data-cleaning admission.
- **Anthropic's >80% figure and its caveats**, read from Anthropic's own footnotes.
- **The absence of any controlled study on reduced-review agent operation.** Searched specifically across arXiv, vendor research pages and general web; found volume evidence and failure-mode evidence, no outcome comparison. This is a negative finding I am confident in.
- **Faros explicitly and by name disagrees with DORA 2025** on whether strong engineering foundations protect against AI's downsides — quoted verbatim from Faros's own page.

### Medium confidence

- **Chen et al. (arXiv:2507.08149) sample size.** The abstract page does not state N and the full text was not retrieved. The study's *existence and design* as the only controlled copilot-vs-agent comparison is confirmed; **do not quote a sample size for it.**
- **The exact confidence interval on the METR 2025 result.** The arXiv abstract does not state one; METR's blog says clustered standard errors are in Appendix D. The point estimate (+19%) is certain; **do not assert a CI for the 2025 study.** The 2026 follow-up CIs (−38% to +9%; −15% to +9%) *are* stated and are quoted here.
- **The arXiv:2607.21832 merge rates by agent** (Claude 84.3%, Codex 73.5%, Cursor 63.9%, Copilot 59.6%, Devin 43.0%) — extracted from the paper's HTML rendering rather than the abstract. Directionally solid; re-verify exact digits before publication.
- **LinearB's precise table values.** LinearB's write-ups present near-duplicate figures (84.4% vs 84.5% acceptance; 5.3× vs 4.6× pickup ratio across different pages). Use the raw minutes (1,055 vs 201) rather than the derived multiple.
- **The New Stack's counter-argument on the review bottleneck.** Headline and thesis confirmed; body text not retrieved. `[SECONDARY]`, and treated as argument rather than evidence.
- **Company-size breakdowns generally.** Only one primary datum exists (Copilot at 40% in 5,000+ employee firms, JetBrains Jan 2026). Everything else returned by search on enterprise-vs-startup depth was content-farm aggregation with no traceable instrument, and was deliberately excluded.

### Low confidence / could not establish

- **The true level of agentic adoption.** The 22–29% (trace mining) vs ~31% (SO 2025) vs 64% (Sonar) vs 90% (JetBrains) spread is unresolved and, on current instruments, unresolvable. Nobody has instrumented a fixed cohort and compared self-report against tooling logs.
- **Whether AI-assisted code degrades maintainability.** Genuine standoff between vendor telemetry (yes, strongly) and controlled experiment (no detectable effect). Neither side is refuted. §2.3 states what would resolve it.
- **Whether the bottleneck has moved to review.** 85% of surveyed practitioners say yes; the best-identified study finds reviewer load doubled but merge and revert rates stable; a counter-argument places the constraint downstream. Perception evidence in this field carries a documented 39-point error bar.
- **Anything about efficacy at high autonomy.** See §2.5. This is not "the evidence is mixed"; it is "the study has not been done."
- **What fraction of professional teams run agents with reduced human review.** No population statistic exists.
- **Cursor / Windsurf / other AI-IDE usage telemetry.** Searched specifically. **None published.** Cursor runs an engineering blog but publishes no aggregated usage data. This is a real hole: the vendor best placed to publish the completion/chat/agent split does not.
- **Non-response bias in any developer survey cited here.** None of the four major instruments publishes a non-response analysis.
- **Domain breakdowns** (fintech vs games vs embedded vs healthcare). Nothing primary found. JetBrains offers a language proxy (C/C++ lowest agent adoption, 38% of code still manual) which is suggestive of a safety-critical/systems-programming effect, but that is inference, not measurement.
- **Longitudinal cost of AI-authored code past ~12 months.** Nothing exists. GitClear's corpus goes back to 2023 but measures structure, not cost; Borg et al. measure cost but over a single experimental session.

### Blocked or unavailable sources (stated for auditability — none circumvented)

- `survey.stackoverflow.co/2026` and `/2026/ai` — **HTTP 404** (not blocked; not yet published)
- `dora.dev/dora-report-2025/` and `dora.dev/ai/roi/report/` — serve landing pages only to automated fetch; the reports themselves sit behind a Google Cloud form. Content obtained from research.google, blog.google, dora.dev/insights and InfoQ.
- `thenewstack.io/ai-code-bottleneck-myth/` — returns navigation chrome only to automated fetch; body not retrieved
- `arxiv.org/abs/2607.21832` — abstract page did not carry the quantitative results; obtained from the paper's HTML rendering instead
- Cursor, Windsurf and other AI-IDE vendors — **no usage telemetry published to block access to**

### Things this project will need to reckon with

1. **"Uses AI" and "lets AI act" are not merely different questions — they produce answers that differ by roughly a factor of three, and no instrument reconciles them.** The project's central axis is real, and it is the axis the survey industry is worst at measuring. Say so in the documents rather than picking a number.

2. **The most-cited contrarian finding in the field has been withdrawn as a current estimate by its own authors.** METR's −19% is now historical. A document citing it without the 24 Feb 2026 update is out of date; a document citing the update as vindication of AI is also wrong, because METR declared that data unusable. The durable finding from METR is the **perception gap**, not the slowdown.

3. **The quality debate splits cleanly along tier lines, and that should be visible to the reader.** Every industry-scale "quality is degrading" number is a vendor metric from a company selling remediation. Every "quality is fine" number is an academic study with a narrow sample. This does not settle the question; it does mean neither camp should be quoted without its tier.

4. **The top of the autonomy spectrum is described, not measured.** Volume data exists (Anthropic >80%, Faros +31.3% unreviewed, Razorpay >1/3, Duma et al.'s "most agentic PRs unreviewed"). Outcome data does not exist at all. The temptation to let adoption figures stand in for efficacy figures will be strongest exactly where the evidence is weakest.

5. **Perception is a measured variable in this field, and it is measurably wrong.** Five independent sources across three tiers agree that self-assessed AI productivity diverges from measured output. Any survey-derived productivity claim in these documents should be labelled *perceived*.

6. **The evidence base itself is being contaminated by AI-generated aggregation.** A concrete case is documented in §1.3: multiple 2026 blogs report the 2025 Stack Overflow survey as the 2026 survey, with correct figures under a wrong year. When the field's own reporting layer cannot keep the year straight, going to the published report is not a stylistic preference — it is the only way to get the date right.

7. **The instrument that would settle most of this does not exist.** A fixed cohort of professional developers, instrumented at the tooling layer, tracked for twelve months, with (a) logged interaction depth, (b) logged review status per merged change, and (c) linked defect and incident outcomes. Every unresolved conflict in this document would be resolved by it. Nobody has run it.
