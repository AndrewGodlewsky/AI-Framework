# IP and Copyright in Agent-Authored Code

**Research date:** 2026-08-30
**Ticket:** [#7 Governance, Legal & IP by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/7) — strand: IP and copyright in agent-authored code
**Question:** Who owns agent-authored code, is it copyrightable at all, and how does the answer change with how much human authorship is present — and by jurisdiction?

> ## ⚠️ This is research, not legal advice.
>
> Nothing here is legal advice, and nothing here creates a lawyer-client relationship. It is a
> reading of primary sources — statutes, regulations, court judgments and official agency
> guidance — assembled to inform an engineering-governance document. Copyright in AI output is
> **actively unsettled in every jurisdiction examined**, three of the four positions surveyed are
> under live consultation, appeal or revision, and the position for *code specifically* has never
> been ruled on anywhere. A company deciding what to do about this needs its own counsel, on its
> own facts, in its own jurisdictions. Treat every paragraph below as a pointer to a primary text
> you should read rather than a conclusion you can rely on.

**Method.** Primary sources only as the source of any claim: statute text, regulation text, court
judgments, and official agency guidance documents, read directly from the issuing body's own site
(copyright.gov, legislation.gov.uk, gov.uk, eur-lex.europa.eu, curia, uspto.gov, govinfo.gov,
japaneselawtranslation.go.jp, bunka.go.jp, english.bjinternetcourt.gov.cn, media.cadc.uscourts.gov).
PDFs were converted with `pdftotext` and quoted from the converted text, not from a summariser —
one subagent found a summarising model materially mis-stating a statutory provision twice, and that
is logged. Law-firm and trade commentary was used only to *locate* primary texts and is labelled
wherever it appears. Everything is dated. Blocked sources are logged at the foot and none was
circumvented.

**Evidence tier is stated with every claim**, per [`CONTEXT.md`](../CONTEXT.md). The scale used here:

| Tier | Meaning |
|---|---|
| **[STATUTE]** | Enacted legislative text. Binding. |
| **[RULING]** | A court judgment. Binding within its jurisdiction, to the extent of its actual holding. |
| **[AGENCY GUIDANCE]** | An administrative body's stated interpretation. **Not binding on a court.** Persuasive, and decisive in practice for anything that agency administers. |
| **[AGENCY ADJUDICATION]** | An agency decision on specific facts — e.g. a refusal of registration. Fact-bound; not a rule. |
| **[GOVERNMENT PROPOSAL]** | A published intention to change the law. **Not law.** |
| **[CONTRACT]** | A vendor's own terms. Binds the parties, cannot create rights that do not exist. |
| **[PRACTITIONER ARTIFACT]** | A project's committed policy. Evidence of practice, not of law. |
| **[NEGATIVE FINDING]** | Established absence: searched for, not found. Reported because the absence is the finding. |

---

## Headline findings

1. **The single most-repeated claim in this area is wrong, and the primary text says so in terms.**
   *Thaler v. Perlmutter* is routinely reported as holding that AI-generated works cannot be
   copyrighted. The D.C. Circuit held something much narrower — that **a machine cannot be named as
   the author** — and went out of its way to say the opposite of the popular gloss:
   *"the human authorship requirement does not prohibit copyrighting work that was made by or with
   the assistance of artificial intelligence."* It expressly declined to reach whether Thaler
   himself was the author, because he had waived it. **[RULING]** This is the same failure mode the
   project already recorded for AI contribution policies in
   [`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md) — nuanced regimes
   reported as flat bans. It recurs here exactly.

2. **The US threshold is control over expressive elements, not effort, and not approval.** The
   Copyright Office's position is that *"prompts alone do not provide sufficient human control"*,
   that revising prompts hundreds of times changes nothing because it is *"re-rolling the dice"*,
   and — the finding that matters most for agentic engineering — that **selecting and accepting a
   generated output is not authorship**: *"the final output reflects the user's acceptance of the AI
   system's interpretation, rather than authorship of the expression it contains."* **[AGENCY
   GUIDANCE]** Three things *do* cross the threshold: human-authored expression **perceptible** in
   the output, **creative selection/coordination/arrangement** of outputs, and **modification** of
   an output that is itself original.

3. **Nothing is tainted.** Unprotectable AI-generated code does not infect the human-authored code
   around it. The Office states it directly: *"the inclusion of elements of AI-generated content in
   a larger human-authored work does not affect the copyrightability of the larger human-authored
   work as a whole."* **[AGENCY GUIDANCE]**, reinforced by [17 U.S.C. § 103(b)](https://www.copyright.gov/title17/92chap1.html)
   **[STATUTE]**. The repository does not become public domain because an agent wrote part of it.

4. **The practical bite is at enforcement, not at existence.** US copyright vests automatically, but
   you cannot sue without registration ([§ 411(a)](https://www.copyright.gov/title17/92chap4.html)),
   registration carries a **duty to disclose and disclaim AI-generated material that is more than
   de minimis** ([88 FR 16190](https://www.copyright.gov/ai/ai_policy_guidance.pdf)), and a
   knowingly inaccurate registration can be disregarded by a court (§ 411(b)) or cancelled by the
   Office — which is exactly what happened to *Zarya of the Dawn*. **[STATUTE]** + **[AGENCY
   ADJUDICATION]**. **The question a company will actually be asked is not "do we own it" but "can
   you tell us which lines a human wrote".**

5. **Trade secret is untouched by any of this, and is the strongest fallback for closed source.**
   [18 U.S.C. § 1839(3)](https://www.law.cornell.edu/uscode/text/18/1839) protects *"programs, or
   codes"* as **information**, conditioned on reasonable secrecy measures and independent economic
   value — **there is no author, no originality requirement and no human anywhere in the
   definition.** **[STATUTE]** The EU Trade Secrets Directive is drafted the same way. The
   authorship problem simply does not arise. It fails, though, for anything published — which is
   most open source and any code disclosed in diligence.

6. **The assignment machinery does not reach output that has no author — and the D.C. Circuit said
   so expressly.** *Thaler* rejected the work-made-for-hire argument on the ground that
   *"the human-authorship requirement necessitates that all 'original works of authorship' be
   created in the first instance by a human being, including those who make work for hire."*
   **[RULING]** [§ 201(a)](https://www.copyright.gov/title17/92chap2.html) vests copyright in the
   author; if there is no author there is nothing to vest, nothing to assign, and a CLA warranty of
   ownership that cannot be truthfully given. This is not theoretical: **OpenJDK's ban is expressly
   grounded in it** — *"The Oracle Contributor Agreement (OCA) requires that a contributor own the
   intellectual property rights in each contribution… contributing such content would violate the
   OCA."* **[PRACTITIONER ARTIFACT]**

7. **Jurisdictions do not merely differ in emphasis — they reach opposite results on the same
   facts.** A user who ran four generations with a long, largely copied prompt string **won**
   copyright in China (*Li v. Liu*, 2023). A user who ran *"hundreds or thousands of descriptive
   prompts"* over a year (*Zarya*) and one who ran **624** (*Théâtre D'opéra Spatial*) both **lost**
   in the US. Japan's guidance says a large number of attempts and mere selection among outputs each
   count for **nothing**. **A team shipping globally inherits the strictest, and as of 2026-08-30
   the strictest is the United States.**

8. **The UK is the outlier, and it is mid-repeal.** [CDPA 1988 s.9(3)](https://www.legislation.gov.uk/ukpga/1988/48/section/9)
   deems the author of a computer-generated work to be *"the person by whom the arrangements
   necessary for the creation of the work are undertaken"* — and the UK government's own March 2026
   report says that for a prompted AI output *"the 'author' will usually be the person who inputted
   the prompt."* **[STATUTE]** + **[GOVERNMENT PROPOSAL]**. But the same report proposes to
   **remove** the provision. It is still in force, unamended, with no outstanding effects recorded.
   **Anyone relying on s.9(3) is relying on a right its own government has published an intention to
   abolish.**

9. **Two US federal agencies now give opposite answers on prompts — and the patent side moved
   *toward* the AI user in November 2025 while the copyright side stood still.** The USPTO's
   revised guidance ([90 FR 54636](https://www.govinfo.gov/content/pkg/FR-2025-11-28/pdf/2025-21457.pdf),
   2025-11-28) **rescinded its February 2024 AI guidance in its entirety** and now says AI systems
   *"are instruments used by human inventors. They are analogous to laboratory equipment, computer
   software, research databases, or any other tool"* — while the Copyright Office's position is that
   the AI system *originates* the traditional elements of authorship. **[AGENCY GUIDANCE]** These
   are different statutes and different doctrines, so they are not formally in conflict; but as a
   signal about how US agencies characterise generative AI they point in opposite directions, in the
   same eighteen months.

10. **The US record has been frozen since January 2025.** Part 2 promised *"additional registration
    guidance and an update to the Compendium"* — **neither has issued.** Compendium §§ 306 and 313.2
    still read as written **2021-01-28**, resting on a 1965 Register's report, a monkey and an
    elephant. Part 3 has been a *"pre-publication version"* for 15 months. Part 4 is promised in
    three footnotes and does not exist. No AI registration decision has been added in over two and a
    half years. **[NEGATIVE FINDING]** Meanwhile the Register of Copyrights has been in APA
    litigation against the Acting Librarian since 2025-05-22, still pending on appeal. The
    correlation is on the face of the official record; no causal claim is made.

11. **Code is almost entirely absent from the sources.** In the Copyright Office's 41-page
    copyrightability report, code appears **once**, in a footnote, and it points the *other* way —
    citing Apple's comment that programmers use *"automated tools to modify software code, such as to
    perform refactoring and translate from one programming language into another"* as an example of
    an **assistive** use that *"should not affect the availability of copyright protection for the
    output."* Circular 61, the Office's own guidance for registering computer programs, was last
    revised **3/2021** and does not mention AI. **No court anywhere has ruled on the copyrightability
    of AI-generated source code** — including in China, where three independent lines of search,
    including the Supreme People's Court IP Tribunal's own survey, found nothing. **[NEGATIVE
    FINDING]**

12. **⚠️ On the autonomy axis, the direction is supported and the mapping is not.** The Office says
    once, in a single sentence, that *"technological advancements that facilitate increased
    automation and optimization may bolster our current conclusions… users' control may be
    diminished."* That is the only place any source connects degree of automation to the authorship
    threshold, and it is about automated prompt optimisation, not agents. **No source anywhere
    distinguishes a developer accepting an inline completion from one merging an unread agent PR.**
    The doctrine that *would* separate them exists — control over expressive elements — but nobody
    has applied it to a coding workflow. **The silence is the finding.** The only artifact in the
    entire corpus that draws the line the ticket is asking about is a practitioner one:
    [Godot's contribution policy](https://contributing.godotengine.org/en/latest/pull_requests/pull_request_guidelines.html)
    permits AI *"for code completion"* while forbidding it to *"author"* code, defining authoring as
    *"making decisions about where the code should go, what techniques/algorithms should be used, and
    ultimately what the code should look like."* **[PRACTITIONER ARTIFACT]** That is a remarkably
    close restatement of the Copyright Office's control-over-expressive-elements test, arrived at
    independently by a game engine project.

---

## 1. The United States

### 1.1 The statutory floor

Three provisions do the work, and none of them mentions AI.

- **[STATUTE]** [17 U.S.C. § 102(a)](https://www.copyright.gov/title17/92chap1.html): *"Copyright
  protection subsists… in original works of authorship fixed in any tangible medium of expression."*
  A *"computer program"* is *"a set of statements or instructions to be used directly or indirectly
  in a computer in order to bring about a certain result"* (§ 101) — protected as a literary work.
- **[STATUTE]** § 102(b): *"In no case does copyright protection for an original work of authorship
  extend to any idea, procedure, process, system, method of operation, concept, principle, or
  discovery."* This matters independently of AI: much of what an agent produces is functionally
  determined and would be thinly protected or unprotected however it was written.
- **[STATUTE]** [§ 201(a)](https://www.copyright.gov/title17/92chap2.html): *"Copyright in a work
  protected under this title vests initially in the author or authors of the work."*

The human-authorship requirement is **not** in the statute. It is derived — from *Burrow-Giles
Lithographic Co. v. Sarony*, 111 U.S. 53 (1884), the *Trade-Mark Cases*, 100 U.S. 82 (1879), and
the structure of the 1976 Act. That derivation is now blessed by the D.C. Circuit (§ 1.2) and stated
as agency rule in the Compendium (§ 1.3).

### 1.2 What *Thaler v. Perlmutter* actually held

**[RULING]** [*Thaler v. Perlmutter*, No. 23-5233 (D.C. Cir.)](https://media.cadc.uscourts.gov/opinions/docs/2025/03/23-5233.pdf),
argued 2024-09-19, **decided 2025-03-18**. Millett, Wilkins, and Rogers (Senior); opinion by Millett.

The holding, in the court's own summary:

> "We affirm the denial of Dr. Thaler's copyright application. The Creativity Machine cannot be the
> recognized author of a copyrighted work because the Copyright Act of 1976 requires all eligible
> work to be authored in the first instance by a human being. **Given that holding, we need not
> address the Copyright Office's argument that the Constitution itself requires human authorship of
> all copyrighted material. Nor do we reach Dr. Thaler's argument that he is the work's author by
> virtue of making and using the Creativity Machine because that argument was waived before the
> agency.**"

**Four limits on that holding, from the opinion itself.** These are what press coverage drops.

1. **It is about naming a machine as author, nothing else.**
   > "Dr. Thaler listed the Creativity Machine as the sole author of the work before us, and it is
   > undeniably a machine, not a human being. Dr. Thaler, in other words, **argues only for the
   > copyrightability of a work authored exclusively by artificial intelligence.**"

2. **The court expressly denied the broad reading.**
   > "First, **the human authorship requirement does not prohibit copyrighting work that was made by
   > or with the assistance of artificial intelligence. The rule requires only that the author of
   > that work be a human being — the person who created, operated, or used artificial intelligence —
   > and not the machine itself.** The Copyright Office, in fact, has allowed the registration of
   > works made by human authors who use artificial intelligence."

3. **It refused to draw the line this ticket is about.**
   > "**Those line-drawing disagreements over how much artificial intelligence contributed to a
   > particular human author's work are neither here nor there in this case.**"

   It also noted, without endorsing, that the Office's approach has critics, quoting the amicus law
   professors: *"The U.S. Copyright Office guidelines are somewhat paradoxical: human contributions
   must be demonstrated within the creative works generated by AI."*

4. **It decided no constitutional question.**
   > "Because the Copyright Act itself requires human authorship, we need not and do not address the
   > Copyright Office's argument that the Constitution's Intellectual Property Clause requires human
   > authorship."

**Also expressly held, and directly on this ticket's fourth question** — work-made-for-hire does not
supply an author:

> "That argument misunderstands the human authorship requirement. The Copyright Act only protects
> 'original works of authorship.' 17 U.S.C. § 102(a). **The authorship requirement applies to all
> copyrightable work, including work-made-for-hire.** The word 'authorship,' like the word 'author,'
> refers to a human being. As a result, the human-authorship requirement necessitates that all
> 'original works of authorship' be created in the first instance by a human being, **including
> those who make work for hire.**"

**Status as of 2026-08-30 — unsettled.** Panel rehearing and rehearing en banc were both denied
(both orders listed on [copyright.gov/ai](https://www.copyright.gov/ai/)). A petition for certiorari
was filed as **No. 25-449 on 2025-10-09**; the government filed a brief in opposition; a reply brief
was filed **2026-02-09**; petitioner's counsel asked the Court to **hold** the petition pending
related litigation. **No grant or denial appears in any record reachable here** — the Supreme Court
docket is blocked to automated fetch (logged below). Treat the petition as pending and the next
event as unscheduled.

### 1.3 The human-authorship threshold, stated precisely

Three documents, in ascending order of specificity.

**(a) [AGENCY GUIDANCE] Compendium of U.S. Copyright Office Practices (3d ed.), effective
2021-01-28.** [§ 306](https://www.copyright.gov/comp3/chap300/ch300-copyrightable-authorship.pdf):

> "The U.S. Copyright Office will register an original work of authorship, provided that the work
> was created by a human being."

§ 313.2, the operative sentence:

> "Similarly, the Office will not register works produced by a machine or mere mechanical process
> that operates randomly or automatically without any creative input or intervention from a human
> author. The crucial question is 'whether the "work" is basically one of human authorship, with the
> computer [or other device] merely being an assisting instrument, or whether the traditional
> elements of authorship in the work (literary, artistic, or musical expression or elements of
> selection, arrangement, etc.) were actually conceived and executed not by man but by a machine.'"

The inner quotation is from the **Register's 1965 Report to the Librarian of Congress**. The
governing administrative test for AI-generated code is a sentence written sixty-one years ago about
mainframes, illustrated by examples that are all pre-generative (resizing an image, VHS→DVD
conversion, transposing a song, MRI output, a random weaving process), sitting next to a monkey
photograph and an elephant mural. **[NEGATIVE FINDING]** It has not been revised (§ 1.6).

**(b) [AGENCY GUIDANCE] Registration Guidance, [88 FR 16190](https://www.copyright.gov/ai/ai_policy_guidance.pdf),
published 2023-03-16, dated 2023-03-10, effective 2023-03-16.** Its legal status matters and is
stated on its face: **"ACTION: Statement of policy"** under 37 CFR Part 202. It is not a legislative
rule, and it does not bind a court.

The rule:

> "When an AI technology determines the expressive elements of its output, the generated material is
> not the product of human authorship. As a result, that material is not protected by copyright and
> **must be disclaimed in a registration application.**"

The other side of it:

> "For example, a human may select or arrange AI-generated material in a sufficiently creative way
> that 'the resulting work as a whole constitutes an original work of authorship.' Or an artist may
> modify material originally generated by AI technology to such a degree that the modifications meet
> the standard for copyright protection. **In these cases, copyright will only protect the
> human-authored aspects of the work, which are 'independent of' and do 'not affect' the copyright
> status of the AI-generated material itself.**"

And, explicitly, tools are fine:

> "This policy does not mean that technological tools cannot be part of the creative process… what
> matters is **the extent to which the human had creative control over the work's expression** and
> 'actually formed' the traditional elements of authorship."

**The applicant's duties**, verbatim:

> "applicants have a **duty to disclose** the inclusion of AI-generated content in a work submitted
> for registration and to provide a brief explanation of the human author's contributions to the
> work."

> "**AI-generated content that is more than de minimis should be explicitly excluded from the
> application.** This may be done in the 'Limitation of the Claim' section in the 'Other' field,
> under the 'Material Excluded' heading."

> "Applicants should not list an AI technology or the company that provided it as an author or
> co-author simply because they used it when creating their work."

**The consequence of not disclosing** — this is the enforcement hinge:

> "Applicants who fail to update the public record after obtaining a registration for material
> generated by AI **risk losing the benefits of the registration.** If the Office becomes aware that
> information essential to its evaluation of registrability 'has been omitted entirely from the
> application or is questionable,' **it may take steps to cancel the registration.** Separately, a
> court may disregard a registration in an infringement action pursuant to section 411(b) of the
> Copyright Act if it concludes that the applicant knowingly provided the Office with inaccurate
> information, and the accurate information would have resulted in the refusal of the registration."

**(c) [AGENCY GUIDANCE] *Copyright and Artificial Intelligence, Part 2: Copyrightability*, published
2025-01-29**, signed by Register Shira Perlmutter
([PDF](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)).
The eight conclusions, verbatim:

> - "Questions of copyrightability and AI can be resolved pursuant to existing law, without the need
>   for legislative change.
> - The use of AI tools to assist rather than stand in for human creativity does not affect the
>   availability of copyright protection for the output.
> - Copyright protects the original expression in a work created by a human author, even if the work
>   also includes AI-generated material.
> - Copyright does not extend to purely AI-generated material, **or material where there is
>   insufficient human control over the expressive elements.**
> - Whether human contributions to AI-generated outputs are sufficient to constitute authorship must
>   be analyzed on a case-by-case basis.
> - **Based on the functioning of current generally available technology, prompts do not alone
>   provide sufficient control.**
> - Human authors are entitled to copyright in their works of authorship that are **perceptible** in
>   AI-generated outputs, as well as the creative **selection, coordination, or arrangement** of
>   material in the outputs, or creative **modifications** of the outputs.
> - The case has not been made for additional copyright or sui generis protection for AI-generated
>   content."

**So the threshold, stated as precisely as the sources allow:**

| Human contribution | Protected? | Source |
|---|---|---|
| Prompt only, however detailed | **No** | Part 2 § II.D.2 |
| Prompt revised hundreds of times | **No** | Part 2 § II.D.2; *Zarya*; *Théâtre* |
| Selecting the best of N outputs | **No** | Part 2 § II.D.2 |
| Choosing a numeric parameter (e.g. style strength) | **No** | *SURYAST* |
| Supplying your own copyrightable work as input, **where it remains perceptible in the output** | **Yes — as to that perceptible portion** | Part 2 § II.E; *Rose Enigma* |
| Supplying your own copyrightable work as input, where it is **consumed and re-rendered** | **No** | *SURYAST* |
| Creative selection/coordination/arrangement of AI outputs | **Yes — as a compilation, over the whole, not the parts** | Part 2 § II.F; *Zarya* |
| Modifying an AI output enough to be original in its own right | **Yes — as to the modifications** | Part 2 § II.F; 88 FR 16190 |
| Using AI as an assistive tool where the human determines the expression | **Yes — unaffected** | Part 2 § II.C; 88 FR 16190 |

Note what the middle rows mean for code review: **perceptibility and separability**, not effort, is
the operative criterion. The Office registered *Rose Enigma* with the annotation *"Registration
limited to unaltered human pictorial authorship that is **clearly perceptible in the deposit and
separable** from the non-human expression that is excluded from the claim."* A codebase where an
agent wrote the implementation and a human wrote the interfaces has a cleaner separability story
than one where a human edited an agent's diff line by line — which is the opposite of the intuition
most teams hold.

### 1.4 How prompts are treated — the reasoning, not just the rule

**[AGENCY GUIDANCE]** Part 2 § II.D.2 is the most directly transferable analysis in the whole corpus,
because prompting an agent is what agentic engineering *is*.

> "The Office concludes that, given current generally available technology, prompts alone do not
> provide sufficient human control to make users of an AI system the authors of the output.
> **Prompts essentially function as instructions that convey unprotectible ideas.** While highly
> detailed prompts could contain the user's desired expressive elements, at present they do not
> control how the AI system processes them in generating the output."

The joint-authorship analogy — and this is the passage most worth reading twice if you manage an
agent fleet:

> "The provision of detailed directions, **without influence over how those directions are
> executed**, is insufficient. As the Third Circuit explained, when a person hires someone to execute
> their expression, 'that process must be **rote or mechanical transcription** that does not require
> intellectual modification or highly technical enhancement' for the delegating party to claim
> copyright authorship in the final work… **In theory, AI systems could someday allow users to exert
> so much control over how their expression is reflected in an output that the system's contribution
> would become rote or mechanical. The evidence as to the operation of today's AI systems indicates
> that this is not currently the case.**"

On iteration — the finding that most directly contradicts how practitioners talk about their craft:

> "**Repeatedly revising prompts does not change this analysis…** First, the time, expense, or effort
> involved in creating a work by revising prompts is irrelevant, as copyright protects original
> authorship, not hard work or 'sweat of the brow.' Second, inputting a revised prompt does not
> appear to be materially different in operation from inputting a single prompt. **By revising and
> submitting prompts multiple times, the user is 're-rolling' the dice**, causing the system to
> generate more outputs from which to select, but not altering the degree of control over the
> process. **No matter how many times a prompt is revised and resubmitted, the final output reflects
> the user's acceptance of the AI system's interpretation, rather than authorship of the expression
> it contains.**"

On selection — **the passage that matters most for merge-based workflows**:

> "The Office also agrees that **authorship by adoption does not in itself provide a basis for
> claiming copyright in AI-generated outputs.** As commenters noted, **providing instructions to a
> machine and selecting an output does not equate to authorship.** Selecting an AI-generated output
> among uncontrolled options is more analogous to curating a 'living garden,' than applying
> splattered paint… 'selection among the offered options' produced by such a system cannot be
> considered copyrightable authorship, because the 'selection of a single output is not itself a
> creative act.'"

Read that against a code review workflow. A reviewer who reads an agent's PR, decides it is good, and
merges it, has — on the Office's own framing — *adopted* an output. Adoption is not authorship. This
is the single most consequential sentence in the corpus for this ticket, and **the Office was not
thinking about code when it wrote it.**

The counterweight, from the *same* report — assistive use, and the only place code appears:

> "The Office agrees that there is an important distinction between **using AI as a tool to assist in
> the creation of works and using AI as a stand-in for human creativity.** While assistive uses that
> enhance human expression do not limit copyright protection, uses where an AI system makes
> expressive choices require further analysis. **This distinction depends on how the system is being
> used, not on its inherent characteristics.**"

The footnote (n.62) supporting that paragraph, citing Apple's NOI comment:

> "In the software industry, programmers and computer engineers use automated tools to modify
> software code, such as **to perform refactoring and translate from one programming language into
> another.**"

And the surrounding text: *"Commenters argued that these types of uses of AI should not affect the
availability of copyright protection for the output"* — with the Office agreeing. **This is the only
code-specific statement in the report, and it is favourable.** An agent that refactors or translates
existing human-authored code is on the assistive side of the line the Office drew; an agent that
originates a module is not.

### 1.5 The registration decisions

Four exist. All are 2022–2023. **[NEGATIVE FINDING]** None has been added since; none concerns code.

**[AGENCY ADJUDICATION] *Zarya of the Dawn*** — letter from Robert J. Kasunic, Associate Register, to
counsel, **2023-02-21** ([PDF](https://www.copyright.gov/docs/zarya-of-the-dawn.pdf)). Registration
VAu001480196 **cancelled** and reissued narrower.

> "We conclude that Ms. Kashtanova is the author of the Work's text as well as the selection,
> coordination, and arrangement of the Work's written and visual elements. That authorship is
> protected by copyright. However… **the images in the Work that were generated by the Midjourney
> technology are not the product of human authorship.**"

The new certificate's annotation reads: *"VAU001480196 cancelled pursuant to 37 CFR 201.7(c)(4) for
**failure to exclude non-human authorship**."*

The effort finding — and the number:

> "To obtain the final image, she describes a process of trial-and-error, in which she provided
> **'hundreds or thousands of descriptive prompts'** to Midjourney until the 'hundreds of iterations
> [created] as perfect a rendition of her vision as possible.'"

> "The Office does not question Ms. Kashtanova's contention that she expended significant time and
> effort working with Midjourney. **But that effort does not make her the 'author' of Midjourney
> images under copyright law.** Courts have rejected the argument that 'sweat of the brow' can be a
> basis for copyright protection in otherwise unprotectable material."

Two Photoshop edits were assessed separately, and the split is instructive:
- Lips/mouth on page 2 — **not enough**: *"too minor and imperceptible to supply the necessary
  creativity for copyright protection."*
- The aged face on page 12 — **undetermined, and not excluded**: *"the Office cannot determine what
  expression in the image was contributed through her use of Photoshop as opposed to generated by
  Midjourney… To the extent that Ms. Kashtanova made substantive edits to an intermediate image
  generated by Midjourney, those edits could provide human authorship and would not be excluded."*

That second bullet is the registration system's version of a provenance problem. **The Office did not
refuse; it could not tell.** Substitute "which lines in this file did the human write" and you have
the practical question a company will face.

**[AGENCY ADJUDICATION] *Théâtre D'opéra Spatial*** — Copyright Review Board, **2023-09-05**
([PDF](https://www.copyright.gov/rulings-filings/review-board/docs/Theatre-Dopera-Spatial.pdf)).
Wilson, Strong, Rubel.

Jason Allen's own account, quoted by the Board: he *"input numerous revisions and text prompts **at
least 624 times** to arrive at the initial version of the image."*

The Board:

> "In the Board's view, Mr. Allen's actions as described do not make him the author of the Midjourney
> Image because **his sole contribution to the Midjourney Image was inputting the text prompt that
> produced it.** Although Mr. Allen describes 'input[ing] numerous revisions and text prompts at
> least 624 times' before producing the Midjourney Image, … the steps in that process were ultimately
> dependent on how the Midjourney system processed Mr. Allen's prompts."

> "The Board acknowledges that the process of prompting can involve creativity — after all, 'some
> prompts may be sufficiently creative to be protected by copyright' as literary works. **But that
> does not mean that providing text prompts to Midjourney 'actually form[s]' the generated images.**"

**And the reason the application failed is procedural, not substantive** — a distinction almost
universally lost in coverage:

> "**Because Mr. Allen has refused to limit his claim to exclude its non-human authorship elements,
> the Office cannot register the Work as submitted.**"

Footnote 13 keeps the door open: *"This decision does not foreclose Mr. Allen's ability to file a new
application for registration of the Work in which he disclaims the Work's AI-generated material."*
Allen instead sued — *Allen v. Perlmutter*, D. Colo. No. 1:24-cv-02665, filed 2024-09-26; still
listed as live litigation on copyright.gov.

**[AGENCY ADJUDICATION] *SURYAST*** — Copyright Review Board, **2023-12-11**
([PDF](https://www.copyright.gov/rulings-filings/review-board/docs/SURYAST.pdf)). The applicant fed
in **his own copyrighted photograph**, a style image (*The Starry Night*), and a style-strength
number. Refused:

> "**Because Mr. Sahni only provided these three inputs to RAHGAV, the RAGHAV app, not Mr. Sahni, was
> responsible for determining how to interpolate the base and style images…** But Mr. Sahni did not
> control where those elements would be placed, whether they would appear in the output, and what
> colors would be applied to them — RAGHAV did."

> "While Mr. Sahni selected the numerical variable for the 'strength' of the style, **that choice
> alone is insufficient to warrant copyright protection.**"

The Board also rejected the "it's just a tool" framing in terms worth carrying over to agent
harnesses:

> "The Board is not convinced by Mr. Sahni's description of RAGHAV as 'an assistive tool' that works
> similarly to 'a camera, digital tablet, or a photo-editing software program.' … **This description
> inaccurately minimizes RAGHAV's role in the creation of the Work and conflicts with other
> information in the record.**"

**The contrast with *Rose Enigma* is the whole test.** Registration VAu001528922 (2023-03-21) was
**granted** where the applicant's hand-drawn illustration was used as an input and *"its expressive
elements are clearly perceptible in the output."* Part 2 n.124 draws the line explicitly: *"Unlike
Rose Enigma, the output did not clearly show the copyrightable work input by the applicant."*
**Supplying your own protected work as an input is not enough. It has to survive visibly into the
output.**

One quantitative datapoint, from *SURYAST* n.3 — **[AGENCY ADJUDICATION]**, the only number the
Office has published on this:

> "**In 2023 to date, the Copyright Office has granted approximately 100 applications to register
> works containing AI-generated material, where the AI-generated contributions are disclaimed.**"

The UK government's March 2026 report puts the running total higher: *"The USCO has registered
hundreds of works that incorporate some form of AI-generated material."* **[GOVERNMENT PROPOSAL]**
The system works. It just requires you to say what the machine did.

### 1.6 The record is frozen — a negative finding worth stating plainly

**[NEGATIVE FINDING]**, verified 2026-08-30 against copyright.gov, the Compendium PDF footer, the
Federal Register API, and the NewsNet archive.

Part 2 promised, twice:

> "It will also provide ongoing assistance to the public, including through **additional registration
> guidance and an update to the Compendium of U.S. Copyright Office Practices.**"

| Promised / expected | Status at 2026-08-30 |
|---|---|
| Updated Compendium | **Not issued.** copyright.gov/comp3 still reads *"This update is effective as of January 28, 2021."* Chapter 300 PDF footer still stamps `01/28/2021`. |
| Additional AI registration guidance | **Not issued.** Federal Register sweep of all 12 Copyright Office documents published since 2025-01-01 returned **none** AI-related. The operative guidance remains 88 FR 16190 (2023-03-16). |
| Part 3 final version | **Still "pre-publication."** Released 2025-05-09; every page of the body carries the running footer *"Pre-Publication Version."* The cover said *"A final version will be published in the near future"*; the live site now says *"in the future."* |
| Part 4 (infringing outputs, liability, transparency) | **Does not exist.** Promised in three separate Part 3 footnotes. Not listed, linked or announced. |
| New AI registration decisions | **None since 2023-12-11.** |
| AI registration FAQ | **Does not exist.** Zero occurrences of "artificial intelligence" on copyright.gov's FAQ or registration pages. |
| AI announcements | **Stop at 2025-01-29.** NewsNet is demonstrably live (latest issue No. 1091, 2026-08-13) and has carried **no** AI item since. |

Running alongside this, from federal court dockets (via a PACER mirror — **labelled: docket-mirror
service, not a .gov endpoint; underlying records are PACER primary records**): **Perlmutter v.
Blanche**, D.D.C. 1:25-cv-01659 (Judge Kelly), filed **2025-05-22**, nature of suit *"Administrative
Procedure Act/Review or Appeal of Agency Decision"* — the Register of Copyrights suing the Acting
Librarian of Congress, thirteen days after the Part 3 pre-publication release. Appealed to the D.C.
Circuit, **No. 25-5285, 2025-08-05**. **Both open and undecided at 2026-08-30**, while
copyright.gov's leadership page still lists Perlmutter as Register. *The correlation is on the face
of the official record. No causal claim is made, and I did not retrieve the complaint or any
opinion.*

**For a governance document, the operational consequence is the point:** the agency whose guidance
everyone is relying on has published nothing new on this subject in nineteen months, and the
administrative manual it applies predates ChatGPT.

### 1.7 ⚠️ Contrarian: two US agencies, opposite characterisations

This is a real finding and it needs careful framing. **Patent inventorship and copyright authorship
are different doctrines under different statutes; they are not formally in conflict.** But as a
signal about how the US federal government characterises generative AI, they diverge sharply, and
the divergence *widened* in the period the Copyright Office went quiet.

**[AGENCY GUIDANCE]** [USPTO, *Inventorship Guidance for AI-Assisted Inventions*, 89 FR 10043
(2024-02-13)](https://www.govinfo.gov/content/pkg/FR-2024-02-13/pdf/2024-02623.pdf) — the original
guidance said, in Principle 2:

> "Merely recognizing a problem or having a general goal or research plan to pursue does not rise to
> the level of conception. A natural person who only presents a problem to an AI system may not be a
> proper inventor… **However, a significant contribution could be shown by the way the person
> constructs the prompt in view of a specific problem to elicit a particular solution from the AI
> system.**"

Principle 3 mirrored the copyright modification rule almost exactly: *"a natural person who merely
recognizes and appreciates the output of an AI system as an invention… is not necessarily an
inventor. However, a person who takes the output of an AI system and makes a significant contribution
to the output to create an invention may be a proper inventor."*

Principle 5 is the one that speaks to fleet operators: *"a person simply **owning or overseeing** an
AI system that is used in the creation of an invention, without providing a significant contribution
to the conception of the invention, does not make that person an inventor."*

**Then it was withdrawn.** **[AGENCY GUIDANCE]** [90 FR 54636 (2025-11-28)](https://www.govinfo.gov/content/pkg/FR-2025-11-28/pdf/2025-21457.pdf):

> "**The guidance issued on February 13, 2024… is rescinded in its entirety.** The approach set forth
> in that guidance, which relied on the application of the Pannu factors to AI-assisted inventions,
> is withdrawn."

> "**The same legal standard for determining inventorship applies to all inventions, regardless of
> whether AI systems were used in the inventive process. There is no separate or modified standard
> for AI-assisted inventions.**"

> "**AI systems, including generative AI and other computational models, are instruments used by
> human inventors. They are analogous to laboratory equipment, computer software, research databases,
> or any other tool that assists in the inventive process.** As the case law establishes, inventors
> may 'use the services, ideas, and aid of others' without those sources becoming coinventors. The
> same principle applies to AI systems: **they may provide services and generate ideas, but they
> remain tools used by the human inventor** who conceived the claimed invention."

**Set that beside the Copyright Office's position that the AI system "originates the 'traditional
elements of authorship'" and "determines the expressive elements of its output."** The USPTO says
"lab equipment." The Copyright Office says "the master mind." Both are US federal agencies in 2026.

Both agencies do agree on the machine-as-inventor/author point: *Thaler v. Vidal*, 43 F.4th 1207
(Fed. Cir. 2022) **[RULING]** held *"that only a natural person can be an inventor, so AI cannot
be"* — and expressly reserved *"the question of whether inventions made by human beings with the
assistance of AI are eligible for patent protection."* Same reservation, same litigant, same
narrowness as the copyright case.

---

## 2. Jurisdictional divergence — the load-bearing part

### 2.1 United Kingdom — s.9(3), and the fact that it is mid-repeal

**[STATUTE]** [CDPA 1988 s.9(3)](https://www.legislation.gov.uk/ukpga/1988/48/section/9), unamended,
**no outstanding effects recorded** on legislation.gov.uk as at 2026-08-30:

> "In the case of a literary, dramatic, musical or artistic work which is computer-generated, the
> author shall be taken to be **the person by whom the arrangements necessary for the creation of the
> work are undertaken.**"

**[STATUTE]** [s.178](https://www.legislation.gov.uk/ukpga/1988/48/section/178): *"'computer-generated',
in relation to a work, means that the work is generated by computer **in circumstances such that
there is no human author of the work**."*

**[STATUTE]** [s.12(7)](https://www.legislation.gov.uk/ukpga/1988/48/section/12): *"If the work is
computer-generated the above provisions do not apply and copyright expires at the end of the period
of **50 years** from the end of the calendar year in which the work was made."*

**[STATUTE]** [s.11(2)](https://www.legislation.gov.uk/ukpga/1988/48/section/11): *"Where a literary,
dramatic, musical or artistic work, or a film, is made by an employee in the course of his
employment, **his employer is the first owner** of any copyright in the work subject to any agreement
to the contrary."* Note the UK vests **ownership**, not authorship, in the employer — structurally
different from US work-made-for-hire, which deems the employer the *author*. For a CGW the s.9(3)
deemed author supplies the missing link, and s.11(2) then routes ownership to the employer if that
person is an employee. That chain has never been litigated for AI.

**Who is the "arranger"?** The UK government answered this in its own words, in the March 2026 report
— **[GOVERNMENT PROPOSAL]**, and note this is the government's reading, not a court's:

> "In the case of a general-purpose AI which generates output in response to a user prompt, **the
> 'author' will usually be the person who inputted the prompt.**"

**That is a flat contradiction of the US position on identical facts.** Prompting gets you nothing in
Washington and everything in London.

**The originality contradiction.** The government's report states it squarely:

> "There appears to be **a legal contradiction within section 9(3)** which leads to uncertainty about
> its interpretation. This is because the provision applies only to literary, dramatic, musical, and
> artistic works **which are original**. The legal test for originality… is that a work must be an
> 'author's own intellectual creation' which is the expression of their creative choices and reflects
> their 'personal touch'. **This test is very much associated with human qualities, suggesting that a
> work created by a non-human could not be 'original'. However, section 9(3) only applies to works
> 'without a human author'.**"

> "This contradiction has led some to question whether the provision could ever apply in practice.
> **In our view, it is unlikely that a court would conclude that it can never apply**, as Parliament
> clearly intended the provision to have an effect. **But it is unclear in the absence of case law
> how an 'original' yet wholly machine-authored work would be defined.**"

The originality standard the report is describing is now settled in the UK, post-Brexit:
**[RULING]** [*THJ Systems Ltd v Sheridan* [2023] EWCA Civ 1354](https://caselaw.nationalarchives.gov.uk/ewca/civ/2023/1354)
(20 November 2023; Arnold, Asplin, Moylan LJJ) holds that the test is the CJEU's *"author's own
intellectual creation"*, not the old English *"skill and labour"*, and that *"these two tests are not
the same, and **the European test is more demanding**."* Arnold LJ expressly identifies
*Navitaire v easyJet* and **Nova Productions v Mazooma Games** as applying the superseded standard.
That matters here because **Nova Productions is the only reported case ever to apply s.9(3)** — so
the single authority on the UK's computer-generated-works provision is a case whose originality
reasoning the Court of Appeal has now said no longer represents the law.

**Status — genuinely unsettled, with dates.**

| Event | Date | Tier |
|---|---|---|
| Copyright and AI consultation (CP1205) opens | **2024-12-17** | **[GOVERNMENT PROPOSAL]** |
| Consultation closes; 11,520 responses | **2025-02-25** | — |
| [Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18/contents) c.18 — Royal Assent | **2025-06-19** | **[STATUTE]** |
| s.137 statement of progress published | **2025-12-15** | **[GOVERNMENT PROPOSAL]** |
| ss.135/136 deadline (9 months from passing) | **2026-03-18** | **[STATUTE]** |
| [Report on Copyright and AI](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence) + Impact Assessment published (DSIT / DCMS / IPO) | **2026-03-18** | **[GOVERNMENT PROPOSAL]** |
| Full consultation response | **Not published.** The consultation page still reads *"We are analysing your feedback."* | **[NEGATIVE FINDING]** |
| Legislation removing s.9(3) | **None introduced.** No amendment or prospective repeal shown on legislation.gov.uk. | **[NEGATIVE FINDING]** |

The government's conclusion, verbatim:

> "The responses to the consultation show **minimal evidence that CGWs protection is being used or has
> significant economic effect.** The majority of respondents who engaged with the CGWs questions
> supported removal… We agree that copyright should incentivise and protect human creativity. There
> is minimal evidence that protection for CWGs is actively used, or that it has a material impact on
> creativity and innovation. We propose to continue to monitor the use and impact of this protection.
> **However, in the absence of evidence of its ongoing value, we propose that it should be removed**,
> while copyright should continue to protect works created with AI assistance."

Supporting numbers from the same report: **78%** of online survey respondents were against
maintaining CGW protection; **87%** of those answering Q32 said the legislation would benefit from
legal clarity; **fewer than half** of all respondents answered the CGW questions at all. And a
directly relevant vendor data point, quoted by the government: *"Open AI said they would be
unaffected as they 'do not claim copyright over generated outputs'."*

Note the s.135 economic impact assessment covers only *"each of the four policy options described in
**section B.4** of the Copyright and AI Consultation Paper"* — **the training/TDM options**. The
computer-generated-works options sit in **section D.1** and are **not** within the statutory
assessment duty. **[STATUTE]** The s.9(3) question therefore has no statutory deadline attached to
it at all.

**Practical reading:** s.9(3) is in force, its only case law has been undermined, its own government
has published an intention to repeal it, and there is no timetable. It is the worst kind of asset —
one you cannot rely on and cannot yet write off.

### 2.2 European Union

The EU has **no computer-generated-works provision**, and the human-author requirement is **implied,
not enacted**. That distinction is important and is frequently overstated; the honest statement of it
follows.

**[STATUTE]** [Software Directive 2009/24/EC](http://data.europa.eu/eli/dir/2009/24/oj), **Art. 1(3)**
— the only *statutory* originality standard that applies to code anywhere in the EU:

> "A computer program shall be protected if it is **original in the sense that it is the author's own
> intellectual creation. No other criteria shall be applied** to determine its eligibility for
> protection."

**Art. 1(2)**: *"Protection… shall apply to the expression in any form of a computer program. Ideas
and principles which underlie any element of a computer program, including those which underlie its
interfaces, are not protected."* **Recital 11** goes further: *"to the extent that **logic,
algorithms and programming languages** comprise ideas and principles, those ideas and principles are
not protected under this Directive."*

**Art. 2(1)** — authorship:

> "The author of a computer program shall be **the natural person or group of natural persons who has
> created the program** or, where the legislation of the Member State permits, the legal person
> designated as the rightholder by that legislation."

**On whether EU law requires a human author — state this carefully.** No EU instrument says so in
terms. The requirement is reached by inference from three directions: (i) Art. 2(1) attaches
*creation* to natural persons (a legal person may only be *"designated as the rightholder"*);
(ii) the term of protection runs *"for the life of the author and for 70 years after his death"*
(Term Directive 2006/116/EC Art. 1(1)) — a term measured by a lifespan presupposes a mortal;
(iii) the CJEU's substantive test is framed wholly in terms of *personality*. **The CJEU has never
ruled on the point.** Do not cite a provision for it, because none exists.

**[RULING] The originality line, in four cases.** The InfoSoc Directive 2001/29/EC contains **no**
definition of originality — the phrase *"own intellectual creation"* appears **zero times** in it.
The standard was generalised judicially from the software, database and photograph directives.

- **[C-5/08 *Infopaq*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62008CJ0005),
  ECLI:EU:C:2009:465, 2009-07-16, ¶37**: *"copyright… is liable to apply only in relation to a
  subject-matter which is original in the sense that it is **its author's own intellectual
  creation**."* ¶45, and this maps almost too neatly onto source code: *"they consist of words which,
  considered in isolation, are not as such an intellectual creation of the author who employs them.
  **It is only through the choice, sequence and combination of those words** that the author may
  express his creativity in an original manner."* ¶38–39: parts of a work are protected *"provided
  that they contain elements which are the expression of the intellectual creation of the author"* —
  i.e. **per-element analysis, which is the EU's structural answer to the taint question.**
- **[C-145/10 *Painer*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62010CJ0145),
  ECLI:EU:C:2011:798, 2011-12-01, ¶88–92**: *"an intellectual creation is an author's own **if it
  reflects the author's personality**… That is the case if the author was able to express his
  creative abilities in the production of the work **by making free and creative choices**… the author
  … can **stamp the work created with his 'personal touch'**."*
- **[C-683/17 *Cofemel*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62017CJ0683),
  ECLI:EU:C:2019:721, 2019-09-12, ¶30–31** — the tightest statement: *"it is both **necessary and
  sufficient** that the subject matter **reflects the personality of its author**, as an expression of
  his free and creative choices… On the other hand, **when the realisation of a subject matter has
  been dictated by technical considerations, rules or other constraints, which have left no room for
  creative freedom, that subject matter cannot be regarded as possessing the originality required**."*
- **[C-833/18 *Brompton Bicycle*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0833),
  ECLI:EU:C:2020:461, 2020-06-11, ¶26–27, 35** — the function-constraint case, and the most relevant
  to code: *"a subject matter satisfying the condition of originality may be eligible for copyright
  protection, **even if its realisation has been dictated by technical considerations**, provided that
  its being so dictated has not prevented the author from reflecting his personality"* — but *"**Where
  the expression of those components is dictated by their technical function**, the different methods
  of implementing an idea are so limited that **the idea and the expression become indissociable**."*
  And ¶35, a limit that cuts against the standard engineering intuition: *"**even though the existence
  of other possible shapes which can achieve the same technical result makes it possible to establish
  that there is a possibility of choice, it is not decisive**."* *"There were other ways to write this
  function"* is, under EU law, expressly **not** sufficient on its own.

The "indissociable" doctrine was born in a **software** case:
**[C-393/09 *Bezpečnostní softwarová asociace*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62009CJ0393),
ECLI:EU:C:2010:816, 2010-12-22, ¶48–49** — *"that criterion cannot be met by components… which are
differentiated only by their technical function."*

**⚠️ Scope caveat, stated because it matters:** *Cofemel* and *Brompton* are design cases, not
software cases. They are good authority on function-constrained originality generally, and *Brompton*
¶27 expressly builds on *BSA* and *SAS Institute* (C-406/10) — but that inferential step should be
visible, not assumed.

**[STATUTE] The EU AI Act does not address output ownership. At all.** In Regulation (EU) 2024/1689
the word *"authorship"* appears **zero times**. Art. 50 is a marking and disclosure duty owed to the
audience. Art. 53(1)(c)–(d) are input-side duties — a copyright-compliance policy honouring the
Art. 4(3) DSM TDM reservation, and a training-content summary. Recital 108 closes it: *"**This
Regulation does not affect the enforcement of copyright rules as provided for under Union law.**"*
Whoever owns AI output in the EU, the AI Act does not decide it.

Cross-check from the UK government's own comparative section — **[GOVERNMENT PROPOSAL]**: *"The EU
does not provide for specific protection for computer-generated works without a human author. The
originality standard developed by the Court of Justice of the EU is tied to human concepts such as
creativity and personal expression… it is **unlikely that such wholly AI-generated outputs will
benefit from copyright protection in the EU**."*

### 2.3 China — protecting, refusing, and split

China has **no** CGW provision. It has judgments, and they disagree.

**[RULING] *Li v. Liu*, (2023) Jing 0491 Min Chu No. 11279 (Beijing Internet Court, 2023-11-27)** —
[court's own English translation](https://english.bjinternetcourt.gov.cn/pdf/BeijingInternetCourtCivilJudgment112792023.pdf).
Chief Judge Zhu Ge; Judges Yan Jun, Li Wanxing.

The test:

> "'Intellectual achievements' refer to the results of intellectual activities, so the work should
> **reflect the intellectual input of a natural person**."

> "Generally speaking, 'originality' requires that the work be completed independently by the author
> and **reflect the author's personalized expression**. 'Mechanical intellectual achievements' are
> excluded… **one has to decide according to the specific situation** whether an AI-generated picture
> reflects the author's personalized expression. Generally speaking… **the more different their needs
> are and the more specific the description of picture elements, layout, and composition is, the more
> personalized the picture will become.**"

Why it was the plaintiff's work — and read the concession in the first clause:

> "**the plaintiff did not draw the lines himself**… the lines and colors that constitute the picture
> involved are **basically done by the Stable Diffusion model**… However, the plaintiff used prompt
> words to work on the picture elements such as the character and how to present it, and set
> parameters to work on the picture layout and composition, **which reflects the plaintiff's choice
> and arrangement**… **Such adjustment and modification also reflect the plaintiff's aesthetic choice
> and personal judgment.**"

> "**as long as the AI-generated images can reflect people's original intellectual investment, they
> should be recognized as works and protected by the Copyright Law.**"

On the model developer: *"in this case, he is only a **producer of the creation tool**… such
investment has gone to the design of the AI model… **not the picture involved.**"* The court noted the
CreativeML Open RAIL-M licence in evidence: *"Except as set forth herein, Licensor claims no rights in
the Output You generate using the Model."*

An under-reported holding, and a governance one: the court **approved a disclosure practice** —
*"the plaintiff should prominently mark the AI technology or model used in line the principle of good
faith and the need to protect the public's right to know… the plaintiff uses the hashtag 'AI
illustration', which is enough… **The Court recognizes this to be a proper practice.**"*

Remedy: public apology displayed **no less than 24 hours**, plus **RMB 500** (≈ US$70) statutory
damages.

**⚠️ Contrarian finding: the "over 150 prompts" figure does not mean what everyone reads it to mean —
and the U.S. Copyright Office repeats it.** Part 2 tells readers: *"the selection of **over 150
prompts** combined with subsequent adjustments and modifications demonstrated that the image was the
result of the author's 'intellectual achievements'."* Read against the judgment, verified by counting
the text directly:

- The judgment records **four generation rounds**, not 150 prompting rounds: (1) initial parameters
  and generate; (2) change a LoRA weight; (3) change the random seed; (4) append eight prompt words.
- It records **two prompt strings** — one positive, one negative — comprising **148 comma-separated
  prompt words** (23 positive, 125 negative), plus the eight added at step 4: **156 total**. That is
  where "over 150" comes from. The judgment's own term is *"prompt words"*.
- The judgment states that of the negative prompt, only one bracketed group *"comes from"* the party
  himself and *"**the rest are directly copied from an online forum**."* On the court's own findings,
  **roughly 84% of the prompt tokens were copied, not authored.**
- There was **no manual pixel editing at all.**

The USCO's sentence is defensible if "prompts" means "prompt words" — but it is near-universally read
as 150 rounds of iteration, and that reading is not supported by the judgment. **This is the project's
standing press-scepticism finding recurring inside an official agency report.** Do not cite "150
prompts" as evidence of extensive human iteration.

**[RULING] The counterweight — Zhangjiagang People's Court, (2024) Su 0582 Min Chu No. 9015,
affirmed by Suzhou Intermediate People's Court, (2025) Su 05 Min Zhong No. 4840** — China's first
decision **refusing** protection to a text-to-image output. Reported by Guangming Daily (state media)
and summarised on the Supreme People's Court IP Tribunal's own site; **the judgment text could not be
obtained** (logged). As reported:

> "Content triggered by a user through **simple prompts alone** fails to reflect original intellectual
> investment and does not constitute a work under the Copyright Law."

> "Because Midjourney's image generation is **random and uncertain**, it is difficult to find that the
> plaintiff's use of the software reflected original personalised selection and modification."

And, per the SPC IP Tribunal page: *"prompts, relative to the generated content, are **merely idea,
not copyright-protected expression**."* **That proposition cannot be reconciled with *Li v. Liu* on
its own terms.**

**[RULING] Changshu People's Court (Jiangsu), 《伴心》, 2025** — protection **granted**, per the Suzhou
municipal government's official report (2025-03-10; case number not published, judgment text not
located). The distinguishing fact: the plaintiff *"made several manual modifications in Photoshop
during iteration."* Court: *"Lin's modification of the prompts and adjustment of the image's detailed
design reflect his unique selection and arrangement."* Remedy: apology for three days plus **RMB
10,000**.

**[RULING] *Shenzhen Tencent v. Shanghai Yingxun* ("Dreamwriter"), (2019) Yue 0305 Min Chu No. 14010
(Shenzhen Nanshan District Court, 2019)** — an AI-generated financial article held protectable **as a
legal person's work**. Sourced from ZHOU Bo, Senior Judge of the SPC IPR Division, writing officially
[for WIPO](https://www.wipo.int/about-ip/en/artificial_intelligence/conversation_ip_ai/pdf/ms_china_1_en.pdf)
— **labelled: authoritative-official commentary by an SPC judge, not the judgment text**:

> "the article in question is considered to be a **legal person work** created by the Plaintiff.
> Accordingly, the copyright of the work completed by the AI in the case is **enjoyed by the user of
> the AI software**."

> "**the Court did not break the general legal rule that the work must be the result of the author's
> intellectual creation**… The textual content was not created autonomously by an AI, but merely the
> result of a **human intellectual activity assisted by an AI**."

The "legal person work" route has no US or EU analogue — the EU permits a legal person to be
*designated as rightholder* but not to have *created* the work.

**[NEGATIVE FINDING] No Chinese court has ruled on AI-generated source code.** Corroborated three
ways: the SPC IP Tribunal's own survey of AI/IP case law contains no such case; two independent
Chinese-language searches returned only commentary; the adjacent cases concern human-written code
(the ByteDance appeal) or an AI model's own structure and parameters (*Douyin v. Yirui*, Beijing IP
Court, March 2025). Every decided Chinese AIGC copyright case concerns **images**, plus the 2019
Dreamwriter text case.

### 2.4 Japan

**[STATUTE]** Copyright Act (Act No. 48 of 1970), **Art. 30-4**, official English translation from
[the Japanese Law Translation database](https://www.japaneselawtranslation.go.jp/en/laws/view/4207)
(page states *"Last Version: Act No. 52 of 2021"*):

> "It is permissible to exploit a work, in any way and to the extent considered necessary, in any of
> the following cases, or in any other case in which it is **not a person's purpose to personally
> enjoy or cause another person to enjoy the thoughts or sentiments expressed in that work**;
> **provided, however, that this does not apply if the action would unreasonably prejudice the
> interests of the copyright owner** in light of the nature or purpose of the work or the
> circumstances of its exploitation:
> … (ii) if it is done for use in **data analysis** (meaning the extraction, comparison,
> classification, or other statistical analysis of the constituent language, sounds, images, or other
> elemental data from a large number of works or a large volume of other such data)…"

**Confirmed from the text: this is an input-side exception and says nothing about output ownership.**
The operative verb throughout is *"exploit a work"* — i.e. use *someone else's existing* work. It sits
in Chapter II, Section 3, Subsection 5 (*Limitations on Copyright*). It contains no words of grant, no
reference to authorship, and no reference to generated material. **Anyone citing Art. 30-4 for the
proposition that Japanese law assigns copyright in AI output to the tool's user is misreading it** —
an error observed in circulation during this research.

**[AGENCY GUIDANCE]** [*General Understanding on AI and Copyright in Japan* — Overview](https://www.bunka.go.jp/english/policy/copyright/pdf/94055801_01.pdf),
Japan Copyright Office, Agency for Cultural Affairs, **May 2024** (underlying General Understanding
adopted March 2024). **Its status is stated on its face and is unusually candid:**

> "**The General Understanding represents the subcommittee's views on the interpretation of the
> current Japanese copyright act as of the time of publication. The General Understanding is not
> legally binding**, nor should it be considered as a definite legal assessment."

> "Normally, the provisions of the Copyright Act should be interpreted by the judiciary on a
> case-by-case basis. **However, there are currently very few court precedents that directly address
> the relationship between AI and copyright.**"

The output test:

> "**Materials autonomously generated by AI** [i.e. *"generated by AI without any instructions from
> humans (or only by giving simple instructions as prompt (e.g., 'Draw a cat.'))"*] **are not
> 'creatively produced expressions of thoughts or sentiments' and are therefore not considered
> (copyrighted) 'works.'**"

> "On the other hand, **if AI is used as a 'tool' by a person to creatively express thoughts or
> sentiments, such material is considered a 'work', and the user of the AI the 'author'.**"

> "Determining whether a person has used AI as a 'tool' depends on two factors: whether the person had
> a **'creative intention'** and whether the person has made a **'creative contribution'**."

**The three factors — and note that two of the three are stated as negatives.** This is the sharpest
divergence from China in the whole corpus:

> "**Amount of instructions/input**: 'Detailed instructions that specifically indicate what
> constitutes creative expression' are more likely to be considered as creative contributions.
> **However, lengthy instructions (i.e., prompts) that merely suggest an idea do not influence the
> assessment of creative contribution.**"

> "**Number of generation attempts: A large number of attempts alone does not affect the assessment of
> creative contribution.** Repeated attempts, **while checking the generated materials and correcting
> the instructions/input**, may be recognized as a creative contribution."

> "**Selection from multiple output materials: The mere act of selection itself does not influence the
> determination of creative contribution.** However, certain elements of choice may be involved which
> may be considered as creative."

> "**any additions or corrections made by humans to AI-generated materials that can be considered
> creative expressions are generally considered to be copyrighted works.**"

Japan and the US converge almost exactly. Japan and China do not: the Beijing Internet Court treated
iterative regeneration and picking one of four images as *"aesthetic choice and personal judgment"*;
the Japanese guidance says bare attempt count and bare selection each count for **nothing**.

**[NEGATIVE FINDING]** The May 2024 Overview is the only English version; the full General
Understanding exists in Japanese only.

### 2.5 The divergence, side by side

Same facts — a human directs an AI system, reviews outputs, accepts one — assessed in each
jurisdiction as at **2026-08-30**.

| | **US** | **UK** | **EU** | **China** | **Japan** |
|---|---|---|---|---|---|
| Machine as author | **No** — *Thaler* **[RULING]** | No — s.178 presupposes it | No (implied) | **No** — *Li v. Liu* **[RULING]** | **No** — ACA **[AGENCY GUIDANCE]** |
| Wholly machine-generated work protected | **No** | **Yes — s.9(3), 50 yrs** **[STATUTE]** | **No** (implied) | **No** | **No** |
| Prompting alone confers authorship | **No** **[AGENCY GUIDANCE]** | **Effectively yes** — the prompter is the "arranger" **[GOVERNMENT PROPOSAL]** | No (implied) | **Split** — yes in Beijing, no in Zhangjiagang/Suzhou **[RULING]** | **No** **[AGENCY GUIDANCE]** |
| Many iterations help | **No** — "re-rolling the dice" | n/a (no originality analysis needed) | Untested | **Yes** — Beijing | **Only with corrective revision** |
| Selecting among outputs helps | **No** — "adoption is not authorship" | n/a | Untested | **Yes** — Beijing | **No** |
| Human modification of output protected | **Yes**, as to the modifications | Yes, as an ordinary original work | Yes, if original | **Yes** — Changshu | **Yes** |
| Legal person can be the *creator* | No | No (deemed author only) | **No** — natural person creates; legal person may be *rightholder* | **Yes** — Dreamwriter | Yes ("a natural or legal person") |
| Specific rule for code | **None** | None | Art. 1(3) Software Directive sets the originality test; nothing AI-specific | None | None |
| Status | Frozen since 2025-01 | **Repeal proposed 2026-03-18, not enacted** | Stable; untested on AI | **Split, unresolved** | Non-binding, few precedents |

**Three genuine disagreements, not differences of emphasis:**

1. **UK vs. everyone on whether a work with no human author can be protected at all.** s.9(3) says
   yes; every other jurisdiction surveyed says no. The UK proposes to join the others but has not.
2. **China (Beijing) vs. US and Japan on iteration and selection.** Beijing treats them as evidence
   of personalised expression; Washington calls selection *"adoption"* and iteration *"re-rolling the
   dice"*; Tokyo says each *alone* counts for nothing.
3. **Within China, Beijing vs. Suzhou on whether prompts are expression or idea.** Unresolved.

**A team shipping globally inherits the strictest.** On these facts the strictest is the **United
States** — because it is the only jurisdiction that combines a firm no-prompting rule with an
**enforcement gate** (registration) that forces you to declare the position in writing, under a duty
of candour, before you can sue.

---

## 3. What this actually means for a codebase

This section is the one with the least primary authority and it is written accordingly. Where the
sources run out, that is stated rather than filled in.

### 3.1 Nothing is tainted — this is directly sourced and should stop a common panic

**[AGENCY GUIDANCE]** Part 2 § II.F, final paragraph:

> "**Similarly, the inclusion of elements of AI-generated content in a larger human-authored work does
> not affect the copyrightability of the larger human-authored work as a whole.** For example, a film
> that includes AI-generated special effects or background artwork is copyrightable, even if the AI
> effects and artwork separately are not."

**[AGENCY GUIDANCE]** 88 FR 16190: the human-authored aspects are *"'independent of' and do 'not
affect' the copyright status of the AI-generated material itself."*

**[STATUTE]** [§ 103(b)](https://www.copyright.gov/title17/92chap1.html), the structural analogue the
Office invokes: *"The copyright in a compilation or derivative work extends only to the material
contributed by the author of such work… **The copyright in such work is independent of, and does not
affect or enlarge the scope, duration, ownership, or subsistence of**, any copyright protection in the
preexisting material."*

Note also what § 103(a) does **not** do: it withdraws protection only *"in which such material has
been used **unlawfully**."* AI-generated code is not *"material in which copyright subsists"* used
unlawfully — it is material in which copyright does not subsist. § 103(a) is not triggered.

**[RULING]** The EU reaches the same place structurally: *Infopaq* ¶38–39 requires per-element
analysis — parts of a work are protected where *"they contain elements which are the expression of the
intellectual creation of the author."*

**So: a repository does not become public domain because an agent wrote part of it.** What happens is
narrower and more awkward — the protected surface has holes in it, and you may not know where they
are.

### 3.2 The bite is at enforcement, and it is a record-keeping problem

Chain it out, all **[STATUTE]** unless marked:

1. Copyright vests automatically on creation, in the author (§ 201(a)). No registration needed to
   *own* it.
2. But *"no civil action for infringement of the copyright in any United States work shall be
   instituted until preregistration or registration of the copyright claim has been made"*
   (§ 411(a)).
3. And § 412 bars **statutory damages and attorney's fees** for infringement that begins before
   registration (subject to the three-month grace period for published works). In practice this is
   what makes small-value software infringement claims economically viable at all.
4. Registration carries a **duty to disclose** AI-generated content and to **exclude** anything more
   than de minimis (88 FR 16190 **[AGENCY GUIDANCE]**).
5. A registration containing knowingly inaccurate information that would have caused refusal can be
   disregarded by the court (§ 411(b)), and the Office may cancel it — which it did in *Zarya*
   **[AGENCY ADJUDICATION]**.

**The question therefore becomes: can you say, truthfully and specifically, what a human wrote?**

Two further primary details make this concrete for code, both from
**[AGENCY GUIDANCE]** [Circular 61, *Copyright Registration of Computer Programs*, **revised 3/2021**](https://www.copyright.gov/circs/circ61.pdf):

- The deposit is an **identifying portion**, not the whole program — the first and last 25 pages of
  source code. So the disclosure burden is not "annotate the whole repo"; it is a claim statement
  plus a bounded deposit.
- The circular **does not mention artificial intelligence anywhere**. **[NEGATIVE FINDING]** The
  Office's dedicated guidance for the exact artifact class in question has not been touched since
  before ChatGPT.

**⚠️ Unanswered by any source: what "more than de minimis" means for code.** The *Théâtre* Board
flagged it as fact-bound — *"there may be cases in the future where the application of the de minimis
standard is a closer call"* — and left it there. There is no line count, no percentage, no test. Godot's
**15-line triviality presumption** (**[PRACTITIONER ARTIFACT]**, recorded in
[`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md)) has **no basis in any
primary legal source found here** — it is a workable heuristic, not a rule, and should not be
described as one.

