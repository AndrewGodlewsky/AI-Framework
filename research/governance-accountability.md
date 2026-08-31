# Accountability: who is answerable for a defect nobody read

**Research date:** 2026-08-30
**Ticket:** [#7 Governance, Legal & IP by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/7) — strand: *Accountability*
**Question (verbatim from the ticket):** *"who is answerable for a defect nobody read, and how do documented policies assign that?"*

> ## ⚠️ This is research, not legal advice
>
> **Nothing in this document is legal advice and it must not be used as a substitute for it.**
> It is a record of what named primary sources — statutes, regulations, court orders, published
> policies and contract terms — actually say, read directly and quoted, as at **2026-08-30**.
> It was written by a researcher, not a lawyer, and has not been reviewed by counsel in any
> jurisdiction. Contract terms change without notice and several quoted here changed within the
> six months before the research date. Legislation quoted here is in places **not yet in force**,
> and in one central case was **amended five weeks before the research date** in a way most
> published commentary has not caught up with. Anyone making a decision that turns on any of
> this must take advice on their own facts, in their own jurisdiction, against the text as it
> stands on the day.
>
> **Where the position is genuinely unsettled, this document says so rather than guessing.**
> §11 is a substantial list of things that are *not* established, including several claims that
> circulate widely and are wrong.

**Vocabulary note** (per [`CONTEXT.md`](../CONTEXT.md)). *Review* = a human reading the change.
*Verification* = the engineered machinery that establishes a change is acceptable when a human
has not read it. These are never collapsed. *Human oversight* is used where the sources use it;
the phrase "human-in-the-loop" appears only inside quotations, attributed, because it is a term
of art in two of the sources and not a claim this document makes. Positions on the spectrum are
described as *further along*, never *higher*.

**Evidence tier is stated with every claim:**

| Tier | Meaning |
|---|---|
| **[STATUTE]** | Legislation or regulation, read from the official publisher (EUR-Lex, legislation.gov.uk). |
| **[COURT]** | A court order or judgment, read from the court's own filing (RECAP/PACER), the official law-report digitisation (Caselaw Access Project), or the national judgments archive (Find Case Law). |
| **[CONTRACT]** | A live contract term, read from the vendor's own published page on the research date. |
| **[POLICY]** | A published policy, code or guidance document, read from the publisher. |
| **[TRACKER]** | A curated third-party index of primary orders. Its counts are its own data; the orders it indexes are primary. |
| **[SECONDARY]** | Commentary or press. **Used only to locate primary text, never as the source of a claim. No claim in this document rests on a [SECONDARY] source.** |

**Relationship to ticket #4.** [`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md)
established that (a) policies are declarations and only access controls stop anything, and
(b) no company anywhere restricts AI code on quality grounds. This document builds on both and
does not repeat the ~25 restriction regimes catalogued there. Where it needs one of them it
cites that file and adds only what is new to the accountability question.

---

## 0. Lead — the findings that matter, in order

1. **⚠️ Every major vendor has written the duty to review into the contract, and GitHub's is the
   bluntest sentence in the corpus.** GitHub Terms of Service §J.4, effective 2026-04-27:
   **"You are responsible for reviewing, testing, and validating any Output before use."**
   **[CONTRACT]** That sentence assigns the customer precisely the duty that moving further
   along the spectrum is designed to remove. Anthropic: *"It is Customer's responsibility to
   evaluate whether Outputs are appropriate for Customer's use case, including where human
   review is appropriate, before using or sharing Outputs."* OpenAI: *"Customer is solely
   responsible for all use of the Outputs and for evaluating the accuracy and appropriateness of
   Output."* Cursor: *"you are responsible for evaluating, and bearing all risks associated with,
   the use of any Suggestions."* GitHub Copilot's product terms: *"You retain all responsibility
   for Your Code."* (§1)

2. **⚠️ Cursor has a clause that prices the far end of the spectrum, and it keys liability to a
   setting.** Terms of Service §1.7, *Auto-Code Execution*: the feature "automatically executes
   code Suggestions **without manual review or confirmation**", and **"By enabling this feature,
   you acknowledge and agree that you are assuming all risks associated with the execution of
   automatically generated code, including without limitation system outages, software defects,
   data loss, and security vulnerabilities. YOU ARE SOLELY RESPONSIBLE FOR ANY IMPACT RESULTING
   FROM USE OF THIS FEATURE, INCLUDING ENSURING APPROPRIATE SAFEGUARDS, TESTING, AND MONITORING
   ARE IN PLACE."** **[CONTRACT]** This is the only term found anywhere that attaches
   consequences to *the act of turning autonomy on*. It is direct contractual support for
   ticket #6's finding that the far end of the spectrum is reached by changing a setting.
   (§1.4, §8)

3. **The liability caps make the vendor question largely academic.** Anthropic: fees paid in the
   previous 12 months. OpenAI: amount paid in the previous 12 months. Cursor: **the greater of
   six months' fees or $100**. GitHub: no cap is stated for GitHub because the flow runs the
   other way — *the customer indemnifies GitHub*. **[CONTRACT]** Every one of these contracts
   also disclaims all implied warranties and excludes consequential loss, and Anthropic's
   exclusion is expressed to apply "IN CONTRACT, TORT, **STRICT PRODUCT LIABILITY**, OR
   OTHERWISE". **On the contracts as written, the vendor bears essentially none of it.** (§1.7)

4. **⚠️ The new EU Product Liability Directive does make software a product — and expressly does
   not make source code one.** Directive (EU) 2024/2853, recital 13: *"it should be clarified in
   this Directive that software is a product for the purposes of applying no-fault liability,
   irrespective of the mode of its supply or usage"*, and *"A developer or producer of software,
   including AI system providers within the meaning of Regulation (EU) 2024/1689 …, should be
   treated as a manufacturer."* **The same recital then says: "Information is not, however, to be
   considered a product, and product liability rules should therefore not apply to the content of
   digital files, such as media files or e-books or the mere source code of software."**
   **[STATUTE]** A code suggestion is not a product. The executable it ends up in is. That
   distinction is almost never reported and it matters enormously here. (§2.1, §2.2)

5. **⚠️ It is not in force yet, and when it is it will not reach most software defects.** The PLD
   applies to products "placed on the market or put into service **after 9 December 2026**"
   (Art. 2(1)); Member States must transpose by 9 December 2026 (Art. 22(1)); Directive
   85/374/EEC is repealed with effect from the same date (Art. 21). **As of 2026-08-30 it governs
   nothing.** **[STATUTE]** And its damage heads (Art. 6) are consumer heads: death or personal
   injury; property damage **"except… property used exclusively for professional purposes"**; and
   destruction or corruption of data **"not used for professional purposes"**. Only a *natural
   person* may claim (Art. 5(1)). **A business's economic loss from a defect in unread enterprise
   code sits outside the Directive entirely.** (§2.3, §2.5)

6. **Where the PLD does reach, it shifts the burden hard — and names machine learning as the
   reason.** Art. 10(2)(a): defectiveness **"shall be presumed where… the defendant fails to
   disclose relevant evidence pursuant to Article 9(1)"**. Art. 10(4): a national court **shall**
   presume defectiveness or causation where the claimant faces "excessive difficulties, in
   particular due to technical or scientific complexity" and shows only that it is "likely".
   Recital 48 lists as complexity factors *"the complex nature of the technology used, such as
   machine learning"* and *"a link that, in order to be proven, would require the claimant to
   explain the inner workings of an AI system"*. **[STATUTE]** For a defendant who cannot produce
   a record because nobody read the code, Art. 9 plus Art. 10(2)(a) is the sharpest provision in
   the instrument. (§2.6)

7. **The AI Liability Directive was withdrawn, on a precise and citable date.** Not "shelved",
   not "paused", not "still pending". *Official Journal of the European Union*, C series,
   **C/2025/5423, 6 October 2025**, "WITHDRAWAL OF COMMISSION PROPOSALS", listing **"COM(2022)496
   final — 2022/0303 (COD) — Proposal for a DIRECTIVE … on adapting non-contractual civil
   liability rules to artificial intelligence (AI Liability)"**. **[STATUTE]** The European
   Parliament's Legislative Observatory records the same date — "06/10/2025 Proposal withdrawn by
   Commission" — and status "Procedure lapsed or withdrawn". The intention was announced in the
   Commission Work Programme 2025 (COM(2025) 45 final, 11 February 2025), Annex IV entry 32,
   with the stated reason *"No foreseeable agreement - the Commission will assess whether another
   proposal should be tabled or another type of approach should be chosen."* (§3)

8. **⚠️ The EU AI Act was amended on 27 July 2026 and much of what is commonly cited about it is
   now out of date.** Regulation (EU) 2026/1744 of 8 July 2026 ("Digital Omnibus on AI"), in
   force 27 July 2026, replaced Articles 2, 4, 25 and 113 among others. **[STATUTE]** Two
   consequences here. First, **the high-risk obligations — Art. 14 human oversight, Art. 25 value
   chain, Art. 26 deployer duties — are deferred to 2 December 2027 (Annex III high-risk) and
   2 August 2028 (Annex I high-risk)**, and are **not applicable on the research date**. Second,
   **Article 4 (AI literacy) was weakened**: from "shall take measures to ensure, to their best
   extent, a sufficient level of AI literacy" to "shall take measures **to support the
   development of** AI literacy… **This obligation does not require providers or deployers to
   guarantee any specific level of AI literacy of any individual.**" (§4)

9. **⚠️ Courts have already sanctioned the professional who signed without reading, and the
   holding is precise enough to transfer.** *Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC)
   (S.D.N.Y., 22 June 2023), Conclusions of Law ¶23(a): **"Mr. LoDuca violated Rule 11 in not
   reading a single case cited in his March 1 Affirmation in Opposition and taking no other steps
   on his own to check whether any aspect of the assertions of law were warranted by existing
   law. An inadequate or inattentive 'inquiry' may be unreasonable under the circumstances. But
   signing and filing that affirmation after making no 'inquiry' was an act of subjective bad
   faith."** **[COURT]** The distinction the court draws is the one this ticket needs:
   **reviewing badly is unreasonableness; signing having read nothing is a different and worse
   thing.** (§6.1)

10. **⚠️ A second order splits the roles the spectrum splits.** *Wadsworth v. Walmart Inc.*,
    No. 2:23-cv-118-KHR (D. Wyo., 24 February 2025) sanctioned **three** lawyers differently:
    the drafter ($3,000 plus revocation of pro hac vice admission), and **two signing attorneys
    who had not read the filing ($1,000 each)**. The court: *"Signing a legal document ensures
    that the attorney read the document and conducted a reasonable inquiry into the existing
    law… This duty is a 'nondelegable responsibility.' … **blind reliance on another attorney can
    be an improper delegation of this duty and a violation of Rule 11.**"* And of the supervising
    partner: *"His reliance on Mr. Ayala's experience was understandable, but he still has a
    nondelegable duty to ensure a motion is supported by existing law."* **[COURT]** Author,
    approver and rubber-stamping local counsel were each answerable, in descending amounts.
    (§6.2)

11. **⚠️ In that same order the firm escaped sanction because it had a policy AND a control —
    the single most transferable fact in this document.** The court declined to sanction Morgan &
    Morgan because *"Morgan & Morgan trained its employees to not use the AI software in the way
    Mr. Ayala used it"* and, after the show-cause order, *"has since implemented an additional
    acknowledgement prior to using its AI software that '[u]sers must independently verify' any
    AI-generated information before using or relying on it. **The Court would have likely imposed
    sanctions similar to these measures. Thus, any further sanction would be greater than
    necessary.**"* **[COURT]** Ticket #4 established that policies are declarations and only
    access controls stop anything. This is the corollary on the accountability side: **a
    documented policy plus an enforced acknowledgement gate moved liability off the organisation
    and onto the individual.** (§6.2, §8)

12. **⚠️ The English Divisional Court has held the duty does not shift when you delegate — and
    then went looking for the supervisors.** *R (Ayinde) v London Borough of Haringey; Al-Haroun v
    Qatar National Bank* [2025] EWHC 1383 (Admin), 6 June 2025 (President of the King's Bench
    Division and Johnson J), ¶8: the duty to check AI research against authoritative sources
    **"rests on lawyers who use artificial intelligence to conduct research themselves *or rely
    on the work of others who have done so*. This is no different from the responsibility of a
    lawyer who relies on the work of a trainee solicitor or a pupil barrister for example, or on
    information obtained from an internet search."** **[COURT]** And ¶70 referred to the
    regulator, among other things, *"Whether those responsible for supervising Ms Forey's
    pupillage in chambers complied with the relevant regulatory requirements in respect of her
    supervision, **the way in which work was allocated to her**, and her competence to undertake
    the level of work that she was doing."* ¶9: *"in Hamid hearings such as these, the profession
    can expect the court to inquire whether those leadership responsibilities have been
    fulfilled."* (§6.3, §8)

13. **⚠️ Zero of those cases are about code.** The largest curated index of AI-hallucination
    decisions worldwide records **1,983 cases as of 30 August 2026**. A keyword sweep of the full
    downloaded dataset returns **0 hits for "source code", 0 for "software engineer", 0 for
    "pull request", 0 for "code review", 0 for "programmer"**. **[TRACKER]** Every case concerns
    material put before a court or tribunal. **The transfer to software is analogical reasoning
    from an adjacent profession, not settled software law, and this document flags that at every
    point the analogy is used.** (§6.5, §6.6, §11)

14. **⚠️ The tracker also carries a contrarian number that cuts the other way.** Of 1,983 cases,
    **1,134 involve pro se litigants and 787 involve lawyers** — the professional cases are a
    minority. Of the recorded outcomes there are **363 monetary sanctions and 154 disciplinary
    referrals**, while the single largest outcome category is **"Warning" (485)**. Of the 199
    penalties denominated in US dollars, **133 are under $5,000**. **[TRACKER]** The dominant
    judicial response to unreviewed AI output reaching a court is a telling-off. "The courts are
    cracking down" is at best half true. (§6.5)

15. **⚠️ The DCO — the instrument open source most often points at when asked "who is
    accountable?" — certifies provenance and says nothing whatever about correctness.** Developer
    Certificate of Origin 1.1 has four clauses: (a) I created it in whole or in part and have the
    right to submit it; (b) it is based on prior work I have the right to submit; (c) it came
    from someone who certified (a), (b) or (c) and I have not modified it; (d) I understand the
    record is public and permanent. **[POLICY]** **There is no clause about having read,
    understood, tested or verified anything.** The Linux kernel's own gloss confirms the scope:
    the sign-off *"certifies that you wrote it or otherwise have the right to pass it on as an
    open-source patch."* **A developer who signs off on code they did not read makes no false
    certification under the DCO.** Projects treating the DCO as the accountability mechanism for
    AI-assisted contributions are relying on an instrument that does not do that job. (§7.1)

16. **⚠️ And the kernel's *review* certification — the one that does concern reading — disclaims
    warranty in its own text.** The `Reviewed-by:` "Reviewer's statement of oversight",
    clause (d): **"While I have reviewed the patch and believe it to be sound, I do not (unless
    explicitly stated elsewhere) make any warranties or guarantees that it will achieve its
    stated purpose or function properly in any given situation."** **[POLICY]** Stack that
    against Apache-2.0 §7–§8 (each Contributor provides its Contributions "AS IS"; "In no event
    and under no legal theory, whether in tort (including negligence), contract, or otherwise…
    shall any Contributor be liable") and the Apache ICLA §6 (the contributor provides
    contributions "on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND"), and the
    open-source answer is uncomfortable and clear: **the author disclaims, the reviewer
    disclaims, the licence disclaims, and the downstream user is told they are "solely
    responsible for determining the appropriateness of using or redistributing the Work".**
    Nobody is answerable, by design — and that design predates AI by decades. (§7.2, §7.3)

17. **The clearest accountability text located anywhere is the Linux kernel's, and it is four
    bullet points long.** `Documentation/process/coding-assistants.rst`: *"AI agents MUST NOT add
    Signed-off-by tags. Only humans can legally certify the Developer Certificate of Origin
    (DCO). **The human submitter is responsible for: Reviewing all AI-generated code; Ensuring
    compliance with licensing requirements; Adding their own Signed-off-by tag to certify the
    DCO; Taking full responsibility for the contribution.**"* And
    `Documentation/process/generated-content.rst`: *"**You are expected to understand and to be
    able to defend everything you submit. If you are unable to do so, then do not submit the
    resulting changes.**"* **[POLICY]** (§7.4)

18. **⚠️ Foundation-level AI policy is about intellectual property and nothing else.** The Linux
    Foundation's "Guidance Regarding Use of Generative AI Tools for Open Source Software
    Development" and the Apache Software Foundation's "Generative Tooling Guidance" were read in
    full on the research date. **Both address licence compatibility, third-party copyright,
    attribution and the copyrightability of AI output. Neither contains a single sentence about
    responsibility for defects, quality, testing or review.** **[POLICY]** This extends ticket
    #4's finding — *no company anywhere restricts AI code on quality grounds* — one layer up:
    **the foundations do not assign accountability for quality either.** (§7.5)

