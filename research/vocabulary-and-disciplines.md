# Vocabulary and Disciplines of AI-Assisted Software Engineering

**Research date:** 2026-08-27
**Purpose:** Establish a precise, primary-sourced glossary for a set of documents about how development teams work with AI coding agents.
**Method:** Live web research against primary sources (specs, official docs, engineering blogs, papers). Secondary sourcing is labelled inline as `[SECONDARY]`. Vendor marketing is flagged per term.

---

## Verdict summary

| Term | Is it real vocabulary? | Recommended usage for this project |
|---|---|---|
| **Harness engineering** | **YES — established, and faster than almost any term in this field.** Coined by Mitchell Hashimoto 5 Feb 2026; OpenAI published a post *titled* "Harness engineering" six days later; Thoughtworks/martinfowler.com, LangChain, Anthropic, Addy Osmani and multiple arXiv papers followed. Wikipedia has an "Agent harness" article. | **Use it.** This was the single biggest surprise of the research: the commissioning brief expected a negative finding here and the opposite is true. Define it once as "everything that isn't the model" and be precise about the eval-harness collision. |
| **Graph engineering** | **NO — not a term of art.** All usage traces to a cluster of 2026 SEO/content-marketing blogs and Medium posts. No framework doc, no vendor engineering blog, no paper, no standards body, no named practitioner uses it. LangGraph — the framework it would describe — does *not* use the phrase. It also collides with the long-established, unrelated "knowledge graph engineering." | **Do not use.** Replace with **agent orchestration** (the established name) or, for the narrower "encode the control flow explicitly rather than letting the agent decide" idea, **flow engineering** (real, coined in a peer-reviewed-style paper, Jan 2024). See §4. |
| **Context engineering** | YES — genuine, widely adopted, and now the field's default framing. | Use it. Define scope explicitly, because scope *is* the contested part. |
| **Prompt engineering** | YES, but demoted. Now generally treated as a *subset* of context engineering, not a peer. | Use it only for the narrow sense (wording of instructions). Do not use it as the name of the discipline. |
| **Skills / Agent Skills** | YES — a published open specification (agentskills.io) since 18 Dec 2025, adopted by every major competitor. **But it has no neutral governance body**, contra some secondary sources claiming AAIF stewardship — I checked the repo and site and found none. | Use "Agent Skills" or "SKILL.md" capitalised. Call it "an open specification with broad multi-vendor adoption," not "an industry standard." Disambiguate from four older senses of "skill". See §3. |
| **Agent orchestration** | YES — the established name for the discipline in §4. | Use this as the primary term. |
| **Subagent** | YES — became standard vocabulary during 2025–2026. | Use it. |
| **Evals** | YES — thoroughly established. `openai/evals` went public 14 Mar 2023; canonical practitioner text is Hamel Husain, 29 Mar 2024. | Use it. **But the eval/benchmark distinction has no authoritative source** — Husain's post never uses the word "benchmark," and `openai/evals` conflates them in its own tagline. See §5.1. |
| **Eval harness vs agent harness** | Both real, and **actively being disentangled in the 2026 literature** because conflating them corrupts benchmark results. Anthropic defines both in adjacent sentences (9 Jan 2026). Note "scaffold" was the 2024 word for what is now the agent harness. | Always qualify on first use. This is the single most important disambiguation in the document. See §5.1 and §2. |
| **Guardrails** | **Substantially vendor product naming.** Meta's Llama Guard paper never uses the word; Microsoft's Content Safety docs never use it; Anthropic says "safeguards"; **AWS is actively renaming its guardrails to "controls" to "align better with industry usage."** OpenAI ships two incompatible things called Guardrails. | Name the actual mechanism (validation, allowlist, sandbox, classifier, tripwire); use "guardrails" only as an umbrella, if at all. See §5.2. |
| **Autonomy levels** | **NO standardised scale — confirmed against ISO, IEEE, NIST, SAE and the EU AI Act.** The vocabulary originates with DeepMind (Morris et al., arXiv:2311.02462, Nov 2023). **The two leading proposals contradict each other**: "Consultant" is Level 2 for DeepMind and Level 3 for Feng et al. Anthropic and OpenAI both explicitly declined discrete levels; Anthropic measures autonomy on a continuous 1–10 scale instead. | **Never write "L3 autonomy"** — it is uninterpretable without naming the scale. Treat autonomy as a per-action dial (Karpathy's "autonomy slider"), and describe what the human approves and when. See §5.3. |
| **Human in / on / out of the loop** | YES, with a sharp caveat: **it is advocacy-and-industry vocabulary, not regulatory vocabulary.** "loop" appears **zero times** in DoDD 3000.09 (2012 *and* 2023), the EU AI Act, the NIST AI RMF, UK MoD JCN 1/18, and the ICRC/US CCW commentaries. HOTL origin pinned: **USAF, 18 May 2009**. Trichotomy: **HRW, 19 Nov 2012**. | Use it per-action, never as a global setting. And note Anthropic's own telemetry: **93% of permission prompts are approved** — claiming HITL is not the same as having it. See §5.4. |
| **MCP** | YES — genuinely foundation-governed (AAIF / Linux Foundation, Dec 2025). But foundation hosting ≠ standards-body ratification. | Use it. Say "open protocol, foundation-governed" rather than "industry standard." See §5.5. |
| **Tool use / function calling** | YES — and now formally synonymous by both vendors' own admission. | Use **tool use** as head term; gloss "function calling" once as the legacy synonym. See §5.6. |
| **Context rot** | Real, but a descriptive umbrella rather than a mechanism. Chroma popularised it; nobody claims to have coined it. | Use it generally; use Breunig's four named modes (poisoning / distraction / confusion / clash) when precision matters. See §5.7. |
| **Agentic AI (as distinct from AI agent)** | **NO as observed usage.** Real only as a stipulated taxonomy in one paper. Peer-reviewed criticism says the word is "diluted beyond utility." | Avoid as a category. Use **AI agent** / **multi-agent system**. See §5.8. |
| **Verifier's Law** | YES — Jason Wei, Jul 2025, personal blog. The least marketing-contaminated term in this document. | Use it. It is the theoretical backbone for why the field moved to eval-driven and spec-driven workflows. See §5.9. |
| **Vibe coding** | YES, but its meaning has been degraded by over-application. **Karpathy has NOT disowned it** — the "vibe coding is dead" headlines misreport him. | Use only in Karpathy's original narrow sense (prototypes, personal tools). See §5.10. |
| **Vibe engineering** | Retired. Its own coiner, Simon Willison, conceded to "agentic engineering" in Feb 2026. | Do not use. |
| **Agentic engineering** | Emerging but rising fast; Karpathy, Apr 2026, endorsed by Willison. | Use as the name for professional AI-assisted development. Note it is young. See §5.10. |
| **Lethal trifecta / Agents Rule of Two** | YES — Willison Jun 2025 and Meta Oct 2025 respectively. Operational, checkable properties of a harness configuration. | Use both. See §5.12. |
| **AGENTS.md** | YES — and genuinely AAIF-governed, unlike Agent Skills. | Use it. It is the cleanest example of a real open standard in this space. See §5.11. |
| **Scaffold** | YES — and it is the *older* name for what is now called an agent harness (OpenAI and METR, 2024). Anthropic treats the two as synonyms; Hugging Face distinguishes them. | Treat as a near-synonym of agent harness. Do not build an argument on the distinction. See §2. |
| **SWE-bench Verified** | ⚠️ **Deprecated by its own publisher.** OpenAI stopped reporting it on 23 Feb 2026 for benchmark contamination and recommends SWE-bench Pro. | Do not cite scores from it. If you must reference it, say it has been disowned. See §5.1. |
| **Meaningful human control** | YES — the rival term to the loop vocabulary, from the arms-control literature (Article 36, Roff & Moyes, 2016). It deliberately refuses the loop framing. | Worth knowing; useful when "human-in-the-loop" is doing reassurance work it cannot support. See §5.4. |

---

## 1. Context engineering

### Definition

The discipline of deciding what occupies a model's context window at each step of an agent's run — and the systems that make that decision dynamically at runtime.

Three definitions worth holding side by side, because they differ in emphasis:

- **Tobi Lütke (Shopify CEO), 19 Jun 2025:** "the art of providing all the context for the task to be plausibly solvable by the LLM."
- **Harrison Chase (LangChain), 23 Jun 2025:** "Building dynamic systems to provide the right information and tools in the right format such that the LLM can plausibly accomplish the task."
- **Anthropic, 29 Sep 2025:** "the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference."

Anthropic's version is the most useful for engineering purposes because it is explicitly *token-budget* framed and explicitly includes everything that lands in the window "outside of the prompts."

### Scope: what is in, what is out

Anthropic enumerates the in-scope surface as: system prompts, tools, examples (few-shot), message history, retrieved data, and MCP. Phil Schmid's widely-cited component list (30 Jun 2025) adds: long-term memory, short-term state/history, and structured output.

Anthropic names four core techniques:
- **Compaction** — summarising conversation contents near the context limit and reinitialising a new window with the summary.
- **Structured note-taking** ("agentic memory") — the agent writes notes persisted outside the context window.
- **Sub-agent architectures** — specialised sub-agents handle focused tasks with clean context windows while a main agent coordinates.
- **Just-in-time retrieval** — the agent loads data into context at runtime *via tools*, rather than pre-loading everything.

**Does RAG / retrieval sit inside or alongside?** Inside, but this is genuinely contested at the architectural level rather than the definitional one. Both LangChain and Phil Schmid list "retrieved information (RAG)" as a *component* of context engineering. Anthropic lists "retrieved data" in scope, but then argues *against* pre-indexed retrieval in favour of just-in-time tool-driven retrieval. The live disagreement in 2026 is not "is retrieval part of context engineering" (everyone says yes) but "should retrieval be embedding-based indexing or agentic grep":

- Anthropic removed vector search from Claude Code in May 2025 and replaced it with grep; Claude Code's creator Boris Cherny is quoted saying the result "outperformed everything. By a lot." `[SECONDARY]` — the quote is reported in third-party writeups; I could not reach a first-party Anthropic statement of it.
- As of mid-2026 the debate has become empirical, with published claims on both sides (token-economics arguments favouring indexed retrieval; robustness arguments favouring grep). Treat this as open.

**Code and knowledge graphs / codebase indexing**: these are *implementation strategies within* context engineering, not separate disciplines. No primary source treats them as a peer discipline.

### Who uses it

Anthropic (engineering blog and platform docs), LangChain/LangGraph, Google (Phil Schmid is a Google DeepMind engineer writing in a personal capacity), Simon Willison, Drew Breunig, Addy Osmani, Dex Horthy/HumanLayer, Redis, Sourcegraph, and an academic survey literature. Block's Goose documents its skills feature under a "context engineering" docs section.

### Origin

- **19 Jun 2025 — Tobi Lütke**, on X: "I really like the term 'context engineering' over prompt engineering. It describes the core skill better: the art of providing all the context for the task to be plausibly solvable by the LLM." This is the coinage event most sources point to. `[SECONDARY]` for the exact date — x.com is not fetchable (HTTP 402); the text is quoted verbatim and consistently by Simon Willison, Phil Schmid and LangChain, so the wording is high-confidence and the date (18 or 19 June 2025) is low-variance but not first-party verified.
- **~25 Jun 2025 — Andrej Karpathy** amplified it: "+1 for 'context engineering' over 'prompt engineering'. People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window with just the right information for the next step." `[SECONDARY]`, same reason.
- **23 Jun 2025 — Harrison Chase / LangChain**, "The rise of context engineering" — first substantial vendor treatment.
- **27 Jun 2025 — Simon Willison** endorsed the rename.
- **17 Jul 2025 — Mei et al.**, "A Survey of Context Engineering for Large Language Models" (arXiv:2507.13334) — first formal academic framing.
- **24 Jul 2025 — Drew Breunig**, "Why 'Context Engineering' Matters" — the best defence of the term against the rebrand charge.
- **29 Sep 2025 — Anthropic** formalised it in "Effective context engineering for AI agents."

**Contested attribution:** at least one source credits **Dex Horthy (HumanLayer)** with coining "context engineering." `[SECONDARY]` I found no primary artifact supporting priority over Lütke. Horthy's substantial contribution is *12-Factor Agents* (github.com/humanlayer/12-factor-agents), whose Factor 3 is "Own your context window" — clearly the same idea, and possibly earlier in substance, but not in name. Treat Lütke as the coiner and Horthy as an independent formulator.

### Is it a successor or a rebrand?

**Genuinely contested, and worth reporting as such.**

- *Successor* position (Anthropic, LangChain, Breunig, Schmid): prompt engineering is a strict subset. Anthropic states plainly that prompt engineering "refers to methods for writing and organizing LLM instructions," while context engineering manages "the entire context state." Breunig's argument: the term is "organizing the work that's already being done," and successful terminology names a genuine common experience rather than inventing one.
- *Rebrand* position: a real strand of practitioner scepticism holds that this is prompt engineering with a bigger noun. `[SECONDARY]` — I found this position widely reported but could not locate a single high-profile named practitioner arguing it forcefully in a primary artifact. That asymmetry is itself informative: the scepticism is real but diffuse; the endorsement is named and concentrated.
- *Middle position* (Simon Willison, 27 Jun 2025): the rename mattered mostly for **reputational** reasons — "prompt engineering" had been degraded in public usage to mean typing hacks into a chatbot, so the serious discipline needed a clean name. This is the most honest framing and the one I would recommend adopting.

### Vendor-marketing flag

**Low.** The term was coined by a CEO of a company that does not sell AI infrastructure, endorsed by an independent researcher, and adopted across competing vendors. It is not any one company's product naming. However: **every vendor now positions its product as "the context engineering layer,"** so vendor *content* about context engineering is heavily marketing-shaped even though the term itself is not.

### Sources
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (29 Sep 2025; accessed 2026-08-27)
- https://www.langchain.com/blog/the-rise-of-context-engineering (23 Jun 2025; accessed 2026-08-27)
- https://www.philschmid.de/context-engineering (30 Jun 2025; accessed 2026-08-27)
- https://simonwillison.net/2025/jun/27/context-engineering/ (27 Jun 2025; accessed 2026-08-27)
- https://www.dbreunig.com/2025/07/24/why-the-term-context-engineering-matters.html (24 Jul 2025; accessed 2026-08-27)
- https://arxiv.org/abs/2507.13334 (17 Jul 2025; accessed 2026-08-27)
- https://github.com/humanlayer/12-factor-agents (accessed 2026-08-27)
- https://x.com/tobi/status/1935533422589399127 (Jun 2025; **not fetchable**, quoted via Willison/Schmid)
- https://x.com/karpathy/status/1937902205765607626 (Jun 2025; **not fetchable**, quoted via Willison)

---

## 2. Harness engineering

### Verdict first

**"Harness engineering" IS a recognised term of art as of 2026.** This contradicts the expectation in the research brief. The evidence is not marginal:

- OpenAI published an engineering post **titled** "Harness engineering: leveraging Codex in an agent-first world" (11 Feb 2026).
- martinfowler.com published "Harness engineering for coding agent users" by Birgitta Böckeler of Thoughtworks (2 Apr 2026).
- Wikipedia has a standalone "Agent harness" article.
- LangChain published "The Anatomy of an Agent Harness" (Vivek Trivedy, 10 Mar 2026).
- Anthropic's engineering blog has posts titled "Effective harnesses for long-running agents" (26 Nov 2025) and "Harness design for long-running application development".
- Peer-reviewable literature exists: at minimum arXiv:2602.14690 ("Harness Engineering for Agentic AI Coding Tools: An Exploratory Study", Galster, Mohsenimofidi, Lulla, Abubakar, Treude, Baltes, 16 Feb 2026) and arXiv:2606.10106 ("What makes a harness a harness", de Macedo, Jun 2026).

- Cursor published "Continually improving our agent harness" on its own engineering blog (30 Apr 2026).
- A 2026 research wave treats **the harness as a measurable confound in benchmarks** — Harness-Bench (arXiv:2605.27922), Claw-SWE-Bench (arXiv:2606.12344), The Scaffold Effect (arXiv:2607.22585). Claw-SWE-Bench measures harness choice moving Pass@1 by **27.4 percentage points** against 29.4 for model choice. That is the strongest possible evidence that this names something real: the harness is roughly as load-bearing as the model.

That is five of the field's most credible venues — OpenAI, Anthropic, Thoughtworks/Fowler, LangChain, Cursor — plus academia, plus an encyclopedia entry, inside nine months.

**Two honest qualifications, both of which strengthen rather than weaken the finding:**

1. **The practice predates the name, under the name "scaffold."** OpenAI's Aug 2024 SWE-bench Verified post and METR's Mar 2024 elicitation guidelines both say *scaffold*, never *harness* (METR: 11 uses vs 0). "Harness engineering" renamed and sharpened an existing discipline; it did not invent one. See the Origin section below.
2. **OpenAI's post is titled "Harness engineering" but barely uses the word in its body** — essentially once, in a list. Böckeler flagged this at the time: "Maybe the term was an afterthought inspired by Mitchell Hashimoto's recent blog post." The title, not the argument, is what carried the term into circulation.

### Definition

Two definitions, one loose and one formal.

**The loose, and now canonical, one — "Agent = Model + Harness."** LangChain's Vivek Trivedy: "A harness is every piece of code, configuration, and execution logic that isn't the model itself." And, memorably: "If you're not the model, you're the harness."

**The formal one** — de Macedo (arXiv:2606.10106) gives a constitutive definition worth using verbatim in a glossary:

> "An agent harness is the runtime engineering layer that wraps one or more language models and turns them into an agent able to accomplish tasks over an external environment, by coupling to the model: (i) an agent loop that interleaves reasoning, action, and observation; (ii) a tool interface that lets the model perceive and alter the environment; (iii) context management that decides what enters and leaves the model's window; and (iv) control mechanisms, that is, limits, verification, and deterministic actions, that make the execution more trustworthy, auditable, and contained."

That paper proposes a four-part test (T1 loop, T2 tool interface, T3 active context management, T4 model-independent control) for whether something is a harness.

**Harness *engineering*** is the practice: Mitchell Hashimoto's original formulation is "anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."

OpenAI's framing (11 Feb 2026): the harness "gathers context, invokes tools, enforces sandbox and approval boundaries, streams execution progress, and carries work across multi-turn sessions" `[SECONDARY]` — openai.com/index/harness-engineering/ returns HTTP 403 to automated fetch; content is via search summarisation and InfoQ's 21 Feb 2026 report. The framing OpenAI gives for the *engineering* practice is that the team's job shifts from writing code to designing environments, specifying intent, and building feedback loops, asking on each failure: "what capability is missing, and how do we make it both legible and enforceable for the agent?"

### Components

Converged list across LangChain, Addy Osmani, and OpenAI:
- System prompts and skill files
- Tools, MCP servers, and their descriptions
- Bundled infrastructure (filesystem, sandbox, browser)
- Orchestration logic — subagent spawning, handoffs, model routing
- Hooks / middleware for deterministic execution (compaction, continuation, lint checks)
- Observability — logs, traces, metering
- Permission and approval boundaries

Böckeler adds a genuinely useful 2×2 that is worth adopting: harness elements are either **guides** (feedforward controls that steer before the agent acts) or **sensors** (feedback controls that detect after the agent acts), and each is either **computational** (deterministic, fast) or **inferential** (semantic, AI-based). Her key claim: "Separately, you get either an agent that keeps repeating the same mistakes (feedback-only) or an agent that encodes rules but never finds out whether they worked (feed-forward-only)."

### Origin — a documented trail, with an important prehistory

**Prehistory: the concept is older than the name, and its earlier name was "scaffold."**

- **10 Oct 2023** — the SWE-bench repo's very first commit contains a top-level `harness/` directory, even though the SWE-bench *paper* never uses the word. "Harness" enters the field through *evaluation* code, not agent code.
- **15 Mar 2024** — METR's *Guidelines for capability elicitation* uses **"scaffold" 11 times and "harness" 0 times.**
- **13 Aug 2024** — OpenAI's *Introducing SWE-bench Verified* keeps both senses apart and uses **scaffold** for the agent side: "we developed a new **evaluation harness** for SWE-bench… the best performing open-source **scaffold**, Agentless." The chart axis label is literally "Scaffolds."

So through 2024 the discipline existed under the name **scaffolding**. "Harness" displaced it during 2025–2026. Any claim that harness engineering is a *new practice* rather than a *renamed and sharpened* one should be resisted.

**The naming trail:**

1. **26 Nov 2025 — Anthropic**, "Effective harnesses for long-running agents" (Justin Young et al.). Earliest major-lab use of "harness" in the *agent* sense that I found — **two and a half months before Hashimoto**, and a gap in Wikipedia's account.
2. **9 Jan 2026 — Anthropic**, "Demystifying evals for AI agents" — defines *evaluation harness* and *agent harness* in adjacent sentences (quoted in §5.1). The best single citation for the distinction.
3. **5 Feb 2026 — Mitchell Hashimoto**, "My AI Adoption Journey," Step 5: "Engineer the Harness." He explicitly disclaims coining it while doing so: **"I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.'"** This is the coinage of the *discipline name*.
4. **11 Feb 2026 — OpenAI**, "Harness engineering: leveraging Codex in an agent-first world" (Ryan Lopopolo `[SECONDARY]`, via InfoQ). Six days later, and this is what converted a personal coinage into industry vocabulary.

   > ⚠️ **Honest caveat that slightly weakens the "OpenAI endorsed it" reading.** The post is *titled* "Harness engineering," but the body uses the word "harness" essentially once — in a list of agent outputs ("Evaluation harnesses"). Böckeler noticed the same thing: "Maybe the term was an afterthought inspired by Mitchell Hashimoto's recent blog post." The title, not the argument, is what carried the term.
5. **17 Feb 2026 — Birgitta Böckeler (Thoughtworks)**, "Harness Engineering – first thoughts" on martinfowler.com — the first sceptical treatment, joking about the day "somebody calls their one-prompt, LLM-based code review agent a harness."
6. **10 Mar 2026 — LangChain**, "The Anatomy of an Agent Harness" (Vivek Trivedy) — the cleanest systematic derivation.
7. **2 Apr 2026 — Böckeler**, the full martinfowler.com article, "Harness engineering for coding agent users" — the most rigorous treatment for coding-agent *users* specifically.
8. **2 Apr 2026 — Lance Martin (Anthropic)**, "Agent Harness Design": "An agent harness is the software scaffolding around a model: the loop, tools, context management, and guardrails that turn raw intelligence into a working agent." ⚠️ vendor.
9. **19 Apr 2026 — Addy Osmani**, "Agent Harness Engineering," crediting Trivedy and citing Dex Horthy/HumanLayer, Anthropic and Böckeler. "That discipline now has a name."
10. **30 Apr 2026 — Cursor**, "Continually improving our agent harness" — the term reaches a coding-agent vendor's own engineering blog. ⚠️ vendor.

Wikipedia records attribution as contested between Hashimoto and Trivedy. On the primary evidence: **Anthropic is first for the noun (Nov 2025), Hashimoto is first for the phrase "harness engineering" (5 Feb 2026), and Trivedy is first for the systematic derivation (10 Mar 2026).** Wikipedia misses the Anthropic use.

### THE CRITICAL AMBIGUITY: agent harness vs eval harness

This is the one thing a glossary must get right. See **§5.1** for the full treatment, including Anthropic's back-to-back definition of both senses and the 2026 research measuring harness-as-confound.

The short version — de Macedo (arXiv:2606.10106) documents the confusion:

> "Sometimes the term denotes the whole product (Claude Code, Codex CLI); sometimes it denotes the evaluation scaffold that runs an agent against tasks (the SWE-bench harness); sometimes it gets conflated with an agent framework, an SDK, an IDE plugin, or an orchestrator."

And gives the separator:

> **"The eval harness acts after the fact, the agent harness during the fact. One judges the race, the other is the vehicle that runs it."**

"Eval harness" is much the older usage, inheriting from ordinary software-testing vocabulary ("test harness"). Note the negative finding: **no formal standards definition of "test harness" was verifiable** — IEEE Std 610.12-1990 is paywalled and the ISTQB glossary is JS-rendered. Do not assert one.

**Recommendation:** always qualify on first use — "agent harness" or "eval harness" — then drop the qualifier within a section.

### ⚠️ Harness vs scaffold: not consistently distinguished

- **Anthropic equates them** — "agent harness (or scaffold)," parenthetically, by two different authors.
- **Hugging Face separates them** — Paniego & Roy Gosthipaty, *Harness, Scaffold, and the AI Agent Terms Worth Getting Right*, 25 May 2026: harness = "the execution layer inside the agent: it calls the model, handles its tool calls, decides when to stop"; scaffolding = "the behavior-defining layer around the model: system prompt, tool descriptions, how the model's responses get parsed, what it remembers across steps."

That post exists *because* of the disagreement, quoting its own author after ICLR 2026: "I have heard a lot of explanations while I was at ICLR, but I could not understand why they did not converge to a single explanation." It states plainly there are "no widely accepted definitions yet."

**Recommendation:** treat *scaffold* as a near-synonym with a slightly narrower, prompt-and-parsing-flavoured connotation, and do not build any argument on the distinction.

### Relationship to context engineering

Two positions, both from credible sources, and they agree:

- **Martin Fowler** (LinkedIn, Feb 2026, `[SECONDARY]` via InfoQ): "Harness Engineering is a valuable framing of a key part of AI-enabled software development. Harness includes context engineering, architectural constraints, and garbage collection."
- **Software Improvement Group** (24 Apr 2026): "Context engineering manages what the model sees at any given moment — retrieval, compression, and context window management. It is one component of the harness."

So: **context engineering ⊂ harness engineering.** Harness engineering additionally covers enforcement hooks, verification gates, sandboxes, permissions, and monitoring. This is a clean nesting and I'd recommend the project adopt it.

### Contested-ness

- **Attribution** is contested (Hashimoto vs Trivedy vs "it was already in use").
- **Scope** is contested: whether "harness" means the whole product, the runtime layer, or the user-configurable surface. Böckeler deliberately narrows it to the coding-agent-user's configurable surface; Trivedy and de Macedo use the broad runtime-layer sense.
- **Novelty** is contestable: the Galster et al. exploratory study (Feb 2026) uses "harness engineering" in its title but, per its abstract, does not formally define it — it uses the phrase descriptively for "configuring these tools through versioned repository-level artifacts." Early academic uptake is therefore looser than the industry definitions.

### Vendor-marketing flag

**Low-to-moderate.** The term was coined by an independent engineer with no product to sell, then adopted by direct competitors (OpenAI, Anthropic, LangChain) *and* by vendor-neutral consultancies (Thoughtworks, SIG). That pattern is the opposite of vendor capture. Caveat: OpenAI also ships a product component it calls Harness, and open-sourced a "Codex harness" in Aug 2026, so OpenAI's usage carries product freight the others' does not.

### Sources
- https://mitchellh.com/writing/my-ai-adoption-journey (5 Feb 2026; accessed 2026-08-27)
- https://openai.com/index/harness-engineering/ (11 Feb 2026; **403 to automated fetch**, accessed via search + InfoQ 2026-08-27)
- https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/ (21 Feb 2026; accessed 2026-08-27)
- https://www.langchain.com/blog/the-anatomy-of-an-agent-harness (10 Mar 2026; accessed 2026-08-27)
- https://martinfowler.com/articles/harness-engineering.html (2 Apr 2026; accessed 2026-08-27)
- https://addyosmani.com/blog/agent-harness-engineering/ (19 Apr 2026; accessed 2026-08-27)
- https://en.wikipedia.org/wiki/Agent_harness (accessed 2026-08-27)
- https://arxiv.org/html/2606.10106v1 (Jun 2026; accessed 2026-08-27)
- https://arxiv.org/abs/2602.14690 (16 Feb 2026; accessed 2026-08-27)
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (26 Nov 2025; accessed 2026-08-27)
- https://www.softwareimprovementgroup.com/blog/what-is-harness-engineering/ (24 Apr 2026; accessed 2026-08-27)

---

## 3. Skills (Agent Skills / SKILL.md)

### Definition

Anthropic's own (16 Oct 2025): Agent Skills are "organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks."

The specification's own framing (agentskills.io): "a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. At its core, a skill is a folder containing a `SKILL.md` file."

### The actual specification

This is a real, published, terse spec. Directory:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
```

`SKILL.md` = YAML frontmatter + Markdown body. Frontmatter fields:

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | 1–64 chars; lowercase `a-z`, `0-9`, hyphens only; no leading/trailing hyphen; no consecutive hyphens; **must match the parent directory name** |
| `description` | Yes | 1–1024 chars, non-empty. Should say what the skill does *and when to use it* |
| `license` | No | License name or reference to a bundled license file |
| `compatibility` | No | ≤500 chars; environment requirements (product, packages, network) |
| `metadata` | No | Arbitrary string→string map for client-specific properties |
| `allowed-tools` | No | Space-separated pre-approved tools. **Experimental**; support varies by implementation |

**Progressive disclosure** — the spec's central mechanism, in three stages:
1. **Discovery** (~100 tokens): `name` + `description` only, loaded at startup for every available skill.
2. **Activation** (<5000 tokens recommended): the full `SKILL.md` body loads when the task matches.
3. **Execution** (as needed): files in `scripts/`, `references/`, `assets/` load only when required.

Spec guidance: keep `SKILL.md` under 500 lines; keep file references one level deep. A reference validator exists (`skills-ref validate ./my-skill`) at github.com/agentskills/agentskills.

### Open standard or vendor-specific?

**Open standard — genuinely, with a caveat.** Originally developed by Anthropic (announced 16 Oct 2025), **released as an open standard on 18 Dec 2025**, now hosted at **agentskills.io** with development on GitHub (github.com/agentskills/agentskills) and a public Discord.

Adoption as of the site's own client showcase (accessed 2026-08-27) includes: Claude / Claude Code, **ChatGPT & Codex (OpenAI)**, **GitHub Copilot**, **VS Code (Microsoft)**, **Cursor**, **Gemini CLI (Google)**, **JetBrains Junie**, **Block Goose**, OpenCode, OpenHands, Amp, Letta, Roo Code, Kiro (AWS), Factory, Tabnine, Qodo, Databricks Genie Code, Snowflake Cortex Code, Mistral AI Vibe, Spring AI, Laravel Boost, Pulumi Neo, Ona, Firebender, Trae (ByteDance), and ~20 more. That is every major competitor.

**The caveat, and it is a real one — Simon Willison (19 Dec 2025):** the spec is "deliciously tiny" but "quite heavily under-specified." He questions whether calling it an open standard is meaningful at this level of specification, and speculated it may end up under the **Agentic AI Foundation (AAIF)**, as MCP did.

**I checked, and it has not.** Several secondary sources assert that agentskills.io "is stewarded by the Agentic AI Foundation." **This appears to be wrong.** Neither agentskills.io nor the github.com/agentskills/agentskills repository mentions AAIF, the Linux Foundation, or any formal governance document. The repo states only that "the Agent Skills format was originally developed by Anthropic, released as an open standard, and has been adopted by a growing number of agent products," and that "the standard is open to contributions from the broader ecosystem." Licensing is Apache-2.0 for code and CC-BY-4.0 for docs. Governance is therefore **de facto Anthropic maintainership with open contribution** — materially weaker than MCP's or AGENTS.md's foundation governance. Treat any claim of AAIF stewardship of Agent Skills as unverified.

**Verdict:** call it "an open specification with broad multi-vendor adoption but no neutral governance body." Do not call it "an industry standard" without that qualification, and do not repeat the AAIF-stewardship claim.

### Competing senses of "skill" — four, and they will cause confusion

1. **Amazon Alexa Skills** (2015–) — third-party voice applications for Alexa. Enormous consumer-facing name recognition; entirely unrelated. This is the sense most non-specialist readers will reach for first.
2. **Microsoft Semantic Kernel "skills"** (2023) — collections of native functions and prompt templates an LLM could invoke. **Renamed to "plugins"** in 2023 (GitHub issue microsoft/semantic-kernel#2119, opened 21 Jul 2023) to align with the OpenAI plugin spec. So this sense is retired — but it is retired *in a direction that collides differently*, since "plugin" now also means an MCP-adjacent thing.
3. **Reinforcement learning / robotics "skills"** — reusable low-level policies or options (in the options-framework sense) that a hierarchical agent composes. Decades of literature. `[SECONDARY]` — I did not source this directly in this pass; treat the RL sense as well-established background rather than a sourced claim.
4. **Agent Skills (2025–)** — the SKILL.md sense above.

A fifth, softer collision: colloquial "skill" meaning "a thing the model can do", which is how most prose uses the word.

**Recommendation:** in project documents, always write **"Agent Skills"** or **"a Skill (SKILL.md)"** on first use in any section, and never use bare lowercase "skill" to mean the packaged-instruction artifact.

### Vendor-marketing flag

**Moderate, decreasing.** It began as Anthropic product naming (Claude Skills, Oct 2025) and was still vendor-specific for two months. The 18 Dec 2025 open-standard release plus cross-vendor adoption converted it into shared vocabulary. But be aware: much writing about "Skills" is still Anthropic-ecosystem content marketing, and the phrase "Skills are the new REST/npm/MCP" is a recurring content-farm trope with no substance behind it.

### Sources
- https://agentskills.io/ (accessed 2026-08-27)
- https://agentskills.io/specification (accessed 2026-08-27)
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (16 Oct 2025, updated 18 Dec 2025; accessed 2026-08-27)
- https://code.claude.com/docs/en/skills (accessed 2026-08-27)
- https://simonwillison.net/2025/Dec/19/agent-skills/ (19 Dec 2025; accessed 2026-08-27)
- https://github.com/agentskills/agentskills (accessed 2026-08-27) — checked specifically for governance language; none found
- https://github.com/microsoft/semantic-kernel/issues/2119 (21 Jul 2023; accessed 2026-08-27)
- https://devblogs.microsoft.com/agent-framework/skills-to-plugins-fully-embracing-the-openai-plugin-spec-in-semantic-kernel/ (accessed 2026-08-27)

---

## 4. Agent orchestration — and the "graph engineering" verdict

### Verdict on "graph engineering"

**"Graph engineering" is NOT a term of art in this field. Do not use it.**

The evidence for that negative finding:

1. **No primary source uses it.** Not Anthropic, not OpenAI, not LangChain, not Google, not Microsoft, not any framework's documentation, not any paper I could locate, not any standards body.
2. **LangGraph — the one framework the phrase would most obviously describe — does not use it.** LangGraph's own overview describes itself as "a low-level orchestration framework and runtime for building, managing, and deploying long-running, stateful agents." Its vocabulary is *orchestration, graphs, nodes, edges, workflows, durable execution* — never "graph engineering."
3. **OpenAI's Agents SDK avoids graph language entirely.** Its primitives are Agents, Handoffs, Guardrails, Sessions, Tracing; its framing word is "workflow." No graph, no DAG, no node vocabulary at all.
4. **All actual usage traces to a 2026 SEO/content-marketing cluster.** The phrase appears in Analytics Vidhya (28 Jul 2026, Harsh Mishra — a tutorial explainer that presents the term as established but cites *no one* who previously used it), plus Medium posts, plus vendor blogs (TrueFoundry, Eigent, explainX, Flowtivity, AI Builder Club) and newsletters. These sources cite each other, not primary literature. This is the signature of a term manufactured by content marketing rather than practice.
5. **It collides with an established, unrelated discipline.** "Knowledge graph engineering" — building graph-structured data with RDF/OWL for retrieval and reasoning — has been a named field since roughly 2012 and draws on decades of semantic-web work. A reader encountering "graph engineering" in an AI context will very reasonably assume you mean knowledge graphs.

Note the instructive contrast with harness engineering: that term went from one blog post to OpenAI, Anthropic, Thoughtworks, LangChain, Wikipedia and arXiv in seven months. "Graph engineering" has had comparable calendar time and has reached *none* of them. That is the difference between a term the field adopted and a term the SEO layer is trying to sell.

### What to use instead

**Primary term: "agent orchestration."** This is the established name.

- **LangGraph/LangChain**: "a low-level orchestration framework and runtime." Gartner has a market category, "Multiagent Orchestration Platforms."
- **OpenAI Agents SDK** defines orchestration functionally as coordinating multiple agents, and asks builders to "decide between handoffs and manager-style orchestration."
- **Anthropic** uses "orchestrator-workers" as a named pattern.

**Sub-terms worth using, all primary-sourced:**

From **Anthropic, "Building effective agents" (19 Dec 2024, Erik Schluntz and Barry Zhang)** — still the single best primary vocabulary source for this area. Its foundational distinction:

> "*Workflows* are systems where LLMs and tools are orchestrated through predefined code paths. *Agents*, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks."

That workflow/agent split is the concept "graph engineering" was groping at, and it already has a name. The five named patterns:

1. **Prompt chaining**
2. **Routing**
3. **Parallelization**
4. **Orchestrator-workers**
5. **Evaluator-optimizer**

From **Anthropic, "How we built our multi-agent research system" (13 Jun 2025, Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford)**:
- **Orchestrator-worker pattern** — "a lead agent coordinates the process while delegating to specialized subagents that operate in parallel."
- **Lead agent** — analyses the query, develops a strategy, spawns subagents.
- **Subagent** — operates with a separate context window; acts as an intelligent filter.
- **Fan-out / parallelisation** — the lead agent "spins up 3-5 subagents in parallel."
- Their definition: "A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together."

From **OpenAI Agents SDK**: **handoffs** (agents delegating to other agents), **agents-as-tools**, **manager-style orchestration**, **sessions**, **tracing**.

**Secondary term worth knowing: "flow engineering."** This is real and predates all of the above. Coined in **Ridnik, Kredo & Friedman, "Code Generation with AlphaCodium: From Prompt Engineering to Flow Engineering" (arXiv:2401.08500, Jan 2024, CodiumAI/now Qodo)**. It names precisely the practice of designing an explicit multi-stage flow that the model fills in locally, rather than relying on one prompt. If the project needs a word for "the developer designs the control structure; the agent makes local decisions inside it," **flow engineering is the correct, cited, primary-sourced term** — and it is a far better fit for what "graph engineering" was reaching for.

Caveat: "flow engineering" carries some vendor freight (it is Qodo's paper, and Qodo ships "Qodo Flow"), and its adoption is narrower than "orchestration."

### Where "graph" *is* legitimate vocabulary

Don't over-correct. "Graph" is entirely correct as a **noun describing a structure**: LangGraph's `StateGraph`, nodes, edges, DAGs, state machines. It is the *"-engineering" compound* that is fabricated. "We model the pipeline as a graph" is fine. "We practise graph engineering" is not.

### Vendor-marketing flag

**"Graph engineering": HIGH — this is the clearest case of manufactured vocabulary in this whole document.** "Agent orchestration": low, though "orchestration platform" is a heavily-sold product category. "Flow engineering": moderate (single-vendor origin).

### Sources
- https://www.anthropic.com/engineering/building-effective-agents (19 Dec 2024; accessed 2026-08-27)
- https://www.anthropic.com/engineering/multi-agent-research-system (13 Jun 2025; accessed 2026-08-27)
- https://docs.langchain.com/oss/python/langgraph/overview (accessed 2026-08-27)
- https://openai.github.io/openai-agents-python/ (accessed 2026-08-27)
- https://arxiv.org/abs/2401.08500 (Jan 2024; accessed 2026-08-27)
- https://github.com/Codium-ai/AlphaCodium (accessed 2026-08-27)
- https://www.analyticsvidhya.com/blog/2026/07/graph-engineering/ (28 Jul 2026; accessed 2026-08-27) — cited as *evidence of the term's provenance*, not as a source for its validity
- https://www.gartner.com/reviews/market/multiagent-orchestration-platforms (accessed 2026-08-27)

---

## 5. Further core terms

### 5.1 Evals / evaluations — and the eval-harness collision

**Definition.** Anthropic's is the cleanest primary source: an eval is "a test for an AI system: give an AI an input, then apply grading logic to its output to measure success." (*Demystifying evals for AI agents*, Mikaela Grace, Jeremy Hadfield, Rodrigo Olivares, Jiri De Jonghe, 9 Jan 2026.) LangSmith: "Evaluations (evals) are a way to breakdown what 'good' looks like and measure it."

**The three-part anatomy is consistent across vendors:** *dataset + task/system-under-test + grader*. Braintrust: "Every evaluation has three parts: **Data** … **Task** … **Scorers and classifiers**." The UK AI Security Institute's **Inspect** framework uses **Dataset / Solver / Scorer** — and notably does not use the word "harness" at all.

**Offline vs online** is the standard axis (offline = fixed dataset, pre-deployment, in CI; online = production traffic, no ground truth). Note this vocabulary is **borrowed, not new** — "offline evaluation" is long-standing recommender-systems and contextual-bandit terminology (Li, Chu, Langford & Wang, WSDM 2011).

#### Eval vs benchmark — the distinction is real in practice but has NO authoritative source

> **Honest negative finding, and a correction to a common assumption.** None of the major primary sources actually draws this distinction.
> - `openai/evals` **conflates them in its own one-line description**: "Evals is a framework for evaluating LLMs and LLM systems, and an open-source registry of benchmarks."
> - Anthropic's Jan 2026 evals piece does not distinguish them — it treats SWE-bench Verified, Terminal-Bench and τ²-Bench as evals.
> - **Hamel Husain's *Your AI Product Needs Evals* (29 Mar 2024) does not use the word "benchmark" at all.** Do not credit him with the distinction. His later FAQ only notes in passing that he covers "product-specific LLM evals (not foundation model benchmarks)."

The sharpest articulation found is from an **independent practitioner site, not a lab** — Brenn Hill, *Evals vs. tests vs. benchmarks*, evaldrivendevelopment.dev, updated June 2026: a **benchmark** is "a standardized dataset plus metric plus protocol, built for cross-*model* comparison"; an **eval** is "*your* application-specific check"; a **test** is "a deterministic assertion." Treat this as the best-stated version of a widely-held informal distinction, **not** as canonical.

#### Origin of "evals" as a noun

| Date | Artifact | Significance |
|---|---|---|
| **28 Aug 2020** | `EleutherAI/lm-evaluation-harness` repo created | "a unified framework to test generative language models on a large number of different evaluation tasks"; backend for HuggingFace's Open LLM Leaderboard. **The canonical "eval harness."** |
| **23 Jan 2023** | `openai/evals` repo created (private) | |
| **14 Mar 2023** | `openai/evals` goes public alongside GPT-4 | **The moment "evals" became industry vocabulary.** |
| **9 Jun 2023** | Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, arXiv:2306.05685 | Popularises **LLM-as-a-judge**; documents position, verbosity and self-enhancement bias |
| **29 Mar 2024** | Hamel Husain, *Your AI Product Needs Evals* | Made evals a product-engineering discipline. Three levels: **L1 unit tests → L2 human & model eval → L3 A/B testing.** "Rigorous and systematic evaluation is the most important part of the whole system." Amplified by Simon Willison two days later |
| **May 2024** | UK AISI **Inspect** released (with Meridian Labs) | |
| **29 Oct 2024** | Husain, *Creating a LLM-as-a-Judge That Drives Business Results* | Introduces **"critique shadowing"**; names four failure modes (too many metrics, arbitrary scoring, ignoring domain experts, unvalidated metrics) |

Tooling vendors, all launched 2023 `[SECONDARY]` on dates: **Braintrust** (Ankur Goyal), **LangSmith** (LangChain), **W&B Weave**.

#### ⭐ THE CRITICAL FINDING: "harness" has two incompatible senses, and the collision is documented

**The pre-existing root.** "Harness" is borrowed from software testing — a **test harness** is the stubs, drivers and infrastructure that run tests in a controlled, observable way. `[SECONDARY]`. **Negative finding:** IEEE Std 610.12-1990 is paywalled and the ISTQB glossary is JS-rendered; **no formal standards definition of "test harness" was verified.** Do not assert one.

**Sense A — evaluation harness = the grading/execution infrastructure.**

SWE-bench is the key case, and the history is precise and slightly surprising:

- **The SWE-bench paper never uses the word "harness."** (Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan, arXiv:2310.06770, 10 Oct 2023.)
- **But the code did, from the very first commit.** The repo's first commit `e5878aa`, dated 10 Oct 2023 and messaged `"init"`, contains a top-level **`harness/`** directory. It moved to `swebench/harness/` on 28 Mar 2024 during PyPI packaging.
- The docs now define it: "the Docker-based evaluation harness for SWE-bench," which "uses Docker containers to create reproducible environments for evaluating model-generated patches."

**Sense B — agent harness = the scaffolding that turns a model into an agent.** See §2.

#### ⭐ "Scaffold" was the 2024 word for what is now called "agent harness"

This is the most important correction to the harness narrative, and it matters because it shows the *concept* is older than the *name*.

**OpenAI, *Introducing SWE-bench Verified*, 13 August 2024** keeps the two senses cleanly apart and uses **scaffold**, not harness, for the agent side:

> "We also collaborated with the SWE-bench authors to develop a new **evaluation harness** for SWE-bench which uses containerized Docker environments… On SWE-bench Verified, GPT-4o resolves 33.2% of samples, with the best performing open-source **scaffold**, Agentless, doubling its previous score of 16%."

The chart axis label on that page is literally "Scaffolds."

**Corroborating hard data:** METR's *Guidelines for capability elicitation* (15 Mar 2024) uses **"scaffold" 11 times and "harness" 0 times.**

So the sequence is: the *practice* existed and was called **scaffolding** through 2024; **harness** displaced it during 2025–2026.

#### ⭐ The collision, stated in a primary source

**Anthropic defines both senses back to back — this is the single best citation for a glossary:**

> "An **evaluation harness** is the infrastructure that runs evals end-to-end. It provides instructions and tools, runs tasks concurrently, records all the steps, grades outputs, and aggregates results. An **agent harness** (or scaffold) is the system that enables a model to act as an agent: it processes inputs, orchestrates tool calls, and returns results. When we evaluate 'an agent,' we're evaluating the harness *and* the model working together. For example, Claude Code is a flexible agent harness…"
> — Anthropic, 9 Jan 2026

De Macedo's paper (arXiv:2606.10106) gives the memorable separator:

> **"The eval harness acts after the fact, the agent harness during the fact. One judges the race, the other is the vehicle that runs it."**

**And both senses appear in the same benchmark paper.** Terminal-Bench (Merrill, Shaw, Carlini, Li et al., arXiv:2601.11868, 17 Jan 2026; Stanford × Laude Institute) uses "harness" seven times across *both* senses — "We publish the dataset and **evaluation harness**" alongside "Performance of each model with its best **agent harness**."

#### ⭐ Harness-as-confound: the 2026 research wave

This is the strongest evidence that harness engineering is a real discipline and not a naming fashion — the harness is *measurably* a large fraction of any benchmark result.

- **Claw-SWE-Bench** (Zheng, Han, Li, Xu, Tian et al., arXiv:2606.12344, 10 Jun 2026): leading SWE-bench-style reports package prompt template, agent loop, tool interface, timeout, patch extraction and stopping logic into one system, so "the resulting resolved rate therefore **conflates three causally distinct factors: the evaluated LLM, the harness that turns the LLM into an agent, and the task instances being solved**." Measured: **model choice changes Pass@1 by 29.4 points; harness choice by 27.4 points under fixed models.** Adapter design alone moved one backbone from 19.1% to 73.4%.
- **Harness-Bench** (Yao, Tan, Liu et al., arXiv:2605.27922, 27 May 2026): across 5,194 trajectories — "agent capability should be reported at the model-harness configuration level rather than attributed to the base model alone."
- **The Scaffold Effect** (Vats & Golev, Sentient Labs, arXiv:2607.22585, 8 Jun 2026): "Harness choice induces up to a **40× difference in tokens per solved task**" while "paired within-model pass-rate differences remain 0–8 percentage points."

**Practical consequence:** a headline like "model X resolves N% of SWE-bench" is a *joint* measurement of model and harness. Any document citing agent benchmark scores without naming the harness is making a claim it cannot support.

#### ⚠️ Contested: harness vs scaffold are NOT consistently distinguished

- **Anthropic equates them** — "agent harness (or scaffold)", parenthetically, by two different authors.
- **Hugging Face separates them** — Sergio Paniego & Aritra Roy Gosthipaty, *Harness, Scaffold, and the AI Agent Terms Worth Getting Right*, 25 May 2026: "**Harness:** the execution layer inside the agent: it calls the model, handles its tool calls, decides when to stop." / "**Scaffolding:** the behavior-defining layer around the model: system prompt, tool descriptions, how the model's responses get parsed, what it remembers across steps."

That post is itself evidence of the contestedness, quoting its own author after ICLR 2026: "I have heard a lot of explanations while I was at ICLR, but I could not understand why they did not converge to a single explanation." It states there are "no widely accepted definitions yet, and different frameworks use the same word differently."

**Recommendation:** treat *scaffold* as a near-synonym of *agent harness* with a slightly narrower, more prompt-and-parsing-flavoured connotation, and do not rely on the distinction.

#### Benchmarks — and a major 2026 development

| Benchmark | Origin | Status |
|---|---|---|
| **SWE-bench** | arXiv:2310.06770, 10 Oct 2023, Princeton/Chicago. 2,294 GitHub issues. Claude 2 solved 1.96% | Superseded |
| **SWE-bench Verified** | OpenAI, 13 Aug 2024. 93 developers screened 1,699 samples → 500 validated instances | ⚠️ **Deprecated by its own creator** |
| **SWE-bench Pro** | Scale AI, arXiv:2509.16941. GPL-licensed public set + private enterprise set as contamination deterrents. Top models ~23% vs 70%+ on Verified | Currently recommended by OpenAI |
| **Terminal-Bench** | Stanford × Laude, launched 19 May 2025; paper arXiv:2601.11868; run via **Harbor** | Active |

> ⭐ **OpenAI retired SWE-bench Verified.** *Why SWE-bench Verified no longer measures frontier coding capabilities*, 23 February 2026: "improvements on SWE-bench Verified no longer reflect meaningful improvements in models' real-world software development abilities. Instead, they increasingly reflect how much the model was exposed to the benchmark at training time. This is why we have stopped reporting SWE-bench Verified scores, and we recommend that other model developers do so too." **Any document citing a SWE-bench Verified score in 2026 is citing a number its own publisher has disowned.**

**Independent validity critiques:**
- **UTBoost** (Yu, Zhu, He, Kang), ACL 2025, arXiv:2506.09289 — found **345 patches incorrectly labelled as passing**, affecting **24.4% of SWE-bench Verified leaderboard entries** and causing 11 ranking changes.
- **LLM-as-judge:** *Reliability without Validity* (Norman, Rivera, Hughes), arXiv:2606.19544, 17 Jun 2026 — exact-match agreement "systematically overstates discriminative ability," inflating scores **33–41 percentage points** versus Cohen's kappa; two production judges showed test–retest reliability >0.95 *and* severe position bias. Reliability is not validity.

**Standards note:** NIST's **ARIA** programme (launched May 2024) is the closest thing to an institutional framing, using TEVV and three levels (model testing, red-teaming, field testing). `[SECONDARY]` — the ARIA evaluation plan PDF would not text-extract.

**Contested-ness:** low for "eval" itself; **high** for benchmark validity and LLM-as-judge validity, both with strong 2025–2026 published critiques.

**Vendor-marketing flag:** low for the word; **high for the surrounding tooling category** (Braintrust, LangSmith, W&B Weave, Humanloop). Prefer describing the practice over naming a platform.

---

### 5.2 Guardrails

**Verdict up front: this is substantially vendor product naming, not a term of art.** The evidence is stronger than expected, and it is mostly *negative* evidence from the companies best placed to use the word.

#### There is no agreed definition — the word covers four things with different failure models

| Category | What it is | Failure model | Canonical artifacts |
|---|---|---|---|
| Structured-output validation | Deterministic schema/type checking | Bugs — **non-adversarial** | Guardrails AI RAIL spec (2023) |
| Content moderation | Classifier against a harm taxonomy | **Probabilistic**, tunable ROC | Llama Guard 1–4; Azure Content Safety; Bedrock filters |
| Prompt-injection / jailbreak defence | Security against an intelligent attacker | **99% is a failing grade** | Prompt Shields; `openai-guardrails`; NeMo input rails |
| Policy / dialog / tool enforcement | Business rules on topics, flows, actions | Rule gaps | NeMo dialog+execution rails; Agents SDK tool guardrails |

The nearest neutral academic definition — Dong, Mu, Jin, Qi, Hu, Zhao, Meng, Ruan & Huang, *Building Guardrails for Large Language Models*, arXiv:2402.01822v2 (updated 29 May 2024): "an algorithm that takes as input a set of objects (e.g., the input and/or the output of LLMs) and determines if and how some enforcement actions can be taken to reduce the risks." Note this definition **excludes structured-output validation** — which is exactly what the library literally named "Guardrails" originally did.

#### Primary sources

**OpenAI Agents SDK** (`openai-agents` 0.0.1, 4 Mar 2025): "Guardrails enable you to do checks and validations of user input and agent output." Two kinds: **input guardrails** (run on initial user input) and **output guardrails** (run on final agent output). A third kind, **tool guardrails**, wraps `FunctionTool` invocations.

> ⭐ Two details worth putting in a glossary. **(i) The motivating example in OpenAI's own docs is cost, not safety** — "imagine you have an agent that uses a very smart (and hence slow/expensive) model… you can run a guardrail with a fast/cheap model… saving time and money." **(ii) Tripwires are control flow, and the default races the action.** "If true, an `InputGuardrailTripwireTriggered` exception is raised." But with `run_in_parallel=True` (the default), "the agent may have already consumed tokens and executed tools before being cancelled." **The default input guardrail does not prevent the action; it cancels alongside it.**

⚠️ **OpenAI ships a second, incompatible "Guardrails."** The standalone `openai-guardrails` package (first release 6 Oct 2025) is "a safety framework for LLM applications that automatically validates inputs and outputs using configurable checks" — moderation, jailbreak, PII, hallucination, off-topic. Same vendor, same word, different thing.

**NVIDIA NeMo Guardrails** — `nemoguardrails` 0.1.0 on PyPI **25 Apr 2023**; **first vendor product named "Guardrails."** ⚠️ Launch-blog definition is marketing: "a set of programmable constraints or rules that sit in between a user and an LLM." ⚠️ **NVIDIA's own two taxonomies do not match**: the launch blog says *topical / safety / security* (purposes); the docs say *input / dialog / retrieval / execution / output rails* (interception points). **Colang** is its dialogue-flow modelling language, itself in two incompatible versions.

**Guardrails AI** (Shreya Rajpal) — repo created **29 Jan 2023**, the *earliest* of the three, predating NeMo by ~3 months. **Its original meaning was structured-output validation, not safety.** From the v0.1.0 README: "Guardrails is an open-source Python package for specifying structure and type, validating and correcting the outputs of large language models," using `rail` (**R**eliable **AI** markup **L**anguage) files. Guardrails Hub launched 15 Feb 2024 with 50+ **validators**. The current README has migrated to risk framing **without renaming anything** — the word silently changed meaning under the same project.

#### ⭐ The companies best placed to use the word avoid it

- **Meta deliberately does not.** *Llama Guard: LLM-based Input-Output **Safeguard** for Human-AI Conversations* (Inan, Upasani, Chi, Rungta et al., arXiv:2312.06674, 7 Dec 2023) **does not contain the word "guardrail" once.** Meta says *safeguard* and *classifier*. This holds through Llama Guard 4 12B: "a natively multimodal **safety classifier**." The artifact most often cited as "a guardrail model" is one whose authors pointedly avoided the term.
- **Microsoft does not** in technical service docs. Azure AI Content Safety's overview has **zero occurrences of "guardrail"**; its vocabulary is *content safety*, *Prompt Shields*, *groundedness detection*.
- **Anthropic** uses it only as informal prose and a docs URL slug. Its product and research vocabulary is **safeguards** and **classifiers** (Constitutional Classifiers, arXiv:2501.18837). There is no "Anthropic Guardrails" product.
- **AWS is simultaneously the strongest endorser and the strongest disavower.** Bedrock Guardrails says "configurable **safeguards**… the following safeguards (**also known as filters**)." Meanwhile AWS Control Tower — which popularised "guardrails" in cloud governance at GA on 24 Jun 2019 — has **renamed them**:

> "We are transitioning our terminology to align better with industry usage and with other AWS services. During this time, you may see the previous term, *guardrail*, as well as the new term, *control*… These terms are synonymous for our purposes."

#### Origin — no coiner; the metaphor is borrowed

| Date | Artifact | Sense |
|---|---|---|
| **24 Jun 2019** | AWS Control Tower GA | Pre-LLM cloud-governance sense. The cleanest datable anchor |
| ~2016–18 | Netflix "paved road with guardrails" `[SECONDARY]` | Platform-engineering idiom. **Could not date a first use — treat as folk history** |
| **29 Jan 2023** | `guardrails-ai/guardrails` created | First LLM library named Guardrails — meaning **schema validation** |
| **14 Mar 2023** | OpenAI GPT-4 announcement: "refusing to go outside of guardrails" `[SECONDARY]` | Informal prose |
| **25 Apr 2023** | NeMo Guardrails | First vendor **product** named Guardrails |
| **4 Mar 2025** | OpenAI Agents SDK 0.0.1 | First **API primitive** named guardrail |

#### Contested-ness and critique

Named critical commentary — **Simon Willison** (who coined "prompt injection"):
> "In application security, 99% is a failing grade. If there's a way to get past the guardrails, no matter how obscure, a motivated adversarial attacker is going to figure that out." (22 Oct 2025)
> "the very best frontier models, unencumbered by additional guardrails, will find an exploit if there is one to be found." (28 Jul 2026)

**OWASP** LLM Prompt Injection Prevention Cheat Sheet: "A guardrail LLM is itself an LLM and is itself susceptible to prompt injection. Treat it as one layer in a defense-in-depth design, not as a replacement for input validation, structured prompts, least-privilege tool scopes, or human approval on destructive actions."

> **Honest negative finding:** despite targeted searching, **no named researcher has published a direct critique of the *word* "guardrails" as marketing.** All published criticism is about *efficacy*, not terminology. The terminological evidence is indirect but strong — AWS's rename notice, Meta's and Microsoft's avoidance, and OpenAI's two incompatible uses.

**Relationship to harness engineering:** guardrails are one implementation of the harness's control mechanisms (condition T4 in §2). In Böckeler's taxonomy they are mostly **sensors** (feedback), while permission rules and hooks are **guides** (feedforward).

**Vendor-marketing flag: HIGH.** Name the actual mechanism — validation, allowlist, sandbox, classifier, tripwire, permission rule, hook — and use "guardrails" only as an umbrella, if at all.

---

### 5.3 Autonomy levels

#### ⭐ Verdict: NO standard exists. Not ISO/IEC, not IEEE, not NIST, not SAE, not the EU AI Act, not any lab or vendor.

The strongest proof is not absent search results. It is that **the two leading proposals assign the same words to different levels with the human on opposite sides**, and that **the two labs publishing most about agent autonomy both explicitly declined a discrete scale.**

#### The distinction people get wrong

**Autonomy** = how independently the system is *permitted* to act (a deployment and interaction-design property). **Capability** = how good the model is. Morris et al. state this explicitly: "AGI is not necessarily synonymous with autonomy. We introduced Levels of Autonomy that are unlocked, but not determined by, progression through the Levels of AGI."

> ⚠️ **ISO rejects the word outright for AI systems.** ISO/IEC 22989:2022 defines **autonomy** as the "characteristic of a system that is capable of modifying its intended domain of use or goal without external intervention, control or oversight," and **heteronomy** as "operating under the constraint of external intervention, control or oversight." Note 2 to 3.1.4: "AI systems are designed to operate with varying levels of **automation**." **By that definition no shipping coding agent is "autonomous"** — they are *heteronomous* and *automated*. There is no clause titled "levels of autonomy" anywhere in 22989.

#### The analogy: SAE J3016 is a real standard — for cars

*Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles.* First issued J3016_201401 on **16 Jan 2014**; current **J3016_202104 (30 Apr 2021)**. Levels: 0 No Driving Automation · 1 Driver Assistance · 2 Partial · 3 Conditional · 4 High · 5 Full.

⭐ **The structural point borrowers miss:** J3016's cut is *not* "how much AI." It is a crisp functional test — *who performs the dynamic driving task and the DDT fallback* — with the decisive break at L2/L3. **No coding-agent scale has an equivalent testable predicate.** That is precisely why none of them converge.

#### ⭐ Origin: Google DeepMind's "Levels of Autonomy" table

Morris, Sohl-Dickstein, Fiedel, Warkentin, Dafoe, Faust, Farabet & **Legg**, *Levels of AGI for Operationalizing Progress on the Path to AGI*, **arXiv:2311.02462, 4 Nov 2023** (ICML 2024). This is the origin artifact for "Levels of Autonomy" as an AI term of art, and it is explicitly SAE-modelled: "Much as the adoption of a standard set of Levels of Driving Automation allowed for clear discussions of policy and progress relating to autonomous vehicles, we posit there is value in defining 'Levels of AGI.'"

**Table 2, verbatim:**

| Level | Name | Description |
|---|---|---|
| 0 | **No AI** | "human does everything" |
| 1 | **AI as a Tool** | "human fully controls task and uses AI to automate mundane sub-tasks" |
| 2 | **AI as a Consultant** | "AI takes on a substantive role, but only when invoked by a human" |
| 3 | **AI as a Collaborator** | "co-equal human-AI collaboration; interactive coordination of goals & tasks" |
| 4 | **AI as an Expert** | "AI drives interaction; human provides guidance & feedback or performs subtasks" |
| 5 | **AI as an Agent** | "fully autonomous AI" |

Caption: "The choice of appropriate autonomy level need not be the maximum achievable given the capabilities of the underlying model." Their example system "Accelerating computer programming with a code-generating model" sits at the **L2/L3 boundary**; L5 is annotated "(not yet unlocked)."

**True ancestor:** Sheridan & Verplank, *Human and Computer Control of Undersea Teleoperators*, MIT Man-Machine Systems Laboratory, **1978** (DTIC ADA057655) — a **10-level** scale, 36 years before J3016.

**Other academic proposals worth knowing:**
- **Hassan, Li, Lin, Adams, Chen, Kashiwa & Qiu, *Agentic Software Engineering: Foundational Pillars and a Research Roadmap*** (arXiv:2509.06216, Sep 2025) — the **SASE** vision, which proposes an SE 1.5–SE 5.0 hierarchy from *Token Assistance* to *General Domain Autonomy*, placing agentic SE at **SE 3.0 (Goal-Agentic)**. It also introduces the **Agent Command Environment (ACE)** and artifacts called **Merge-Readiness Packs** and **Consultation Request Packs**. ⭐ Notably, **it calls for an SAE-J3016-style standard rather than claiming to be one** — the clearest available evidence from inside the literature that none exists.
- **Measuring AI agent autonomy: Towards a scalable approach with code inspection** (arXiv:2502.15212) — an attempt to *measure* autonomy empirically rather than declare levels.
- The **Knight First Amendment Institute** hosts Feng et al. as a policy-side framing.

#### ⭐ The competing scale — and the proof of non-convergence

Feng, McDonald & Zhang (University of Washington), *Levels of Autonomy for AI Agents*, **arXiv:2506.12469, 14 Jun 2025**; also published by the Knight First Amendment Institute, 28 Jul 2025. Five levels named for the **user's** role: **1 Operator · 2 Collaborator · 3 Consultant · 4 Approver · 5 Observer.**

**The contradiction:**

| Term | DeepMind (2023) | Feng et al. (2025) |
|---|---|---|
| Collaborator | **Level 3** — describes the *AI* | **Level 2** — describes the *user* |
| Consultant | **Level 2** — describes the *AI* | **Level 3** — describes the *user* |

Under DeepMind, "Consultant" is *low* autonomy. Under Feng et al. it is *higher*. **"We run our agents at Level 3" is uninterpretable without naming the scale.** DeepMind and CSA start at 0 with six levels; Feng et al. and most vendors start at 1 with five.

#### ⭐ Frontier labs decline discrete autonomy levels

**Anthropic — ASL levels are safeguard tiers, NOT autonomy levels.** RSP v3.4 (effective 8 Jul 2026), from the changelog: "**ASL definition changed:** The term 'ASL' now refers to groups of technical and operational safeguards (it previously also referred to models)." And: "We have decided not to maintain a commitment to define ASL-N+1 evaluations… such an approach would add unnecessary complexity because **Capability Thresholds do not naturally come grouped in discrete levels.**"

**Anthropic's actual autonomy measurement is a continuous 1–10 scale.** *Measuring AI agent autonomy in practice* (McCain, Millar, Huang, Eaton et al., 18 Feb 2026): "we use 'autonomy' somewhat informally to refer to the degree to which an agent operates independently of human direction," scored on "a comparative scale from 1 to 10." Findings: **73% of tool calls appear to have a human in the loop; 0.8% of actions appear irreversible**; software engineering is roughly 50% of tool calls.

> ⚠️ **Correction flag:** third-party posts describing an "Anthropic Five-Level Agent Autonomy Framework" **misdescribe this paper.** Do not repeat that.

**OpenAI's "five levels"** (Chatbots → Reasoners → Agents → Innovators → Organizations) come from an internal all-hands in July 2024, **reported by Bloomberg** `[SECONDARY]`; **not published on openai.com**. Even as reported it is an AGI-progress roadmap, not an autonomy scale. And OpenAI's Feb 2026 harness post has a section literally headed "Increasing levels of autonomy" **that defines no numbered scale.**

**Google DeepMind's Frontier Safety Framework v3** (Sept 2025) uses **Critical Capability Levels** — capability thresholds, not autonomy levels. (Note the irony: DeepMind publishes the field's best-known autonomy table *and* a safety framework that does not use it.)

#### Standards bodies — all checked, all negative

| Body | Document | Levels? | Evidence |
|---|---|---|---|
| **NIST** | AI RMF 1.0 (AI 100-1), Jan 2023 | **No** | Only **3 occurrences of "autonom\*"** in the whole framework; one is a spectrum, not a scale: "Human-AI configurations can span from fully autonomous to fully manual" |
| **NIST/CAISI** | **AI Agent Standards Initiative**, announced **17 Feb 2026** | **No** | Three pillars; describes agents as "capable of autonomous actions" but defines **no levels**. ⭐ Most likely future home of a real standard; has produced none |
| **ISO/IEC** | 22989:2022 | **No** | Clause 5.13 defines autonomy qualitatively |
| **ISO/IEC** | **DIS/FDIS 42105** — *Guidance for human oversight of AI systems* | **Unpublished/unverified** | Closest in spirit; FDIS ~Jun 2026. Paywalled. **"One to watch," not a finding** |
| **IEEE** | **P3394** (LLM Agent Interface) | **No** | Message formats, agent roles, sessions — an interface standard |
| **EU** | **AI Act (Reg. 2024/1689)** | **No — confirmed** | Art. 3(1) says systems "designed to operate with **varying levels of autonomy**"; Recital 12 glosses it as "some degree of independence of actions from human involvement." **No levels scale anywhere in the Act** |

> ⚠️ **The strongest candidate has a disqualifying caveat.** Cloud Security Alliance, *Agentic AI Autonomy Levels and Control Framework* v2.0 (18 Mar 2026; six levels, L0 No Autonomy → L5 Full Autonomy, with L3 called "a significant governance threshold"), following Jim Reavis's *Autonomy Levels for Agentic AI* (28 Jan 2026), which candidly says "Consider this an invitation to a conversation rather than a finished proposal." The v2.0 cover page states verbatim: **"Unofficial AI-assisted Research"** and **"This document was generated with AI assistance and has not undergone official CSA review and approval processes."** No named human author. **The most standards-shaped autonomy-levels document in existence as of Aug 2026 is a self-declared unofficial, AI-generated, unreviewed white paper.**

#### ⚠️ No coding-agent vendor publishes an L1–L5 scale

Official docs checked for **GitHub/Copilot, Cursor, Cognition/Devin, Google Jules, Amazon Kiro, Sourcegraph Amp, Replit, Factory AI, Augment** — **none publishes a numbered autonomy scale.** GitHub categorises agents by *deployment context* (cloud agent, CLI, IDE, code-review agent), not autonomy level.

What exists instead is content marketing inventing mutually inconsistent scales: Swarmia (Assistive · Conversational · Task Agent · Autonomous Teammate · Agentic Avalanche — cites no prior work, not even SAE), asdlc.io (unattributed, "SAE-inspired"), Zencoder, Augment Code, Dash0, Vellum, MindStudio — five or six levels, all different.

#### The serious objection: autonomy is a dial, not a ladder

- **Andrej Karpathy**, "Software 3.0" (YC AI Startup School, Jun 2025), argues for an **"autonomy slider"** — a continuous per-context control, not discrete tiers, drawing on his Tesla Autopilot experience. `[SECONDARY]` transcript.
- **Empirical support:** *Hedwig: Dynamic Autonomy for Coding Agents Under Local Oversight* (Shukla, Feng, Wang, Rostami, Zhang), arXiv:2605.11495, 12 May 2026 — a survey of 21 software engineers found they "experience frustration with calibrating autonomy and have evolving preferences for level of oversight"; static permission settings "cannot account for how developers' preferences for agent autonomy can shift across tasks and over time."
- Anthropic's continuous 1–10 scale is the same objection expressed as measurement.

**Recommendation for this project:** if you need a scale, **define your own explicitly and say you are defining it.** Cite Morris et al. (arXiv:2311.02462) as the origin of the vocabulary and Feng et al. (arXiv:2506.12469) as the leading alternative, and note that they contradict each other. Better still, follow Karpathy and Anthropic: treat autonomy as a **per-action dial**, and describe **what the human approves and when** — which maps onto §5.4.

**Vendor-marketing flag: HIGH.** Level frameworks are a standard content-marketing form because they let a vendor place its product one rung above the competition.

---

### 5.4 Human-in-the-loop / on-the-loop / out-of-the-loop

#### Definitions as the agent field uses them

- **Human-in-the-loop (HITL)** — the run blocks until a human acts. The human is a *required step*.
- **Human-on-the-loop (HOTL)** — the system proceeds; the human monitors and can override or abort. A *supervisor with a veto*, not a step.
- **Human-out-of-the-loop (HOOTL)** — no human can intervene during execution. Review, if any, is after the fact.

#### Origin — pinned precisely, and it is not where most people think

**HITL: no coiner, and probably none exists.** It appears as ordinary aerospace and control-engineering jargon by the early 1960s.
- Earliest verified titled artifact: R. G. Nagel, *"X-15 pilot-in-the-loop and redundancy evaluation,"* Air Force Flight Test Center, Edwards AFB, in the NASA FRC *Conference on the Progress of the X-15 Project*, **1961**.
- Earliest "man in the loop" in NASA's archive: R. M. Smith, *"Analysis and design of space vehicle flight control systems. Volume X — Man in the loop,"* **NASA-CR-829, 1 Jul 1967**.
- Google Books Ngrams shows "man in the loop" near zero through the 1950s, then a ~10× step change at **1962**.

> ⚠️ **Two negative findings that protect this glossary.** (i) **Any claim that "man-in-the-loop" originates in a specific 1950s missile-guidance document is unverified** — DTIC and HathiTrust, the two corpora that would settle it, both refuse automated access. Safe wording: *"in use in US aerospace and flight-control engineering by the early 1960s; no identifiable coiner."* (ii) The **Wiener → Licklider *Man-Computer Symbiosis* (1960) → HITL** genealogy is folk etymology. Licklider's paper is real and is 1960, but **does not use the phrase.**

**The ML sense is a later re-coinage, c. 2015–2021.** Hard evidence: Burr Settles's *Active Learning Literature Survey* (UW-Madison TR#1648, January 2009) — the field's standard survey — contains the word **"loop" zero times.**

**⭐ HOTL: origin pinned to a specific document and date.** **US Air Force, *Unmanned Aircraft Systems Flight Plan 2009–2047*, HQ USAF, 18 May 2009:**

> §4.6 Path to Autonomy: "Advances in computing speeds and capacity will change how technology affects the OODA loop… **Increasingly humans will no longer be 'in the loop' but rather 'on the loop' — monitoring the execution of certain decisions.** Simultaneously, advances in AI will enable systems to make combat decisions and act within legal and policy constraints without necessarily requiring human input."

> Assumption 6: "Agile, redundant, interoperable and robust command and control (C2) creates the capability of supervisory control **('man on the loop')** of UAS."

So the in-the-loop → on-the-loop contrast is a **US Air Force coinage of 18 May 2009**, framed as OODA-loop compression.

**⭐ The three-way trichotomy: Human Rights Watch & Harvard Law School International Human Rights Clinic, *Losing Humanity: The Case against Killer Robots*, 19 November 2012, p. 2** (verified verbatim):

> "Robotic weapons, which are unmanned, are often divided into three categories based on the amount of human involvement in their actions:
> • **Human-in-the-Loop Weapons:** Robots that can select targets and deliver force only with a human command;
> • **Human-on-the-Loop Weapons:** Robots that can select targets and deliver force under the oversight of a human operator who can override the robots' actions; and
> • **Human-out-of-the-Loop Weapons:** Robots that are capable of selecting targets and delivering force without any human input or interaction.
>
> …The term 'fully autonomous weapon' refers to both out-of-the-loop weapons and those that allow a human on the loop, but that are effectively out-of-the-loop weapons because **the supervision is so limited.**"

HRW's own footnote 3 undercuts its middle category on the same page, quoting Major Jeffrey Thurnher: oversight "would not be effective if **the human operator were merely a rubber stamp** to approve an engagement."

Note HRW's hedge — "are often divided into" — it presents the taxonomy as pre-existing. **HRW 2012 is the earliest artifact stating all three as named, defined categories and is what made them canonical; the underlying in/on contrast is USAF 2009**, and HRW cites that very document at its footnote 12.

#### ⭐ The load-bearing caveat: the institutions people cite don't use these terms

This is the most surprising finding in this section.

| Institution | Document | "loop" occurrences |
|---|---|---|
| **US DoD** | Directive 3000.09 (2012) and (2023) | **ZERO in both** |
| **EU** | Reg. (EU) 2024/1689 (AI Act) | **ZERO.** Art. 14 says **"Human oversight"** |
| **NIST** | AI RMF 1.0 | **ZERO.** Uses "human-AI configuration/teaming," "oversight" |
| **UK MoD** | JCN 1/18 *Human-Machine Teaming*, May 2018 | **Only "OODA loop" (×7)** — in a doctrine note whose subject *is* human-machine teaming |
| **ICRC** | Commentary on CCW Guiding Principles, 16 Jul 2020 | **ZERO** |
| **US delegation** | CCW Commentaries, 1 Sep 2020 | **ZERO** |

**DoDD 3000.09 in detail.** The 2012 version says instead: "Autonomous and semi-autonomous weapon systems shall be designed to allow commanders and operators to exercise **appropriate levels of human judgment over the use of force**" — a phrase that deliberately refuses to specify a loop position. Its glossary defines *autonomous weapon system*, *human-supervised autonomous weapon system* and *semi-autonomous weapon system*. **The 2023 reissue went further and stripped "human" from the definitions**, renaming *human-supervised* → **operator-supervised** and *human operator* → *operator*.

**Conclusion for the glossary:** the loop vocabulary is **advocacy-and-industry vocabulary, not regulatory vocabulary.** Regulators say *human oversight*, *human-machine interaction*, *appropriate levels of human judgment*, or *meaningful human control*.

#### Contested-ness — a 43-year-old refutation and a 2026 measurement

**Lisanne Bainbridge, "Ironies of Automation," *Automatica* 19(6):775–779, 1983:**
> "it is impossible for even a highly motivated human being to maintain effective visual attention towards a source of information on which very little happens, for more than about half an hour. This means that it is humanly impossible to carry out the basic function of monitoring for unlikely abnormalities…"
> "the automatic control system has been put in because it can do the job better than the operator, but yet the operator is being asked to monitor that it is working effectively."

That is, in effect, **a 1983 refutation of "human-on-the-loop," written 26 years before the USAF coined it.**

**Madeleine Clare Elish, "Moral Crumple Zones," *Engaging Science, Technology, and Society* 5 (2019): 40–60:**
> "A prevailing rhetoric of human-computer interaction design suggests that keeping a 'human in the loop' assures that human judgment will always be able to supplement automation as needed… In practice, the dynamics of shared control between human and computer system are more complicated."
> "the human… may become simply a component… that bears the brunt of the moral and legal responsibilities when the overall system malfunctions… the moral crumple zone protects the integrity of the technological system, at the expense of the nearest human operator."

**Santoni de Sio & van den Hoven, "Meaningful Human Control over Autonomous Systems," *Frontiers in Robotics and AI* 5 (2018):**
> "**simple human presence or 'being in the loop' is not a sufficient condition for being in control**… for instance, if the human task consists in 'merely pushing a button in a reflex when a light goes on'."

**Meaningful human control (MHC)** is the rival term — Roff & Moyes, *Meaningful Human Control, Artificial Intelligence and Autonomous Weapons*, Article 36 briefing to the CCW Meeting of Experts, April 2016. ⭐ In that entire paper the word "loop" appears **once**, inside a cited title: the MHC school does not argue *within* the loop vocabulary, it refuses it.

#### ⭐ The strongest 2026 data point — a vendor confirming Bainbridge with production telemetry

Anthropic, *How we contain Claude across products* (~30 May 2026):

> "The first is to supervise the agent's behavior via a human-in-the-loop. Claude Code previously protected against agents taking unintended actions by asking users for permission at each turn. **Theoretically that works, but we've found the approach to be fallible. Our telemetry showed users approved roughly 93% of permission prompts. The more approvals a user sees, the less attention they pay to each, becoming over time much less diligent in their supervision.** … Still, vulnerabilities remain—any probabilistic defense has a non-zero miss rate."

> "The second approach… is containment. **Rather than supervising what the agent does, we supervise what it's able to do** by enforcing access boundaries through, for example, sandboxes, virtual machines, and egress controls."

A 93% approval rate is Thurnher's 2012 "rubber stamp," measured. It also documents the field's replacement move — **containment / capability restriction instead of loop position** — which is the same conclusion Willison reaches about guardrails (§5.2) and the same conclusion the lethal-trifecta framing implies (§5.12). Anthropic also notes the pattern's audience limit: "a non-technical knowledge worker shouldn't be expected to judge bash incantations."

#### Current agent-field usage

- **LangChain/LangGraph** — the canonical framework usage: "The Human-in-the-Loop (HITL) middleware lets you add human oversight to agent tool calls. When a model proposes an action that might require review… the middleware can pause execution and wait for a decision." Implemented via **interrupts**.
- **OpenAI Agents SDK** — "When a tool call requires approval, the SDK pauses the run, returns `interruptions`, and lets you resume later from the same `RunState`." API: `needsApproval`, `RunToolApprovalItem`, `.approve()`/`.reject()`.
- **Microsoft Agent Framework** — clearest vendor definition: "When agents require any user input, for example to approve a function call, this is referred to as a human-in-the-loop pattern."
- ⭐ **Anthropic uses it in engineering writing but NOT in Claude Code product docs** — zero occurrences across the permissions, hooks and Agent SDK permissions pages. Claude Code's vocabulary is **permission modes, allow/deny rules, approval, auto mode.**
- ⚠️ **AWS is blog-level only** — the Bedrock agents user guide page on human input has zero HITL occurrences; AWS says "user input."

#### Why this matters for this project

This is the most operationally useful triple in the glossary, because it maps directly onto harness configuration: HITL = permission prompts and approval gates; HOTL = interruptible streaming and monitored background agents; HOOTL = CI-triggered or scheduled agents where the only control is the harness itself.

**The same team is normally at all three points simultaneously** for different classes of action — HITL for a production deploy, HOTL for an edit in a worktree, HOOTL for a lint fix. Documents that ask "are you human-in-the-loop?" as a single global setting are asking the wrong question; the right question is per-action. And per Anthropic's own telemetry, **claiming HITL is not the same as having it.**

**Vendor-marketing flag: MODERATE.** "Human-in-the-loop" is heavily used as reassurance language in enterprise AI marketing, frequently for systems that are in fact human-on-the-loop, and — at a 93% approval rate — arguably human-out-of-the-loop with extra clicks.

---
### 5.5 MCP — Model Context Protocol

**Definition (from the spec itself):** "an open protocol that enables seamless integration between LLM applications and external data sources and tools." JSON-RPC 2.0 between three roles — **Hosts** (LLM applications initiating connections), **Clients** (connectors within the host), **Servers** (services providing context and capabilities). Servers expose **Resources**, **Prompts**, and **Tools**; clients may offer **Elicitation**. The spec names its own ancestor explicitly: "MCP takes some inspiration from the Language Server Protocol."

**Origin:** Announced by Anthropic **25 November 2024**, created by **David Soria Parra and Justin Spahr-Summers**. Launch partners: Block, Apollo (adopters); Zed, Replit, Codeium, Sourcegraph (dev tools).

> **Date correction worth carrying into the glossary:** several secondary sources say "late 2023." That is wrong. The confusion arises because the first *spec revision* is dated `2024-11-05`, twenty days before the public announcement.

**Current spec revision (Aug 2026): `2026-07-28`.** Versioning is a date string meaning "the last date backwards-incompatible changes were made" — it does not increment for compatible changes. Lineage: `2024-11-05` → `2025-03-26` → `2025-06-18` → `2025-11-25` → `2026-07-28`. `[SECONDARY]` for the middle revisions; both ends are primary-confirmed.

`2026-07-28` is a large breaking release and materially changes the vocabulary: it **removed protocol-level sessions**, **removed the `initialize`/`initialized` handshake (MCP is now stateless)**, added a mandatory `server/discover` RPC, introduced **Multi Round-Trip Requests (MRTR)** replacing server-initiated requests, and **deprecated Roots, Sampling and Logging**. It also adopted a formal **feature lifecycle and deprecation policy** with a minimum twelve-month deprecation window — a genuine standards-governance artifact.

**Is it a standard?** The precise, defensible answer:

> MCP began as a vendor protocol with unusually fast cross-vendor adoption, and since **9 December 2025** it is formally vendor-neutral-governed: Anthropic donated it to the **Agentic AI Foundation (AAIF)**, a directed fund under the Linux Foundation, co-founded with **Block and OpenAI** (supporting members Google, Microsoft, AWS, Cloudflare, Bloomberg). But **governance neutrality is not standards-body ratification.** The Linux Foundation is a neutral *host*, not a standards development organization. MCP has no formal standards track, no RFC, no ISO number. Its change process remains the maintainer-run **SEP** (Specification Enhancement Proposal) process, which the donation explicitly left unchanged: "For MCP little changes. The governance model we introduced earlier this year continues as is."

The AAIF's three founding projects were **MCP (Anthropic), goose (Block), and AGENTS.md (OpenAI)**. Adoption figures given in the donation announcement: 97 million monthly SDK downloads; 10,000+ active public servers.

**Adoption by rivals:** OpenAI (Sam Altman, 26 Mar 2025 `[SECONDARY]` via TechCrunch); Google DeepMind (Demis Hassabis, ~9 Apr 2025 — "MCP is a good protocol and it's rapidly becoming an open standard for the AI agentic era"); Microsoft (native Windows 11 support announced at Build 2025 `[SECONDARY]`).

**Contested — on security, heavily.** The spec itself concedes: "MCP itself cannot enforce these security principles at the protocol level." OWASP has a named attack entry, **MCP Tool Poisoning**. The Cloud Security Alliance published a research note titled "MCP Security Crisis: Systemic Design Flaws in AI Agent Infrastructure" (4 May 2026). Microsoft Security published "The state of MCP security in 2026."

**Competing / adjacent protocols — the "protocol wars" framing is now obsolete:**

| Protocol | Origin | Governance (Aug 2026) |
|---|---|---|
| **A2A (Agent2Agent)** | Google Cloud, Apr 2025 | Donated to Linux Foundation 23 Jun 2025; **became an AAIF hosted project in Aug 2026** — same foundation as MCP. 150+ orgs. |
| **AGNTCY** ("Internet of Agents") | Cisco, Mar 2025 | Joined Linux Foundation 29 Jul 2025. Explicitly interoperable with, not competing with, A2A and MCP. |
| **WebMCP** | Google + Microsoft engineers | **W3C Draft Community Group Report, 10 Feb 2026**, Web Machine Learning CG. `navigator.modelContext`. **The only one on a genuine standards-body track.** `[SECONDARY]` — no w3.org primary reached; verify before publishing. |
| **agents.json** | Wildcard AI | v0.1.0 atop OpenAPI. Marginal; absent from mainstream 2026 roundups. `[SECONDARY]`, partly promotional sourcing. |

The layers are complementary: MCP = model↔tool; A2A = agent↔agent; AGNTCY = discovery/identity substrate; WebMCP = website↔agent.

**Vendor-marketing flag:** Low for the protocol; **moderate for "Agentic AI Foundation" itself**, which is a co-branding exercise by Anthropic/Block/OpenAI. The substantive evidence of real governance is the feature-lifecycle policy and SEP process, not the press releases.

---

### 5.6 Tool use / function calling

**Origin:** "Function calling" originates with **OpenAI, 13 June 2023**, in "Function calling and other API updates." `[SECONDARY]` — openai.com returned HTTP 403 to automated fetch; corroborated same-day by Simon Willison, who characterised it as an implementation of the **ReAct pattern** and noted the post acknowledged prompt-injection risk without naming it.

**Anthropic** uses **"tool use"** as the head term, with `tool_use` / `tool_result` content blocks and `stop_reason: "tool_use"`.

**Has the field converged? Yes — explicitly and bidirectionally.** This is the cleanest convergence finding in the whole document. Both vendors now gloss the other's term in the opening sentence of their own docs:

- **Anthropic:** "**Tool use (also called function calling)** lets Claude call functions that you define or that Anthropic provides."
- **OpenAI:** "**Function calling (also known as tool calling)**" … "A function call or tool call refers to a special kind of response we can get from the model."

The directional drift is toward **"tool"** as the noun, because "function" became too narrow once tools included server-executed capabilities (web search, code execution) and MCP servers. Anthropic's 2026 taxonomy subdivides further into **client tools** (run in your app) and **server tools** (run on the provider's infrastructure) — a distinction "function calling" never encoded.

**Recommendation:** use **"tool use"** as the head term and gloss "function calling" once as the legacy synonym.

**Vendor-marketing flag:** none. This is plain API vocabulary.

---

### 5.7 Context rot, context window management, compaction

**Context rot.** Popularised by the **Chroma Technical Report, "Context Rot: How Increasing Input Tokens Impacts LLM Performance," 14 July 2025** — Kelly Hong, Anton Troynikov, Jeff Huber; evaluated 18 models. Their framing: "LLMs are typically presumed to process context uniformly — that is, the model should handle the 10,000th token just as reliably as the 100th. However, in practice, this assumption does not hold."

> **Honest negative finding: Chroma does NOT claim to have coined the term.** It circulated informally before the report. Write "given its canonical empirical grounding in" — never "coined by."

**Academic ancestor: "Lost in the Middle."** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang — arXiv:2307.03172 (Jul 2023), later TACL 2024. Performance is highest when relevant information sits at the beginning or end of context and degrades significantly in the middle, *including* in models explicitly built for long context.

**"Needle in a haystack."** Greg Kamradt, ~8 Nov 2023 `[SECONDARY]` — an informal community benchmark, not a paper. Hide one fact at varying depths in a long document, sweep length and depth, plot a heatmap. The heatmap visualisation is what made it standard. The Chroma report exists partly as a critique of how *easy* NIAH is relative to real tasks.

**Drew Breunig's taxonomy of context failures — "How Long Contexts Fail," 22 June 2025.** This is the most analytically useful vocabulary in this area and there are **four** modes, not three:

| Term | Breunig's definition (verbatim) | Evidence he cites |
|---|---|---|
| **Context Poisoning** | "When a hallucination or other error makes it into the context, where it is repeatedly referenced." | DeepMind Gemini 2.5 technical report |
| **Context Distraction** | "When a context grows so long that the model over-focuses on the context, neglecting what it learned during training." | Gemini 2.5 tech report; Databricks long-context RAG study |
| **Context Confusion** | "When superfluous content in the context is used by the model to generate a low-quality response." | Berkeley Function-Calling Leaderboard; GeoEngine benchmark |
| **Context Clash** | "When you accrue new information and tools in your context that conflicts with other information in the prompt." | Microsoft + Salesforce sharded-prompt research (39% average performance drop) |

**Compaction.** Anthropic's definition: "taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary." In Claude Code, compaction preserves architectural decisions, unresolved bugs and implementation details while discarding redundant tool outputs, then continues with the compressed context plus the five most recently accessed files.

**Contested-ness:** low for "compaction" (a concrete implemented mechanism with a vendor definition). Moderate for "context rot" — it is a *descriptive umbrella*, not a mechanism. Breunig's taxonomy and Chroma's report are independent and near-simultaneous (June/July 2025), which is why the two vocabularies sit awkwardly together: people often say "context rot" when they mean specifically distraction or confusion.

**Recommendation:** use **"context rot"** for the general phenomenon, and Breunig's four named modes when you need to be precise about which failure you mean.

---

### 5.8 Agentic AI vs AI agents

**"Agentic" as an adjective long predates AI.** OED records earliest use in the 1960s; established in psychology by **Albert Bandura**, *Social Foundations of Thought and Action* (1986), where it denotes the capacity to act intentionally and exercise control over one's environment. `[SECONDARY]` — the OED entry is paywalled.

**Entry into AI usage: Andrew Ng, March 2024** — and the reason he chose it is the most under-reported fact in this glossary. Ng deliberately imported the *adjective* as a **de-escalation device**:

> "Rather than having to choose whether or not something is an agent in a binary way, I thought it would be more useful to think of systems as being agent-like to different degrees." … "Unlike the noun 'agent,' the adjective 'agentic' allows us to contemplate such systems and include all of them in this growing movement."

`[SECONDARY]` — this quote reaches us via search snippet, not a successful fetch of the X post. **Verify before quoting.** His four **agentic design patterns** (The Batch, 27 Mar 2024) are solid: **Reflection, Tool use, Planning, Multi-agent collaboration.**

The irony worth recording: a word introduced specifically to *end* definitional fights became the industry's most contested marketing term.

**The academic attempt to distinguish the two:** "AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges" — arXiv:2505.10468 (May 2025), published in *Information Fusion* Vol. 126 (2025). Their stipulated distinction:
- **AI Agents** = "modular, single-entity systems," for task-specific automation.
- **Agentic AI** = "a paradigm shift marked by multi-agent collaboration, dynamic task decomposition, persistent memory, and coordinated autonomy" — "orchestrated ecosystems with emergent behaviors."

**Contested — very.** Named critics with citable positions:
- **Brinnae Bent, "The Term 'Agent' Has Been Diluted Beyond Utility and Requires Redefinition"** — arXiv:2508.05338, **accepted to AIES 2025** (AAAI/ACM). Argues the ambiguity damages "research communication, system evaluation and reproducibility, and policy development," and proposes a multidimensional spectrum (environmental interaction, learning/adaptation, autonomy, goal complexity, temporal coherence).
- **"Agentic AI and Multiagentic: Are We Reinventing the Wheel?"** — arXiv:2506.01463. Argues the field is renaming decades-old multi-agent-systems research.
- **"Agent-washing"** — the industry's own self-critical coinage, analogous to greenwashing.

**Verdict for the glossary:** the distinction is **real as a stipulated technical taxonomy** but **not real as observed usage**. Write it as: *a distinction proposed in the literature (single modular agent vs. orchestrated multi-agent system with persistent memory) that is not reliably observed in industry usage, where the two are used interchangeably and "agentic" primarily signals product positioning.*

**Vendor-marketing flag: HIGHEST in this document, jointly with "graph engineering."** Use "AI agent" and "multi-agent system" as your working terms; use "agentic" only as Ng intended — a scalar adjective, never a product category.

---

### 5.9 Verifier's Law and verification

**Origin:** **Jason Wei (then OpenAI), "Asymmetry of verification and verifier's law," 15 July 2025**, on his personal blog — not an OpenAI publication.

**Asymmetry of verification:** "Some tasks are much easier to verify than to solve." Wei argues this is becoming "one of the most important ideas in AI" specifically because RL now works generally.

**The law itself, verbatim from the live page (verified 2026-08-27):**

> "The ease of training AI to solve a task is proportional to how verifiable the task is. All tasks that are possible to solve and easy to verify will be solved by AI."

> **Naming quirk, verified twice:** the URL slug and Wei's own announcement say **"verifier's law"**, but the *heading on the page itself* renders as **"Verifier's rule."** Both readings are defensible; the field universally says "law." Use "Verifier's Law" and note the page heading if precision matters. Also beware a circulating paraphrase that inverts "ease" to "difficulty" — that reverses the proportionality and is wrong.

**Wei's five properties of easy-to-verify tasks:** objective truth; fast to verify; scalable to verify; low noise; continuous reward (ability to *rank* goodness, not just pass/fail).

**The implication he draws:** "Anything we can measure will be solved" — producing "a jagged edge of intelligence, where AI is much smarter at verifiable tasks."

**Why it matters to this project:** Verifier's Law is the theoretical backbone for why the field's practice vocabulary has shifted toward test-first, spec-driven and eval-driven agent workflows. Verifiability is the lever, so engineering effort moves to *constructing verifiers*. This connects directly to harness engineering (Böckeler's "sensors") and to evals. Karpathy independently states the same idea: "Traditional software automates what you can specify. LLMs and reinforcement learning automate what you can verify."

**Contested-ness:** low-to-moderate. It is presented as a heuristic, not a theorem, and Wei does not overclaim. Main academic engagement is empirical work on whether LLM verification is actually reliable (e.g. arXiv:2509.17995, "Variation in Verification").

**Vendor-marketing flag: none — the lowest in this document.** Personal blog, no product attached.

---

### 5.10 Vibe coding — and what replaced it

**Origin: Andrej Karpathy, X, 2 February 2025:**

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good."

`[SECONDARY]` for the fetch (x.com returns HTTP 402), but the text appears verbatim in the search-result title for that exact status URL and matches every rendering. Karpathy later called it "a shower of thoughts throwaway tweet."

**Dictionary status: yes.** **Collins Dictionary Word of the Year 2025**, announced 6 Nov 2025. Collins' gloss: "the use of artificial intelligence prompted by natural language to write computer code." Collins explicitly credits Karpathy.

**Meaning drift — the heart of this entry.** Karpathy's original sense was narrow and self-deprecating: throwaway weekend projects, not reading the diffs. Within months it was applied indiscriminately to all AI-assisted development including disciplined test-driven work, and became a way to dismiss people.

**Succession, in three stages:**

1. **Simon Willison, "Vibe engineering," 7 Oct 2025.** His distinction: vibe coding is "the fast, loose and irresponsible way of building software with AI — entirely prompt-driven, and with no attention paid to how the code actually works"; vibe engineering is for professionals who remain "proudly and confidently accountable for the software they produce." He was openly ambivalent about his own coinage: "Is this a stupid name? Yeah, probably."
2. **Willison conceded his own coinage.** His post now carries a **February 2026 update** indicating "Agentic Engineering" has become the preferred term. A rare and citable instance of a coiner withdrawing in favour of a rival term.
3. **Karpathy, 30 April 2026** — his own blog, summarising his Sequoia Ascent 2026 fireside chat. Verified verbatim on 2026-08-27:
   > "Vibe coding raises the floor. It lets almost anyone create software by describing what they want. Agentic engineering raises the ceiling. It is the professional discipline of coordinating fallible agents while preserving correctness, security, taste, and maintainability."

   Also: "Agentic engineering is what serious teams need." "The agentic engineer does not blindly accept generated code." "Vibe coding is fine for prototypes and personal tools."

> **Important correction to the popular framing — verified against the primary source.** Secondary headlines say Karpathy "killed," "declared passé," or "regrets" vibe coding. **His own post does not support that.** He expresses no regret, does not call the term passé, and treats the two as **complementary — floor-raising vs ceiling-raising.** The "vibe coding is dead" narrative is press amplification. Cite the bearblog post, not the headlines.

**Terminology state as of Aug 2026:** three-way split — **vibe coding** (Karpathy's original, now narrowed back toward "prototypes and personal tools"), **vibe engineering** (Willison, Oct 2025, superseded by his own admission), **agentic engineering** (dominant since early 2026, endorsed by both).

**Vendor-marketing flag:** low for the terms themselves (both coined by independent individuals), but "vibe coding" is now heavily used in product marketing for no-code/low-code AI builders, where it means little more than "our product is easy."

---

### 5.11 Related terms this glossary should also carry

Established during research; shorter entries because they are less contested.

**Workflow vs agent** — Anthropic, "Building effective agents," 19 Dec 2024 (Erik Schluntz, Barry Zhang): "*Workflows* are systems where LLMs and tools are orchestrated through predefined code paths. *Agents* are systems where LLMs dynamically direct their own processes and tool usage." This is the single most load-bearing distinction in the field and the cleanest primary source for it.

**Agent loop / ReAct** — the reason–act–observe cycle. Introduced in **Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (2022)** — Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao. The model writes a Thought, takes an Action by calling a tool, reads the Observation, and thinks again. Nearly every agent harness implements a descendant of this loop; the de Macedo harness definition makes it condition T1.

**Subagent** — an agent spawned by another agent with its own context window, prompt, and tool permissions. Anthropic's multi-agent research post (13 Jun 2025) is the best primary source; Claude Code's docs define it operationally. `[SECONDARY]` for the claim that it "became industry-standard terminology in a matter of months" — plausible and widely reported, but not first-party sourced.

**AGENTS.md** — primary definition from agents.md itself: "a simple, open format for guiding coding agents" giving them "a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project." Released by **OpenAI in August 2025**; the site states it "emerged from collaboration among OpenAI Codex, Amp, Jules from Google, Cursor, and Factory," and reports **over 60,000 open-source projects** using it.

**Governance — and this is the sharp contrast with Agent Skills:** agents.md states plainly that "AGENTS.md is stewarded by the **Agentic AI Foundation** under the Linux Foundation," and it was one of AAIF's three founding project contributions in December 2025. So **AGENTS.md and MCP are genuinely foundation-governed; Agent Skills is not** (see §3). If your documents need to distinguish "open standard" from "openly published vendor format," that is the line.

`[SECONDARY]` only for the claim that Claude Code does not read AGENTS.md natively and that the recommended pattern is AGENTS.md as source of truth with a thin CLAUDE.md importing it.

**Hooks** — user-supplied commands the harness runs at fixed points in the session lifecycle; the primary *deterministic* enforcement mechanism in a harness, as opposed to instructions, which are advisory. In Claude Code, `PreToolUse` is the checkpoint before any tool runs. `[SECONDARY]` for the specific mechanics.

**Permission modes** — the session-wide posture governing what an agent may do without asking (e.g. default / accept-edits / plan / bypass in Claude Code). Together with allow/deny rules and sandboxing these form the *control mechanisms* of condition T4 in the harness definition. `[SECONDARY]`.

**Sandbox** — an OS-level boundary limiting what an agent's shell can touch; platform-dependent in practice. `[SECONDARY]`.

**Spec-driven development (SDD)** — "a methodology in which a written specification is treated as the primary, executable artifact of a software project, and code is a regenerable output produced from that spec by humans, AI agents, or both." Emerged 2025 as an explicit response to vibe coding's failure modes. Tooling: **GitHub Spec Kit**, **AWS Kiro** (spec → design → tasks → implementation), OpenSpec, BMAD, Tessl. `[SECONDARY]` — this definition and the adoption claims come from secondary explainers; I did not reach a primary coinage artifact, and efficacy claims such as "3–10× higher first-pass success" should be treated as unverified vendor-adjacent marketing.

**Flow engineering** — see §4. Ridnik, Kredo & Friedman, arXiv:2401.08500 (Jan 2024). Real, primary-sourced, and the correct term for "the developer designs the control structure; the agent makes local decisions inside it."

**Agentic engineering** — see §5.10. Karpathy, Apr 2026. Emerging; young but rising fast, and endorsed by both Karpathy and Willison.

---

### 5.12 Agent security vocabulary

A glossary about teams working with agents would be negligent to omit these three. All are primary-sourced and all are genuine practice vocabulary rather than product naming.

**Prompt injection** — coined by **Simon Willison on 12 September 2022**, by explicit analogy to SQL injection: the problem of concatenating trusted instructions and untrusted content into the same context, where the model cannot distinguish them. Note it is *not* the same as jailbreaking: jailbreaking is a user trying to bypass a model's own guidelines; prompt injection is a third party's content hijacking an application's instructions.

**The lethal trifecta** — **Simon Willison, 16 June 2025.** An agent session is dangerous when it combines all three of:
1. "Access to your private data"
2. "Exposure to untrusted content"
3. "The ability to externally communicate" in a way that could exfiltrate data

Any two are safe; all three let an attacker who controls the untrusted content steal the private data. This is the single most useful trust-boundary heuristic in the field and it is a checkable property of a harness configuration, which makes it directly actionable for harness engineering.

> Disambiguation: the AI-safety literature has a different, unrelated "lethal trifecta" (advanced capabilities + agentic behaviour + situational awareness). `[SECONDARY]`. If your documents touch both areas, qualify on first use.

**Agents Rule of Two** — **Meta, October 2025**, "Agents Rule of Two: A Practical Approach to AI Agent Security." A deterministic architectural restatement of the trifecta: an agent session should satisfy **at most two** of (A) processing untrustworthy inputs, (B) access to sensitive data, (C) ability to change state or communicate externally. Meta's framing of the underlying problem: "Prompt injection is a fundamental, unsolved weakness in all LLMs."

**Why these belong in this glossary:** they are the clearest example in the field of vocabulary that is *operational* rather than descriptive — each is a property you can check against a specific harness configuration, which is exactly what makes them useful in documents about how teams actually work.

---

## Terms we should NOT use

| Term | Why not | Use instead |
|---|---|---|
| **Graph engineering** | Manufactured vocabulary. No primary source, no framework doc, no paper, no named practitioner. All usage is a 2026 SEO/content-marketing cluster citing itself. Also collides with the established, unrelated "knowledge graph engineering." | **Agent orchestration** for the discipline; **flow engineering** (Ridnik et al. 2024) for the narrower "design the control structure explicitly" sense. "Graph" as a *noun* for a structure is fine. |
| **"Agentic AI" as a product category** | The academic distinction from "AI agent" is stipulated in one paper and is not observed in practice. Peer-reviewed criticism exists (Bent, AIES 2025) arguing the word has been "diluted beyond utility." The industry has its own name for its misuse: *agent-washing*. | **AI agent**, **multi-agent system**. Keep "agentic" only as Ng intended — a scalar adjective describing degree, never a category. |
| **Bare lowercase "skill"** for the SKILL.md artifact | Four live competing senses: Alexa Skills, Semantic Kernel skills (retired to "plugins" in 2023), RL/robotics skills, and colloquial "a thing the model can do." | **Agent Skill** or **SKILL.md**, capitalised, on first use in every section. |
| **Bare "harness"** in any document that also discusses evaluation | Genuine, documented ambiguity: `swebench.harness` is an *evaluation* harness; Claude Code is an *agent* harness. The literature is now actively disentangling the two because conflating them corrupts benchmark results. | **Agent harness** / **eval harness**, qualified on first use per section. |
| **"Prompt engineering" as the name of the discipline** | Demoted. Every major primary source now treats it as a subset of context engineering. Simon Willison's diagnosis is that public usage degraded it to "typing stupid hacks into a chatbot." | **Context engineering** for the discipline; keep "prompt engineering" for the narrow, genuine sense of wording instructions well. |
| **"Vibe coding" for professional AI-assisted work** | Karpathy's original sense was narrow and self-deprecating — prototypes, not reading the diffs. Applying it to disciplined work is a category error and reads as dismissal. Karpathy himself now scopes it to "prototypes and personal tools." | **Agentic engineering** (Karpathy, Apr 2026; Willison conceded to it Feb 2026). Reserve "vibe coding" for its literal original meaning. |
| **"Vibe engineering"** | Retired coinage. Its own author, Simon Willison, updated his post in Feb 2026 to say "agentic engineering" is now preferred. Using it dates a document. | **Agentic engineering**. |
| **"L3 autonomy" or any bare level reference** | **Uninterpretable without naming the scale.** The two leading proposals swap terms: "Consultant" is Level 2 for DeepMind (Morris et al., 2023) and Level 3 for Feng et al. (2025). At least six further vendor scales circulate, all mutually inconsistent. No standards body has published one. | Define your own scale explicitly and say you are defining it; or better, treat autonomy as a per-action dial and describe **what the human approves and when** (see §5.4). |
| **"Guardrails"** as a load-bearing noun | Umbrella term with no vendor-neutral specification, shaped by three 2023 products, and a favourite of governance marketing where it often means only "we have safety features." | Name the mechanism: validation, allowlist, sandbox, classifier, tripwire, permission rule, hook. Use "guardrails" only as the umbrella. |
| **"MCP is the USB-C of AI"** and similar analogies | Vendor-adjacent marketing shorthand that obscures the actual governance question (foundation-hosted, not standards-body-ratified) and the substantial open security literature. | Say what it is: an open protocol, JSON-RPC 2.0, foundation-governed since Dec 2025, with an unresolved prompt-injection threat model the spec itself concedes it cannot fix. |
| **"Agent Skills is an industry standard"** | Overstated. It is an openly published, broadly adopted vendor format with no neutral governance body — unlike MCP and AGENTS.md, which are AAIF-governed. Some secondary sources wrongly claim AAIF stewardship of Skills; the repo and site say no such thing. | "An open specification with broad multi-vendor adoption." |
| **SWE-bench Verified scores** | **Deprecated by its own publisher.** OpenAI stopped reporting them on 23 Feb 2026: improvements "increasingly reflect how much the model was exposed to the benchmark at training time." UTBoost (ACL 2025) separately found 24.4% of leaderboard entries affected by mislabelled patches. | SWE-bench Pro, Terminal-Bench — and always name the agent harness alongside the model. |
| **Any bare agent benchmark score** | Harness choice moves Pass@1 by up to 27.4 points and token cost by up to 40×. A score without a named harness is a joint measurement presented as a model measurement. | "Model X + harness Y resolves N%." |
| **"Human-in-the-loop"** as a reassurance claim | Anthropic's own telemetry: **93% of permission prompts approved.** Bainbridge (1983) predicted this; HRW's own 2012 footnote called it a "rubber stamp." The claim describes a mechanism, not an outcome. | Say what the human actually gates, and prefer **containment** language — sandboxes, egress controls, least-privilege tool scopes — over supervision language. |
| **"loop" vocabulary in a regulatory register** | Zero occurrences in DoDD 3000.09 (2012 and 2023), the EU AI Act, the NIST AI RMF, UK MoD JCN 1/18, and the ICRC/US CCW commentaries. It is advocacy-and-industry vocabulary. | Regulators say **human oversight**, **appropriate levels of human judgment**, or **meaningful human control**. |
| **Leaning on the harness/scaffold distinction** | Anthropic equates them ("agent harness (or scaffold)"); Hugging Face separates them. Its own author reports that practitioners at ICLR 2026 "did not converge to a single explanation." | Treat them as near-synonyms. Qualify **eval harness** vs **agent harness** instead — that distinction is real and load-bearing. |
| **"OpenAI's five levels of AI"** (Chatbots → Reasoners → …) | Reported by Bloomberg from an internal all-hands, July 2024. **Not published on openai.com.** And even as reported it is an AGI-progress roadmap, not an autonomy scale. | Don't cite it as an OpenAI publication. |
| **Attributing the eval/benchmark distinction to Hamel Husain** | His 2024 post never uses the word "benchmark." `openai/evals` conflates the two in its own tagline. The distinction is real in practice but has no authoritative source. | State it as a widely-held informal distinction and cite Brenn Hill (Jun 2026) as the clearest articulation. |

---

## Sources

All URLs accessed **2026-08-27** unless otherwise noted. Fetch failures are marked.

### Context engineering
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — Anthropic, 29 Sep 2025
- https://www.langchain.com/blog/the-rise-of-context-engineering — Harrison Chase, 23 Jun 2025
- https://www.philschmid.de/context-engineering — Phil Schmid, 30 Jun 2025
- https://simonwillison.net/2025/jun/27/context-engineering/ — 27 Jun 2025
- https://www.dbreunig.com/2025/07/24/why-the-term-context-engineering-matters.html — 24 Jul 2025
- https://arxiv.org/abs/2507.13334 — Mei et al., 17 Jul 2025
- https://github.com/humanlayer/12-factor-agents — Dex Horthy / HumanLayer
- https://x.com/tobi/status/1935533422589399127 — **HTTP 402, not fetchable**
- https://x.com/karpathy/status/1937902205765607626 — **HTTP 402, not fetchable**

### Harness engineering
- https://mitchellh.com/writing/my-ai-adoption-journey — Mitchell Hashimoto, 5 Feb 2026
- https://openai.com/index/harness-engineering/ — OpenAI, 11 Feb 2026 — **HTTP 403, not fetchable directly**
- https://www.infoq.com/news/2026/02/openai-harness-engineering-codex/ — InfoQ, 21 Feb 2026
- https://www.langchain.com/blog/the-anatomy-of-an-agent-harness — Vivek Trivedy, 10 Mar 2026
- https://martinfowler.com/articles/harness-engineering.html — Birgitta Böckeler / Thoughtworks, 2 Apr 2026
- https://addyosmani.com/blog/agent-harness-engineering/ — Addy Osmani, 19 Apr 2026
- https://en.wikipedia.org/wiki/Agent_harness
- https://arxiv.org/html/2606.10106v1 — de Macedo, Jun 2026
- https://arxiv.org/abs/2602.14690 — Galster et al., 16 Feb 2026
- https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents — Anthropic, 26 Nov 2025
- https://www.anthropic.com/engineering/harness-design-long-running-apps — Anthropic
- https://www.softwareimprovementgroup.com/blog/what-is-harness-engineering/ — SIG, 24 Apr 2026

### Skills
- https://agentskills.io/ and https://agentskills.io/specification
- https://github.com/agentskills/agentskills — checked for governance language; none found
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills — 16 Oct 2025, updated 18 Dec 2025
- https://code.claude.com/docs/en/skills
- https://simonwillison.net/2025/Dec/19/agent-skills/ — 19 Dec 2025
- https://github.com/microsoft/semantic-kernel/issues/2119 — 21 Jul 2023
- https://devblogs.microsoft.com/agent-framework/skills-to-plugins-fully-embracing-the-openai-plugin-spec-in-semantic-kernel/

### Orchestration / graph engineering
- https://www.anthropic.com/engineering/building-effective-agents — Schluntz & Zhang, 19 Dec 2024
- https://www.anthropic.com/engineering/multi-agent-research-system — Hadfield et al., 13 Jun 2025
- https://docs.langchain.com/oss/python/langgraph/overview
- https://openai.github.io/openai-agents-python/
- https://arxiv.org/abs/2401.08500 — Ridnik, Kredo & Friedman, Jan 2024 (AlphaCodium / flow engineering)
- https://github.com/Codium-ai/AlphaCodium
- https://www.gartner.com/reviews/market/multiagent-orchestration-platforms
- https://www.analyticsvidhya.com/blog/2026/07/graph-engineering/ — 28 Jul 2026 — cited as *evidence of provenance*, not as authority

### Evals and benchmarks
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents — Grace, Hadfield, Olivares, De Jonghe, Anthropic, 9 Jan 2026 — **defines eval harness and agent harness in adjacent sentences**
- https://hamel.dev/blog/posts/evals/ — Hamel Husain, 29 Mar 2024
- https://hamel.dev/blog/posts/llm-judge/ — Husain, 29 Oct 2024 (critique shadowing)
- https://hamel.dev/blog/posts/evals-faq/ — Husain, 28 May 2025, modified 18 Jul 2026
- https://simonwillison.net/2024/Mar/31/your-ai-product-needs-evals/ — 31 Mar 2024
- https://github.com/openai/evals — public 14 Mar 2023
- https://github.com/EleutherAI/lm-evaluation-harness — repo created 28 Aug 2020; the canonical *eval* harness
- https://arxiv.org/abs/2306.05685 — Zheng et al., LLM-as-a-Judge / MT-Bench, 9 Jun 2023
- https://inspect.aisi.org.uk/ — UK AI Security Institute, May 2024 (Dataset/Solver/Scorer; does not use "harness")
- https://www.braintrust.dev/docs/guides/evals · https://docs.langchain.com/langsmith/evaluation-concepts · https://docs.wandb.ai/weave/guides/evaluation/scorers
- https://evaldrivendevelopment.dev/evals-vs-tests-vs-benchmarks — Brenn Hill, Jun 2026 — `[SECONDARY]`, independent practitioner; best-stated eval/benchmark/test distinction
- https://arxiv.org/abs/2310.06770 — SWE-bench, Jimenez et al., 10 Oct 2023 (**never uses "harness"**)
- https://www.swebench.com/SWE-bench/reference/harness/
- https://openai.com/index/introducing-swe-bench-verified/ — 13 Aug 2024 — **uses "scaffold" for the agent side**; HTTP 403 to automated fetch
- https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ — 23 Feb 2026 — **deprecation notice**; HTTP 403
- https://metr.org/blog/2024-03-15-guidelines-for-capability-elicitation/ — 15 Mar 2024 — "scaffold" x11, "harness" x0
- https://arxiv.org/abs/2601.11868 — Terminal-Bench, Merrill, Shaw, Carlini, Li et al., 17 Jan 2026
- https://arxiv.org/abs/2509.16941 — SWE-bench Pro, Scale AI
- https://arxiv.org/abs/2605.27922 — Harness-Bench, 27 May 2026
- https://arxiv.org/abs/2606.12344 — Claw-SWE-Bench, 10 Jun 2026
- https://arxiv.org/abs/2607.22585 — The Scaffold Effect, Vats and Golev, 8 Jun 2026
- https://arxiv.org/abs/2506.09289 — UTBoost, Yu, Zhu, He, Kang, ACL 2025
- https://arxiv.org/abs/2606.19544 — Reliability without Validity, Norman, Rivera, Hughes, 17 Jun 2026
- https://huggingface.co/blog/agent-glossary — Paniego and Roy Gosthipaty, 25 May 2026 — harness vs scaffold
- https://www.nist.gov/news-events/news/2024/05/nist-launches-aria-new-program-advance-sociotechnical-testing-and — May 2024

### Guardrails
- https://openai.github.io/openai-agents-python/guardrails/ — SDK 0.0.1 released 4 Mar 2025
- https://openai.github.io/openai-guardrails-python/ — the *second*, incompatible OpenAI "Guardrails," 6 Oct 2025
- https://github.com/NVIDIA/NeMo-Guardrails — `nemoguardrails` 0.1.0 on PyPI 25 Apr 2023
- https://developer.nvidia.com/blog/nvidia-enables-trustworthy-safe-and-secure-large-language-model-conversational-systems/ — 25 Apr 2023
- https://raw.githubusercontent.com/guardrails-ai/guardrails/v0.1.0/README.md — repo created 29 Jan 2023; **original meaning was schema validation**
- https://www.guardrailsai.com/blog/the-future-of-ai-reliability — Guardrails Hub, 15 Feb 2024
- https://arxiv.org/abs/2312.06674 — Llama Guard, Inan et al., 7 Dec 2023 — **contains "guardrail" zero times**
- https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview — **zero occurrences of "guardrail"**
- https://docs.aws.amazon.com/controltower/latest/controlreference/controls.html — **AWS renaming guardrails to controls**
- https://arxiv.org/abs/2402.01822 — Dong et al., *Building Guardrails for LLMs*, updated 29 May 2024
- https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks
- https://simonwillison.net/2025/Oct/22/openai-ciso-on-atlas/ · https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion/
- OWASP LLM Prompt Injection Prevention Cheat Sheet

### Autonomy levels
- https://arxiv.org/abs/2311.02462 — **Morris, Sohl-Dickstein, Fiedel, Warkentin, Dafoe, Faust, Farabet, Legg, *Levels of AGI*, 4 Nov 2023 — origin of "Levels of Autonomy"**
- https://arxiv.org/abs/2506.12469 — **Feng, McDonald and Zhang, *Levels of Autonomy for AI Agents*, 14 Jun 2025** (also Knight First Amendment Institute, 28 Jul 2025)
- https://knightcolumbia.org/content/levels-of-autonomy-for-ai-agents-1
- https://arxiv.org/abs/2509.06216 — Hassan, Li, Lin, Adams, Chen, Kashiwa & Qiu, *Agentic Software Engineering* (SASE), Sep 2025 — calls for a standard rather than being one
- https://arxiv.org/abs/2502.15212 — Measuring AI agent autonomy via code inspection
- Sheridan and Verplank, *Human and Computer Control of Undersea Teleoperators*, MIT, 1978 — DTIC ADA057655; DOI 10.21236/ada057655
- SAE J3016_202104, 30 Apr 2021 (first issued 16 Jan 2014)
- https://cdn.standards.iteh.ai/samples/74296/c4efbadbf1a146d4af6d62fcad09438f/ISO-IEC-22989-2022.pdf — official preview; **autonomy / heteronomy definitions**
- https://www.anthropic.com/responsible-scaling-policy — RSP v3.4, effective 8 Jul 2026 — ASL are *safeguard tiers*, not autonomy levels
- https://www.anthropic.com/research/measuring-agent-autonomy — McCain, Millar, Huang, Eaton et al., 18 Feb 2026 — **continuous 1–10 scale; 73% of tool calls have a human in the loop**
- https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf — AI RMF 1.0, Jan 2023 — 3 occurrences of "autonom*", no levels
- https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative — 17 Feb 2026 — no levels
- https://www.iso.org/standard/86902.html — ISO/IEC 42105, *Guidance for human oversight of AI systems* — **unpublished, paywalled; one to watch**
- https://cloudsecurityalliance.org/blog/2026/01/28/levels-of-autonomy — Jim Reavis, 28 Jan 2026, "an invitation to a conversation rather than a finished proposal"; v2.0 (18 Mar 2026) is labelled **"Unofficial AI-assisted Research"**
- https://arxiv.org/abs/2605.11495 — *Hedwig: Dynamic Autonomy for Coding Agents*, 12 May 2026
- https://www.latent.space/p/s3 — Karpathy, "autonomy slider," Jun 2025 `[SECONDARY]` transcript
- EU Reg. (EU) 2024/1689, Art. 3(1) and Recital 12 — "varying levels of autonomy," **no scale**

### Human-in/on/out-of-the-loop
- https://web.archive.org/web/2013/http://www.govexec.com/pdfs/072309kp1.pdf — **USAF, *UAS Flight Plan 2009-2047*, 18 May 2009 — origin of "on the loop"**
- https://cdn.netzpolitik.org/wp-upload/2016/12/Air-Force-Unmanned-Aerial-Flight-Plan-2009-2047.pdf — corroborating briefing deck
- https://www.hrw.org/sites/default/files/reports/arms1112_ForUpload.pdf — **HRW and Harvard IHRC, *Losing Humanity*, 19 Nov 2012, p. 2 — origin of the trichotomy**
- DoD Directive 3000.09, 21 Nov 2012 and 25 Jan 2023 — **"loop" appears zero times in both**
- https://ntrs.nasa.gov/citations/19710070150 — Nagel, X-15 "pilot-in-the-loop," 1961
- https://ntrs.nasa.gov/citations/19670020803 — NASA-CR-829, "Man in the loop," 1 Jul 1967
- https://minds.wisconsin.edu/bitstream/handle/1793/60660/TR1648.pdf — Settles, *Active Learning Literature Survey*, Jan 2009 — "loop" x0
- https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf — Bainbridge, *Ironies of Automation*, 1983
- Elish, *Moral Crumple Zones*, ESTS 5 (2019): 40-60, DOI 10.17351/ests2019.260
- Santoni de Sio and van den Hoven, *Meaningful Human Control over Autonomous Systems*, Frontiers in Robotics and AI 5, 28 Feb 2018, DOI 10.3389/frobt.2018.00015
- https://article36.org/wp-content/uploads/2016/04/MHC-AI-and-AWS-FINAL.pdf — Roff and Moyes, Apr 2016
- https://www.anthropic.com/engineering/how-we-contain-claude — ~30 May 2026 — **93% of permission prompts approved**
- https://docs.langchain.com/oss/python/langchain/human-in-the-loop · https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval
- https://www.csis.org/analysis/dod-updating-its-decade-old-autonomous-weapons-policy-confusion-remains-widespread
### MCP, protocols, tools
- https://modelcontextprotocol.io/specification/latest
- https://modelcontextprotocol.io/specification/versioning
- https://modelcontextprotocol.io/specification/2026-07-28/changelog
- https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ — 9 Dec 2025
- https://www.anthropic.com/news/model-context-protocol — 25 Nov 2024
- https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation
- https://agents.md/
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- https://developers.openai.com/api/docs/guides/function-calling
- https://openai.com/index/function-calling-and-other-api-updates/ — 13 Jun 2023 — **HTTP 403**
- https://simonwillison.net/2023/Jun/13/function-calling/
- https://owasp.org/www-community/attacks/MCP_Tool_Poisoning
- https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents
- https://www.linuxfoundation.org/press/linux-foundation-welcomes-the-agntcy-project-to-standardize-open-multi-agent-system-infrastructure-and-break-down-ai-agent-silos

### Context failure, verification, vibe coding, security
- https://www.trychroma.com/research/context-rot — Hong, Troynikov & Huber, 14 Jul 2025
- https://arxiv.org/abs/2307.03172 — Liu et al., Lost in the Middle, Jul 2023
- https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html — 22 Jun 2025
- https://www.jasonwei.net/blog/asymmetry-of-verification-and-verifiers-law — Jason Wei, 15 Jul 2025
- https://arxiv.org/html/2509.17995v1 — Variation in Verification
- https://x.com/karpathy/status/1886192184808149383 — 2 Feb 2025 — **HTTP 402, not fetchable**
- https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/ — 6 Nov 2025
- https://simonwillison.net/2025/Oct/7/vibe-engineering/ — 7 Oct 2025, updated Feb 2026
- https://karpathy.bearblog.dev/sequoia-ascent-2026/ — 30 Apr 2026
- https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ — 16 Jun 2025
- https://ai.meta.com/blog/practical-ai-agent-security/ — Meta, Oct 2025 (Agents Rule of Two)
- https://arxiv.org/abs/2505.10468 — AI Agents vs Agentic AI, May 2025
- https://arxiv.org/abs/2508.05338 — Bent, "The Term 'Agent' Has Been Diluted Beyond Utility," AIES 2025
- https://arxiv.org/abs/2506.01463 — "Are We Reinventing the Wheel?"
- https://www.deeplearning.ai/the-batch/issue-242/ — Andrew Ng, 27 Mar 2024

---

## Confidence and gaps

### High confidence
- **Harness engineering is real vocabulary.** Five credible venues (OpenAI, Anthropic, Thoughtworks/Fowler, LangChain, Cursor) plus academia plus Wikipedia, with a documented six-day coinage-to-adoption trail — *and* independent quantitative evidence that the harness is roughly as load-bearing as the model (Claw-SWE-Bench: 27.4 vs 29.4 percentage points on Pass@1).
- **"Graph engineering" is not a term of art.** Verified negatively against LangGraph's own docs, OpenAI's Agents SDK docs, and the absence of any primary usage anywhere.
- **"Scaffold" was the 2024 name for the agent harness.** Verified by word-count against two primary artifacts: OpenAI's SWE-bench Verified post (Aug 2024) and METR's elicitation guidelines (Mar 2024, "scaffold" x11 vs "harness" x0).
- **The eval-harness / agent-harness distinction**, verified against Anthropic's own back-to-back definitions (9 Jan 2026), the SWE-bench repo's first commit (10 Oct 2023), and de Macedo's paper.
- **The Agent Skills specification contents** — read field by field from agentskills.io/specification.
- **Agent Skills is NOT AAIF-governed**, contra several secondary sources — verified against both the site and the GitHub repo. AGENTS.md and MCP *are*.
- **No autonomy-levels standard exists**, verified negatively against NIST AI RMF (3 occurrences of "autonom*", no levels), ISO/IEC 22989, IEEE P3394, SAE, and the EU AI Act. Plus the positive proof of non-convergence: DeepMind and Feng et al. swap "Consultant" and "Collaborator" between levels.
- **"loop" appears zero times in DoDD 3000.09 (both 2012 and 2023), the EU AI Act, the NIST AI RMF, UK MoD JCN 1/18, and the ICRC/US CCW commentaries.** Independently confirmed. The 2023 DoDD reissue additionally renamed *human-supervised* to *operator-supervised*.
- **HOTL origin: USAF, 18 May 2009.** Trichotomy origin: **HRW, 19 Nov 2012, p. 2** — both verified verbatim from the primary documents.
- **Karpathy does not say vibe coding is dead** — verified verbatim against his own blog. The press framing is wrong.
- **OpenAI deprecated SWE-bench Verified on 23 Feb 2026** for benchmark contamination.
- **Anthropic's telemetry: ~93% of Claude Code permission prompts were approved**, published by Anthropic itself.

### Medium confidence
- **Exact dates of the June 2025 Lütke and Karpathy tweets.** x.com returns HTTP 402 to automated fetch. The *wording* is high-confidence (quoted verbatim and identically by Willison, Schmid and LangChain); the dates vary by one day across sources.
- **OpenAI's harness-engineering post content.** openai.com returns HTTP 403. Existence, title and date are certain; the specific quotes should be re-verified in a browser before publication. ⚠️ One quote circulating in coverage ("We built Harness to provide a consistent and reliable way to run large-scale AI workloads") reads as though it describes an OpenAI *infrastructure product* rather than the discipline — **do not use it.**
- **MCP spec revision lineage.** Both ends are primary-confirmed; the middle revisions rest on secondary timelines.
- **Attribution of "harness engineering."** Anthropic is first for the noun (Nov 2025), Hashimoto first for the phrase (Feb 2026), Trivedy first for the derivation (Mar 2026). Wikipedia records it as contested and misses the Anthropic use.
- **Vendor tooling launch dates** (Braintrust, LangSmith, Weave, Guardrails AI founding) — `[SECONDARY]`.

### Low confidence / could not establish
- **Whether any high-profile named practitioner argues forcefully that context engineering is merely a rebrand.** Widely reported, no strong primary artifact. Do not write "critics say X" without a name.
- **The claim that Dex Horthy coined "context engineering."** Asserted in a secondary source; no supporting primary artifact; Lütke's tweet predates any Horthy usage located.
- **A formal standards definition of "test harness."** IEEE Std 610.12-1990 is paywalled; the ISTQB glossary is JS-rendered. **Do not assert one.**
- **Any pre-1961 "man-in-the-loop" origin.** DTIC (HTTP 403) and HathiTrust (Cloudflare 403) are the corpora that would settle it; neither was accessible and neither was circumvented. Safe wording: *"in use in US aerospace and flight-control engineering by the early 1960s; no identifiable coiner."*
- **The Wiener → Licklider → HITL genealogy is folk etymology.** Licklider's *Man-Computer Symbiosis* (1960) is real but does not use the phrase. Do not cite it as origin.
- **The eval/benchmark distinction has no authoritative primary source.** The best statement is an independent practitioner site (Brenn Hill, Jun 2026). **Do not attribute it to Hamel Husain** — his 2024 post never uses the word "benchmark."
- **No named researcher has published a direct critique of the *word* "guardrails" as marketing.** All published criticism targets efficacy. The terminological case is strong but circumstantial (AWS's rename notice; Meta's and Microsoft's avoidance; OpenAI's two incompatible uses).
- **ISO/IEC 42105** (*Guidance for human oversight of AI systems*) is unpublished and paywalled. Closest thing to a future standard in this area; watch it.
- **NIST ARIA's own definition of "evaluation"** — the plan PDF would not text-extract.
- **WebMCP's W3C status.** No w3.org primary reached.
- **The RL/robotics sense of "skill."** Asserted from background knowledge, not sourced in this pass.
- **Spec-driven development's coinage.** No primary artifact found; efficacy claims are unverified and vendor-adjacent.
- **Andrew Ng's "agent-like to different degrees" rationale quote.** Reached via search snippet only; verify before quoting.
- **OpenAI's "five levels" (Chatbots → Reasoners → …)** — reported by Bloomberg from an internal all-hands; **not published on openai.com**. Do not cite as an OpenAI publication.

### Blocked sources (stated for auditability — none circumvented)
`openai.com` (HTTP 403 to automated fetch), `x.com` (HTTP 402), `apps.dtic.mil` (403), HathiTrust (Cloudflare 403), `esd.whs.mil` (403 — DoDD 3000.09 2023 came from an Internet Archive capture), `iso.org` (403 — ISO/IEC 22989 verified via the official iTeh preview PDF), IEEE Xplore (paywalled), ISTQB glossary (JS-rendered), Medium (403 on some posts).

### Things this project will need to reckon with
1. **The eval-harness / agent-harness collision is not cosmetic, and it has a number attached.** Claw-SWE-Bench measures harness choice moving Pass@1 by 27.4 points against 29.4 for model choice; The Scaffold Effect measures up to a **40× difference in tokens per solved task** from harness choice alone. A headline like "model X resolves N% of SWE-bench" is a joint measurement. Any document citing agent benchmark scores without naming the harness is making a claim it cannot support.
2. **Several widely-cited numbers are dead.** OpenAI stopped reporting SWE-bench Verified on 23 Feb 2026 for contamination, and independent work (UTBoost, ACL 2025) had already found 24.4% of its leaderboard entries affected by mislabelled patches. Purge SWE-bench Verified scores from any draft.
3. **"Open standard" means three different things here.** MCP and AGENTS.md are foundation-governed (AAIF/Linux Foundation). Agent Skills is openly published with open contribution but **no neutral governance**. WebMCP is on an actual W3C track. The field uses one phrase for all three.
4. **"Human-in-the-loop" is doing reassurance work it cannot support** — and the vendor best placed to know published the number: **93% approval rate**, which is Thurnher's 2012 "rubber stamp," measured. Bainbridge predicted exactly this in 1983, 26 years before the USAF coined "on the loop." The field's own replacement move is **containment over supervision** — restrict what the agent *can* do rather than approving what it *does*. That is the same conclusion Willison reaches about guardrails and the same one the lethal trifecta implies.
5. **The concept is older than the name, twice over.** Harness engineering was called *scaffolding* through 2024. Autonomy levels descend from Sheridan & Verplank (1978), 36 years before SAE J3016. Treat "new discipline" claims with suspicion; usually something got renamed and sharpened.
6. **"Agentic" won three separate naming contests independently** — the enterprise category, the successor to vibe coding, and the name of the foundation governing the protocols. It is simultaneously the most-used and most-derided adjective in the field, and Ng introduced it in Mar 2024 specifically to *end* definitional fights.
7. **This vocabulary is moving at roughly one major new term per quarter.** Harness engineering went from a single personal blog post to Wikipedia in under three months. Carry a dated "as of" and expect revision.