### 3.3 Trade secret — the fallback that is completely unaffected

**[STATUTE]** [18 U.S.C. § 1839(3)](https://www.law.cornell.edu/uscode/text/18/1839) (DTSA):

> "the term 'trade secret' means **all forms and types of financial, business, scientific, technical,
> economic, or engineering information, including patterns, plans, compilations, program devices,
> formulas, designs, prototypes, methods, techniques, processes, procedures, **programs, or codes**,
> whether tangible or intangible**… if — (A) **the owner thereof has taken reasonable measures to keep
> such information secret**; and (B) **the information derives independent economic value**, actual or
> potential, **from not being generally known** to, and not being readily ascertainable through proper
> means by, another person who can obtain economic value from the disclosure or use of the
> information."

**Read that definition for the word "author". It is not there.** Neither is "original", "creation",
"human", or "work". Trade secret law protects **information** on the basis of **secrecy and value**.
The entire authorship debate is irrelevant to it.

**[STATUTE]** [Directive (EU) 2016/943](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016L0943)
Art. 2(1) is drafted identically in structure — three cumulative conditions: not generally known /
commercial value because secret / subject to reasonable steps to keep it secret. Transposition
deadline 2018-06-09.

**[AGENCY GUIDANCE]** And the two regimes are already designed to coexist for code: Circular 61 has a
dedicated *"Code with Trade Secret Material"* procedure permitting redacted deposits, and *"The
Copyright Office strictly applies these rules."*

**What this means, plainly:** for **closed-source** code, the authorship question is largely a
non-event, because the protection that actually stops a competitor — secrecy — never depended on
authorship. What it *does* depend on is *"reasonable measures"*, which is a governance obligation:
access control, egress control, NDAs, exit procedures. That is the same machinery a containment
posture already requires.

**Where it fails:** anything published. Open source. Source escrow. Code shipped to customers. Code
disclosed in diligence. There, copyright was the only lever, and it is the lever with holes in it.

### 3.4 Contract — available, weaker, and untested here

**[RULING]** *ProCD, Inc. v. Zeidenberg*, 86 F.3d 1447 (7th Cir. 1996) — contract terms restricting
use of **uncopyrightable** material (there, post-*Feist* phone listings) are **not preempted** by
§ 301. So a contract can restrict what someone does with code that copyright does not protect.

**But contract is a materially weaker instrument than copyright**, and the differences are structural,
not incidental: it binds only parties in privity — a third party who obtains the code is not bound;
there is no § 412 statutory-damages route; and there is no copyright injunction as of right. Circuits
also differ on where the preemption line runs. **No court has applied any of this to AI-generated
code.** **[NEGATIVE FINDING]**

### 3.5 ⚠️ Open source and copyleft — the genuinely unsettled part

State the mechanism from primary texts, then stop.

- **[STATUTE]** [§ 106](https://www.copyright.gov/title17/92chap1.html) grants exclusive rights to
  *"the owner of copyright"*. No copyright, no § 106 rights.
- **[RULING]** *Jacobsen v. Katzer*, 535 F.3d 1373 (Fed. Cir. 2008) established that open source
  licence terms operate as copyright **conditions** — breach is infringement, not merely breach of
  contract. **That mechanism runs entirely through copyright.**
- Therefore: **to the extent a contribution has no copyright owner, the copyright hook a copyleft
  licence relies on has nothing to attach to.** Contract may remain (§ 3.4), with the weaknesses
  noted.

**Everything past that sentence is inference, and no authority has tested it.** Nobody has litigated
whether a GPL project containing unprotectable AI-generated files can enforce against a downstream
violator; whether the remaining human-authored code is enough of a hook on its own (probably, per
§ 3.1, but with the copyleft *scope* question then live); or how a court would treat a contributor's
DCO sign-off over material with no author. **Do not state any of this as settled. It is not.**

What *is* established is that maintainers have noticed. **[PRACTITIONER ARTIFACT]**, from
[`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md) (research date
2026-08-27), the two clearest IP-chain policies in that corpus:

- **OpenJDK** (openjdk.org/legal/ai, page dated 2026-04-09) — the rationale is explicitly the
  assignment chain: *"The Oracle Contributor Agreement (OCA) requires that a contributor own the
  intellectual property rights in each contribution… **contributing such content would violate the
  OCA.**"*
- **GCC** (gcc.gnu.org/ai-policy.html, last modified 2026-07-29) — declines *"**legally significant**"*
  LLM contributions while permitting *"legally insignificant"* ones. That hinge is the **FSF
  copyright-assignment threshold**. It is a copyright-chain policy wearing an AI policy's clothes. It
  also requires an `Assisted-by:` trailer and provides that *"**An LLM may not commit code to the
  project repository**"* and *"Only a human may provide the 'Signed-off-by:' tag certifying the
  Developer Certificate of Origin."*

**The pattern is the finding:** the projects that hit the problem first are the ones with a CLA or a
copyright-assignment requirement — because the assignment machinery is the part that breaks (§ 4). A
project with an inbound=outbound licence and no CLA has a much smaller exposure and, consistently,
has published a much narrower policy or none at all.

### 3.6 Who owns it under the contracts you already signed

**[CONTRACT]** Every major vendor's terms are drafted as a **disclaimer of the vendor's rights, not
an assertion that rights exist.** Read the qualifiers.

- **Anthropic Commercial Terms**, effective **2025-06-17**: *"Anthropic hereby assigns to Customer
  **its right, title and interest (if any)** in and to Outputs."* The parenthetical is the entire
  point: it concedes there may be nothing to assign.
- **GitHub Terms of Service, Section J (AI Features)**, effective **2026-04-27**: *"**GitHub does not
  claim ownership of your Input or Output.**"* — a disclaimer, not a grant. And: *"Output may contain
  material that resembles code or content in the model's training data or that is subject to
  third-party copyrights or open source license terms… **You are responsible for determining whether
  your use of Output requires a third-party license.**"* (The predecessor Copilot Product Specific
  Terms, deprecated 2026-03-05, said *"GitHub does not own Suggestions. You retain ownership of Your
  Code"* — note it never said you own the *Suggestions*.)
- **OpenAI**, quoted in the UK government's March 2026 report **[GOVERNMENT PROPOSAL]**: they *"do not
  claim copyright over generated outputs."*

**No vendor asserts that its output is ownable.** They assign whatever they may have and disclaim the
rest. That is a rational drafting posture and it is also a tell: **the contract layer cannot answer
the ownership question, because a party cannot assign a right that does not exist.**

---

## 4. Work-for-hire and the assignment machinery

The ticket asks whether the usual assignment machinery reaches output that has no author. **The
sources answer this unusually clearly, and the answer is no.**

**[RULING]** *Thaler v. Perlmutter* (D.C. Cir. 2025-03-18), § IV, quoted in full at § 1.2 above:
*"The authorship requirement applies to all copyrightable work, **including work-made-for-hire**…
the human-authorship requirement necessitates that all 'original works of authorship' be created in
the first instance by a human being, including those who make work for hire."*

**[STATUTE]** The mechanism, traced:

- [§ 101](https://www.copyright.gov/title17/92chap1.html): a work made for hire is *"a work prepared
  by an employee within the scope of his or her employment"*, or a specially commissioned work in one
  of nine enumerated categories with a signed writing. **Software is not one of the nine categories**
  — which is why contractor software agreements always carry a belt-and-braces assignment clause
  alongside the WFH recital.
- [§ 201(b)](https://www.copyright.gov/title17/92chap2.html): *"In the case of a work made for hire,
  the employer or other person for whom the work was prepared **is considered the author**."*
- § 201(a): copyright *"vests initially in the author or authors."*
- § 201(d): *"The ownership of a copyright may be transferred…"*

Every link presupposes a work of authorship with an author. Where the output has none, § 201(b)
deems the employer the author **of nothing**, § 201(a) vests **nothing**, and § 201(d) transfers
**nothing**. Assignment clauses are not defective; they are simply operating on an empty set for that
material.

**The UK routes it differently but reaches the same structural place.** **[STATUTE]** s.11(2) gives
the employer **first ownership** of a work made by an employee in the course of employment — ownership
transferred from a human author, not authorship deemed. For an AI output the missing author is
supplied by **s.9(3)**, which deems the "arranger" the author; if that person is an employee, s.11(2)
then routes ownership to the employer. **That chain has never been litigated and depends entirely on a
provision the government proposes to repeal.**

**The EU:** **[STATUTE]** Software Directive Art. 2(3) gives the employer the right to *"exclusively…
exercise all economic rights"* in an employee-created program absent contrary contract — again,
downstream of there being an author.

**Practical consequences that follow directly from the texts:**

1. **A CLA or contributor agreement warranting that the contributor owns the IP in the contribution
   cannot be truthfully given for wholly agent-generated material.** This is not speculation — it is
   the reason OpenJDK gives for its ban **[PRACTITIONER ARTIFACT]**.
2. **An acquirer's IP representations and warranties are where this surfaces commercially.** No source
   says this; it follows from the chain above and from § 3.2. Flagged as inference.
3. **Nothing about this affects trade secret assignment**, which moves *information*, not works
   (§ 3.3).

---

## 5. ⚠️ The autonomy axis — what the sources say, and where they are silent

This is the ticket's organising question. It deserves a blunt answer.

### 5.1 The direction is supported

**[AGENCY GUIDANCE]** Part 2, the one sentence in the entire corpus that connects degree of automation
to the authorship threshold:

> "There may come a time when prompts can sufficiently control expressive elements in AI-generated
> outputs to reflect human authorship. If further advances in technology provide users with increased
> control over those expressive elements, a different conclusion may be called for. **On the other
> hand, technological advancements that facilitate increased automation and optimization may bolster
> our current conclusions. For example, if generative AI systems integrate or further improve
> automated prompt optimization, users' control may be diminished.**"

Read literally: **more automation between the human and the output means less human control, which
means less authorship.** The direction the ticket assumes is supported. But the example given is
*automated prompt optimisation* — a 2024 concern about text-to-image tools rewriting prompts
internally, not about agent loops, tool use, or unattended merges.

Two more sentences point the same way:

- **[AGENCY GUIDANCE]** The joint-authorship test: *"The provision of detailed directions, **without
  influence over how those directions are executed**, is insufficient."* Every step of agent autonomy
  added is a step of execution influence removed.
- **[AGENCY GUIDANCE]** The adoption rule: *"providing instructions to a machine and selecting an
  output does not equate to authorship."*

### 5.2 The mapping is not

**[NEGATIVE FINDING], stated plainly because the silence is the finding.**

**No primary source found in this research — statute, ruling, or agency guidance, in any of the five
jurisdictions — distinguishes:**

- a developer accepting an inline completion from one merging an unread agent PR;
- a developer who reviews a diff line by line from one who reads only the tests;
- code written by an agent under a human's step-by-step direction from code written by an agent
  overnight against a ticket;
- a human-written interface with an agent-written implementation from the reverse.

The doctrine that *would* separate them exists and is well developed — control over expressive
elements, perceptibility, separability, execution influence. **Nobody has applied it to a software
workflow.** The Copyright Office has considered images, music, film, comics and text. It has
considered code exactly once, in a footnote, favourably, about refactoring. There is no ruling
anywhere on AI-generated source code.

**Do not manufacture the mapping.** Anyone who tells you that "accepting a completion keeps your
copyright but merging an agent PR loses it" is extrapolating, not citing. The extrapolation is
*plausible* — it follows the reasoning — but it has no authority behind it, and the one place a rule
about degree of automation might have been written down (the promised Compendium update) has not been
written.

### 5.3 What the doctrine *would* suggest, marked clearly as inference

Offered as a reasoning aid, not as law. **Every row is inference from § 1.3–1.4; none is sourced to a
holding about code.**

| Per-action autonomy — what the human approves and when | Doctrinal reading (inference) |
|---|---|
| Human writes; AI completes the token, human accepts or rejects each | Closest to the **assistive tool** side of Part 2 § II.C. The human is determining expression; the tool accelerates typing. Strongest position. |
| Human specifies the design and the algorithm; agent writes the code; human edits substantively | **Modification** limb (§ II.F) plus, arguably, human expression **perceptible** in the output (§ II.E). Protected as to what the human contributed. |
| Human writes the tests/interfaces; agent writes the implementation | Structurally the **cleanest separability story** — the human-authored parts are identifiable and bounded. Note this is the *opposite* of most teams' intuition, which favours line-by-line editing. |
| Human writes a detailed ticket; agent implements; human reviews and merges | Squarely inside *"providing instructions to a machine and selecting an output"*. On the Office's reasoning, **adoption, not authorship.** |
| Agent implements and merges under automated verification; no human reads the diff | No human control over expressive elements at any point. **Nothing to disclaim from, because there is nothing to claim.** |

**Note what determines the row: not the tool, and not a scale.** It is what the human decided and when
— which is exactly the per-action framing [`CONTEXT.md`](../CONTEXT.md) requires and
[ADR-0002](../docs/adr/0002-define-our-own-archetype-set.md) mandates. Two teams using the same agent
harness land in different rows depending on what they gate. **There is no scale here to adopt, and the
sources supply none.**

### 5.4 The one artifact that draws the line

**[PRACTITIONER ARTIFACT]** [Godot contribution policy](https://contributing.godotengine.org/en/latest/pull_requests/pull_request_guidelines.html),
via [`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md) (2026-08-27):

> "**Do not use AI to generate substantial pieces of code** — AI should not be used to author code.
> **Code authoring is more than typing, it includes making decisions about where the code should go,
> what techniques/algorithms should be used, and ultimately what the code should look like. All those
> decisions need to be made by a human.** For example **using AI for code completion is
> permissible**… If you do not have the knowledge/ability to write the code yourself, you are not
> allowed to use AI to write it."

Set that against Part 2's *"uses where an AI system makes **expressive choices** require further
analysis"* and § II.D.2's *"detailed directions **without influence over how those directions are
executed**"*. A game engine project, with no legal citation, has independently restated the Copyright
Office's control-over-expressive-elements test and applied it to a coding workflow — the exact
application the Office has never made.

**That is worth reporting for what it is: the best available articulation of the autonomy/authorship
mapping is a practitioner artifact, not a legal one.** It is evidence of practice, not of law, and it
should never be cited as the latter. But it is the only place in the corpus where anyone has actually
done the work.

---

## Sources

**Primary — United States**

- [17 U.S.C. §§ 101, 102, 103, 106](https://www.copyright.gov/title17/92chap1.html) · [§§ 201, 205](https://www.copyright.gov/title17/92chap2.html) · [§§ 411, 412](https://www.copyright.gov/title17/92chap4.html)
- [18 U.S.C. § 1839](https://www.law.cornell.edu/uscode/text/18/1839) (DTSA definitions)
- [*Thaler v. Perlmutter*, No. 23-5233 (D.C. Cir. Mar. 18, 2025)](https://media.cadc.uscourts.gov/opinions/docs/2025/03/23-5233.pdf)
- *Thaler v. Vidal*, 43 F.4th 1207 (Fed. Cir. 2022) — as quoted in 89 FR 10043 and 90 FR 54636
- *ProCD, Inc. v. Zeidenberg*, 86 F.3d 1447 (7th Cir. June 20, 1996)
- *Jacobsen v. Katzer*, 535 F.3d 1373 (Fed. Cir. Aug. 13, 2008)
- [USCO, *Copyright and AI, Part 2: Copyrightability* (Jan. 29, 2025)](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)
- [USCO, *Copyright and AI, Part 3: Generative AI Training* — **pre-publication version** (May 2025, released May 9, 2025)](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf)
- [Copyright Registration Guidance, 88 FR 16190 (Mar. 16, 2023)](https://www.copyright.gov/ai/ai_policy_guidance.pdf) — *statement of policy*
- [Compendium of U.S. Copyright Office Practices (3d ed.), ch. 300, §§ 306, 313.2, eff. Jan. 28, 2021](https://www.copyright.gov/comp3/chap300/ch300-copyrightable-authorship.pdf)
- [Circular 61, *Copyright Registration of Computer Programs*, rev. 3/2021](https://www.copyright.gov/circs/circ61.pdf)
- [*Zarya of the Dawn*, USCO letter (Feb. 21, 2023)](https://www.copyright.gov/docs/zarya-of-the-dawn.pdf)
- [*Théâtre D'opéra Spatial*, Copyright Review Board (Sept. 5, 2023)](https://www.copyright.gov/rulings-filings/review-board/docs/Theatre-Dopera-Spatial.pdf)
- [*SURYAST*, Copyright Review Board (Dec. 11, 2023)](https://www.copyright.gov/rulings-filings/review-board/docs/SURYAST.pdf)
- [copyright.gov/ai](https://www.copyright.gov/ai/) — report and litigation index, fetched 2026-08-30
- [USPTO, *Inventorship Guidance for AI-Assisted Inventions*, 89 FR 10043 (Feb. 13, 2024)](https://www.govinfo.gov/content/pkg/FR-2024-02-13/pdf/2024-02623.pdf) — **rescinded**
- [USPTO, revised *Inventorship Guidance*, 90 FR 54636 (Nov. 28, 2025)](https://www.govinfo.gov/content/pkg/FR-2025-11-28/pdf/2025-21457.pdf)

**Primary — United Kingdom**

- [CDPA 1988 s.9](https://www.legislation.gov.uk/ukpga/1988/48/section/9) · [s.11](https://www.legislation.gov.uk/ukpga/1988/48/section/11) · [s.12](https://www.legislation.gov.uk/ukpga/1988/48/section/12) · [s.178](https://www.legislation.gov.uk/ukpga/1988/48/section/178)
- [Data (Use and Access) Act 2025 (c.18)](https://www.legislation.gov.uk/ukpga/2025/18/contents), Royal Assent 19 June 2025 — [s.135](https://www.legislation.gov.uk/ukpga/2025/18/section/135), [s.136](https://www.legislation.gov.uk/ukpga/2025/18/section/136), s.137
- [Copyright and AI consultation (CP1205), opened 2024-12-17, closed 2025-02-25](https://www.gov.uk/government/consultations/copyright-and-artificial-intelligence/copyright-and-artificial-intelligence)
- [*Report on Copyright and Artificial Intelligence*, DSIT/DCMS/IPO, 2026-03-18](https://www.gov.uk/government/publications/report-and-impact-assessment-on-copyright-and-artificial-intelligence/report-on-copyright-and-artificial-intelligence) ([PDF](https://assets.publishing.service.gov.uk/media/69ba692226909a14239612e4/CP2602959_-_Report_on_Copyright_and_Artificial_Intelligence_web.pdf)) · [Impact Assessment](https://assets.publishing.service.gov.uk/media/69ba68f7c06ba9576435abb0/CP2602959_-_AI_and_Copyright_Impact_Assessment_Web.pdf)
- [s.137 statement of progress, 2025-12-15](https://www.gov.uk/government/publications/copyright-and-artificial-intelligence-progress-report/copyright-and-artificial-intelligence-statement-of-progress-under-section-137-data-use-and-access-act)
- [*THJ Systems Ltd v Sheridan* [2023] EWCA Civ 1354 (20 Nov 2023)](https://caselaw.nationalarchives.gov.uk/ewca/civ/2023/1354)

**Primary — European Union**

- [Directive 2009/24/EC (Software), Arts. 1(2), 1(3), 2(1), 2(3); recitals 8, 11](http://data.europa.eu/eli/dir/2009/24/oj) — CELEX 32009L0024
- Directive 2001/29/EC (InfoSoc) — CELEX 32001L0029 · Directive 96/9/EC (Database) Art. 3(1) · Directive 2006/116/EC (Term) Arts. 1(1), 6
- [C-5/08 *Infopaq*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62008CJ0005), ECLI:EU:C:2009:465 (16 Jul 2009)
- [C-393/09 *Bezpečnostní softwarová asociace*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62009CJ0393), ECLI:EU:C:2010:816 (22 Dec 2010)
- [C-145/10 *Painer*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62010CJ0145), ECLI:EU:C:2011:798 (1 Dec 2011)
- [C-683/17 *Cofemel*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62017CJ0683), ECLI:EU:C:2019:721 (12 Sep 2019)
- [C-833/18 *Brompton Bicycle*](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62018CJ0833), ECLI:EU:C:2020:461 (11 Jun 2020)
- Regulation (EU) 2024/1689 (AI Act), Arts. 50, 53; recital 108 — CELEX 32024R1689
- [Directive (EU) 2016/943 (Trade Secrets), Arts. 2(1), 4(2)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016L0943)

**Primary — China and Japan**

- [*Li v. Liu*, (2023) Jing 0491 Min Chu No. 11279, Beijing Internet Court, 2023-11-27 — court's English translation](https://english.bjinternetcourt.gov.cn/pdf/BeijingInternetCourtCivilJudgment112792023.pdf)
- Zhangjiagang People's Court (2024) Su 0582 Min Chu No. 9015, aff'd Suzhou Intermediate (2025) Su 05 Min Zhong No. 4840 — **judgment text not obtained**; reported by [Guangming Daily (state media), 2025-04-23](https://m.gmw.cn/2025-04/23/content_1304021700.htm) and the [SPC IP Tribunal](https://ipc.court.gov.cn/zh-cn/news/view-4513.html)
- Changshu People's Court, 《伴心》, 2025 — **judgment text not obtained**; [Suzhou Municipal Government report, 2025-03-10](https://www.suzhou.gov.cn/szsrmzf/szyw/202503/be045c6eed3948e59f56116eaaa0d2cc.shtml)
- *Shenzhen Tencent v. Shanghai Yingxun* ("Dreamwriter"), (2019) Yue 0305 Min Chu No. 14010 — **judgment text paywalled**; sourced from [ZHOU Bo, Senior Judge, SPC IPR Division, for WIPO](https://www.wipo.int/about-ip/en/artificial_intelligence/conversation_ip_ai/pdf/ms_china_1_en.pdf) *(authoritative-official commentary, labelled)*
- [Japan Copyright Act (Act No. 48 of 1970), Art. 30-4 — Japanese Law Translation database](https://www.japaneselawtranslation.go.jp/en/laws/view/4207)
- [*General Understanding on AI and Copyright in Japan* — Overview, Japan Copyright Office / Agency for Cultural Affairs, May 2024](https://www.bunka.go.jp/english/policy/copyright/pdf/94055801_01.pdf)

**Contract text**

- [Anthropic Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), effective 2025-06-17
- [GitHub Terms of Service, Section J (AI Features)](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service), effective 2026-04-27
- [GitHub Copilot Product Specific Terms](https://github.com/customer-terms/github-copilot-product-specific-terms), Oct 2024, **deprecated 2026-03-05**

**Cross-referenced within this repository**

- [`research/refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md) (2026-08-27) — the verbatim OpenJDK, GCC, Godot, Fedora and MicroPython policy text quoted at §§ 3.5 and 5.4. **That file is authoritative for those quotes; this one does not re-verify them.**
- [`CONTEXT.md`](../CONTEXT.md) · [`docs/adr/0002-define-our-own-archetype-set.md`](../docs/adr/0002-define-our-own-archetype-set.md)

---

## Confidence and gaps

**High confidence.** The US doctrinal position (§§ 1.1–1.5) — read from the statute, the D.C. Circuit
opinion, the Federal Register policy statement, the Compendium, and all three registration decisions,
in full text. The EU originality line (§ 2.2) — ten EUR-Lex documents, all HTTP 200, verbatim, with
ECLI identifiers independently verified. The UK statutory position and the March 2026 government
proposal (§ 2.1) — full report text extracted and read. The DTSA and EU trade-secret definitions
(§ 3.3). *Li v. Liu* (§ 2.3) — the court's own English translation, read in full, with the prompt
token count verified by direct counting. The Japanese guidance (§ 2.4) — the ACA PDF read in full, and
Art. 30-4 cross-checked between two independent official sources after a summariser twice mis-stated
it.

**Medium confidence.** The Chinese cases other than *Li v. Liu*. Neither the Changshu nor the
Zhangjiagang/Suzhou judgment text could be obtained; both rest on official government or state-media
reports. The Dreamwriter analysis rests on an SPC judge's WIPO paper, labelled as such, not the
judgment. **Treat the Chinese "split" as well-evidenced in outcome and thinly evidenced in reasoning.**

**Low confidence / inference only, marked as such in the text.** § 3.5 (copyleft) past the two cited
authorities. § 4's second practical consequence (acquisition warranties). All of § 5.3. The
characterisation of the USPTO/USCO divergence as *meaningful* rather than merely *doctrinally
different* is a judgement call, and a reader is entitled to disagree with it.

**Real gaps, named.**

1. **No authority anywhere on AI-generated source code.** Not a ruling, not a registration decision,
   not an agency example. Everything in this document is transposed from images, text and comics.
2. **No definition of "more than de minimis" for code.** No line count, no percentage, no test. The
   Board expressly left it open.
3. **No published USCO registration of a computer program with disclaimed AI-generated code.** The
   ~100 (2023) / "hundreds" (2026) registrations reported are not broken down by work type, and the
   Office publishes no such breakdown.
4. **No empirical data on what companies are actually doing.** No survey, no filing statistics, no
   litigation. Everything in § 3 is doctrinal reasoning plus a handful of open-source policies.
5. **The German, French and Nordic national implementations** of the Software Directive were not
   examined; Member State law can differ within the EU framework.
6. **India, Hong Kong, New Zealand and Singapore** have s.9(3)-style provisions and were not
   examined beyond the UK government's one-line note that their legislation *"has been largely
   untested in the courts."*
7. **Nothing here addresses infringement risk from training** — whether an agent's output infringes
   code it was trained on is a different question with different sources (*Doe v. GitHub*, USCO
   Part 3, Part 4-when-it-exists) and is out of scope for this strand.

---

## Unsettled — do not state as fact

Each row has a next known date where one exists. Where none exists, that is the point.

| Question | Status at 2026-08-30 | Next known date |
|---|---|---|
| Whether the Supreme Court will hear *Thaler* | Petition **No. 25-449** filed 2025-10-09; BIO filed; reply 2026-02-09; counsel requested a **hold**. No grant or denial found in any reachable record. | **None.** Docket blocked (logged). |
| Whether s.9(3) CDPA will be repealed | **Proposed 2026-03-18. Not enacted.** No bill, no amendment, no prospective repeal on legislation.gov.uk. | **None set.** ss.135/136 duties are discharged; the CGW question carries no statutory deadline. |
| Whether the UK full consultation response will issue | Consultation page still reads *"We are analysing your feedback."* | **None set.** |
| What the UK originality test means for a work with no human author | The government's own report calls it *"a legal contradiction"* and says *"it is unclear in the absence of case law."* The only case applying s.9(3) (*Nova Productions*) has had its originality reasoning superseded by *THJ Systems*. | **None.** No litigation known. |
| Whether the USCO will update the Compendium or issue further AI registration guidance | **Promised twice in Part 2 (2025-01-29). Neither issued 19 months later.** | **None announced.** |
| Whether Part 3 will be finalised, and whether Part 4 exists | Part 3 pre-publication since 2025-05-09; Part 4 promised in three footnotes, not published. | **None announced.** |
| Whether Chinese law protects AI output | **Split.** Beijing (2023) and Changshu (2025) protect; Zhangjiagang/Suzhou (2024–25) refuse and hold prompts to be *idea*. | **None.** No SPC guiding case identified. |
| Whether copyleft enforcement survives unprotectable contributions | **Never litigated anywhere.** § 3.5 states a mechanism, not a holding. | **None.** |
| Whether a CLA warranty can be given for agent-generated code | **Never litigated.** OpenJDK and GCC have answered it *as a matter of policy*, not law. | GCC policy *"will be reviewed at the start of 2027"* — the only expiry date in the corpus. |
| *Doe v. GitHub* (Copilot) | On appeal, **9th Cir. No. 24-7700**, argued **2026-02-11**; no decision as of the docket state reached (2026-04-15). Concerns DMCA § 1202 and licence terms — **not** authorship or ownership of output. | Decision pending. |
| *Perlmutter v. Blanche* | D.D.C. 1:25-cv-01659 (filed 2025-05-22) and D.C. Cir. 25-5285 (filed 2025-08-05) both **open**. | Pending. |
| *Allen v. Perlmutter* | D. Colo. 1:24-cv-02665, filed 2024-09-26, listed as live on copyright.gov. | Pending. |
| Whether accepting an inline completion differs from merging an unread agent PR | **No source anywhere addresses it.** | **None.** This is the finding. |

**Two claims specifically flagged as widely repeated and not supported by the primary text:**

- *"Thaler held that AI-generated works can't be copyrighted."* — **No.** It held a machine cannot be
  named as author, and said the opposite of the gloss in terms (§ 1.2).
- *"The Chinese court protected an image made with over 150 prompts."* — **Misleading, and the USCO
  repeats it.** The judgment records **four generation rounds** and **156 comma-separated prompt
  words**, of which the great majority of the negative prompt was, on the court's own findings,
  *"directly copied from an online forum"* (§ 2.3).

---

## Blocked or unavailable sources — logged, none circumvented

| Source | Block | Handling |
|---|---|---|
| `federalregister.gov` (all documents attempted) | **302 redirect to `unblock.federalregister.gov`** — an anti-bot interstitial | Not circumvented. Substituted copyright.gov's own PDF of 88 FR 16190 and govinfo.gov for both USPTO notices. Same official text. |
| `supremecourt.gov` docket 25-449, and its search wrapper | **HTTP 403** on both | Not circumvented. *Thaler* cert status therefore established only from the filings indexed on copyright.gov and the docket PDFs surfaced by search. **Cannot confirm whether cert has been acted on.** |
| `courtlistener.com` `/docket/…` HTML and `/api/rest/v4/dockets/` | **HTTP 403** / **HTTP 401** (token required) | Not circumvented. Fell back to the unauthenticated `/search/` endpoint, which returned sufficient docket metadata. |
| `bailii.org` (*THJ Systems*) | **HTTP 403** | Substituted the National Archives' Find Case Law service — the official primary publisher. |
| `openai.com/policies/*` (three URLs) | **HTTP 403** on all | Not circumvented. Substituted OpenAI's own statement as quoted in the UK government's March 2026 report. **OpenAI's output-ownership clause is therefore not quoted verbatim here.** |
| `chinajusticeobserver.com` — Dreamwriter judgment | **Paywalled, US$220** | Not purchased. Substituted the SPC judge's WIPO paper, labelled. |
| `wenshu.court.gov.cn` (China Judgements Online) | Known CAPTCHA/access gate | **Not attempted.** |
| Changshu 《伴心》 and Zhangjiagang/Suzhou judgment texts | **Not published / not located.** Changshu case number not published at all. | Reported from official government and state-media sources, labelled. |
| `chinapeace.gov.cn` | **ECONNREFUSED** | Substituted the Suzhou municipal government report. |
| `gov.uk` publication search with date filters | Returned **0 results** for the March 2026 documents despite their existing | One WebSearch used to locate them; the documents themselves were then read directly from `gov.uk` and `assets.publishing.service.gov.uk`. |
| PACER (complaint and opinions in *Perlmutter v. Blanche*) | Paywalled | **Not attempted.** Findings limited to docket captions, dates and entry descriptions. |
| Full English text of Japan's *General Understanding* (beyond the May 2024 Overview) | **Does not exist** — Japanese only | Overview used; noted. |
| National implementations of the Software Directive (DE/FR/Nordics) | Not attempted — scope | Recorded as a gap. |

**One tool-reliability caution worth recording for future strands.** WebFetch's summarising model
**twice** produced materially incorrect paraphrases of Japanese statutory text, and once gave a wrong
Royal Assent date for the Data (Use and Access) Act 2025 (August rather than 19 June), which was
caught only because the 9-month deadline arithmetic did not match the published report date. **Every
statutory quotation in this document was taken from raw extracted text (`pdftotext` or direct HTML),
not from a summariser.** Do not quote legislation from a fetch summary.
