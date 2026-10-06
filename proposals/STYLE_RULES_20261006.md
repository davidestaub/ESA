# ESA style rules (6 Oct 2026)

Every section of the ESA must follow these rules before it is committed. They are derived from Ben Moseley's DPhil thesis, *Physics-informed machine learning: from concepts to real-world applications* (Oxford, 2022). The thesis is at `~/Desktop/ICL_PHD/references/Moseley_2022_Physics-informed_machine_learning.pdf` and is not in the repo. Read Chapter 1 (PDF pages 21–32) and Chapter 4 before a style review.

`proposals/style_check.py` measures the numbers below for any `.tex` file.

## 1. Measured targets

| Measure | Ben, thesis body (52k words) | Ben, Chapter 1 | ESA intro now | ESA methods now | Target |
|---|---|---|---|---|---|
| Median sentence length | 23 words | 18 | 33–34 | 32 | 18–24 |
| Sentences over 35 words | 20% | 11% | 43–47% | 42% | at most 20% |
| Sentences under 10 words | 8% | 22% | 3% | 7% | 8–20% |
| Commas per 1000 words | 53 | 58 | 77 | 77 | at most 60 |
| Semicolons per 1000 words | 1.6 | 1.0 | 3.3–3.7 | 4.1 | at most 1.5 |
| Colons per 1000 words | 1.8 | 1.0 | 4.0–4.3 | 2.6 | at most 2 |
| "which" per 1000 words | 6.0 | 4.5 | 10.7–11.0 | 8.7 | at most 6 |
| "For example" per 1000 words | 1.4 | 2.6 | 0.9–1.0 | 0.2 | at least 1 |
| First person per 1000 words | 11.7 ("we"/"our") | 9.9 | 1.8–2.0 ("I") | 2.4 ("I") | 4–8 ("I") |
| Em dashes | 0 | 0 | 0 | 0 | 0 |
| Sentences in the passive | 33% | | | | at most 35% |

The current ESA text differs from Ben mainly in sentence length. Its sentences are about 50% longer than his, and are held together by commas, semicolons and "which" clauses. Splitting sentences is the main style change, including in the parts of the Introduction we keep.

## 2. Write like this

- **Why before how.** Open with the context and purpose, then describe the mechanism.
- **Signpost sections.** Open a section with "In this section, I …" (Ben writes "In this chapter we …").
- **Use Ben's connectives:** "Firstly, … Secondly, … Finally, …", "For example, …", "In particular, …", "However, …", "Furthermore, …" (Ben uses it about once per 1,200 words; never stack it with "moreover" or "additionally", which he never uses), "whilst", "Note that …".
- **Equations.** Follow every equation with a "where X is …" clause.
- **Abbreviations.** Introduce each one in parentheses on first use: "time-series observation (TSO)".
- **Figures.** Let figures lead paragraphs where possible: "Figure 3 shows …". Ben refers to a figure about every 270 words.
- **Numbers.** Give plain numbers with units, and the uncertainty where one exists.
- **Limitations.** State them directly, in a sentence of their own.
- **Hedging.** Hedge only as much as the evidence requires, using "may", "could" and "suggests". Ben uses these about 2.4 times per 1,000 words.
- **Questions.** Questions are allowed in the Introduction, where Ben asks them freely (25 in Chapter 1). Avoid them elsewhere.
- **Spelling.** British: modelling, behaviour, whilst, -ise endings as the existing text has them.
- **Person.** First person singular "I", for what I did and decided. Never "we" (Davide's ruling).

## 3. Never write

- **Em dashes**, or "---" in LaTeX.
- **Contrast reflexes:** "not X, but Y" and "X isn't just A, it's B". "Rather than" is allowed as Ben uses it (about 0.3 per 1,000 words), never as a flourish.
- **Short dramatic closers or openers:** "This matters." "The answer is no." "That is the problem." Short sentences that state a plain fact are fine.
- **Lists of three used as rhythm.** Ben writes "A, B and C" about once per 1,000 words when there really are three things; never pad a list to three.
- **Rhetorical questions** outside the research questions.
- **Colon reveals**, as in "The reason is simple: …".
- **Bold or bullet points in prose.** An enumerated list is allowed only for the objectives.
- **AI vocabulary:** delve, leverage, pivotal, landscape, notably, crucially, it is worth noting, underscores, highlights the importance, plays a key role, seamless, in essence, moreover, additionally, and "e.g." (Ben writes "for example"; "i.e." is rare). "Importantly" is his and is allowed.
- **Our working jargon:** frozen, registered, pre-registered, sealed, genuine, gate, firewall, admissible, authoritative, certificate, byte for byte.
- **Internal names:** V45, R7, sp0022, sp0025, MVI, Track A/B, dga_00, LOW/HIGH. Describe things by what they are, for example "the lower estimate of the starlight".
- **Claims stronger than the evidence.** Never present an untested design as validated.

## 4. Content rules

- Every number and every causal "why" must be traced to a file. Each section gets a fact sheet listing the source of every number. On 24 Sep, two invented reasons slipped in when a section was rewritten "reason first".
- After every cut or condensing pass, compare the new text with the previous version, sentence by sentence. The 24 Sep cut to 20 pages introduced about 26 errors.
- Describe what is implemented now, not a design that has not been built. The new benchmark is described as a design with its planned tests.

## 5. Checks on every section before commit

1. Run `style_check.py`: every target is met, or the reason it isn't is noted.
2. Style read by Fable or ASTRA, against these rules and the named thesis pages.
3. Fact check against the fact sheet and the source files.
4. A "suspicious professor" read: would an examiner ask "what is he trying to say here?" anywhere?

Passing an AI detector is not a target. Detectors are unreliable in both directions. The aim is clear writing in Ben's register, with Davide's own final read.

## Changes after Fable 1256Z

- "Rather than" and lists of three moved from banned to judgment rules.
- Questions allowed in the Introduction.
- "e.g." banned; "importantly" allowed.
- The checker matches banned words on word boundaries, so "gate" no longer fires on "investigate".

## Changes after ASTRA 1311Z (corrections to the evidence for the rules)

- **Page range.** Chapter 1 is PDF pages 23–36 (printed 1–14); PDF 21 is the abbreviations list.
- **"e.g."** Ben does use it (PDF 25, 26, 30, 104, 120). Preferring "for example" is our editorial choice, not his rule.
- **Bullets.** Ben uses bullets in his Contributions list (PDF 33–35). In the ESA they are allowed for objectives and contributions, never in running prose.
- **"where" after equations.** Define symbols where they are new. Do not repeat "where" mechanically (cf. Eqs. 4.5 and 4.7).
- **Questions.** Ben also opens Chapter 4 with a research question (PDF 101). In the ESA, questions are allowed in the Introduction and in a section opening that states its question.
- **Vocabulary.** The banned list is our editorial choice. Ben does use "seamlessly" once (PDF 26).
- **The statistics are editing diagnostics, not per-section quotas.** Never insert "I", "For example" or "In this section" just to hit a number.
- **Model for exposition:** Chapter 4 (equations 4.5–4.6; Section 4.5.1), which separates sampled real noise from generated components and synthetic-truth tests from checks on real images.
