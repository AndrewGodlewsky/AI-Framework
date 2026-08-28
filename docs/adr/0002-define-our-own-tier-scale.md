# Define our own tier scale rather than adopting an autonomy-levels standard

This project's whole structure is an ordered set of positions between minimal AI assistance and
full autonomy, so the obvious move is to adopt an existing autonomy-levels scale. Research
established that no such standard exists: verified negatively against NIST AI RMF, ISO/IEC 22989,
IEEE P3394, SAE and the EU AI Act. The vocabulary originates with a DeepMind paper (Morris et al.,
2023), but the leading proposals actively contradict each other — "Consultant" is Level 2 for
DeepMind and Level 3 for Feng et al. — and both Anthropic and OpenAI have explicitly declined
discrete levels. We therefore define this project's own tiers, and state in the documents that we
are defining them rather than reporting a standard.

## Consequences

- **Tier Taxonomy (issue #8) inherits this as a constraint**, not an open question. That ticket
  decides what our tiers are; it does not get to decide whether to adopt someone else's, because
  there is no coherent someone else.
- Documents must never write a bare level reference such as "L3 autonomy" — it is uninterpretable
  without naming the scale. Where a tier is referenced, name it.
- Tiers are boundaries in what the human stops doing and what verification replaces them, not
  points on a published autonomy dial. Autonomy itself is treated as a per-action property.
- Where an external scale is genuinely useful for comparison, cite it by author and year
  (e.g. "Morris et al.'s Level 2") rather than by bare number.
