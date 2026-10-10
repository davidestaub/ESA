# Opus style review of the ESA (b50eb10), 9 October 2026

> **Correction (10 Oct):** this review describes the Introduction as "not reworked since September". That is wrong. The git log shows it was rewritten from scratch on 7 October in the structure Davide approved (39c147f). It then went through Davide's read-through and Overleaf comments, a three-way review the same evening, a purpose sweep on 8 October (3d4b9f1) and one sentence on 9 October. The claim came from an old memory note and was not checked. Each item still stands on the current text, but the framing does not. Per 1,000 words, the Introduction has the fewest suggestions of any section (11.5, against 15 to 20 elsewhere).


Individual review, written before reading Fable's or ASTRA's. Five readers each covered one part of the report sentence by sentence, using STYLE_RULES_20261006.md, and I then checked every item against the text. "Current" is verbatim LaTeX source (every quote was matched against the file), and "Proposed" is LaTeX-ready. Impact 3 means a reader would stumble or an examiner would notice, 2 means clearly better, and 1 means polish. No ESA file was edited.

**Totals:** 210 items and 15 whole-paragraph rewrites. Each rewrite combines items from the same paragraph, so apply either the rewrite or its items, not both.

## If Davide changes only fifteen things

1. **abs-s3-s5-03-32** (03_benchmark.tex:32): "The reference atmosphere" is never defined anywhere in the report, yet it is used here, in the Figure 6 caption and in Section 3.3. A reader will ask "which reference atmosphere?". The proposal names it in the abstract's own terms ("one injected atmosphere"). See the question to Davide for a fuller gloss.
2. **abs-s3-s5-03-110** (03_benchmark.tex:110): Logic slip. Two depths can both be non-zero and still agree, so "should be zero. Instead, they differed" is a non sequitur. The quantity being tested is their difference, and an examiner will notice the gap.
3. **nova-237** (02_nova.tex:237): Eq. 8 ends with a comma, but no 'where' clause follows. The next sentence starts 'The first term ...', so the PDF shows '..., (8) The first term'. The comma is a leftover from the version that had a 'where' clause after the equation. The equation should end with a full stop.
4. **measured-111** (04_measured_benchmark.tex:111): The text cites Figure 8 (line 48) before Figure 7 (line 76), so the PDF numbers the figures out of order. Moving the programme-4476 figure above the WASP-17 Gaia figure fixes this. The original block at lines 151-166 must then be deleted, and the caption fixes measured-156 and measured-162 applied to the moved copy.
5. **intro-A-175** (01_introduction.tex:175): The PDF currently prints '(Figure 2), [Albert et al., 2023, Louie et al., 2025], at about', with a stray comma before the citation and two bracket groups in a row. Leading with the figure removes both and keeps exactly the same citations on the same claims.
6. **nova-200** (02_nova.tex:200): The two field-star sentences added on 9 October sit in the middle of the background-map paragraph. As a result, 'these pixels' in 'The maps are made orthonormal over these pixels' now follows a sentence about field stars on the traces, so the reader has to search three sentences back for the antecedent. This change moves the field-star sentences, otherwise unchanged, to the end as their own short paragraph. Because 'also' would then have nothing close to refer to, it is replaced by 'left out of the off-trace pixels and of', which says the same thing. If Davide wants the agreed wording kept exactly, keep 'Field stars are also left out of the $1/f$ correction' and drop the paragraph break. The change also fixes the agreement error ('How well ..., and how much ..., has' should be plural, or recast), uses active 'I have not yet tested', and corrects 'WASP-17 visit' to 'WASP-17~b visit'.
7. **intro-B-522** (01_introduction.tex:522): "Crucially" is on the banned list, and style_check flags it. The sentence makes its point without the intensifier.
8. **intro-B-636** (01_introduction.tex:636): In the current version the verb "can cause" comes only after two comma-fenced gerund phrases, so the question has to be read twice. The fix puts the verb first and lists the two causes in pipeline order. Meaning and scope ("can") are unchanged.
9. **measured-47** (04_measured_benchmark.tex:47): Field sources stay fixed on the sky; only their position on the detector changed. A physicist will read "moved with the telescope" literally.
10. **measured-20** (04_measured_benchmark.tex:20): This gives "the moved exposure" (Davide's term, used in the abstract, the captions and Sections 4.2-4.3) its name where the exposure is introduced. At present the section switches between "second", "moved" and "real" exposure without saying that they are the same.
11. **abs-s3-s5-05-41** (05_discussion_plan.tex:41): "Fixed" is ambiguous here. Right after "improve NOVA", most readers will take it to mean "repaired", whereas the intended meaning is that no further changes are made, which is the sense of "fixed" in Paper 2.
12. **abs-s3-s5-03-61** (03_benchmark.tex:61): The object is delayed by two modifiers ("counts as starlight near the traces only the light..."), so the sentence cannot be parsed on the first pass. "In the first" also tells the reader that this is the first of the three injections just announced. This item is also covered by paragraph rewrite S3 L58-70.
13. **measured-204** (04_measured_benchmark.tex:204): Garden path: "where the orders overlap with ATOCA" first reads as the orders overlapping with ATOCA.
14. **nova-316** (02_nova.tex:316): 'After interpolating ..., NOVA is deeper' is a dangling participle: NOVA did not do the interpolating, and 'NOVA' is a method, not a spectrum. 'Throughout' could be read as 'throughout the range below 1.8 um', the subject of the first half of the sentence. 'At every wavelength' is the wording of the abstract and Section 5, so this also makes the three places consistent. The meaning is unchanged.
15. **intro-B-378** (01_introduction.tex:378): "Subtracted before the light curves were fitted" is the third time in about fifteen lines that this point is made (364-365, 370-371). The fix keeps the cited fact (background held fixed) and the consequence in one sentence.

## Abstract, Section 3, Section 5, Section 6

**How it reads now.** The abstract is in good shape. It has only two or three small idiom points, and none of them is a real problem. Section 3 tells a clear story, but it is the roughest of my four files. Three colons work as reveals. One sentence delays its object ("counts as starlight near the traces only the light..."), and one fit sentence stacks four modifiers. The term "the reference atmosphere" is used without ever being defined. The null test has a small logic slip ("should be zero. Instead, they differed"), and "matters" appears twice as a closer. Section 5 is well structured, but the Paper 2 paragraph is very long and dense. Its main faults are a noun pile, a them/its mismatch, "which" chains and an ambiguous "NOVA's differences". The Discussion has two unclear referents ("It is designed", "cannot provide it"), and "held back until NOVA is fixed" can be read as "repaired". In the Gantt chart, "Thesis integration" clashes with the report's technical meaning of "integration", and "geometry extensions" is unclear. The AI statement in Section 6 needs no change.

### abs-s3-s5-00-16: 00_abstract.tex:16 · grammar · impact 1

Current:
```latex
but must decide which of the observed light belongs to the star.
```
Proposed:
```latex
but must decide which part of the observed light belongs to the star.
```
Reason: This is the only point in the agreed abstract worth raising. "which of" with the mass noun "light" is slightly unidiomatic, and the Introduction says "which part of the recorded light".

### abs-s3-s5-00-17: 00_abstract.tex:17 · clarity · impact 1

Current:
```latex
exoTEDRF reversed with the
```
Proposed:
```latex
exoTEDRF reversed when I changed the
```
Reason: "reversed with the share" can be read as if the ranking and the share reversed together. This is optional, because the abstract is agreed.

### abs-s3-s5-00-20: 00_abstract.tex:20 · clarity · impact 1

Current:
```latex
It observed a star at its usual position and again moved off the SOSS
```
Proposed:
```latex
It observed a star at its usual position and again with the star moved off the SOSS
```
Reason: "and again moved off" can be misread as "moved off again". This is optional, because the abstract is agreed.

### abs-s3-s5-03-7: 03_benchmark.tex:7 · AI tell · impact 2

Current:
```latex
For a real planet the true spectrum is unknown. An injection test supplies a
truth: a known transmission spectrum is added to detector data, and the
spectrum that each method recovers is compared with it.
```
Proposed:
```latex
For a real planet the true spectrum is unknown, so an injection test supplies
one. It adds a known transmission spectrum to detector data and compares the
spectrum that each method recovers with it.
```
Reason: "supplies a truth: ..." is a colon reveal. Linking the first two sentences with "so" also turns the restated fact from Section 1.6 into the reason for the test, so it no longer reads as a bare repeat.

### abs-s3-s5-03-13: 03_benchmark.tex:13 · grammar · impact 1

Current:
```latex
the injector has to decide which of the observed light is
```
Proposed:
```latex
the injector has to decide which part of the observed light is
```
Reason: "which of" with the mass noun "light" is unidiomatic. The Introduction uses "which part of the recorded light".

### abs-s3-s5-03-19: 03_benchmark.tex:19 · flow · impact 1

Current:
```latex
and this section describes
what they taught me.
```
Proposed:
```latex
and in this section I describe
what they taught me.
```
Reason: Uses the first-person signpost of the style rules ("In this section, I ...") instead of the section as subject.

### abs-s3-s5-03-26: 03_benchmark.tex:26 · repetition · impact 1

Current:
```latex
This is simple, but it adds the transit
only after the steps
```
Proposed:
```latex
This is simple, but the transit then skips the steps
```
Reason: The previous sentence already says "after the detector stages". "adds the transit only after the steps" repeats "after" and "adds the transit".

### abs-s3-s5-03-32: 03_benchmark.tex:32 · clarity · impact 3

Current:
```latex
NOVA's root-mean-square error for the reference atmosphere
```
Proposed:
```latex
NOVA's root-mean-square error for one injected atmosphere, which I call the reference atmosphere,
```
Reason: "The reference atmosphere" is never defined anywhere in the report, yet it is used here, in the Figure 6 caption and in Section 3.3. A reader will ask "which reference atmosphere?". The proposal names it in the abstract's own terms ("one injected atmosphere"). See the question to Davide for a fuller gloss.

### abs-s3-s5-03-44: 03_benchmark.tex:44 · clarity · impact 2

Current:
```latex
I subtracted from the injected data the $1/f$ correction
calculated from the same data without the transit. There, the light curve is
```
Proposed:
```latex
I calculated the $1/f$ correction from the same data without
the transit and subtracted it from the injected data. Without the transit, the light curve is
```
Reason: "subtracted from the injected data the ... correction calculated from ..." delays the object, and "There," could point to either data set. Putting the steps in order and naming the case makes this read in one pass.

### abs-s3-s5-03-50: 03_benchmark.tex:50 · AI tell · impact 2

Current:
```latex
How much of the faint light outside the traces dims therefore matters.
To inject a transit correctly, I would need to know
```
Proposed:
```latex
To inject a transit correctly, I would therefore need to know
```
Reason: "X therefore matters." is the short-closer AI tell that style_check flags. The next sentence already states the point concretely, so the "matters" sentence adds nothing.

### abs-s3-s5-03-59: 03_benchmark.tex:59 · AI tell · impact 2

Current:
```latex
To see how much this matters, I made three
```
Proposed:
```latex
To see how strongly the recovered spectra depend on this, I made three
```
Reason: This is the second "matters" in two paragraphs (style_check flags "this matters"). The proposal says what is being measured.

### abs-s3-s5-03-61: 03_benchmark.tex:61 · clarity · impact 3

Current:
```latex
The lower estimate counts as starlight near the traces only
the light explained by a model of the star.
```
Proposed:
```latex
In the first, the lower estimate, only the part of the light near the traces that
a model of the star explains counts as starlight.
```
Reason: The object is delayed by two modifiers ("counts as starlight near the traces only the light..."), so the sentence cannot be parsed on the first pass. "In the first" also tells the reader that this is the first of the three injections just announced. This item is also covered by paragraph rewrite S3 L58-70.

### abs-s3-s5-03-64: 03_benchmark.tex:64 · clarity · impact 2

Current:
```latex
through ATOCA's model of the detector, together with a smooth background made
of four of NOVA's eight background maps and held in place by the same
off-trace pixels (Section~\ref{sec:continuum}).
```
Proposed:
```latex
through ATOCA's model of the detector. The fit also included a smooth
background, made of four of NOVA's eight background maps and held in place by
the off-trace pixels that NOVA uses (Section~\ref{sec:continuum}).
```
Reason: About 50 words with four stacked modifiers. "the same off-trace pixels" also has no antecedent in this section (same as what?). The proposal splits the sentence and says whose pixels they are.

### abs-s3-s5-03-66: 03_benchmark.tex:66 · clarity · impact 2

Current:
```latex
this estimate leaves typically 0.4, 2.2 and 4.0\% of the light undimmed at 1.0 to 1.8, 1.8 to 2.3 and 2.3 to $2.8\,\mu\mathrm{m}$.
```
Proposed:
```latex
this estimate typically leaves 0.4\% of the light undimmed at 1.0 to $1.8\,\mu\mathrm{m}$, 2.2\% at 1.8 to $2.3\,\mu\mathrm{m}$ and 4.0\% at 2.3 to $2.8\,\mu\mathrm{m}$.
```
Reason: Three numbers followed by three ranges force the reader to match them up by hand, and "leaves typically" has the adverb in the wrong place. Pairing each number with its range reads at once.

### abs-s3-s5-03-67: 03_benchmark.tex:67 · clarity · impact 2

Current:
```latex
The second injection is the same, except that it also dims
this faint light; it changed NOVA's spectrum by about 40~ppm. The upper
estimate instead counts all the light in the box as starlight and dims it,
and leaves the faint light beyond 80 pixels undimmed, like the lower estimate.
```
Proposed:
```latex
The second injection is the same, except that it also dims
this faint light, and this changed NOVA's spectrum by about 40~ppm. The third, the upper
estimate, instead counts all the light in the box as starlight and dims it.
Like the lower estimate, it leaves the faint light beyond 80 pixels undimmed.
```
Reason: The paragraph announces three injections but names them "lower estimate", "second injection" and "upper estimate", so the reader has to work out that the upper estimate is the third. The proposal also removes a semicolon (Section 3 is at 1.6 per 1000 words) and the stacked "and dims it, and leaves ...".

### abs-s3-s5-03-88: 03_benchmark.tex:88 · consistency · impact 1

Current:
```latex
Under the upper estimate the order
```
Proposed:
```latex
Under the upper estimate, the ranking
```
Reason: The abstract and Section 5.1 call this "the ranking", so using the same word here keeps the terms consistent. The comma matches the parallel "Under the lower estimate," one sentence earlier.

### abs-s3-s5-03-91: 03_benchmark.tex:91 · grammar · impact 2

Current:
```latex
exoTEDRF counts all the light left in its box
after background subtraction as starlight, like the upper estimate, whereas
the lower estimate split the light
```
Proposed:
```latex
Like the upper estimate, exoTEDRF counts as starlight all the light left in
its box after background subtraction, whereas the lower estimate splits the light
```
Reason: As it stands, the sentence opens with a lower-case name ("light. exoTEDRF counts"), which looks like a typo in print. The object is also split from "as starlight" by a long phrase. The past tense "split" also clashes with the present tense used for the estimates elsewhere ("counts", "leaves").

### abs-s3-s5-03-107: 03_benchmark.tex:107 · grammar · impact 1

Current:
```latex
by the same fraction as the centre; if part of it is background, the box dims less.
```
Proposed:
```latex
by the same fraction as the centre. If part of this light is background, the box dims less.
```
Reason: Removes a semicolon (Section 3 is over target) and the vague "it".

### abs-s3-s5-03-108: 03_benchmark.tex:108 · AI tell · impact 2

Current:
```latex
repeated it on stretches without a transit: I fitted the same transit shape,
at a time when no transit happens, to the box and to the bright centre.
```
Proposed:
```latex
repeated it on stretches without a transit. I fitted the same transit shape to
the box and to the bright centre, at a time when no transit happens.
```
Reason: This colon works as a reveal (Section 3 has 3.9 colons per 1000 words against a target of 2). Moving "at a time when no transit happens" to the end also stops it splitting "fitted ... to the box".

### abs-s3-s5-03-110: 03_benchmark.tex:110 · clarity · impact 3

Current:
```latex
fitted depths should be zero. Instead, they differed
```
Proposed:
```latex
fitted depths should be zero, and so should their difference. Instead, the two depths differed
```
Reason: Logic slip. Two depths can both be non-zero and still agree, so "should be zero. Instead, they differed" is a non sequitur. The quantity being tested is their difference, and an examiner will notice the gap.

### abs-s3-s5-03-114b: 03_benchmark.tex:114 · AI tell · impact 2

Current:
```latex
Only this range gives a clear answer: at 1.75
```
Proposed:
```latex
Only this range gives a clear answer. At 1.75
```
Reason: This colon is a reveal. A full stop reads more naturally and lowers the colon count.

### abs-s3-s5-03-114c: 03_benchmark.tex:114 · AI tell · impact 2

Current:
```latex
it depends on how the detector behaves: if the fit allows
```
Proposed:
```latex
it depends on how the detector behaves. If the fit allows
```
Reason: This colon is a reveal, the third in this paragraph. Splitting it gives two sentences that each read in one pass.

### abs-s3-s5-03-114a: 03_benchmark.tex:114 · clarity · impact 2

Current:
```latex
but it cannot tell the injector how much of it to dim.
```
Proposed:
```latex
but the measurement cannot tell the injector how much of the light to dim.
```
Reason: Two uses of "it" with different referents (the measurement, the light) in one clause. See also paragraph rewrite S3 L114, which moves this conclusion to the end, after its reasons.

### abs-s3-s5-05-9: 05_discussion_plan.tex:9 · clarity · impact 2

Current:
```latex
belongs to the star, stated or not, and its verdict
```
Proposed:
```latex
belongs to the star, whether or not it says so, and its verdict
```
Reason: The clipped "stated or not" is wedged between the object and the next clause, and it is unclear what is (not) stated. The fuller phrase reads naturally.

### abs-s3-s5-05-14: 05_discussion_plan.tex:14 · clarity · impact 2

Current:
```latex
readout. It
is designed to measure which kinds of error each method makes when the
injected light curve is known, and where in its processing they arise.
```
Proposed:
```latex
readout. The
benchmark is designed to measure, against a known injected light curve, which
kinds of error each method makes and where in its processing they arise.
```
Reason: After "The price is a different star, field and readout", the word "It" seems to point to the price or the readout, not the benchmark. In the benchmark the injected light curve is always known, so "when the injected light curve is known" reads as if it were a condition.

### abs-s3-s5-05-20: 05_discussion_plan.tex:20 · grammar · impact 1

Current:
```latex
wavelength, and most in the red (Section~\ref{sec:nova-real}), and its
```
Proposed:
```latex
wavelength, most in the red (Section~\ref{sec:nova-real}), and its
```
Reason: Two "and"s in a row. The abstract has the same phrase without the first one ("deeper at every wavelength, most in the red").

### abs-s3-s5-05-21: 05_discussion_plan.tex:21 · clarity · impact 3

Current:
```latex
An injection test shows how accurately each method recovers a known spectrum, which is the best guide to which real spectrum to trust, and an injector built from the WASP-17~b data alone cannot provide it.
```
Proposed:
```latex
An injection test shows how accurately each method recovers a known spectrum. This is the best guide to which real spectrum to trust, but an injector built from the WASP-17~b data alone cannot provide it.
```
Reason: The "which ... which" chain is followed by "and ... it", where "it" has no clear antecedent (the test? the guide?). Two sentences make "it" point to the guide. The contrast is already implied, and "but" states it.

### abs-s3-s5-05-41: 05_discussion_plan.tex:41 · clarity · impact 2

Current:
```latex
held back until NOVA is fixed.
```
Proposed:
```latex
held back until the changes to NOVA are complete.
```
Reason: "Fixed" is ambiguous here. Right after "improve NOVA", most readers will take it to mean "repaired", whereas the intended meaning is that no further changes are made, which is the sense of "fixed" in Paper 2.

### abs-s3-s5-05-42: 05_discussion_plan.tex:42 · clarity · impact 2

Current:
```latex
will refit NOVA's spectrum of the real WASP-17~b visit, with uncertainties
from an ensemble of simulated observations, and compare it with the three
```
Proposed:
```latex
will refit the real WASP-17~b visit with NOVA, estimate the uncertainties
from an ensemble of simulated observations, and compare the spectrum with the three
```
Reason: One refits data, not a spectrum. "with uncertainties from ..." also hangs loosely. Three parallel verbs (three real steps) read more cleanly.

### abs-s3-s5-05-45: 05_discussion_plan.tex:45 · repetition · impact 2

Current:
```latex
also propose that JWST repeat programme 4476 for several cooler stars, read
out as a SOSS time series and with more integrations at the usual position.
```
Proposed:
```latex
also propose that JWST repeat programme 4476 for several cooler stars
(Section~\ref{sec:benchmark-limits}).
```
Reason: The last paragraph of Section 4.5, one page earlier, gives the same details (SOSS time-series readout, more integrations at the usual position). A cross-reference avoids saying it twice in a row. "Cooler" is kept.

### abs-s3-s5-05-53: 05_discussion_plan.tex:53 · clarity · impact 3

Current:
```latex
NOVA together with those pipelines of each visit's published reductions that
are publicly available, and run each of them on the benchmark as well, so that its errors on the same known case can be measured.
```
Proposed:
```latex
NOVA together with the publicly available pipelines used in each visit's
published reductions. I will also run each of these pipelines on the benchmark, so that its errors on the same known case can be measured.
```
Reason: "those pipelines of each visit's published reductions that are publicly available" is a noun pile with a delayed relative clause. "each of them ... its" also mixes plural and singular. Splitting the sentence fixes both.

### abs-s3-s5-05-56: 05_discussion_plan.tex:56 · clarity · impact 2

Current:
```latex
including supreme-SPOON, now exoTEDRF, and \texttt{transitspectroscopy},
```
Proposed:
```latex
including supreme-SPOON (now exoTEDRF) and \texttt{transitspectroscopy},
```
Reason: "supreme-SPOON, now exoTEDRF, and transitspectroscopy, and a joint analysis" has four commas and two "and"s in a row, so it is unclear where the list ends. Parentheses take the appositive out.

### abs-s3-s5-05-58a: 05_discussion_plan.tex:58 · clarity · impact 2

Current:
```latex
This is in the red range where NOVA's spectrum of WASP-17~b differs most from Ahsoka's
```
Proposed:
```latex
This fall lies in the red, where NOVA's spectrum of WASP-17~b differs most from Ahsoka's
```
Reason: "This" has no clear referent (the metallicity? the clouds? the 2 to 2.3 um range?). "This is in the red range where" is also awkward.

### abs-s3-s5-05-58b: 05_discussion_plan.tex:58 · consistency · impact 1

Current:
```latex
while the fall in depth
```
Proposed:
```latex
whilst the fall in depth
```
Reason: House spelling: Sections 1 and 2 use "whilst" throughout. Section 5 has the only other "while"s, apart from one in Section 4.

### abs-s3-s5-05-62: 05_discussion_plan.tex:62 · clarity · impact 2

Current:
```latex
while another analysis does not
\citep{WangEtAl2026}.
```
Proposed:
```latex
whilst another analysis finds none
\citep{WangEtAl2026}.
```
Reason: Coming after "and favour an explanation ...", the bare "does not" can attach to "favour" instead of "find". "Whilst" also matches the house spelling used everywhere else.

### abs-s3-s5-05-63: 05_discussion_plan.tex:63 · clarity · impact 2

Current:
```latex
Both sides suggest differences in reduction as possible causes, and NOVA's reduction will show which of the two its spectrum supports.
```
Proposed:
```latex
Both sides suggest differences in reduction as possible causes of the disagreement, and I will test which of the two NOVA's spectrum supports.
```
Reason: "NOVA's reduction will show which of the two its spectrum supports" is circular and hard to parse ("its" = NOVA's). "Causes" also needs an object.

### abs-s3-s5-05-64: 05_discussion_plan.tex:64 · clarity · impact 2

Current:
```latex
The HAT-P-18~b visit contains a spot crossed by the planet during the transit
and a field star on the order-1 trace whose brightness changes, probably an
eclipsing binary \citep{FuEtAl2022}. It therefore tests
```
Proposed:
```latex
The HAT-P-18~b visit contains a spot that the planet crosses during the
transit, and a variable field star on the order-1 trace, probably an
eclipsing binary \citep{FuEtAl2022}. This visit therefore tests
```
Reason: "the order-1 trace whose brightness changes" attaches "whose" to the trace, not the star. After the field star, "It" is also ambiguous. "Variable" is the standard plain word, and the meaning is unchanged.

### abs-s3-s5-05-69: 05_discussion_plan.tex:69 · clarity · impact 2

Current:
```latex
so it tests whether NOVA's
differences still matter
```
Proposed:
```latex
so it tests whether the differences between NOVA and the other pipelines
still matter
```
Reason: "NOVA's differences" does not say differences from what. Please confirm the reading (see questions).

### abs-s3-s5-05-72: 05_discussion_plan.tex:72 · clarity · impact 2

Current:
```latex
\citep{BellEtAl2023},
overlapping the red end of SOSS, where NOVA differs most for WASP-17~b, which
gives an independent check of NOVA's red end.
```
Proposed:
```latex
\citep{BellEtAl2023}.
This range overlaps the red end of SOSS, where NOVA differs most for
WASP-17~b, so it gives an independent check of NOVA's spectrum there.
```
Reason: A dangling participle ("overlapping" seems to modify NIRCam), then "where ..., which ...", and "red end" twice in one sentence. Two sentences remove the chain.

### abs-s3-s5-05-77: 05_discussion_plan.tex:77 · grammar · impact 1

Current:
```latex
which is again tested on the benchmark
```
Proposed:
```latex
which will again be tested on the benchmark
```
Reason: The tense should match the future plan ("will go into a later version").

### abs-s3-s5-05-82: 05_discussion_plan.tex:82 · AI tell · impact 2

Current:
```latex
This matters most for
small planets around cool stars.
```
Proposed:
```latex
These questions matter most for
small planets around cool stars.
```
Reason: "This matters ..." is a flagged AI tell (style_check finds it), and "This" is vague after a two-part aim. "These questions" points to the two aims.

### abs-s3-s5-05-85: 05_discussion_plan.tex:85 · flow · impact 2

Current:
```latex
\citep{RackhamEtAl2018}, and they change, as do flares, from one visit to the
next.
```
Proposed:
```latex
\citep{RackhamEtAl2018}. They change from one visit to the next, and so
do flares.
```
Reason: "they change, as do flares, from one visit" splits the verb from its phrase with an aside. Two clean clauses read at once.

### abs-s3-s5-05-89: 05_discussion_plan.tex:89 · clarity · impact 2

Current:
```latex
to test whether spots on the star that the planet does not cross explain this rise, as \citet{FournierTondreauEtAl2024} propose, rather than a haze \citep{FuEtAl2022}.
```
Proposed:
```latex
to test whether this rise comes from spots on the star that the planet does not cross, as \citet{FournierTondreauEtAl2024} propose, or from a haze \citep{FuEtAl2022}.
```
Reason: "rather than a haze" is cut off from "spots" by the "as ... propose" aside, so it dangles. "whether ... or from ..." states the same test with the alternatives side by side.

### abs-s3-s5-05-93: 05_discussion_plan.tex:93 · clarity · impact 1

Current:
```latex
flares and such stellar signals into the benchmark
```
Proposed:
```latex
flares and the signals of such spots and bright regions into the benchmark
```
Reason: "such stellar signals" is vague, and flares are stellar signals too. The proposal names the second model's signal.

### abs-s3-s5-05-95: 05_discussion_plan.tex:95 · clarity · impact 2

Current:
```latex
in the out-of-transit SOSS data, which would
feed directly into this paper.
```
Proposed:
```latex
in the out-of-transit SOSS data, and their results would
feed directly into this paper.
```
Reason: "which" grammatically points to "the SOSS data", not the projects.

### abs-s3-s5-05-112: 05_discussion_plan.tex:112 · clarity · impact 2

Current:
```latex
These signals are weak, and it would be
interesting to see whether a detector-level analysis also makes them more
reliable.
```
Proposed:
```latex
These signals are weak, and I would test whether a detector-level analysis
also makes them more reliable.
```
Reason: "it would be interesting to see" is filler and sounds casual for a plan. The first person matches the rest of the plan. "also" is kept (see questions).

### abs-s3-s5-05-154: 05_discussion_plan.tex:154 · clarity · impact 2

Current:
```latex
{Instrument and geometry extensions}
```
Proposed:
```latex
{Extensions to NIRSpec and eclipses}
```
Reason: "geometry extensions" is unclear: a reader will think of transit geometry, not secondary eclipses. The new label matches Section 5.2's own summary, "extend NOVA to NIRSpec and to secondary eclipses".

### abs-s3-s5-05-164: 05_discussion_plan.tex:164 · consistency · impact 2

Current:
```latex
{Thesis integration}
```
Proposed:
```latex
{Thesis chapters from papers}
```
Reason: In this report, "integration" is a technical term for a detector exposure, used dozens of times. A Gantt bar called "Thesis integration" makes the reader pause. The proposed label says what the bar means.

### abs-s3-s5-05-172: 05_discussion_plan.tex:172 · grammar · impact 1

Current:
```latex
The research phase ends on approximately 27 April
2029, and
```
Proposed:
```latex
The research phase ends around 27 April
2029, and
```
Reason: "ends on approximately" is awkward. "around" carries the same approximation.

### Paragraph rewrites (Abstract, Section 3, Section 5, Section 6)

**03_benchmark.tex, lines 41-48**, starting "My injector, however, dimmed only its model of the star."

```latex
My injector, however, dimmed only its model of the star. Near the traces,
this model matched the real images, but outside them, at 0.85 to
$1.75\,\mu\mathrm{m}$ in order~1, it held only about a third of the light that
the correction expects to dim. During the transit, the correction therefore
found too much light left outside the traces, mistook it for $1/f$ noise and
removed it from the whole column, so the transit became about 1 to 2\% too
deep. To confirm this, I calculated the $1/f$ correction from the same data
without the transit and subtracted it from the injected data. Without the
transit, the light curve is flat, so the correction removes the same stripes
but has no transit to react to. NOVA's error then fell to 150~ppm, so the
correction caused about half of the increase. In the real data, the dimming
outside the traces at these wavelengths was consistent with what the
correction assumes (Section~\ref{sec:real-data-test}), so much of this faint
light seems to behave like starlight.
```
Reason: In the current order, the real-data sentence sits between the cause (the injector held only a third of the light) and its "therefore" consequence, which breaks the chain. It also makes "To confirm this" point to the wrong sentence. Moving it to the end, with a pointer to Section 3.4 where the measurement is given in full, restores the cause-and-effect order. It also turns the repetition with Section 3.4 into an explicit preview and leads into "To inject a transit correctly, I would therefore need to know ..." (item abs-s3-s5-03-50). The rewrite also includes item abs-s3-s5-03-44. "there" becomes "outside the traces at these wavelengths", which keeps the 0.85 to 1.75 um scope.

**03_benchmark.tex, lines 58-70**, starting "The WASP-17~b data alone cannot say how much of this light is starlight, not"

```latex
The WASP-17~b data alone cannot say how much of this light is starlight, not
even inside the extraction box. To see how strongly the recovered spectra
depend on this, I made three injections. All three dim the measured light in
the wings, 16 to 80 pixels from the traces. In the first, the lower estimate,
only the part of the light near the traces that a model of the star explains
counts as starlight. I made this model by fitting the star's spectrum, with a
slow change in time, to the out-of-transit images through ATOCA's model of
the detector. The fit also included a smooth background, made of four of
NOVA's eight background maps and held in place by the off-trace pixels that
NOVA uses (Section~\ref{sec:continuum}). In exoTEDRF's 40-row extraction box,
this estimate typically leaves 0.4\% of the light undimmed at 1.0 to
$1.8\,\mu\mathrm{m}$, 2.2\% at 1.8 to $2.3\,\mu\mathrm{m}$ and 4.0\% at 2.3
to $2.8\,\mu\mathrm{m}$. It also leaves the faint light beyond 80 pixels
undimmed. The second injection is the same, except that it also dims this
faint light, and this changed NOVA's spectrum by about 40~ppm. The third, the
upper estimate, instead counts all the light in the box as starlight and dims
it. Like the lower estimate, it leaves the faint light beyond 80 pixels
undimmed.
```
Reason: This is the hardest paragraph in my part to read on the first pass. It combines items 03-59, 03-61, 03-64, 03-66 and 03-67: the three injections are numbered as announced, the delayed object and the four-modifier fit sentence are untangled, each percentage is paired with its range, and the semicolon and the double "and" are removed. No number, range or condition is changed.

**03_benchmark.tex, lines 106-112**, starting "I also tried to measure the share of starlight directly from the real data."

```latex
I also tried to measure the share of starlight in the box directly from the
real data. If the bright centre of the trace is almost pure starlight, and all
the light in the extraction box is starlight too, the box dims during the
transit by the same fraction as the centre. If part of this light is
background, the box dims less. In the red part of order~1, the two fractions
typically agreed to within about 1\%, which would favour the upper estimate.
To check how reliable this comparison is, I repeated it on stretches without
a transit. I fitted the same transit shape to the box and to the bright
centre, at a time when no transit happens. Both fitted depths should be zero,
and so should their difference. Instead, the two depths differed by up to
about 11\% of the real transit depth, ten times more than the 1\% needed to
tell the two estimates apart. The real data therefore cannot decide.
```
Reason: Combines items 03-107, 03-108 and 03-110. The semicolon and the colon reveal are removed, the "should be zero. Instead, they differed" slip is fixed, and "the share of starlight" and "the two" say what is being compared ("in the box", "fractions"). The closing sentence is kept as committed. It repeats the subsection title and comes before the second real-data test, but changing it would narrow its scope.

**03_benchmark.tex, lines 114**, starting "I also measured how much the faint light outside the traces dims during the real transit,"

```latex
I also measured how much the faint light outside the traces dims during the
real transit, on the pixels that the $1/f$ correction uses. At 0.85 to
$1.75\,\mu\mathrm{m}$ in order~1, it dimmed by
$0.033\pm0.007$~DN\,s$^{-1}$ per pixel, as much as if all the light left
there after background subtraction were starlight. This suggests that most of
this light behaves like starlight. Only this range gives a clear answer,
however. At 1.75 to $2.1\,\mu\mathrm{m}$ the measurement is too noisy to tell
the cases apart, and at 2.1 to $2.8\,\mu\mathrm{m}$ the light appears to dim
about four times more than even starlight would, which I cannot explain. Even
where the answer is clear, it depends on how the detector behaves. If the fit
allows the detector's level to change during the transit, the share of this
light that dims like starlight ranges from about half to all of it. The
measurement cannot tell the injector how much of this light to dim.
```
Reason: Removes both colon reveals (items 03-114b and 03-114c) and the double "it" (03-114a). The paragraph's conclusion ("cannot tell the injector how much to dim") is moved from the middle, where it came before its reasons, to the end. No "therefore" is added, so no new causal claim is made.

**05_discussion_plan.tex, lines 50-79**, starting "\paragraph{Paper 2: Five further SOSS visits.} The aim is to find out whether"

```latex
\paragraph{Paper 2: Five further SOSS visits.} The aim is to find out whether
NOVA changes the atmospheric conclusions for other SOSS targets, and if so,
why. I will analyse five SOSS visits as real data. As in Paper~1, I will run
NOVA together with the publicly available pipelines used in each visit's
published reductions. I will also run each of these pipelines on the
benchmark, so that its errors on the same known case can be measured. Each
visit was chosen for its own reason. WASP-39~b has the best-studied SOSS
spectrum, with six independent reductions of the same visit, including
supreme-SPOON (now exoTEDRF) and \texttt{transitspectroscopy}, and a joint
analysis with three other JWST modes
\citep{FeinsteinEtAl2023,CarterEtAl2024}. Its metallicity is constrained by
the water bands across the spectrum, whilst the fall in depth between 2 and
$2.3\,\mu\mathrm{m}$ favours patchy, non-grey clouds. This fall lies in the
red, where NOVA's spectrum of WASP-17~b differs most from Ahsoka's, so the
question is whether NOVA reproduces these conclusions. For WASP-96~b,
published analyses of the same visit disagree on whether the spectrum rises
towards the blue. Some find such a slope
\citep{RadicaEtAl2023,TaylorEtAl2023,RadicaEtAl2026} and favour an
explanation involving small particles high in the atmosphere
\citep{TaylorEtAl2023,RadicaEtAl2026}, whilst another analysis finds none
\citep{WangEtAl2026}. Both sides suggest differences in reduction as possible
causes of the disagreement, and I will test which of the two NOVA's spectrum
supports. The HAT-P-18~b visit contains a spot that the planet crosses during
the transit, and a variable field star on the order-1 trace, probably an
eclipsing binary \citep{FuEtAl2022}. This visit therefore tests how NOVA
handles light that its transit model does not describe, and Paper~3 returns
to it with a model of the star. HAT-P-26~b has the shallowest transit of the
five, with features of only a few hundred ppm, so it tests whether the
differences between NOVA and the other pipelines still matter for such small
signals. HST and NIRSpec spectra exist for comparison
\citep{WakefordEtAl2017,GressierEtAl2025}. For WASP-80~b, NIRCam has
measured methane between 2.4 and $4\,\mu\mathrm{m}$ \citep{BellEtAl2023}.
This range overlaps the red end of SOSS, where NOVA differs most for
WASP-17~b, so it gives an independent check of NOVA's spectrum there.

I will analyse all five visits with the same version of NOVA, fixed before
the spectra are compared. Anything learnt from them, such as a better
treatment of field stars, will go into a later version, which will again be
tested on the benchmark before it is used. Since the errors measured in
Paper~1 come from a hotter star, a repeat of programme 4476 on cooler stars
would make this comparison firmer.
```
Reason: The paragraph runs for almost a full column with no break, and most of its sentences have comma or "which" problems. The rewrite combines items 05-53, 05-56, 05-58a, 05-58b, 05-62, 05-63, 05-64, 05-69, 05-72 and 05-77. It also adds one paragraph break before "I will analyse all five visits ...", which separates the per-visit reasons from the method rule. All citations, targets, numbers and hedges are unchanged.

### Notes across sections

- The true spectrum of a real planet is unknown: the report says this in the abstract, the opening of Section 1, the first sentence of Section 1.6, the end of Section 2.9 and the first sentence of Section 3.1. Item 03-7 turns the Section 3 instance into a reason, not a bare repeat.
- The real-data dimming of the faint light outside the traces at 0.85 to 1.75 um is stated in Section 3.2 (line 41) and again, with the number, in Section 3.4 (line 114). Sections 2.5 and 4.5 also point to it. Paragraph rewrite S3 L41-48 makes the Section 3.2 mention an explicit preview of Section 3.4.
- Repeating programme 4476 comes up four times: in Section 4.5 (last paragraph, with full details), in Paper 1 (the same details again), in the last sentence of Paper 2 (cooler stars) and in Paper 4 (the NIRSpec equivalent). Item 05-45 trims Paper 1 to a cross-reference.
- "Where NOVA's spectrum of WASP-17 b differs most" appears twice in the Paper 2 paragraph (WASP-39 b and WASP-80 b), and the same point is made in Sections 5.1 and 2.9.
- "Rests on a single star" or "one star" appears twice in Section 4.5 and again in Paper 1.
- Units: Section 2.3 writes "100~DN/s" and "1.5 to 2~DN/s", whereas Sections 3 and 4 write DN\,s$^{-1}$. One form should be used throughout.
- The same idea is worded three ways: "which of the observed light" (abstract and Section 3.1), "which part of the recorded light" (Introduction) and "which light belongs to the star" (Section 5.1). "Which part of" is the idiomatic form.
- "The ranking ... reversed" (abstract and Section 5.1) against "the order reversed" (Section 3.3); item 03-88 aligns them.
- "while" in Section 4 (line 305) and Section 5 (lines 58 and 62) against "whilst" everywhere in Sections 1 and 2.
- The abstract says "repeated transits and stellar variability", but Section 5 and the Gantt chart say "repeated visits". These are close but not identical, and the abstract is agreed, so I only note it.
- The abstract uses "the SOSS strip" without defining it. The Introduction (Section 1.6) and Section 4 define the strip. This is acceptable for an abstract, but a non-SOSS examiner may stumble.
- Secondary eclipses are defined in Section 1.1 and defined again in Paper 5. The second definition is harmless as a reminder.
- The four needs of a benchmark are listed at the end of Section 1.6 and restated in Section 3.1. This is acceptable as a deliberate reminder, but the Section 3.1 version adds a serial comma ("raw reads, and several pipelines") that the rest of the report does not use.

### Questions for Davide (would change meaning, so not proposed as replacements)

- Section 3.2, line 32: "the reference atmosphere" is never defined. Could you add one plain clause saying what it is (for example, the model WASP-17 b atmosphere injected in every test of Section 3)? My item uses only "one injected atmosphere, which I call the reference atmosphere", which is all the abstract supports.
- Section 3.2: the spectrum was "about 90 ppm too deep", yet the 1/f correction made "the transit ... about 1 to 2% too deep". At a depth of about 1.5%, 1 to 2% is roughly 150 to 300 ppm, and the correction caused only about half of the 90 ppm. Is the 1 to 2% local (0.85 to 1.75 um, order 1), or relative to something else? If so, the sentence should say so, because a careful reader will do this arithmetic.
- Section 3.3: "Neither estimate is the truth" says that both are wrong, whereas the next two sentences only say that each may be wrong or is not determined. Do you mean "Neither estimate is known to be right"? I left the sentence unchanged because this would change the meaning.
- Section 3.4: "too noisy to tell the cases apart": which cases? If they are "all of this light is starlight" against "none of it is", naming them would help.
- Paper 2, HAT-P-26 b: does "NOVA's differences" mean the differences between NOVA's spectra and those of the other pipelines? My item assumes so.
- Paper 4: "validate each on injected data": the benchmark itself is checked against the real exposure (Section 4.4), not on injected data. Is "each" meant to cover the benchmark?
- Paper 4: "favour a possible water world" stacks two hedges. Damiano et al. say "potentially habitable water world". Would "favour a water world" or "are consistent with a water world" be closer to what you mean? This is a scope change, so I did not propose it.
- Paper 5: "whether a detector-level analysis also makes them more reliable": the word "also" presupposes that NOVA makes transit spectra more reliable, which Paper 1 has yet to show. Keep "also", or drop it? My item keeps it.
- Abstract: "predicts every pixel". NOVA fits only the pixels in its two apertures (Section 2.2: "every fitted pixel"). Is the compression acceptable in the abstract?
- Gantt chart: is "Thesis integration" meant as "turning the papers into thesis chapters"? My proposed label is "Thesis chapters from papers".

### Possible errors noticed in passing

- Section 3.2: "about 90~ppm too deep" against "the transit became about 1 to 2% too deep". For a transit of about 1.5%, 1 to 2% too deep is about 150 to 300 ppm, which is more than the total 90 ppm bias, and the correction caused only about half of the RMSE increase. These are consistent only if the 1 to 2% refers to a limited wavelength range or to a different quantity. Please check the source.
- "The reference atmosphere" (Section 3.2, Section 3.3 and the Figure 6 caption) is used but never defined anywhere in the report.
- Section 3.4 null test: "Both fitted depths should be zero. Instead, they differed ..." is a logic slip. The test concerns the difference between the two depths, not whether each depth is zero.
- Section 5.2, Paper 1: "held back until NOVA is fixed" can be read as "until NOVA is repaired", whereas the meaning is "until NOVA stops changing".
- Gantt chart: "Thesis integration" clashes with "integration" as a detector exposure, and "Instrument and geometry extensions" does not obviously cover secondary eclipses.

## Introduction, lines 1–229 (opening, §1.1, §1.2)

**How it reads now.** Lines 1-229 mostly read clearly and plainly, and the statistics meet the targets: median sentence 19 words, 3% of sentences over 35 words, no semicolons or colon reveals. The text has not been reworked since September, and four kinds of weakness remain. First, a handful of sentences put a long appositive or parenthesis between the subject and the verb. These are the GR700XD sentence, the limb-darkening aside, the cylindrical-lens sentence and the 'atmospheric signal' sentence, and they are where a reader stumbles. Second, there is one visible punctuation error in the PDF, a stray comma before the citation at column 700, and one repeated fact: HST's sodium detection in HD 209458 b is told twice, in two neighbouring subsections. Third, the opening paragraph packs the problem, NOVA and the benchmark into one block, and the first-point sentence ('Firstly, the background light is subtracted') reads as a processing step, not as the first of two error points. Subsection 1.2 also restarts with planet discovery right after 1.1 promised 'an instrument ... and a planet'. Fourth, a few AI-sounding tics and small term drifts remain: 'not by choice', 'However, whilst', 'apparent' against 'effective' radius, 'the first order' against 'order 1', hyphenated number ranges where Sections 2-4 write 'X to Y', and 'visit' and 'pipeline' used without a definition.

### intro-A-7a: 01_introduction.tex:7 · clarity · impact 2

Current:
```latex
Firstly, the background light is subtracted, and any background that remains is not modelled when the transit is fitted.
```
Proposed:
```latex
The first is the subtraction of the background light. Any background that remains after this subtraction is not modelled when the transit is fitted.
```
Reason: After 'I focus on two of them', the reader expects the first error point to be named. 'Firstly, the background light is subtracted' reads instead like the first step of the chain. Naming the point directly also matches the opening of Section 1.4 ('The first step is the treatment of the background').

### intro-A-7b: 01_introduction.tex:7 · clarity · impact 2

Current:
```latex
Secondly, each image is compressed into a one-dimensional spectrum, which can lose
information that the later steps cannot recover.
```
Proposed:
```latex
The second is the compression of each image into a one-dimensional spectrum. This compression can lose information that the later steps cannot recover.
```
Reason: Grammatically, 'which' attaches to 'spectrum', but it is the compression that loses information. This also parallels intro-A-7a.

### intro-A-8: 01_introduction.tex:8 · clarity · impact 2

Current:
```latex
I have therefore developed
Nonlinear Order-coupled Variable-projection Analysis (NOVA).
```
Proposed:
```latex
I have therefore developed a method called Nonlinear Order-coupled Variable-projection Analysis (NOVA).
```
Reason: 'Developed Nonlinear Order-coupled ... Analysis' reads as if he developed an analysis technique in general. Saying 'a method called' tells the reader at once that NOVA is the method's name. A paragraph break before this sentence would also help (see the paragraph rewrite).

### intro-A-11: 01_introduction.tex:11 · flow · impact 2

Current:
```latex
and in the same fit it fits whatever background the earlier
```
Proposed:
```latex
and the same fit includes whatever background the earlier
```
Reason: 'In the same fit it fits' repeats the word 'fit' clumsily. The meaning, one fit for both, is unchanged.

### intro-A-12: 01_introduction.tex:12 · clarity · impact 2

Current:
```latex
Whether NOVA or the established methods give the
more accurate spectrum cannot be decided from real data, because the true
spectrum of a real planet is unknown.
```
Proposed:
```latex
Real data cannot decide whether NOVA or the established methods give the more accurate spectrum, because the true spectrum of a real planet is unknown.
```
Reason: The current sentence opens with a 13-word 'Whether' clause as its subject and a passive verb. The active version reads correctly on the first pass and echoes the Section 3.4 title, 'The real data cannot decide'.

### intro-A-21: 01_introduction.tex:21 · grammar · impact 2

Current:
```latex
temperatures and orbits, many with no
```
Proposed:
```latex
temperatures and orbits, and many have no
```
Reason: 'Orbits, many with no counterpart' can attach to 'orbits'. The edit makes it clear that the planets are what lack a counterpart.

### intro-A-25: 01_introduction.tex:25 · clarity · impact 2

Current:
```latex
The atmosphere helps to distinguish between these possible compositions, and its composition can also hint
```
Proposed:
```latex
Observing the atmosphere of a planet helps to distinguish between these possibilities, and the composition of the atmosphere can also hint
```
Reason: An atmosphere does not 'help'; observing it does. 'Compositions ... its composition' repeats a word, and 'its' could mean the planet's bulk composition. The sentence also switches from plural planets to an unexplained singular 'the atmosphere'.

### intro-A-28: 01_introduction.tex:28 · clarity · impact 2

Current:
```latex
If the stellar disc were uniformly bright (in reality it dims towards its edge, an effect called limb darkening), the depth of a transit would be approximately
```
Proposed:
```latex
The stellar disc dims towards its edge, an effect called limb darkening. If the disc were instead uniformly bright, the depth of a transit would be approximately
```
Reason: The parenthesis, which itself contains an appositive, interrupts the conditional just before the equation. Stating the fact first and then the idealisation reads more naturally and keeps the equation attached to its own sentence.

### intro-A-48: 01_introduction.tex:48 · consistency · impact 1

Current:
```latex
hence the apparent radius of the
```
Proposed:
```latex
hence the effective radius of the
```
Reason: The text defines $R_p(\lambda)$ as the 'effective radius', and the caption then calls it the 'apparent radius'. Use one name. The figure label in figures/transmission_spectroscopy_schematic.tex (line 87, 'larger apparent radius') should change too.

### intro-A-54: 01_introduction.tex:54 · clarity · impact 2

Current:
```latex
Only a thin ring of atmosphere around the planet filters the starlight, so the atmospheric signal, the part of the transit depth that changes with wavelength, is a small fraction of the stellar flux.
```
Proposed:
```latex
Only a thin ring of atmosphere around the planet filters the starlight. The atmospheric signal, the part of the transit depth that changes with wavelength, is therefore a small fraction of the stellar flux.
```
Reason: Currently a 'so' clause is followed by a definition wedged between subject and verb. Splitting the sentence leaves the definition in a sentence of its own.

### intro-A-58: 01_introduction.tex:58 · grammar · impact 2

Current:
```latex
A class of planets that satisfies these
conditions is the so-called hot Jupiters, gas giants that orbit close to their
stars \citep{Brown2001,Madhusudhan2019}.
```
Proposed:
```latex
Hot Jupiters, gas giants that orbit close to their stars, satisfy these conditions \citep{Brown2001,Madhusudhan2019}.
```
Reason: 'A class ... is the so-called hot Jupiters' mixes singular and plural and delays the subject. 'So-called' also sounds slightly dismissive. The edit is shorter and direct, with the same claim and citations.

### intro-A-66: 01_introduction.tex:66 · repetition · impact 1

Current:
```latex
the drop in light isolates the light
```
Proposed:
```latex
the drop in brightness isolates the light
```
Reason: 'Light ... light' in four words reads clumsily.

### intro-A-71: 01_introduction.tex:71 · grammar · impact 2

Current:
```latex
I start with transmission because a transit has a well-defined geometry that repeats with every orbit, making it a convenient test case of how the processing of the data affects the recovered spectrum.
```
Proposed:
```latex
I start with transmission because a transit has a well-defined geometry that repeats with every orbit. This makes a transit a convenient way to test how the processing of the data affects the recovered spectrum.
```
Reason: In the current sentence, 'making it' dangles: it could refer to the geometry, the orbit or the transit. 'Test case of how' is also unidiomatic. The edit splits the sentence and names the subject.

### intro-A-77: 01_introduction.tex:77 · flow · impact 1

Current:
```latex
does not always have a unique answer, because different combinations
```
Proposed:
```latex
does not always have a unique answer. Different combinations
```
Reason: The current sentence is 40 words with 'and it ... because'. Splitting it lets the list of degenerate quantities stand on its own, and the cause is still obvious from the order.

### intro-A-82: 01_introduction.tex:82 · repetition · impact 1

Current:
```latex
propagate into the retrieval.
```
Proposed:
```latex
carry over into the retrieved atmosphere.
```
Reason: 'Propagate into' already appears four lines earlier. Objective 4 itself says 'carry over into the atmospheric properties that a retrieval infers', so this wording makes the forward reference match the objective.

### intro-A-103: 01_introduction.tex:103 · repetition · impact 2

Current:
```latex
In 2002, HST found
sodium in the atmosphere of HD~209458~b \citep{CharbonneauEtAl2002}.
```
Proposed:
```latex
The detection of sodium in HD~209458~b, mentioned above, was made with HST in 2002 \citep{CharbonneauEtAl2002}.
```
Reason: The same detection, with the same citation, is already told in Section 1.1 (lines 60-62). An examiner reading it again a column later notices the repetition. The edit acknowledges the earlier mention and adds only the new facts, HST and 2002.

### intro-A-109: 01_introduction.tex:109 · consistency · impact 1

Current:
```latex
such as $1.1$-$1.7\,\mu\mathrm{m}$
```
Proposed:
```latex
such as 1.1 to $1.7\,\mu\mathrm{m}$
```
Reason: In LaTeX, a hyphen between numbers prints a short hyphen, which is typographically wrong for a range. Sections 2-4 write ranges as 'X to Y'. The same issue occurs at lines 110, 123, 135 and 197; see the items for 110, 123 and 135 and the paragraph rewrite for 197.

### intro-A-110: 01_introduction.tex:110 · clarity · impact 1

Current:
```latex
spectrum, such as one over $0.3$-$5\,\mu\mathrm{m}$, therefore had to be
combined from observations with several instruments of HST and Spitzer, made
at different times
```
Proposed:
```latex
spectrum, such as one over 0.3 to $5\,\mu\mathrm{m}$, therefore had to be combined from observations made at different times with several instruments on HST and Spitzer
```
Reason: In the current wording, 'made at different times' trails after the instruments and seems to modify them. Instruments are 'on' a telescope, not 'of' it. The edit also fixes the range format.

### intro-A-114: 01_introduction.tex:114 · clarity · impact 1

Current:
```latex
Like HST, it is used for exoplanets mainly to
characterise planets that are already known.
```
Proposed:
```latex
Like HST, it is used in exoplanet science mainly to characterise planets that are already known.
```
Reason: 'Used for exoplanets mainly to characterise planets' is clumsy and says 'planets' twice. The scope ('in exoplanet science') is kept, so the edit does not imply that JWST is mainly an exoplanet telescope.

### intro-A-123: 01_introduction.tex:123 · consistency · impact 1

Current:
```latex
covers $0.6$-$2.8\,\mu\mathrm{m}$ in one observation
```
Proposed:
```latex
covers 0.6 to $2.8\,\mu\mathrm{m}$ in one observation
```
Reason: Range format consistent with Sections 2-4 (see intro-A-109).

### intro-A-130: 01_introduction.tex:130 · flow · impact 2

Current:
```latex
In this project, I use a mode of NIRISS, called Single Object Slitless
```
Proposed:
```latex
In this project, I use this mode of NIRISS, called Single Object Slitless
```
Reason: The previous paragraph has just introduced 'a mode that covers 0.6-2.8 µm'. Saying 'a mode' again reads as if this were a different mode, and 'this mode' ties the two paragraphs together.

### intro-A-133: 01_introduction.tex:133 · clarity · impact 3

Current:
```latex
An optical element called GR700XD, a grism (a prism carrying a diffraction grating) combined with a prism, spreads the light into several copies of the spectrum, called orders
```
Proposed:
```latex
An optical element called GR700XD spreads the light into several copies of the spectrum, called orders. GR700XD combines a grism, which is a prism carrying a diffraction grating, with a second prism
```
Reason: Thirteen words, including a parenthesis inside an appositive, sit between the subject and its verb, and 'prism' appears twice in the insertion. Splitting the sentence lets the reader first learn what GR700XD does, then what it is. The existing \citep on the next line then closes the second sentence.

### intro-A-135: 01_introduction.tex:135 · consistency · impact 1

Current:
```latex
$0.6$-$2.8\,\mu\mathrm{m}$ range mentioned above
```
Proposed:
```latex
range of 0.6 to $2.8\,\mu\mathrm{m}$ mentioned above
```
Reason: Range format (see intro-A-109). The sentence then reads 'Orders 1 and 2 together give the range of 0.6 to 2.8 µm mentioned above.'

### intro-A-136: 01_introduction.tex:136 · consistency · impact 1

Current:
```latex
$\lambda/\Delta\lambda$ of the first order is about 650 at
```
Proposed:
```latex
$\lambda/\Delta\lambda$ of order 1 is about 650 at
```
Reason: The report says 'order 1' everywhere else, including the previous sentence. 'The first order' is the one exception.

### intro-A-140: 01_introduction.tex:140 · clarity · impact 2

Current:
```latex
cylindrical lens spreads the light over about 23 detector rows, so that bright stars can be observed without saturating the pixels, and so that small pointing jitter and errors in the flat field, the map of each pixel's sensitivity, matter less
```
Proposed:
```latex
cylindrical lens spreads the light over about 23 detector rows. Bright stars can then be observed without saturating the pixels, and small pointing jitter and errors in the flat field, the map of each pixel's sensitivity, matter less
```
Reason: In the current wording, two 'so that' clauses are chained with a definition inside the second, which makes the sentence hard to follow. Putting the effects in their own sentence makes it read at once.

### intro-A-146: 01_introduction.tex:146 · clarity · impact 1

Current:
```latex
The arrows mark a field star whose light falls on the
  edge of the order-1 trace, and the step in the zodiacal background near
  column 700, to the right of which the background is brighter.
```
Proposed:
```latex
One arrow marks a field star whose light falls on the edge of the order-1 trace. The other marks the step in the zodiacal background near column 700, to the right of which the background is brighter.
```
Reason: 'Falls on the edge of the order-1 trace, and the step ...' briefly reads as 'the edge of the trace and the step'. The figure has exactly two labelled arrows (plot_soss_detector_scene.py), so 'one ... the other' is accurate.

### intro-A-156: 01_introduction.tex:156 · repetition · impact 1

Current:
```latex
tested during commissioning, the test period before science operations, on
```
Proposed:
```latex
measured during commissioning, the test period before science operations, on
```
Reason: 'Tested ... the test period' repeats the word, and the precision was in fact measured.

### intro-A-162: 01_introduction.tex:162 · flow · impact 1

Current:
```latex
The spectrum, in contrast to the white-light curve,
```
Proposed:
```latex
Unlike the white-light curve, the spectrum
```
Reason: This puts the contrast first and the subject next to its verb ('the spectrum is measured in channels').

### intro-A-167: 01_introduction.tex:167 · AI tell · impact 2

Current:
```latex
However, whilst SOSS measures light precisely, its data are difficult to
```
Proposed:
```latex
Although SOSS measures light precisely, its data are difficult to
```
Reason: 'However, whilst' stacks two contrast words, which is a typical machine-written pattern. One connective is enough.

### intro-A-172a: 01_introduction.tex:172 · clarity · impact 2

Current:
```latex
The spectra of other stars in the field of view, called field stars, therefore also fall on the detector, and some of them land on the traces of the target
```
Proposed:
```latex
Other stars in the field of view, called field stars, therefore also form spectra on the detector, and some of these spectra land on the traces of the target
```
Reason: As written, 'called field stars' could name the spectra, and 'some of them' is ambiguous between the spectra and the stars. The edit makes the stars the subject, so the defined term attaches to the right noun.

### intro-A-172b: 01_introduction.tex:172 · AI tell · impact 2

Current:
```latex
SOSS is slitless out of necessity, not by choice.
```
Proposed:
```latex
SOSS is slitless out of necessity.
```
Reason: 'Not by choice' is the banned 'not X, but Y' contrast reflex, here as a short dramatic sentence. It also sits awkwardly two sentences before 'Being slitless also helps transit observations'. The plain fact is enough, and the next sentence gives the reason.

### intro-A-175: 01_introduction.tex:175 · LaTeX · impact 3

Current:
```latex
Its level changes abruptly
near detector column 700 (Figure~\ref{fig:soss-detector-orders}), \citep{AlbertEtAl2023,LouieEtAl2025},
```
Proposed:
```latex
Figure~\ref{fig:soss-detector-orders} shows that its level changes abruptly near detector column 700 \citep{AlbertEtAl2023,LouieEtAl2025},
```
Reason: The PDF currently prints '(Figure 2), [Albert et al., 2023, Louie et al., 2025], at about', with a stray comma before the citation and two bracket groups in a row. Leading with the figure removes both and keeps exactly the same citations on the same claims.

### intro-A-183: 01_introduction.tex:183 · clarity · impact 1

Current:
```latex
the background is therefore almost only
```
Proposed:
```latex
the background is therefore almost entirely
```
Reason: 'Almost only first-order light' is unidiomatic, and 'almost entirely' is the natural phrase.

### intro-A-195: 01_introduction.tex:195 · flow · impact 2

Current:
```latex
I focus on a hot Jupiter, WASP-17~b.
```
Proposed:
```latex
I focus on the hot Jupiter WASP-17~b.
```
Reason: The paragraph jumps from WASP-39 b to WASP-17 b in mid-flow, and the target of the whole project deserves its own paragraph. 'A hot Jupiter, WASP-17 b' reads as if any hot Jupiter would do. See also the paragraph rewrite for lines 193-205, which merges the following two-sentence 'However' paragraph into it.

### intro-A-208: 01_introduction.tex:208 · consistency · impact 2

Current:
```latex
A data reduction is the chain of software that
turns the detector data into a spectrum.
```
Proposed:
```latex
A data reduction is the processing that turns the detector data into a spectrum, and the software that performs it is called a pipeline.
```
Reason: The report uses both 'reduction' (one analysis) and 'pipeline' (the software). 'The pipelines' first appears at line 287 without definition, and the current definition makes a reduction a piece of software. Defining both terms here makes the distinction clear. This slightly changes the definition, so Davide should confirm (see questions).

### intro-A-209: 01_introduction.tex:209 · clarity · impact 2

Current:
```latex
The three reductions were Ahsoka,
which Louie et al.\ introduced, \texttt{transitspectroscopy}
\citep{Espinoza2022TransitSpectroscopy} with the transit-fitting code
\texttt{juliet} \citep{EspinozaEtAl2019}, and supreme-SPOON
\citep{RadicaEtAl2023}, now distributed as exoTEDRF \citep{Radica2024}.
```
Proposed:
```latex
One reduction used Ahsoka, which Louie et al.\ introduced. Another used \texttt{transitspectroscopy} \citep{Espinoza2022TransitSpectroscopy} with the transit-fitting code \texttt{juliet} \citep{EspinozaEtAl2019}. The third used supreme-SPOON \citep{RadicaEtAl2023}, now distributed as exoTEDRF \citep{Radica2024}.
```
Reason: With a relative clause, a 'with' phrase, four citations and the final appositive all separated by commas, a first-time reader cannot tell whether the list has three or four items ('introduced, transitspectroscopy ... juliet, and supreme-SPOON'). One sentence per reduction removes the ambiguity, and the names and citations are unchanged.

### intro-A-215: 01_introduction.tex:215 · flow · impact 2

Current:
```latex
The SOSS data also tightened the constraint on the water
abundance, compared with the HST and Spitzer data, and placed the abundance
above the solar value
```
Proposed:
```latex
Compared with the HST and Spitzer data, the SOSS data also tightened the constraint on the water abundance and placed it above the solar value
```
Reason: 'Compared with ...' is wedged between the two verbs and breaks the sentence. Putting the comparison first reads cleanly and avoids saying 'abundance' twice.

### Paragraph rewrites (Introduction, lines 1–229 (opening, §1.1, §1.2))

**01_introduction.tex, lines 4-16**, starting "The transmission spectrum of an exoplanet is the depth of its transit, the"

```latex
The transmission spectrum of an exoplanet is the depth of its transit, the
fraction of starlight that the planet blocks, at each wavelength. It is
obtained from a time series of detector images through a chain of processing
steps. Errors could enter at many points in this chain, and I focus on two of
them. The first is the subtraction of the background light. Any background
that remains after this subtraction is not modelled when the transit is
fitted. An error in that subtraction can bias the fitted transit depth, even
when the transit model fits the data well. The second is the compression of
each image into a one-dimensional spectrum. This compression can lose
information that the later steps cannot recover.

I have therefore developed a method called Nonlinear Order-coupled
Variable-projection Analysis (NOVA). NOVA does not compress the images into
spectra. It fits the transit to the detector pixels themselves, and the same
fit includes whatever background the earlier subtraction has left behind. Real
data cannot decide whether NOVA or the established methods give the more
accurate spectrum, because the true spectrum of a real planet is unknown. I am
therefore building a benchmark in which a known transit is added to the raw
data of a real observation from the James Webb Space Telescope (JWST). The
error of each method, NOVA included, can then be measured against a known
truth.
```
Reason: This combines intro-A-7a, 7b, 8, 11 and 12, and splits the opening into the problem (two error points) and the response (NOVA, then the benchmark). Currently the 200-word block runs the problem, the method and the validation together. The first-point sentence also reads as a processing step, and the 'which can lose' clause attaches to the wrong noun. All facts, scope words and wording choices ('the established methods', 'known truth') are kept.

**01_introduction.tex, lines 193-205**, starting "Despite these difficulties, SOSS has delivered detailed spectra. For example,"

```latex
Despite these difficulties, SOSS has delivered detailed spectra. For example,
one of the first SOSS analyses recovered the water bands, potassium absorption
and clouds of the Saturn-mass gas giant WASP-39~b \citep{FeinsteinEtAl2023}.

I focus on the hot Jupiter WASP-17~b. Its low density and low gravity give it
an extended atmosphere \citep{AndersonEtAl2010}. HST and Spitzer had already
measured its transmission spectrum over 0.3 to $5\,\mu\mathrm{m}$, by combining
observations made with several instruments between 2012 and 2017
\citep{AldersonEtAl2022}. However, that spectrum could not constrain how much
water the atmosphere contains \citep{LouieEtAl2025}. Depending on the
atmospheric model assumed in the retrieval, the HST and Spitzer data were
consistent with a water abundance below the solar value, with one above it, or
with two separate solutions, one below and one above
\citep{AldersonEtAl2022,LouieEtAl2025}.
```
Reason: This gives the project's target its own paragraph, instead of a mid-paragraph jump from WASP-39 b. It folds the two-sentence 'However, that spectrum ...' paragraph into it, because both describe WASP-17 b before SOSS. It also fixes the hyphenated range. All citations and claims are unchanged.

### Notes across sections

- Number ranges: the Introduction writes '$1.1$-$1.7\,\mu\mathrm{m}$' (lines 109, 110, 123, 135, 197 and also 490, outside this part), which prints a short hyphen. Sections 2-4 write '0.85 to $1.75\,\mu\mathrm{m}$'. Pick one convention: 'to' in prose, or an en dash '--' (an en dash is not an em dash).
- The flat field is defined twice: at line 140 ('the map of each pixel's sensitivity') and again at lines 304-306 ('a reference image of how sensitive each pixel is relative to the others'). Keep the first definition and shorten the second to a plain use.
- 'visit' first appears in the Figure 2 caption (line 145, 'the WASP-17~b SOSS visit') and is used throughout Sections 2-5, but it is never defined. A physicist who is not an SOSS specialist may not know that it means one observation of one transit.
- 'reduction' vs 'pipeline': the Introduction first says 'The pipelines therefore estimate the stripes' (line 287) and 'Pipelines differ ...' (line 333) without having defined the word, right after talking about 'reductions'. Sections 3-5 use 'pipeline' for the software and 'reduction' for a published analysis. intro-A-208 defines both at the first mention.
- Line 522 (Section 1.5) opens with 'Crucially', which is on the banned list; style_check.py flags it.
- The point 'a good fit does not show the background was subtracted correctly' is made three times in the Introduction: line 7 (opening), lines 480-482 (end of 1.4) and lines 522-526 (1.5). The background-not-modelled point is also restated at lines 365 and 370-371. One full statement plus brief back-references would be enough.
- 'extraction box' (Sections 3 and 4), 'extraction aperture ... also called the extraction box' (line 609) and 'a band of fixed width' (line 320) name the same thing. Introducing 'extraction box' once at the box-extraction sentence (lines 319-320) would let line 609 simply use it.
- The figure label in figures/transmission_spectroscopy_schematic.tex (line 87) says 'larger apparent radius', while the main text says 'effective radius' (see intro-A-48).
- Abstract (only flagging, not proposing): 'the published Ahsoka spectrum' and 'NOVA and exoTEDRF' name pipelines that an abstract reader has not met. A reader may not realise these are other pipelines. Two words such as 'the published Ahsoka reduction' or 'the exoTEDRF pipeline' would fix this, if the reviewers agree.

### Questions for Davide (would change meaning, so not proposed as replacements)

- Line 25, 'Some planets are also observed to lose gas from their upper atmosphere': what is this sentence for? As it stands, it is a loose end at the end of a paragraph about why atmospheres tell us about composition and formation. Either link it, for example by saying that such escape was also detected in transmission (if that is what Vidal-Madjar et al. 2003 shows and you want it), or cut it.
- Line 71: an examiner may object that a secondary eclipse also has a well-defined geometry that repeats with every orbit, so this reason does not single out transmission. Is the real reason different, for example that the benchmark dims starlight, or that transmission is the main use of SOSS? I did not reword it, because that would change the stated reason.
- Lines 187-191: 'Subtracting a single constant level instead would bias ...'. Does Radica et al. (2023) mean a flat constant pedestal, or one scale factor for the whole background model, as the transitspectroscopy reduction used (line 345)? If the latter, 'a single constant level' misdescribes it. If the former, the contrast with 'scaled separately on each side' is not parallel.
- Lines 88-99: Section 1.1 ends by saying I need 'an instrument ... and a planet', and Section 1.2 then steps back to how planets are found (pulsars in 1992, Kepler, TESS). Would you rather move this detection paragraph to the start of 1.1, before 'Exoplanets span a wide range ...'? Then 1.1 would run from discovery to atmospheres, and 1.2 would start with HST and Spitzer.
- intro-A-208 changes the definition of a data reduction from 'the chain of software' to 'the processing', and adds 'pipeline' as the name of the software. Is that the distinction you intend across the report? If not, keep the original and define 'pipeline' some other way before line 287.
- Where should 'visit' be defined? One option is line 207, for example 'one SOSS transit of WASP-17~b, which I call the WASP-17~b visit'. Another is to write 'observation' in the Figure 2 caption.

### Possible errors noticed in passing

- Lines 175-176 render in the PDF as '(Figure 2), [Albert et al., 2023, Louie et al., 2025], at about 2.15 µm', with a stray comma before the citation (fix in intro-A-175).
- Possible inconsistency inside the Introduction: line 190 says that subtracting 'a single constant level' would bias the depths, while line 345 describes the transitspectroscopy reduction as using 'a single scale factor for the background'. If these are meant to be the same alternative, the wording differs. If they are different, the reader may confuse them.
- The sodium detection in HD 209458 b by HST in 2002 (Charbonneau et al. 2002) is stated twice, at lines 60-62 and 103-104. It is not a factual error, but it is a visible repetition.

## Introduction, lines 230–665 (§1.3–§1.6)

**How it reads now.** At sentence level, lines 230-665 read cleanly. The median sentence is 18 words, commas run at 52 per 1000 words, there are no semicolons, and the language is plain and British. The main weakness is repetition rather than wording. The point that the background is subtracted before the transit fit, so the fit cannot correct it, is made about seven times across 1.3 to 1.5: at 357-360, 364-365, 370-371, 378-381, 413-415, 424-428 and 507-508. Three of these are back to back within a page. The same image or region also goes by several names: extraction aperture/aperture/extraction box; clean/constructed/cleaned image; outer/far wings. A few weak spots remain. The banned "Crucially" sits at 522, and the research question ends in a garden path ("the biases that fitting ..., and extracting ..., can cause?"). Some sentences duplicate their neighbours: the disagreement sentence at 500, the "transit could not help" sentence that repeats JExoRES at 427, and two "still"s at 525. The bad-pixel detail in 1.3 never comes back. The final paragraph of 1.5 uses "difference" four times in four sentences and moves between "will build", "turn" and "will be known".

### intro-B-fig3-label: conventional_reduction_workflow.tex:49 · clarity · impact 1

Current:
```latex
{fit clean slopes\\to retain rate}
```
Proposed:
```latex
{rate fitted from\\unaffected differences}
```
Reason: "Fit clean slopes to retain rate" is opaque. The new label repeats the caption's wording.

### intro-B-239: 01_introduction.tex:239 · clarity · impact 1

Current:
```latex
A cosmic ray adds a jump, which
  the several groups make visible, so the count rate can be fitted from the
  unaffected differences between reads.
```
Proposed:
```latex
Because the detector is read several times, a cosmic ray shows up as a jump, and the count rate can be fitted from the unaffected differences between reads.
```
Reason: "Which the several groups make visible" is an awkward relative clause. The new version gives the cause first.

### intro-B-250: 01_introduction.tex:250 · flow · impact 2

Current:
```latex
All three reductions used for WASP-17~b turned the raw detector data into a
transmission spectrum through the same basic chain of steps
\citep{LouieEtAl2025}.
```
Proposed:
```latex
In this section, I follow the chain of steps that turns the raw detector data into a transmission spectrum, to show where errors could enter. All three reductions of WASP-17~b used the same basic chain \citep{LouieEtAl2025}.
```
Reason: The subsection is long (about 1.5 pages) and starts with no purpose stated. One signpost sentence links it to the opening of the Introduction and to the title of 1.4. It also changes "reductions used for WASP-17~b" to the report's usual "reductions of WASP-17~b". A minimal alternative is to make only that change.

### intro-B-304: 01_introduction.tex:304 · grammar · impact 1

Current:
```latex
In Ahsoka and supreme-SPOON, the images are then flat-field corrected with the JWST pipeline.
```
Proposed:
```latex
In Ahsoka and supreme-SPOON, the count-rate images were first flat-field corrected with the JWST pipeline.
```
Reason: "Then" dangles after a sentence that only points to the figure. The sentence also describes two specific reductions, so it should be in the past tense like the rest of the paragraph ("Ahsoka ... used"). "First" orders it within the steps of Figure 3b.

### intro-B-309: 01_introduction.tex:309 · cut · impact 1

Current:
```latex
then flagged and replaced. 
Ahsoka, for example, used the bad-pixel step of supreme-SPOON. This step
flags a pixel of the median out-of-transit image if its value is negative or
undefined. It also flags a pixel that differs from the nearby pixels in its
column by more than five standard deviations. Each flagged pixel is given the
median value of the surrounding pixels \citep{LouieEtAl2025}.
```
Proposed:
```latex
then flagged and replaced \citep{LouieEtAl2025}.
```
Reason: This is an optional cut. These four sentences give thresholds of a step that is not about background or extraction and never returns. Ahsoka's use of the supreme-SPOON bad-pixel step is stated again at 515. Cutting them shortens a long subsection. See the question below in case the negative-pixel rule is meant to matter later.

### intro-B-338: 01_introduction.tex:338 · flow · impact 1

Current:
```latex
pixels combined in extraction and the treatment of limb darkening. A further
choice is the model of slow instrumental trends in the light curves, meaning
```
Proposed:
```latex
pixels combined in extraction, the treatment of limb darkening and the model of slow instrumental trends in the light curves, meaning
```
Reason: "Examples are ... Other choices are ... A further choice is ..." spreads one list over three sentences and reads mechanically. Two sentences are enough.

### intro-B-343: 01_introduction.tex:343 · clarity · impact 1

Current:
```latex
Both scaled the background model separately
```
Proposed:
```latex
Both reductions scaled the background model separately
```
Reason: "Both" refers back three sentences, past a "they" and a passive sentence about the background, so for a moment its referent is unclear.

### intro-B-352: 01_introduction.tex:352 · clarity · impact 1

Current:
```latex
Ahsoka, which used Eureka! \citep{BellEtAl2022} for its light-curve fits, fitted a linear trend in time together with
the transit model for each light curve, and scaled the expected noise by a
fitted factor.
```
Proposed:
```latex
Ahsoka used Eureka! \citep{BellEtAl2022} to fit each light curve with the transit model and a linear trend in time, and scaled the expected noise by a fitted factor.
```
Reason: The "which" clause delays the verb, and the sentence says "fits ... fitted ... fitted". The new version keeps the same content in a direct order.

### intro-B-365: 01_introduction.tex:365 · repetition · impact 2

Current:
```latex
The subtracted background and the extracted spectra are therefore both fixed before the transit fit begins, and the transit fit does not model any background that remains.
```
Proposed:
```latex
The subtracted background and the extracted spectra are therefore both fixed before the transit fit begins.
```
Reason: Section 1.4 opens three lines later with the same clause ("Any background that remains after the subtraction is not modelled in the transit fit"), so the end of 1.3 and the start of 1.4 say the same thing back to back. The clause is better kept in 1.4, where it leads to its consequence.

### intro-B-372: 01_introduction.tex:372 · repetition · impact 1

Current:
```latex
remains in the data after the subtraction. If the residual background is
```
Proposed:
```latex
remains in the data. If this background is
```
Reason: "After the subtraction" repeats the sentence two lines earlier, and "residual background" comes twice in consecutive sentences.

### intro-B-378: 01_introduction.tex:378 · repetition · impact 2

Current:
```latex
In all three reductions of WASP-17~b,
the background was subtracted before the light curves were fitted, and the
transit fit held the subtracted background fixed \citep{LouieEtAl2025}. The
transit fit therefore could not correct an error in the subtraction.
```
Proposed:
```latex
In all three reductions of WASP-17~b, the transit fit held the subtracted background fixed \citep{LouieEtAl2025}, so it could not correct an error in the subtraction.
```
Reason: "Subtracted before the light curves were fitted" is the third time in about fifteen lines that this point is made (364-365, 370-371). The fix keeps the cited fact (background held fixed) and the consequence in one sentence.

### intro-B-427: 01_introduction.tex:427 · repetition · impact 2

Current:
```latex
afterwards \citep{LouieEtAl2025}. The transit therefore could not help to
separate the starlight from the background.
```
Proposed:
```latex
afterwards \citep{LouieEtAl2025}.
```
Reason: This repeats the end of the JExoRES paragraph almost word for word ("The transit therefore cannot help JExoRES to decide..."). The next paragraph then states it a third time ("Neither JExoRES nor ATOCA ... fits the background and the transit together"). The supreme-SPOON example already makes the point.

### intro-B-490: 01_introduction.tex:490 · flow · impact 1

Current:
```latex
For example, NIRSpec measured the $3$-$5\,\mu\mathrm{m}$ spectrum of
WASP-39~b. For these data, differences between reductions changed the
```
Proposed:
```latex
For example, differences between reductions of the 3 to $5\,\mu\mathrm{m}$ NIRSpec spectrum of WASP-39~b changed the
```
Reason: This merges a scene-setting sentence into the sentence it serves and removes the double "For" opening. It also writes the range as "3 to 5", as Sections 3 and 4 do, instead of a LaTeX hyphen (see cross-section note).

### intro-B-497: 01_introduction.tex:497 · clarity · impact 2

Current:
```latex
None found evidence of an atmosphere, but two showed
weak candidate absorption features at different wavelengths, which retrievals
assigned to different gases, and the authors concluded that the features were not real astrophysical signals.
```
Proposed:
```latex
None found evidence of an atmosphere. Two, however, showed weak candidate absorption features at different wavelengths, which retrievals assigned to different gases. The authors concluded that these features were not real astrophysical signals.
```
Reason: This is a 40-word sentence with four stacked clauses ('but ... which ... and'), and the authors' conclusion is buried at the end. Three sentences read correctly on the first pass.

### intro-B-500: 01_introduction.tex:500 · repetition · impact 2

Current:
```latex
disagreement of this kind shows that a result depends on the reduction. It
does not show which reduction, if any, recovered the true spectrum.
```
Proposed:
```latex
disagreement of this kind does not show which reduction, if any, recovered the true spectrum.
```
Reason: Line 489-490 has just said that disagreement shows dependence on the analysis ("When the reductions disagree, the spectrum is shown to depend on the analysis"). Only the second half adds anything.

### intro-B-507: 01_introduction.tex:507 · repetition · impact 2

Current:
```latex
Each subtracted the background from
the images and extracted a spectrum before it fitted the transit. They also
```
Proposed:
```latex
They also
```
Reason: This restates the definition of "extraction-first order" that the same sentence has just cited (Section 1.3), where it is spelled out at 362-365. Dropping it lets the paragraph get to the shared software sooner.

### intro-B-514: 01_introduction.tex:514 · cut · impact 1

Current:
```latex
Science Institute (STScI), although
```
Proposed:
```latex
Science Institute, although
```
Reason: The abbreviation STScI is defined here but never used again anywhere in the report.

### intro-B-520: 01_introduction.tex:520 · repetition · impact 2

Current:
```latex
they could also share an error. Their agreement could not reveal an error common to all three. Leaving any remaining background out of the transit fit could cause exactly such a shared error.
```
Proposed:
```latex
they could also share an error, and their agreement could not reveal it. Leaving any remaining background out of the transit fit could cause such a shared error.
```
Reason: "Could not reveal an error common to all three" restates "share an error" from the previous clause. "Exactly" is emphasis with no work to do. Three "could"s in a row become two.

### intro-B-522: 01_introduction.tex:522 · AI tell · impact 3

Current:
```latex
Crucially, a good fit to the extracted light curves does not show that the
```
Proposed:
```latex
A good fit to the extracted light curves does not show that the
```
Reason: "Crucially" is on the banned list, and style_check flags it. The sentence makes its point without the intensifier.

### intro-B-525: 01_introduction.tex:525 · grammar · impact 1

Current:
```latex
light curve, however, still has the shape of a transit, so it can still be
```
Proposed:
```latex
light curve, however, keeps the shape of a transit, so it can still be
```
Reason: "still ... still" in one sentence.

### intro-B-530: 01_introduction.tex:530 · clarity · impact 1

Current:
```latex
Historically, known test signals have been supplied in two ways.
```
Proposed:
```latex
Earlier studies have supplied known test signals in two ways.
```
Reason: "Historically" reads oddly when the examples that follow are from 2022 to 2026, and it is also a slightly grand opener.

### intro-B-538: 01_introduction.tex:538 · grammar · impact 1

Current:
```latex
also used simulated data, to study how the steps that
```
Proposed:
```latex
also used simulated data to study how the steps that
```
Reason: The comma before a purpose clause makes it look like an afterthought.

### intro-B-563: 01_introduction.tex:563 · flow · impact 1

Current:
```latex
rates. Measured light has also been injected into real observations in a
```
Proposed:
```latex
rates.

Measured light has also been injected into real observations in a
```
Reason: The paragraph turns to a different field (direct imaging) mid-way and runs to about 170 words. A paragraph break helps the reader, and the data-challenge paragraph uses the same pattern.

### intro-B-592: 01_introduction.tex:592 · consistency · impact 1

Current:
```latex
complete pipelines should recover the spectrum, and each should learn the
injected truth only after it has delivered its final result.
```
Proposed:
```latex
complete pipelines should recover the spectrum, each without knowing the injected truth until it has delivered its final result.
```
Reason: A pipeline that "learns" reads as personification, and "learn" also suggests machine learning. Sections 3 and 4 use "without knowing" and "without knowledge of" the truth.

### intro-B-594: 01_introduction.tex:594 · clarity · impact 1

Current:
```latex
studies above combines these four things.
```
Proposed:
```latex
studies above combines all four.
```
Reason: "Things" is vague right after a paragraph that calls them needs.

### intro-B-601: 01_introduction.tex:601 · flow · impact 1

Current:
```latex
The second need is difficult to meet. A transit dims only the starlight. An
injector, the tool that adds the transit to the data, must therefore know
```
Proposed:
```latex
The second need is difficult to meet. Because a transit dims only the starlight, an injector, the tool that adds the transit to the data, must know
```
Reason: "A transit dims only the starlight" has already been stated at 370, 442 and 474. As a separate short sentence it reads like a dramatic beat. Folded in as the reason, it does its job without standing out.

### intro-B-609: 01_introduction.tex:609 · consistency · impact 2

Current:
```latex
outside the extraction aperture, the band of pixels that is combined into the spectrum, also called the extraction box.
```
Proposed:
```latex
outside the extraction box, the band of pixels that is combined into the spectrum.
```
Reason: Two names for one thing are joined by an "also called" patch. Sections 3 and 4 use only "extraction box". In Section 2, "apertures" are NOVA's fitted pixel regions, so "aperture" for the extraction box is also confusing there. The same fix applies at line 613.

### intro-B-613: 01_introduction.tex:613 · consistency · impact 1

Current:
```latex
aperture \citep{VolkEspinoza2023}.
```
Proposed:
```latex
extraction box \citep{VolkEspinoza2023}.
```
Reason: This follows from intro-B-609, so one name is used for the extraction box. Line 609 already equates the two names, so the meaning is unchanged.

### intro-B-616: 01_introduction.tex:616 · repetition · impact 1

Current:
```latex
the difference between the two exposures measures the light of the star. This
difference greatly reduces
```
Proposed:
```latex
the difference between the two exposures measures the light of the star. This
measurement greatly reduces
```
Reason: "Difference" appears four times in four consecutive sentences (616, 617, 618, 619). Varying the second one removes the echo without changing the meaning.

### intro-B-618: 01_introduction.tex:618 · consistency · impact 1

Current:
```latex
I will build the benchmark from this
difference
```
Proposed:
```latex
I am building the benchmark from this
difference
```
Reason: The next two sentences are in the present tense ("I first turn", "I then dim"), so "will build" jars. The abstract ("I am therefore building") and Section 4 ("The benchmark I am now building") use the progressive.

### intro-B-619: 01_introduction.tex:619 · consistency · impact 1

Current:
```latex
I first turn the difference into a clean image of the star
```
Proposed:
```latex
I first turn the difference into a cleaned image of the star
```
Reason: The abstract and Section 4 use "cleaned image of the star" as the fixed term.

### intro-B-619b: 01_introduction.tex:619 · consistency · impact 1

Current:
```latex
smoothing the faint outer wings.
```
Proposed:
```latex
smoothing the faint far wings.
```
Reason: Section 4 calls this region "the far wings" throughout, including the figure captions and "far-wing model".

### intro-B-622: 01_introduction.tex:622 · consistency · impact 2

Current:
```latex
apply the transit to the constructed image
```
Proposed:
```latex
apply the transit to the cleaned image
```
Reason: The paragraph has already called this a "clean image" (619), and the abstract and Section 4 call it "the cleaned image of the star". "Constructed image" is a third name, and a reader may take it for a different object.

### intro-B-636: 01_introduction.tex:636 · clarity · impact 3

Current:
```latex
biases that fitting the transit without a background term, and extracting a spectrum first, can cause?
```
Proposed:
```latex
biases that can arise from extracting a spectrum first and fitting the transit without a background term?
```
Reason: In the current version the verb "can cause" comes only after two comma-fenced gerund phrases, so the question has to be read twice. The fix puts the verb first and lists the two causes in pipeline order. Meaning and scope ("can") are unchanged.

### intro-B-644: 01_introduction.tex:644 · consistency · impact 1

Current:
```latex
adds a known transit to the detector reads of
```
Proposed:
```latex
adds a known transit to the raw reads of
```
Reason: Everywhere else the report says "raw reads" (lines 590, 620, Sections 3 and 4, abstract).

### intro-B-653: 01_introduction.tex:653 · clarity · impact 2

Current:
```latex
I will switch off its parts one at a time and measure how
  the recovery changes, to find out which of them an accurate spectrum
  needs.
```
Proposed:
```latex
I will find out which of its parts are needed for an accurate spectrum, by switching them off one at a time and measuring how the recovery changes.
```
Reason: "Which of them an accurate spectrum needs" is inverted and ends the objective weakly. The fix states the goal first and the method second, which follows the style rule of why before how. Meaning is unchanged.

### Paragraph rewrites (Introduction, lines 230–665 (§1.3–§1.6))

**01_introduction.tex, lines 370-384**, starting "The first step is the treatment of the background. Any background that remains"

```latex
The first step is the treatment of the background. Any background that remains after the subtraction is not modelled in the transit fit, so it could bias the transit depth. The background adds light to the image, whereas the transit dims only the starlight. Suppose that some steady residual background remains in the data. If this background is counted as starlight, the star appears brighter than it is. The light blocked by the planet is then a smaller fraction of the total, and the transit comes out too shallow. Removing too much light as background has the opposite effect and makes the transit too deep. An error that varies across the detector changes the depth by different amounts at different wavelengths, and so changes the shape of the spectrum. In all three reductions of WASP-17~b, the transit fit held the subtracted background fixed \citep{LouieEtAl2025}, so it could not correct an error in the subtraction. The reductions also report one uncertainty per wavelength channel. A single number per channel cannot describe how one background error moves neighbouring channels up or down together.
```
Reason: This combines intro-B-372 and intro-B-378 so the paragraph can be read whole. It removes the repeated "after the subtraction" and "residual background", and the third statement in a page that the background was subtracted before the fit. Every fact and citation is kept.

**01_introduction.tex, lines 417-428**, starting "The second method, ATOCA, addresses the overlap of the orders."

```latex
The second method, ATOCA, addresses the overlap of the orders. It models every pixel as the sum of the light of both orders. Because the two orders are copies of the same stellar spectrum, one spectrum has to explain both, so ATOCA can separate the two orders during the extraction \citep{DarveauBernierEtAl2022}. It needs the profile of each order across the detector, and the APPLESOSS package can estimate these profiles from the observation itself \citep{RadicaEtAl2022}. Like JExoRES, however, ATOCA still extracts the spectrum before the transit is fitted. In the supreme-SPOON reduction of WASP-17~b, for example, the background was subtracted before the ATOCA extraction, and the transit was fitted to the extracted light curves afterwards \citep{LouieEtAl2025}.
```
Reason: Four consecutive sentences currently begin with "ATOCA". The closing sentence repeats the JExoRES paragraph, and the next paragraph's opener makes the point again (intro-B-427). Content and citations are unchanged.

**01_introduction.tex, lines 601-610**, starting "The second need is difficult to meet. A transit dims only the starlight."

```latex
The second need is difficult to meet. Because a transit dims only the starlight, an injector, the tool that adds the transit to the data, must know which part of the recorded light belongs to the star. For this, the injector needs an image of the star on the detector. My first injectors took this image from the WASP-17~b data themselves. These data, however, cannot show how much of the faint light in the wings of the traces comes from the star (Section~\ref{sec:benchmark}). The commissioning study of SOSS met a related limit. It could not determine how much of the light of a star falls outside the extraction box, the band of pixels that is combined into the spectrum. Neither the commissioning data nor WebbPSF, the software that models how JWST images a star, could provide this fraction \citep{AlbertEtAl2023}.
```
Reason: This folds the repeated "a transit dims only the starlight" into a reason, replaces "That study" with "It", and settles on one name, "extraction box", in place of "extraction aperture ... also called the extraction box".

**01_introduction.tex, lines 612-625**, starting "Calibration programme 4476 was designed to measure the light outside the"

```latex
Calibration programme 4476 was designed to measure the light outside the extraction box \citep{VolkEspinoza2023}. In a SOSS time series, only a strip of the detector is read out. Programme 4476 observed a star at its usual position on this strip, and then again with the star moved off the strip. On the strip, the difference between the two exposures measures the light of the star. This measurement greatly reduces the need to split the observed light into starlight and background with a fit. I am building the benchmark from this difference (Section~\ref{sec:measured-benchmark}). I first turn it into a cleaned image of the star, by removing the field sources (field stars and any other objects in the field) and smoothing the faint far wings. I then dim this image with a known transit and add it to the raw reads of the exposure in which the star was moved off the strip. The noise, the background and the field stars of that exposure are real. Because I apply the transit to the cleaned image myself, the injected signal will be known exactly for that image. The benchmark is designed to show whether the established pipelines recover a known transit without a detectable bias, and whether NOVA improves on them.
```
Reason: This combines intro-B-613, 616, 618, 619, 619b and 622. "Difference" no longer appears four times in four sentences, the image has one name ("cleaned image") as in the abstract and Section 4, the wings are "far wings" as in Section 4, and the tense sequence ("will build" / "turn" / "will be known") becomes consistent. "Will be known" is kept because the benchmark is not yet built.

### Notes across sections

- The point that the background is subtracted before the transit fit, so the fit cannot correct it, is made at intro 7, 357-360, 364-365, 370-371, 378-381, 413-415, 424-428, 430-432, 507-508 and 520. My items cut three of these (365 clause, 378-381, 427-428, 507-508). The others are each doing distinct work.
- "For a real planet, the true spectrum is unknown" opens 1.5 (line 487). Section 3 opens with almost the same sentence ("For a real planet the true spectrum is unknown."), and the idea is also at intro 13-14 and the abstract. Section 3's opener could point back to 1.5 instead of restating it.
- The roadmap at 658-659 ("Section 2 describes NOVA as it is currently implemented and ends with a first, preliminary spectrum of WASP-17~b") is repeated almost word for word in the last sentence of the Section 2 opener.
- The flat field is defined twice: at line 140 ("the map of each pixel's sensitivity") and again at 304-306 ("a reference image of how sensitive each pixel is relative to the others"). The second could be shortened to a reminder.
- "Where the two orders overlap, their light must be separated" appears at 170-171 and again at 404-405.
- Wavelength ranges are written with a LaTeX hyphen ($0.6$-$2.8\,\mu\mathrm{m}$) at intro 109, 110, 123, 135, 197 and 490, but as "0.85 to 1.75" in Sections 3 and 4. Pick one style for the whole report; the hyphen is typographically wrong for a range, and an en dash or "to" would be right.
- "data set" in Section 2 (lines 10, 12, 120, 207, 221, 222, 274) vs "dataset" in intro 581 and Section 4 line 237.
- Geometry is called "transit geometry" in intro 475, "orbital geometry" in Section 2 (lines 12, 273), and "white-light geometry" in the Section 2.8 heading.
- "Extraction aperture"/"aperture" (intro 609, 613) vs "extraction box" (Sections 3, 4). Section 2 uses "apertures" for NOVA's own fitted pixel regions, which makes "aperture" for the extraction box doubly confusing.
- "Clean image" (619) and "constructed image" (622) vs "cleaned image" (abstract, Section 4); "outer wings" (619) vs "far wings" (Section 4).
- The background left after subtraction is variously "residual background", "background that remains", "remaining background" and "background left" (intro), and "background left after Stage~2" in Section 2. These are clear in context, but "residual background" could be the default after its first use.
- Ahsoka's use of Eureka! is stated at 352 and 518. Ahsoka's use of the supreme-SPOON bad-pixel step is stated at 310 and 515.
- Figure 3a draws six groups (G1-G6), while line 256 says each WASP-17~b integration had eight groups (and Section 4 says programme 4476 had five). That is fine for a schematic, but a careful examiner may notice it.

### Questions for Davide (would change meaning, so not proposed as replacements)

- Is the detailed supreme-SPOON bad-pixel rule at 310-314 (negative or undefined pixels of the median image, five standard deviations, median replacement) there for a reason, for example a planned link to negative faint-light pixels? If not, I suggest cutting it (intro-B-309). It is the one place in 1.3 where detail does not serve the background/extraction story.
- Research question (intro-B-636): may the two causes be swapped into pipeline order ("extracting a spectrum first and fitting the transit without a background term")? The meaning is unchanged, but this is the RQ, so I am asking explicitly.
- Line 304 says only Ahsoka and supreme-SPOON were flat-field corrected with the JWST pipeline, and line 511 says transitspectroscopy started from archive count-rate files. An examiner may ask whether transitspectroscopy applied a flat field at all. If it did so by other means, a few words would close the question.
- 1.3 opener (intro-B-250): are you happy with an 'In this section, I ...' signpost here? The minimal alternative is to change only 'reductions used for WASP-17~b' to 'reductions of WASP-17~b'.

### Possible errors noticed in passing

- Figure 3a shows six reads (G1-G6), whereas line 256 states eight groups per WASP-17~b integration. As a schematic this is not wrong, but the caption does not say 'schematic'.
- Line 304 implies transitspectroscopy did not flat-field (only Ahsoka and supreme-SPOON are named). Worth checking against Louie et al. 2025, since archive rateints files are Stage 1 products and are not flat-fielded.

## Section 2 (NOVA)

**How it reads now.** Section 2 is the most technical part of the report, and most of it reads well. Sentence lengths are close to the targets (median 21 words, 10% over 35 words), most paragraphs give the reason before the method, and each equation is followed by its definitions. The problems are local. Two later additions break the flow: the field-star sentences were inserted into the middle of the background-map paragraph, so "these pixels" in the next sentence no longer clearly refers back to the off-trace pixels, and Eq. 8 still ends with a comma left over from an earlier version that had a "where" clause after it. Several sentences send the reader down the wrong path on first reading or contain a dangling modifier: the list of columns that are left out, the double appositive that defines the limb-darkening deviation, and "After interpolating ..., NOVA is deeper". Some terms are used before they are defined, or appear under two names: "continuum", "sample", u1/u2, "noise scale"/"factor", "WASP-17 visit"/"WASP-17 b visit", and DN/s against DN s^-1. A few passives with no agent ("has not been tested") hide who did what. Colons (3.2 per 1000 words) and commas (67 per 1000 words) are still slightly above target.

### nova-11: 02_nova.tex:11 · consistency · impact 2

Current:
```latex
a noise scale for each
pixel and the orbital geometry. The others are the same for every data set:
the depth bins, the limb-darkening reference, the apertures, the background
maps and two noise scales.
```
Proposed:
```latex
a noise factor for each
pixel and the orbital geometry. The others are the same for every data set:
the depth bins, the limb-darkening reference, the apertures, the background
maps and a noise factor for each order.
```
Reason: At this point the reader cannot know what 'two noise scales' are, as opposed to 'a noise scale for each pixel'. Section 2.5 calls them 'the factor N_p' (one per order) and 'the factor s_p'. Using 'factor' in both places and saying 'for each order' makes the list clear and the terms consistent.

### nova-14: 02_nova.tex:14 · repetition · impact 2

Current:
```latex
In this section, I describe NOVA as it is currently
implemented, and end with a first, preliminary spectrum of WASP-17~b.
```
Proposed:
```latex
In this section, I describe NOVA as it is currently
implemented, part by part, and then compare its first, preliminary spectrum of WASP-17~b with the published Ahsoka spectrum.
```
Reason: The roadmap at the end of the Introduction (01:658-659) says almost word for word 'describes NOVA as it is currently implemented and ends with a first, preliminary spectrum of WASP-17 b', and on PDF page 11 the two sentences are about 20 lines apart. Keeping the scope phrase 'as it is currently implemented' but changing the second half removes the echo and tells the reader what Section 2.9 actually does. An alternative is to shorten the roadmap sentence in the Introduction instead.

### nova-23: 02_nova.tex:23 · clarity · impact 2

Current:
```latex
To estimate it, the step subtracts from the group the median out-of-transit
image, scaled by a light curve measured from the data, and takes the median of
what is left in each column outside the trace cores, leaving out field stars
found in a separate exposure through the F277W filter. It then subtracts this
column offset from the original group. For this step only, it subtracts a
scaled background model beforehand and adds it back afterwards.
```
Proposed:
```latex
To estimate this noise, it subtracts from the group the median out-of-transit
image, scaled by a light curve measured from the data. It then takes the median of
what is left in each column outside the trace cores, leaving out field stars
found in a separate exposure through the F277W filter, and subtracts this
column offset from the original group. For this step only, a scaled background model is subtracted beforehand and added back afterwards.
```
Reason: The first sentence is 44 words long and joins three actions with 'and' and a participle. 'The step' has no antecedent, since the previous sentence names exoTEDRF, not a step. In 'it subtracts a scaled background model ... and adds it back', the two 'it's refer to different things. Splitting the sentence and making the last one passive solves all three problems without changing any fact.

### nova-52: 02_nova.tex:52 · clarity · impact 3

Current:
```latex
Four edge columns, the 51 reddest columns of
order~1 (Section~\ref{sec:transit}) and flagged samples are left out.
```
Proposed:
```latex
I leave out four edge columns, the 51 reddest columns of
order~1 (Section~\ref{sec:transit}) and flagged samples, where a sample is one pixel in one integration.
```
Reason: In the current sentence, 'Four edge columns, the 51 reddest columns of order 1' first reads as an apposition (as if the four edge columns were the 51 reddest columns). The reader only sees that it is a list when the verb arrives at the end. Starting with the verb signals a list. 'Sample' is used later ('each sample has the uncertainty', 'for every fitted sample') but is never defined, and the indices t and p show that it means one pixel in one integration.

### nova-60: 02_nova.tex:60 · clarity · impact 1

Current:
```latex
in the group $g$ of pixel $p$,
```
Proposed:
```latex
in the group $g$ that contains pixel $p$,
```
Reason: 'The group g of pixel p' is hard to parse on first reading.

### nova-62: 02_nova.tex:62 · clarity · impact 2

Current:
```latex
$\bar{\mathcal{T}}_{tg}$ is the dimming of
the group's light by the transit
```
Proposed:
```latex
$\bar{\mathcal{T}}_{tg}$ is the fraction of
the group's light that the transit leaves
```
Reason: T-bar multiplies the starlight and equals one out of transit. 'The dimming' would naturally mean 1 - T-bar, which a physicist examiner may notice. The new wording describes the same quantity precisely and matches Section 4's r_p(t).

### nova-63: 02_nova.tex:63 · clarity · impact 2

Current:
```latex
$\gamma_t$ is a small,
fixed curvature of the baseline
```
Proposed:
```latex
$\gamma_t$ is a fixed factor,
close to one, for a slight curvature of the baseline
```
Reason: gamma_t is a multiplicative factor close to one (Section 2.5 says so). Calling it 'small' suggests that the starlight term is small. The new wording keeps 'fixed' and the idea of slight curvature.

### nova-88: 02_nova.tex:88 · consistency · impact 2

Current:
```latex
100~DN/s of starlight therefore dims by only about 1.5
to 2~DN/s during the transit
```
Proposed:
```latex
100~DN\,s$^{-1}$ of starlight dims by only about 1.5
to 2~DN\,s$^{-1}$ during the transit
```
Reason: Sections 3 and 4 write the unit as DN\,s$^{-1}$, and this is the only place that writes DN/s. Removing the first 'therefore' also avoids two 'therefore's in consecutive sentences ('therefore dims', 'is therefore noisy').

### nova-101: 02_nova.tex:101 · clarity · impact 2

Current:
```latex
It combines three public calibration
products: the PASTASOSS trace and wavelength calibration, which says where
each wavelength falls on the detector
\citep{BainesEtAl2023Trace,BainesEtAl2023Wavelength}; the line-spread kernel,
which spreads the light of one wavelength over a few neighbouring columns; and
the throughput, which says how much of the light at each wavelength is
detected. NOVA combines them with ATOCA
```
Proposed:
```latex
It combines three public calibration
products. The PASTASOSS trace and wavelength calibration says where
each wavelength falls on the detector
\citep{BainesEtAl2023Trace,BainesEtAl2023Wavelength}. The line-spread kernel
describes how the light of one wavelength spreads over a few neighbouring columns, and
the throughput says how much of the light at each wavelength is
detected. NOVA builds $K_{g\lambda}$ from these products with ATOCA
```
Reason: One sentence carries a colon, two semicolons and three 'which' clauses. It is then followed by 'NOVA combines them', which repeats 'combines' from the sentence before. Splitting it removes the colon, both semicolons and all three 'which's. 'Describes how the light ... spreads' is also more precise, because a calibration product does not itself spread light.

### nova-110: 02_nova.tex:110 · clarity · impact 2

Current:
```latex
The group is therefore dimmed by the transit at the wavelengths
of its column,
```
Proposed:
```latex
The fraction of a group's light that the transit leaves is therefore the mean of the transit light curve over the wavelengths
of its column, weighted by the light that each wavelength contributes,
```
Reason: The current sentence before the equation does not say what the equation computes. The new wording describes Eq. 4 in words (a mean of T_t(lambda) weighted by K s), so a non-specialist can read the fraction before reading the symbols. It also matches the wording proposed for T-bar in Section 2.2 and Section 4's definition of r_p(t) ('the fraction of the star's light that remains').

### nova-123: 02_nova.tex:123 · clarity · impact 2

Current:
```latex
It
is represented by 160 top-hat bins from 0.62 to $2.84\,\mu\mathrm{m}$. Below
$2\,\mu\mathrm{m}$ the bins are about $0.01\,\mu\mathrm{m}$ wide and above it
$0.038\,\mu\mathrm{m}$, wider in the red, where the signal-to-noise ratio is
lower.
```
Proposed:
```latex
The spectrum
is represented by 160 top-hat bins from 0.62 to $2.84\,\mu\mathrm{m}$. The bins are about $0.01\,\mu\mathrm{m}$ wide below
$2\,\mu\mathrm{m}$ and $0.038\,\mu\mathrm{m}$ wide above it, in the red, where the signal-to-noise ratio is
lower.
```
Reason: 'It' could refer to the planet or to D(lambda). 'And above it 0.038 um, wider in the red, where ...' piles up three short phrases. The new wording keeps every number and the reason for the wider bins.

### nova-128: 02_nova.tex:128 · clarity · impact 2

Current:
```latex
The two reddest bins receive no light in the model: order~2 does
not reach them, and order~1 is cut at $2.758\,\mu\mathrm{m}$, beyond which
this calibration would have to be extrapolated.
```
Proposed:
```latex
The two reddest bins receive no light in the model, because order~2 does
not reach them and order~1 is cut at $2.758\,\mu\mathrm{m}$, beyond which
the PASTASOSS calibration would have to be extrapolated.
```
Reason: The colon introduces a reason, so 'because' is plainer and lowers the colon count, which is above target. 'This calibration' could mean K as a whole or PASTASOSS. The cut is set by the PASTASOSS support, so naming it is clearer. Davide should check that PASTASOSS is the intended referent.

### nova-138: 02_nova.tex:138 · clarity · impact 1

Current:
```latex
where $\bar D$ is the overall, achromatic depth and $w_k$ are the bin widths,
```
Proposed:
```latex
where $D_j$ is the depth in bin $j$, $\bar D$ is the overall, achromatic depth and $w_k$ are the bin widths,
```
Reason: D_j and the bin index j are never stated, although the rest of the equation is defined. This is a small addition for completeness.

### nova-154: 02_nova.tex:154 · repetition · impact 1

Current:
```latex
transit is computed with jaxoplanet
```
Proposed:
```latex
transit light curve is evaluated with jaxoplanet
```
Reason: 'Computed' appears in two consecutive sentences ('all computed from NOVA's white-light fit', 'The transit is computed'). The first one is deliberate, because b is derived from the fit. 'Transit light curve' is also more precise.

### nova-161: 02_nova.tex:161 · clarity · impact 2

Current:
```latex
u_2=\sqrt{q_1}\,(1-2q_2).
 \label{eq:kipping-coordinates}
\end{equation}
Limb darkening
```
Proposed:
```latex
u_2=\sqrt{q_1}\,(1-2q_2),
 \label{eq:kipping-coordinates}
\end{equation}
where $u_1$ and $u_2$ are the coefficients of the quadratic law. Limb darkening
```
Reason: u1 and u2 are never defined, but they appear again in the priors of Section 2.7. Every other equation in the section is followed by a 'where' clause for its new symbols.

### nova-166: 02_nova.tex:166 · clarity · impact 3

Current:
```latex
In order $o$, the logit of each
coordinate $q_c$ is its reference value plus a deviation
$\delta_{oc}(\lambda)=a_{oc}+b_{oc}\,\ell_o(\lambda)$, an offset and a slope in
$\ell_o$, the logarithm of wavelength centred on the order and scaled to a
largest magnitude of one.
```
Proposed:
```latex
In order $o$, the logit of each
coordinate $q_c$ is its reference value plus a deviation
$\delta_{oc}(\lambda)=a_{oc}+b_{oc}\,\ell_o(\lambda)$, with an offset $a_{oc}$ and a slope $b_{oc}$. Here $\ell_o$ is the logarithm of wavelength, centred on the order and scaled so that its largest magnitude is one.
```
Reason: Two appositives follow one another ('..., an offset and a slope in l_o, the logarithm of wavelength centred ...'), so on first reading it is unclear what each phrase describes. 'Scaled to a largest magnitude of one' is also awkward. Splitting the sentence names each symbol explicitly and reads correctly the first time.

### nova-175: 02_nova.tex:175 · consistency · impact 2

Current:
```latex
The brightness of the star in each group is a straight line in time,
```
Proposed:
```latex
The continuum, the brightness of the star in each group, is a straight line in time,
```
Reason: 'Continuum' appears in the title of Section 2.5, in Figure 4 ('continuum C_tg') and in Section 2.6 ('continuum coefficients beta'), but the text never says that it means C_tg. A spectroscopist would read 'continuum' as the part of a spectrum without lines. Defining it once where C_tg is described removes the question.

### nova-179: 02_nova.tex:179 · repetition · impact 2

Current:
```latex
A curvature is harder
than a straight line to measure from the integrations before and after the
transit,
```
Proposed:
```latex
A curvature is harder
to measure than a straight line from these integrations,
```
Reason: Splitting the comparison ('harder than a straight line to measure') is awkward. 'The integrations before and after the transit' was used two sentences earlier, and 'out-of-transit data' follows in the next sentence, so the phrase appears three times in four sentences.

### nova-186: 02_nova.tex:186 · grammar · impact 2

Current:
```latex
as a factor close to one. $\gamma_t$ is the geometric mean
```
Proposed:
```latex
as a factor close to one. In the detector model, $\gamma_t$ is the geometric mean
```
Reason: In printed text a sentence should not start with a symbol. The added phrase also links gamma_t back to Eq. 2, which the reader last saw two pages earlier.

### nova-193: 02_nova.tex:193 · clarity · impact 1

Current:
```latex
an amplitude that follows one time
pattern $G(t)$,
```
Proposed:
```latex
an amplitude that follows one time
pattern $G(t)$, shared by all maps,
```
Reason: 'One time pattern' can be read as one pattern per map. Eq. 7 shows that G has no index k, so this states what the equation already shows.

### nova-200: 02_nova.tex:200 · flow · impact 3

Current:
```latex
Field stars are also left out of the $1/f$ correction (Section~\ref{sec:detector-processing}), but NOVA does not yet treat field-star light that falls on the traces, which it cannot tell apart from the light of the target. A treatment of such light, for example with the positions of field-star spectra that Gaia predicts (Section~\ref{sec:measuring-star}), is future work, needed for both the benchmark and the WASP-17~b visit. The
maps are made orthonormal over these pixels. The maps and these pixels were
chosen once from the WASP-17 visit, where eight maps predicted held-out strips
of the off-trace image better than two or four. How well the maps
describe the background under the traces, and how much an error of the maps
there changes the depths, has not yet been tested.
```
Proposed:
```latex
The
maps are made orthonormal over these pixels. The maps and these pixels were
chosen once from the WASP-17~b visit, where eight maps predicted held-out strips
of the off-trace image better than two or four. I have not yet tested how well the maps
describe the background under the traces, or how much an error in the maps
there would change the depths.

Field stars are left out of the off-trace pixels and of the $1/f$ correction (Section~\ref{sec:detector-processing}), but NOVA does not yet treat field-star light that falls on the traces, which it cannot tell apart from the light of the target. A treatment of such light, for example with the positions of field-star spectra that Gaia predicts (Section~\ref{sec:measuring-star}), is future work, needed for both the benchmark and the WASP-17~b visit.
```
Reason: The two field-star sentences added on 9 October sit in the middle of the background-map paragraph. As a result, 'these pixels' in 'The maps are made orthonormal over these pixels' now follows a sentence about field stars on the traces, so the reader has to search three sentences back for the antecedent. This change moves the field-star sentences, otherwise unchanged, to the end as their own short paragraph. Because 'also' would then have nothing close to refer to, it is replaced by 'left out of the off-trace pixels and of', which says the same thing. If Davide wants the agreed wording kept exactly, keep 'Field stars are also left out of the $1/f$ correction' and drop the paragraph break. The change also fixes the agreement error ('How well ..., and how much ..., has' should be plural, or recast), uses active 'I have not yet tested', and corrects 'WASP-17 visit' to 'WASP-17~b visit'.

### nova-200a: 02_nova.tex:200 · repetition · impact 1

Current:
```latex
The 244,657 off-trace pixels, away from the traces, field stars and bad pixels, are assumed
```
Proposed:
```latex
Away from the traces, field stars and bad pixels, 244,657 off-trace pixels are assumed
```
Reason: 'Off-trace pixels, away from the traces' says the same thing twice, and 'The' presents the set as if it had already been introduced. Putting the location first defines the set.

### nova-209: 02_nova.tex:209 · clarity · impact 2

Current:
```latex
is their strongest principal component that does not look like the transit,
with an absolute correlation of at most 0.25. On the real visit,
```
Proposed:
```latex
is the strongest of their principal components whose absolute correlation
with the transit is at most 0.25. On the real WASP-17~b visit,
```
Reason: 'Does not look like the transit, with an absolute correlation of at most 0.25' states the criterion twice, once loosely and once exactly, and leaves out what the correlation is with. The new wording states the criterion once, exactly. 'The real visit' has not yet been named in Section 2, and Section 2.9 says 'the real WASP-17 b visit'.

### nova-218: 02_nova.tex:218 · clarity · impact 2

Current:
```latex
It was measured once on the WASP-17 visit, from
how well the model predicted held-out out-of-transit integrations, so it also
covers part of the model mismatch, treated as random noise. Measuring it again
with the current model, and for each data set, is future work.
```
Proposed:
```latex
It was measured once on the WASP-17~b visit, from
how well the model predicted out-of-transit integrations held out of the fit, so it also
absorbs part of the model mismatch, as if it were random noise. I still need to measure it again
with the current model, and for each data set.
```
Reason: 'Held-out out-of-transit' puts two 'out's next to each other. In 'treated as random noise', the clause dangles, since it is not clear who treats what. 'Is future work' appears twice in this subsection (also at the end of the field-star sentence). 'WASP-17 visit' becomes 'WASP-17~b visit' for consistency with the rest of the report. The meaning is unchanged.

### nova-237: 02_nova.tex:237 · grammar · impact 3

Current:
```latex
\right\rangle_{o}\right],
```
Proposed:
```latex
\right\rangle_{o}\right].
```
Reason: Eq. 8 ends with a comma, but no 'where' clause follows. The next sentence starts 'The first term ...', so the PDF shows '..., (8) The first term'. The comma is a leftover from the version that had a 'where' clause after the equation. The equation should end with a full stop.

### nova-245: 02_nova.tex:245 · AI tell · impact 2

Current:
```latex
which therefore do not
dominate. The second term is a background anchor.
```
Proposed:
```latex
which therefore do not
dominate the fit. The second term ties the background to the off-trace pixels.
```
Reason: 'Background anchor' is working jargon, of the same kind as 'gate' or 'firewall'. The new wording says what the term does, and the rest of the paragraph then explains how. 'Dominate' also needs an object.

### nova-250: 02_nova.tex:250 · grammar · impact 1

Current:
```latex
increase of the $\chi^2$ of those pixels
```
Proposed:
```latex
increase in the $\chi^2$ of those pixels
```
Reason: Idiom: one speaks of an 'increase in' a quantity. This also avoids 'of ... of'.

### nova-256: 02_nova.tex:256 · clarity · impact 1

Current:
```latex
The second limits the curvature of the
deviation in wavelength
```
Proposed:
```latex
The second limits the curvature $\delta''_{oc}$ of the
deviation in wavelength
```
Reason: delta'' appears in Eq. 8 but the prose never names it. This links the symbol to its description.

### nova-260: 02_nova.tex:260 · clarity · impact 1

Current:
```latex
nonlinear in 166 numbers:
```
Proposed:
```latex
nonlinear in 166 parameters:
```
Reason: 'Numbers' is vaguer than the standard term, and the next sentence then says 'the nonlinear ones'.

### nova-261: 02_nova.tex:261 · flow · impact 2

Current:
```latex
At every step, NOVA solves for the linear
coefficients exactly, by variable projection \citep{GolubPereyra1973}, and
the trust-region reflective method \citep{BranchColemanLi1999} adjusts the
nonlinear ones, with exact derivatives that use JAX for the transit model.
```
Proposed:
```latex
The trust-region reflective method \citep{BranchColemanLi1999} adjusts the
nonlinear parameters, using exact derivatives that JAX computes for the transit model. At every step of this method, NOVA solves for the linear
coefficients exactly, by variable projection \citep{GolubPereyra1973}.
```
Reason: 'At every step' comes before the reader knows which iteration has steps, and the sentence switches subject halfway through. Introducing the optimiser first makes 'every step' meaningful. 'Derivatives that use JAX' is odd, because derivatives do not use anything.

### nova-264: 02_nova.tex:264 · clarity · impact 1

Current:
```latex
The
Huber loss is minimised by reweighting. The weights
$w_{tp}=\min(1,\,1.345/|r_{tp}|)$ depend on the residuals, so they are
recomputed after each fit,
```
Proposed:
```latex
The
Huber loss is minimised by repeated reweighting. Each sample is given the weight
$w_{tp}=\min(1,\,1.345/|r_{tp}|)$. The weights depend on the residuals, so they are
recomputed after each fit,
```
Reason: 'The weights w_tp' appear without saying what they weight. Stating that each sample gets a weight, and that the process repeats, makes the iteration clear before the stopping rule.

### nova-274: 02_nova.tex:274 · clarity · impact 2

Current:
```latex
two orders of the same data set.
```
Proposed:
```latex
two orders, from the same data set as the spectral fit.
```
Reason: 'The same data set' leaves the reader asking 'the same as what?'. The point is that the geometry is NOVA's own, measured on the data it fits.

### nova-276: 02_nova.tex:276 · clarity · impact 2

Current:
```latex
Whether using
$q^\star_{pg}$ here instead would change the geometry has not been tested.
```
Proposed:
```latex
I have not tested whether using
$q^\star_{pg}$ as the profile instead would change the geometry.
```
Reason: The sentence opens with a long 'Whether ...' subject and has no agent. Active first person is easier to read, and the style rules ask for 'I' for what I did. Scope is unchanged (no 'yet' is added).

### nova-286: 02_nova.tex:286 · clarity · impact 1

Current:
```latex
accepted only if it gives little weight
```
Proposed:
```latex
accepted only if its posterior gives little weight
```
Reason: A fit does not 'give weight' to orbits. Its sampled posterior does, and the white-light fit is sampled with dynesty.

### nova-292: 02_nova.tex:292 · clarity · impact 2

Current:
```latex
I plan to estimate the uncertainty from the calibration products and the
geometry with an ensemble of simulated observations.
```
Proposed:
```latex
I plan to use an ensemble of simulated observations to estimate the uncertainty that the calibration products and the
geometry add to the spectrum.
```
Reason: 'Estimate the uncertainty from the calibration products' can be read as using the calibration products to estimate the uncertainty, when it means the uncertainty that they contribute. 'With an ensemble' is attached to the end of the sentence. Putting the method first and the contribution after it removes the ambiguity, and the next sentence ('conditional on the quantities held fixed') still follows logically.

### nova-312: 02_nova.tex:312 · clarity · impact 1

Current:
```latex
from a reduction of 18 September 2026
```
Proposed:
```latex
from a reduction made on 18 September 2026
```
Reason: 'A reduction of 18 September' can read as a reduction of data taken on that date.

### nova-316: 02_nova.tex:316 · grammar · impact 3

Current:
```latex
spectrum is deeper throughout. After interpolating the published spectrum to
the NOVA bins, NOVA is deeper by a median of about
```
Proposed:
```latex
spectrum is deeper at every wavelength. With the published spectrum interpolated to
the NOVA bins, the NOVA spectrum is deeper by a median of about
```
Reason: 'After interpolating ..., NOVA is deeper' is a dangling participle: NOVA did not do the interpolating, and 'NOVA' is a method, not a spectrum. 'Throughout' could be read as 'throughout the range below 1.8 um', the subject of the first half of the sentence. 'At every wavelength' is the wording of the abstract and Section 5, so this also makes the three places consistent. The meaning is unchanged.

### nova-323: 02_nova.tex:323 · flow · impact 1

Current:
```latex
because there the starlight is faintest
```
Proposed:
```latex
because the starlight is faintest there
```
Reason: Fronting 'there' sounds stilted. The plain word order reads more naturally.

### nova-325: 02_nova.tex:325 · consistency · impact 2

Current:
```latex
This is why I build the benchmark of the
next two sections, which measures the errors of each method against a known,
injected truth.
```
Proposed:
```latex
This is why I am building a benchmark, described in the
next two sections, that is designed to measure the errors of each method against a known,
injected truth.
```
Reason: 'I build' (simple present) reads oddly for work that is still in progress. The abstract says 'I am therefore building'. 'Which measures' presents the benchmark as already working. Sections 1 and 5 say it 'is designed to show' or 'is designed to measure', and the style rules forbid presenting an untested design as validated. Davide may prefer to keep 'measures'; see the questions.

### Paragraph rewrites (Section 2 (NOVA))

**02_nova.tex, lines 190-205**, starting "The background left after Stage~2 is modelled with eight fixed spatial maps:"

```latex
The background left after Stage~2 is modelled with eight fixed spatial maps:
the zodiacal-light model that Stage~2 subtracted, and seven smooth polynomials
in detector position ($1$, $y$, $x$, $xy$, $y^2$, $x^2$ and $xy^2$). Each map
$\Phi_{pk}$ has a constant amplitude and an amplitude that follows one time
pattern $G(t)$, shared by all maps,
\begin{equation}
 B_{tp}=\sum_{k=1}^{8}\Phi_{pk}
 \left[\alpha_{k0}+\alpha_{k1}\,G(t)\right].
 \label{eq:background-model}
\end{equation}
Away from the traces, field stars and bad pixels, 244,657 off-trace pixels are
assumed to see only background, although some starlight from the faint wings
of the traces may reach them (Section~\ref{sec:which-light}). The maps are
made orthonormal over these pixels. The maps and these pixels were chosen once
from the WASP-17~b visit, where eight maps predicted held-out strips of the
off-trace image better than two or four. I have not yet tested how well the
maps describe the background under the traces, or how much an error in the
maps there would change the depths.

Field stars are left out of the off-trace pixels and of the $1/f$ correction
(Section~\ref{sec:detector-processing}), but NOVA does not yet treat
field-star light that falls on the traces, which it cannot tell apart from the
light of the target. A treatment of such light, for example with the positions
of field-star spectra that Gaia predicts (Section~\ref{sec:measuring-star}),
is future work, needed for both the benchmark and the WASP-17~b visit.
```
Reason: This is the paragraph with items nova-193, nova-200a and nova-200 applied, shown so it can be read as a whole. Apply either the items or this rewrite, not both. The map description is now self-contained, so 'these pixels' clearly refers to the off-trace pixels, and the field-star limitation agreed today has its own short paragraph with its wording kept except for the 'also' bridge.

**02_nova.tex, lines 99-121**, starting "Each column records light from a range of wavelengths. For each group $g$ and"

```latex
Each column records light from a range of wavelengths. For each group $g$ and
wavelength $\lambda$, $K_{g\lambda}$ is how much of the star's light at
$\lambda$ is recorded in the column. It combines three public calibration
products. The PASTASOSS trace and wavelength calibration says where each
wavelength falls on the detector
\citep{BainesEtAl2023Trace,BainesEtAl2023Wavelength}. The line-spread kernel
describes how the light of one wavelength spreads over a few neighbouring
columns, and the throughput says how much of the light at each wavelength is
detected. NOVA builds $K_{g\lambda}$ from these products with ATOCA, the SOSS
extraction code of the JWST pipeline
\citep{DarveauBernierEtAl2022,JWSTPipeline2025}. In this calibration, all
pixels of a column see the same wavelengths, and only the light of each
group's own order is modelled. The fraction of a group's light that the
transit leaves is therefore the mean of the transit light curve over the
wavelengths of its column, weighted by the light that each wavelength
contributes,
\begin{equation}
 \bar{\mathcal{T}}_{tg}
 = \frac{\sum_{\lambda} K_{g\lambda}\, s_\lambda\, \mathcal{T}_t(\lambda)}
        {\sum_{\lambda} K_{g\lambda}\, s_\lambda},
 \label{eq:group-transit}
\end{equation}
where $\mathcal{T}_t(\lambda)$ is the transit light curve at wavelength
$\lambda$, whose depth is $D(\lambda)$, and $s_\lambda$ is the spectrum of the
star, fitted to the out-of-transit data of each data set and then held
fixed.
```
Reason: This is the paragraph with items nova-101 and nova-110 applied. Apply either the items or this rewrite. It removes one colon, two semicolons and three 'which' clauses, avoids repeating 'combines', and says in words what Eq. 4 computes before the reader reaches the symbols.

### Notes across sections

- Roadmap repetition: 01_introduction.tex:658-659 ('Section 2 describes NOVA as it is currently implemented and ends with a first, preliminary spectrum of WASP-17 b') and 02_nova.tex:14-15 say almost the same words, about 20 lines apart on PDF page 11. Change one of them (see nova-14).
- 'WASP-17 visit' (02:202, 02:218) against 'WASP-17~b visit' (02:200, 02:303, 02:312 and Sections 3-5). Use 'WASP-17 b' for the visit or observation, and 'WASP-17' only for the star, as Section 4 does.
- Units: 02:88-89 writes 'DN/s', while 03:114 and 04:37 and 04:140 write 'DN\,s$^{-1}$'.
- 'data set' (seven times in Section 2) against 'dataset(s)' (01:581, 04:237). Choose one spelling.
- 'learned' (01:660, 02:207) against 'learnt' (05:76). Choose one.
- Figure 4 (the nova_schematic.pdf graphic) says 'retained pixels' and 'fitted to the count rate of every retained pixel', while the text and caption say 'fitted pixels'. The graphic also uses 'continuum C_tg', a term the text does not define (see nova-175).
- Section 2.6 'The fit' has no \label. Section 3 (03:66) says the lower-estimate background was 'held in place by the same off-trace pixels (Section~\ref{sec:continuum})', but that holding term is described in 2.6. Consider adding \label{sec:fit} and pointing there. Pointing to 2.5, where the off-trace pixels are introduced, is also defensible.
- Section 2.9 says 'deeper throughout', while the abstract and 05:19-20 say 'deeper ... at every wavelength' (nova-316 aligns them).
- If nova-62 and nova-110 are applied, the T-bar wording ('the fraction of the group's light that the transit leaves') will match Section 4's r_p(t) ('the fraction of the star's light that remains').
- The exoTEDRF 1/f correction is described three times: in the Introduction (01:287-301), in 2.1 (02:22-28) and again in 3.2 (03:34-39, 'In each column, this correction estimates the stripe ...'). Section 3.2 already points to 2.1 and could rely more on that pointer, but Section 3 was agreed today.
- 'The real data cannot ...' recurs as a refrain: 02:324 'The real data cannot tell which reduction ...', the title of 3.4 'The real data cannot decide', and 03:112 'The real data therefore cannot decide.' Each use is fine on its own, but together they become noticeable.
- The Introduction writes ranges with a hyphen, '$0.6$-$2.8\,\mu\mathrm{m}$' (01:109-110, 123, 135, 197, 490), which prints as a hyphen, not an en dash. Section 2 uses 'to' or 'between ... and'. Use one convention, either 'to' or '--'.
- Section 2 opening (02:7-8) says the fit estimates 'the brightness of the star in each column', but the model has one per group (order and column). The difference is minor, since groups are defined only later.

### Questions for Davide (would change meaning, so not proposed as replacements)

- Should the Huber loss have a citation, for example Huber (1964)? It is the only standard method in Section 2 without one, and adding it would be a new reference, so I did not propose it.
- In 2.3, 'I smooth it across neighbouring columns, like a running average' is a simile. If the smoother is in fact a specific kernel (for example a running median or a Gaussian of a given width), naming it would answer the obvious examiner question. This would add content, so I left it.
- F277W first appears in 2.1 with no explanation of why that exposure shows field stars. Section 4.1 explains it ('in which the traces of WASP-17 almost vanish'). Would you like that half-clause at the first mention in 2.1?
- Notation reuse that an examiner may notice. b is the impact parameter (02:152) and b_oc is the limb-darkening slope (02:168). l_p is the intercept in Eq. 3 and l_o is the scaled log-wavelength. w_k are bin widths and w_tp are Huber weights. s_lambda is the stellar spectrum and s_p is the noise factor. N_p is indexed by pixel but takes one value per order (N_o would be clearer). Should some of these be renamed, for example l_o to Lambda_o and the slope b_oc to another letter?
- 02:323 says 'The larger difference in the red matters most'. Matters most for what? If you mean 'for this project, because the background has the largest effect there', saying so would answer the examiner's question. I did not change it because that would change the meaning.
- Section 2.9 gives medians below 1.6 um, at 1.8-2.3 um and above 2.3 um, but nothing for 1.6-1.8 um. An examiner may ask why. Is there a reason to leave that band out, and should the text say what it is?
- nova-325 changes 'which measures the errors' to 'that is designed to measure', to match the abstract, Sections 1 and 5 and the style rule against presenting an untested design as validated. Are you happy with the more cautious wording, or do you want to keep 'measures'?
- In nova-200, I replaced the 'also' in your agreed field-star sentence with 'left out of the off-trace pixels and of', because after the move the 'also' no longer has anything nearby to refer to. Are you happy with that, or should the sentence stay exactly as agreed and stay inside the map paragraph?

### Possible errors noticed in passing

- Eq. 8 (02:237) ends with a comma, but the next sentence starts a new sentence ('The first term ...'). This is left over from the earlier version that had a 'where' clause after the equation.
- Subject-verb agreement at 02:203-205: 'How well the maps describe ..., and how much an error of the maps there changes the depths, has not yet been tested.' The compound subject needs 'have', or the sentence should be recast.
- There is a tension between 2.2 ('Within one detector column, the pixels of a trace see nearly the same wavelength') and the opening of 2.4 ('Each column records light from a range of wavelengths'). Both are true, but read in sequence they seem to contradict each other until 'In this calibration, all pixels of a column see the same wavelengths'.
- 02:52-53 refers to Section 2.4 for 'the 51 reddest columns of order 1', but 2.4 gives only the 2.758 um cut and never the number 51, so the reader cannot match the two.
- Symbol clashes within one page: b (impact parameter) and b_oc; a/R_star and a_oc; l_p (Eq. 3) and l_o; w_k and w_tp; s_lambda and s_p. N_p is written with a pixel index but has one value per order.

## Section 4 (measured benchmark)

**How it reads now.** Section 4 reads more plainly than any other section of the report. Most sentences are concrete and in the first person, and they say what was done and why. Its problems are local. Several sentences chain "because ... so ... but" (the halo glow, the halo model, the dark spots). A few "which", "it" and "the two" have two possible antecedents (lines 38, 67, 109, 129, 204), and the garden path "split the light where the orders overlap with ATOCA" will make a reader stop. The Gaia material (lines 75-109) is one paragraph of about 600 words. It mixes the mapping, the source detection, the matching, the error statistics, why programme 4476 cannot be fitted, and the circularity caveat. It also pushes "Thirdly" a page and a figure away from "Secondly", and it should be four paragraphs. Names drift: the moved exposure is also "the second exposure" and "the real exposure" (and at line 269 "the real exposure" means the other exposure); "groups" and "reads" both appear; the field sources are called blobs, spots, sources and bumps; the labels inside the figures say "normal" where the text says "usual". There is one near-verbatim repetition between 4.2 and 4.3, and Figures 7 and 8 are numbered out of the order in which the text cites them.

### measured-5: 04_measured_benchmark.tex:5 · consistency · impact 1

Current:
```latex
once moved away
from the strip that SOSS time series read out.
```
Proposed:
```latex
once moved off
the strip that SOSS time series read out.
```
Reason: The abstract and the introduction both say "moved off the strip"; use the same words here.

### measured-7: 04_measured_benchmark.tex:7 · flow · impact 2

Current:
```latex
so the injector depends
much less on a fitted split between starlight and background.
```
Proposed:
```latex
so the injector depends
much less on a fitted split between starlight and background. In this
section, I describe how I turn this difference into a cleaned image of the
star and inject it with a known transit, how I will test the injector and the
pipelines, and the limitations of the benchmark.
```
Reason: The section has no signpost (style rule 2). This sentence names the four subsections, so the reader knows where the long Section 4.1 is heading. The list has four items because there are four subsections, not for rhythm.

### measured-14: 04_measured_benchmark.tex:14 · clarity · impact 2

Current:
```latex
TYC 4213-1116-1, an
A-type star that gives about 1.6 times as much light per detector column as
WASP-17, in two full-frame exposures taken about 25 minutes apart.
```
Proposed:
```latex
TYC~4213-1116-1 in two full-frame exposures taken about 25 minutes apart.
This A-type star gives about 1.6 times as much light per detector column as
WASP-17.
```
Reason: As written, "in two full-frame exposures" arrives after "WASP-17" and can attach to it, and the long appositive delays the main point. The tilde also stops the star's name from breaking across lines.

### measured-17: 04_measured_benchmark.tex:17 · consistency · impact 1

Current:
```latex
ten integrations of five groups
```
Proposed:
```latex
ten integrations of five reads
```
Reason: The rest of the section says "reads" (lines 214, 305, 309), and the introduction defines a group as a read, so one word is enough.

### measured-20: 04_measured_benchmark.tex:20 · consistency · impact 2

Current:
```latex
This second exposure has 150 integrations covering
2.68~h, and it is the one into which I inject the star.
```
Proposed:
```latex
This second exposure, the moved exposure, has 150 integrations covering
2.68~h. It is the one into which I inject the star.
```
Reason: This gives "the moved exposure" (Davide's term, used in the abstract, the captions and Sections 4.2-4.3) its name where the exposure is introduced. At present the section switches between "second", "moved" and "real" exposure without saying that they are the same.

### measured-27: 04_measured_benchmark.tex:27 · AI tell · impact 1

Current:
```latex
whatever is the same at the same pixels cancels: the zodiacal background,
```
Proposed:
```latex
everything that is the same at the same pixels cancels. This includes the
zodiacal background,
```
Reason: "whatever ... cancels:" reads like a colon reveal, and the section is above the colon target (2.6 per 1000 words).

### measured-31: 04_measured_benchmark.tex:31 · cut · impact 1

Current:
```latex
The read noise and the offsets that vary in time, such as the $1/f$
stripes, do not cancel, because they change from moment to moment.
```
Proposed:
```latex
The read noise and the offsets that vary in time, such as the $1/f$
stripes, do not cancel.
```
Reason: The reason is circular: offsets "that vary in time" fail to cancel "because they change from moment to moment". The because-clause adds nothing for a physicist.

### measured-38: 04_measured_benchmark.tex:38 · clarity · impact 3

Current:
```latex
The benchmark keeps this glow, because it is built on the second
exposure, so the total light out of transit is right, but the glow does not
dim during the transit.
```
Proposed:
```latex
The benchmark is built on the second exposure, so it keeps this glow,
and the total light out of transit is right. The glow, however, does not
dim during the transit.
```
Reason: The sentence stacks "because ... so ... but", and "it" can be read as the glow. Split it into the cause and its two consequences.

### measured-41: 04_measured_benchmark.tex:41 · clarity · impact 2

Current:
```latex
this makes the depth 2 to 19~ppm shallower
```
Proposed:
```latex
the undimmed glow makes the depth 2 to 19~ppm shallower
```
Reason: After the previous sentence, "this" has no clear antecedent. Name what makes the depth shallower.

### measured-42: 04_measured_benchmark.tex:42 · clarity · impact 2

Current:
```latex
The full frames show this halo at 700 to 800 rows from the
moved star, and with its measured fall-off it can be extrapolated to the
strip, so I can correct the image of the star by adding this model of the
halo.
```
Proposed:
```latex
The full frames show this halo at 700 to 800 rows from the
moved star. Extrapolating its measured fall-off to the strip gives a model of
the halo there, and I can correct the image of the star by adding this model.
```
Reason: "this model of the halo" points to a model that the sentence never introduces. The rewrite introduces it and removes one "and ... so" chain.

### measured-47: 04_measured_benchmark.tex:47 · clarity · impact 2

Current:
```latex
Secondly, field sources do not cancel, because they moved with the telescope
```
Proposed:
```latex
Secondly, field sources do not cancel, because they moved on the detector when the telescope moved
```
Reason: Field sources stay fixed on the sky; only their position on the detector changed. A physicist will read "moved with the telescope" literally.

### measured-54: 04_measured_benchmark.tex:54 · clarity · impact 2

Current:
```latex
A dark spot would cancel the field source in the
benchmark out of transit and let part of it reappear during the transit, so
at its pixels I subtract an estimate of the sky alone instead of the second
exposure.
```
Proposed:
```latex
A dark spot in the injected star would cancel the field source in the
benchmark out of transit, and part of the source would reappear during the
transit. At these pixels, I therefore subtract an estimate of the sky alone
instead of the second exposure.
```
Reason: This now parallels the bright-spot sentence ("part of the injected star"), so the reader sees why a negative spot matters. The current chain "and let ... so at its pixels" is hard to parse on a first read.

### measured-63: 04_measured_benchmark.tex:63 · clarity · impact 1

Current:
```latex
I find the dark spots in the second exposure, where the star is not in the
way, and the bright spots as compact bumps that the neighbouring columns of
the trace do not have.
```
Proposed:
```latex
I find the dark spots in the second exposure, where the star is not in the
way. The bright spots show up as compact bumps that the neighbouring columns
of the trace do not have.
```
Reason: The two halves are not parallel ("find X in Y" against "find X as Z"). Two sentences read more easily.

### measured-67: 04_measured_benchmark.tex:67 · clarity · impact 3

Current:
```latex
Gaia, however, also tells me where
the spectra of known stars fall, which a search for compact spots cannot
find, even for stars that lie off the strip.
```
Proposed:
```latex
Gaia, however, also tells me where
the spectra of known stars fall, even for stars that lie off the strip. A
search for compact sources cannot find these spectra.
```
Reason: "which a search ... cannot find" can refer to Gaia or to where the spectra fall, and "even for stars off the strip" then attaches to the wrong verb. "compact sources" also matches line 86 and the legend of Figure 7.

### measured-69: 04_measured_benchmark.tex:69 · clarity · impact 1

Current:
```latex
I move each star's catalogue
```
Proposed:
```latex
I update each star's catalogue
```
Reason: "Move" already names the moved exposure and the moved star. "Update ... to the date" is the plainer verb for a catalogue position.

### measured-72: 04_measured_benchmark.tex:72 · repetition · impact 2

Current:
```latex
The grism slightly rotates and stretches this pattern, and each field star's
spectra are those of the target, moved by the star's offset from it.
```
Proposed:
```latex
The grism slightly rotates and stretches this pattern of positions.
```
Reason: The second clause is repeated four lines later, after Eq. (9) ("The spectra of star i are those of the target, moved by A Delta_i"). Keep the precise version there.

### measured-86: 04_measured_benchmark.tex:86 · clarity · impact 2

Current:
```latex
To locate the compact
sources, I first removed everything that is smooth along the rows, such as
the traces and the sky, by subtracting from each row a running median over 51
columns, and removed the $1/f$ stripes by subtracting the median of each
column. I then smoothed the result slightly, with a Gaussian of 1.5 pixels,
and flagged
```
Proposed:
```latex
To locate the compact
sources, I first subtracted from each row a running median over 51 columns.
This removed everything that is smooth along the rows, such as the traces and
the sky. I then removed the $1/f$ stripes by subtracting the median of each
column, smoothed the result slightly with a Gaussian of 1.5 pixels,
and flagged
```
Reason: This is one sentence of more than 50 words with two "removed ... by" clauses, and the action comes after the effect. The split gives one step per clause.

### measured-93: 04_measured_benchmark.tex:93 · grammar · impact 1

Current:
```latex
are left over from their removal; a source counts as real if
```
Proposed:
```latex
are left over from their removal. A source counts as real if
```
Reason: The semicolon joins a problem to the rule that answers it. Two sentences are clearer.

### measured-105: 04_measured_benchmark.tex:105 · AI tell · impact 2

Current:
```latex
Programme 4476 cannot provide such a fit: its field is
sparse, with 208 Gaia stars within $5.4'$ of the target against 1,455 around
WASP-17, and its strip contains the undispersed image of at most one, very
faint Gaia star.
```
Proposed:
```latex
Programme 4476 cannot provide such a fit, because its field is
sparse. It has 208 Gaia stars within $5.4'$ of the target, against 1,455 around
WASP-17, and its strip contains the undispersed image of at most one Gaia
star, which is very faint.
```
Reason: This removes a colon reveal and the odd comma in "at most one, very faint Gaia star".

### measured-109: 04_measured_benchmark.tex:109 · clarity · impact 3

Current:
```latex
Because NOVA may later use the same predictions, agreement between the two would not by itself show
```
Proposed:
```latex
Because NOVA may later use the same Gaia predictions, agreement between NOVA and the injector would not by itself show
```
Reason: "The two" could mean the images and Gaia, the pair named in the previous sentence. The point is that NOVA and the injector could share errors.

### measured-111: 04_measured_benchmark.tex:111 · LaTeX · impact 2

Current:
```latex
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figures/w17_gaia_mapping.pdf}
```
Proposed:
```latex
\begin{figure*}[t]
  \centering
  \includegraphics[width=0.92\textwidth]{figures/pid4476_star_and_carrier.pdf}
  \caption{The SOSS strip in programme 4476. (a) The exposure with the star at
  its usual position. (b) The exposure with the star moved 1,026 rows lower,
  into which the star is injected. (c) The cleaned image of the star, given by
  the difference between (a) and (b) with the field sources removed and the
  far wings smoothed (a preliminary version, made before the corrections for
  the sky and the halo of the moved star). Orange outlines mark the field
  sources found in each exposure. Blue dashed lines are the spectra of Gaia
  DR3 stars with $G\leq20.5$ predicted on the strip
  (Section~\ref{sec:measuring-star}). In (b), the predictions are moved by 10
  rows so that the target falls at its measured position. The grey scale is
  logarithmic.}
  \label{fig:4476}
\end{figure*}

\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figures/w17_gaia_mapping.pdf}
```
Reason: The text cites Figure 8 (line 48) before Figure 7 (line 76), so the PDF numbers the figures out of order. Moving the programme-4476 figure above the WASP-17 Gaia figure fixes this. The original block at lines 151-166 must then be deleted, and the caption fixes measured-156 and measured-162 applied to the moved copy.

### measured-125: 04_measured_benchmark.tex:125 · flow · impact 1

Current:
```latex
Thirdly, the far wings are noisy.
```
Proposed:
```latex
Thirdly, the far wings of the difference are noisy.
```
Reason: "Secondly" is a page and a figure earlier. "Of the difference" links back to the three reasons announced at line 34.

### measured-129: 04_measured_benchmark.tex:129 · clarity · impact 2

Current:
```latex
combining the pipeline's error estimates for the two exposures, which agree
with the actual scatter between neighbouring pixels to within 10\%.
```
Proposed:
```latex
combining the pipeline's error estimates for the two exposures. These
estimates agree with the actual scatter between neighbouring pixels to within
10\%.
```
Reason: "which agree" can be read as referring to the two exposures.

### measured-134: 04_measured_benchmark.tex:134 · clarity · impact 2

Current:
```latex
The shape of the wings is set by the
optics and changes only slowly with wavelength, so beyond 40 rows from the
nearest trace I replace each pixel
```
Proposed:
```latex
The shape of the wings is set by the
optics and changes only slowly with wavelength. Beyond 40 rows from the
nearest trace, I therefore replace each pixel
```
Reason: This is a sentence of about 50 words. Splitting it separates the reason from the method.

### measured-141: 04_measured_benchmark.tex:141 · consistency · impact 1

Current:
```latex
the weight of this
model rises linearly
```
Proposed:
```latex
the weight of this
far-wing model rises linearly
```
Reason: The text never calls the median a model before this point. "Far-wing model" is the name used in the caption of Figure 9.

### measured-156: 04_measured_benchmark.tex:156 · clarity · impact 1

Current:
```latex
(c) The cleaned image of the star, given by
  the difference between (a) and (b) with the field sources removed and the
  far wings smoothed (a preliminary version, made before the corrections for
  the sky and the halo of the moved star).
```
Proposed:
```latex
(c) The cleaned image of the star, given by
  the difference between (a) and (b) with the field sources removed and the
  far wings smoothed. It is a preliminary version, made before the corrections
  for the sky and the halo of the moved star.
```
Reason: The panel description runs to 45 words and ends in a long parenthesis. The caveat reads better as its own sentence, as it already is in the caption of Figure 9.

### measured-162: 04_measured_benchmark.tex:162 · consistency · impact 1

Current:
```latex
the predictions are moved by 10
```
Proposed:
```latex
the predictions are shifted by 10
```
Reason: This avoids yet another use of "moved" in a caption about the moved exposure.

### measured-179: 04_measured_benchmark.tex:179 · clarity · impact 1

Current:
```latex
negative values are kept
```
Proposed:
```latex
negative values can be shown
```
Reason: "Kept" suggests a processing step. The point is that the axis can display negative values.

### measured-187: 04_measured_benchmark.tex:187 · consistency · impact 2

Current:
```latex
to the raw reads of
the second exposure.
```
Proposed:
```latex
to the raw reads of
the moved exposure.
```
Reason: From Section 4.2 on, the abstract, the captions and Section 4.3 say "moved exposure", and Eq. (10) is where a reader will look the term up.

### measured-194: 04_measured_benchmark.tex:194 · consistency · impact 1

Current:
```latex
$O_p(t)$ is the count rate of the second exposure
```
Proposed:
```latex
$O_p(t)$ is the count rate of the moved exposure
```
Reason: Same reason as measured-187. Figure 10 labels O as the "moved exposure".

### measured-204: 04_measured_benchmark.tex:204 · clarity · impact 3

Current:
```latex
I take the
wavelength at each position along each order from PASTASOSS
\citep{BainesEtAl2023Wavelength}, and split the light where the orders overlap
with ATOCA
```
Proposed:
```latex
I take the
wavelength at each position along each order from PASTASOSS
\citep{BainesEtAl2023Wavelength} and, where the orders overlap, split the
light with ATOCA
```
Reason: Garden path: "where the orders overlap with ATOCA" first reads as the orders overlapping with ATOCA.

### measured-220: 04_measured_benchmark.tex:220 · clarity · impact 2

Current:
```latex
The detector does not record charge in proportion: as a pixel fills,
each additional electron raises the recorded value a little less.
```
Proposed:
```latex
The recorded value is not proportional to the charge. As a pixel fills,
each additional electron raises it a little less.
```
Reason: "does not record charge in proportion" leaves "in proportion to what?" open, and the colon works as a reveal.

### measured-223: 04_measured_benchmark.tex:223 · grammar · impact 1

Current:
```latex
behaves as real light
```
Proposed:
```latex
behaves like real light
```
Reason: "As" reads as "in the role of", but the meaning is "in the same way as". Section 3.4 already says "behaves like starlight".

### measured-233: 04_measured_benchmark.tex:233 · clarity · impact 2

Current:
```latex
The two share the real exposure and every photon that the transit did not remove, so they differ only by the removed light, and the only noise left in their difference is the small photon noise of that light.
```
Proposed:
```latex
The two share the real exposure and every photon that the transit did not remove. They differ only by the removed light, so the only noise left in their difference is the small photon noise of that light.
```
Reason: This is 43 words joined by "so ... and the only". The next sentence already has "therefore", so split here.

### measured-237: 04_measured_benchmark.tex:237 · consistency · impact 1

Current:
```latex
A single dataset with a transit
```
Proposed:
```latex
A single data set with a transit
```
Reason: Section 2 writes "data set" seven times. Apart from one instance in the introduction, this is the only "dataset" in the report.

### measured-244: 04_measured_benchmark.tex:244 · clarity · impact 2

Current:
```latex
Further tests would be needed to isolate the faint light.
```
Proposed:
```latex
Further tests would be needed to isolate the effect of the faint light.
```
Reason: Read literally, "isolate the faint light" means separating the light itself, which is what the cleaning does. The point is to attribute the difference to the faint light.

### measured-256: 04_measured_benchmark.tex:256 · clarity · impact 1

Current:
```latex
stay there and do not transit
```
Proposed:
```latex
stay in the data and do not transit
```
Reason: "There" has no clear place to refer to.

### measured-267: 04_measured_benchmark.tex:267 · consistency · impact 2

Current:
```latex
Secondly, out of
transit, the injected data, made of the moved exposure plus the injected star,
should look like the real exposure with the star at its usual position.
```
Proposed:
```latex
Secondly, out of
transit, the moved exposure plus the injected star should look like the
first exposure, in which the star was at its usual position.
```
Reason: This removes the definition squeezed between commas. Also, "the real exposure" means the moved exposure at lines 227 and 233 but the other exposure here.

### measured-275: 04_measured_benchmark.tex:275 · clarity · impact 2

Current:
```latex
Neither
comparison can show that the cleaned image is the true star; that rests on the
cleaning
```
Proposed:
```latex
Neither
test can show that the cleaned image is the true star. That rests on the
cleaning
```
Reason: The checks of the code are not a comparison, so "neither comparison" does not fit both tests. The semicolon is also replaced.

### measured-279: 04_measured_benchmark.tex:279 · clarity · impact 2

Current:
```latex
Each pipeline runs its own workflow on the same raw files, set up without
knowledge of the injected transit.
```
Proposed:
```latex
Each pipeline, set up without knowledge of the injected transit, runs its
own workflow on the same raw files.
```
Reason: Misplaced modifier: "set up without knowledge" sits next to "raw files" and reads as describing them.

### measured-284: 04_measured_benchmark.tex:284 · clarity · impact 1

Current:
```latex
spectrum, which gives the total error that a user would get.
```
Proposed:
```latex
spectrum. This gives the total error that a user would get.
```
Reason: "Which" can be read as referring to the injected spectrum.

### measured-287: 04_measured_benchmark.tex:287 · repetition · impact 2

Current:
```latex
Because the two runs differ only by the light that the transit removed, each comparison shows the transit as that step passed it on. Knowing
```
Proposed:
```latex
Knowing
```
Reason: This repeats Section 4.2 (line 233) almost word for word, including "shows the transit as that step passed it on".

### measured-299: 04_measured_benchmark.tex:299 · clarity · impact 1

Current:
```latex
hotter than 50 of the 51 exoplanet hosts that SOSS had observed by October 2026, whose median temperature is 4,870~K.
```
Proposed:
```latex
hotter than 50 of the 51 exoplanet hosts that SOSS had observed by October 2026. The median temperature of these hosts is 4,870~K.
```
Reason: "Whose" comes straight after "October 2026", far from "hosts".

### measured-309: 04_measured_benchmark.tex:309 · clarity · impact 1

Current:
```latex
the star's light in
its box.
```
Proposed:
```latex
the star's light in
the exoTEDRF extraction box.
```
Reason: "Its box" can be read as the star's box.

### measured-315: 04_measured_benchmark.tex:315 · clarity · impact 2

Current:
```latex
It could be added by shifting
```
Proposed:
```latex
This motion could be added by shifting
```
Reason: "It" has no antecedent, because the previous sentence ends on "this".

### measured-319: 04_measured_benchmark.tex:319 · grammar · impact 1

Current:
```latex
Fourthly, the injection adds light but no response of the detector's
electronics to the change in light. If the detector itself reacts when the star dims, as the faint light outside the traces may suggest (Section~\ref{sec:real-data-test}), the benchmark does not contain this.
```
Proposed:
```latex
Fourthly, the injection adds light, but it does not add any response of
the detector's electronics to the change in light. If the detector itself reacts when the star dims, as the faint light outside the traces may suggest (Section~\ref{sec:real-data-test}), the benchmark does not contain this reaction.
```
Reason: "Adds light but no response" makes one verb do two jobs and reads oddly, and "contain this" lacks a noun.

### measured-324: 04_measured_benchmark.tex:324 · clarity · impact 2

Current:
```latex
Fifthly, the exposure lasts only 2.68~h, so the injected transit lasts
51.5~minutes, to leave time before and after it. A planet crossing the centre
of this star would take hours, so with the one-day orbit that I chose, the
shape of this short transit corresponds to an unphysical star, about a hundred
times denser than this one.
```
Proposed:
```latex
Fifthly, the exposure lasts only 2.68~h, so the injected transit is
51.5~minutes long, to leave time before and after it. A planet crossing the
centre of this star would take hours. With the one-day orbit that I chose, the
shape of this short transit corresponds to an unphysical star, about a hundred
times denser than this one.
```
Reason: The first sentence uses "lasts" twice, and the second runs to 40 words through "so with ... the shape". The following sentence keeps its "therefore".

### measured-333: 04_measured_benchmark.tex:333 · flow · impact 2

Current:
```latex
allows deviations from it; I still need to give NOVA a reference suited to this star. Both fit the limb darkening freely in the white-light curves.
```
Proposed:
```latex
allows deviations from it. Both fit the limb darkening freely in the white-light curves. I still need to give NOVA a reference suited to this star.
```
Reason: This removes the semicolon, and "Both" now follows the sentence that names exoTEDRF and NOVA rather than a sentence about NOVA alone.

### measured-335: 04_measured_benchmark.tex:335 · repetition · impact 2

Current:
```latex
With the existing data, this is as close to a real observation as I can make
the benchmark, and it rests on a single star.
```
Proposed:
```latex
With the existing data, this is as close to a real observation as I can make
the benchmark.
```
Reason: "It rests on one star" is already the first limitation (line 297), and Section 5 (Paper 1) repeats it again.

### Paragraph rewrites (Section 4 (measured benchmark))

**04_measured_benchmark.tex, lines 75-109**, starting "I fitted this rotation and stretch on the WASP-17~b data"

```latex
I fitted this rotation and stretch on the WASP-17~b data
(Figure~\ref{fig:w17-gaia}). For a Gaia star $i$, let
$\boldsymbol{\Delta}_i$ be its offset from the target on the detector without
the grism, in pixels. Its undispersed image then lands at
\begin{equation}
  \mathbf{p}_i = \mathbf{A}\,\boldsymbol{\Delta}_i + \mathbf{t},
  \label{eq:gaia-map}
\end{equation}
where $\mathbf{A}$ is a $2\times2$ matrix that rotates and stretches the
offsets, and $\mathbf{t}$ is the position of the target's own undispersed
image, which lies off the strip. The spectra of star $i$ are those of the
target, shifted by $\mathbf{A}\,\boldsymbol{\Delta}_i$.

To locate the compact sources, I first subtracted from each row a running
median over 51 columns. This removed everything that is smooth along the rows,
such as the traces and the sky. I then removed the $1/f$ stripes by
subtracting the median of each column, smoothed the result slightly with a
Gaussian of 1.5 pixels, and flagged groups of at least 12 touching pixels that
lie more than five times the noise above zero. Many of these detections lie
along the traces and are left over from their removal. A source counts as
real if it also appears in an exposure through the F277W filter, in which the
traces of WASP-17 almost vanish, or if it matches a Gaia star.

To find which detected source belongs to which Gaia star, I held the stretch
fixed and slid the whole predicted pattern across the image, within 300 pixels
of the position given by the standard model of the ExoCTK contamination tool.
At each position, I counted how many predicted images fell within 8 pixels of
a detected source. At most positions none did, and at 99\% of them at most two
did. At the best position, seven of the nine predicted images did, so this
alignment stands out clearly from all others. I then fitted the six numbers in
$\mathbf{A}$ and $\mathbf{t}$ by least squares to the eight pairs found this
way. The fitted mapping places these images to within 0.8 columns and 3.6 rows
(rms), against 4.3 columns and 14.9 rows for the standard model. When each pair
is left out of the fit and predicted from the other seven, the errors are 1.5
columns and 7.8 rows.

Programme 4476 cannot provide such a fit, because its field is sparse. It has
208 Gaia stars within $5.4'$ of the target, against 1,455 around WASP-17, and
its strip contains the undispersed image of at most one Gaia star, which is
very faint. Both observations used the same instrument setting, so I use the
WASP-17~b fit for programme 4476. I will check the faint spectra that this fit
predicts in both pointings. The injector finds field sources from the images,
with Gaia guiding the search. Because NOVA may later use the same Gaia
predictions, agreement between NOVA and the injector would not by itself show
that the field-star light was separated correctly.
```
Reason: The current paragraph is about 600 words and does six jobs. Splitting it into the mapping, the detection, the matching and fit, and the application to programme 4476 makes each step readable and gives the circularity caveat a clear subject. The rewrite includes measured-86, -93, -105 and -109, uses "shifted" for the A Delta_i offset, and changes no number or claim.

**04_measured_benchmark.tex, lines 125-149**, starting "Thirdly, the far wings are noisy."

```latex
Thirdly, the far wings of the difference are noisy. The subtraction removes
the sky, so the image shows the light of the star far from the traces, where
it is fainter than the sky (Figure~\ref{fig:4476-profiles}). The first
exposure, however, has only ten integrations. I estimate the uncertainty of
each pixel by combining the pipeline's error estimates for the two exposures.
These estimates agree with the actual scatter between neighbouring pixels to
within 10\%. Dividing each pixel by its uncertainty gives a signal-to-noise
ratio of 112 to 675 in the cores of the traces, 10 to 73 at 20 to 40 rows from
them, and only 2 to 3 at 40 to 200 rows from order~1 in the red. Injected as
it is, this noise would become a fixed pattern in the star.

The shape of the wings is set by the optics and changes only slowly with
wavelength. Beyond 40 rows from the nearest trace, I therefore replace each
pixel by the median of the pixels at the same distance from the trace in the
61 neighbouring columns, which span about $0.06\,\mu\mathrm{m}$ in order~1.
Where the wings of several orders overlap, the nearest order dominates this
estimate. On average, this far-wing model differs from the measured pixels by
only about 0.16\% at 40 to 100 rows, so the wings change slowly enough for
this. The model lowers the noise per pixel from about 0.10 to about
0.017~DN\,s$^{-1}$, and it also removes the $1/f$ stripes left in the
difference. Between 30 and 40 rows, its weight rises linearly from zero to
one, so that the image passes smoothly from the data to the model. Nearer the
traces, I keep the measured light, with its noise and stripes. These are fixed
in the image of the star, whereas the real, changing $1/f$ noise of the
benchmark comes from the reads of the second exposure across the whole strip.
The result is the cleaned image of the star, $S$, a count rate per pixel
(Figure~\ref{fig:4476}c).
```
Reason: This splits the problem (noise) from the fix (the far-wing model). It moves the 0.16% check next to the assumption it supports ("changes only slowly"); it now dangles at the end with "for this". It names the model once, as the caption of Figure 9 does. The rewrite includes measured-125, -129, -134 and -141 and changes no number.

### Notes across sections

- The moved exposure has three names in Section 4: "second exposure" (lines 20, 25, 37, 39, 57, 63, 146, 188, 194), "moved exposure" (captions, lines 251 and 268, the abstract) and "real exposure" (lines 227 and 233). At line 269, "real exposure" means the other exposure, the one with the star at its usual position. Introduce "moved exposure" at line 20 and use it from Section 4.2 on (measured-20, -187, -194, -267).
- The labels inside the figures do not match the text. Figure 8 panel titles read "Star at the normal position" and "Star moved 1,026 rows away", where the text says "usual position" and "lower". The Figure 9 legend says "normal exposure", "cleaned source" and "cleaned source, far-wing model", and Figure 10 says "normal exposure N", where the text says "usual position" and "cleaned image of the star". These need the figure scripts, not the .tex.
- Line 17 says "groups" while the rest of Section 4 says "reads". The introduction (lines 255-270) defines a read as a group, and Section 2 uses "group".
- "data set" appears seven times in Section 2, but "dataset" appears in Section 1 (line 581) and in Section 4 (line 237).
- The idea that the difference between the two 4476 exposures measures the star directly is stated four times: in the abstract, at the end of Section 1.5, at the end of Section 3.4 and in the opening of Section 4. The Section 4 opening is fine as a short recap, but it should not grow.
- The closing paragraph of Section 4.4 (repeat programme 4476 for several stars, read out as a time series, with more integrations at the usual position) is restated almost point by point in Section 5, Paper 1 ("Because the benchmark rests on a single star, I will also propose ..."). "Rests on one/a single star" appears at Section 4 line 297, Section 4 line 336 and Section 5 Paper 1, and Section 5.1 also says "The price is a different star, field and readout". Cut the line-336 instance (measured-335), and consider letting Paper 1 refer back to Section 4.4.
- Section 4 uses "compact blobs" (lines 48, 65), "compact spots" (line 68), "compact bumps" (line 64) and "compact sources" (line 86, the Figure 7 caption and legend) for the same objects. "Bright/dark spots" is a separate pair and is fine. Pick "compact sources" (measured-67), and decide whether "blobs" stays once as the first description.
- "Moved" carries several senses in Section 4: the moved exposure, the moved star, "moved by the star's offset", "I move each star's catalogue position" and "predictions are moved by 10 rows". measured-69 and -162 and paragraph rewrite 75-109 reduce this.
- "Standard" is used both for "the standard model of the ExoCTK contamination tool" (lines 98, 103 and the Figure 7 caption and legend) and for "a standard calibration curve" (line 222).
- The introduction (line 619) says "a clean image of the star", while the abstract and Section 4 say "cleaned image of the star". Line 34 ("not yet a clean image") is fine because it means the target state.
- The pipelines run on the benchmark are named only in Section 5 (NOVA, exoTEDRF, Ahsoka and transitspectroscopy). Section 4.4 line 330 says "the four pipelines" without saying anywhere in Section 4 which four.

### Questions for Davide (would change meaning, so not proposed as replacements)

- Lines 100-101: "At the best position, seven of the nine predicted images did" is followed by "the eight pairs found this way". Both numbers are verified (a5_03_state.json: best position 7 of 9, 8 pairs), but a reader will see the jump from seven to eight and ask where the eighth came from. Can I add one clause saying how the eighth pair was found, for example after a first refit?
- The captions of Figures 8 and 9 say the cleaned image was made "before the corrections for the sky and the halo of the moved star". The text describes the halo correction but no correction "for the sky" of the cleaned image; the closest is the sky-alone estimate at the dark spots, and the 1% agreement of the zodiacal levels. Which sky correction is meant? Should the text name it, or should the caption say only "the halo"?
- Line 330 says "None of the four pipelines", but Section 4 never says which four. Should Section 4.3 name them (NOVA, exoTEDRF, Ahsoka and transitspectroscopy), as Section 5 does?
- ExoCTK is neither expanded nor cited, and there is no entry in references.bib. "The standard model" also reads oddly to a physics examiner. Would "the default mapping of the ExoCTK contamination tool" be acceptable? The Figure 7 legend ("Gaia, standard model") and caption would then need the same change.
- PHOENIX (line 333) has no citation; STAGGER is cited as MagicEtAl2015. Add Husser et al. (2013)?
- The caption of Figure 9 says "dashed where the far-wing model is used, which depends on the distance from the nearest trace". Does "which" mean that the model itself is a function of the distance, or that where the dashed part starts depends on which trace is nearest? Either is fine, but the caption should say which.
- Lines 204-211: the paragraph says "I take the wavelength ... and split the light" in the present tense, then "I have not yet built these spectral cases". Should I switch it to "I will take ... and split" so that the tense matches the status? I did not propose this because it changes the wording of agreed text.
- Should the opening of Section 4 have an "In this section, I ..." signpost (measured-7)? Section 2 has one; Sections 3 and 4 do not.

### Possible errors noticed in passing

- Figure numbering: the text cites fig:4476 (Figure 8) at line 48, before fig:w17-gaia (Figure 7) at line 76. The fig:w17-gaia float comes first in the source (line 111 against line 151), so the PDF shows Figure 8 cited before Figure 7. The fix is in measured-111.
- Line 47, "field sources do not cancel, because they moved with the telescope": field sources are fixed on the sky, and it is their position on the detector that changed. Taken literally the statement is physically wrong, though the intended meaning is clear (measured-47).
- Lines 100-101: "seven of the nine predicted images" at the best position, then "the eight pairs found this way". As written, the sliding search did not find eight pairs (see questions).
- The captions of Figures 8 and 9 refer to a "correction for the sky" of the cleaned image that the text does not describe (see questions).