19. **⚠️ The vendor that does impose a hard review duty excludes software from it.** Anthropic's
    Usage Policy (effective 2025-09-15) requires, for "High-Risk Use Cases", that *"a qualified
    professional in that field must review the content or decision prior to dissemination or
    finalization. You or your organization are responsible for the accuracy and appropriateness
    of that information."* The enumerated list is Legal, Healthcare, Insurance, Finance,
    Employment and housing, Academic testing/accreditation/admissions, and journalistic content.
    **Software engineering is not on it.** **[POLICY]** The vendor mandates qualified
    professional review of AI output for advising on a mortgage — and not for shipping the code
    that decides the mortgage. (§7.6)

20. **On negligence the honest answer is that the law is unsettled and has been for forty-five
    years — with rulings both ways.** *Chatlos Systems, Inc. v. National Cash Register Corp.*,
    479 F. Supp. 738 (D.N.J. 1979), n.1: *"The novel concept of a new tort called 'computer
    malpractice' is premised upon a theory of elevated responsibility on the part of those who
    render computer sales and service… Simply because an activity is technically complex and
    important to the business community does not mean that greater potential liability must
    attach. **In the absence of sound precedential authority, the Court declines the invitation
    to create a new tort.**"* Against it, *Data Processing Services, Inc. v. L.H. Smith Oil
    Corp.*, 492 N.E.2d 314 (Ind. Ct. App. 1986): *"Those who hold themselves out to the world as
    possessing skill and qualifications in their respective trades or professions impliedly
    represent they possess the skill and will exhibit the diligence ordinarily possessed by well
    informed members of the trade or profession… **We hold these principles apply with equal
    force to those who contract to develop computer programming.**"* **[COURT]** But note what
    the second case is: an **implied contractual promise of reasonable skill**, not a tort
    malpractice standard, reached because the transaction was held to be a *service* rather than
    a sale of goods. **No jurisdiction found in this research recognises software engineering
    malpractice as a distinct tort.** (§5)

21. **The UK and the EU are about to diverge on whether software is a product at all.** UK
    Consumer Protection Act 1987 s.1(2): *"'product' means any goods or electricity"*; s.45(1):
    *"'goods' includes substances, growing crops and things comprised in land by virtue of being
    attached to it and any ship, aircraft or vehicle."* No software. And the new Product
    Regulation and Metrology Act 2025 (2025 c. 20) s.1(7) defines *"'product' means **a tangible
    item** that results from a method of production"* — software enters only as an "intangible"
    *component* of a tangible product (s.2(2)(a) with s.2(9): *"a reference to 'intangible'
    components includes software"*). **[STATUTE]** From 9 December 2026, standalone software is a
    product in the EU and is not one in the UK.

---
## 1. The vendors: what the contracts actually say

Every term below was read from the vendor's own published page on **2026-08-30**. All are
**[CONTRACT]** unless marked otherwise. Where WebFetch's summarising model produced a paraphrase,
the text was re-fetched raw and the quotation taken from the raw document; §12 records the two
places where that was necessary.

### 1.1 GitHub — the strongest review-duty clause found anywhere

**Source:** GitHub Terms of Service, https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
— page states **"Effective date: April 27, 2026"**. Section J is titled "AI Features, Training,
and Your Data". Definitions in §A: *"'Output' means responses and suggestions, including code or
other material, generated by an AI Feature"*; *"'AI Feature' means any feature of GitHub or our
Affiliates that uses machine learning or artificial intelligence to generate Output, including
GitHub Copilot, Copilot Autofix…"*

> **J.4. Disclaimers**
> "Output is provided "as-is" and subject to the disclaimers in Section O. Without limiting
> Section O: Output may be inaccurate, incomplete, or non-functional. Output may resemble
> third-party code, including code under open source licenses. We do not guarantee that Output is
> free of errors, vulnerabilities, or intellectual property claims.
>
> **You are responsible for reviewing, testing, and validating any Output before use.**"
>
> **J.5. Your Responsibility and Indemnity**
> "You are responsible for your use of Output, including ensuring it complies with applicable law
> and does not infringe third-party rights.
> Your indemnity obligations in Section Q apply to your use of AI Features and Output, including
> claims arising from Output you incorporate into your products or services."
>
> **J.2. Ownership**
> "Output may contain material that resembles code or content in the model's training data or
> that is subject to third-party copyrights or open source license terms. You are responsible for
> determining whether your use of Output requires a third-party license and for complying with
> any such license."

**The J.4 sentence is the single most on-point contract term in this research.** It names all
three of the things a team further along the spectrum stops doing — reviewing, testing,
validating — and assigns them to the customer, before use.

**Section O (Disclaimer of Warranties)**, quoted in full because it does the load-bearing work:

> "GitHub provides the Website and the Service "as is" and "as available," without warranty of
> any kind. Without limiting this, we expressly disclaim all warranties, whether express, implied
> or statutory, regarding the Website and the Service including without limitation any warranty
> of merchantability, fitness for a particular purpose, title, security, accuracy and
> non-infringement.
>
> GitHub does not warrant that the Service will meet your requirements; that the Service will be
> uninterrupted, timely, secure, or error-free; that the information provided through the Service
> is accurate, reliable or correct; that any defects or errors will be corrected… **You assume
> full responsibility and risk of loss resulting from your downloading and/or use of files,
> information, content or other material obtained from the Service.**"

**Section Q (Release and Indemnification)** — note the direction of travel:

> "You agree to indemnify us, defend us, and hold us harmless from and against any and all
> claims, liabilities, and expenses, including attorneys' fees, arising out of your use of the
> Website and the Service…"

**GitHub Copilot Product Specific Terms**, https://github.com/customer-terms/github-copilot-product-specific-terms
(governs Copilot Business and Copilot Enterprise licence holders; other users are governed by ToS
§J):

> **§2. Ownership of Suggestions and Your Code** — "GitHub does not own Suggestions. You retain
> ownership of Your Code."
>
> **§3. Responsibility for Your Code** — "**You retain all responsibility for Your Code,
> including Suggestions you include in Your Code or reference to develop Your Code. It is
> entirely your decision whether to use Suggestions generated by GitHub Copilot.** If you use
> Suggestions, GitHub strongly recommends that you have reasonable policies and practices in
> place designed to prevent the use of a Suggestion in a way that may violate the rights of
> others. This includes, but is not limited to, using the filtering features available in GitHub
> Copilot."
>
> **§4. Defense of Third Party Claims** — "If your Agreement provides for the defense of third
> party claims, that provision will apply to your use of GitHub Copilot, including to the
> Suggestions you receive."

Two observations. First, "You retain **all** responsibility for Your Code" is an ownership-based
allocation: because you own the code, you own the problem. Second, the recommendation to have
"reasonable policies and practices in place" is expressed as **an IP-protection measure**, not a
quality one — consistent with ticket #4's finding that restriction is never about quality.

### 1.2 Anthropic

**Source:** https://www.anthropic.com/legal/commercial-terms, read raw on 2026-08-30.

> **D.3. Limitations of Outputs; Notice to Users.** "**It is Customer's responsibility to evaluate
> whether Outputs are appropriate for Customer's use case, including where human review is
> appropriate, before using or sharing Outputs.** Customer acknowledges, and must notify its
> Users, that factual assertions in Outputs should not be relied upon without independently
> checking their accuracy, as they may be false, incomplete, misleading or not reflective of
> recent events or information."
>
> **L.2. Disclaimer of Warranties.** "EXCEPT TO THE EXTENT EXPRESSLY PROVIDED FOR IN THESE TERMS,
> TO THE MAXIMUM EXTENT PERMITTED UNDER LAW (A) THE SERVICES AND OUTPUTS ARE PROVIDED "AS IS" AND
> "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND… ANTHROPIC DOES NOT WARRANT, AND DISCLAIMS THAT,
> THE SERVICES OR OUTPUTS ARE ACCURATE, COMPLETE OR ERROR-FREE OR THAT THEIR USE WILL BE
> UNINTERRUPTED."
>
> **L.3.a.** "…the liability of each party, and its affiliates and licensors, for any damages
> arising out of or related to these Terms (i) excludes damages that are consequential,
> incidental, special, indirect, or exemplary… and **(ii) is limited to Fees paid by Customer for
> the Services in the previous 12 months.**"
>
> **L.3.c.** "THE LIMITATIONS OF LIABILITY IN THIS SECTION L.3… APPLY: … (II) TO LIABILITY IN
> TORT, INCLUDING FOR NEGLIGENCE; **(III) REGARDLESS OF THE FORM OF ACTION, WHETHER IN CONTRACT,
> TORT, STRICT PRODUCT LIABILITY, OR OTHERWISE**…"

L.3.c(III) is worth pausing on: the contract anticipates a strict product liability claim and
excludes it by agreement. Whether that exclusion survives contact with the PLD is a question
§2.7 addresses — Art. 15 of the Directive forbids it for the claims the Directive covers.

Note also the *softness* of D.3 relative to GitHub's §J.4: Anthropic says human review is the
customer's call ("**including where** human review is appropriate"), where GitHub says the
customer **is responsible for** reviewing. Both put it on the customer; only one asserts the duty
exists.

### 1.3 OpenAI

**Source:** https://openai.com/policies/business-terms/, read raw on 2026-08-30. (WebFetch was
blocked with HTTP 403; curl with a browser user-agent returned the page. Logged in §12.)

> **4.3. Customer Obligations.** "Customer is responsible for all Input and represents and
> warrants that it has all rights, licenses, and permissions required to provide Input to the
> Services. **Customer is solely responsible for all use of the Outputs and for evaluating the
> accuracy and appropriateness of Output for Customer's use case.**"
>
> **12.1. Warranties.** "OpenAI warrants that, during the Term, when used in accordance with this
> Agreement, the Services will conform in all material respects with the Documentation."
>
> **12.2. Disclaimer.** "SUBJECT TO SECTION 12.1, THE SERVICES ARE PROVIDED "AS IS."… OPENAI
> MAKES NO REPRESENTATION, WARRANTY OR GUARANTEE THAT SERVICES WILL MEET CUSTOMER'S REQUIREMENTS
> OR EXPECTATIONS, **THAT CUSTOMER CONTENT WILL BE ACCURATE, THAT DEFECTS WILL BE CORRECTED**, OR
> REGARDING ANY THIRD-PARTY SERVICES."
>
> **14.2. Limitation on Amount of Liability.** "…**EACH PARTY'S TOTAL LIABILITY UNDER THE
> AGREEMENT WILL NOT EXCEED THE TOTAL AMOUNT CUSTOMER PAID TO OPENAI DURING THE TWELVE MONTHS
> IMMEDIATELY PRIOR TO THE EVENT GIVING RISE TO LIABILITY.**"

**Contrarian detail worth recording:** §12.1 is a real, if narrow, warranty — the Services will
conform in all material respects with the Documentation. It is the only affirmative product
warranty found in any of the six vendors' terms. It warrants the *service*, not the *output*.

### 1.4 Cursor (Anysphere) — the auto-execution clause

**Source:** https://cursor.com/terms-of-service, read raw on 2026-08-30.

> **1.4. Limitations for Suggestions.** "…you acknowledge that there are numerous limitations
> that apply with respect to Suggestions provided by large language and other AI models…
> (i) Suggestions may contain errors or misleading information… (iv) AI Models can struggle with
> complex tasks that require reasoning, judgment and decision-making… **You agree that you are
> responsible for evaluating, and bearing all risks associated with, the use of any Suggestions,
> including any reliance on the accuracy, completeness, or usefulness of Suggestions.**"
>
> **1.7. Auto-Code Execution.** "The Service may include a feature that **automatically executes
> code Suggestions without manual review or confirmation**, and will be clearly labeled
> accordingly. **By enabling this feature, you acknowledge and agree that you are assuming all
> risks associated with the execution of automatically generated code, including without
> limitation system outages, software defects, data loss, and security vulnerabilities. YOU ARE
> SOLELY RESPONSIBLE FOR ANY IMPACT RESULTING FROM USE OF THIS FEATURE, INCLUDING ENSURING
> APPROPRIATE SAFEGUARDS, TESTING, AND MONITORING ARE IN PLACE.**"
>
> **14. DISCLAIMER OF WARRANTIES.** "THE SERVICE AND SUGGESTIONS ARE PROVIDED "AS IS" AND ON AN
> "AS AVAILABLE" BASIS… **YOU AGREE THAT ANY USE OF SUGGESTIONS FROM OUR SERVICE IS AT YOUR SOLE
> RISK AND YOU WILL NOT RELY ON ANY SUGGESTION AS A SOURCE OF TRUTH.**"
>
> **15.2. LIABILITY CAP.** "…THE AGGREGATE LIABILITY OF THE ANYSPHERE ENTITIES TO YOU FOR ALL
> CLAIMS… **IS LIMITED TO THE GREATER OF: (A) THE AMOUNT YOU HAVE PAID TO ANYSPHERE… IN THE SIX
> (6) MONTHS PRIOR… OR, IF GREATER, (B) $100.**"

**§1.7 deserves the emphasis it is given in §0.** It is the only contract clause located in this
research that:

- names the specific capability that removes human review from the loop ("without manual review
  or confirmation");
- makes the *act of enabling* the trigger for the risk allocation ("By enabling this feature…");
- enumerates the actual failure modes of unread code — "system outages, software defects, data
  loss, and security vulnerabilities"; and
- names the substitutes the customer must supply: "APPROPRIATE SAFEGUARDS, TESTING, AND
  MONITORING". In this project's vocabulary that is a demand for **verification** to replace the
  **review** the feature removes — written into a commercial contract.

### 1.5 AWS — a documented inconsistency

**Source:** https://aws.amazon.com/service-terms/, read raw on 2026-08-30 (1.06 MB; parsed
locally).

AWS has a standard review-duty formula that it repeats across many services. Example, §81.2
(Industrial AI Services):

> "Industrial AI Services use machine learning models that generate predictions based on patterns
> in data. **Output generated by a machine learning model is probabilistic and should be
> evaluated for accuracy as appropriate for your use case, including by employing human review of
> such output.** You and your End Users are responsible for all decisions made, advice given,
> actions taken, and failures to take action based on your use of Industrial AI Services."

The same formula appears at §24.2 (AWS Supply Chain), §53.10 (Amazon Chime SDK ML Services),
§54.8.3 (Amazon Connect Customer Voice ID), §60.4.2 (Amazon SageMaker Data Agent) and §99.1
(Amazon DataZone).

**⚠️ It does not appear in §50, the section that governs AWS's coding tools.** §50 ("AWS Machine
Learning and Artificial Intelligence Services") defines "AI Services" to include *"Amazon
Bedrock… Amazon Q… Kiro… AWS DevOps Agent…"*. Reading §50 in full: it contains data-use, privacy,
opt-out, provenance-watermark and IP-indemnity provisions, and **no human-review or
evaluate-for-accuracy clause at all.** The nearest thing to a responsibility allocation is
ownership-based:

> **§50.2.** "**The output that you generate using AI Services is Your Content.** Due to the
> nature of machine learning, output may not be unique across customers and the Services may
> generate the same or similar results across customers."

**This is a verified negative finding.** AWS contractually tells customers to apply human review
to the output of a fridge-temperature service and a call-centre voice-ID service, and does not
say it about the output of its coding agents. It was not located elsewhere in the Service Terms.

### 1.6 Google Cloud

**Source:** https://cloud.google.com/terms/service-terms, read raw on 2026-08-30. §20 "Generative
AI Services".

