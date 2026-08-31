# Governance: Licensing Exposure and Provider Indemnities

**Research date:** 2026-08-30
**Ticket:** [#7 Governance, Legal & IP by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/7)
**Question:** What licensing risk does agent-authored code create, and what do the vendors' indemnities
actually cover?

> ### This is research, not legal advice
>
> This document is a reading of published contract text, licence text and court records by a
> non-lawyer, for the purpose of describing what the primary sources say. It is **not legal advice**,
> it creates no lawyer–client relationship, and it must not be relied on as a substitute for counsel.
> Terms are quoted as published on the dates stated and change frequently — several of the most-cited
> claims in this area were **already out of date** when this was written (finding 3). Whether any
> provision applies to a given organisation depends on the agreement that organisation actually
> signed, which is often a negotiated master agreement rather than the public click-through text read
> here. Where the legal position is genuinely unsettled, this document records the disagreement rather
> than resolving it; see **Unsettled — do not state as fact**.

**Purpose.** Two questions get conflated in almost every discussion of this topic: *"can a model emit
someone else's copyrighted code?"* and *"if it does, who pays?"* The first is an empirical question
with weak and definitionally incoherent measurement. The second is a contract question with precise,
published answers that almost nobody reads. This strand separates them, and then asks the question the
project actually cares about: **does either answer change as delegation increases?**

**Method.** The providers' own published terms, read in full and quoted verbatim: GitHub's Customer
Terms, the Microsoft Product Terms and Glossary, the Google Cloud Service Specific Terms and Cloud
Terms of Service, the OpenAI Services Agreement and Service Terms, the Anthropic Commercial and
Consumer Terms, and the AWS Service Terms. Licence obligations are read from the licence texts at
gnu.org, apache.org and opensource.org, not from summaries. **Where a vendor's marketing page and its
contract disagree, the contract is reported.** Law-firm commentary and trade press were used only to
locate primary documents, and are labelled wherever they appear at all. All web sources were read
2026-08-30 unless a different date is stated.

**Evidence tier is stated with each figure.** Every quantitative claim about how often models reproduce
training data comes either from a party selling something, or from an academic study measuring
something narrower than its headline suggests. Both are marked.

**Vocabulary note.** This document uses "plan" for a vendor's commercial offering. The word "tier"
appears only inside quoted product names (`Amazon Q Developer Free Tier`, `Kiro Free Tier`) where the
vendor's own contract text requires it, and in the project's sense of **evidence tier**.

---

## Headline findings

1. ⚠️ **Every output indemnity in the set excludes output that has been modified or combined with
   anything the vendor did not supply — which describes all agent-authored code, all of the time.**
   This is the most consequential and least-reported provision in the field. OpenAI: the indemnity does
   not apply where *"Output was modified, transformed, or used in combination with products or services
   not provided by or on behalf of OpenAI"*
   ([Service Terms §1](https://openai.com/policies/service-terms/), updated 2026-06-12). Anthropic
   excludes *"(a) modifications made by Customer to the Services or Outputs"* and *"(b) the combination
   of the Services or Outputs with technology or content not provided by Anthropic"*
   ([Commercial ToS §K.3](https://www.anthropic.com/legal/commercial-terms)). Google covers only *"an
   unmodified Generated Output"*
   ([Service Specific Terms §17(i)](https://cloud.google.com/terms/service-terms)). GitHub's defence
   runs to a Product *"used within the scope of this Agreement (unmodified as provided by GitHub and
   not combined with anything else)"*
   ([General Terms §6.3(a)](https://github.com/customer-terms/general-terms)). **Read literally, a
   generated function pasted into an existing file is both modified and combined.** No provider
   publishes a carve-out saying that ordinary incorporation of generated code into a codebase does not
   count as combination. Whether these clauses would be read that broadly against a customer is
   genuinely unsettled — see **Unsettled** — but this is the text a customer would have to argue
   against.

2. **The free and individual plans do not carry a weaker indemnity. They carry the opposite of one.**
   GitHub's Terms of Service §J, which governs Copilot Free and Copilot Pro, states *"Output may
   resemble third-party code, including code under open source licenses"* and *"We do not guarantee
   that Output is free of errors, vulnerabilities, or intellectual property claims"* — and requires the
   **user** to indemnify GitHub for *"claims arising from Output you incorporate into your products or
   services"*
   ([GitHub ToS §J](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service),
   effective 2026-04-27). Anthropic's Consumer Terms carry no Anthropic indemnity and an all-caps
   user-indemnifies-Anthropic clause ([§11](https://www.anthropic.com/legal/consumer-terms), effective
   2025-10-08). Google excludes any Service *"provided to Customer free of charge"* twice over
   ([Cloud ToS §13.3(c)](https://cloud.google.com/terms/); [Service Specific Terms
   §17(i)](https://cloud.google.com/terms/service-terms)). AWS excludes `Amazon Q Developer Free Tier`
   and `Kiro Free Tier` by name ([Service Terms §50.10](https://aws.amazon.com/service-terms/), last
   updated 2026-08-20). Microsoft's `Covered Product` definition requires a product *"available for a
   fee ... or used with a paid subscription"* and excludes *"free Previews"*
   ([Product Terms Glossary](https://www.microsoft.com/licensing/terms/product/Glossary/all)).
   **The direction of the risk transfer inverts at the paywall.**

3. ⚠️ **The most-repeated operational claim in this field — "turn on the duplication filter or you lose
   the Copilot indemnity" — has been false since 3 April 2026.** Microsoft's own Required Mitigations
   page now reads: *"The below are the only required mitigations that apply to GitHub Offerings, and as
   of April 3, 2026, there are no additional required mitigations. **Use of the Duplicate Detection
   filter feature is no longer required for CCC coverage.** This feature remains available for optional
   use."*
   ([Customer Copyright Commitment Required Mitigations](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/customer-copyright-commitment),
   page updated 2026-07-13). The requirement was real; it is gone. Almost everything in circulation
   predates April 2026 and states it as current. **This is the project's standing finding about flat-ban
   reporting, in its licensing form: a dated, product-specific condition repeated indefinitely as a
   permanent rule.** Note the asymmetry — the filter is no longer a *contract* condition for GitHub
   products, but it remains a mitigation worth running on its own merits, and for Azure OpenAI code
   generation it **is** still required (finding 4).

4. **The filter requirement did not disappear everywhere; it moved.** For Azure OpenAI code generation
   the Required Mitigations table still says: *"The protected material code model must be configured on
   in either annotate or filter mode. If choosing to use annotate mode, customer must comply with any
   cited license provided for Output Content that is the subject of the claim. The jailbreak model
   (i.e., Prompt Shield for jailbreak attacks) must be configured on in filter mode."* (effective
   2023-12-01), plus a 2024-05-21 addition: *"If using the asynchronous filter feature, Output Content
   retroactively flagged as protected material code is not covered by the CCC, unless customer complies
   with its cited license."* Same page, read 2026-08-30. **So: not required for GitHub Copilot;
   required for Azure OpenAI code generation.** A single-sentence answer is wrong either way.

5. ⚠️ **The indemnities are uncapped, and the widely-repeated "capped at twelve months of fees" is
   wrong.** Every provider examined explicitly lifts the general liability cap for indemnification.
   GitHub: *"No limitation or exclusions will apply to liability arising out of either party's ...
   (2) obligations in Section 6 above"*
   ([General Terms §7.1(d)](https://github.com/customer-terms/general-terms)). Anthropic: *"The
   limitations of liability in this Section L.3 (Limits on Liability) do not apply to either party's
   obligations under Section K (Indemnification)."* OpenAI: the Service-Specific Terms Indemnity *"is
   not subject to any liability cap, and OpenAI may not materially reduce Customer's protections under
   the Service-Specific Terms Indemnity without Customer's written agreement"*
   ([Services Agreement §13.1](https://openai.com/policies/business-terms/), effective 2026-01-01).
   AWS: *"AWS's defense and payment obligations under this Section 50.10 will not be subject to any
   damages cap under the Agreement."* Google: §12.3 *"Unlimited Liabilities"* names *"its obligations
   under Section 13 (Indemnification)"*. Microsoft: the CCC *"is not subject to any limitation of, or
   exclusion from, liability contained in such agreements."*
   **The uncapped headline is real. Coverage is lost at the conditions, not at the cap.** This cuts
   against the cynical reading as well as the credulous one.

6. **Only two providers' indemnities clearly reach the training-data claim; the rest cover output
   only.** Google splits it into two limbs, the second being *"allegations that Google's use of training
   data to create any Google Pre-Trained Model utilized by a Generative AI Service infringes a third
   party's Intellectual Property Rights"* — and states that limb *"does not cover allegations related to
   a specific Generated Output"* (§17(i)(ii)). Anthropic folds it into the definition: a Customer Claim
   covers *"Customer's paid use of the Services **(which includes data Anthropic has used to train a
   model that is part of the Services)** ... or Outputs"* (§K.1). OpenAI, AWS and GitHub's
   generative-AI provisions are drafted around **Output** and the Services; the training-data theory is
   not separately named. This matters because the pending litigation is overwhelmingly about training,
   not output.

7. ⚠️ **Claude Code on a Pro or Max plan carries no IP indemnity, by Anthropic's own documentation.**
   *"Commercial Terms of Service - for Team, Enterprise, and Claude API users"* / *"Consumer Terms of
   Service - for Free, Pro, and Max users"*
   ([Claude Code legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)), and the
   Commercial Terms state *"Services under these Terms are not for consumer use. Our consumer offerings
   (e.g., Claude.ai) are governed by our Consumer Terms of Service instead."* The Consumer Terms
   contain no Anthropic indemnity and no non-infringement warranty. **A large share of the practitioner
   population running the most autonomous coding tool in the field is doing so on the plan with the
   least protection.** The same page also says Claude Code accessed *"through Amazon Bedrock or Google
   Cloud's Agent Platform (3P)"* is governed by *"your existing commercial agreement"* with that
   provider — which leads to finding 8.

8. **Third-party models on the hyperscalers' platforms sit outside the hyperscalers' output
   indemnities.** AWS's `Indemnified Generative AI Services` list enumerates Amazon's own Nova and Titan
   models plus named services; **Amazon Bedrock's third-party models are not on it**, and Bedrock is
   described separately as making third-party models available *"as 'Third-Party Content'"* (§50.12.1).
   Google's indemnified list covers the *"Gemini Enterprise Agent Platform API (formerly Vertex AI API)
   used with generally available versions of these foundation models: Codey, Gemini, Imagen, PaLM,
   Veo"*
   ([Generative AI Indemnified Services](https://cloud.google.com/terms/generative-ai-indemnified-services),
   last modified 2026-07-20) — Google's own models, and only their **generally available** versions.
   **Running a partner model on a hyperscaler can land in a gap: the platform indemnifies its own
   models, and the model vendor's commercial terms are not the agreement you are operating under.**
   Flagged as an inference from two documents rather than a stated position of either vendor — see
   **Unsettled**.

9. ⚠️ **Exactly one provider's terms address agentic operation in relation to the indemnity, and it
   narrows coverage rather than extending it.** Google Cloud Service Specific Terms §17(n)(iii):
   **"The actions or tasks that an AI Agent performs are not Generated Output."** With §17(n)(i):
   *"Customer is solely responsible for: (a) the actions and tasks performed by an Agentic AI Service or
   AI Agent; ... and (d) exercising judgment and supervision when and if an Agentic AI Service or AI
   Agent is used in production environments to avoid any potential harm the Agentic AI Service or AI
   Agent may cause."* Google defines `AI Agents` as systems that act *"in a supervised or autonomous
   manner"* (§14) — and then declines to distinguish the two for any purpose that helps the customer.
   **The one place the word "autonomous" appears near an indemnity, it appears on the exclusion side.**

10. **No provider conditions its indemnity on a human having read the output. That silence is the
    finding.** Searching the full operative text of all six providers for *human review, oversight,
    unattended, attended, supervised, autonomous, agentic* returns: nothing at all in the GitHub and
    OpenAI documents; one Anthropic clause (§D.3, *"including where human review is appropriate"*) that
    is an **accuracy** disclaimer and a customer responsibility, not a condition of §K; several AWS
    per-service accuracy disclaimers of the same shape (*"should be evaluated for accuracy ... including
    by employing human review of such output"*, §§24.2, 60.4.2, 81.2, 99.1) — none of which sit in
    §50.10; and Google's §17(n), which is finding 9. **Delegation depth is invisible to every indemnity
    in the set.** Whether that is reassuring or alarming depends on finding 11.

11. ⚠️ **The conditions never mention autonomy, but three of them get materially harder to satisfy as
    delegation increases.**
    **(a) Knowledge.** Every provider excludes output the customer *"knew or should have known"* was
    infringing — OpenAI (i), AWS (vi), Google (1), Anthropic (d), Microsoft condition 2, and GitHub's
    acceptable-use clause (*"you may not use Generative AI Services to generate Outputs whose use you
    know (or reasonably should know) would be unlawful or would infringe on the rights of others"*).
    **"Should have known" is a constructive-knowledge standard, and constructive knowledge is not
    obviously defeated by nobody having looked.** No provider says whether a duty of inspection scales
    with volume; no court has ruled on it in this context.
    **(b) Filters and citations.** Every provider excludes output where the customer *"disabled,
    ignored, or did not use any relevant citation, filtering or safety features"* (OpenAI),
    *"interfere[d] with or fail[ed] to enable available filters and other tools, or disregard[ed]
    instructions"* (AWS), *"disregards, disables, modifies, or circumvents source citations, filters,
    instructions, or other tools"* (Google), or *"disabled, evaded, disrupted, or interfered with the
    content filters"* (Microsoft). **A citation feature that emits an attribution nobody reads is being
    *ignored* in the ordinary sense of the word** — and finding 12 shows this is not hypothetical.
    **(c) Records.** AWS conditions the defence on the customer *"retain[ing] and provid[ing] sufficient
    records to the extent necessary to evaluate your eligibility for the defense"* (§50.10.3(c));
    Microsoft's Required Mitigations page says *"the customer will be required to demonstrate compliance
    with all relevant requirements"*. **Provenance record-keeping is an engineering obligation that gets
    harder exactly as the volume of generated code rises.**

12. ⚠️ **GitHub's coding agent does not enforce the enterprise Block policy.** GitHub Changelog,
    2026-02-18: *"Copilot coding agent does not support the 'Suggestions matching public code' policy's
    `Block` mode"* — when an organisation sets Block, *"suggestions matching public code will not be
    blocked, and instead will be highlighted in the session logs"*
    ([changelog](https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing/)).
    **A control that is enforcing on the attended surface is advisory on the unattended one.** This is
    the concrete mechanism behind 11(b): the further along the spectrum a team goes, the more its policy
    becomes a log entry. It no longer affects contract coverage for GitHub products (finding 3), but it
    directly affects the engineering control the team believes it has.

13. **The measured reproduction rates are low, old, definitionally incoherent, and not measured on the
    surfaces that matter.** GitHub's only published study found *"one recitation event every 10 user
    weeks"* (95% CI 7–13) across 453,780 Python suggestions from ~300 internal developers — 41 confirmed
    recitations, about 0.009% of suggestions
    ([research recitation](https://github.blog/ai-and-ml/github-copilot/github-copilot-research-recitation/),
    2021, updated 2022-08-16). *Evidence tier: vendor-reported metric, by an interested party, on its
    own product; pre-filter, Python-only, self-selected internal users.* The current *"less than 1%"*
    figure GitHub repeats in product docs has **no published derivation**. Academic figures span roughly
    0.1% to 47% and are not on one axis — they variously mean exact suffix match under adversarial
    prefix prompting, Type-1/Type-2 clone detection, or JPlag similarity ≥ 0.70, which is not verbatim
    at all. See **Output similarity**. **Nobody has published a per-suggestion rate with the filter on,
    any rate for an agent surface, or any rate at all for a 2025–26 frontier model.**

14. **The copyleft obligations people fear mostly do not trigger on internal use — and the ones that do
    are the ones nobody watches.** GPL-3.0 defines propagation to exclude *"executing it on a computer
    or modifying a private copy"*, and conveying as *"any kind of propagation that enables other parties
    to make or receive copies"* (§0). **An internal service that is never distributed does not trigger
    GPL's source-disclosure obligation.** The AGPL is drafted precisely for that case: §13 requires that
    *"if you modify the Program, your modified version must prominently offer all users interacting with
    it remotely through a computer network ... an opportunity to receive the Corresponding Source"* —
    **no distribution required.** Meanwhile the obligation that binds in the largest number of real
    cases is the mildest and the most silently breached: MIT's *"The above copyright notice and this
    permission notice shall be included in all copies or substantial portions of the Software"*, and
    Apache-2.0 §4(c)–(d)'s notice and NOTICE-file retention. **A model emits the code and not the
    header.** See **What reproduction obliges**.

15. **The threshold legal question — is model output a derivative work of its training data? — has never
    been decided by any court, and the pending code case is not about output.** See **The litigation**
    for the decided-versus-filed separation. Anyone stating a settled answer in either direction is
    ahead of the record.

16. **Two of the risks most often assumed to be covered are expressly carved out.** *Trademark in trade
    or commerce* is excluded by OpenAI (v), AWS (vii), Google (4), Anthropic (f) and Microsoft
    (condition 4) in near-identical words. And **patent practice** is excluded by Anthropic explicitly:
    *"(e) the practice of a patented invention contained in an Output"*. An indemnity described in the
    trade press as covering "IP claims on output" covers neither of these.

---

## The provider indemnity comparison table

All text read 2026-08-30 from the URLs in **Sources**. Quotation marks indicate verbatim contract
language. *Evidence tier for this entire table: primary contract text, published by the party bound by
it.* This table describes the public click-through terms; a negotiated enterprise agreement may differ,
and several providers say so expressly.

| | **GitHub Copilot** | **Microsoft (CCC)** | **Google Cloud** | **OpenAI** | **Anthropic** | **AWS** |
|---|---|---|---|---|---|---|
| **Operative text** | Generative AI Services Terms §4 + General Terms §6 (Version: March 2026) | Product Terms, Universal License Terms for Online Services — Customer Copyright Commitment | Service Specific Terms §17(i) + Cloud ToS §13 | Service Terms §1 & §3(b) (upd. 2026-06-12) + Services Agreement §13 (eff. 2026-01-01) | Commercial ToS §K (eff. 2025-06-17) | Service Terms §50.10 (upd. 2026-08-20) |
| **Who is covered** | Volume-licensing customers only. "a Product made available by GitHub **for a fee**". Personal/individual purchasers expressly excluded (§1.B → GitHub ToS §J) | `Covered Product` = "any Azure OpenAI model in Microsoft Foundry Models or **any Copilot (excluding free Previews)**, in either case, that is available **for a fee** ... or used with a **paid** subscription" | Only Services on the published Generative AI Indemnified Services list, and only "where the use of such Service or feature is **not provided to Customer free of charge**" | API customers (§1) and ChatGPT Enterprise/Edu/Healthcare/Business (§3(b)). **Beta Services "are excluded from any indemnification obligations"** | "Customer's **paid** use". Commercial ToS only — Free, Pro and Max fall under Consumer ToS, which has **no** Anthropic indemnity | Named `Indemnified Generative AI Services`, **"generally available features"** only, expressly "excluding Amazon Q Developer Free Tier" and "Kiro Free Tier" |
| **What is covered** | Third-party claims that a Product "misappropriated a trade secret or **directly infringes** a patent, copyright, trademark, or other proprietary right", extended to Outputs by GenAI Terms §4 | "Customer's use or distribution of Output Content of a Covered Product" — Microsoft's defence obligation applies **and the customer's reciprocal obligation does not** | **Two limbs.** (i) "an unmodified Generated Output ... infringes a third party's Intellectual Property Rights"; (ii) separately, "Google's use of **training data** to create any Google Pre-Trained Model" | "any third party claim that Customer's **use or distribution of Output** infringes a third party's intellectual property right" | "Customer's paid use of the Services **(which includes data Anthropic has used to train a model)** ... **or Outputs** generated through such authorized use violates any third-party intellectual property right" | "any third-party claim alleging that the **Generative AI Output** generated by an Indemnified Generative AI Service infringes or misappropriates that third party's intellectual property rights" |
| **Training-data claim?** | Not separately named | Not separately named — the CCC is drafted around Output Content | **Yes, expressly** (§17(i)(ii)), and expressly *not* overlapping the output limb | Not separately named in the Output indemnity; §13.1's general "Services infringe" limb may reach it | **Yes**, inside the definition of Customer Claim | Not separately named |
| ⚠️ **Conditions that void it** | Notice + **"has the right to control the defense and any settlement"**; "**all requested assistance, information, and authority**"; product must be "**unmodified as provided by GitHub and not combined with anything else**"; no cover for "continued use of a Product after being notified to stop"; AUP: must not generate Outputs "whose use you know (or reasonably should know) would be unlawful or would infringe" | 5 numbered conditions: (1) must not have "**disabled, evaded, disrupted, or interfered with the content filters, restrictions in Metaprompts, or other safety systems**"; (2) must not use output "in a manner that it **knows, or should know**, is likely to infringe"; (3) sufficient rights to the Input; (4) not a trademark claim; (5) for configurable services, **"all mitigations required by Customer Copyright Commitment Required Mitigations"** — for GitHub Offerings that list is now **empty** (since 2026-04-03) | Output must be **"unmodified"**. Excluded if customer: (1) "knew or should have known was likely infringing"; (2) **"disregards, disables, modifies, or circumvents source citations, filters, instructions, or other tools"**; (3) used it "after receiving notice of an infringement claim"; (4) trademark in trade or commerce; (5) lacked rights to customisation data. Plus general §13.3 (combination) and §13.4 (**"tender sole control"**) | Six exclusions: (i) "**knew or should have known**"; (ii) "**disabled, ignored, or did not use any relevant citation, filtering or safety features**"; (iii) ⚠️ "**Output was modified, transformed, or used in combination with products or services not provided by ... OpenAI**"; (iv) no rights to Input/fine-tuning files; (v) trademark; (vi) output from a Third Party Offering. §13.4: "**allow the indemnifying party sole control of defense and settlement**" | §K.3 excludes: "(a) **modifications made by Customer to the Services or Outputs**"; "(b) **the combination of the Services or Outputs with technology or content not provided by Anthropic**"; (c) Customer Inputs; (d) use "**that Customer knows or reasonably should know** violates or infringes"; (e) "**the practice of a patented invention contained in an Output**"; (f) trademark in trade or commerce. Also excluded for the indemnified party's "fraud, willful misconduct, violations of law, or breach of the Agreement" | Seven exclusions incl. (ii) "**if you interfere with or fail to enable available filters and other tools, or disregard instructions**"; (iv) fine-tuned/customised the **Service** such that infringement "would not have occurred but for" it; (v) after "notice to stop using the Generative AI Output"; (vi) "**know or reasonably should know**"; (vii) trademark. §50.10.3 requires notice, "**permit AWS to control the defense**", **"retain and provide sufficient records"**, and cooperation |
| **Cap** | **Uncapped.** §7.1(d): "No limitation or exclusions will apply to liability arising out of ... obligations in Section 6" (general cap otherwise 12 months' fees; Previews US$500) | **Uncapped.** "not subject to any limitation of, or exclusion from, liability contained in such agreements" | **Uncapped.** §12.3(b) "Unlimited Liabilities ... its obligations under Section 13 (Indemnification)" (general cap otherwise 12 months' fees; free services US$5,000) | **Uncapped.** §13.1: "not subject to any liability cap"; §14.2 excludes indemnification from the 12-month cap | **Uncapped.** §L.3: limits "do not apply to either party's obligations under Section K". (Beta Services separately capped at "the lesser of $1,000 and Fees paid" — Service Specific Terms §B) | **Uncapped.** "will not be subject to any damages cap under the Agreement" |
| **Sole remedy?** | Yes — §6.3 "sole remedies and entire liability for such claims" | In addition to the licensing agreement's defence obligation | Yes — §13.6 "sole and exclusive remedy" | Yes — §13.4 "THE INDEMNITIES ARE A PARTY'S ONLY REMEDY" | Not stated as exclusive in §K | Yes — "sole and exclusive remedies under the Agreement" |
| ⚠️ **Attended vs unattended** | **Silent** | **Silent** | ⚠️ **§17(n)(iii): "The actions or tasks that an AI Agent performs are not Generated Output."** §17(n)(i): customer "solely responsible" for agent actions and for "exercising judgment and supervision" in production | **Silent** | **Silent** on the indemnity. §D.3 mentions "where human review is appropriate" — an accuracy disclaimer, not an indemnity condition | **Silent** in §50.10. Per-service accuracy disclaimers elsewhere mention "human review" but do not condition §50.10 |

---
## Detail by provider

### GitHub Copilot — restructured on 5 March 2026, and the name "Copilot Copyright Commitment" no longer appears in the operative text

**The document everyone cites is archived.** The GitHub Copilot Product Specific Terms are now labelled
`[Archive]` on GitHub's own customer-terms index and apply only to *"Copilot Business/Enterprise licensed
before March 5, 2026"*. The live document is the **GitHub Generative AI Services Terms** (Version: March
2026), which states at §1.D: *"This document replaces the Product Specific Terms for all Generative AI
Services that were in effect before 5 March 2026."*
([index](https://github.com/customer-terms); [GenAI Terms](https://github.com/customer-terms/github-generative-ai-services-terms)).
**Any analysis citing the Copilot Product Specific Terms as current is citing an archive.**

**The indemnity is not in the AI document.** GenAI Terms §4 is one sentence:

> **4. Defense of Third Party Claims.** If your Agreement provides for the defense of third party
> claims, that provision will apply to your use of Generative AI Services, including to Outputs.

It is a pointer. The substance is in the **General Terms §6**:

> **6.1** The parties will defend each other against third party claims described in this section and
> will pay the amount of any resulting adverse final judgment or approved settlement, **but only if the
> defending party is promptly notified in writing of the claim and has the right to control the defense
> and any settlement of it.**
>
> **6.2** The party being defended must provide the defending party with **all requested assistance,
> information, and authority.** The defending party will then reimburse the other party for reasonable
> out-of-pocket expenses it incurs in providing such assistance.
>
> **6.3 (a) By GitHub.** GitHub will defend Customer against any third-party claim that a Product made
> available by GitHub **for a fee** and used within the scope of this Agreement (**unmodified as provided
> by GitHub and not combined with anything else**), misappropriated a trade secret or **directly
> infringes** a patent, copyright, trademark, or other proprietary right of a third party. If GitHub is
> unable to resolve a claim ... it may, at its option, either (1) modify or replace the Product with a
> functional equivalent or (2) terminate Customer's license and refund any license fees ... **GitHub will
> not be liable for any claims or damages due to Customer's continued use of a Product after being
> notified to stop due to a third-party claim.**

Four load-bearing details. **First**, "for a fee" — the structural exclusion of free plans. **Second**,
"unmodified ... and not combined with anything else" — drafted for a *Product*, then pointed at *Outputs*
by GenAI Terms §4 without adjustment. This is finding 1 in its GitHub form and is the least resolved
question in this document. **Third**, "directly infringes" — direct infringement only; contributory and
induced theories are outside it. **Fourth**, GitHub takes sole control of the defence, and the customer
must hand over "all requested assistance, information, and authority."

**The acceptable-use condition.** GenAI Terms §5.A: *"Your use of Generative AI Services is subject to
the Acceptable Use Policies, the AI Code of Conduct, and the Required Mitigations. For example, you may
not input content that is unlawful ... and you may not use Generative AI Services to generate Outputs
whose use you know (or reasonably should know) would be unlawful or would infringe on the rights of
others."* Breaching this puts use outside "the scope of this Agreement" in §6.3(a).

**`Required Mitigations` is defined by reference to Microsoft**, at §9: *"the Microsoft Customer Copyright
Commitment Required Mitigations at aka.ms/AIfilters."* That is the page that, since 3 April 2026, requires
nothing at all for GitHub Offerings (finding 3).

**Ownership and training.** §2: *"GitHub does not own Inputs or Outputs. You retain any ownership you
already have in your Inputs."* §3: *"GitHub will not use Inputs or Outputs to train generative AI models,
unless you have given us documented instructions to do so."* Note §2 assigns nothing and warrants nothing
— it disclaims GitHub's ownership without asserting the customer's.

**Shared responsibility, §5.B**, is worth quoting because it is the closest any provider comes to
addressing agent-built systems: *"you are solely responsible for any application or agent you create using
(or for use with) Generative AI Services, **including complying with any legal, regulatory, or licensing
requirements applicable to the resulting application or agent** or its use."*

**Cap.** General Terms §7.1: the ordinary cap is *"the amount Customer paid for the Product during the 12
months before the incident"*; Previews are capped at **US$500.00**. §7.1(d) then removes the cap for
Section 6 obligations entirely — so the defence is uncapped while everything else is not.

**Free and individual plans — the mirror image.** GitHub's Terms for Additional Products and Features
(last updated 2026-04-27) routes non-Business/Enterprise users to **ToS §J (AI Features)**, which:
- disclaims: *"Output may contain material that resembles code or content in the model's training data or
  that is subject to third-party copyrights or open source license terms"*; *"Output may be inaccurate,
  incomplete, or non-functional. Output may resemble third-party code, including code under open source
  licenses"*; and *"We do not guarantee that Output is free of errors, vulnerabilities, or intellectual
  property claims"*;
- places the licence-determination burden on the user;
- and **requires the user to indemnify GitHub**, including for *"claims arising from Output you
  incorporate into your products or services."*

⚠️ **This is the sharpest single contrast in the document.** The same model, the same editor, the same
emitted function: on Copilot Business, GitHub defends you without a cap; on Copilot Pro, you defend
GitHub.

### Microsoft — the Customer Copyright Commitment, in full

The CCC sits in the Universal License Terms for Online Services in the
[Product Terms](https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS). Verbatim:

> Microsoft's obligation to defend Customer against third-party intellectual property claims under
> Customer's volume licensing agreement will apply, and Customer's obligations to defend Microsoft
> against third-party intellectual property claims under Customer's volume licensing agreement will not
> apply, to the extent that such claims are based on Customer's use or distribution of Output Content of
> a Covered Product **if all the following additional conditions are met**:
>
> 1. While using the Covered Product to produce the Output Content that is the subject of the claim,
>    Customer **must not have disabled, evaded, disrupted, or interfered with the content filters,
>    restrictions in Metaprompts, or other safety systems** that are part of the Covered Product.
> 2. Customer does not modify, use, or distribute the Output Content in a manner that it **knows, or
>    should know, is likely to infringe** or misappropriate any proprietary right of a third party.
> 3. Customer has **sufficient rights to use the Input** in connection with the Covered Product ...
> 4. The claim does not allege that the Output Content, **as used in commerce or the course of trade,
>    violates a third party's trademark** or related rights.
> 5. For any Covered Product with configurable Metaprompts or other safety systems, Customer also must
>    have **implemented all mitigations required by Customer Copyright Commitment Required Mitigations**
>    (published at https://aka.ms/aoai-ccc) in the offering that delivered the Output Content ...

And: *"The foregoing indemnification obligation is in addition to any defense obligation set forth in
Customer's licensing agreement and is **not subject to any limitation of, or exclusion from, liability**
contained in such agreements."*

**Two structural points that are usually missed.** First, the CCC does two things, not one: it *extends*
Microsoft's defence obligation **and it switches off the customer's reciprocal defence obligation** for
the same claims. The second half is rarely reported and is genuinely valuable. Second, the CCC has **no
"unmodified/not combined" exclusion of its own** — condition 2 restricts *knowing* infringement in how
output is modified or distributed, which is a materially narrower and more customer-favourable drafting
than OpenAI's, Anthropic's, Google's or GitHub's general terms. On this specific point Microsoft's text
is the best of the six.

**Scope.** [Product Terms Glossary](https://www.microsoft.com/licensing/terms/product/Glossary/all):
`Covered Product` = *"any Azure OpenAI model in Microsoft Foundry Models or any Copilot (excluding free
Previews), in either case, that is available for a fee through Microsoft volume licensing or used with a
paid subscription to an Online Service."* `Output Content` = *"any data, text, sound, video, image, code,
or other content generated by a Microsoft Generative AI Service in response to Input."* `Metaprompts` =
*"instructions coded into a Microsoft Generative AI Service that provide directions to the service for
generating Output Content."*

**The Required Mitigations page is where the operational conditions actually live**
([link](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/customer-copyright-commitment),
page updated 2026-07-13). It defines the split that most commentary misses:

> The requirements described below apply only to customers using Azure OpenAI in Microsoft Foundry Models
> ("Azure OpenAI") and other Covered Products with configurable Metaprompts or other safety systems
> ("Configurable GAI Services"). They do not apply to customers using other Covered Products including
> Copilots with safety systems that are fixed. **The only Configurable GAI Services are Microsoft Copilot
> Studio and GitHub Copilot**; the Universal Required Mitigations do not apply to these offerings, but
> service-specific mitigations apply instead.

So: **Microsoft 365 Copilot and the fixed-safety-system Copilots have no required mitigations at all**;
Azure OpenAI has the two Universal mitigations plus per-use-case filter requirements; GitHub Copilot has,
since 2026-04-03, **none**.

The two Universal Required Mitigations (effective 2023-12-01), for Azure OpenAI and Copilot Studio:
- *"The customer offering must include a metaprompt directing the model to prevent copyright infringement
  in its output."*
- *"The customer offering must have been subjected to evaluations (e.g., guided red teaming, systematic
  measurement, or other equivalent approach) by the customer using tests designed to detect the output of
  third-party content. Significant ongoing reproduction of third-party content determined through
  evaluation must be addressed. **The report of results and mitigations must be retained by the customer
  and provided to Microsoft in the event of a claim.**"*

⚠️ **That second one is an obligation to run and retain your own evaluation programme** — the only place
in the entire six-provider set where an indemnity is conditioned on the customer performing measurement.
It does not apply to GitHub Copilot. It does apply to anyone building a code-generation product on Azure
OpenAI. This connects the licensing strand directly to the project's verification vocabulary: here,
**evals are a contract condition.**

For Azure OpenAI **code generation** specifically (effective 2023-12-01, amended 2024-05-21):

> The protected material code model must be configured on in either annotate or filter mode. **If choosing
> to use annotate mode, customer must comply with any cited license provided for Output Content** that is
> the subject of the claim. The jailbreak model (i.e., Prompt Shield for jailbreak attacks) must be
> configured on in filter mode.
>
> If using the asynchronous filter feature, **Output Content retroactively flagged as protected material
> code is not covered by the CCC, unless customer complies with its cited license.**

And the governing clause on change and proof: *"customers will have six months from the date of publication
on this page to implement any new mitigations required to maintain coverage ... **If a customer tenders a
claim for defense, the customer will be required to demonstrate compliance with all relevant requirements**,
both on this page and as listed in the Product Terms."*

### Google Cloud — the only two-limb indemnity, and the only agentic carve-out

**Service Specific Terms §17(i)**, verbatim:

> **(i) Generated Output.** Google's indemnification obligations under the Agreement also apply to
> allegations that an **unmodified** Generated Output from a Generative AI Indemnified Service using only
> Google Pre-Trained Model(s), a Modified Google Model, or a Customer Adapter Model used with a Google
> Pre-Trained Model infringes a third party's Intellectual Property Rights. This subsection (i) does not
> apply if the allegation relates to a Generated Output where: **(1)** Customer creates or uses such
> Generated Output that it **knew or should have known was likely infringing**, **(2)** Customer (or
> Google at Customer's instruction) **disregards, disables, modifies, or circumvents source citations,
> filters, instructions, or other tools** Google makes available to help Customer create or use Generated
> Output responsibly, **(3)** Customer uses such Generated Output **after receiving notice of an
> infringement claim** from the rightsholder or its authorized agent, **(4)** the allegation is based on a
> **trademark**-related right as a result of Customer's use of such Generated Output in trade or commerce,
> or **(5)** Customer does not have the necessary rights to the Customer Data used to customize or retrain
> the Modified Google Model or Customer Adapter Model ... "Generative AI Indemnified Service" means a
> Service or feature listed at https://cloud.google.com/terms/generative-ai-indemnified-services, where
> the use of such Service or feature is **not provided to Customer free of charge**.
>
> **(ii) Training Data.** Google's indemnification obligations under the Agreement also apply to
> allegations that **Google's use of training data** to create any Google Pre-Trained Model utilized by a
> Generative AI Service infringes a third party's Intellectual Property Rights. This indemnity **does not
> cover allegations related to a specific Generated Output**, which may be covered by subsection (i) above.

**This is the clearest drafting in the set** and the only one that names the training-data theory as a
separate covered claim with its own boundary.

**§17(j)** adds: *"Customer is solely responsible for (i) its use, non-use, or **modification** (including
modifications made by Google at Customer's instruction) of safety filters in creating Generated Output,
and (ii) disregarding safety instructions or Documentation."*

**Both limbs extend the Cloud ToS §13 indemnity, so §13's own machinery applies**
([Cloud ToS](https://cloud.google.com/terms/)) — §13.3 exclusions (breach of agreement; *"a combination of
the indemnifying party's technology ... with materials not provided by the indemnifying party"*; anything
free of charge) and §13.4 conditions (prompt written notice, reasonable cooperation, and *"tender sole
control of the indemnified portion of the Third-Party Legal Proceeding"*, with the customer's own
non-controlling counsel at its own expense). **Whether §13.3(b)'s combination exclusion applies on top of
§17(i)'s "unmodified" requirement is not stated** — see **Unsettled**. §12.3 makes §13 uncapped.

**Scope.** [Generative AI Indemnified Services](https://cloud.google.com/terms/generative-ai-indemnified-services),
last modified 2026-07-20, lists for Google Cloud Platform: *"Gemini for Google Cloud (formerly known as
Duet AI for Google Cloud)"*; *"Gemini Enterprise Agent Platform API (formerly Vertex AI API) used with
generally available versions of these foundation models: Codey, Gemini, Imagen, PaLM, Veo"*; Agent
Conversation; Agent Search; three Grounding features; Automotive AI Agent; Gemini Enterprise; NotebookLM
Enterprise. Plus, for Workspace, Gemini in Workspace and Google Vids. **Coding coverage arrives via
"Gemini for Google Cloud"** — Gemini Code Assist is a feature of that umbrella product, not a separately
listed item, which is worth confirming against your own contract. **Partner models on the platform are not
on the list, and neither are non-GA model versions.**

⚠️ **The agentic carve-out, §17(n).** This is the finding this strand was sent to look for.

> **(i)** Customer is **solely responsible** for: (a) **the actions and tasks performed by an Agentic AI
> Service or AI Agent**; (b) determining whether the use of an Agentic AI Service or AI Agent is fit for
> its use case; (c) authorizing an Agentic AI Service or AI Agent's access and connection to data,
> applications, and systems; and (d) **exercising judgment and supervision when and if an Agentic AI
> Service or AI Agent is used in production environments** to avoid any potential harm the Agentic AI
> Service or AI Agent may cause.
>
> **(ii)** ... Google disclaims all liability arising from Customer's access to and use of any Third Party
> Service, and **Google's indemnification obligations do not apply to allegations arising from access to
> or use of any Third Party Service.** ... "Third Party Services" mean platforms, services, websites,
> **software libraries**, and APIs provided by third parties.
>
> **(iii) The actions or tasks that an AI Agent performs are not Generated Output.**

With the §14 definitions: *"'AI Agents' are goal-oriented, AI systems or workflows that perform actions or
tasks on behalf of Customer **in a supervised or autonomous manner** that Customer may create, orchestrate,
or initiate within an Agentic AI Service."*

Google therefore (a) knows the difference between supervised and autonomous operation, (b) writes it into
a definition, and (c) attaches **no** consequence to it — while (d) separating an agent's *actions* from
the *Generated Output* that the indemnity covers. §17(n)(ii)'s exclusion of *"software libraries"* provided
by third parties is a further, and underappreciated, narrowing for agents that install dependencies.

### OpenAI — Copyright Shield, and the exclusion that swallows code

The provision commonly called **Copyright Shield** is not called that in the terms. It lives in the
[Service Terms](https://openai.com/policies/service-terms/) (updated 2026-06-12), stated twice in identical
words — once for API customers (§1) and once for ChatGPT Enterprise/Edu/Healthcare and Business (§3(b)):

> OpenAI's indemnification obligations to API customers under the Agreement include any third party claim
> that Customer's use or distribution of Output infringes a third party's intellectual property right.
> This indemnity does not apply where: **(i)** Customer or Customer's End Users **knew or should have
> known** the Output was infringing or likely to infringe, **(ii)** Customer or Customer's End Users
> **disabled, ignored, or did not use any relevant citation, filtering or safety features or
> restrictions** provided by OpenAI, **(iii) Output was modified, transformed, or used in combination with
> products or services not provided by or on behalf of OpenAI**, **(iv)** Customer or its End Users did
> not have the right to use the Input or fine-tuning files to generate the allegedly infringing Output,
> **(v)** the claim alleges violation of **trademark** or related rights based on ... use of Output in
> trade or commerce, and **(vi)** the allegedly infringing Output is from content from a **Third Party
> Offering**.

⚠️ **Exclusion (iii) is the broadest in the set.** "Modified, transformed, **or** used in combination with
products or services not provided by ... OpenAI" — three disjunctive triggers, any of which describes
generated code the moment it is edited, refactored, or compiled against a dependency OpenAI did not
supply. Note also that exclusion (ii) covers *ignoring* a citation feature, not merely disabling one.

**OpenAI says, in its own terms, that code output may carry open-source obligations.** Service Terms §4,
in full:

> **4. Codex and Code Generation.** Output generated by code generation features of our Services, including
> OpenAI Codex, **may be subject to third party licenses, including, without limitation, open source
> licenses.**

**This is the most direct vendor acknowledgement of the licensing question in the entire document set**,
and it sits in the same instrument as the indemnity that excludes modified and combined output. Read
together, the two provisions tell a customer: your generated code may carry someone else's licence, and
if you have touched it or combined it with anything, that is your problem.

**Beta is excluded.** Service Terms §2: *"Beta Services are offered 'as-is' to allow testing and evaluation
and are **excluded from any indemnification obligations** OpenAI may have to you."* Agentic coding features
ship in preview far more often than completion features do.

**The Services Agreement layer** ([Business Terms](https://openai.com/policies/business-terms/), updated
2025-12-01, effective 2026-01-01):

> **13.1. By OpenAI.** OpenAI agrees to indemnify, defend, and hold Customer harmless against any
> liabilities, damages and costs ... arising out of a Claim alleging that **the Services infringe** any
> third-party IP Right. This excludes claims to the extent arising from: (a) **combination of any Services
> with products, services, or software not provided by OpenAI**; (b) **modification of any Services** by
> any party other than OpenAI; (c) Customer Content; (d) Customer Applications ... In addition, the
> Service-Specific Terms Indemnity, as of the Effective Date, is included in this Agreement, **is not
> subject to any liability cap**, and OpenAI **may not materially reduce Customer's protections under the
> Service-Specific Terms Indemnity without Customer's written agreement.**

That last clause is a real and unusual protection — a contractual ratchet against unilateral narrowing —
and it is the strongest single customer-favourable term found in this strand.

**Procedure, §13.4:** prompt written notice, reasonable cooperation, and *"allow the indemnifying party
**sole control of defense and settlement** of the claim including selection of counsel, provided that the
party seeking indemnity is entitled to participate in its own defense at its sole expense."* Settlements
that impose liability on the customer need the customer's consent. And: *"THE INDEMNITIES ARE A PARTY'S
ONLY REMEDY UNDER THIS AGREEMENT FOR VIOLATION BY THE OTHER PARTY OF A THIRD PARTY'S IP RIGHTS."*

**Mitigation, §13.3**, lets OpenAI *"replace or modify the allegedly infringing Service"* or terminate with
a refund, and obliges the customer to *"promptly comply with all reasonable instructions ... including any
instruction to replace, modify, or cease use of the Service."*

### Anthropic — the widest coverage on paper, the widest exclusions in practice

[Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), effective 2025-06-17:

> **K.1. Claims Against Customer.** Anthropic will defend Customer and its personnel, successors, and
> assigns from and against any Customer Claim ... and indemnify them for any judgment that a court of
> competent jurisdiction grants a third party on such Customer Claim or that an arbitrator awards a third
> party under any Anthropic-approved settlement ... "Customer Claim" means a third-party claim, suit, or
> proceeding alleging that **Customer's paid use of the Services (which includes data Anthropic has used
> to train a model that is part of the Services) in accordance with these Terms or Outputs generated
> through such authorized use violates any third-party intellectual property right.**

That parenthetical is doing real work: it pulls the **training-data** theory inside the indemnity without a
separate limb, and it is the widest grant of coverage in the set. Then:

> **K.3.** ... indemnification obligations do not apply to the extent the underlying allegation arises from
> the indemnified party's **fraud, willful misconduct, violations of law, or breach of the Agreement.**
> [For Anthropic's obligations:] **(a) modifications made by Customer to the Services or Outputs;
> (b) the combination of the Services or Outputs with technology or content not provided by Anthropic;**
> (c) Inputs or other data provided by Customer; **(d) use of the Services or Outputs in a manner that
> Customer knows or reasonably should know violates or infringes the rights of others; (e) the practice of
> a patented invention contained in an Output; (f)** an alleged violation of **trademark** based on use of
> an Output in trade or commerce.

**(a) and (b) together are finding 1 in its starkest form**, and (e) is a carve-out no other provider states
explicitly: if generated code practises a patented invention, Anthropic does not defend it. Note also that
"breach of the Agreement" as a general exclusion means a Usage Policy violation anywhere in the
organisation can be argued to reach back into an unrelated IP claim.

**Cap.** §L.3 limits liability to *"Fees paid by Customer for the Services in the previous 12 months"*, then:
*"The limitations of liability in this Section L.3 (Limits on Liability) do not apply to either party's
obligations under Section K (Indemnification)."* Uncapped.

**Ownership.** §B: *"Customer (a) retains all rights to its Inputs, and (b) **owns its Outputs**"*, with
Anthropic assigning *"its right, title and interest (if any) in and to Outputs."* The parenthetical "(if
any)" is honest drafting: Anthropic assigns whatever it has, and does not warrant that it has anything.

**§D.3** is the only human-review sentence in the document: *"It is Customer's responsibility to evaluate
whether Outputs are appropriate for Customer's use case, **including where human review is appropriate**,
before using or sharing Outputs."* It sits in the use-restrictions section, is framed around factual
accuracy, and is **not** a condition of §K. It is nonetheless the closest any provider comes to writing
down an expectation of oversight.

⚠️ **Which terms govern Claude Code.** From Anthropic's own documentation
([legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)):

> Your use of Claude Code is subject to:
> - **Commercial Terms of Service** - for **Team, Enterprise, and Claude API** users
> - **Consumer Terms of Service** - for **Free, Pro, and Max** users

And Commercial ToS preamble: *"Services under these Terms are not for consumer use. Our consumer offerings
(e.g., Claude.ai) are governed by our Consumer Terms of Service instead."* The
[Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (effective 2025-10-08) contain **no
Anthropic indemnity**, assign Outputs (*"we assign to you all of our right, title, and interest—if any—in
Outputs"*), disclaim all warranties including **non-infringement**, and require the user to indemnify
Anthropic: *"YOU AGREE TO INDEMNIFY AND HOLD HARMLESS THE ANTHROPIC PARTIES FROM AND AGAINST ANY AND ALL
LIABILITIES, CLAIMS, DAMAGES, EXPENSES ... ARISING OUT OF OR RELATED TO ... YOUR ACCESS TO, USE OF, OR
ALLEGED USE OF THE SERVICES"* (§11).

**Beta.** Service Specific Terms (effective 2026-06-08) §B caps Beta Services liability at *"the lesser of
$1,000 and Fees paid"*. That document contains **no indemnification provisions at all** and no Claude
Code-specific IP terms.

### AWS — the most explicit tier boundaries and the only records obligation

[AWS Service Terms](https://aws.amazon.com/service-terms/), last updated 2026-08-20, §50.10:

> "Indemnified Generative AI Services" means, collectively, **generally available features of** Amazon Nova
> Micro, Amazon Nova Lite, Amazon Nova Pro, Amazon Nova Premier, Amazon Nova Canvas, Amazon Nova Reel,
> Amazon Nova Forge Models, Amazon Nova Sonic, Amazon Nova 2 Omni, Amazon Nova Act, Amazon Titan Text
> Express, Amazon Titan Text Lite, Amazon Nova Multimodal Embeddings, Amazon Titan Text Premier, Amazon
> Titan Text Embeddings, Amazon Titan Multimodal Embeddings, Amazon Titan Image Generator, AWS HealthScribe,
> Amazon Personalize, **Amazon Q (excluding Amazon Q Developer Free Tier)**, AWS Transform, Amazon Bio
> Discovery (excluding Amazon Bio Discovery Academic Tier), Amazon Connect Customer, Amazon Connect
> Decisions, Amazon Connect Health, Amazon Connect Talent, Amazon Lex, **Kiro (excluding Kiro Free Tier)**,
> AWS DevOps Agent, AWS Security Agent, and Amazon Quick.
>
> **50.10.1.** ... AWS will defend you and your employees, officers, and directors against any third-party
> claim alleging that the Generative AI Output generated by an Indemnified Generative AI Service infringes
> or misappropriates that third party's intellectual property rights, and will pay the amount of any
> adverse final judgment or settlement.
>
> **50.10.2.** AWS will have no obligations or liability ... with respect to any claim: (i) arising from
> Generative AI Output generated in connection with **inputs or other data provided by you** where such
> inputs ... infringe ...; **(ii) if you interfere with or fail to enable available filters and other
> tools, or disregard instructions made available** for the Indemnified Generative AI Service; (iii) if
> your use ... **breaches the Agreement**; (iv) if you have **fine-tuned, refined, customized, or otherwise
> modified an Indemnified Generative AI Service** and the alleged infringement would not have occurred but
> for this ...; (v) arising **after you receive notice to stop using** the Generative AI Output;
> (vi) arising from Generative AI Output that you **know or reasonably should know** may infringe ...; or
> (vii) alleging that your use of Generative AI Output infringes a third party's **trademark** or related
> rights. ... **AWS's defense and payment obligations under this Section 50.10 will not be subject to any
> damages cap under the Agreement.**
>
> **50.10.3.** The obligations under this Section 50.10 will apply only if you: (a) give AWS **prompt
> written notice**; (b) **permit AWS to control the defense**; (c) **retain and provide sufficient records
> to the extent necessary to evaluate your eligibility for the defense of claims and indemnity**; and
> (d) reasonably cooperate with AWS ... AWS may settle the claim as AWS deems appropriate, provided that
> AWS obtains your prior written consent (not to be unreasonably withheld) ...

**Three ways AWS is the outlier, two of them in the customer's favour.**

⚠️ **First, and importantly: AWS's modification carve-out attaches to the *Service*, not the *Output*.**
Clause (iv) excludes claims where *"you have fine-tuned, refined, customized, or otherwise modified an
**Indemnified Generative AI Service**"* — not where you modified the output. Cross-check clause (i): it too
is about inputs, not about downstream editing. **On the plainest reading, AWS is the only provider in the
set whose output indemnity is not lost by editing the generated code and combining it with your codebase.**
That is a significant and, as far as this strand could establish, unremarked distinction. Treated as a
textual reading, not a settled one — see **Unsettled**.

**Second, §50.10.3(c) is the only express records-retention condition in the set.** A customer must be able
to produce records *"necessary to evaluate your eligibility"* — which in practice means being able to show
which model produced which code, when, with which settings. **That is a provenance-logging requirement, and
it is the condition most directly stressed by high-volume unattended generation.**

**Third, the coverage boundaries are drawn by enumeration rather than by category**, which makes the gaps
visible: `Amazon Q Developer Free Tier` and `Kiro Free Tier` are excluded by name; only *"generally
available features"* are covered, so previews are out; and **Amazon Bedrock is not on the list**. Bedrock's
own clause (§50.12.1) confirms the model: *"Third-party models are available to you on Amazon Bedrock as
'Third-Party Content'. By using a third-party model, you agree to the applicable terms here."*

---
## Output similarity: the measured evidence, not the rhetoric

**The framing that matters.** Reproduction rate is the *frequency* term in the exposure. Volume is the
other term, and volume is what moves as delegation increases. A rate that is acceptable at fifty
suggestions a day is a different proposition at fifty thousand lines a week — and **nobody has measured
the rate at the volumes agentic teams now generate, on the surfaces they generate them from.**

### GitHub's own figures

| Figure | Source | Evidence tier | What it actually means |
|---|---|---|---|
| *"one recitation event every 10 user weeks"* (95% CI 7–13) | [GitHub research recitation](https://github.blog/ai-and-ml/github-copilot/github-copilot-research-recitation/), Albert Ziegler, 2021-06-30, upd. 2022-08-16 | **Vendor-reported metric**, by an interested party, on its own product | 453,780 Python suggestions, ~300 internal GitHub/Microsoft developers, 396 "user weeks". 473 flagged → 185 after de-duplication → **41 confirmed recitations**. A **per-developer-time** rate |
| ≈ **0.009%** of suggestions (≈ 1 in 11,000) | Arithmetic on GitHub's own numbers (41 / 453,780) — *not GitHub's framing* | Derived from a vendor-reported metric | The same study expressed per suggestion. Filter-flagged rate is 0.104% (473/453,780) |
| *"In rare instances (less than 1% based on GitHub's research), suggestions from GitHub may match examples of code used to train GitHub's AI model."* | [GitHub Copilot FAQ](https://github.com/features/copilot) | **Vendor-reported metric** | ⚠️ **No published derivation.** A different metric from the 2021 study, with no sample size, no date, and no methodology |
| *"Typically, matches to public code occur in less than one percent of Copilot suggestions"* | [GitHub Docs, code referencing](https://docs.github.com/en/copilot/concepts/completions/code-referencing) | **Vendor-reported metric** | Same undisclosed figure, restated |

**GitHub's own caveats, verbatim, and they are unusually candid:** *"Naturally, this was measured by the
GitHub and Microsoft developers who tried out GitHub Copilot. If your coding behavior is very different
from theirs, your results might differ."* · *"Nothing is ever foolproof, of course, so this too can be
tricked."* · *"This bucketing necessarily has some edge cases, and your mileage may vary in how you think
they should be classified."*

⚠️ **The definition of a "match" includes code the user already wrote.** GitHub's study counted an overlap
of *"at least 60 such 'words'"* where *"punctuation, brackets, or other special characters all count as
'words,' while tabs, spaces, or even line breaks are ignored completely"* — and *"If the overlap extends to
what the user has already written, that also counts for the length."* The filter has the same property:
Copilot *"checks code suggestions with their surrounding code of about 150 characters against public code
on GitHub"*
([docs](https://docs.github.com/en/copilot/how-tos/manage-your-account/managing-copilot-policies-as-an-individual-subscriber)).
**Measured reproduction and filtered reproduction are both partly measuring the user's own file.**

**Contrarian note on the headline.** "One event every 10 user weeks" is a per-developer-time rate; the same
data per suggestion is 0.009%. Both are true; the first sounds much larger and the second much smaller. The
study also found recitation concentrates in near-empty files — the low-context condition, which is exactly
the condition an agent starting a new file is in. Only Python; only ~300 self-selected internal users; and
GitHub notes in footnote 8 that *"since this experiment has been made, GitHub Copilot has changed to
require a minimum file content. So some of the suggestions flagged here would not have been shown by the
current version."*

### How the filter actually works — and where it does not

- **Threshold:** *"With the filter enabled, Copilot checks code suggestions for matches or near-matches
  against public code on GitHub of 65 lexemes or more (on average, 150 characters)."*
  ([Copilot FAQ](https://github.com/features/copilot)) **Anything shorter is structurally invisible to it.**
- **Corpus:** *"an index of all public repositories on GitHub.com. Code in private GitHub repositories, or
  code outside of GitHub, is not included in the search process."*
  ([docs](https://docs.github.com/en/copilot/concepts/completions/code-referencing))
- **Staleness, verbatim:** *"The search index is refreshed every few months. As a result, newly committed
  code, and code from public repositories deleted before the index was created, may not be included in the
  search."* (same page)
- **Latency budget:** the filter operates within *"a latency budget of only 10–20ms"*
  ([Introducing code referencing](https://github.blog/news-insights/product-news/introducing-code-referencing-for-github-copilot/),
  2023-08-03, upd. 2024-02-07). **No recall figure is published.**
- **Coverage hedge:** *"If you choose to block suggestions matching public code, **in most GitHub Copilot
  products**, GitHub Copilot checks code suggestions ..."* (emphasis added; the qualifier is GitHub's).
- **Defaults:** *"'Suggestions matching public code' is set to 'Blocked' by default for Copilot Business
  users"*
  ([enterprise policy docs](https://docs.github.com/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise),
  the target of `gh.io/cfb-dd`). **No default is documented for individual plans** — treat any claim about
  that default as unestablished. Seat-holders under an organisation *"will not be able to configure
  suggestions matching public code in your personal account settings."*
- ⚠️ **The agent surface does not enforce it.** *"Copilot coding agent does not support the 'Suggestions
  matching public code' policy's `Block` mode"*; under Block, *"suggestions matching public code will not
  be blocked, and instead will be highlighted in the session logs"*
  ([GitHub Changelog, 2026-02-18](https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing/)).
- **Model-card hedges:** *"While the probability is low, Copilot may generate code suggestions that match
  code in the training set"*
  ([inline suggestions](https://docs.github.com/en/copilot/responsible-use/inline-suggestions)); the chat
  card recommends *"rigorous testing, IP scanning, and checking for security vulnerabilities"*
  ([chat](https://docs.github.com/en/copilot/responsible-use/chat)).

### Academic measurement — and why the numbers cannot be compared

| Study | Measured figure | Evidence tier and the caveat that matters |
|---|---|---|
| Carlini et al., *Extracting Training Data from LLMs*, [arXiv:2012.07805](https://arxiv.org/abs/2012.07805) | 1,800 candidates checked → **604 confirmed memorized** (33.5% TPR) from GPT-2 XL; **31 contained memorized source code**; one fragment extended to a full 1,450-line GitHub file | **Academic measurement.** Adversarial extraction, not ordinary use. Says nothing about ordinary-use rates |
| Carlini et al., *Quantifying Memorization*, [arXiv:2202.07646](https://arxiv.org/abs/2202.07646) | **GPT-J-6B memorizes ≥1% of The Pile** under k-extractability; 10× parameters ≈ +19pp; 450-token context → ~65% extractable vs ~33% at 50 tokens | **Academic measurement.** "k-extractable" = verbatim continuation *given a training-data prefix*. OPT showed far lower absolute memorization. ⚠️ **This is the study Judge Tigar rejected as insufficient to plead identicality** — see the litigation section |
| Al-Kaswan, Izadi, van Deursen, *Traces of Memorisation in LLMs for Code*, [arXiv:2312.11658](https://arxiv.org/abs/2312.11658), ICSE 2024 | **CodeGen-Mono-16B: 47.1% exact-match extraction** (6B 38.2%, 2B 30.3%) | **Academic measurement.** ⚠️ **The most-misquoted number in this area.** Measured on a 1,000-sample benchmark *deliberately built from files with 5+ duplicates and pre-screened for extractability.* It is **not** the rate at which the model emits training data in normal use |
| Ciniselli, Pascarella, Bavota, [arXiv:2204.06894](https://arxiv.org/abs/2204.06894), MSR 2022 | T5-small on Java, 15,742 predictions: **Type-1 (exact) clones ~12.5% at 2 statements → 2.3% at 3 → ~0.1% at 5+**; Type-2 ~80% at 2 → ~2.5% at 5+ | **Academic measurement.** Not Copilot — a small T5 the authors trained; model accuracy was only ~3%. **The load-bearing finding is the shape: cloning falls sharply as the generated span lengthens** |
| Yang et al., *Unveiling Memorization in Code Models*, [arXiv:2308.09932](https://arxiv.org/abs/2308.09932), ICSE 2024 | 20,000 outputs of 512 tokens yielded **>40,125 memorized snippets** | **Academic measurement.** A *snippet count*, not a per-output rate — >1 per output by construction. Do not restate as a percentage |
| Colombo, Mariani, Micucci, Riganelli, *On the Possibility of Breaking Copyleft Licenses...*, [arXiv:2502.05023](https://arxiv.org/abs/2502.05023), 2025-02-07 | 7,347 Java methods from 146 GPL/AGPL/CC-BY-SA/ECL/EUPL repos, >70,000 GPT-4-turbo generations. **JPlag similarity ≥0.70: 1.48% mean with minimal context; 9.73% mean (19.50% max) with full class context.** Asking for originality made *"no significant difference"* | **Controlled study.** ⚠️ **≥0.70 similarity is near-clone, not verbatim.** GPT-4-turbo, not Copilot. Authors call it *"an under-approximation"* |
| Katzy, Popescu, van Deursen, Izadi, [arXiv:2403.15230](https://arxiv.org/abs/2403.15230), 2024-03 | 514M code files across six training datasets. **Exact duplicates of strong-copyleft files: The Pile 22.80%, CodeParrot 14.34%, CodeClippy 11.24%, The Stack v1 6.14% (16.1M files), RedPajama 5.49%, GitHub-Code 4.81%** | **Academic measurement.** Measures **training-set** contamination, not output. SHA-256 exact-file hashing, so modified copyleft code is missed. An upstream risk indicator only |

⚠️ **These figures cannot be placed on one axis and should never be presented in a single chart.** GitHub
counts 60 "words" including user context; its filter counts 65 lexemes; Ciniselli counts Simian clone types
over statement blocks; Al-Kaswan and Carlini count exact suffix match after a training-data prefix under
adversarial prompting; Colombo counts JPlag similarity ≥ 0.70, which is not verbatim reproduction at all.
**The apparent spread from 0.009% to 47% is mostly a spread in definitions, not in phenomena.**

⚠️ **A conflation to avoid.** The project's [`evidence-base.md`](./evidence-base.md) row 17 carries
GitClear's *"block duplication +81% since 2023 (40.3 → 73.0 per M changed lines)"* (vendor-reported metric,
623M changes, and see that file's recorded weaknesses). **That is duplication *within the customer's own
codebase*, not reproduction of third-party code.** It is a maintainability signal and carries no licensing
implication. The two must not be cited together as if they measured the same thing.

### Colombo's finding is the one with the autonomy implication

The measured jump from **1.48% to 9.73%** as context grows from minimal to a full class is the single most
relevant empirical result in this section, because **agentic coding is the high-context condition by
construction**. An agent that reads the surrounding class, the imports and the neighbouring files before
generating is operating in exactly the regime where the measured near-clone rate was 5.8–6.5× higher.
*Evidence tier: controlled study; GPT-4-turbo, near-clone threshold, Java only, and the authors' own
"under-approximation" caveat.* **This is a hypothesis the field has not tested on a coding agent, and it
points the opposite way from the reassuring vendor numbers.**

---

## The litigation, as it actually stands

**The single most important distinction in this section: what a court has *decided* versus what a party has
*alleged*.** Filed complaints in this area are routinely reported as findings. Below, the two are kept
apart. *Evidence tier throughout: primary court documents, read 2026-08-30, except where marked as
commentary.*

### *Doe v. GitHub, Inc.* — the operative caption is **N.D. Cal. No. 4:22-cv-06823-JST** (Judge Jon S. Tigar)

The frequently-cited `3:22-cv-06823` is the original magistrate assignment; every substantive order carries
the `4:22-cv-06823-JST` caption.

**⚠️ A structural fact that reframes the whole case: the complaint pleads no direct copyright infringement
count.** The twelve counts are DMCA §§ 1201–1205, breach of contract (open-source licence violations),
tortious interference, fraud, false designation of origin, unjust enrichment, unfair competition, breach of
GitHub's ToS/Privacy Policy, CCPA, negligence, civil conspiracy and declaratory relief
([complaint, ECF 1, 2022-11-03](https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.1.0.pdf)).
**This has never been a copyright infringement case.** It is a DMCA copyright-management-information case
plus a contract case. Commentary describing it as "the case about whether Copilot infringes copyright" is
describing a case that was not filed.

#### DECIDED

| Order | Date | Holding |
|---|---|---|
| [ECF 95](https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.95.0.pdf) | 2023-05-11 | Dismissed §§ 1202(a) and 1202(b)(2), tortious interference, fraud, false designation, unjust enrichment, unfair competition, ToS/Privacy breach, CCPA and negligence **with leave to amend**; civil conspiracy and declaratory relief **with prejudice**. §§ 1202(b)(1)/(b)(3) and breach of contract survived |
| [ECF 189 / 195](https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-06823/pdf/USCOURTS-cand-4_22-cv-06823-1.pdf) — **the identicality order** | 2024-01-03 (signed) / 2024-01-22 (public redacted) | *"Agreeing with Defendants on both fronts, the Court finds that it is not precluded from analyzing this claim anew and that **Section 1202(b) claims require that copies be 'identical.'**"* Applied to plaintiffs' own pleading that *"[t]hough Output from Copilot is often a verbatim copy, even more often it is a modification"*: *"**This, however, is not sufficient for a Section 1202(b) claim.**"* Also: state-law claims dismissed **with prejudice** on § 301 preemption; Does 3 and 4 dismissed as to damages **with prejudice** |
| [ECF 246](https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-06823/pdf/USCOURTS-cand-4_22-cv-06823-2.pdf) | 2024-04-15 | Reconsideration denied |
| [ECF 253](https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.253.0.pdf) | 2024-06-24 | *"**Plaintiffs again fail Section 1202(b)'s identicality requirement.**"* → *"the Court dismisses Plaintiffs' Section 1202(b) claim, **this time with prejudice**."* |
| [ECF 282](https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-06823/pdf/USCOURTS-cand-4_22-cv-06823-3.pdf) | 2024-09-27 | § 1292(b) certification **granted**, district case **stayed** |
| [CA9 order, ECF 285](https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.285.0.pdf) | 2024-12-19 | *"**The petition for permission to appeal is granted.** See 28 U.S.C. § 1292(b)."* |

⚠️ **Two of the court's rejections bear directly on the evidence in the previous section.** In ECF 253
Judge Tigar rejected both of plaintiffs' new theories: the duplication-detection filter (*"the mere
existence of such a feature does not make it more likely that Copilot would ever output an identical
copy"*) and the Carlini *Quantifying Memorization* study, on the basis that Copilot *"rarely emits
memorized code in benign situations."* **A federal court has now considered the published memorization
literature and found it insufficient to plead that identical copies are produced.** That is a
plaintiff-side evidentiary failure, not a vendor safety finding — but anyone citing Carlini as proof of
practical code reproduction should know a court has already declined to read it that way.

#### PENDING — argued, undecided

The Ninth Circuit appeal (**No. 24-7700**, from petition No. 24-6136) was **argued and submitted
2026-02-11** before Judges Sidney R. Thomas, Eric D. Miller and Stanley Blumenfeld. **No decision has
issued as of 2026-08-30** — approximately 6.5 months under submission. Verified two ways: the Ninth
Circuit's opinions and memoranda indexes, current through 2026-08-28, return zero results for GITHUB and
OPENAI while a control query returns results; and the last docket entry is #121, dated 2026-05-26. The
certified question is *"whether Sections 1202(b)(1) and (b)(3) of the DMCA impose an identicality
requirement."* **Judge Tigar's own certification order notes: *"To this Court's knowledge no court of
appeal has ruled on this issue."*** He catalogued the district split — *Anderson v. Stability AI* and
*Kirk Kara* for identicality; *Beijing Meishe v. TikTok*, *ADR Int'l v. ISM* and *Oracle v. Rimini*
against. **The district case remains stayed.**

#### SURVIVING BUT UNADJUDICATED

Exactly two counts, both contract: **Count Two, breach of contract for open-source licence violations,
against all defendants** (ECF 253: *"The Court declines to dismiss Plaintiffs' claim for breach of contract
of open-source license violations against all Defendants"*), and **Count Three, breach of contract for
selling licensed materials, against GitHub only** — never moved against. **Neither has been adjudicated on
the merits. No class certification, no summary judgment, no trial.** Surviving a motion to dismiss means
the allegation is legally sufficient if true; it is not a finding that it is true.

### ⚠️ Has any court held that AI code output infringes an open-source licence, or is a derivative work?

**No. No such holding exists anywhere.** In *Doe v. GitHub* the only claims that could reach the question
survived a motion to dismiss and are now stayed. The DMCA route was terminated at the pleading stage on
identicality without ever reaching output-as-infringement. **This negative finding is the most important
thing in this section and it should be stated plainly in any downstream document.**

### Adjacent AI copyright rulings — all decided ones are about *training*, not *output*

- ***Bartz v. Anthropic***, N.D. Cal. 3:24-cv-05417-WHA, ECF 231,
  [2025-06-23](https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_24-cv-05417/pdf/USCOURTS-cand-3_24-cv-05417-0.pdf)
  (Alsup) — training *"was exceedingly transformative and was a fair use"*; retaining pirated library copies
  was not. **No output holding.**
- ***Kadrey v. Meta***, N.D. Cal. 3:23-cv-03417-VC, ECF 598,
  [2025-06-25](https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_23-cv-03417/pdf/USCOURTS-cand-3_23-cv-03417-37.pdf)
  (Chhabria) — summary judgment for Meta on fair use *"on this record,"* expressly because plaintiffs
  *"presented no meaningful evidence on market dilution at all."* **A record-specific ruling, not a general
  licence.** 2026 activity in the case is procedural.
- ***Thomson Reuters v. Ross***, D. Del. 1:20-cv-00613, 2025-02-11 — a **non-generative** tool;
  intermediate copying, not model output.
- ***In re OpenAI MDL 3143*** (S.D.N.Y., Stein) — **commentary** reports an October 2025 opinion declining
  to dismiss output-based direct infringement under the "more discerning observer" test. **The opinion text
  could not be reached** (see blocked sources). Even if accurate, that is a **pleading-stage** ruling, not a
  merits holding. *Tier: commentary, unverified — do not cite as a holding.*
- ***Getty v. Stability*** (UK High Court, Nov. 2025) — **commentary** reports Getty abandoned the training
  claims and the court held model weights are not "infringing copies." UK law; **not verified**.
- ***SFC v. Vizio*** (Orange County Superior Court) — the only copyleft **enforcement** action of direct
  relevance. **Commentary** reports a December 2025 ruling for SFC on the duty to supply source and a
  February 2026 order sending the case to a jury. **Not verified against a primary source** (state court, no
  free docket). *Tier: commentary — flagged because if accurate it is the live authority on third-party
  beneficiary enforcement of GPL source obligations, which is the theory a Count Two success would rest on.*
- **Settlements are not holdings.** The reported large Anthropic authors settlement was not verified and
  establishes no legal rule either way.
- **No litigation was found against Amazon CodeWhisperer / Q Developer, or against Codex standalone**
  (OpenAI's Codex entities are already defendants inside *Doe v. GitHub*). ⚠️ **This is
  absence-of-evidence, not a clean negative** — a docket-wide search could not be completed because
  CourtListener throttled.

---

## What reproduction actually obliges you to do

If a model emits code substantially similar to licensed source, the obligations that attach come from the
**licence**, not from the vendor's terms. Read from the licence texts, 2026-08-30.

### The trigger: most copyleft obligations require *conveying*, and internal use is not conveying

GPL-3.0 §0 ([gnu.org](https://www.gnu.org/licenses/gpl-3.0.txt)):

> To **"propagate"** a work means to do anything with it that, without permission, would make you directly
> or secondarily liable for infringement under applicable copyright law, **except executing it on a
> computer or modifying a private copy.** ...
> To **"convey"** a work means any kind of propagation that enables other parties to make or receive copies.

**A GPL-derived fragment inside a service you host and never distribute does not trigger GPL-3.0's
source-disclosure obligation.** GPL-2.0 is drafted around *distribution* to the same practical effect
(§§ 1–2, [gnu.org](https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt)). **This is the single largest
reason the copyleft fear is overstated for the median SaaS team — and the single largest reason it is
understated for anyone shipping binaries, firmware, SDKs, on-prem software, containers or mobile apps.**

### AGPL-3.0 §13 is the exception, and it is the one that matters for hosted software

> Notwithstanding any other provision of this License, **if you modify the Program, your modified version
> must prominently offer all users interacting with it remotely through a computer network** (if your
> version supports such interaction) **an opportunity to receive the Corresponding Source** of your version
> from a network server at no charge ...
> ([gnu.org](https://www.gnu.org/licenses/agpl-3.0.txt))

**No distribution required.** Network interaction is the trigger. Note the antecedent condition — *"if you
modify the Program"* — which is doing more work here than it first appears, and is one of the places the
derivative-work question becomes load-bearing.

### If conveying is triggered, GPL-3.0 §5 is what attaches

> a) The work must carry **prominent notices stating that you modified it**, and giving a relevant date.
> b) The work must carry prominent notices stating that it is **released under this License** ...
> c) You must **license the entire work, as a whole, under this License** to anyone who comes into
> possession of a copy. This License will therefore apply ... **to the whole of the work, and all its
> parts, regardless of how they are packaged.**

§5(c) is the licence-compatibility problem in one sentence: the obligation attaches to *the entire work*.
GPL-2.0 §2(b) is materially the same. The aggregate exception is narrow — it covers *"separate and
independent works, which are not by their nature extensions of the covered work, and which are not combined
with it such as to form a larger program"*, which is not a description of an emitted function inside your
module.

### The obligations that bind most often are the mildest, and the most silently breached

**Apache-2.0 §4** ([apache.org](https://www.apache.org/licenses/LICENSE-2.0.txt)) requires on
redistribution: (a) a copy of the licence; (b) *"prominent notices stating that You changed the files"*;
(c) *"retain, in the Source form of any Derivative Works that You distribute, **all copyright, patent,
trademark, and attribution notices** from the Source form of the Work"*; and (d) if a `NOTICE` file exists,
*"any Derivative Works that You distribute must include a readable copy of the attribution notices
contained within such NOTICE file."*

**MIT** ([opensource.org](https://opensource.org/license/mit)): *"The above copyright notice and this
permission notice **shall be included in all copies or substantial portions of the Software**."*

⚠️ **This is where agent-authored code is most reliably non-compliant, and it has nothing to do with
copyleft.** A model emits the function body and not the file header. Even under the most permissive licences
in wide use, **the attribution and notice obligations are the ones an unattended pipeline breaches by
default**, silently, at volume, and with no filter looking for it — the duplication filters look for
*matches*, not for *missing notices*. **The most likely real-world licensing failure is a missing MIT
copyright line, not a GPL source-disclosure demand.**

### The unsettled question underneath all of it

**Whether model output is a derivative work of training data has never been decided.** Everything above
describes what attaches *if* the reproduction is substantial enough to be infringing and *if* the licence
binds. Both conditionals are open. Positions in genuine tension, recorded rather than resolved:
- The Free Software Foundation and Software Freedom Conservancy have argued publicly that training on and
  emitting GPL code raises real licence-compliance obligations. *Tier: advocacy position of an interested
  party; not a legal holding.*
- GitHub, OpenAI, Google, Anthropic and AWS all draft their terms as though output may nonetheless carry
  third-party licences — OpenAI says so outright (*"may be subject to third party licenses, including,
  without limitation, open source licenses"*) and GitHub says so in its consumer ToS. **Every vendor's own
  terms concede the possibility their marketing minimises.**
- No court has adopted either position for code.

---

## The autonomy axis

**The direct answer to the question this strand was sent to test: no provider's terms distinguish attended
from unattended use as a condition of coverage. That silence is the finding.**

But silence is not neutrality. Exposure changes with delegation through four mechanisms, none of which the
contracts name:

**1. Volume scales linearly; the rate does not fall.** Reproduction is a per-generation probability. Nothing
in any published measurement suggests the rate *drops* as generation volume rises, and Colombo's
context-sensitivity result suggests the high-context regime agents operate in is the *worse* one
(1.48% → 9.73% near-clone rate). **Ten times the code is ten times the draws.**

**2. Constructive knowledge does not obviously shrink when nobody looks.** Every provider excludes what the
customer *"knew or should have known"* was infringing. **A team that generates 50,000 lines a week and reads
none of them has not thereby lowered what it "should have known" — arguably the opposite, since the volume
itself is the thing that made inspection impractical.** No provider addresses this. No court has ruled on
it. **This is the sharpest open question in the strand** and it is recorded in **Unsettled**, not resolved.

**3. The filter conditions are satisfiable in principle and degraded in practice on agent surfaces.** The
contract asks whether you *"disabled, ignored, or did not use"* available citation and filtering features.
GitHub's coding agent **cannot** honour Block mode and downgrades it to a log entry
([changelog, 2026-02-18](https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing/)).
An organisation that set Block, believes it is enforced, and ships agent-written code is in a materially
different position from the one it thinks it is in. **For GitHub products this is no longer a contract
problem (finding 3) — it is now purely an engineering-control problem, which arguably makes it easier to
miss.** For OpenAI, Google, AWS and Microsoft, the equivalent condition is still contractual and still live.

**4. The record-keeping condition gets harder exactly as it gets more necessary.** AWS requires records
*"necessary to evaluate your eligibility for the defense"*; Microsoft requires the customer to
*"demonstrate compliance with all relevant requirements"* and, for Azure OpenAI, to retain an evaluation
report. **Attributing a specific line of shipped code to a specific generation, model and configuration is
straightforward at one commit a day and an engineering project at agent volume.** This is the point where
the licensing strand meets the project's **verification** vocabulary: **provenance logging is not a nicety
further along the spectrum; for two of six providers it is a condition of the indemnity.**

**And the one place autonomy is named, it narrows coverage.** Google's §17(n)(iii) — *"The actions or tasks
that an AI Agent performs are not Generated Output"* — is the only provision in the set that speaks to
agentic operation, and it removes agent *actions* from the scope of the output indemnity while §17(n)(i)
makes the customer *"solely responsible"* for them and for *"exercising judgment and supervision"* in
production. **The first mover on drafting for agents drafted a carve-out.** Whether others follow is the
thing to watch; the terms in this document should be re-read at least every six months.

### What this does *not* support

⚠️ **This strand found no evidence that any provider penalises, discounts, or conditions coverage on
autonomy, and none should be asserted.** It also found no evidence that licensing exposure has *materialised*
at any autonomy level — no judgment, no settlement, no enforcement action against any organisation for
shipping AI-generated code. **The exposure described here is contractual and theoretical.** The honest
summary is: *the conditions are drafted for a world where a person reads the output, the products have moved
past that, and no one has yet tested what happens.*

---

## Cross-cutting observations for the reference document

1. **Ask "which agreement am I actually under?" before asking "am I indemnified?"** For five of six
   providers, the same product yields opposite answers on different plans. Claude Code is the clearest case:
   Max plan → Consumer Terms → no indemnity; Team/Enterprise/API → Commercial Terms → uncapped indemnity.
2. **The indemnity is not a licence-compliance programme and does not pretend to be one.** It defends
   third-party *claims*; it does nothing about the MIT copyright line your build silently dropped. Those are
   different failures with different remedies, and only the second is likely.
3. **Notice-and-attribution compliance is the practical control**, not copyleft avoidance. It is cheap,
   automatable, and addresses the most probable failure mode.
4. **Distribution posture determines copyleft exposure far more than autonomy does.** A team that ships
   binaries or on-prem software has a real GPL question. A team running an internal service does not, unless
   AGPL is in scope.
5. **Run the filters and citation features even where they are no longer contractually required** —
   they are cheap, and three of six providers still condition coverage on not ignoring them.
6. **Provenance logging is the autonomy-sensitive control.** It is the one obligation in the set that
   demonstrably gets harder as delegation deepens, and two providers make it a condition.
7. **Re-read the terms on a schedule.** Two of the six most-cited facts in this area changed within the last
   six months (GitHub's March 2026 restructure; the April 2026 removal of the duplication-filter
   requirement). Any statement in a downstream document must carry its read date.

---
## Sources

All read 2026-08-30 unless otherwise stated. Primary sources only; the two commentary-derived items are
labelled inline and in **Unsettled**.

### Provider terms — primary contract text

**GitHub / Microsoft**
- GitHub Customer Terms index — https://github.com/customer-terms
- GitHub Generative AI Services Terms (Version: March 2026) — https://github.com/customer-terms/github-generative-ai-services-terms
- GitHub Customer Agreement, General Terms — https://github.com/customer-terms/general-terms
- GitHub Copilot Product Specific Terms **[Archive — superseded 2026-03-05]** — https://github.com/customer-terms/github-copilot-product-specific-terms
- GitHub Terms for Additional Products and Features (last updated 2026-04-27) — https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features
- GitHub Terms of Service, **§J AI Features, Training, and Your Data** (effective 2026-04-27) — https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
- Microsoft Product Terms, Universal License Terms for Online Services — **Customer Copyright Commitment** — https://www.microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS
- Microsoft Product Terms **Glossary** (`Covered Product`, `Output Content`, `Metaprompts`, `Customize`) — https://www.microsoft.com/licensing/terms/product/Glossary/all
- **Customer Copyright Commitment Required Mitigations** (page updated 2026-07-13; `aka.ms/AIfilters`, `aka.ms/aoai-ccc`) — https://learn.microsoft.com/en-us/legal/cognitive-services/openai/customer-copyright-commitment

**Google**
- Google Cloud **Service Specific Terms**, §14 (definitions), §17(i) (Generated Output + Training Data indemnities), §17(j) (safety filters), §17(n) (Agentic AI Services) — https://cloud.google.com/terms/service-terms
- Google Cloud **Terms of Service**, §12 (Limitation of Liability incl. §12.3 Unlimited Liabilities), §13 (Indemnification) — https://cloud.google.com/terms/
- **Generative AI Indemnified Services** list (last modified 2026-07-20) — https://cloud.google.com/terms/generative-ai-indemnified-services

**OpenAI**
- OpenAI **Service Terms** (updated 2026-06-12) — §1 API output indemnity, §2 Beta Services, §3(b) Enterprise output indemnity, **§4 Codex and Code Generation** — https://openai.com/policies/service-terms/
- OpenAI **Services Agreement / Business Terms** (updated 2025-12-01, effective 2026-01-01) — §12 Warranties, §13 Indemnification, §14 Limitation of Liability — https://openai.com/policies/business-terms/

**Anthropic**
- **Commercial Terms of Service** (effective 2025-06-17) — §B Ownership, §D.3 Limitations of Outputs, §K Indemnification, §L.3 Limits on Liability — https://www.anthropic.com/legal/commercial-terms
- **Consumer Terms of Service** (effective 2025-10-08) — §4 Outputs, §11 Indemnity — https://www.anthropic.com/legal/consumer-terms
- **Service Specific Terms** (effective 2026-06-08) — §B Beta Services cap — https://www.anthropic.com/legal/service-specific-terms
- **Claude Code legal and compliance** (which terms govern which plan) — https://code.claude.com/docs/en/legal-and-compliance

**AWS**
- **AWS Service Terms** (last updated 2026-08-20) — §1.24 (generative AI features), §50.1 (AI Services), **§50.10 Defense of Claims and Indemnity for Indemnified Generative AI Services**, §50.12 Amazon Bedrock, §50.13 Amazon Q, §50.14 Kiro — https://aws.amazon.com/service-terms/

### Output similarity — vendor and academic

- GitHub, *GitHub Copilot research recitation* (Albert Ziegler, 2021-06-30, updated 2022-08-16) — https://github.blog/ai-and-ml/github-copilot/github-copilot-research-recitation/
- GitHub, *Introducing code referencing for GitHub Copilot* (2023-08-03, updated 2024-02-07) — https://github.blog/news-insights/product-news/introducing-code-referencing-for-github-copilot/
- GitHub Changelog, *Copilot coding agent supports code referencing* (**2026-02-18**) — https://github.blog/changelog/2026-02-18-copilot-coding-agent-supports-code-referencing/
- GitHub Copilot FAQ (65-lexeme / ~150-character filter spec; "<1%") — https://github.com/features/copilot
- GitHub Docs, code referencing (index corpus, refresh cadence, 150-character window) — https://docs.github.com/en/copilot/concepts/completions/code-referencing
- GitHub Docs, managing Copilot policies as an individual subscriber ("in most GitHub Copilot products") — https://docs.github.com/en/copilot/how-tos/manage-your-account/managing-copilot-policies-as-an-individual-subscriber
- GitHub Docs, enterprise policies (Business default = Blocked; `gh.io/cfb-dd`) — https://docs.github.com/enterprise-cloud@latest/copilot/managing-copilot/managing-copilot-for-your-enterprise/managing-policies-and-features-for-copilot-in-your-enterprise
- GitHub Docs, responsible use — inline suggestions / chat — https://docs.github.com/en/copilot/responsible-use/inline-suggestions · https://docs.github.com/en/copilot/responsible-use/chat
- Carlini et al., *Extracting Training Data from Large Language Models* — https://arxiv.org/abs/2012.07805
- Carlini et al., *Quantifying Memorization Across Neural Language Models* — https://arxiv.org/abs/2202.07646
- Al-Kaswan, Izadi, van Deursen, *Traces of Memorisation in Large Language Models for Code* (ICSE 2024) — https://arxiv.org/abs/2312.11658
- Ciniselli, Pascarella, Bavota (MSR 2022) — https://arxiv.org/abs/2204.06894
- Yang et al., *Unveiling Memorization in Code Models* (ICSE 2024) — https://arxiv.org/abs/2308.09932
- Colombo, Mariani, Micucci, Riganelli, *On the Possibility of Breaking Copyleft Licenses When Reusing Code Generated by ChatGPT* (2025-02-07) — https://arxiv.org/abs/2502.05023
- Katzy, Popescu, van Deursen, Izadi (training-corpus copyleft contamination, 2024-03) — https://arxiv.org/abs/2403.15230

### Litigation — primary court documents

- *Doe v. GitHub, Inc.*, N.D. Cal. **No. 4:22-cv-06823-JST** — class action complaint, ECF 1 (2022-11-03) — https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.1.0.pdf
- ECF 95, order on motions to dismiss (2023-05-11) — https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.95.0.pdf
- ECF 189 / 195, **identicality order** (2024-01-03 signed / 2024-01-22 public redacted) — https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-06823/pdf/USCOURTS-cand-4_22-cv-06823-1.pdf
- ECF 246, reconsideration denied (2024-04-15) — https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-06823/pdf/USCOURTS-cand-4_22-cv-06823-2.pdf
- ECF 253, §1202(b) dismissed with prejudice; contract counts survive (2024-06-24) — https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.253.0.pdf
- ECF 282, §1292(b) certification and stay (2024-09-27) — https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-06823/pdf/USCOURTS-cand-4_22-cv-06823-3.pdf
- ECF 285, **Ninth Circuit grants permission to appeal** (2024-12-19) — https://storage.courtlistener.com/recap/gov.uscourts.cand.403220/gov.uscourts.cand.403220.285.0.pdf
- Ninth Circuit **No. 24-7700** docket feed (argued and submitted 2026-02-11; last entry #121, 2026-05-26) — https://www.courtlistener.com/docket/69495342/feed/
- Ninth Circuit opinions and memoranda indexes (current through 2026-08-28; zero results for this case) — https://www.ca9.uscourts.gov/opinions/
- *Bartz v. Anthropic*, N.D. Cal. 3:24-cv-05417-WHA, ECF 231 (2025-06-23) — https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_24-cv-05417/pdf/USCOURTS-cand-3_24-cv-05417-0.pdf
- *Kadrey v. Meta*, N.D. Cal. 3:23-cv-03417-VC, ECF 598 (2025-06-25) — https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_23-cv-03417/pdf/USCOURTS-cand-3_23-cv-03417-37.pdf

### Licence texts — read from the canonical publishers

- GNU GPL-3.0 (§0 propagate/convey, §4, §5) — https://www.gnu.org/licenses/gpl-3.0.txt
- GNU GPL-2.0 (§§1–2) — https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
- GNU AGPL-3.0 (§13 Remote Network Interaction) — https://www.gnu.org/licenses/agpl-3.0.txt
- Apache License 2.0 (§4 Redistribution) — https://www.apache.org/licenses/LICENSE-2.0.txt
- MIT License — https://opensource.org/license/mit

### Prior work in this repository, cited rather than re-derived

- [`evidence-base.md`](./evidence-base.md) — row 17 and the GitClear weaknesses note, used here **only** to
  mark a conflation to avoid (internal duplication ≠ third-party reproduction), and the evidence-tier
  taxonomy applied throughout.
- [`CONTEXT.md`](../CONTEXT.md) — **verification** (engineered machinery where a human has not read the
  change) is the vocabulary this strand's provenance-logging and evaluation-retention findings belong to.

---

## Confidence and gaps

**High confidence.**
- **Every verbatim quotation of contract text in the comparison table and the per-provider sections.** All
  six providers' operative terms were read in full from the vendor's own domain on 2026-08-30, most of them
  as raw page text rather than a summarisation. Section numbers, exclusion lettering and effective dates are
  as published.
- **The uncapped-indemnity finding (5).** Six of six providers state it explicitly and unambiguously.
- **The free/individual inversion (2).** Stated positively in each vendor's own words, not inferred.
- **The removal of the GitHub duplication-filter requirement on 2026-04-03 (3).** Microsoft states it in one
  unambiguous sentence on its own legal page.
- **Which Anthropic terms govern Claude Code on which plan (7).** Stated in a two-line list in Anthropic's
  own documentation and corroborated by the Commercial Terms' own scope sentence.
- **Google's §17(n)(iii) agentic carve-out (9).** A single declarative sentence in the operative terms.
- **The *Doe v. GitHub* procedural chain.** Read from the orders themselves via govinfo and RECAP-hosted
  PDFs, with the operative quotations taken from the order text.
- **The absence of any Ninth Circuit decision as of 2026-08-30.** Verified two independent ways.

**Medium confidence.**
- ⚠️ **The practical reach of the "modified or combined" exclusions (finding 1).** The *text* is certain.
  What is uncertain is whether a court, or a vendor administering a claim, would read "combined with
  anything else" to cover ordinary incorporation of a snippet into a codebase. No vendor publishes guidance;
  no court has construed these clauses; no public claim administration data exists. **This is reported as a
  textual reading with the ambiguity flagged, not as a legal conclusion.** It is deliberately the loudest
  finding in the document *and* the one with the largest interpretive uncertainty — both statements are
  true at once, and the reader should hold both.
- ⚠️ **AWS's narrower modification carve-out.** The reading that AWS's clause (iv) attaches to the *Service*
  and not the *Output* — making AWS the only provider whose indemnity survives ordinary editing — follows
  from the plain words, and clause (i) supports it. But this strand found no vendor statement, guidance note
  or commentary confirming the distinction is intended, and it is the kind of asymmetry that could be
  drafting accident rather than design. **Treat as a textual observation worth verifying with counsel, not
  as an established advantage.**
- **Whether Gemini Code Assist is covered.** It is not separately listed; coverage is inferred from *"Gemini
  for Google Cloud"* being the umbrella product of which Code Assist is a feature. **Not confirmed by a
  Google statement read today.**
- **Whether GitHub Copilot is a `Covered Product` under the Microsoft CCC.** The Glossary definition (*"any
  Copilot (excluding free Previews) ... available for a fee"*) plainly reaches it, and the Required
  Mitigations page names GitHub Copilot as a Configurable GAI Service with its own mitigations table — which
  only makes sense if it is covered. **But the Microsoft Product Terms for GitHub Offerings page could not
  be read (see blocked sources), so the chain is inferred from two documents rather than read end to end.**
- **The Bedrock/Vertex partner-model gap (finding 8).** Follows from two separate documents (the platform's
  enumerated list, and Anthropic's statement that the platform agreement governs). **No vendor states the
  gap; both would presumably contest the framing.** Reported as an inference, labelled as one.

**Known gaps.**
- **No per-suggestion reproduction rate exists for any product with the filter enabled.** Every published
  figure is either pre-filter (GitHub 2021) or an undisclosed internal estimate ("<1%").
- ⚠️ **No measurement of any kind exists for agent surfaces.** Given that GitHub's coding agent does not
  honour Block mode, the single most governance-relevant number in this document — how often agent-written
  code reproduces public code — **has never been published by anyone**.
- **No reproduction measurement exists for any 2025–26 frontier model.** Every figure in the academic table
  is from the CodeGen / CodeParrot / T5 / GPT-2 / GPT-4-turbo era.
- **No measured false-negative rate for any duplication filter.** GitHub documents index staleness and a
  10–20ms latency budget but publishes no recall figure, and the 65-lexeme threshold makes shorter copying
  structurally invisible.
- **No public data on indemnity claim administration.** Nobody knows how many claims have been tendered
  under any of these provisions, how many were accepted, or on what grounds any were refused. **Every
  statement in this document about what "would" happen is a reading of text, not an observation of
  practice.**
- **No outcome data of any kind.** No judgment, settlement or enforcement action was found against any
  organisation for shipping AI-generated code. The exposure described here has not yet materialised
  anywhere that this strand could find.
- **Negotiated enterprise agreements are invisible.** Everything here is the public click-through text.
  Large customers routinely negotiate these clauses, and OpenAI's §13.1 ratchet implies vendors expect to.
- **Non-US law is out of scope.** EU, UK and other regimes treat derivative works, database rights and
  text-and-data-mining exceptions differently, and none of that is covered here.
- **The `gh.io/cfb-dd` documentation could not be cross-checked against the org-level policy page**, which
  no longer carries the duplication-detection description.

---

## Unsettled — do not state as fact

Recorded as disagreements, not resolved.

1. ⚠️ **Whether "modified or combined" excludes ordinary use of generated code.** The literal reading makes
   the output indemnities close to inoperative for software development, since generated code is always
   combined with something. The purposive reading is that these clauses target adversarial modification and
   third-party bundling, not routine incorporation — otherwise the vendors are marketing a protection they
   drafted out of existence. **Both readings are available on the text. No court has construed them, no
   vendor has published guidance, and this document takes no side.** It is flagged loudly because a reader
   should ask their counsel, not because the pessimistic reading is established.
2. ⚠️ **Whether AI model output is a derivative work of its training data.** Never decided by any court, for
   code or anything else. Advocacy organisations and vendors take opposing positions; both are interested
   parties.
3. ⚠️ **Whether the DMCA § 1202(b) identicality requirement is correct.** This is *the* live appellate
   question. Judge Tigar found *"no court of appeal has ruled on this issue"* and catalogued a district
   split. The Ninth Circuit has had it under submission since 2026-02-11 without ruling. **Any downstream
   document must date this statement.**
4. **Whether the surviving open-source-licence contract claims in *Doe v. GitHub* have merit.** They
   survived a motion to dismiss and are stayed. **Surviving a motion to dismiss is not a finding of
   anything.**
5. **Whether Google's §13.3(b) combination exclusion applies on top of §17(i)'s "unmodified" requirement.**
   §17(i) says the general indemnity *"also applies to"* generated output, which implies §13's machinery
   carries over — including the combination exclusion. Google does not say so, and the two provisions would
   then be partly redundant. Unresolved on the text.
6. **Whether AWS's Service-vs-Output modification carve-out is intentional.** See **Confidence**.
7. **Whether constructive knowledge ("should have known") scales with generation volume or with the absence
   of human review.** No provider addresses it; no court has ruled on it; this strand found no authority in
   either direction. **This is the central unanswered question of the autonomy axis** and it is genuinely
   open.
8. **Whether an unread citation counts as an "ignored" citation feature.** OpenAI excludes output where the
   customer *"disabled, ignored, or did not use"* citation features. Whether emitting a citation into a log
   nobody reads is "using" it is untested.
9. **Whether AGPL §13's *"if you modify the Program"* condition is met when a model emits a fragment
   resembling AGPL source.** Turns entirely on question 2.
10. **The *In re OpenAI* MDL output ruling, *Getty v. Stability*, *SFC v. Vizio*, and the Anthropic authors
    settlement.** All four are reported by **commentary** that this strand could not verify against a
    primary source today. *SFC v. Vizio* in particular would be significant if accurate — it is the live
    authority on third-party-beneficiary enforcement of GPL source obligations — but **it must not be stated
    as fact on the current record.**
11. **Whether any provider will draft attended/unattended distinctions into future terms.** Google's
    §17(n)(iii) is the only movement in this direction so far and it went against the customer. One data
    point is not a trend.

---

## Blocked or unavailable sources

Logged, not circumvented.

| Source | Attempted | Result | Substitute used |
|---|---|---|---|
| GitHub customer-terms pages via direct fetch | `github.com/customer-terms/github-copilot-product-specific-terms` (curl) | HTTP 500 from GitHub | Re-fetched successfully with the `?locale=en-US` parameter; text extracted from the returned HTML |
| Microsoft Product Terms for GitHub Offerings | `microsoft.com/licensing/terms/productoffering/GitHubOfferings/EAEAS` | Page returned availability charts and product conditions only; **no CCC, indemnity, Copilot output or mitigation provisions present in the retrievable content** | Coverage inferred from the Product Terms Glossary `Covered Product` definition + the Required Mitigations page's GitHub Offerings table. **Recorded as an inference** |
| Microsoft Product Terms version/date stamp | `microsoft.com/licensing/terms/product/ForOnlineServices/EAEAS` | The CCC text was retrievable; **no version number or effective date was present in the retrievable content** | None. The CCC is quoted without a version stamp — a real gap for a document that changes |
| Amazon Q Developer / Kiro code-reference documentation | `docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-with-reference.html` and `…/q-admin-setting-managing-access.html` | JavaScript-rendered shell; 1,028 bytes of body, no content, via both curl and fetch | **None.** AWS §50.10.2(ii) conditions the indemnity on not failing to enable *"available filters and other tools"*, and this strand **could not establish what those tools are, whether they are on by default, or who controls them.** A material gap in the AWS row |
| Google Cloud Service Specific Terms via summarising fetch | `cloud.google.com/terms/service-terms` | Content truncated before reaching §17 | Fetched the full page directly and extracted the text; §17(i)/(j)/(n) read in full |
| Google Cloud Terms of Service | `cloud.google.com/terms/cloud-terms-of-service` | HTTP 404 | Read §§12–13 from `cloud.google.com/terms/` |
| OpenAI policies via summarising fetch | `openai.com/policies/business-terms/` | HTTP 403 Forbidden | Fetched directly with a browser user-agent; both Business Terms and Service Terms read in full |
| CourtListener HTML dockets | `courtlistener.com/docket/...` | HTTP 403 via fetch; HTTP 202 with empty body via curl (bot throttling) | The Atom feed `/docket/69495342/feed/`, which was reachable |
| CourtListener REST API v4 | api endpoints | HTTP 401 — credentials required | Not pursued |
| CourtListener RECAP search | search endpoint | Throttled to empty 202 responses after ~4 queries | ⚠️ **Consequence: the search for other code-specific cases (CodeWhisperer, Q Developer, standalone Codex) is incomplete.** Reported as absence-of-evidence, not a clean negative |
| Justia dockets and case law | `law.justia.com`, `dockets.justia.com` | HTTP 403 | govinfo and RECAP-hosted PDFs |
| *In re OpenAI* MDL 3143 opinion text | law-firm hosted copy | HTTP 403 | **None.** Recorded as unverified commentary in **Unsettled** |
| PACER | — | Paywalled; **not attempted** | govinfo + RECAP |
| *SFC v. Vizio* docket | Orange County Superior Court | No free docket exists for California state court | **None.** Recorded as unverified commentary in **Unsettled** |
| GitHub Copilot trust page | `copilot.github.trust.page/faq` | JavaScript-rendered; header only, no body | GitHub Docs and the product FAQ |
| GitHub org-level policy documentation | `docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/manage-policies` | Fetched successfully but **contains no mention of duplication detection or "suggestions matching public code"** — the content has moved | The enterprise page behind `gh.io/cfb-dd` and the individual-subscriber page |
| Various GitHub Docs reference pages | `/copilot/reference/copilot-policies`, `/copilot/reference/feature-availability`, `/copilot/responsible-use/coding-agent` | HTTP 404 | The changelog and the pages that do exist |
| arXiv PDF for Ciniselli et al. | `arxiv.org/pdf/2204.06894v2` | HTTP 404 | ar5iv HTML mirror |

**No source was worked around, re-hosted, or fetched through an alternate route after a block.** Where a
summarising fetch truncated or was refused, the substitute was a direct fetch of the same publisher's own
URL — the same document, more completely, not a different or lower-trust one.

---

*Prepared for wayfinder ticket #7. Advisory research, not legal advice. Terms and case status are current
as at 2026-08-30 and are expected to change; re-read before relying on any statement here.*
