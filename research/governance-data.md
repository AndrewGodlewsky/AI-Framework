# Data governance: what leaves the building when code becomes context

**Research date: 2026-08-30.** Every claim below is dated by the source I read. Vendor terms and
trust-centre pages carry effective dates where they have them; documentation pages usually do not,
so I record the read date. These pages change monthly — several of the most important findings here
are less than six months old.

**Ticket:** [#7 Governance, Legal & IP by Autonomy Level](https://github.com/AndrewGodlewsky/AI-Framework/issues/7),
strand 4 of 6 — data governance.

**Question:** when a team's code becomes an agent's context, what leaves the building, under what
terms, for how long — and what changes in regulated or air-gapped environments?

> ## This is research, not legal advice
>
> Nothing here is legal advice, and it is not a substitute for counsel. It is a reading of published
> vendor terms, vendor documentation and regulatory text, recorded with sources and dates so that a
> lawyer, a DPO or a procurement team can check it. Contractual position depends on the specific
> agreement a customer has signed — several vendors below negotiate terms that differ from the
> published ones — and on jurisdiction. Where a position is unsettled, it is recorded as unsettled
> in "Unsettled — do not state as fact" rather than resolved.

**Terminology.** This document follows [CONTEXT.md](../CONTEXT.md): *containment* for restricting
what an agent **can** do (never "guardrails" outside a quotation); *lethal trifecta* for private
data access + untrusted content + external communication; "further along the spectrum" for greater
delegation. Vendor plan names ("Free tier", "Pro Tier", "Business") are quoted as the vendors write
them and are product names, not archetypes.

**Evidence tiers used below**, stated with each claim:
- **Binding terms** — a contract document the vendor publishes as governing the service.
- **Vendor documentation** — product docs, trust-centre pages, data-governance pages.
- **Vendor announcement** — changelog or staff-authored community post; first-party but not binding.
- **Regulatory primary text** — regulation, adequacy decision, supervisory-authority opinion.
- **Court record** — judgment or Official Journal notice.

---

## Headline findings

1. ⚠️ **The single most consequential change in the last six months is GitHub's, and it runs in the
   opposite direction to everyone else's.** GitHub told Free, Pro and Pro+ subscribers that
   interaction data — inputs, outputs, code snippets, file names — would be used to train the models
   behind Copilot, **on by default, opt-out, effective 24 April** (GitHub Community Admin post,
   [2026-03-02](https://github.com/orgs/community/discussions/188488); *tier: vendor announcement*).
   The GitHub Privacy Statement effective **27 April 2026** now says: *"User Content and Files: When
   you use our Services, we collect Personal Data included as part of the information you provide
   such as code, inputs, AI outputs, text, documents, images, or feedback"*, processed for
   *"Product Development and Improvement… including artificial intelligence and machine learning
   technologies"*, and shared with *"GitHub affiliates, including Microsoft"* for
   *"training and improving artificial intelligence and machine learning technologies"*
   ([docs.github.com, read 2026-08-30](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement);
   *tier: binding terms*). Business and Enterprise are excluded. **The default for an individual
   developer on a paid personal plan is now "trained on".**

2. ⚠️ **"We don't train on your code" and "we don't keep your code" are different sentences, and
   almost every vendor says the first while the terms say something narrower about the second.**
   Anthropic's commercial retention page: *"We retain inputs and outputs for up to 2 years and trust
   and safety classification scores for up to 7 years if your chat is flagged"*
   ([privacy.claude.com, read 2026-08-30](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data);
   *tier: vendor documentation*). Microsoft's Foundry page describes named humans reading flagged
   prompts: *"Human reviewers assessing potential abuse can access prompts and completions data only
   when that data has already been flagged… The human reviewers are authorized Microsoft employees"*
   ([learn.microsoft.com, doc dated 2026-05-18](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy);
   *tier: vendor documentation*). AWS states plainly that using one model class means opting in to
   *"sharing retained traffic with Anthropic for abuse detection and potential human review"*
   ([docs.aws.amazon.com, read 2026-08-30](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html);
   *tier: vendor documentation*). None of that is training. All of it is code leaving the building.

3. **A model can now carry its own retention floor, and it overrides the customer's zero-retention
   arrangement.** Anthropic designates Claude Fable 5 and Claude Mythos 5 "Covered Models" that
   *"require 30-day data retention and are not available under ZDR"*
   ([platform.claude.com, read 2026-08-30](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention);
   *tier: vendor documentation*). On Bedrock the same models expose `allowed_modes:
   ["provider_data_share"]`, so *"Customers must explicitly set their data retention mode to
   `provider_data_share` before they can invoke these models"* — and Cursor's enterprise
   documentation passes it straight through to its own customers: *"Anthropic stores its inputs and
   outputs to run automatic and human harm-prevention reviews"*
   ([cursor.com, read 2026-08-30](https://cursor.com/docs/enterprise/privacy-and-data-governance);
   *tier: vendor documentation*). **Model choice is now a data-governance decision, not only a
   quality or cost one.**

4. ⚠️ **Exposure widens as delegation increases, and one vendor says so in a single sentence.**
   Cursor: *"Legacy Privacy Mode is not supported for Cloud Agents, because agents need to store code
   and environment data in the cloud while they run"*
   ([cursor.com/docs/cloud-agent/security, read 2026-08-30](https://cursor.com/docs/cloud-agent/security);
   *tier: vendor documentation*). The privacy control that works for the attended IDE does not
   survive the move to the unattended cloud agent. This is the clearest primary-source statement
   found that the data posture is a function of autonomy.

5. **No vendor's terms distinguish attended from unattended use — and that silence is a finding.**
   Across Anthropic's Commercial Terms, GitHub's Generative AI Services Terms, the AWS service pages,
   Google's data-governance page and Cognition's security page, I found no clause that varies
   training, retention or review rights according to whether a human was watching. The variation is
   entirely in *product documentation* — which cloud-agent product stores repositories, which one
   scopes access — not in the contract. A team that has read only the contract has read nothing
   about the autonomy axis.

6. **Ticket #6's finding that `.gitignore`-style exclusion is weak is confirmed by a second vendor,
   in stronger words.** Cursor's own reference page: *"The terminal and MCP server tools used by
   Agent cannot block access to code governed by .cursorignore"*, and *"While Cursor blocks ignored
   files, complete protection isn't guaranteed due to LLM unpredictability"*
   ([cursor.com/docs/reference/ignore-file, read 2026-08-30](https://cursor.com/docs/reference/ignore-file);
   *tier: vendor documentation*). Alongside GitHub's *"Content exclusion is currently not supported
   in Edit and Agent modes"* (established in
   [research/tooling-inline-and-chat.md](./tooling-inline-and-chat.md)), the pattern is now: **file
   exclusion is an editor-context feature, and it stops at the shell.**

7. **The most detailed public account of what an agent actually uploads is Anthropic's, and it
   includes an OS-dependent gap.** For repositories not connected to GitHub, `claude --cloud`
   bundles and uploads *"your full repository history across all branches, plus uncommitted changes
   to tracked files"*. Credential-like uncommitted files are excluded — but the exclusion is
   platform-scoped: *"On macOS, Linux, and WSL, Claude Code leaves uncommitted changes to files named
   like credentials or keys out of the upload"*
   ([code.claude.com, read 2026-08-30](https://code.claude.com/docs/en/claude-code-on-the-web);
   *tier: vendor documentation*). Windows is not in that list. I did not test the behaviour; the
   documentation's own scoping is the finding.

8. **The lethal trifecta is documented by the vendor as an unavoidable residue of cloud execution.**
   *"When running with network access disabled, Claude Code can still communicate with the Anthropic
   API, which may allow data to exit the VM"*
   ([code.claude.com, read 2026-08-30](https://code.claude.com/docs/en/claude-code-on-the-web);
   *tier: vendor documentation*). Egress containment that leaves the inference channel open leaves
   the third leg of the trifecta standing, by design, and the vendor writes it down.

9. **Zero data retention is real, and almost nowhere is it self-serve.** Anthropic: *"ZDR is not
   included in the standard Claude for Enterprise plan and cannot be enabled from your admin
   settings"*. OpenAI: *"these controls are subject to prior approval by OpenAI"*. AWS Bedrock for
   retention-requiring models: *"contact your AWS account manager to discuss eligibility"*. Cursor's
   US-only data residency is *"exclusively offered to enterprise customers"*. The two counterexamples
   are **Bedrock's default posture** — *"by default, Amazon Bedrock does not store model inputs or
   outputs"*, configurable by API and enforceable by SCP — and **Tabnine's deployment model**, where
   the product can be installed inside the customer's own network. (All *tier: vendor documentation*,
   read 2026-08-30; links in §3.)

10. **Amazon Q Developer's opt-out is per-developer, per-IDE, and administrators cannot set it.**
    AWS repeats the same note under every IDE: *"This is a decision for each developer to make inside
    their own IDE. If you are using Amazon Q as part of an enterprise, your administrator will not be
    able to change this setting for you."* The same page records two toggles that do nothing: in
    AWS Cloud9 and Lambda, *"The settings do contain a toggle switch for sharing Amazon Q content
    with AWS, but that switch is non-functional"*
    ([docs.aws.amazon.com, read 2026-08-30](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/opt-out-IDE.html);
    *tier: vendor documentation*). Amazon Q Developer is also sunsetting — end of support
    **2027-04-30** ([research/tooling-background-agents.md](./tooling-background-agents.md)).

11. **The EU-US Data Privacy Framework is standing but under appeal, and that is the honest answer.**
    Commission Implementing Decision (EU) 2023/1795 of 10 July 2023 shows EUR-Lex legal status
    **"In force"** as read on 2026-08-30
    ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023D1795);
    *tier: regulatory primary text*). The General Court dismissed the challenge in
    **T-553/23 Latombe v Commission on 3 September 2025** (ECLI:EU:T:2025:831), and an appeal was
    **brought on 31 October 2025 as C-703/25 P**
    ([OJ notice](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202506610);
    *tier: court record*). No decision on that appeal was found. Adequacy is currently valid; its
    permanence is not established.

12. **Air-gapped and local options exist and are narrower than the marketing implies.** JetBrains
    Full Line code completion *"runs entirely on your local device without sending any code over the
    internet"* ([jetbrains.com, read 2026-08-30](https://www.jetbrains.com/help/idea/full-line-code-completion.html);
    *tier: vendor documentation*) — but it is completion only, not chat and not an agent. Tabnine
    documents SaaS, VPC, on-premises and air-gapped deployments. Devin/Windsurf holds **FedRAMP High,
    IL4/IL5 and ITAR authorisation for Devin CLI and Devin Desktop only**, with Devin itself
    *"In Process"* ([docs.devin.ai/federal/compliance, read 2026-08-30](https://docs.devin.ai/federal/compliance.md);
    *tier: vendor documentation*). Anthropic's self-hosted environments are **public beta**, exclude
    ZDR organisations entirely, and still send the conversation off-site: *"The conversation itself,
    including prompts, responses, and tool results, goes to `api.anthropic.com` for model inference"*
    ([code.claude.com, read 2026-08-30](https://code.claude.com/docs/en/self-hosted-environments)).
    **Self-hosted execution is not self-hosted inference.**

13. **A sharing default worth flagging on its own.** Claude Code on the web sessions shared from a
    Max or Pro account offer **Private** and **Public** visibility, where public *"makes the session
    visible to any user logged into claude.ai"*, and *"Repository access verification is not enabled
    by default"* — beside the vendor's own warning that *"Sessions may contain code and credentials
    from private GitHub repositories"*
    ([code.claude.com, read 2026-08-30](https://code.claude.com/docs/en/claude-code-on-the-web);
    *tier: vendor documentation*). Team and Enterprise accounts get **Private/Team** with
    verification on by default. The riskiest default sits on the individual plan.

---

## 1. The comparison table

The most useful artifact this strand produces. Columns answer, per provider and plan: **trained on
by default? · can it be turned off, by whom? · what is retained, how long? · does paying change the
answer?** All entries read **2026-08-30** unless a different date is given. Every entry is *tier:
binding terms* or *vendor documentation* as marked in the detail sections that follow.

| Provider / plan | Trained on by default? | Off switch — and who holds it | Standard retention | Does paying change it? |
|---|---|---|---|---|
| **GitHub Copilot Free / Pro / Pro+** | **Yes**, since **24 April** (announced 2026-03-02) — inputs, outputs, code snippets, file names | Yes — **the individual developer**, in Copilot account settings. No admin control | Not stated in the terms; Privacy Statement (eff. 2026-04-27) covers User Content incl. code for "product development and improvement" | **No — paying for Pro/Pro+ does not change it.** Only Business/Enterprise is excluded |
| **GitHub Copilot Business / Enterprise** | No — *"GitHub will not use Inputs or Outputs to train generative AI models, unless you have given us documented instructions to do so"* (GitHub Generative AI Services Terms, March 2026) | N/A (already off); documented instructions could turn it on | Terms defer: *"Details on data retention are provided in the product documentation for each Generative AI Service."* Superseded product terms (deprecated 2026-03-05) said prompts *"are deleted once Suggestions are generated"*, with named exceptions | Yes — this is the plan that buys the exclusion |
| **Anthropic — Claude Code / API under Commercial Terms (Team, Enterprise, API)** | No — *"Anthropic may not train models on Customer Content from Services"* (Commercial Terms, eff. 2025-06-17) | N/A; Development Partner Program is an explicit org-admin opt-**in**, first-party API only | **30 days**. Flagged content: **up to 2 years** for inputs/outputs, **7 years** for trust-and-safety classification scores. Feedback transcripts **5 years**. Local transcripts 30 days by default | ZDR available only to *qualified accounts* on Claude for Enterprise, enabled by the account team |
| **Anthropic — consumer Free / Pro / Max (incl. Claude Code on those accounts)** | Setting-dependent: *"We will train new models using data from Free, Pro, and Max accounts when this setting is on (including when you use Claude Code from these accounts)"* | Yes — the individual, at claude.ai data-privacy controls | **5 years** if data use allowed; **30 days** if not | Pro/Max are paid consumer plans and do **not** move you to Commercial Terms |
| **OpenAI API** | No — *"As of March 1, 2023, data sent to the OpenAI API is not used to train or improve OpenAI models (unless you explicitly opt in to share data with us)"* | N/A (opt-in only) | Abuse-monitoring logs **up to 30 days** by default; stateful endpoints (Assistants, conversations, vector stores) retain "until deleted" | ZDR removes content from abuse logs and forces `store:false`; *"subject to prior approval by OpenAI"*, via sales |
| **OpenAI — ChatGPT Business / Enterprise / Edu (incl. Codex in those workspaces)** | No — *"OpenAI doesn't use business data to train its models by default"* | N/A | Conversations follow workspace retention settings; deleted chats *"generally scheduled for permanent deletion within 30 days"*; Compliance Logs Platform retains **30 days** | Yes — the workspace product is what carries the no-training default |
| **OpenAI — ChatGPT consumer (Free/Plus/Pro)** | **Not established here** — openai.com and help.openai.com returned HTTP 403 (see Blocked sources) | Not established | Not established | Not established |
| **Google — Gemini for Google Cloud, incl. Gemini Code Assist Standard & Enterprise** | No — *"Gemini doesn't use your prompts or its responses as data to train its models"* (page updated **2026-08-27**) | N/A; Trusted Tester Program is opt-in | Not stated on the data-governance page. Exception documented: *"When you use code customization, we securely access and store your private code"* | Standard/Enterprise are the editions this page governs |
| **Google — Gemini Code Assist for individuals (free)** | **Product deprecated**: the consumer-account page records deprecation as of **2026-06-18**, directing users to Antigravity. Terms for the successor not retrievable (see Blocked sources) | — | — | — |
| **AWS — Amazon Q Developer Free tier** | **Yes** — *"We may use certain content from Amazon Q Developer Free tier for service improvement… for de-bugging, or for model training"* | Yes — **each developer, per IDE**. AWS: *"your administrator will not be able to change this setting for you"*. Org-level only via AWS Organizations AI services opt-out policy for console/chat surfaces | Not stated | **Yes** — Pro is the fix |
| **AWS — Amazon Q Developer Pro** | No — *"We do not use content from Amazon Q Developer Pro or Amazon Q Business for service improvement"* | N/A | Not stated | Yes. Note: end of support **2027-04-30** |
| **AWS — Amazon Bedrock** | No — *"Amazon Bedrock uses a zero data retention (ZDR) data security model. This means that by default, Amazon Bedrock does not store model inputs or outputs"*, plus zero-operator-access | Retention is an API-set **mode** (`none` / `default` / `provider_data_share` / `inherit`), enforceable org-wide by SCP | Model-dependent. Named exceptions: classifier-flagged GPT-5.x traffic **up to 30 days**; Claude Fable 5 **up to 30 days** and requires opt-in to *"sharing retained traffic with Anthropic for abuse detection and potential human review"* | ZDR for retention-requiring models is *"evaluated on a per-account, per-model basis"* with the account manager |
| **Microsoft Foundry / Azure OpenAI ("models sold by Azure")** | No — prompts, completions, embeddings and training data *"are NOT used to train any generative AI foundation models without your permission or instruction"* | N/A | Stateless inference; **abuse monitoring stores a sample of prompts and completions for human review** unless the customer is approved for modified abuse monitoring | Modified abuse monitoring (no storage, no human review) is an application, for "managed customers" |
| **Cursor** | No when Privacy Mode is on — *"Privacy Mode ensures your code is never used for training by Cursor or other AI model providers"* | Yes. **On by default for Enterprise teams**; individuals must enable it. Enterprise admins can *"Enable Privacy Mode for the team [and] Optionally enforce it so members can't disable it"* | ZDR agreements with most model providers; **exception** — models like Claude Fable 5 where *"Anthropic stores its inputs and outputs to run automatic and human harm-prevention reviews"*, requiring explicit enterprise approval. **Cloud Agents store encrypted repository copies for the run**, deleted after | Enterprise buys enforcement, US-only data residency, and the model-approval gate — not a different training answer |
| **Cognition — Devin / Windsurf (Devin Desktop)** | No — *"By default, Cognition does not train its models on customer data or code"*; enterprise requires express written consent | Paid plans opt out: *"After you opt out, your data will not be used for training and Zero Data Retention will be enabled with our model providers"* | *"Cognition only retains data processed through Devin for the duration of the relationship with a given Customer, unless otherwise specified"* | Yes — the training opt-out and ZDR are described as paid-plan actions |
| **JetBrains AI (AI Assistant, Junie)** | Detailed code-related data: **no for commercial users** — *"We do not collect Detailed code-related data from our commercial users unless explicit, informed consent has been obtained in advance"*. Where collected, it is used for *"training AI models"* | Consent-gated; individual setting in the IDE | **1-year retention** for detailed code-related data; *"The collected data remains stored within the European Economic Area (EEA)"* | Commercial status, not payment per se, is what gates collection (policy v1.6, **2026-07-07**) |
| **Tabnine** | No — *"Tabnine's code completion model and Tabnine Protected chat model are only trained on open source code with permissive licenses"* | N/A | *"Tabnine doesn't retain any user code beyond the immediate time frame required for inferencing"*; operational metrics **one week** | Deployment mode is the lever: SaaS / VPC / on-premises / air-gapped |

**How to read this table.** Two columns matter more than the training column: *what is retained* and
*who holds the off switch*. On the first, every no-training vendor still retains something under some
condition. On the second, three products put the control in the individual developer's hands where an
organisation would expect an admin control — GitHub Copilot Free/Pro/Pro+, Amazon Q Developer Free
tier telemetry, and Cursor Privacy Mode outside Enterprise.

---

## 2. Where the terms are narrower than the marketing

The brief asked for the gap. It exists in five recurring shapes. In each case the marketing sentence
and the terms sentence are quoted side by side.

### 2.1 "We don't train on your code" versus "we retain flagged content for years"

**Anthropic.** The Commercial Terms are absolute on training: *"Anthropic may not train models on
Customer Content from Services"*, alongside *"Anthropic agrees that Customer (a) retains all rights
to its Inputs, and (b) owns its Outputs"* (Commercial Terms, effective **17 June 2025**;
[anthropic.com/legal/commercial-terms](https://www.anthropic.com/legal/commercial-terms);
*tier: binding terms*). The retention documentation is where the qualification lives:

> *"we automatically delete inputs and outputs on our backend within 30 days of receipt or
> generation"* … *"We retain inputs and outputs for up to 2 years and trust and safety classification
> scores for up to 7 years if your chat is flagged"*
> ([privacy.claude.com, read 2026-08-30](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data);
> *tier: vendor documentation*)

The same carve-out is written into the ZDR product itself, so it survives the strongest contractual
control the vendor sells: *"Even with ZDR enabled, Anthropic may retain data where required by law or
to address Usage Policy violations. If a session is flagged for a policy violation, Anthropic may
retain the associated inputs and outputs for up to 2 years"*
([code.claude.com/docs/en/zero-data-retention](https://code.claude.com/docs/en/zero-data-retention);
*tier: vendor documentation*). The API page carries the same sentence for the API arrangement:
*"Even with ZDR or HIPAA arrangements in place, Anthropic may retain data where required by law or
where it has been flagged by Anthropic's automated trust and safety systems."*

**Reading.** These are consistent statements, not a contradiction: training and retention are
different rights. But a team that reads only "Anthropic may not train models on Customer Content"
has not learned that a flagged session can sit in a vendor's systems for two years, with a
classification score for seven.

### 2.2 "No training" versus "a human may read it"

**Microsoft Foundry / Azure OpenAI** is the most explicit primary text found anywhere on human
review, and it is worth quoting at length because it is the counterexample to the industry's usual
vagueness (doc dated **2026-05-18**, change-log entry 3 October 2025;
[learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy);
*tier: vendor documentation*):

> *"Your prompts (inputs) and completions (outputs), your embeddings, and your training data: are NOT
> available to other customers… are NOT used by providers of Models sold by Azure to improve their
> models or services… are NOT used to train any generative AI foundation models without your
> permission or instruction."*

and, in the same document:

> *"When these indicators are detected, a sample of customer's prompts and completions may be selected
> for review. Review is conducted by automated means including by AI models such as LLMs by default,
> with additional reviews by human reviewers as necessary."*
>
> *"Human reviewers assessing potential abuse can access prompts and completions data only when that
> data has already been flagged by the abuse monitoring system, or when the prompts and completions
> are part of a potentially abusive pattern of use. The human reviewers are authorized Microsoft
> employees who access the data via point wise queries using request IDs, Secure Access Workstations
> (SAWs), and Just-In-Time (JIT) request approval granted by team managers. For Models sold by Azure
> deployed in the European Economic Area, the authorized Microsoft employees are located in the
> European Economic Area."*

The escape hatch is an application, not a setting: *"If the customer has been approved for modified
abuse monitoring… the data storage and human review process described above is not performed."*
Microsoft also documents how to verify it — a `ContentLogging` capability set to `false` in the
resource's JSON view — and notes the property *"appears only if data storage for abuse monitoring is
turned off."*

**AWS Bedrock** makes the same trade explicit at the point of model selection:
*"In order to use Claude Fable 5, as required by Anthropic, you must opt in to sharing retained
traffic with Anthropic for abuse detection and potential human review"*
([abuse-detection, read 2026-08-30](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html);
*tier: vendor documentation*). It also documents an unconditional CSAM path: Bedrock
*"may store and review the flagged input or output exclusively to determine if it is CSAM and may
also file a report with the National Center for Missing and Exploited Children (NCMEC)"*.

**Cursor** then relays it to its own customers, which is the clearest example in this research of a
retention obligation travelling down a supply chain: *"Anthropic stores its inputs and outputs to run
automatic and human harm-prevention reviews"*, and enterprise customers must explicitly approve such
models before team use
([cursor.com/docs/enterprise/privacy-and-data-governance](https://cursor.com/docs/enterprise/privacy-and-data-governance);
*tier: vendor documentation*).

### 2.3 The GitHub inversion: marketing narrower than the terms

This is the one case in this research where the **terms are broader than the marketing**, which is
the more dangerous direction.

The binding document is short and reassuring:

> *"GitHub will not use Inputs or Outputs to train generative AI models, unless you have given us
> documented instructions to do so."* — GitHub Generative AI Services Terms, version dated
> **March 2026**, replacing prior terms effective before **5 March 2026**
> ([github.com/customer-terms/github-generative-ai-services-terms](https://github.com/customer-terms/github-generative-ai-services-terms);
> *tier: binding terms*)

The superseded GitHub Copilot Product Specific Terms — *"These terms have been deprecated effective
5 March 2026"* — carried the retention commitment that is most often quoted in the wild:

> *"Prompts are transmitted only to generate Suggestions in real-time, are deleted once Suggestions
> are generated"* (§6.A), with retention in three named cases only: CLI and external tools, private
> language model customization requests, and user-configured alternative data handling with
> third-party extensions. Those terms applied to Copilot Business and Copilot Enterprise; for
> Copilot Individual, *"your use of GitHub Copilot is instead governed by the GitHub Terms of
> Service"*
> ([github.com/customer-terms/github-copilot-product-specific-terms](https://github.com/customer-terms/github-copilot-product-specific-terms);
> *tier: binding terms, deprecated*)

**The replacement terms do not carry that retention sentence forward.** They say instead:
*"Details on data retention are provided in the product documentation for each Generative AI
Service."* Retention moved from a contract that changes with notice into documentation that changes
without it.

Meanwhile the Privacy Statement effective **27 April 2026** reads broadly and, on the reading
performed here, **contains no user-facing opt-out procedure for AI training** — the opt-out is
documented in the Copilot settings UI and in the community announcement, not in the privacy
statement itself
([docs.github.com, read 2026-08-30](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement);
*tier: binding terms*).

The announcement that ties it together is a **GitHub Community Admin post dated 2026-03-02**
(*tier: vendor announcement* — first-party but not a contract):

> *"The change goes into effect on April 24."* Free/Pro/Pro+ individual users are in scope, opt-out;
> Business/Enterprise explicitly excluded; students and teachers with free access unaffected;
> the feature defaults to enabled for those in scope, with prior disablers' preferences retained.
> Opt out at **Settings > Copilot > Features**
> ([github.com/orgs/community/discussions/188488](https://github.com/orgs/community/discussions/188488))

**Contrarian note, recorded not filtered.** The strongest reading against alarm is that GitHub gave
30 days' notice, kept an opt-out, honoured prior preferences, and excluded the plans that
organisations actually buy. The strongest reading for alarm is that the default flipped on a *paid*
plan, that the privacy statement does not name the opt-out, and that the professional developer most
likely to be affected is the individual contractor working on a client's private code under a
personal subscription. Both readings sit on the same primary sources.

### 2.4 "Zero data retention" that is a mode, a negotiation, or a subset

The phrase does not mean one thing.

- **AWS Bedrock**: a genuine *default*. *"Amazon Bedrock uses a zero operator access (ZOA) data
  security model. This means no operators of the service can access model input or output. Also,
  Amazon Bedrock uses a zero data retention (ZDR) data security model. This means that by default,
  Amazon Bedrock does not store model inputs or outputs"*
  ([data-protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html)).
  Configurable per account or project by API — `none`, `default`, `provider_data_share`, `inherit` —
  and enforceable organisation-wide with an SCP denying any mode other than `none`
  ([data-retention](https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html)).
  AWS also warns that the adjacent-looking control is not the same thing: *"Setting `store=false`
  does not guarantee zero data retention. Some models may still retain data for safety review even
  when `store=false`."*
- **OpenAI**: a subset of endpoints, by approval. Eligible: chat completions, responses, images,
  embeddings, audio transcriptions/translations/speech, completions, moderations, realtime.
  Ineligible: Assistants API, conversations, threads, vector stores and others.
  *"Currently, these controls are subject to prior approval by OpenAI"*
  ([developers.openai.com/api/docs/guides/your-data](https://developers.openai.com/api/docs/guides/your-data)).
- **Anthropic**: per-organisation, account-team enabled, and it *disables features*. Claude Code on
  the web, Desktop cloud sessions, Claude Tag, Artifacts, feedback submission and Remote Control are
  *"blocked in the backend regardless of client-side display"* under ZDR. Third-party integrations
  and MCP servers are outside it entirely. Metrics logging is *"exempted from ZDR"*, and ZDR
  *"does not automatically apply to new organizations created under the same account"*
  ([zero-data-retention](https://code.claude.com/docs/en/zero-data-retention)).
- **Cognition**: attached to the training opt-out — *"Zero Data Retention will be enabled with our
  model providers"* — i.e. ZDR **downstream**, at the model vendors, while Cognition separately
  retains *"for the duration of the relationship with a given Customer"*
  ([docs.devin.ai/admin/security](https://docs.devin.ai/admin/security.md)).
- **Tabnine**: a property of the architecture rather than a contract term — *"Tabnine NEVER retains
  or shares any of your code with third parties"*, *"no code is stored on our servers. The code is
  only ephemerally processed… and then immediately discarded"*
  ([docs.tabnine.com privacy](https://docs.tabnine.com/main/welcome/readme/privacy.md),
  [security](https://docs.tabnine.com/main/welcome/readme/security.md)).

**The distinction that matters operationally:** ZDR at Bedrock is a switch you can enforce; ZDR at
Anthropic and OpenAI is an entitlement you must be granted, and at Anthropic it costs you the
cloud-agent product line.

### 2.5 Subprocessors and the honest limit of a single-vendor review

Cursor's security page is candid that the chain does not stop at Cursor: *"Our list of subprocessors
is published on our trust portal. Each subprocessor is evaluated under our vendor risk management
program and re-reviewed annually"*, and *"When you use AI features, Cursor sends prompts and code
context to model providers like OpenAI, Anthropic, and Google"*
([cursor.com/security, page last updated **2026-08-25**](https://cursor.com/security);
[cursor.com/help/security-and-privacy/privacy](https://cursor.com/help/security-and-privacy/privacy);
*tier: vendor documentation*).

GitHub publishes the equivalent for Copilot as a model-hosting page — the most complete
subprocessor-shaped disclosure found in this research
([docs.github.com/en/copilot/reference/ai-models/model-hosting](https://docs.github.com/en/copilot/reference/ai-models/model-hosting);
*tier: vendor documentation*): OpenAI models *"hosted by OpenAI and GitHub's Azure infrastructure"*
with *"a zero data retention agreement with OpenAI"*; Anthropic models *"hosted by Amazon Web
Services, Anthropic PBC, and Google Cloud Platform"*, with ZDR *"for generally available Anthropic
features"*; Google models on GCP, where Gemini *"doesn't use your prompts, or its responses, as data
to train its models"*; xAI content *"only… Exist temporarily in RAM"*; Moonshot AI models
*"covered by zero data retention agreements with the hosting providers"* and *"prompts and
completions are not sent to Moonshot AI."*

**Note the qualifier.** "Zero data retention agreement with Anthropic **for generally available
Anthropic features**" is narrower than "zero data retention with Anthropic". Preview features are
not covered by that sentence.

**Blocked:** Anthropic's public subprocessor list was not retrievable at
`anthropic.com/legal/subprocessors` (HTTP 404), and `trust.anthropic.com` returned a title-only
shell. Recorded, not circumvented.

---

## 3. Zero-data-retention and enterprise controls: what exists, on what plan, self-serve or not

| Control | Provider | Plan | Self-serve or negotiated | Documented exclusions |
|---|---|---|---|---|
| ZDR | **Anthropic** (Claude Code on Claude for Enterprise) | Enterprise, *qualified accounts* | **Negotiated** — *"cannot be enabled from your admin settings"*; account team enables per organisation; *"All enablement actions are audit-logged"* | claude.ai chat, Cowork, analytics metadata, seat management, third-party integrations/MCP. Disables Claude Code on the web, Desktop cloud sessions, Claude Tag, Artifacts, `/feedback`, Remote Control. Covered Models (Fable 5, Mythos 5) unavailable. Flagged content retained up to 2 years |
| ZDR | **Anthropic API** | Commercial org via API keys | Negotiated | Feature-by-feature eligibility table; "No" for Agent Skills, code execution (containers up to 30 days), Files API, MCP connector, Batch. Metrics logging exempt |
| ZDR | **OpenAI API** | Any, by approval | **Negotiated** — *"subject to prior approval by OpenAI"* | Assistants API, conversations, threads, vector stores and others ineligible |
| ZDR / ZOA | **AWS Bedrock** | All, by default | **Self-serve** (API/SDK; *"At launch, there is no console UI for configuring data retention"*), SCP-enforceable | Models that require retention; flagged GPT-5.x traffic 30 days; Fable 5/Mythos 5 require `provider_data_share`. ZDR for those is per-account, per-model, via the account manager |
| Modified abuse monitoring (no storage, no human review) | **Microsoft Foundry / Azure OpenAI** | "Managed customers" | **Application form**, then verifiable via `ContentLogging: false` | Automated review still runs; severe/recurring abuse can still throttle or suspend |
| Privacy Mode | **Cursor** | Free and Pro (manual), **Enterprise (default on, enforceable)** | Self-serve for the individual; admin enforcement is an Enterprise dashboard setting plus MDM to block personal accounts | Not supported in its legacy form for Cloud Agents; retention-requiring models require explicit enterprise approval |
| US-only data residency | **Cursor** | **Enterprise only** | Negotiated (*"Pricing varies depending on the enrollment"*) | *"supported models and features"*, with unstated exclusions |
| Training opt-out + downstream ZDR | **Cognition (Devin/Windsurf)** | Paid plans; enterprise requires express written consent for any training | Self-serve opt-out documented; enterprise deployment negotiated | ZDR is *"with our model providers"*; Cognition's own retention is relationship-duration |
| Customer-managed keys | **Cognition** | *Enterprise Assured Deployment* | Negotiated via account team | Adds CMK on top of dedicated single-tenant VPC |
| EEA-only storage for detailed code data | **JetBrains** | Applies to the collected category | Consent-gated, not a purchasable control | 1-year retention |
| On-prem / air-gapped | **Tabnine** | Enterprise private installation | Negotiated deployment | SaaS datacentres named (AWS/GCP, North Virginia and Council Bluffs) for the hosted mode |
| Self-hosted execution | **Anthropic** (self-hosted environments) | **Public beta**, Team and Enterprise, off by default | Admin toggle, then you operate the runner fleet | **Unavailable for ZDR organisations.** Inference cannot route via Bedrock, Google Cloud's Agent Platform, Microsoft Foundry or an LLM gateway. Claude Security and Code Review sessions do not route to it yet |

**Two structural observations.**

First, **the strongest retention control and the most autonomous product are mutually exclusive at
Anthropic**: ZDR blocks Claude Code on the web, and self-hosted environments are *"unavailable for
organizations with Zero Data Retention enabled"*. An organisation cannot currently have both maximum
containment of data and cloud-executed agents from this vendor.

Second, **Bedrock is the only provider found where zero retention is the default rather than an
entitlement** — and it is also the only one that lets a security team enforce it as policy code
(a `bedrock-mantle:DataRetentionMode` condition key in an SCP). For a regulated team, that is a
materially different governance posture from a negotiated ZDR letter.

---

## 4. What is technically transmitted, not just what is promised

Ticket #6 established that `.gitignore`-style exclusion is weak. This strand does not re-derive it;
it adds the second vendor confirmation and then documents what the tools say they *do* send.

### 4.1 Exclusion mechanisms and their documented limits

| Mechanism | What it blocks | What it does not block — vendor's own words |
|---|---|---|
| **GitHub Copilot content exclusion** | Inline suggestions in excluded files | *"Content exclusion is currently not supported in Edit and Agent modes of Copilot Chat in Visual Studio Code and other editors."* · *"Currently, content exclusions do not apply to symbolic links (symlinks) and repositories located on remote filesystems."* · *"It's possible that Copilot may use semantic information from an excluded file if the information is provided by the IDE indirectly."* ([docs.github.com, read 2026-08-30](https://docs.github.com/en/copilot/concepts/content-exclusion)) |
| **Cursor `.cursorignore`** | *"Code accessible by Agent, Tab, and Inline Edit"* and `@` mention references | *"The terminal and MCP server tools used by Agent cannot block access to code governed by .cursorignore."* · *"While Cursor blocks ignored files, complete protection isn't guaranteed due to LLM unpredictability."* · negation patterns cannot re-include from an excluded parent directory ([cursor.com, read 2026-08-30](https://cursor.com/docs/reference/ignore-file)) |
| **Kilo Code `.env` prompt** | A prompt on `.env` / `.env.*` reads | The agent can still reach the environment by other means — established in [research/tooling-agentic-ide.md](./tooling-agentic-ide.md) |

**The synthesis across tickets #6 and #7:** every shipped file-exclusion mechanism is an
*editor-context* filter. None of them is a boundary at the shell, and two vendors say so in their own
documentation. A team whose data-governance answer is "we added it to the ignore file" has protected
the least-delegated surface only. Containment that survives the agent's shell has to be enforced
below the assistant — filesystem permissions, a sandbox, a separate checkout — not by a list the
assistant is asked to respect.

### 4.2 What the agent products document sending

**Anthropic — Claude Code, local.** *"This data includes all user prompts and model outputs,
encrypted in transit via TLS 1.2+."* Telemetry is separated and bounded: *"Metrics never include your
code, prompts, or file paths"*; error reports redact *"known patterns of secrets, file paths, email
addresses, and other personal information before anything leaves your machine."* `/feedback`, `/bug`
and `/share` send *"a copy of your conversation history including code"*, stored in Google Cloud
Storage, retained **5 years**, optionally opening a public GitHub issue. Session-quality survey
transcript sharing uploads *"your conversation transcript, any subagent transcripts, and the raw
session log file from disk"* with *"Known API key and token patterns… redacted before upload"* while
*"Source code, file contents, and other conversation content are uploaded as-is"* — retained up to
**6 months**, and explicitly not used for training
([data-usage, read 2026-08-30](https://code.claude.com/docs/en/data-usage); *tier: vendor documentation*).
Local session transcripts sit on disk *"in plaintext under `~/.claude/projects/` for 30 days by
default"*.

**Anthropic — Claude Code on the web (cloud).** *"Your repository is cloned to an isolated VM"*;
*"GitHub authentication is handled through a secure proxy; your GitHub credentials never enter the
sandbox"*; *"All outbound traffic goes through a security proxy for audit logging and abuse
prevention."* For non-GitHub repositories the local bundle includes *"your full repository history
across all branches, plus uncommitted changes to tracked files"*, with the OS-scoped credential
exclusion quoted in headline finding 7. Untracked files are not included.

**OpenAI — Codex.** Local session history is stored on the machine under `CODEX_HOME`; the docs point
at *"local data retention settings (for example, `history.persistence` / `history.max_bytes`) if you
don't want Codex to save session transcripts."* Opt-in OpenTelemetry export covers *"chats, API
requests, SSE/WebSocket stream activity, user prompts (redacted by default), tool approval decisions,
and tool results."* Default sandbox is `workspace-write` with approval policy `on-request`, and
*"By default, the agent runs with network access turned off."* Cloud secrets *"are available only
during setup and are removed before the agent phase starts"*
([learn.chatgpt.com agent approvals & security](https://learn.chatgpt.com/docs/agent-approvals-security.md),
[sandboxing](https://learn.chatgpt.com/docs/sandboxing.md); *tier: vendor documentation*).

**Cursor.** Indexing: *"File paths are encrypted before being sent to Cursor's servers. Code content
is never stored in plaintext"*
([codebase-indexing, read 2026-08-30](https://cursor.com/docs/context/codebase-indexing)). Cloud
Agents: Cursor's backend holds *"prompts, model responses, tool calls, diff context, and demo
artifacts"*, the VM holds *"the checked-out repository, build artifacts, and tool-execution
context"*, and *"Encrypted copies of repositories that Cloud Agents work on [are] Stored temporarily
while the agent runs [and] Deleted after the agent completes."* Secrets are *"encrypted at rest with
KMS, encrypted in transit, and injected as environment variables at runtime"*, with Runtime Secrets
*"kept out of the transcript, tool output, and commits"*
([cloud-agent/security](https://cursor.com/docs/cloud-agent/security),
[enterprise/privacy-and-data-governance](https://cursor.com/docs/enterprise/privacy-and-data-governance)).

**JetBrains.** *"AI Assistant needs to send your requests and pieces of your code to the LLM
provider"*, plus context such as *"file types, frameworks used"*. Users can audit what was sent via
an `ai-assistant-requests.md` log
([how-we-handle-your-code-and-data, read 2026-08-30](https://www.jetbrains.com/help/ai-assistant/how-we-handle-your-code-and-data.html)).

**Tabnine.** *"No code or PII data is ever sent to Tabnine's servers"* in the self-hosted cluster
telemetry path; operational metrics (GPU/CPU utilisation, latency, throughput, IDE type, aggregated
language statistics) retained **one week**.

### 4.3 The lethal trifecta, in the vendors' own words

The trifecta is not hypothetical in this material; all three of its legs are documented as product
behaviour.

- **Private data access.** Repository clone into the agent VM (Anthropic, Cursor, Copilot cloud
  agent); index and embeddings (Cursor); secrets injected as environment variables (Cursor).
- **Untrusted content.** GitHub documents the exposure and its partial mitigation: the agent
  *"filters hidden characters that might allow users to hide harmful instructions in comments or
  issue contents"*
  ([docs.github.com/en/copilot/responsible-use/agents](https://docs.github.com/en/copilot/responsible-use/agents)).
  Cursor: *"AI can behave unexpectedly due to prompt injection, hallucinations, and other issues."*
- **External communication.** Default-deny egress is now near-universal (Copilot cloud agent firewall
  on by default; Codex network off by default; Anthropic Trusted allowlist) — **and the inference
  channel is the documented residue**: *"When running with network access disabled, Claude Code can
  still communicate with the Anthropic API, which may allow data to exit the VM."*

**The governance consequence.** Egress containment reduces the number of exfiltration paths; it does
not close the one that must stay open. For a team whose concern is *data leaving the building*, the
inference channel is not a leak to be plugged — it is the product. The controls that actually bear
weight are therefore retention and training terms at the far end, not network policy at the near end.

---

## 5. Regulated and air-gapped environments: what is real, what is announced

| Option | Status as of 2026-08-30 | Source and date |
|---|---|---|
| **Tabnine SaaS / VPC / on-premises / air-gapped** | Documented as offered; SOC 2 and GDPR compliance claimed; *"Tabnine Enterprise customers [deploy] Tabnine in a private installation to comply with the strictest enterprise security and privacy policies"* | [docs.tabnine.com privacy](https://docs.tabnine.com/main/welcome/readme/privacy.md) / [security](https://docs.tabnine.com/main/welcome/readme/security.md), read 2026-08-30 |
| **JetBrains Full Line code completion (local model)** | Shipped. *"Full Line code completion runs entirely on your local device without sending any code over the internet"*; models bundled for Java/Kotlin, downloadable for others. **Completion only** — not chat, not an agent | [jetbrains.com](https://www.jetbrains.com/help/idea/full-line-code-completion.html), read 2026-08-30 |
| **JetBrains EEA data storage** | For detailed code-related data: *"The collected data remains stored within the European Economic Area (EEA)"*, 1-year retention, policy **v1.6, 2026-07-07** | [jetbrains.com/help/ai](https://www.jetbrains.com/help/ai/data-collection-and-use-policy.html) |
| **Cognition — FedRAMP High, IL4/IL5, ITAR** | **Partial.** Authorised today: **Devin CLI and Devin Desktop** (FedRAMP High, IL4/IL5, ITAR). **Devin itself and Devin Review are *"slated for FedRAMP High authorization in 2026"*, and "In Process" for IL and ITAR.** *"Zero Data Retention (ZDR) is enabled for all Devin Desktop and Devin CLI features in federal deployments."* Approved model list *"last updated on 25 AUG 26"* | [docs.devin.ai/federal/compliance](https://docs.devin.ai/federal/compliance.md), read 2026-08-30 |
| **Cognition — dedicated / private deployment** | Two models generally available: Enterprise Cloud (multi-tenant) and Customer Dedicated Deployment (*"an auto-scaling, customer-isolated environment within a single-tenant VPC"*, AWS PrivateLink or IPSec). *Enterprise Assured Deployment* adds customer-managed keys, on request. **No on-premises option documented** | [docs.devin.ai/enterprise/deployment/overview](https://docs.devin.ai/enterprise/deployment/overview.md) |
| **Anthropic self-hosted environments** | **Public beta**, Team and Enterprise, off by default. *"Repository checkouts, build artifacts, secrets, and any files a session creates or modifies stay on the machines you provision. The conversation itself, including prompts, responses, and tool results, goes to `api.anthropic.com` for model inference"*. **Unavailable to ZDR organisations.** Inference cannot be routed via Bedrock, Google Cloud's Agent Platform, Microsoft Foundry or an LLM gateway. *"Anthropic never connects into your network"* — all traffic is outbound | [code.claude.com/docs/en/self-hosted-environments](https://code.claude.com/docs/en/self-hosted-environments), read 2026-08-30 |
| **BYOK / private-cloud model access — Bedrock** | Generally available. Deep-copied model weights in per-provider deployment accounts; *"Because the model providers don't have access to those accounts, they don't have access to Amazon Bedrock logs or to customer prompts and completions."* VPC/PrivateLink, KMS and FIPS 140-3 endpoints documented | [data-protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) |
| **BYOK / private-cloud — Microsoft Foundry** | Generally available. *"Microsoft hosts the Models sold by Azure in Microsoft's Azure environment and Models sold by Azure do NOT interact with any services operated by providers of Models sold by Azure, for example, OpenAI (e.g. ChatGPT, or the OpenAI API)."* Standard deployments process within the customer geography; **Global and DataZone deployment types process outside it** — data *at rest* stays in the designated geography | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy), doc dated 2026-05-18 |
| **Anthropic on Microsoft Foundry** | Documented, with a split posture: *"For Hosted on Azure deployments, prompts and completions remain within Azure; only usage metadata and content flagged by Anthropic's safety systems egress to Anthropic. For Hosted on Anthropic deployments, requests route to Anthropic infrastructure with AES-256 disk encryption."* | [code.claude.com/docs/en/data-usage](https://code.claude.com/docs/en/data-usage) |
| **Claude Code default telemetry on third-party platforms** | Error reporting, telemetry and `/feedback` are **off by default** on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry and Claude Platform on AWS. Session-quality surveys and the WebFetch domain safety check run **regardless of provider** | [code.claude.com/docs/en/data-usage](https://code.claude.com/docs/en/data-usage) |
| **Cursor US-only data residency** | Enterprise only; *"Enterprise customers can enroll in US-only data residency so inference, processing, and storage for supported features stay in the US"*, with unstated exclusions and variable pricing | [cursor.com/help/security-and-privacy/regions](https://cursor.com/help/security-and-privacy/regions) |
| **Continue / Ollama-backed local setups** | **Not established.** The Continue telemetry doc URL redirected to a shell page; no primary text retrieved | see Blocked sources |

**The honest summary for an air-gapped team.** Two things are genuinely local: a completion model
running on the developer's machine (JetBrains Full Line), and a vendor's inference stack installed
inside the customer's network (Tabnine's private installation). Everything else labelled
"self-hosted" in this space self-hosts *execution* and still ships the conversation to a vendor API.
The Anthropic documentation says this plainly, which is to its credit, and it is the sentence most
likely to be skimmed past: *"Session content still goes to `api.anthropic.com` for model
inference."*

**One caution about the WebFetch preflight.** Claude Code sends the hostname of every URL the
WebFetch tool is asked to retrieve to `api.anthropic.com` for a blocklist check, *"regardless of
which model provider you use"*, and it is *"not affected by `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`"*.
Only the hostname, not the path or page contents — but for a genuinely air-gapped or
egress-restricted network this is a documented call home that must be either allowlisted or disabled
with `skipWebFetchPreflight`.

---

## 6. GDPR and cross-border

Code contains personal data more often than teams assume: test fixtures with real names and emails,
log samples, comments, commit metadata, seeded databases. Where it does, transferring it to a model
vendor is a restricted transfer, and the GDPR machinery applies.

### 6.1 Roles

The vendors position themselves as **processors** for inference, and the primary texts say so
directly where they say anything at all:

- **Anthropic**: *"This page covers the Claude API (`api.anthropic.com`), Claude Platform on AWS, and
  Claude in Microsoft Foundry, where Anthropic is the data processor. On Amazon Bedrock and Google
  Cloud's Agent Platform, the cloud provider is the data processor"*
  ([platform.claude.com, read 2026-08-30](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention);
  *tier: vendor documentation*). **The processor identity changes with the deployment route** — a
  fact that is easy to miss and directly determines who signs what.
- **Microsoft**: *"Please also see Microsoft Products and Services Data Protection Addendum
  (https://aka.ms/DPA), which governs data processing by Models sold by Azure"*
  (*tier: vendor documentation* pointing at *binding terms*).
- **Google**: *"Google Cloud handles your prompts in accordance with our terms of service and Cloud
  Data Processing Addendum"*
  ([docs.cloud.google.com, updated 2026-08-27](https://docs.cloud.google.com/gemini/docs/discover/data-governance)).

**Art. 28 GDPR** requires the processing terms — subject matter, duration, nature and purpose,
categories of data and data subjects, confidentiality, security, sub-processor authorisation, audit
and deletion or return on termination — to be in a contract. Each of the DPAs above is the instrument
meant to carry them. **I could not retrieve OpenAI's DPA text** (openai.com returned HTTP 403; see
Blocked sources), so no verbatim Art. 28 comparison is offered here.

### 6.2 Transfer mechanism: the EU-US Data Privacy Framework

- **The adequacy decision.** Commission Implementing Decision **(EU) 2023/1795 of 10 July 2023**,
  OJ L 231, 20.9.2023, pp. 118–229. The EUR-Lex legal-status field read **"In force"** on
  2026-08-30. The decision's finding is that *"the United States ensures an adequate level of
  protection for personal data transferred under the EU-U.S. DPF"*
  ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023D1795);
  *tier: regulatory primary text*).
- **The challenge, first instance.** **T-553/23 Latombe v Commission**, General Court (Tenth Chamber,
  Extended Composition), judgment **3 September 2025**, ECLI:EU:T:2025:831 — **action dismissed**,
  all five pleas rejected as unfounded, the Court confirming that at the date of adoption the United
  States ensured an adequate level of protection. The applicant's pleas included that the Data
  Protection Review Court *"is neither impartial nor independent, but dependent on the executive"*
  and that US bulk collection *"is not circumscribed in a sufficiently clear and precise manner"*
  ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:62023TJ0553);
  *tier: court record*).
- **The appeal.** ⚠️ **Appeal brought 31 October 2025, Case C-703/25 P**, against the T-553/23
  judgment
  ([OJ notice](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202506610);
  *tier: court record*). **No judgment or Advocate General's opinion on the appeal was found as of
  2026-08-30.**

**How to state this.** "The EU-US DPF adequacy decision is in force as of 2026-08-30; the General
Court dismissed the first challenge on 3 September 2025 and an appeal (C-703/25 P) is pending." Not
"the DPF has been upheld", and not "the DPF is about to fall". A pending appeal is neither.

**Practical consequence, recorded without a recommendation:** teams that hold Standard Contractual
Clauses (Commission Implementing Decision (EU) 2021/914) alongside DPF certification have a second
mechanism if adequacy changes; teams relying on DPF alone do not. Whether that redundancy is worth
its cost is a decision for counsel, not for this document.

### 6.3 The EDPB on AI models

**Opinion 28/2024, adopted 18 December 2024** (*tier: regulatory primary text*, read via the EDPB's
own summary page — the PDF returned as unparseable binary, so the quotations below are from the
EDPB's published summary rather than the numbered opinion text, and are labelled accordingly):

- **Anonymity is case-by-case, and the bar is high.** *"It should be very unlikely (1) to directly or
  indirectly identify individuals whose"* data was used, and *"(2) to extract such personal data from
  the model."*
- **Legitimate interest can work, conditionally.** Services such as conversational agents can rely on
  legitimate interest *"but only if the processing is shown to be strictly necessary and the
  balancing of rights is respected."*
- **Unlawful upstream processing contaminates downstream deployment.** *"When an AI model was
  developed with unlawfully processed personal data, this could have an impact on the lawfulness of
  its deployment, unless the model has been duly anonymised."*
  ([edpb.europa.eu](https://www.edpb.europa.eu/news/news/2024/edpb-opinion-ai-models-gdpr-principles-support-responsible-ai_en))

**Why this matters to this strand specifically.** The third conclusion connects provenance to data
governance: a team's exposure is not only about what its own code discloses, but about the lawfulness
of the training corpus behind the model it is sending that code to. That is a supplier-diligence
question, and it is not answerable from any vendor page read in this research.

---

## 7. The autonomy axis: does exposure widen as delegation increases?

**Yes — measurably, in product documentation. No — in the contracts, which say nothing about it.**

### 7.1 What changes as you move further along the spectrum

| Surface | What leaves the building | Primary source |
|---|---|---|
| **Inline completion** | The prompt context the IDE assembles. Copilot content exclusion applies here — and only here | GitHub content-exclusion docs |
| **Chat / edit modes** | Prompt plus attached and retrieved context. **Copilot content exclusion stops working**: *"not supported in Edit and Agent modes"* | GitHub content-exclusion docs |
| **Local agent** | Prompts, model outputs, tool results, terminal output the agent reads back. `.cursorignore` no longer binds the shell. Local transcripts persist on disk (Claude Code: `~/.claude/projects/`, plaintext, 30 days by default; Codex: `CODEX_HOME`) | Cursor ignore-file docs; Anthropic data-usage; Codex security docs |
| **Cloud / background agent** | **The repository itself.** Cursor: *"agents need to store code and environment data in the cloud while they run"*. Anthropic: *"Your repository is cloned to an isolated VM"* — or, for non-GitHub repos, a bundle of *"full repository history across all branches, plus uncommitted changes to tracked files"* | Cursor cloud-agent security; Anthropic web docs |
| **Scheduled / triggered automation** | The same as above, unattended, repeatedly, on content the agent did not choose — CI output, PR comments, issue text. Anthropic warns that auto-fix replies *"are posted using your GitHub account"* and can trigger comment-driven automation such as Atlantis or Terraform Cloud | Anthropic Claude Code on the web |

### 7.2 Repository access scope, product by product

This is where the products differ most, and it is the sharpest practical distinction found.

- **GitHub Copilot cloud agent — narrow.** *"The cloud agent only has access to the repository where
  it is creating a pull request and cannot access other repositories."* It *"does not have access to
  Actions organization or repository secrets—only secrets and variables specifically added to the
  `copilot` environment are passed to the agent"*, and *"By default, the cloud agent has a firewall
  enabled to prevent exfiltration of code or other sensitive data, either accidentally or due to
  malicious user input"*
  ([docs.github.com/en/copilot/responsible-use/agents](https://docs.github.com/en/copilot/responsible-use/agents);
  *tier: vendor documentation*).
- **Cursor Cloud Agents — user-scoped.** *"A Cloud Agent can only reach repositories the triggering
  user could already reach. Starting an agent never grants access to a repository the user didn't
  already have."*
- **Claude Code on the web — account-scoped, and the vendor says so in a Note.** ⚠️ *"With either
  method, a cloud session can access any repository the connecting GitHub account can see, not just
  the repositories the Claude GitHub App is installed on. App installation enables PR webhooks for
  Auto-fix; it is not a session-level access control. To restrict which repositories your team can
  reach from cloud sessions, restrict access on GitHub itself"*
  ([code.claude.com, read 2026-08-30](https://code.claude.com/docs/en/claude-code-on-the-web)).
  This confirms ticket #6's finding verbatim and adds the remedy the vendor names: the control is on
  GitHub, not in the product.

  **A qualification worth recording, because it reads as a tension.** The same vendor's data-usage
  page states: *"Note for remote Claude Code, Claude accesses the repository where you initiate your
  Claude Code session. Claude does not access repositories that you have connected but have not
  started a session in"*
  ([data-usage](https://code.claude.com/docs/en/data-usage)). These are reconcilable — one describes
  the *credential's reach* (what a session could clone), the other the *product's behaviour* (what it
  does clone) — but they are two different claims on two pages, and a reader who sees only the second
  will underestimate the credential's scope. **Recorded as a documentation inconsistency, not as a
  security finding.**

### 7.3 The silence in the contracts

I looked for any clause, in any of the terms read for this strand, that varies training rights,
retention, review or liability according to whether the use was attended or unattended, interactive
or scheduled, human-approved or autonomous. **I found none.**

- Anthropic Commercial Terms: Customer Content is Customer Content, however it was produced.
- GitHub Generative AI Services Terms: Inputs and Outputs, with no autonomy qualifier. The
  responsibility clause runs the other way — *"You are solely responsible for any application or
  agent you create using (or for use with) Generative AI Services, including complying with any
  legal, regulatory, or licensing requirements"* — allocating risk **to** the customer for agentic
  use without granting anything in return.
- AWS service-improvement and retention pages: per-plan and per-model, never per-autonomy.
- Google data-governance: per-product, never per-autonomy.
- Cognition security: per-plan and per-deployment, never per-autonomy.

**This is a finding, not an absence of one.** Every meaningful difference in what leaves the building
as delegation increases lives in documentation the vendor can change without notice, while the
contract — the instrument a procurement process actually reviews — is silent on the distinction. A
team that assesses "is it safe to let this run unattended overnight?" by reading the MSA will find
nothing in the MSA that addresses the question.

---

## Sources

**Binding terms**
- Anthropic Commercial Terms of Service, effective 17 June 2025 — https://www.anthropic.com/legal/commercial-terms (read 2026-08-30)
- GitHub Generative AI Services Terms, version March 2026 — https://github.com/customer-terms/github-generative-ai-services-terms (read 2026-08-30)
- GitHub Copilot Product Specific Terms, **deprecated effective 5 March 2026** — https://github.com/customer-terms/github-copilot-product-specific-terms (read 2026-08-30)
- GitHub General Privacy Statement, effective 27 April 2026 — https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement (read 2026-08-30)

**Vendor documentation — Anthropic**
- Claude Code data usage — https://code.claude.com/docs/en/data-usage (2026-08-30)
- Claude Code zero data retention — https://code.claude.com/docs/en/zero-data-retention (2026-08-30)
- API and data retention — https://platform.claude.com/docs/en/manage-claude/api-and-data-retention (2026-08-30)
- Commercial data retention policy — https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data (2026-08-30)
- Claude Code on the web — https://code.claude.com/docs/en/claude-code-on-the-web (2026-08-30)
- Self-hosted environments — https://code.claude.com/docs/en/self-hosted-environments (2026-08-30)

**Vendor documentation — GitHub / Microsoft**
- Copilot content exclusion — https://docs.github.com/en/copilot/concepts/content-exclusion (2026-08-30)
- Hosting of models for GitHub Copilot — https://docs.github.com/en/copilot/reference/ai-models/model-hosting (2026-08-30)
- Responsible use of Copilot agents — https://docs.github.com/en/copilot/responsible-use/agents (2026-08-30)
- Data, privacy and security for Foundry Models sold by Azure — https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/openai/data-privacy (doc dated 2026-05-18; read 2026-08-30)

**Vendor announcement**
- GitHub Community Admin, "FAQ: Privacy Statement update on Copilot data use for model training (Free/Pro/Pro+)", posted 2026-03-02 — https://github.com/orgs/community/discussions/188488 (read 2026-08-30)

**Vendor documentation — OpenAI**
- Your data (API) — https://developers.openai.com/api/docs/guides/your-data (2026-08-30; reached via 301 from platform.openai.com)
- ChatGPT Work cloud security — https://learn.chatgpt.com/docs/enterprise/chatgpt-work-cloud-security.md (2026-08-30)
- ChatGPT Work admin FAQ — https://learn.chatgpt.com/docs/enterprise/work-admin-faq.md (2026-08-30)
- Agent approvals and security — https://learn.chatgpt.com/docs/agent-approvals-security.md (2026-08-30)
- Sandboxing — https://learn.chatgpt.com/docs/sandboxing.md (2026-08-30)

**Vendor documentation — AWS**
- Amazon Q Developer service improvement — https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/service-improvement.html (2026-08-30)
- Opt out of data sharing in the IDE and command line — https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/opt-out-IDE.html (2026-08-30)
- Bedrock data protection — https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html (2026-08-30)
- Bedrock abuse detection — https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html (2026-08-30)
- Bedrock data retention — https://docs.aws.amazon.com/bedrock/latest/userguide/data-retention.html (2026-08-30)

**Vendor documentation — Google**
- How Gemini for Google Cloud uses your data, last updated 2026-08-27 — https://docs.cloud.google.com/gemini/docs/discover/data-governance (read 2026-08-30; reached via 301 from cloud.google.com)
- Gemini Code Assist for individuals — deprecation notice, page dated 2026-06-23 — https://developers.google.com/gemini-code-assist/resources/privacy-notice-gemini-code-assist-individuals (read 2026-08-30)
- Cloud Code and Gemini Code Assist data governance, updated 2026-08-26 — https://docs.cloud.google.com/code/docs/cloud-code-gemini-code-assist-data-governance (read 2026-08-30)
- Gemini Code Assist privacy notices index — https://developers.google.com/gemini-code-assist/resources/privacy-notices (2026-08-30)

**Vendor documentation — Cursor**
- Security, page last updated 2026-08-25 — https://cursor.com/security (read 2026-08-30)
- Privacy Mode — https://cursor.com/help/security-and-privacy/privacy (2026-08-30)
- Enterprise privacy and data governance — https://cursor.com/docs/enterprise/privacy-and-data-governance (2026-08-30)
- Cloud Agent security — https://cursor.com/docs/cloud-agent/security (2026-08-30)
- Ignore files — https://cursor.com/docs/reference/ignore-file (2026-08-30)
- Codebase indexing — https://cursor.com/docs/context/codebase-indexing (2026-08-30)
- Regions / data residency — https://cursor.com/help/security-and-privacy/regions (2026-08-30)
- Agent security — https://cursor.com/docs/agent/security (2026-08-30)

**Vendor documentation — Cognition (Devin / Windsurf)**
- Security — https://docs.devin.ai/admin/security.md (2026-08-30)
- Enterprise security — https://docs.devin.ai/enterprise/security-access/security/enterprise-security.md (2026-08-30)
- Federal compliance — https://docs.devin.ai/federal/compliance.md (2026-08-30)
- Deployment overview — https://docs.devin.ai/enterprise/deployment/overview.md (2026-08-30)

**Vendor documentation — JetBrains and Tabnine**
- JetBrains Product Data Collection and Usage Notice, v1.6, 2026-07-07 — https://www.jetbrains.com/help/ai/data-collection-and-use-policy.html (read 2026-08-30)
- JetBrains AI Assistant data handling — https://www.jetbrains.com/help/ai-assistant/how-we-handle-your-code-and-data.html (2026-08-30)
- JetBrains Full Line code completion — https://www.jetbrains.com/help/idea/full-line-code-completion.html (2026-08-30)
- Tabnine privacy — https://docs.tabnine.com/main/welcome/readme/privacy.md (2026-08-30)
- Tabnine security — https://docs.tabnine.com/main/welcome/readme/security.md (2026-08-30)
- Tabnine Privacy Policy, effective 12 September 2024 — https://www.tabnine.com/privacy-policy/ (read 2026-08-30)

**Regulatory and court primary text**
- Commission Implementing Decision (EU) 2023/1795 of 10 July 2023 (EU-US DPF adequacy), OJ L 231, 20.9.2023 — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023D1795 (status read 2026-08-30: "In force")
- Case T-553/23 *Latombe v Commission*, General Court, judgment 3 September 2025, ECLI:EU:T:2025:831 — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:62023TJ0553
- Appeal C-703/25 P, brought 31 October 2025 — https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:C_202506610
- EDPB Opinion 28/2024, adopted 18 December 2024 (read via the EDPB summary page; PDF unparseable) — https://www.edpb.europa.eu/news/news/2024/edpb-opinion-ai-models-gdpr-principles-support-responsible-ai_en · document record: https://www.edpb.europa.eu/our-work-tools/our-documents/opinion-board-art-64/opinion-282024-certain-data-protection-aspects_en

**Prior tickets in this project, relied on and not re-derived**
- [research/tooling-inline-and-chat.md](./tooling-inline-and-chat.md) — Copilot content exclusion limits
- [research/tooling-agentic-ide.md](./tooling-agentic-ide.md) — Kilo Code `.env` prompt as the entire hard floor
- [research/tooling-background-agents.md](./tooling-background-agents.md) — Claude Code on the web repository scope; Copilot cloud agent constraints; Amazon Q sunset dates

---

## Confidence and gaps

**High confidence.**
- The comparison table's training-default column for GitHub, Anthropic, OpenAI API, AWS, Google,
  Cursor, Cognition, JetBrains and Tabnine. Each rests on a quoted sentence from the vendor's own
  terms or documentation, read on 2026-08-30.
- Anthropic's retention numbers (30 days standard; 2 years flagged; 7 years classification scores;
  5 years feedback; 6 months shared transcripts). Unusually well documented and consistent across
  four Anthropic pages.
- The exclusion-mechanism limits (§4.1). Two vendors state them in their own words.
- The DPF's current status and the pending appeal. Court records and the EUR-Lex status field.
- Bedrock's retention-mode API and SCP enforcement. The documentation includes the condition key and
  a worked policy.

**Medium confidence.**
- **The GitHub training-default change.** The *effective date of 24 April* and the *opt-out location*
  come from a GitHub Community Admin post, not from a terms document. The Privacy Statement effective
  27 April 2026 is consistent with the change and broad enough to cover it, but does not itself name
  the Copilot setting. Two first-party sources pointing the same way; one is not binding.
- **Cursor's Privacy Mode default.** *"Privacy Mode is on by default for Enterprise teams"* is
  documented; the default for a new individual or Pro user is **not** stated on the pages read — the
  security page does not specify whether Privacy Mode is enabled by default for those users.
- **Cognition's retention.** *"for the duration of the relationship with a given Customer"* is an
  unusual formulation and its interaction with the paid-plan ZDR opt-out is not spelled out.

**Low confidence / not established.**
- **OpenAI ChatGPT consumer defaults.** openai.com and help.openai.com returned HTTP 403. The API
  and Business/Enterprise positions are established from primary sources; the consumer position is
  not, and no claim about it should be made from this document.
- **Google's individual/free coding-assistant terms.** Gemini Code Assist for individuals is recorded
  as deprecated (2026-06-18, directing to Antigravity), and no Antigravity data-governance page was
  retrievable. The successor product's terms are unknown.
- **Retention periods for GitHub Copilot Business/Enterprise under the current terms.** The binding
  document defers to product documentation, and the product documentation page carrying retention
  periods was not located.
- **Anthropic's subprocessor list** and the contents of `trust.anthropic.com`.
- **OpenAI's DPA text**, and therefore any verbatim Art. 28 comparison.
- **Continue / Ollama local-agent posture.** No primary text retrieved.

**Ageing risk — high.** Four of the most load-bearing facts here are less than six months old: the
GitHub Copilot Product Specific Terms deprecation (5 March 2026), the GitHub training default (24
April 2026), the GitHub Privacy Statement (27 April 2026), and the Gemini Code Assist individuals
deprecation (18 June 2026). Two documentation hosts moved during this research
(`platform.openai.com` → `developers.openai.com`, `cloud.google.com` → `docs.cloud.google.com`).
Anything built on this document should carry the **2026-08-30** date visibly and be re-verified
before reuse.

**What this research does not cover.** It documents published positions, not observed behaviour. No
traffic was captured, no product was instrumented, and no claim here is that a vendor does or does
not do what it says. Nothing here measures how many teams actually enable any of these controls; that
is unmeasured by the vendors and, as far as this research found, by anyone else. It also does not
cover copyright, IP indemnity or licence-contamination questions, which belong to other strands of
ticket #7.

---

## Unsettled — do not state as fact

1. **Whether the EU-US Data Privacy Framework survives.** Adequacy is in force and the first
   challenge failed; **C-703/25 P is pending with no outcome found**. Both "the DPF has been upheld"
   and "the DPF is on the verge of collapse" overstate the record. State it as: in force, under
   appeal, no outcome.
2. **Whether "we do not train on your code" and multi-year retention of flagged content are in
   tension.** They are legally distinct and vendors are entitled to both positions. Whether a given
   organisation's risk model treats a two-year retention of flagged source as acceptable is a
   judgement this document does not make.
3. **Whether embeddings of source code are personal data or a derived work.** Nothing read in this
   research addresses it, and EDPB Opinion 28/2024's anonymity test is framed for models, not for
   customer-side vector indexes. Genuinely open.
4. **Whether the GitHub default change is material for professional teams.** Business and Enterprise
   are excluded; the affected population is individuals on personal plans, which includes contractors
   working on client code. Whether that is a marginal or a serious exposure depends entirely on who
   is using what, and is not resolvable from the terms.
5. **Whether "self-hosted" deployments meaningfully reduce data-governance exposure** when the
   conversation still reaches the vendor's inference API. The infrastructure argument (checkouts and
   artifacts stay put) and the data argument (prompts and outputs do not) point in opposite
   directions, and which dominates is jurisdiction- and sector-dependent.
6. **Whether the absence of any attended/unattended distinction in vendor contracts is a gap or a
   deliberate design.** It is consistently absent. Whether that is because the distinction is
   commercially irrelevant, legally awkward, or simply not yet demanded by customers is not
   established by any source read here.
7. **Which controller/processor roles apply to a background agent acting on public issue text.** The
   vendor is a processor for inference; the customer is the controller for the repository; the status
   of untrusted third-party issue content that becomes agent input is not addressed by any DPA read
   here.

---

## Blocked or unavailable sources

Logged, never circumvented. No security control, login wall, paywall or bot challenge was bypassed,
and no alternate route around any block was attempted.

| URL | Block type | Consequence |
|---|---|---|
| `openai.com/enterprise-privacy/` | **HTTP 403** | OpenAI's consolidated enterprise privacy position not read from source |
| `openai.com/policies/data-processing-addendum/` | **HTTP 403** | OpenAI DPA text, SCC and DPF references unestablished; no Art. 28 comparison offered |
| `docs.github.com/en/site-policy/privacy-policies/github-copilot-privacy-statement` | **HTTP 404** | The dedicated Copilot privacy statement appears to have been folded into the general statement; retention specifics not recovered |
| `docs.github.com/en/copilot/get-started/privacy` | **HTTP 404** | — |
| `docs.github.com/en/copilot/how-tos/manage-your-account/manage-copilot-policies-as-an-individual-subscriber` | **HTTP 404** | The individual opt-out setting could not be confirmed from a docs page; only from the community announcement |
| `copilot.github.trust.page/faq` | HTTP 200, JS shell — title only | GitHub Copilot Trust Center FAQ not readable |
| `www.anthropic.com/legal/subprocessors` | **HTTP 404** | Anthropic subprocessor list unestablished |
| `trust.anthropic.com` | HTTP 200, title-only shell | Anthropic certifications and residency commitments not read from source |
| `developers.google.com/gemini-code-assist/resources/data-governance` | **HTTP 404** | Superseded; content now on docs.cloud.google.com |
| `antigravity.google/privacy` and `antigravity.google/docs` | Redirect to the generic Google privacy policy / a getting-started shell | Successor to Gemini Code Assist for individuals has no retrievable product data-governance page |
| `docs.cloud.google.com/gemini-code-assist/docs/data-governance` | **HTTP 404** | Edition-by-edition (Standard vs Enterprise vs individual) comparison for Google not established |
| `docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance` and `.../learn/data-governance` | Nav index only / **HTTP 404** | Vertex-specific caching and abuse-monitoring terms for third-party models unestablished |
| `www.jetbrains.com/legal/docs/ai/data-collection-and-use-policy/` and `/legal/docs/ai/` | **HTTP 404** | Equivalent content reached at `jetbrains.com/help/ai/` instead |
| `docs.continue.dev/telemetry` | Redirect shell, no content | Continue's local/offline posture unestablished |
| `edpb.europa.eu/.../edpb_opinion_202428_ai-models_en.pdf` | PDF returned as unparseable binary | Opinion 28/2024 quoted from the EDPB's own summary page, labelled as such; paragraph numbers unavailable |
| `docs.tabnine.com/main/welcome/readme/tabnine-privacy` | **HTTP 404** | Correct paths (`/privacy.md`, `/security.md`) used instead |
| `learn.chatgpt.com/docs/security` | Fetched, but covers a different product (Codex Security, an application-security agent) | Codex data-handling read from `agent-approvals-security.md` and `sandboxing.md` instead |

**Redirects recorded as findings rather than blocks:** `platform.openai.com/docs/guides/your-data`
→ 301 → `developers.openai.com/api/docs/guides/your-data`; `cloud.google.com/gemini/docs/*` → 301 →
`docs.cloud.google.com/gemini/docs/*`; `developers.openai.com/codex/security` → 308 →
`learn.chatgpt.com/docs/security`.

⚠️ **Anomaly, recorded and not acted on — second independent occurrence in this project.** Five AWS
documentation pages read for this strand (`service-improvement.html`, `opt-out-IDE.html`,
`data-protection.html`, `abuse-detection.html`, `data-retention.html`) each ended with an identical
trailing block, styled as documentation, instructing the reader to run an
`aws agent-toolkit search-skills` command. The same pattern was recorded independently in
[research/tooling-background-agents.md](./tooling-background-agents.md) across four *different* AWS
pages. Verbatim repetition of a command-promotion snippet across unrelated pages remains inconsistent
with AWS documentation authoring and resembles content injected somewhere in the fetch pipeline.
**The command was not run and the text was treated as untrusted data.** Its recurrence across two
independent research sessions raises rather than lowers the concern, and it is exactly the shape of
input the lethal trifecta's second leg describes: untrusted content arriving inside otherwise
authoritative material, addressed to an agent with tool access.