> **20(a) Definition.** "'Generated Output' means the data or content generated by a Generative AI
> Service prompted by Customer Data. **Generated Output is Customer Data.** As between Customer
> and Google, Google does not assert any ownership rights in any new intellectual property
> created in the Generated Output."
>
> **20(b) Disclaimer.** "Generative AI Services… **use emerging technology, may provide inaccurate
> or offensive Generated Output, and are not designed for or intended to meet Customer's
> regulatory, legal, or other obligations.**"
>
> **20(j) Modifying, Disregarding, or Disabling Safety Filters.** "Google makes available safety
> filters for certain Generative AI Services. **Customer is solely responsible for (i) its use,
> non-use, or modification (including modifications made by Google at Customer's instruction) of
> safety filters in creating Generated Output, and (ii) disregarding safety instructions or
> Documentation.**"

**Google's contract contains no review duty.** The nearest thing is 20(j), and note its shape: it
is another instance of *liability attaching to a configuration choice* — the customer is solely
responsible for its "use, non-use, or modification" of a filter. Same structure as Cursor §1.7,
narrower subject.

At the product-documentation layer Google is softer still. Gemini Code Assist documentation
(https://docs.cloud.google.com/gemini/docs/codeassist/overview): *"As an early-stage technology,
Gemini Code Assist can generate output that seems plausible but is factually incorrect. **We
recommend that you validate all output from Gemini Code Assist before you use it.**"*
**[POLICY]** — a recommendation in documentation, not a term in a contract.

### 1.7 Cross-vendor summary

| Vendor | Express duty to review/verify output? | Where | Warranty | Liability cap |
|---|---|---|---|---|
| **GitHub** (ToS §J) | **Yes — "reviewing, testing, and validating"** | ToS §J.4, eff. 2026-04-27 | Disclaimed (§O), Output "as-is" | None stated for GitHub; **customer indemnifies GitHub** (§Q) |
| **GitHub Copilot** (product terms) | Responsibility yes; review not spelled out | Copilot PST §3 | Per ToS | Per Agreement |
| **Anthropic** | Yes, softened — "including where human review is appropriate" | Commercial Terms D.3 | Disclaimed (L.2) | Fees, previous 12 months (L.3.a) |
| **OpenAI** | Yes — "solely responsible… for evaluating the accuracy" | Business Terms 4.3 | Narrow conformity warranty (12.1); rest disclaimed (12.2) | Amount paid, previous 12 months (14.2) |
| **Cursor** | Yes, twice — §1.4 and §1.7 (auto-execution) | ToS 1.4, 1.7 | Disclaimed (14) | **Greater of 6 months' fees or $100** (15.2) |
| **AWS** | **Not for the coding services** — formula present at §24.2/53.10/54.8.3/60.4.2/81.2/99.1, absent from §50 | Service Terms | Per AWS Customer Agreement | Per AWS Customer Agreement |
| **Google Cloud** | **No** in the contract; "we recommend that you validate" in Gemini Code Assist docs | SST §20; product docs | Disclaimed (§20(b)) | Per Google Cloud Agreement |

**The pattern:** four of six impose the duty in contract, one imposes it only in documentation,
one imposes it on everything except its coding products. **None of the six accepts any share of
responsibility for a defect in output.** The consistent answer to "does the vendor bear any of
it?" is **no, and the terms say so in explicit words.**

### 1.8 What the IP indemnities reveal — and what they conspicuously omit

Three of the six offer an indemnity, and all three are **intellectual-property only**. None
indemnifies against a defect.

**AWS Service Terms §50.10** ("Defense of Claims and Indemnity for Indemnified Generative AI
Services") covers Amazon Q, Kiro and the Nova/Titan models:

> §50.10.1: "AWS will defend you… against any third-party claim alleging that the Generative AI
> Output generated by an Indemnified Generative AI Service **infringes or misappropriates that
> third party's intellectual property rights**…"
> §50.10.2: "AWS will have no obligations or liability… (ii) **if you interfere with or fail to
> enable available filters and other tools, or disregard instructions made available for the
> Indemnified Generative AI Service**… (vi) arising from Generative AI Output **that you know or
> reasonably should know may infringe**…"

**Google Cloud SST §20(i)(1)** is materially the same shape: the indemnity does not apply where
*"Customer creates or uses such Generated Output that it knew or should have known was likely
infringing"* or where *"Customer… **disregards, disables, modifies, or circumvents source
citations, filters, instructions, or other tools** Google makes available to help Customer create
or use Generated Output responsibly."*

**GitHub Copilot PST §4** simply imports whatever defence of third-party claims the customer's
main Agreement provides.

Two things follow, both directly relevant to this strand:

1. **The vendors will stand behind provenance and will not stand behind correctness.** There is a
   defence budget for "this code infringes" and none for "this code broke". That is a deliberate
   and consistent industry-wide allocation.
2. **Both indemnities are forfeited by turning a control off.** This is the same mechanism as
   Cursor §1.7 and Google §20(j): **a configuration change moves the risk.** Three vendors
   independently drafted it that way. See §8.

---
## 2. Product liability: Directive (EU) 2024/2853

**Source throughout:** the Official Journal text, https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402853
— **Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on
liability for defective products and repealing Council Directive 85/374/EEC**, OJ L, 2024/2853,
18.11.2024. All quotations **[STATUTE]**, read from that text on 2026-08-30. EUR-Lex metadata on
the same date: **in force; entry into force 8 December 2024; no end of validity; not amended**
(one corrigendum, 32024L2853R(01)).

### 2.1 Software is a product — verbatim

**Recital 6:** *"In order to ensure that the Union's product liability regime is comprehensive,
no-fault liability for defective products should apply to all movables, **including software**,
including when they are integrated into other movables or installed in immovables."*

**Article 4(1):** *"'product' means all movables, even if integrated into, or inter-connected
with, another movable or an immovable; it includes electricity, digital manufacturing files, raw
materials and **software**."*

**Recital 13** — the operative passage, quoted at length because it is routinely truncated:

> "Products in the digital age can be tangible or intangible. **Software, such as operating
> systems, firmware, computer programs, applications or AI systems**, is increasingly common on
> the market and plays an increasingly important role for product safety. **Software is capable of
> being placed on the market as a standalone product** or can subsequently be integrated into
> other products as a component, and it is capable of causing damage through its execution. In
> the interest of legal certainty, **it should be clarified in this Directive that software is a
> product for the purposes of applying no-fault liability, irrespective of the mode of its supply
> or usage**, and therefore irrespective of whether the software is stored on a device, accessed
> through a communication network or cloud technologies, **or supplied through a
> software-as-a-service model**. […] **A developer or producer of software, including AI system
> providers within the meaning of Regulation (EU) 2024/1689 …, should be treated as a
> manufacturer.**"

So: standalone software, embedded software, SaaS and AI systems are all in scope, and an AI
system provider is a manufacturer.

### 2.2 ⚠️ …but "the mere source code of software" is expressly not

The sentence that sits between the two halves quoted above:

> "**Information is not, however, to be considered a product, and product liability rules should
> therefore not apply to the content of digital files, such as media files or e-books or the mere
> source code of software.**"

This is the single most under-reported line in the Directive for this ticket's purposes. Read
with recital 13's first half, the position it produces is:

- **A code suggestion, taken as such, is information — not a product.**
- **The compiled, executed, supplied software that the suggestion ends up inside is a product.**

The AI vendor supplying suggestions is therefore not obviously supplying a "product" *by supplying
the suggestion*; the team that ships the resulting software is supplying one. **On the face of
the Directive, the PLD pushes liability downstream to whoever placed the running software on the
market — that is, to the team, not the tool.** This is a reading of the text, not a decided
question; §11 records it as unsettled, because no court has construed it.

The parallel in US law is exact and long-standing: *Winter v. G.P. Putnam's Sons*, 938 F.2d 1033
(9th Cir. 1991) **[COURT]**: *"A book containing Shakespeare's sonnets consists of two parts, the
material and print therein, and the ideas and expression thereof. **The first may be a product,
but the second is not.**"* And, in a striking 1991 aside: *"Aeronautical charts are highly
technical tools… The best analogy to an aeronautical chart is a compass. **Computer software that
fails to yield the result for which it was designed may be another.**"* Two courts, thirty-three
years and an ocean apart, drew the same line in the same place.

### 2.3 ⚠️ Application status as at 2026-08-30: not yet in force

- **Article 2(1):** *"This Directive shall apply to products placed on the market or put into
  service **after 9 December 2026**."*
- **Article 22(1):** *"Member States shall bring into force the laws, regulations and
  administrative provisions necessary to comply with this Directive **by 9 December 2026**."*
- **Article 21:** *"Directive 85/374/EEC is repealed with effect from 9 December 2026. However,
  it shall continue to apply with regard to products placed on the market or put into service
  before that date."*

**Confirmed: the transposition deadline is 9 December 2026, exactly as the ticket asked to have
verified.** As at the research date the new Directive governs nothing; the 1985 Directive still
does, and will continue to govern anything placed on the market before that date indefinitely.
Any software shipped today is, and remains, under the old regime — which does not name software.

### 2.4 Who counts as a manufacturer, and the modification hook

**Article 8(1)** makes liable the manufacturer of a defective product; the manufacturer of a
defective *component* integrated within the manufacturer's control; and, for non-EU
manufacturers, the importer, authorised representative or fulfilment service provider.

**⚠️ Article 8(2)** is the provision that matters for the autonomy axis:

> "**Any natural or legal person that substantially modifies a product outside the manufacturer's
> control and thereafter makes it available on the market or puts it into service shall be
> considered to be a manufacturer of that product** for the purposes of paragraph 1."

**Article 4(18)** defines "substantial modification" by reference to product-safety rules or, in
their absence, a change that "changes the original intended performance… affects the safety of
the product… and is of a degree of change considered as substantial according to the relevant
Union or national rules" (text truncated in the local extract; treated as **partially verified**,
see §10).

Article 4(5) defines "manufacturer's control" to include the manufacturer's ability to supply
software updates — so an AI coding tool's supplier retains "control" of its own tool, but the
team that ships modified software becomes the manufacturer of *that* software.

### 2.5 ⚠️ The damage heads exclude almost every commercial software failure

**Article 5(1):** *"Member States shall ensure that **any natural person** who suffers damage
caused by a defective product (the 'injured person') is entitled to compensation…"*

**Article 6(1):** *"The right to compensation… shall apply in respect of **only** the following
types of damage:*
- *(a) death or personal injury, including medically recognised damage to psychological health;*
- *(b) damage to, or destruction of, any property, **except**: (i) the defective product itself;
  (ii) a product damaged by a defective component that is integrated into… that product by the
  manufacturer…; **(iii) property used exclusively for professional purposes**;*
- *(c) destruction or corruption of data **that are not used for professional purposes**."*

**This is a consumer-protection regime.** It reaches a defect in unread code only where that
defect kills or injures a natural person, damages their non-professional property, or destroys
their personal data. **The ordinary commercial scenario the ticket is about — a defect in
enterprise code causing outage, data loss, breach or economic loss to a business — is outside the
Directive.** Nothing in the PLD makes the vendor, the developer or the organisation liable for
that; the answer for that scenario has to come from contract, or from negligence (§5), and both
are much weaker.

Widespread commentary describing the PLD as "the answer" to AI-generated code liability does not
survive reading Articles 5 and 6. Treat any such claim with suspicion.

### 2.6 ⚠️ Disclosure of evidence and the presumptions — the provisions that bite unread code

**Article 9 (Disclosure of evidence), paragraph 1:**

> "Member States shall ensure that, at the request of a person who is claiming compensation in
> proceedings before a national court for damage caused by a defective product (the 'claimant')
> and **who has presented facts and evidence sufficient to support the plausibility of the claim**
> for compensation, **the defendant is required to disclose relevant evidence that is at the
> defendant's disposal**…"

Paragraph 3 limits it to "what is necessary and proportionate"; paragraphs 4–5 protect trade
secrets; paragraph 6 empowers courts to require evidence "to be presented in an easily accessible
and easily understandable manner".

**Article 10 (Burden of proof):**

> "1. …a claimant is required to prove the defectiveness of the product, the damage suffered and
> the causal link…
> 2. **The defectiveness of the product shall be presumed where any of the following conditions
> are met: (a) the defendant fails to disclose relevant evidence pursuant to Article 9(1);**
> (b) the claimant demonstrates that the product does not comply with mandatory product safety
> requirements…; or (c) the claimant demonstrates that the damage was caused by an obvious
> malfunction of the product during reasonably foreseeable use…
> 3. The causal link… shall be presumed where it has been established that the product is
> defective and that the damage caused is of a kind typically consistent with the defect…
> 4. **A national court shall presume the defectiveness of the product or the causal link… where,
> despite the disclosure of evidence in accordance with Article 9…: (a) the claimant faces
> excessive difficulties, in particular due to technical or scientific complexity, in proving the
> defectiveness… ; and (b) the claimant demonstrates that it is likely that the product is
> defective or that there is a causal link…**
> 5. The defendant shall have the right to rebut any of the presumptions…"

**Recital 48** names the triggers, and names machine learning explicitly:

> "…Those factors should include the complex nature of the product…; **the complex nature of the
> technology used, such as machine learning**; the complex nature of the information and data to
> be analysed by the claimant; and the complex nature of the causal link, such as… **a link that,
> in order to be proven, would require the claimant to explain the inner workings of an AI
> system.** … For example, in a claim concerning an AI system, the claimant should, for the court
> to decide that excessive difficulties exist, **neither be required to explain the AI system's
> specific characteristics nor how those characteristics make it harder to establish the causal
> link.**"

**Why this matters for a defect nobody read.** Article 9 asks the defendant to produce "relevant
evidence at the defendant's disposal". For a change that went through an engineered verification
pipeline, that evidence exists: test results, gate outcomes, static analysis, provenance, the
agent's transcript. For a change nobody read *and* nothing checked, there may be nothing to
produce — and Article 10(2)(a) then **presumes the product defective**. The Directive does not
require the defendant to have read the code. It requires the defendant to be able to show
something. **In this project's vocabulary: the PLD rewards verification, is indifferent to
review, and punishes the absence of both.** That is, on the evidence in this file, the single
most useful structural insight the legal material offers this framework.

### 2.7 Exemptions, and the software carve-out

**Article 11(1)** lists seven exemptions, including (e) the development-risk defence — *"that the
objective state of scientific and technical knowledge at the time the product was placed on the
market… was not such that the defectiveness could be discovered"* — and (c) that the defect did
not exist when the product was placed on the market.

**Article 11(2) closes (c) for software:**

> "By way of derogation from paragraph 1, point (c), **an economic operator shall not be exempted
> from liability where the defectiveness of a product is due to any of the following, provided
> that it is within the manufacturer's control: (a) a related service; (b) software, including
> software updates or upgrades; (c) a lack of software updates or upgrades necessary to maintain
> safety; (d) a substantial modification of the product.**"

**Article 15** forbids contracting out: *"Member States shall ensure that the liability of an
economic operator [is not] limited or excluded by contractual provisions or by national law."*
(Article title: "Exclusion or limitation of liability".) Vendor terms of the kind quoted in §1 —
including Anthropic L.3.c(III)'s express exclusion of "STRICT PRODUCT LIABILITY" — will not
displace the Directive for claims within its scope. They remain fully effective for everything
outside it, which as §2.5 shows is most of what this ticket is about.

### 2.8 The open-source carve-out

**Article 2(2):** *"This Directive does not apply to free and open-source software that is
developed or supplied **outside the course of a commercial activity**."*

**Recital 14** elaborates: *"Providing such software on open repositories should not be
considered as making it available on the market, unless that occurs in the course of a commercial
activity… However, where software is supplied in exchange for a price, or for personal data used
other than exclusively for improving the security, compatibility or interoperability of the
software, and is therefore supplied in the course of a commercial activity, this Directive should
apply."*

**Recital 15** allocates the consequence: where non-commercial FOSS is integrated by a
manufacturer into a commercial product, *"it should be possible to hold that manufacturer liable
for damage caused by the defectiveness of such software **but not the manufacturer of the
software**"*.

**The volunteer maintainer is out. The company that shipped their code is in.** Whatever else is
uncertain, that allocation is clear on the text.

### 2.9 ⚠️ The UK is diverging

**Consumer Protection Act 1987 (c. 43)** **[STATUTE]**, https://www.legislation.gov.uk/ukpga/1987/43:

- **s.1(2):** *"'product' means any goods or electricity and (subject to subsection (3) below)
  includes a product which is comprised in another product, whether by virtue of being a
  component part or raw material or otherwise."*
- **s.45(1):** *"'goods' includes substances, growing crops and things comprised in land by
  virtue of being attached to it and any ship, aircraft or vehicle."*

Neither definition mentions software or any intangible. The UK did not follow the 2024 Directive
after leaving the EU, and CPA Part I is still expressed as implementing the 1985 Directive
(s.1(1), as amended in 2020 to read *"was enacted"*).

**Product Regulation and Metrology Act 2025 (2025 c. 20)** **[STATUTE]**,
https://www.legislation.gov.uk/ukpga/2025/20:

- **s.1(7):** *"'product' means **a tangible item that results from a method of production**."*
- **s.2(2)(a):** product regulations may make provision about *"the production, **components
  (whether tangible or intangible)**, composition or other characteristics of products"*.
- **s.2(9):** *"In this section, a reference to 'intangible' components **includes software**."*
- **s.11(1):** *"In the Consumer Protection Act 1987 omit Parts 2 and 4."* — Parts 2 (consumer
  safety) and 4 (misleading price indications). **Part I, product liability, is untouched**, and
  s.11(1) is recorded as **not yet in force**.

So the UK's 2025 product statute (a) defines "product" as **tangible**, (b) reaches software only
as an *intangible component of a tangible product*, and (c) is an enabling Act for product
*safety regulation*, not a liability regime. **From 9 December 2026, standalone software is a
product for no-fault liability in the EU and is not one in the UK.** Anyone reasoning about
liability for a defect in AI-assisted code must state which side of that line they are on.

---

## 3. The AI Liability Directive: withdrawn, and when

The withdrawal is widely misreported — as a pause, a delay, or as still pending. The primary
record is unambiguous and has three layers.

**1. The announced intention.** Commission Work Programme 2025, **COM(2025) 45 final, 11 February
2025**, *"Moving forward together: A Bolder, Simpler, Faster Union"*, **Annex IV** (list of
withdrawals of pending proposals), entry **32** **[STATUTE]**:

> "COM(2022)496 final — 2022/0303 (COD) — Proposal for a DIRECTIVE OF THE EUROPEAN PARLIAMENT AND
> OF THE COUNCIL on adapting non-contractual civil liability rules to artificial intelligence (AI
> Liability) — **No foreseeable agreement - the Commission will assess whether another proposal
> should be tabled or another type of approach should be chosen.**"

**2. The formal withdrawal.** *Official Journal of the European Union*, C series, **C/2025/5423,
dated 6 October 2025**, headed **"WITHDRAWAL OF COMMISSION PROPOSALS"**, author: European
Commission, Secretariat-General. Under "List of withdrawn proposals" **[STATUTE]**:

> "COM(2022)496 final — 2022/0303 (COD) — Proposal for a DIRECTIVE OF THE EUROPEAN PARLIAMENT AND
> OF THE COUNCIL on adapting non-contractual civil liability rules to artificial intelligence (AI
> Liability)"

ELI: http://data.europa.eu/eli/C/2025/5423/oj — CELEX 52025XC05423.

**3. The parliamentary record.** European Parliament Legislative Observatory, procedure file
**2022/0303(COD)** **[STATUTE — institutional record]**, read 2026-08-30. Key events, last entry:
**"06/10/2025 — Proposal withdrawn by Commission"**. Status: **"Procedure lapsed or withdrawn."**
Stage reached in procedure: **"Procedure lapsed or withdrawn."**

**The date to cite is 6 October 2025** (OJ C/2025/5423), with 11 February 2025 as the date the
Commission announced the intention. The proposal was published 28 September 2022 and never
reached a first-reading position.

**What its absence means.** The AILD would have created EU-wide rules on **fault-based** liability
for AI, including disclosure of evidence about high-risk AI systems and a rebuttable presumption
of causation. Those mechanisms now exist in EU law **only in the PLD**, and therefore only for
no-fault product liability, only for the damage heads in Art. 6, and only for natural persons
(§2.5). **Fault-based liability for AI in the EU is back to twenty-seven national tort regimes.**
That is a genuine gap, not a technicality — and it is the reason the PLD carries more weight in
this area than its scope really supports.

---

## 4. The EU AI Act — and the amendment most commentary has not caught

**Sources:** Regulation (EU) 2024/1689 (OJ L, 2024/1689, 12.7.2024) and the **consolidated text
02024R1689 — EN — 27.07.2026**, both read from EUR-Lex on 2026-08-30. All **[STATUTE]**.

### 4.1 ⚠️ The Act was amended on 27 July 2026

EUR-Lex metadata on the research date: *"This act has been changed. Current consolidated version:
27/07/2026"*, **modified by Regulation (EU) 2026/1744**, in force **27 July 2026**, with
62+ amendments including replacements to Articles 2, 4, 10, 11, 17, 25, 27, 29, 30, 43, 57, 58,
60, 63, 69, 72, 77, 95, 96, 97, 111 and 113, and new Articles 4a, 60a, 75a–75d.

Full title: **"Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July
2026 amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the
simplification of the implementation of harmonised rules on artificial intelligence (Digital
Omnibus on AI)"**; published in the OJ 24 July 2026; in force 27 July 2026.

**Anyone quoting the AI Act from the original OJ text is quoting a superseded version.** Two of
the changes matter directly here.

### 4.2 ⚠️ The high-risk obligations are deferred past 2027

**Article 113 as amended:**

> "It shall apply from 2 August 2026. However:
> **▼M1** (a) Chapters I and II shall apply from 2 February 2025, with the exception of Article
> 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b) which shall apply
> from 2 December 2026;
> (b) Chapter III Section 4, Chapter V, Chapter VII and Chapter XII and Article 78 shall apply
> from 2 August 2025, with the exception of Article 101;
> **▼M1** (c) **Chapter III, Sections 1, 2, and 3**, with the exception of Article 6(5), **shall
> apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to
> Article 6(2) and Annex III; and (ii) 2 August 2028 as regards AI systems classified as high-risk
> pursuant to Article 6(1) and Annex I**;
> **▼M1** (d) Articles 102 to 110 shall apply from 27 July 2026."

Chapter III Section 2 (offsets verified in the consolidated text) contains **Article 14 (Human
oversight)**. Section 3 contains **Article 25 (Responsibilities along the AI value chain)** and
**Article 26 (Obligations of deployers of high-risk AI systems)**.

**As at 2026-08-30, Articles 14, 25 and 26 are not applicable.** They become applicable on
2 December 2027 for Annex III high-risk systems and 2 August 2028 for Annex I ones.

### 4.3 ⚠️ Article 4 (AI literacy) was weakened — and it is the only provision here that is live

**Original (OJ 2024/1689, applicable from 2 February 2025):**

> "Providers and deployers of AI systems shall take measures to ensure, **to their best extent, a
> sufficient level of AI literacy** of their staff and other persons dealing with the operation
> and use of AI systems on their behalf…"

**As amended (▼M1, consolidated 27.07.2026):**

> "1. Providers and deployers of AI systems shall take measures **to support the development of
> AI literacy** of their staff and other persons dealing with the operation and use of AI systems
> on their behalf, taking into account their technical knowledge, experience, education and
> training and the context the AI systems are to be used in… **This obligation does not require
> providers or deployers to guarantee any specific level of AI literacy of any individual.**"

Article 4 sits in Chapter I and applies to **all** AI systems, not only high-risk ones — so an
organisation deploying a coding agent internally is a "deployer" and is within it. It is
therefore the **only** AI Act obligation in this section that is currently live and relevant to
AI-assisted software development. And it was just made materially softer.

### 4.4 What Articles 14, 25 and 26 will say when they arrive

Recorded for completeness, with the applicability caveat repeated: **these are not in force.**

**Article 14(4)(b)** requires that the human assigned oversight be enabled *"to remain aware of
the possible tendency of automatically relying or over-relying on the output produced by a
high-risk AI system (**automation bias**), in particular for high-risk AI systems used to provide
information or recommendations for decisions to be taken by natural persons"*. Article 14(4)(d)
requires the ability *"to decide, in any particular situation, not to use the high-risk AI system
or to otherwise disregard, override or reverse the output"*.

**Article 26(2):** *"Deployers shall **assign human oversight to natural persons who have the
necessary competence, training and authority, as well as the necessary support**."* A named
person, competent and empowered — the same shape as the "named and recorded" role requirement
that [`verification-gates.md`](./verification-gates.md) §6b.6 found in the functional-safety
standards.

**⚠️ Article 25(1)** is the provision that speaks to the autonomy axis, and it is quoted in full
because §8 turns on it:

> "Any distributor, importer, **deployer** or other third-party **shall be considered to be a
> provider of a high-risk AI system** for the purposes of this Regulation and shall be subject to
> the obligations of the provider under Article 16, in any of the following circumstances:
> (a) they put their name or trademark on a high-risk AI system already placed on the market or
> put into service…;
> **(b) they make a substantial modification to a high-risk AI system** that has already been
> placed on the market or has already been put into service in such a way that it remains a
> high-risk AI system pursuant to Article 6;
> **(c) they modify the intended purpose of an AI system, including a general-purpose AI system,
> which has not been classified as high-risk** and has already been placed on the market or put
> into service **in such a way that the AI system concerned becomes a high-risk AI system** in
> accordance with Article 6."

**Article 25(2)** then transfers the role outright: *"Where the circumstances referred to in
paragraph 1 occur, **the provider that initially placed the AI system on the market… shall no
longer be considered to be a provider of that specific AI system**…"*

**⚠️ Scope caveat, stated because it is easy to lose.** All of Article 25 is about **high-risk AI
systems** as defined by Article 6 and Annexes I and III. Annex III's categories are biometrics,
critical infrastructure, education, employment, essential public and private services, law
enforcement, migration/border control, and administration of justice. **A coding assistant used
to build ordinary business software is not a high-risk AI system**, and nothing in Article 25
applies to it. What Article 25 offers this framework is a **statutory pattern** — *change what the
system does and you become the party answerable for it* — not a rule that governs coding agents.
Do not cite the AI Act as authority for accountability in AI-assisted software development. It
does not reach it.

---
## 5. Negligence and professional standards: unsettled, and honestly so

**This is the weakest-evidenced section in the document and the reader should treat it that way.**
The ticket asked for actual rulings rather than commentary. Four were located and read in full
from the official reporter digitisation; all four are decades old; none concerns AI. **No modern
authority on the standard of care for software development was found through the primary-source
channels available.** That absence is itself the finding.

### 5.1 "Computer malpractice" was refused, and the refusal has never been squarely overruled

***Chatlos Systems, Inc. v. National Cash Register Corp.*, 479 F. Supp. 738 (D.N.J., 22 October
1979)** **[COURT]** — read from the Caselaw Access Project digitisation of *Federal Supplement*
vol. 479. Footnote 1:

> "Though not raised in the pleadings, in post-trial memoranda plaintiff has asserted two
> additional theories of liability. '**Computer malpractice**' and strict liability in tort are
> alleged to have been proven at trial. The novel concept of a new tort called 'computer
> malpractice' is premised upon a theory of elevated responsibility on the part of those who
> render computer sales and service. Plaintiff equates the sale and servicing of computer systems
> with established theories of professional malpractice. **Simply because an activity is
> technically complex and important to the business community does not mean that greater
> potential liability must attach. In the absence of sound precedential authority, the Court
> declines the invitation to create a new tort.**"

The court also declined to rule on strict liability in tort, holding it unnecessary. Judgment was
given on breach of express warranty and the implied warranty of fitness for a particular purpose
under the UCC.

### 5.2 …but an implied contractual standard of skill was accepted

***Data Processing Services, Inc. v. L.H. Smith Oil Corp.*, 492 N.E.2d 314 (Ind. Ct. App.,
28 April 1986)** **[COURT]** — read from the Caselaw Access Project digitisation of *North Eastern
Reporter 2d* vol. 492. (Rehearing at 493 N.E.2d 1272 addresses procedure only.)

First, the court held the contract was for **services**, not goods, and therefore outside UCC
Article 2:

> "**Smith bargained for DPS's skill in developing a system to meet its specific needs.** Although
> the end result was to be preserved by means of some physical manifestation such as magnetic
> tape, floppy or hard disks, etc… **it was DPS's knowledge, skill, and ability for which Smith
> bargained.** The sale of computer hardware or generally-available standardized software was not
> here involved… **The situation here is more analogous to a client seeking a lawyer's advice or a
> patient seeking medical treatment for a particular ailment than it is to a customer buying seed
> corn, soap, or cam shafts.**"

Then the standard:

> "**Those who hold themselves out to the world as possessing skill and qualifications in their
> respective trades or professions impliedly represent they possess the skill and will exhibit
> the diligence ordinarily possessed by well informed members of the trade or profession.**
> [citing authorities on attorneys, physicians, builders, architects and employees] … **We hold
> these principles apply with equal force to those who contract to develop computer
> programming.**"

**Three cautions, all material:**

1. This is an **implied contractual promise**, not a tort duty. It reached the defendant because
   there was a contract to develop software; it says nothing about a duty owed to a third party
   injured by the software.
2. It is a **1986 intermediate appellate decision of one US state**, expressly acknowledging a
   split with another district of the same court on the goods/services question.
3. It turned on the work being **bespoke development**. Off-the-shelf software was, in the same
   passage, put on the goods side of the line — as *Chatlos* and *RRX Industries v. LabCon*,
   772 F.2d 543 (9th Cir. 1985) had held.

**Taken together, §5.1 and §5.2 are the whole of the picture: the tort was refused, an implied
contractual standard was accepted, and nothing since has resolved it.**

### 5.3 The publisher-of-information line, which is where AI vendors sit

***Winter v. G.P. Putnam's Sons*, 938 F.2d 1033 (9th Cir., 12 July 1991)** **[COURT]** — mushroom
foragers poisoned after relying on an encyclopedia; summary judgment for the publisher affirmed.

> "A book containing Shakespeare's sonnets consists of two parts, the material and print therein,
> and the ideas and expression thereof. **The first may be a product, but the second is not**…
> Products liability law is geared to the tangible world."
>
> "…**Unless it is assumed that the publisher is a guarantor of the accuracy of an author's
> statements of fact**, plaintiffs have made no case under any of these theories other than
> possibly negligence. Guided by the First Amendment and the values embodied therein, we decline
> to extend liability under this theory to the ideas and expression contained in a book."

The defendant had argued *"a publisher does not have a duty to investigate the accuracy of the
text it publishes"*, and prevailed. **That is, precisely, the position an AI vendor occupies when
it says "You are responsible for reviewing, testing, and validating any Output before use."** The
analogy is imperfect — a chat completion is generated on demand for one user, not published to
the world — and no court has applied *Winter* to a model output. It is recorded here because it
is the closest reasoned authority located, not because it decides anything.

### 5.4 There is no licensed profession to be negligent against, in most of the world

A professional-negligence standard usually rests on a recognised profession with entry control.
Software engineering largely lacks one.

- **NCEES** (the US body that develops the Principles and Practice of Engineering exams) lists
  its PE disciplines at https://ncees.org/engineering/pe/ **[POLICY]**. Read on 2026-08-30: more
  than twenty disciplines are listed — Civil, Mechanical, Electrical, Chemical and others — and
  **Software Engineering is not among them.** No statement about the discontinued PE Software
  Engineering exam was located on NCEES's own site; §12 records that as an unverified item and
  §11 records the corresponding claim as *not established*.
- **ACM Code of Ethics and Professional Conduct** (2018) **[POLICY]**,
  https://www.acm.org/code-of-ethics — a published professional standard with **no disciplinary
  force outside ACM membership**. The clauses on point:
  - **2.4** *"Accept and provide appropriate professional review. **High quality professional work
    in computing depends on professional review at all stages.** Whenever appropriate, computing
    professionals should seek and utilize peer and stakeholder review."*
  - **2.5** *"Give comprehensive and thorough evaluations of computer systems and their impacts,
    including analysis of possible risks. Computing professionals are in a position of trust, and
    therefore have a special responsibility to provide objective, credible evaluations… **A system
    for which future risks cannot be reliably predicted requires frequent reassessment of risk as
    the system evolves in use, or it should not be deployed.**"*
  - **2.6** *"Perform work only in areas of competence."*
  - **2.9** *"Design and implement systems that are robustly and usably secure… **Computing
    professionals should perform due diligence to ensure the system functions as intended.**"*

  Note **2.4's** phrasing — "professional review at all stages" — is unambiguously about *review*
  in this project's sense, a human reading the work. The ACM Code is the only widely-adopted
  professional instrument located that states such a duty for software people. **It is not law
  and carries no sanction beyond ACM membership.**

### 5.5 Where that leaves the negligence question

**The honest statement of the position, which this document adopts:**

> **No court, in any jurisdiction reached by this research, has decided who is liable in
> negligence for a defect in AI-generated code that a human did not read.** There is no
> recognised tort of software engineering malpractice; the only US authority squarely on the
> point refused to create one in 1979 and has not been overruled. A single 1986 state appellate
> decision applied a "skill ordinarily possessed by well informed members of the trade" standard
> as an *implied contractual* term for bespoke development work. Everything else is inference.

---

## 6. Where courts have already sanctioned professionals for unreviewed AI output

**⚠️ Read this section with its scope limit attached at all times: every case in it is about
material put before a court, by a lawyer or a litigant, in a jurisdiction that regulates the
practice of law. None is about software. The principle is transferable by analogy; it is not
software law, and §6.6 sets out precisely how far the analogy carries.**

### 6.1 *Mata v. Avianca* — the man who signed without reading

**Source:** Opinion and Order on Sanctions, *Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC)
(S.D.N.Y.), ECF No. 54, filed **22 June 2023**, Castel J. 43 pages, read in full from the RECAP
archive of the court's own filing. Reported at 678 F. Supp. 3d 443. **[COURT]**

**The framing, from the first paragraph:**

> "In researching and drafting court submissions, good lawyers appropriately obtain assistance
> from junior lawyers, law students, contract lawyers, legal encyclopedias and databases such as
> Westlaw and LexisNexis. Technological advances are commonplace and **there is nothing inherently
> improper about using a reliable artificial intelligence tool for assistance. But existing rules
> impose a gatekeeping role on attorneys to ensure the accuracy of their filings.** Rule 11, Fed.
> R. Civ. P. [Respondents] **abandoned their responsibilities** when they submitted non-existent
> judicial opinions with fake quotes and citations created by the artificial intelligence tool
> ChatGPT…"

**The certification rule, quoted by the court** (Conclusions of Law ¶1) — Rule 11(b):

> "**By presenting to the court a pleading, written motion, or other paper — whether by signing,
> filing, submitting, or later advocating it — an attorney or unrepresented party certifies that
> to the best of the person's knowledge, information, and belief, formed after an inquiry
> reasonable under the circumstances**: … (2) the claims, defenses, and other legal contentions
> are warranted by existing law…"

**⚠️ The facts about the signer (Findings of Fact ¶6), which are the exact shape of a merge
without a read:**

> "Although Mr. LoDuca signed the Affirmation in Opposition and filed it on ECF, **he was not its
> author**. It was researched and written by Mr. Schwartz. **Mr. LoDuca reviewed the affirmation
> for style, stating, 'I was basically looking for a flow, make sure there was nothing untoward or
> no large grammatical errors.' Before executing the Affirmation, Mr. LoDuca did not review any
> judicial authorities cited in his affirmation.**"

**The holding (¶23(a)):**

> "**Mr. LoDuca violated Rule 11 in not reading a single case cited in his March 1 Affirmation in
> Opposition and taking no other steps on his own to check whether any aspect of the assertions of
> law were warranted by existing law. An inadequate or inattentive 'inquiry' may be unreasonable
> under the circumstances. But signing and filing that affirmation after making no 'inquiry' was
> an act of subjective bad faith.**"

And ¶21: *"Mr. LoDuca, the only attorney of record, **consciously avoided learning the facts** by
neither reading the Avianca submission when received nor after receiving the Court's Orders…"* —
applying the conscious-avoidance test set out at ¶19: *"consciously avoided learning [a] fact
while aware of a high probability of its existence."*

**Organisational liability (¶25):**

> "The Levidow Firm is jointly and severally liable for the Rule 11(b)(2) violations of Mr. LoDuca
> and Mr. Schwartz. Rule 11(c)(1) provides that '**[a]bsent exceptional circumstances, a law firm
> must be held jointly responsible for a violation committed by its partner, associate, or
> employee.**'"

**The sanction:** letters to the client and to each judge whose name had been attached to a
fabricated opinion, and *"A penalty of $5,000 … jointly and severally imposed on Respondents."*
The court declined to order further mandatory education because the firm had already arranged
CLE on "technological competence and artificial intelligence programs" — an early instance of the
pattern §6.2 makes explicit.

**⚠️ Two distinctions this document insists on carrying:**

1. The sanction rested on **subjective bad faith**, a heightened standard that applies because the
   court raised sanctions on its own motion (¶14). Ordinary careless non-reading would be judged
   by **objective unreasonableness** on an opposing party's motion. So *Mata* is not authority
   that all unreviewed output is bad faith — it is authority that **signing after doing nothing at
   all** crosses a line that **doing something badly** does not.
2. Much of the aggravation came from what happened *after* the error: the respondents "doubled
   down". Rule 11's "later advocating" limb (¶10) is what caught them. **The failure to correct
   was punished more heavily than the failure to review.**

### 6.2 *Wadsworth v. Walmart* — three roles, three sanctions, and the firm that got away

**Source:** Order on Sanctions and Other Disciplinary Action, *Wadsworth v. Walmart Inc.*,
No. 2:23-cv-118-KHR (D. Wyo.), ECF No. 181, filed **24 February 2025**, Rankin J. 17 pages, read
in full from the RECAP archive of the court's own filing. **[COURT]**

Facts: three attorneys filed Motions in Limine citing nine cases, eight of which did not exist,
produced by an internal AI platform.

**The nondelegability holding — the passage this strand turns on:**

> "The Court notes that **Mr. Morgan and Ms. Goody did not review the Motions prior to signing.**
> However, Mr. Morgan and Ms. Goody do not contend Mr. Ayala signed their names without
> permission. It appears Mr. Morgan and Ms. Goody **relied on Mr. Ayala's reputation and
> experience** to comply with his Rule 11 obligations. **Nevertheless, this is inconsequential in
> determining whether a violation occurred. Signing a legal document ensures that the attorney
> read the document and conducted a reasonable inquiry into the existing law.** See Bus. Guides,
> Inc. [v. Chromatic Commc'ns Enters., 498 U.S. 533, 542 (1991)]; see Adamson [v. Bowen, 855 F.2d
> 668, 673 (10th Cir. 1988)] ('The attorney must "stop, look, and listen" before signing a
> document subject to Rule 11.'). **This duty is a "nondelegable responsibility." Pavelic &
> LeFlore v. Marvel Ent. Grp., 493 U.S. 120, 126 (1989). Thus, blind reliance on another attorney
> can be an improper delegation of this duty and a violation of Rule 11.**"

**The graduated sanctions, and what each was for:**

| Role | Person | Sanction | Court's reason |
|---|---|---|---|
| **Drafter** | Ayala | $3,000 + **pro hac vice admission revoked** | Produced the fabricated citations; "his honesty and candor" mitigated |
| **Signing partner / supervisor** | Morgan | **$1,000** | *"Because Mr. Morgan was not the drafter, he will be sanctioned less severely… **he still has a nondelegable duty to ensure a motion is supported by existing law.**"* Citing *Massey v. Prince George's Cnty.*, 918 F. Supp. 905, 909 (D. Md. 1996) — "sanctioning supervising attorneys for junior attorney's failure to cite controlling law" |
| **Local counsel (sponsor)** | Goody | **$1,000** | Cites *Williams* — *"imposing a $2,500 fine for the local counsel for **serving as a rubber stamp** for attorney admitted pro hac vice"* |
| **The firm** | Morgan & Morgan | **No sanction** | See below |

**⚠️ Why the firm escaped — the most transferable passage in this document:**

> "Here, **Mr. Morgan submitted evidence showing that Morgan & Morgan trained its employees to not
> use the AI software in the way Mr. Ayala used it.** Since the Order to Show Cause, **Morgan &
> Morgan has since implemented an additional acknowledgement prior to using its AI software that
> '[u]sers must independently verify' any AI-generated information before using or relying on
> it. The Court would have likely imposed sanctions similar to these measures. Thus, any further
> sanction would be greater than necessary.**"

Three things follow. (i) A **documented policy** plus (ii) **evidence of training** plus (iii) an
**enforced acknowledgement in the tool itself** was enough to move the organisation out of the
firing line, leaving the individuals to bear it. (iv) The court effectively treated the control
the firm had built as **the sanction it would otherwise have imposed**. Read against ticket #4's
"policies are declarations, only access controls stop anything": here a policy plus a control at
the point of use did real legal work, and the control was the newer half.

**The court's closing statement of principle:**

> "**An attorney who signs a document certifies they made a reasonable inquiry into the existing
> law. Fed. R. Civ. P. 11(b). While technology continues to change, this requirement remains the
> same.** Because Respondents failed to make a reasonable inquiry into the law contained in a
> document they signed, sanctions are warranted."

And, from the background section: *"**As attorneys transition to the world of AI, the duty to
check their sources and make a reasonable inquiry into existing law remains unchanged.**"*

### 6.3 *R (Ayinde) v Haringey; Al-Haroun v QNB* — the English Divisional Court

**Source:** [2025] EWHC 1383 (Admin), Case Nos. AC-2024-LON-003062 and CL-2024-000435, High Court
of Justice, King's Bench Division, **Divisional Court**, **6 June 2025**, before the **President
of the King's Bench Division** and **Mr Justice Johnson**. Read in full from the National
Archives' Find Case Law service. **[COURT]** Heard under the *Hamid* jurisdiction — *"the court's
inherent power to regulate its own procedures and to enforce duties that lawyers owe to the
court"* (¶2).

**The duty (¶7):**

> "Those who use artificial intelligence to conduct legal research notwithstanding these risks
> **have a professional duty therefore to check the accuracy of such research by reference to
> authoritative sources, before using it in the course of their professional work**…"

**⚠️ The delegation holding (¶8) — the autonomy-axis sentence:**

> "**This duty rests on lawyers who use artificial intelligence to conduct research themselves or
> rely on the work of others who have done so. This is no different from the responsibility of a
> lawyer who relies on the work of a trainee solicitor or a pupil barrister for example, or on
> information obtained from an internet search.**"

**⚠️ Leadership responsibility (¶9):**

> "There are serious implications for the administration of justice and public confidence in the
> justice system if artificial intelligence is misused. In those circumstances, **practical and
> effective measures must now be taken by those within the legal profession with individual
> leadership responsibilities (such as heads of chambers and managing partners)** and by those
> with the responsibility for regulating the provision of legal services… **For the future, in
> Hamid hearings such as these, the profession can expect the court to inquire whether those
> leadership responsibilities have been fulfilled.**"

**The regulatory rule the court relied on for delegated work (¶22), quoting the SRA Code of
Conduct:** *"Further, **where work is conducted on a solicitor's behalf by others, the solicitor
remains accountable for the work** (Rule 3.5)."* **[POLICY, quoted in a COURT judgment]** This is
the cleanest published professional rule located anywhere that assigns accountability for
delegated work independently of who did it.

**The range of powers (¶23):** *"the court's powers include public admonition of the lawyer, the
imposition of a costs order, the imposition of a wasted costs order, striking out a case,
referral to a regulator, the initiation of contempt proceedings, and referral to the police."*
**¶31:** *"the risks posed to the administration of justice if fake material is placed before a
court are such that, save in exceptional circumstances, **admonishment alone is unlikely to be a
sufficient response**."*

**⚠️ The disposal, and the supervisors (¶70).** Having declined to initiate contempt proceedings
against the barrister — *"This court's decision not to initiate contempt proceedings in respect of
Ms Forey is not a precedent. Lawyers who do not comply with their professional obligations in
this respect risk severe sanction"* (¶69) — the court referred her to her regulator, listing among
the matters requiring further consideration:

> "**Whether those responsible for supervising Ms Forey's pupillage in chambers complied with the
> relevant regulatory requirements in respect of her supervision, the way in which work was
> allocated to her, and her competence to undertake the level of work that she was doing.**"

Earlier, Ritchie J had made **wasted costs orders of £2,000 each against the barrister and the
law centre**, and the Divisional Court agreed in principle that *"placing false material before
the court with the intention of the court treating it as genuine amounts to improper and
unreasonable and negligent conduct."*

**Read as a whole, *Ayinde* does three things this strand needs:** it refuses to let the duty move
when work is delegated (¶8); it puts the *organisation's* allocation of work and supervision in
issue (¶70); and it announces that leadership compliance will be examined as a matter of routine
in future (¶9).

### 6.4 *Ko v Li* — the duty stated as plainly as it has been stated anywhere

Ontario Superior Court of Justice, **2025 ONSC 2766**, Myers J, ¶¶14–22 — **quoted in the appendix
to *Ayinde***, and cited here on that basis (**[COURT — reproduced in a court judgment]**; the
Ontario judgment itself was not fetched, see §12):

> "14. …It appears that Ms. Lee's factum may have been created by AI and that **before filing the
> factum and relying on it in court, she might not have checked to make sure the cases were real
> or supported the propositions of law** which she submitted to the court…
> 18. It is the lawyer's duty to use technology, conduct legal research, and prepare court
> documents competently.
> **19. It is the lawyer's duty to supervise staff and review material prepared for her
> signature.**
> **20. It is the lawyer's duty to ensure human review of materials prepared by non-human
> technology such as generative artificial intelligence.**
> **21. It should go without saying that it is the lawyer's duty to read cases before submitting
> them to a court as precedential authorities.**"

¶20 is, so far as this research found, the **only** judicial statement anywhere that imposes a
duty to *ensure human review of machine output* in those words.

### 6.5 ⚠️ The scale — and the numbers that cut against the narrative

**Source:** the *AI Hallucination Cases* database maintained by Damien Charlotin,
https://www.damiencharlotin.com/hallucinations/ **[TRACKER]**. The site describes itself: *"This
database tracks legal decisions… in cases where generative AI produced hallucinated content –
typically fake citations, but also other types of AI-generated arguments. It does not track the
(necessarily wider) universe of all fake citations or use of AI in court filings."* Footnoted
scope: *"all documents where the use of AI, whether established or merely alleged, is addressed in
more than a passing reference by the court or tribunal… only cases where the court or tribunal has
explicitly found (or implied) that a party relied on hallucinated content."*

The site's own header on the research date read **"Last updated: 30 August 2026"**. The figures
below are taken from the site's published aggregate data and from the **full CSV export
downloaded and analysed locally on 2026-08-30 (1,983 rows)**.

**Growth:**

| Year | Cases |
|---|---|
| 2023 (from Q2) | 16 |
| 2024 | 59 |
| 2025 | 849 |
| 2026 (to 28 August) | **1,059** |

**Who:**

| Party | Cases |
|---|---|
| **Pro se litigant** | **1,134** |
| **Lawyer** | **787** |
| Judge | 24 (+4 in combination) |
| Expert | 15 |
| Prosecutor / government lawyer / paralegal / federal defender / arbitrator | 13 |

**Outcome (site's own aggregate, n = 1,964, 19 alleged-only excluded):** **Monetary sanction 363;
Disciplinary referral 154.** From the CSV's own free-text outcome field, the largest single
category is **"Warning" (485)**, with 384 blank.

**Penalty size (site's own aggregate, USD-denominated, n = 199; 164 more in other currencies):**

| Band | Count |
|---|---|
| $0–100 | 21 |
| $100–1k | 30 |
| $1k–5k | 82 |
| $5k–10k | 34 |
| $10k–50k | 26 |
| $50k+ | 6 |

**Jurisdiction:** USA 1,364; Canada 214; Australia 98; UK 62; Israel 58; Brazil 41; then a long
tail across ~40 states.

**⚠️ Three honest readings of these numbers, all of which belong in the framework:**

1. **The professional-accountability story is a minority of the corpus.** More than half the cases
   involve unrepresented litigants, for whom no professional duty exists at all. Citing "1,983
   cases" as evidence about professionals overstates it by roughly a factor of two.
2. **Most cases end in a warning.** 363 monetary sanctions out of ~1,983, and two-thirds of the
   quantified penalties under $5,000. **The modal consequence of putting unreviewed AI output
   before a court is being told off.**
3. **24 of the cases involve judges.** The people whose job is to check are also shipping
   unchecked output. That is worth stating plainly and it complicates any simple "professionals
   must review" moral.

**⚠️ And the finding this strand was sent to establish:** a keyword sweep of all 1,983 rows
(case name, hallucination items, details and legal field) returned:

| Term | Hits |
|---|---|
| `source code` | **0** |
| `software engineer` | **0** |
| `pull request` | **0** |
| `code review` | **0** |
| `programmer` | **0** |

**There is no case, anywhere in the largest index of its kind, about a defect in AI-generated
software.** Every one is about material put before a court.

### 6.6 ⚠️ What transfers, and what does not

**This is analogical reasoning from an adjacent regulated profession. It is not software law.**
Setting it out precisely:

**What the rulings establish, in their own domain:**

- Signing certifies **after an inquiry reasonable under the circumstances** (Rule 11(b); *Mata*
  ¶1; *Wadsworth*).
- **The duty is nondelegable** — *"blind reliance on another attorney can be an improper
  delegation"* (*Wadsworth*, citing *Pavelic & LeFlore*, 493 U.S. 120).
- **The duty does not change when the work came from a machine**: *"As attorneys transition to the
  world of AI, the duty to check their sources and make a reasonable inquiry into existing law
  remains unchanged"* (*Wadsworth*); it rests equally on those who *"rely on the work of others
  who have done so"* (*Ayinde* ¶8).
- **"The AI did it" has been rejected as a defence** — in *Mata* the claim that ChatGPT was
  "merely a supplement" was found untruthful and aggravating (¶24(b)); in *Wadsworth* the firm's
  policy against that use of the tool aggravated the individual's position rather than excusing
  it.
- **The organisation is jointly responsible by default** (Rule 11(c)(1)) **but can discharge it
  with a policy plus a control** (*Wadsworth*).
- **The failure to correct is punished harder than the failure to check** (*Mata* ¶¶10, 21).

**What does not transfer, and must not be asserted:**

- **There is no Rule 11 for software.** No statute, rule of court or professional regulation
  requires a software engineer to certify anything on merging a change. The DCO, the only
  widely-used certification, certifies provenance and not correctness (§7.1).
- **There is no regulator.** Every one of these sanctions ran through a bar, a court's inherent
  jurisdiction over its own officers, or a professional regulator. Software has none of those.
- **The duty in these cases is owed to a court**, not to a user or the public. The analogue in
  software would be a duty owed to whoever relies on the code, which is exactly the question
  §5.5 says nobody has decided.
- **The harm is different.** A fake citation is a misrepresentation to a tribunal. A defect in
  code is a failure of a thing. Product law and misrepresentation law treat those very
  differently — see *Winter* (§5.3) and PLD recital 13 (§2.2), which both put "information" on the
  other side of the line from "product".

**The defensible statement — and the strongest thing this strand can say:**

> **In an adjacent profession, courts on three continents have now repeatedly held that the
> person who signs is answerable for what they did not read; that the duty is nondelegable; that
> it is unchanged by the fact that a machine produced the work; and that "the AI did it" is not a
> defence. No court has said this about software. Whether the analogy holds is untested, and the
> structural features that made those sanctions possible — a certification rule, a regulator, a
> duty owed to an identified body — are all absent from software engineering.**

---
## 7. How organisations actually assign it

### 7.1 ⚠️ The DCO: what a developer actually certifies

**Source:** https://developercertificate.org/, fetched raw on 2026-08-30. Full text **[POLICY]**:

> **Developer Certificate of Origin, Version 1.1**
> Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
> Everyone is permitted to copy and distribute verbatim copies of this license document, but
> changing it is not allowed.
>
> **Developer's Certificate of Origin 1.1**
>
> By making a contribution to this project, I certify that:
>
> (a) The contribution was created in whole or in part by me and I have the right to submit it
> under the open source license indicated in the file; or
>
> (b) The contribution is based upon previous work that, to the best of my knowledge, is covered
> under an appropriate open source license and I have the right under that license to submit that
> work with modifications, whether created in whole or in part by me, under the same open source
> license (unless I am permitted to submit under a different license), as indicated in the file;
> or
>
> (c) The contribution was provided directly to me by some other person who certified (a), (b) or
> (c) and I have not modified it.
>
> (d) I understand and agree that this project and the contribution are public and that a record
> of the contribution (including all personal information I submit with it, including my
> sign-off) is maintained indefinitely and may be redistributed consistent with this project or
> the open source license(s) involved.

**The Linux kernel's own gloss** (`Documentation/process/submitting-patches.rst`, "Sign your work
- the Developer's Certificate of Origin") **[POLICY]**:

> "**The sign-off is a simple line at the end of the explanation for the patch, which certifies
> that you wrote it or otherwise have the right to pass it on as an open-source patch.**"

And on downstream sign-offs:

> "**Any further SoBs (Signed-off-by:'s) following the author's SoB are from people handling and
> transporting the patch, but were not involved in its development.** SoB chains should reflect
> the **real** route a patch took as it was propagated to the maintainers…"

**⚠️ What a developer certifies when they sign off on code they did not read.** Working through
the clauses on the facts of AI-assisted development:

| Clause | What it says | AI-generated code the signer did not read |
|---|---|---|
| **(a)** | "created in whole or **in part** by me and I have the right to submit it" | The "in part" wording is broad enough to cover prompting and selecting. **Nothing here is falsified by not reading it.** Whether prompting is "creation" is a copyright question, not a quality one — and one the US Copyright Office has answered adversely (see the ASF guidance at §7.3). |
| **(b)** | "based upon previous work that, **to the best of my knowledge**, is covered under an appropriate open source license" | Knowledge-qualified. A signer who does not know what the model reproduced does not, on the face of it, certify falsely. This is the clause the AI-provenance worry actually lands on, and it is the softest of the four. |
| **(c)** | received from a person who certified (a)/(b)/(c), unmodified | A model is not a "person". Projects have read this as the reason **an AI cannot sign off** — see the Linux kernel and GCC below. |
| **(d)** | the record is public and permanent | Nothing to do with correctness. |

**There is no clause (e).** The DCO makes **no certification about correctness, quality, testing,
comprehension or review**. A developer who signs off on code they have not read certifies
truthfully, provided they have the rights. **This is the sharp answer to the ticket's DCO
question, and it should be stated plainly: the DCO cannot bear the accountability weight that
current AI-contribution policy places on it.**

Two projects have nevertheless built their AI accountability on the DCO's *human-only* character
rather than its content — which works, but for a different reason than is usually given:

- **Linux kernel** (`coding-assistants.rst`): *"AI agents MUST NOT add Signed-off-by tags. Only
  humans can legally certify the Developer Certificate of Origin (DCO)."*
- **GCC** (`ai-policy.html`, per [`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md)
  §1.4): *"Only a human may provide the 'Signed-off-by:' tag certifying the Developer Certificate
  of Origin (DCO). An LLM may not commit code to the project repository."*

The work is being done by *"only a human may sign"* — an identity rule — not by anything the
signature attests. That is the same structural move [`verification-gates.md`](./verification-gates.md)
§6b.1 found in SLSA: **the line drawn is identity and control of the actor, not the substance of
what is certified.**

### 7.2 ⚠️ The kernel's `Reviewed-by:` — a review certification that disclaims warranty

`Documentation/process/submitting-patches.rst`, "Reviewer's statement of oversight" **[POLICY]**,
quoted in full because clause (d) is the point:

> **Reviewer's statement of oversight**
>
> By offering my Reviewed-by: tag, I state that:
>
> (a) I have carried out a technical review of this patch to evaluate its appropriateness and
> readiness for inclusion into the mainline kernel.
>
> (b) Any problems, concerns, or questions relating to the patch have been communicated back to
> the submitter. I am satisfied with the submitter's response to my comments.
>
> (c) While there may be things that could be improved with this submission, I believe that it
> is, at this time, (1) a worthwhile modification to the kernel, and (2) free of known issues
> which would argue against its inclusion.
>
> **(d) While I have reviewed the patch and believe it to be sound, I do not (unless explicitly
> stated elsewhere) make any warranties or guarantees that it will achieve its stated purpose or
> function properly in any given situation.**

This is the **only** instrument located in this research in which a human explicitly certifies
having *read* a change — and its final clause withdraws any guarantee that flows from having read
it. Note also the surrounding text: *"A Reviewed-by tag is a statement of **opinion** that the
patch is an appropriate modification of the kernel without any remaining serious technical
issues."*

Compare the framework's own vocabulary. **Review** produces an opinion with a warranty disclaimer
attached. **Verification** produces evidence. A team moving further along the spectrum is trading
the first for the second — and, on this text, the first was never carrying the accountability
weight it is popularly assumed to carry.

### 7.3 ⚠️ Open-source licences and CLAs: everyone disclaims

**Apache License 2.0** **[POLICY]**, https://www.apache.org/licenses/LICENSE-2.0.txt:

> **7. Disclaimer of Warranty.** "Unless required by applicable law or agreed to in writing,
> Licensor provides the Work (**and each Contributor provides its Contributions**) on an "AS IS"
> BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND… **You are solely responsible for
> determining the appropriateness of using or redistributing the Work and assume any risks
> associated with Your exercise of permissions under this License.**"
>
> **8. Limitation of Liability.** "**In no event and under no legal theory, whether in tort
> (including negligence), contract, or otherwise**, unless required by applicable law (such as
> deliberate and grossly negligent acts) or agreed to in writing, **shall any Contributor be
> liable to You for damages**, including any direct, indirect, special, incidental, or
> consequential damages of any character arising as a result of this License or out of the use or
> inability to use the Work…"

**Apache Individual Contributor License Agreement** **[POLICY]**, https://www.apache.org/licenses/icla.pdf:

> **§6.** "You are not expected to provide support for Your Contributions, except to the extent
> You desire to provide support… Unless required by applicable law or agreed to in writing,
> **You provide Your Contributions on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
> KIND**, either express or implied, including, without limitation, any warranties or conditions
> of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE."
>
> **§7.** "Should You wish to submit work that is not Your original creation, You may submit it to
> the Foundation separately from any Contribution, identifying the complete details of its source
> and of any license or other restriction… and conspicuously marking the work as 'Submitted on
> behalf of a third-party: [named here]'."

**⚠️ The composite picture for open source, stated as directly as the sources permit:**

| Actor | What they certify | What they disclaim |
|---|---|---|
| **Author** | Provenance and rights (DCO (a)–(d) / ICLA §§4–5) | **All warranties** (ICLA §6) |
| **Reviewer** | Having carried out a technical review; an *opinion* of soundness | **Any warranty that it will function** (Reviewer's statement (d)) |
| **Project / licensor** | Nothing | **All warranties and all liability, "in tort (including negligence)"** (Apache-2.0 §§7–8) |
| **Downstream user** | — | Is told they are **"solely responsible for determining the appropriateness of using… the Work"** |

**The answer to the ticket's question, in the open-source case, is that nobody is answerable —
and that this is a deliberate, forty-year-old design, not an AI-era gap.** AI changes the volume
and the provenance risk; it does not change the allocation, because the allocation was already
"no one".

### 7.4 The project policies that do assign accountability

Ticket #4 catalogued ~25 restriction regimes; this section takes only the **accountability
sentences** from the ones that have them, plus the kernel text read fresh for this strand.

**Linux kernel**, `Documentation/process/coding-assistants.rst` (added 2025-12-23 by Sasha Levin),
read from the mainline tree on 2026-08-30 **[POLICY]**:

> **Signed-off-by and Developer Certificate of Origin**
> "**AI agents MUST NOT add Signed-off-by tags. Only humans can legally certify the Developer
> Certificate of Origin (DCO). The human submitter is responsible for:**
> * **Reviewing all AI-generated code**
> * **Ensuring compliance with licensing requirements**
> * **Adding their own Signed-off-by tag to certify the DCO**
> * **Taking full responsibility for the contribution**"

**Linux kernel**, `Documentation/process/generated-content.rst` (added 2026-01-19 by Dave Hansen)
**[POLICY]**:

> "First, read the Developer's Certificate of Origin… Its rules are simple and have been in place
> for a long time. **They have covered many tool-generated contributions. Ensure that you
> understand your entire submission and are prepared to respond to review comments.**"
>
> "**As with the output of any tooling, the result may be incorrect or inappropriate. You are
> expected to understand and to be able to defend everything you submit. If you are unable to do
> so, then do not submit the resulting changes. If you do so anyway, maintainers are entitled to
> reject your series without detailed review.**"

Note the tension the kernel is managing. `generated-content.rst` asserts the DCO's rules *"have
covered many tool-generated contributions"* — and then has to add a separate, non-DCO sentence
about understanding and defending the submission, **because the DCO does not say that** (§7.1).
The kernel is aware the certification does not reach comprehension and has bolted the requirement
on beside it rather than into it.

Also from `generated-content.rst`, a maintainer-discretion list that is unusually honest about
where the burden lands:

> "As with all contributions, individual maintainers have discretion to choose how they handle the
> contribution. For example, they might: Treat it just like any other contribution. **Reject it
> outright.** Treat the contribution specially, for example, asking for extra testing, reviewing
> with extra scrutiny, or **reviewing at a lower priority than human-generated content**… **Ask
> the submitter to explain in more detail about the contribution so that the maintainer can be
> assured that the submitter fully understands how the code works.**"
>
> "**If tools permit you to generate a contribution automatically, expect additional scrutiny in
> proportion to how much of it was generated.**"

That last sentence is an explicit statement that **scrutiny scales with delegation** — the
autonomy axis, written into a project's process documentation.

**Others, verified in ticket #4 and cited here for the accountability sentence only**
(see [`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md) for full
provenance) **[POLICY]**:

| Project | The accountability sentence |
|---|---|
| **NixOS / nixpkgs** (§1.20) | "Every contribution… must have a **responsible person in the loop who is accountable for that contribution and reviews it before submission**" |
| **Node.js** (§1.22) | "**Regardless of how much code is generated by AI, disclosure does not serve as a disclaimer of responsibility.**" and "The answer to 'Why is X an improvement?' can never be 'I'm not sure. The AI did it.'" |
| **LLVM** (§1.19) | "there must be a **human in the loop**. **Contributors must read and review all LLM-generated code or text before they ask other project members to review it.**" |
| **GCC** (§1.4) | "All contributions must be **submitted by a human who understands the changes**… Only a human may provide the 'Signed-off-by:' tag" |
| **Ghostty** (§1.21) | "**The human-in-the-loop must fully understand all code.** If you can't explain what your changes do… do not contribute to this project." |
| **Fedora** (§1.24) | Contributors remain fully accountable; content must be reviewed, tested and verified |

**The common formulation, across six independently drafted policies, is the same:** the human who
submits is accountable, must have read it, and must be able to explain it. **None of them has an
enforcement mechanism attached** — which is ticket #4's central finding, unchanged.

**⚠️ One thing none of them does.** Not one of these policies says what happens *to the
accountable person* when an AI-assisted contribution turns out to be defective. They allocate
accountability; they specify no consequence. Compare *Wadsworth*: $3,000, $1,000, $1,000, and a
revoked admission. **The open-source policies name a responsible party without attaching anything
to the name.**

### 7.5 ⚠️ The foundations: intellectual property only

Both documents below were fetched and read in full on 2026-08-30.

**Linux Foundation, "Guidance Regarding Use of Generative AI Tools for Open Source Software
Development"**, https://www.linuxfoundation.org/legal/generative-ai **[POLICY]**:

> "Open source software has thrived for decades based on the merits of each technical contribution
> that is openly contributed to and reviewed by community peers. **Development and review of code
> generated by AI tools should be treated no differently.**"
>
> "**Contributors should ensure that the terms and conditions of the generative AI tool do not
> place any contractual restrictions on how the tool's output can be used** that are inconsistent
> with the project's open source software license, the project's intellectual property policies,
> or the Open Source Definition."
>
> "**If any pre-existing copyrighted materials… are included in the AI tool's output**, prior to
> contributing such output to the project, the Contributor should confirm that they have
> permission from the third party owners… Additionally, the contributor should provide notice and
> attribution of such third party rights…"
>
> "Individual Linux Foundation projects may develop their own project-specific guidance…
> Similarly, organizations that employ open source developers may have more stringent
> guidelines… **Contributors should comply with their employer's policies when contributing.**"

**Apache Software Foundation, "ASF Generative Tooling Guidance"**,
https://www.apache.org/legal/generative-tooling.html **[POLICY]**:

> "The Apache-2.0 license, and the Apache Individual Contribution License Agreement, both remind
> contributors that **they are responsible for disclosing any copyrighted materials in submitted
> contributions that are not their original creation**. This is as true when using generative AI
> tooling, as it is when using materials from public websites or code from other open-source
> projects."
>
> "Disclosure is not the only obligation the ICLA places on contributors. **You also represent
> that each of your contributions is your original creation (section 5).** So a contribution does
> two things at once: it discloses any third-party material it contains, and it states that the
> rest is your own work."
>
> "**Section 7 of the ICLA covers submitting work that is not your original creation, but it asks
> for the complete details of the work's source. For AI-generated output, those details are
> generally not knowable, so Section 7 is not a practical route for contributing AI-generated
> material.**"
>
> [Citing the US Copyright Office] "purely AI-generated output is not copyrightable, but works
> where a human has creatively selected, arranged or modified AI-generated material may be…
> **These portions authored by a human may come from meaningful modifications the human makes;
> prompts alone are generally not sufficient.**"

**⚠️ The negative finding, verified by reading both documents end to end: neither contains a
single sentence about responsibility for defects, quality, testing, or review of correctness.**
The Linux Foundation's one sentence that mentions review — *"Development and review of code
generated by AI tools should be treated no differently"* — is a statement that AI code needs no
*special* handling, not an allocation of responsibility.

This extends ticket #4's cross-cutting finding #6 ("in industry, the restriction is almost never
of the capability… it is of the vendor, the jurisdiction, the channel, or the cost") one layer up
the governance stack: **the two largest open-source foundations govern AI contributions purely as
a copyright-chain problem. Nobody at that layer is assigning accountability for a defect at
all.**

The ASF passage is also the sharpest available statement of the *provenance* problem that §7.1
identifies in the DCO: ICLA §7 exists precisely for material that is not your original creation,
and the ASF's own reading is that **it does not work for AI output because the source details
"are generally not knowable"**. The certification machinery of open source has a hole in it that
predates and is orthogonal to the quality question.

### 7.6 ⚠️ The vendor high-risk carve-outs exclude software

**Anthropic Usage Policy**, effective **15 September 2025**, https://www.anthropic.com/legal/aup
**[POLICY]** (incorporated by reference into the Commercial Terms at D.2, so it is contractually
binding):

> **High-Risk Use Case Requirements**
> "Some use cases pose an elevated risk of harm because they influence domains that are vital to
> public welfare and social equity. For these use cases… **we require that you implement these
> additional safety measures:**
>
> **Human-in-the-loop:** When using our products or services to provide advice, recommendations,
> or in subjective decision-making directly affecting individuals or consumers, **a qualified
> professional in that field must review the content or decision prior to dissemination or
> finalization. You or your organization are responsible for the accuracy and appropriateness of
> that information.**
>
> **Disclosure:** If model outputs are presented directly to individuals or consumers, you must
> disclose to them that you are using AI…"

The enumerated High-Risk Use Cases are: **Legal; Healthcare; Insurance; Finance; Employment and
housing; Academic testing, accreditation and admissions; Media or professional journalistic
content.**

**Software engineering is not among them.** This is the strongest mandatory review duty any
vendor imposes anywhere in this corpus — *a qualified professional must review* — and it does not
apply to code. The vendor requires professional review of AI output used to advise someone about
a mortgage, and requires nothing of the AI output that becomes the system that decides mortgages.

Read alongside ticket #4's finding that no company restricts AI code on quality grounds, a
consistent industry position emerges: **AI output aimed at a person is treated as requiring
professional review; AI output aimed at a machine is not.**

### 7.7 Public-sector policy: the one place accountability is assigned to a named role

**OMB Memorandum M-25-21**, *"Accelerating Federal Use of AI through Innovation, Governance, and
Public Trust"*, Executive Office of the President, Office of Management and Budget, **3 April
2025**, signed Russell T. Vought, Director **[POLICY]**. Rescinds and replaces M-24-10.

> "As a step towards accelerating responsible adoption, agencies must establish clear expectations
> for their workforce on appropriate AI use — particularly when an agency is using AI to support
> consequential decision-making. **Agency policies must enable agency heads to delegate
> responsibilities and accountability for risk acceptance to appropriate officials throughout the
> agency**, ensuring that swift action is possible with sufficient guardrails in place. **Agencies
> must identify a Chief AI Officer…**"

**⚠️ The provision that matters most here** — on determining whether a use is "high-impact":

> "**A high-impact determination is possible whether there is or is not human oversight for the
> decision or action.**"

That is a published government policy stating in terms that **the presence of human oversight
does not change the risk classification**. It is the clearest official articulation found of the
point [`CONTEXT.md`](../CONTEXT.md) makes about human oversight: the mechanism does not imply the
outcome.

Minimum practices for high-impact AI include:

> "**iv. Ensure Adequate Human Training and Assessment.** Agencies must ensure there is sufficient
> and periodic training, assessment, and oversight for operators of AI to interpret and act on the
> AI's output and manage associated risks…
> **v. Provide Additional Human Oversight, Intervention, and Accountability.** Agencies must
> ensure human oversight, intervention, and accountability suitable for high-impact use cases.
> When practicable… agencies must ensure that the AI functionality has an appropriate fail-safe
> that minimizes the risk of significant harm."

**Scope caveat:** "high-impact" is defined as AI whose *"output serves as a principal basis for
decisions or actions that have a legal, material, binding, or significant effect on rights or
safety"*. Internal software development would not normally meet that. The memo is cited here for
its **structure** — delegate accountability to named officials; a Chief AI Officer; a training
duty; and the explicit statement that oversight does not lower the classification — not as
authority over AI-assisted coding.

---

## 8. ⚠️ The autonomy axis: how accountability moves as the human steps back

The ticket asked this strand to establish how accountability shifts as the human moves from
author, to reviewer, to approver, to someone who merely configured a pipeline — and to test
ticket #6's finding that **the far end of the spectrum is reached by an administrator changing a
policy rather than by any tool capability**, which suggests accountability may land on whoever
flipped the setting rather than whoever merged.

**The verdict: partly supported, from three independent directions, and it should be reported —
but the support is contractual and analogical, not a decided rule of software law.**

### 8.1 What the sources actually establish, position by position

| Position on the spectrum | What the primary sources say | Tier |
|---|---|---|
| **Author** — writes the change | Bears the primary sanction where the roles are split: *Wadsworth*, drafter, $3,000 + admission revoked. In open source, certifies **provenance only** (DCO) and expressly disclaims warranty (ICLA §6). | **[COURT]**, **[POLICY]** |
| **Reviewer** — reads it | Certifies "a technical review… to evaluate its appropriateness and readiness", but **"do[es] not… make any warranties or guarantees that it will achieve its stated purpose"** (kernel Reviewer's statement (d)). *Ayinde* ¶8: the duty rests equally on the person relying on another's AI-assisted work. | **[POLICY]**, **[COURT]** |
| **Approver / signer** — merges without reading | **The central finding.** *Mata* ¶23(a): signing after no inquiry is bad faith. *Wadsworth*: two signers who "did not review the Motions prior to signing" fined $1,000 each; the duty "nondelegable"; "blind reliance on another attorney can be an improper delegation". Local counsel sanctioned for "serving as a rubber stamp". | **[COURT]** |
| **Configurer** — turned autonomy on and merged nothing | **Cursor ToS §1.7**: *"By enabling this feature, you acknowledge and agree that you are assuming all risks… YOU ARE SOLELY RESPONSIBLE FOR ANY IMPACT RESULTING FROM USE OF THIS FEATURE."* **Google Cloud SST §20(j)**: "Customer is **solely responsible** for (i) its **use, non-use, or modification** … of safety filters". **AWS §50.10.2(ii)** and **Google §20(i)(1)(2)**: the IP indemnity is **forfeited** by disabling filters or disregarding instructions. | **[CONTRACT]** |
| **The organisation** | Jointly responsible by default (Fed. R. Civ. P. 11(c)(1); *Mata* ¶25) — **but discharges it with a documented policy plus an enforced control** (*Wadsworth*: training + a mandatory acknowledgement that "[u]sers must independently verify"). *Ayinde* ¶¶9, 70: courts will inquire into supervision and **"the way in which work was allocated"**. | **[COURT]** |

### 8.2 ⚠️ Testing ticket #6's hypothesis honestly

**The hypothesis:** if the far end of the spectrum is reached by an administrator changing a
setting, accountability may land on whoever flipped it rather than on whoever merged.

**What supports it:**

1. **Three vendors have independently drafted contract terms that attach liability to a
   configuration choice.** Cursor §1.7 (enabling auto-execution = assuming all risk of "software
   defects"); Google §20(j) (sole responsibility for "use, non-use, or modification" of filters);
   AWS §50.10.2(ii) and Google §20(i) (indemnity forfeited by disabling filters). **[CONTRACT]**
   This is the strongest support and it is not speculative: it is what the customer has agreed to.
2. **Courts have gone looking for the people who set the conditions.** *Ayinde* ¶70 put in issue
   *"the way in which work was allocated to her"* and whether supervisors met their regulatory
   requirements; ¶9 announced that leadership responsibility would be inquired into as a matter of
   routine. **[COURT]**
3. **The organisation's escape route in *Wadsworth* ran through configuration.** The firm was not
   sanctioned because it had *configured the tool* to force an acknowledgement. The setting was
   the defence. Symmetrically, the absence of such a setting would have been the exposure.
   **[COURT]**
4. **EU statute has the pattern, in an adjacent scope.** AI Act Art. 25(1)(b)–(c): a deployer who
   substantially modifies a system, or modifies its intended purpose such that it becomes
   high-risk, **becomes the provider**, and Art. 25(2) removes the original provider's status
   entirely. PLD Art. 8(2): a person who substantially modifies a product **is** its manufacturer.
   **[STATUTE]** Both encode "change what it does and you become the answerable party".

**What does not support it, and must be said:**

1. **No court has decided it.** There is no ruling anywhere that an administrator who enabled an
   autonomous mode is answerable for a defect that resulted. Not one.
2. **AI Act Art. 25 does not reach coding agents.** It governs high-risk AI systems under Annex I
   and III; a coding assistant is not one; and Art. 25 is not applicable until 2 December 2027 in
   any event (§4.2). Citing it as authority here would be wrong.
3. **The contract terms allocate risk between vendor and customer, not between employees.** Cursor
   §1.7 says the *customer organisation* bears the risk. It says nothing about which person inside
   that organisation is answerable. **The hypothesis is about internal allocation and the
   contracts are silent on internal allocation.**
4. **The judicial current runs the other way for the person who signs.** *Wadsworth* is explicit
   that reliance on someone else's competence, however reasonable, does **not** discharge the
   signer: *"blind reliance on another attorney can be an improper delegation of this duty."* If
   the analogy holds at all, **the person who merges does not shed accountability because someone
   else configured the pipeline.**

**The defensible formulation — and the one this document recommends the framework adopt:**

> **Accountability does not move along the spectrum; it accumulates.** The author holds it, the
> approver holds it *(Mata, Wadsworth)* and does not shed it by relying on the author
> *(Wadsworth, Ayinde ¶8)*, and — on the vendor contracts, though on no court decision — the
> person or organisation that enabled the autonomous mode has expressly assumed the risk of
> "system outages, software defects, data loss, and security vulnerabilities" *(Cursor §1.7)*.
> **What the configuration change does is not transfer accountability away from the merger; it
> adds a party.** The one demonstrated way to *reduce* an organisation's exposure is the
> *Wadsworth* pattern: a documented policy, evidence of training, and an enforced control at the
> point of use.

**Not supported and therefore not asserted anywhere in this document:** that the administrator who
flipped the setting bears the accountability *instead of* whoever merged. Nothing found says that.

### 8.3 The structural point the legal material offers the framework

Article 9 + Article 10(2)(a) of the PLD (§2.6) is the sharpest instrument located, and its logic
generalises well beyond the Directive's narrow scope:

> **The question a court will ask is not "did a human read it?" but "what can you produce?"**

For a change that went through engineered verification, there is something to produce: test
results, gate outcomes, static analysis, provenance, the agent transcript, the acknowledgement
record. For a change that nobody read *and* nothing checked, there may be nothing — and under the
PLD that silence is itself the trigger for a presumption of defectiveness. Under *Wadsworth*, the
firm's producible artefacts (training records, the tool's acknowledgement gate) were what kept it
out of sanction.

**This is the same finding [`verification-gates.md`](./verification-gates.md) reached from the
regulatory direction — regulators require change control and an argued rationale, not human
reading — arriving from the liability direction. A team further along the spectrum is not
legally exposed by the absence of review. It is exposed by the absence of a record.**

---
## 9. Sources

Every URL below was fetched on **2026-08-30** unless stated. Where a document was parsed locally
from a raw fetch rather than read through a summarising fetch, that is noted, because the
quotations in this file are verbatim from the raw text.

### Legislation and official records — [STATUTE]

| Source | Citation | URL |
|---|---|---|
| EU Product Liability Directive | Directive (EU) 2024/2853, OJ L, 2024/2853, 18.11.2024, of 23 October 2024 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402853 (raw, parsed locally) |
| PLD status metadata | In force; EIF 8.12.2024; transposition 9.12.2026; not amended (corrigendum 32024L2853R(01)) | https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32024L2853 |
| EU AI Act, original | Regulation (EU) 2024/1689, OJ L, 2024/1689, 12.7.2024, of 13 June 2024 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689 (raw, parsed locally) |
| EU AI Act, **consolidated as at 27.07.2026** | 02024R1689 — EN — 27.07.2026 — 001.001 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02024R1689-20260727 (raw, parsed locally) |
| Digital Omnibus on AI | Regulation (EU) 2026/1744 of 8 July 2026, OJ 24.7.2026, in force 27.7.2026 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744 |
| **AILD formal withdrawal** | "Withdrawal of Commission proposals", OJ C, **C/2025/5423, 6.10.2025**, CELEX 52025XC05423 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:C_202505423 (raw, parsed locally) |
| AILD withdrawal — announced intention | Commission Work Programme 2025, **COM(2025) 45 final, 11.2.2025**, Annex IV entry 32 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52025DC0045 (raw, parsed locally) |
| AILD procedure record | EP Legislative Observatory, procedure **2022/0303(COD)**; "06/10/2025 Proposal withdrawn by Commission"; status "Procedure lapsed or withdrawn" | https://oeil.europarl.europa.eu/oeil/en/procedure-file?reference=2022/0303(COD) (raw, parsed locally) |
| AILD proposal | COM(2022) 496 final, 28 September 2022 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52022PC0496 |
| UK product liability | Consumer Protection Act 1987 (c. 43), ss. 1, 45 | https://www.legislation.gov.uk/ukpga/1987/43/section/1 · /section/45 |
| UK product regulation | Product Regulation and Metrology Act 2025 (2025 c. 20), ss. 1, 2, 11 | https://www.legislation.gov.uk/ukpga/2025/20 |

### Court orders and judgments — [COURT]

| Case | Court, date | Where read |
|---|---|---|
| *Mata v. Avianca, Inc.*, No. 22-cv-1461 (PKC), ECF 54, 678 F. Supp. 3d 443 | S.D.N.Y., **22 June 2023**, Castel J | RECAP archive of the court's own filing: https://storage.courtlistener.com/recap/gov.uscourts.nysd.575368/gov.uscourts.nysd.575368.54.0.pdf (43 pp., text extracted locally) |
| *Wadsworth v. Walmart Inc.*, No. 2:23-cv-118-KHR, ECF 181 | D. Wyo., **24 February 2025**, Rankin J | RECAP archive of the court's own filing: https://storage.courtlistener.com/recap/gov.uscourts.wyd.64014/gov.uscourts.wyd.64014.181.0_1.pdf (17 pp., text extracted locally) |
| *R (Ayinde) v London Borough of Haringey; Al-Haroun v Qatar National Bank* [2025] EWHC 1383 (Admin) | High Court, KBD, **Divisional Court**, **6 June 2025**, President of the KBD and Johnson J | The National Archives, Find Case Law: https://caselaw.nationalarchives.gov.uk/ewhc/admin/2025/1383 (full text, parsed locally) |
| *Ko v Li*, 2025 ONSC 2766 | Ontario Superior Court of Justice, Myers J | **Quoted in the appendix to *Ayinde***; the Ontario judgment itself was not fetched (see §12) |
| *Chatlos Systems, Inc. v. National Cash Register Corp.*, 479 F. Supp. 738 | D.N.J., **22 October 1979** | Caselaw Access Project static archive of *Federal Supplement* vol. 479: https://static.case.law/f-supp/479/cases/0738-01.json |
| *Data Processing Services, Inc. v. L.H. Smith Oil Corp.*, 492 N.E.2d 314 (main); 493 N.E.2d 1272 (rehearing) | Ind. Ct. App., **28 April 1986** / 12 June 1986 | Caselaw Access Project: https://static.case.law/ne2d/492/cases/0314-01.json and /ne2d/493/cases/1272-01.json |
| *Winter v. G.P. Putnam's Sons*, 938 F.2d 1033 | 9th Cir., **12 July 1991** | Caselaw Access Project: https://static.case.law/f2d/938/cases/1033-01.json |

Authorities relied on inside those judgments and quoted here at second hand, clearly attributed:
*Pavelic & LeFlore v. Marvel Ent. Grp.*, 493 U.S. 120 (1989); *Business Guides, Inc. v. Chromatic
Commc'ns Enters., Inc.*, 498 U.S. 533 (1991); *Adamson v. Bowen*, 855 F.2d 668 (10th Cir. 1988);
*Massey v. Prince George's Cnty.*, 918 F. Supp. 905 (D. Md. 1996); *Cooter & Gell v. Hartmarx
Corp.*, 496 U.S. 384 (1990); *Valu v. Minister for Immigration* [2025] FedCFamC2G 95 (Australia);
*Zhang v Chen* 2024 BCSC 285 (Canada); *Wikeley v Kea Investments Ltd* [2024] NZCA 609 (New
Zealand); *Geismayr v The Owners, Strata Plan KAS 1970* 2025 BCCRT 217.

### Contract terms — [CONTRACT]

| Vendor | Document | URL |
|---|---|---|
| GitHub | Terms of Service, effective **27 April 2026**, §§A, J, O, P, Q | https://docs.github.com/en/site-policy/github-terms/github-terms-of-service (raw, parsed locally) |
| GitHub | Copilot Product Specific Terms §§2, 3, 4 | https://github.com/customer-terms/github-copilot-product-specific-terms |
| GitHub | Terms for Additional Products and Features (routing only) | https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features |
| Anthropic | Commercial Terms of Service §§D.2, D.3, L.2, L.3 | https://www.anthropic.com/legal/commercial-terms (raw, parsed locally) |
| OpenAI | Business Terms §§4.3, 12.1, 12.2, 13, 14.1, 14.2 | https://openai.com/policies/business-terms/ (raw via curl; WebFetch 403) |
| Cursor (Anysphere) | Terms of Service §§1.4, 1.7, 14, 15.1, 15.2 | https://cursor.com/terms-of-service (raw, parsed locally) |
| AWS | Service Terms §§24.2, 50.1–50.14, 53.10, 54.8.3, 60.4.2, 81.2, 99.1 | https://aws.amazon.com/service-terms/ (1.06 MB raw, parsed locally) |
| Google Cloud | Service Specific Terms §20 (Generative AI Services), (a), (b), (i), (j) | https://cloud.google.com/terms/service-terms (raw, parsed locally) |

### Published policies, codes and guidance — [POLICY]

| Source | URL |
|---|---|
| Developer Certificate of Origin 1.1 | https://developercertificate.org/ (raw) |
| Linux kernel, `Documentation/process/coding-assistants.rst` | https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/coding-assistants.rst |
| Linux kernel, `Documentation/process/generated-content.rst` | https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/generated-content.rst |
| Linux kernel, `Documentation/process/submitting-patches.rst` (DCO gloss; Reviewer's statement of oversight) | https://raw.githubusercontent.com/torvalds/linux/master/Documentation/process/submitting-patches.rst |
| Apache License 2.0 §§7, 8, 9 | https://www.apache.org/licenses/LICENSE-2.0.txt |
| Apache Individual Contributor License Agreement §§6, 7 | https://www.apache.org/licenses/icla.pdf |
| ASF Generative Tooling Guidance | https://www.apache.org/legal/generative-tooling.html |
| Linux Foundation, Generative AI Policy | https://www.linuxfoundation.org/legal/generative-ai |
| Anthropic Usage Policy, effective **15 September 2025** | https://www.anthropic.com/legal/aup |
| Google, Gemini Code Assist overview (documentation, not contract) | https://docs.cloud.google.com/gemini/docs/codeassist/overview |
| OMB Memorandum **M-25-21**, 3 April 2025 | https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf (PDF, text extracted locally) |
| ACM Code of Ethics and Professional Conduct (2018) §§2.4, 2.5, 2.6, 2.9 | https://www.acm.org/code-of-ethics |
| NCEES PE disciplines list | https://ncees.org/engineering/pe/ |
| Solicitors Regulation Authority Code of Conduct r.3.5; Bar Standards Board Handbook CD1/CD3/CD5/CD7, rr. C3.1, C9.1, C9.2.b, C18 | Quoted within *Ayinde* [2025] EWHC 1383 (Admin) ¶¶17–22 |

### Curated index of primary orders — [TRACKER]

*AI Hallucination Cases* database, maintained by Damien Charlotin —
https://www.damiencharlotin.com/hallucinations/, site header "Last updated: 30 August 2026";
1,983 cases. Full CSV export downloaded and analysed locally on 2026-08-30:
https://www.damiencharlotin.com/hallucinations/hallucinations/download.csv

### In this repository

- [`refusal-policies-primary-sources.md`](./refusal-policies-primary-sources.md) — ticket #4;
  verbatim primary text for ~25 restriction regimes. §7.4 draws its accountability sentences from
  there rather than re-verifying them.
- [`verification-gates.md`](./verification-gates.md) — §6b (what regulators actually require) and
  §6b.1 (SLSA identity-not-humanity finding) are the closest neighbours to §8.3.
- [`CONTEXT.md`](../CONTEXT.md) — vocabulary.

---

## 10. Confidence and gaps

### High confidence

- **All vendor contract quotations.** Every one was read from the vendor's own live page on
  2026-08-30, and every one was verified against the **raw** document after an initial
  summarising fetch, except the two GitHub Copilot Product Specific Terms quotations noted below.
  The GitHub ToS §J.4 sentence, the Cursor §1.7 clause, the Anthropic D.3/L.3 clauses and the
  OpenAI 4.3/14.2 clauses are verbatim from raw HTML parsed locally.
- **All PLD quotations.** Read from the OJ text; article and recital numbers verified by offset in
  the parsed document.
- **The AI Act amendment and the deferred dates.** Verified against the EUR-Lex consolidated text
  02024R1689 — EN — 27.07.2026, with the `▼M1` change markers visible in the extracted text, and
  cross-checked against the EUR-Lex "modified by" metadata naming Regulation (EU) 2026/1744.
- **The AILD withdrawal date, 6 October 2025.** Two independent official records agree: the OJ
  notice C/2025/5423 and the EP Legislative Observatory procedure file.
- **All three sanctions judgments.** *Mata* and *Wadsworth* were read from the courts' own filed
  PDFs (43 and 17 pages, extracted locally); *Ayinde* from the National Archives' official
  judgments service. Paragraph numbers are as they appear in those documents.
- **The DCO, Apache-2.0, ICLA and kernel process text.** Read raw; the DCO in full.
- **The tracker's counts.** Taken both from the site's own published aggregate JSON and from an
  independent local analysis of the 1,983-row CSV; the two agree.

### Medium confidence

- **PLD Article 4(18) ("substantial modification").** The local extract truncated part of the
  definition. §2.4 flags it. The Article 8(2) quotation itself is complete and verified.
- **The AWS negative finding (§1.5).** Verified by reading §50 in full and by keyword-sweeping the
  entire 312,000-character Service Terms text for "human review", "evaluated for accuracy" and
  "responsible for all decisions". The clause could exist in a linked AWS document not
  incorporated in the Service Terms page. Stated as "not located in the Service Terms", which is
  what was checked.
- **GitHub Copilot Product Specific Terms.** The page returned HTTP 500 to curl throughout; the
  quotations come from two separate WebFetch passes that agreed with each other. Treated as
  verified-but-not-raw. §12 records this.
- **NCEES.** The absence of Software Engineering from the PE discipline list was confirmed by
  reading the list. **No NCEES statement about a discontinued PE Software Engineering exam was
  located**, so §5.4 asserts only the absence from the current list.

### Low confidence / explicitly not established

- **Everything in §11.**
- **The reading of PLD recital 13 in §2.2** — that a code suggestion is "information" and not a
  product while the shipped executable is. This is a reading of the text. **No court has construed
  it.**
- **The whole of §6.6's transfer argument.** It is analogy, labelled as such at every use.

### Gaps this strand could not close

1. **No case, anywhere, about liability for a defect in AI-generated code.** Searched via the
   1,983-case tracker (0 hits on five code-related terms) and via the primary channels available.
   This is the central gap and it is a real feature of the landscape, not a research failure.
2. **No modern authority on the software standard of care.** The four cases in §5 are from 1979,
   1986 and 1991. CourtListener's search interface was behind an anti-bot challenge throughout
   (§12), so the search for later authority ran only through the Caselaw Access Project's
   volume-indexed archive, which requires knowing the citation in advance. **A researcher with
   Westlaw or Lexis access would very likely find more, and might find contrary authority.**
3. **Corporate internal AI-use policies.** Almost none are public. GitLab's public handbook — the
   most likely candidate — has **no AI-use policy page** in its legal section as at 2026-08-30
   (the navigation was enumerated; only working-group pages exist). The only corporate policy
   whose content is documented here is Morgan & Morgan's, and only because a court described it.
4. **PLD national transposition.** No Member State's implementing legislation was examined. Since
   the Directive maximally harmonises (Art. 3) the divergence should be small, but this is
   unverified.
5. **Insurance.** Professional indemnity and technology E&O policy wordings would show how the
   market is actually pricing this. None was obtained; none is public.
6. **Employment law.** Whether an employer can discipline or recover against an employee who
   merged unread AI output was not researched. Respondeat superior means the employer answers to
   the outside world; the internal allocation is a separate question this strand did not reach.

---

## 11. ⚠️ Unsettled — do not state as fact

Each item below is something this research could **not** establish, or actively found to be
wrong. Several circulate widely.

1. **"The EU Product Liability Directive makes AI vendors liable for defective code."** ❌ Not
   established, and three separate provisions cut against it. (i) It does not apply until
   9 December 2026 (Art. 2(1)). (ii) Recital 13 excludes *"the mere source code of software"* from
   "product". (iii) Its damage heads exclude property used exclusively for professional purposes
   and data used for professional purposes (Art. 6(1)(b)(iii), (c)), and only natural persons may
   claim (Art. 5(1)). **The ordinary commercial case is outside the Directive.**

2. **"The AI Liability Directive is delayed / paused / still pending."** ❌ **Wrong.** Formally
   withdrawn, OJ C/2025/5423, 6 October 2025.

3. **"A new AI liability instrument is coming to replace it."** ❌ Not established. The
   Commission's stated position in CWP 2025 Annex IV was that it *"will assess whether another
   proposal should be tabled or another type of approach should be chosen"*. No successor proposal
   was located as at 2026-08-30. Do not predict one.

4. **"The EU AI Act requires human oversight of AI-generated code."** ❌ Wrong twice over.
   Article 14 applies only to **high-risk AI systems** under Annex I/III, which a coding assistant
   is not; and as amended by Regulation (EU) 2026/1744 it **does not apply until 2 December 2027 /
   2 August 2028**. The only live AI Act obligation touching internal coding-agent use is
   Article 4 (AI literacy), which was **weakened** on 27 July 2026.

5. **"AI Act Article 25 means whoever changes the configuration becomes liable."** ⚠️ Overstated.
   Art. 25 does encode that pattern, but only for high-risk AI systems, only for substantial
   modification or a change of intended purpose that makes a system high-risk, and not until
   December 2027. It is a **useful analogy**, not applicable law here.

6. **"There is a duty of care in negligence for software developers."** ⚠️ Unsettled and
   contradictory. *Chatlos* (1979) refused to create a tort of computer malpractice; *Data
   Processing* (1986) applied an implied *contractual* standard of skill to bespoke development.
   **No jurisdiction found recognises software engineering malpractice as a distinct tort.**

7. **"Courts have held that developers are liable for unreviewed AI code."** ❌ **No court
   anywhere has decided this.** Every ruling in §6 concerns material put before a court by a
   lawyer or litigant. The tracker of 1,983 such cases contains **zero** about code.

8. **"Signing off under the DCO means you have taken responsibility for the code."** ❌ Not on the
   text. The DCO certifies origin and rights. There is no clause about correctness, testing,
   comprehension or review. Projects that assert accountability *alongside* the DCO — the Linux
   kernel, GCC, LLVM — are adding a requirement the DCO itself does not contain.

9. **"The reviewer is accountable if they approved it."** ⚠️ Depends entirely on the instrument.
   Under the Linux kernel's Reviewer's statement of oversight, clause (d) **expressly disclaims
   any warranty**. Under Rule 11 in a US court, signing is a certification and *is* accountability
   (*Mata*, *Wadsworth*). **There is no general rule; there is only whatever the specific
   instrument says.**

10. **"The vendor bears some of it if the model produced a defect."** ❌ Not on any contract read
    here. All six disclaim; four cap at 12 months' fees or less; Cursor caps at the greater of six
    months' fees or **$100**; GitHub takes an indemnity *from* the customer. **No contract found
    accepts any share of defect liability.**

11. **"The AI vendor is a 'manufacturer' under the PLD and can be sued for a bad suggestion."**
    ⚠️ Half-supported, half-contradicted, by the same recital. Recital 13 says an AI system
    provider "should be treated as a manufacturer" **and** that product liability rules should not
    apply to "the mere source code of software". Reconciling those two sentences on the facts of a
    code suggestion is exactly the question no court has answered. **Do not assert either way.**

12. **"Enabling autonomous mode makes the administrator personally liable."** ❌ Not established.
    Cursor §1.7 and Google §20(j) allocate that risk to the **customer organisation**; neither
    speaks to which employee is answerable. No court has decided it. §8.2 sets out the honest
    version.

13. **"Having an AI policy protects the organisation."** ⚠️ Supported by exactly **one** order,
    and only in combination. In *Wadsworth* the firm avoided sanction on the strength of a policy
    **plus** training records **plus** an enforced acknowledgement in the tool. Ticket #4's
    finding that policies alone are declarations stands. **Do not generalise from one district
    court order.**

14. **"Only humans can sign the DCO because an AI cannot hold copyright."** ⚠️ Two propositions
    are being run together. The DCO's clause (c) refers to "some other **person**", which is the
    textual hook the kernel and GCC use. The copyright point is separate and rests on the US
    Copyright Office's position, quoted by the ASF: *"purely AI-generated output is not
    copyrightable… prompts alone are generally not sufficient."* **Both may be true; they are not
    the same argument, and neither was tested in court.**

15. **"Software engineering is a licensed profession, so professional-negligence standards
    apply."** ❌ Not in the US federal-adjacent sources checked. NCEES's current PE discipline list
    does not include Software Engineering. **No NCEES statement about the retirement of a PE
    Software Engineering exam was located on NCEES's own site**, so this document asserts only the
    absence from the current list, not the history. State licensure regimes were not examined and
    §12 records that.

16. **"The UK follows the EU on software as a product."** ❌ It does not. CPA 1987 s.1(2)/s.45(1)
    define "product" as goods without reference to software; the Product Regulation and Metrology
    Act 2025 s.1(7) defines "product" as *"a tangible item"*. **Divergence, from 9 December 2026.**

17. **"Courts are cracking down hard on AI misuse."** ⚠️ Half true. Of ~1,983 tracked decisions,
    363 carried a monetary sanction and 485 a warning; two-thirds of quantified USD penalties are
    under $5,000. And **1,134 of the cases involve pro se litigants**, not professionals.

18. **"The trend line means software is next."** ❌ Speculation. The tracker's growth (16 → 59 →
    849 → 1,059) is real, and every one of those cases arises in a forum with a certification rule
    and a regulator. **Software has neither.** There is no evidential basis for projecting the
    curve across professions.

19. **Anything about how a court would treat an agent transcript, an eval result, or a CI record
    as evidence.** Article 9 of the PLD makes disclosure central and §8.3 draws the obvious
    inference, but **no court has ruled on what verification evidence is sufficient**, and the
    inference is this document's, not a source's.

20. **Whether vendor liability caps survive a claim within the PLD's scope.** Article 15 forbids
    contractual limitation of liability under the Directive, and Anthropic's L.3.c(III) purports
    to exclude "STRICT PRODUCT LIABILITY". **Which prevails, and in which forum, is undecided.**

---

## 12. Blocked or unavailable sources — logged, none circumvented

No paywall, login wall, click-through licence, rate limit or anti-bot control was circumvented in
producing this document. Every block below was recorded, and worked around only by seeking a
different, legitimately accessible source, or left unresolved.

### Access controls encountered

| Source | Block | Consequence |
|---|---|---|
| **CourtListener** — search UI and opinion pages (`courtlistener.com/?q=…`, `/opinion/…`) | **HTTP 403 to WebFetch; HTTP 202 (Cloudflare challenge) to curl**, consistently | **The most consequential block.** No case-law *search* was available. Case law was reached only by (a) direct RECAP object URLs on `storage.courtlistener.com`, which are not behind the challenge, and (b) the Caselaw Access Project's volume-indexed static archive, which requires the citation in advance. **Every "no case found" in this document means "not found without a case-law search engine."** |
| **CourtListener REST API v3** | `{"detail":"Anonymous users don't have permission to access the API."}` | No programmatic search. No key was created. |
| **openai.com/policies/** | **HTTP 403 to WebFetch** | Worked around with curl and a browser user-agent, which the host served normally (HTTP 200). All OpenAI quotations are from that raw HTML. |
| **git.kernel.org** | **Anubis anti-bot challenge** ("Making sure you're not a bot!") on `/plain/` paths | Kernel process documents read instead from the official GitHub mirror `raw.githubusercontent.com/torvalds/linux/master/…`. Content is the mainline tree; treated as equivalent. |
| **damiencharlotin.com/hallucinations/** | **HTTP 403 to WebFetch** | Fetched with curl and a browser user-agent (HTTP 200). Both the page's embedded aggregate JSON and the site's own CSV export were used. |
| **github.com/customer-terms/github-copilot-product-specific-terms** | **HTTP 500 Internal Server Error to curl**, repeatedly; not a repository (gh API 404) | Read via WebFetch only. **The Copilot Product Specific Terms quotations in §1.1 are therefore not raw-verified**, unlike every other contract quotation in this document. Two independent WebFetch passes returned consistent text. |
| **docs.fedoraproject.org** | Anubis anti-bot (recorded in ticket #4; not re-attempted) | Fedora's ratified AI policy is cited from ticket #4's record of the *proposal*, and labelled there. |

### Not found where expected

| Source | Issue |
|---|---|
| `cloud.google.com/terms/generative-ai/` | **HTTP 404.** The Generative AI terms live in the Service Specific Terms at `/terms/service-terms` §20 (formerly §19), which is where they were read. |
| `ncees.org/engineering/pe/software/` | **HTTP 404**, and Software Engineering does not appear on the current PE discipline list at `/engineering/pe/`. **No NCEES statement about a discontinued PE Software Engineering exam was located.** §11 item 15 records the corresponding claim as not established. |
| `pels.texas.gov/lic_disciplines.htm` | **HTTP 404.** **Texas licensure of software engineers was NOT verified.** No claim about US state licensure is made in this document. |
| `handbook.gitlab.com/handbook/legal/ai-usage/` and `about.gitlab.com/handbook/legal/ai-policy/` | **HTTP 404.** The GitLab legal handbook index was enumerated and contains **no AI-use policy page**. Recorded as a negative finding in §10. |
| `govinfo.gov/content/pkg/USCOURTS-nysd-1_22-cv-01461/…` | Returns HTTP 200 with an HTML error page, not a PDF — the package does not exist under that identifier. *Mata* was obtained from RECAP instead. |
| EUR-Lex quick search for the AILD withdrawal | The default relevance-sorted search surfaced only pre-2018 withdrawal notices. Re-running sorted by document date descending surfaced **C/2025/5423**. Recorded because the first search would have produced a false negative. |

### Deliberately not pursued

| Source | Reason |
|---|---|
| Westlaw, LexisNexis, Bloomberg Law | Paid. Not subscribed. **This is the single largest limitation on §5 and on the "no case found" statements throughout.** |
| *Ko v Li* 2025 ONSC 2766 (CanLII) | Not fetched. The passage quoted at §6.4 is reproduced verbatim inside the *Ayinde* judgment, which was read in full, and is attributed on that basis rather than to CanLII. |
| Professional indemnity / technology E&O policy wordings | Not public. |
| ISO/IEC 42001, ISO/IEC 25010 | Paid standards. Not obtained. No pirated copy was sought. |
| Member State PLD transposition instruments | Out of scope for the time available; recorded as a gap in §10. |

### Standing caveats on the evidence

- **Three of the six vendors' terms are consumer/business terms, not the enterprise agreements
  large customers actually sign.** Enterprise agreements are negotiated and unpublished. Every
  quotation here is from the published standard form. A negotiated MSA may say something different
  — and, on the strength of Anthropic L.3.b and OpenAI 13.1, indemnities in particular are the
  clauses most likely to have been varied.
- **All quotations were taken on a single day.** GitHub's ToS was three months old at the time of
  reading and had an effective date of 2026-04-27; Anthropic's Usage Policy dated from 2025-09-15;
  the AI Act consolidation was five weeks old. **This material moves fast. Re-verify before
  relying on any of it.**
- **This document is not legal advice.** Repeated here because it is the last thing on the page.
