# Wording review of the ESA: Opus, Fable and ASTRA merged (b50eb10)

Davide asked each of us to read the whole report individually, sentence by sentence, for wording and style, and then to say what we would change and where. Each review was written independently: Opus 210 items, Fable 92 and ASTRA 56. The three are in this folder as `Opus.md`, `Fable.md` and `ASTRA.md`. This file merges them.

**What is here.** 247 changes: 45 in tier 1, 111 in tier 2 and 91 in tier 3. There are also 14 paragraph rewrites and 43 questions that only Davide can answer. Finally, 17 reviewer proposals we decided against are listed with the reason, so nothing has been dropped silently.

**How to read it.**
- *Tier 1* is must-fix: a visible error in the PDF, a grammar or logic slip, a term that is never defined, a banned word, a sentence that is wrong if read literally or that has to be read twice, or a point that all three of us flagged.
- *Tier 2* is a clear improvement in readability.
- *Tier 3* is polish or taste.

"Current" is the exact LaTeX source, and every quote was matched against the file. "Recommended" is ready to paste. Every citation and cross-reference in the current text is kept in the recommended text. A change of meaning is never proposed as a replacement; where one might be wanted, it is asked as a question instead. A paragraph rewrite is an alternative to the entries it lists, so apply one or the other, not both. **Nothing has been applied to the ESA.**

## 1. Report-wide choices (one decision each)

| What | Recommended | Where it changes |
|---|---|---|
| Wavelength ranges | "0.6 to $2.8\,\mu$m", as Sections 2 to 5 already write | Six hyphen ranges in the Introduction (lines 109, 110, 123, 135, 197, 490), which print as hyphens |
| Count-rate unit | DN\,s$^{-1}$ (all three now agree; Fable withdrew DN/s at 22:19) | 02:88–89 only |
| "whilst" or "while" | "whilst", as Sections 1 and 2 write nine times | 04:305, 05:58, 05:62 |
| "data set" or "dataset" | "data set", as Section 2 writes seven times | 01:581, 04:237 |
| The exposure the star is injected into | "the moved exposure", named once where it is introduced (04:20) | 04:36, 54, 63, 145, 187, 194, 267 |
| The band of pixels summed in extraction | "extraction box" (Section 2 uses "apertures" for NOVA's own pixels) | 01:609, 01:613 |
| The image built from programme 4476 | "cleaned image of the star"; its outer part "far wings" | 01:619, 01:622 |
| Reads of a ramp | "raw reads" | 01:644 (objective 2) |
| R_p(λ) | "effective radius" | Figure 1 caption (01:48) and its label in figures/transmission_spectroscopy_schematic.tex |
| Order naming | "order 1", never "the first order" | 01:136 |
| The NOVA/exoTEDRF result | "the ranking reversed", as in the abstract and Section 5 | 03:88 |
| The observation | "WASP-17~b visit"; "WASP-17" only for the star | 02:202, 02:210, 02:218 |
| Undispersed field objects | "compact sources" (blobs/spots/bumps now) | 04:48, 65, 68 |
| learned / learnt | one form ("learned" needs one edit) | 05:76 |
| Gantt labels | "Thesis chapters from papers"; "Extensions to NIRSpec and eclipses" | 05:164, 05:154 |

## 2. Questions only Davide can answer

Each of these would change meaning or content, so none is proposed as a straight replacement. Where Opus has checked a fact, the answer follows the question.

1. **Abstract (approved by Davide this evening), `00_abstract.tex:10`** (Opus). "Predicts every pixel": NOVA fits only the pixels in its two apertures (Section 2 says "every fitted pixel"). Is the compression acceptable in an approved abstract, or would "predicts every fitted pixel" be safer?
2. **1.1 Exoplanet atmospheres and transmission spectroscopy, `01_introduction.tex:25`** (Opus, Fable). What is the gas-loss sentence for: 'Some planets are also observed to lose gas from their upper atmosphere \citep{VidalMadjarEtAl2003}'? Nothing later uses it, and it is a loose end at the close of a paragraph about composition and formation. Options: (a) cut it (Fable); (b) link it to the paragraph, for example by saying that this escape was itself seen in transmission, if that is what Vidal-Madjar et al. (2003) show and you want the point (Opus); (c) keep it as it is. A cut removes a cited fact, so this is your decision, not a wording fix.
3. **1.1 Exoplanet atmospheres and transmission spectroscopy, `01_introduction.tex:71`** (Opus). Line 71 gives the well-defined, repeating geometry of a transit as the reason to start with transmission. An examiner may object that a secondary eclipse also has a well-defined geometry that repeats every orbit, so this reason does not single out transmission. Is the real reason different, for example that the benchmark dims starlight during the transit, or that transmission is the main use of SOSS? Options: keep the reason (entry intro-A-71 changes only the wording), or state the reason that singles out transmission.
4. **1.2 JWST, NIRISS/SOSS and WASP-17 b, `01_introduction.tex:88`** (Opus). Section 1.1 ends by saying that I need 'an instrument ... and a planet', and Section 1.2 then steps back to how planets are found (the 1992 pulsar planets, 1995, Kepler, TESS). Options: (a) keep the order; (b) move this detection paragraph (lines 88-99) to the start of Section 1.1, before 'Exoplanets span a wide range ...', so that 1.1 runs from discovery to atmospheres and 1.2 opens with HST and Spitzer.
5. **1.2 JWST, NIRISS/SOSS and WASP-17 b (Figure 2 caption), `01_introduction.tex:145`** (Opus). 'Visit' first appears in the Figure 2 caption ('the WASP-17~b SOSS visit') and is used throughout Sections 2-5, but it is never defined. A physicist who does not work with SOSS may not know that it means one observation of one transit. Options: (a) define it at line 207, for example 'one SOSS transit of WASP-17~b, which I call the WASP-17~b visit'; (b) write 'observation' in the Figure 2 caption and define 'visit' where the text first uses it.
6. **1.2 JWST, NIRISS/SOSS and WASP-17 b, `01_introduction.tex:187`** (Opus). Lines 189-191 say that subtracting 'a single constant level instead' would bias the depths \citep{RadicaEtAl2023}. Line 345 says that the transitspectroscopy reduction used 'a single scale factor for the background'. Does Radica et al. (2023) mean a flat constant pedestal, or one scale factor for the whole background model? If the latter, 'a single constant level' misdescribes it and could become 'a single scale factor for the whole background'. If the former, the contrast with 'scaled separately on each side' is not parallel, and a reader may confuse the two alternatives.
7. **1.2 JWST, NIRISS/SOSS and WASP-17 b, `01_introduction.tex:207`** (Opus). Line 208 defines a data reduction as 'the chain of software that turns the detector data into a spectrum'. However, 'pipeline' is first used at line 287 without a definition, and Sections 3-5 use 'pipeline' for the software and 'reduction' for a published analysis. Opus proposes: 'A data reduction is the processing that turns the detector data into a spectrum, and the software that performs it is called a pipeline.' This changes the definition, so it is your decision. Options: (a) adopt the two-term definition (then intro-A-209's 'One reduction used Ahsoka ...' fits better than 'was'); (b) keep the current definition and define 'pipeline' somewhere else before line 287.
8. **1.3 How a transmission spectrum is obtained, `01_introduction.tex:304`** (Opus). Line 304 says only that Ahsoka and supreme-SPOON were flat-field corrected with the JWST pipeline, and line 511 says that transitspectroscopy started from count-rate files from the JWST archive. An examiner may ask whether transitspectroscopy applied a flat field at all, because the archive count-rate files are Stage 1 products and are not flat-fielded. If it applied a flat field by other means, a few words would answer the question; if it applied none, the text could say so. This needs checking against Louie et al. (2025) before any wording changes.
9. **1.3 How a transmission spectrum is obtained, `01_introduction.tex:310`** (Opus, Fable). Lines 310-314 give the details of the supreme-SPOON bad-pixel step that Ahsoka used: negative or undefined pixels of the median out-of-transit image, a test for pixels more than five standard deviations from their neighbours in the column, and replacement by the median of the surrounding pixels. Opus suggests cutting these four sentences, leaving only "then flagged and replaced \citep{LouieEtAl2025}.". The reasons are that the detail is not about the background or the extraction, it never comes back, and line 515 says again that Ahsoka used this step. Fable looked at the same overlap and kept the sentences, because line 310 introduces the description of the step. Keep them (Fable) or cut them (Opus)? If the negative-pixel rule is meant to link to something later, such as the negative faint-light pixels, they should stay.
10. **1.6 Research question and objectives, `01_introduction.tex:633`** (Opus, ASTRA). All three reviewers rewrite the ending of the research question, and all three put the two causes in pipeline order ("extracting a spectrum first and fitting the transit without a background term"). Opus asks explicitly whether this swap is acceptable in the research question. ASTRA also proposes splitting it into two questions ("How accurately ...? Does fitting ...?"), which would no longer match the lead-in "The central research question of this project is:". The options are: (a) one question with the new ending (recommended, intro-B-636); (b) two questions (ASTRA), with the lead-in changed to match; (c) keep the current order of the causes and only bring the verb forward: "reduce the biases that can arise from fitting the transit without a background term and from extracting a spectrum first?".
11. **2.1 Detector processing, `02_nova.tex:26`** (Opus). F277W first appears here with no hint of why that exposure shows the field stars. Section 4.1 explains it ('in which the traces of WASP-17 almost vanish'). Add that half-clause here, or leave the explanation to Section 4.1?
12. **2.2 The detector model (Figure 4), `02_nova.tex:38`** (Opus). The Figure 4 graphic (nova_schematic.pdf) says 'retained pixels' and 'fitted to the count rate of every retained pixel', while the text and caption say 'fitted pixels'. It also says 'continuum C_tg'. Change the graphic to say 'fitted pixels'? ('Continuum' is fine once nova-19 defines it.)
13. **2.3 The spatial profile, `02_nova.tex:92`** (Opus). 'I smooth it across neighbouring columns, like a running average' is a simile. If the smoother is a specific kernel (for example a running median or a Gaussian of a given width), naming it would answer the obvious examiner question. Name it, or keep the simile?
14. **2.4 The transit and the spectrum, `02_nova.tex:130`** (Opus). In 'beyond which this calibration would have to be extrapolated', does 'this calibration' mean the combined K (as in 'In this calibration' at line 108) or the PASTASOSS trace and wavelength calibration? Opus proposed 'the PASTASOSS calibration', which matches the 8 September decision on calibration support. It would narrow the referent, though, if the kernel or throughput also limit the cut. Keep 'this calibration', or name PASTASOSS?
15. **2.2-2.6 (notation), `02_nova.tex:152`** (Opus). Several symbols are used twice: b is both the impact parameter (02:152) and the slope b_oc (02:168); a/R_star and the offset a_oc share a; the intercept l_p (Eq. 3) and the log-wavelength l_o share l; the bin widths w_k and the Huber weights w_tp share w; the stellar spectrum s_lambda and the noise factor s_p share s. N_p also has a pixel index but one value per order. Rename some of them (for example l_o to Lambda_o, the slope b_oc to another letter, N_p to N_o), or leave them?
16. **2.5 The continuum, the background and the noise, `02_nova.tex:200`** (Opus). You agreed the field-star sentences today. Once they move to their own paragraph, 'also' in 'Field stars are also left out of the $1/f$ correction' has nothing close to refer to. There are three options. (a) 'Field stars are left out of the off-trace pixels and of the $1/f$ correction' (Opus), which is the version recommended in nova-24. (b) Keep your agreed sentence exactly, with 'also', either in the new paragraph (ASTRA) or at the end of the map paragraph (Fable). (c) Leave the sentences where they are and fix only 'WASP-17~b visit' and the has/have agreement.
17. **2.6 The fit, `02_nova.tex:226`** (Opus). Section 2.6 has no \label. Section 3 (03:66) says the lower-estimate background was 'held in place by the same off-trace pixels (Section~\ref{sec:continuum})', but that holding term is described in 2.6. Add \label{sec:fit} and point 03:66 there, or keep the pointer to 2.5, where the off-trace pixels are introduced?
18. **2.6 The fit, `02_nova.tex:243`** (Opus). The Huber loss is the only standard method in Section 2 without a citation. Add one (for example Huber 1964), or leave it? Adding one means a new bibliography entry.
19. **2.9 A first spectrum of WASP-17 b, `02_nova.tex:317`** (Opus). The medians are given below 1.6 um, from 1.8 to 2.3 um and above 2.3 um, but not from 1.6 to 1.8 um. Is there a reason to leave that band out, and should the text say what it is?
20. **2.9 A first spectrum of WASP-17 b, `02_nova.tex:323`** (Opus). 'The larger difference in the red matters most': matters most for what? If you mean for this project, because the background has the largest effect there, saying so would answer the examiner. Add a few words, or leave it?
21. **2.9 A first spectrum of WASP-17 b, `02_nova.tex:325`** (Opus). nova-42 changes 'which measures the errors' to 'which is designed to measure the errors'. This matches the abstract ('I am therefore building'), Sections 1 and 5 ('is designed to') and the style rule against presenting an untested design as working. Are you happy with the more cautious wording, or do you want to keep 'measures'?
22. **3.2 Injecting into the raw reads (PDF p. 15), `03_benchmark.tex:32`** (Opus, Fable). What is "the reference atmosphere"? It is used in Section 3.2, Section 3.3 and the Figure 6 caption but never introduced. Options: (a) the minimal clause in entry 03-32, "one injected atmosphere, which I call the reference atmosphere", which says only what the abstract supports; (b) a fuller clause saying what it is (for example which model atmosphere of WASP-17 b, and that it is the one used in every test of Section 3), which only you can supply.
23. **3.2 Injecting into the raw reads / 3.3 Which light belongs to the star (PDF pp. 15-16), `03_benchmark.tex:33`** (Fable). Section 3.2 says NOVA's error rose "from 125 to 182 ppm", and Section 3.3 then gives 124 ppm under the lower estimate. Fable's fact sheet has these as different runs (124.8 for the count-rate injection, 124.0 for the lower estimate on the raw reads), but a reader will ask whether 124 is the 125 again and why the error fell from 182 to 124. Options: add one clause at the start of Section 3.3 giving the reason (for example, if it is because the three injections of Section 3.3 dim the measured wings and the first raw-read injector did not, say so), or leave both numbers as they are.
24. **3.2 Injecting into the raw reads (PDF p. 15), `03_benchmark.tex:43`** (Opus). The spectrum was "about 90 ppm too deep", yet the 1/f correction made "the transit ... about 1 to 2% too deep". At a depth of about 1.5%, 1 to 2% is roughly 150 to 300 ppm, more than the whole 90 ppm, and the correction caused only about half of the increase. Is the 1 to 2% local (0.85 to 1.75 um in order 1) or relative to something else? If so, the sentence should say so; if not, one of the numbers needs checking against the source.
25. **3.3 Which light belongs to the star (PDF p. 16), `03_benchmark.tex:96`** (Opus). "Neither estimate is the truth" says that both are wrong, whereas the next two sentences only say that each may be wrong or is not determined. Did you mean "Neither estimate is known to be right"? Left unchanged because it would change the meaning.
26. **3.4 The real data cannot decide (PDF p. 16), `03_benchmark.tex:114`** (Opus). "Too noisy to tell the cases apart": which cases? If they are "all of this light is starlight" and "none of it is" (or the lower and upper estimates), naming them would help. Rewrite R4 keeps "the cases" until you say which.
27. **4.1 Measuring the star, `04_measured_benchmark.tex:48`** (Opus). The same field objects are called "compact blobs" (lines 48 and 65), "compact spots" (line 68) and "compact sources" (line 86 and Figure 7); "compact bumps" (line 64) describes their imprint on the trace. measured-67 makes line 68 "compact sources". Should "blobs" stay once as the plain first description at line 48, with "compact sources" afterwards (including line 65), or should "compact sources" be used throughout?
28. **4.1 Measuring the star, `04_measured_benchmark.tex:98`** (Opus). ExoCTK (line 98, line 103, the Figure 7 caption and legend) is neither expanded nor cited, and references.bib has no entry for it. "The standard model" also reads oddly to a physicist and clashes with "a standard calibration curve" at line 222. Options: "the default mapping of the ExoCTK contamination tool" with a citation (the Figure 7 legend "Gaia, standard model" would then need the same change in the figure script), or keep the current wording.
29. **4.1 Measuring the star, `04_measured_benchmark.tex:100`** (Opus). Lines 100-102: at the best position the sliding search matches seven of the nine predicted images, but the fit then uses "the eight pairs found this way". Opus reports that both numbers match the source file (7 of 9 at the best position, 8 pairs), but a reader will ask where the eighth pair came from. Options: add one clause saying how the eighth pair was found (for example, after a first refit), or leave the text as it is.
   - **Opus checked the injector's matching script** (`stageA/A5/scripts/a5_03_project_detect_match.py`). The sliding search counts predictions only inside the strip and finds 7 of 9. The least-squares fit then matches mutual-nearest pairs again after each step, over a slightly wider area, and that added the eighth pair. Suggested clause: "I then fitted the six numbers in $\mathbf{A}$ and $\mathbf{t}$ by least squares, matching the pairs again after each fit, which added an eighth pair."
30. **4.1 Measuring the star (Figure 8 and 9 captions), `04_measured_benchmark.tex:158`** (Opus, Fable). The captions of Figures 8 and 9 (lines 158 and 180) say the cleaned image was made "before the corrections for the sky and the halo of the moved star". Section 4.1 describes the halo correction (lines 42-45) but no correction of the cleaned image for the sky; the nearest statements are the sky-alone estimate at the dark spots and the 1% agreement of the zodiacal levels. Options: name the sky correction in one sentence in Section 4.1 (for example after line 31), or reduce both captions to "the correction for the halo of the moved star".
31. **4.1 Measuring the star (Figure 9 caption), `04_measured_benchmark.tex:174`** (Opus). In "dashed where the far-wing model is used, which depends on the distance from the nearest trace", does "which" mean that the model itself is a function of the distance from the nearest trace, or that where the dashed part starts depends on which trace is nearest? Entry measured-176 assumes the second, which is ASTRA's reading. If the first is meant, the caption should say so instead, for example "the far-wing model, which is a function of the distance from the nearest trace".
32. **4.2 Injecting the star, `04_measured_benchmark.tex:204`** (Opus). Lines 204-211 describe the spectral cases in the present tense ("I take the wavelength ... and split the light"), then say "I have not yet built these spectral cases". Options: switch to "I will take ... and split" so that the tense matches the status (style rule: describe what is implemented, not an unbuilt design), or keep the present as a description of the design. Not proposed as an entry because it changes agreed text.
33. **4.2 Injecting the star / 4.4 Limitations, `04_measured_benchmark.tex:210`** (Fable). Line 210 says the limb darkening for the spectral cases "is still to be chosen", whilst line 333 says "the injected limb darkening follows one quadratic law computed from PHOENIX models of the star". If line 333 describes the grey case, "For the grey case, the injected limb darkening follows ..." would reconcile them. If both describe the same thing, one of them needs to change.
34. **4.4 Limitations, `04_measured_benchmark.tex:319`** (Fable). Section 4.4 counts six limitations with "Firstly ... Fifthly, Finally". If "Fourthly" and "Fifthly" feel heavy, the fourth and fifth could open "The injection also adds light ..." and "The exposure also lasts only 2.68~h ...", with no change of content. A matter of judgement, not a correction.
35. **4.4 Limitations, `04_measured_benchmark.tex:330`** (Opus). Line 330 says "None of the four pipelines", but Section 4 never says which four; only Section 5 names NOVA, exoTEDRF, Ahsoka and transitspectroscopy. Options: name them in Section 4.3, where "Each pipeline runs its own workflow" is introduced; point to Section 5; or leave it.
36. **4.4 Limitations, `04_measured_benchmark.tex:333`** (Opus). PHOENIX has no citation, whereas STAGGER is cited (MagicEtAl2015). Add Husser et al. (2013)? This adds a reference, so it is Davide's call.
37. **5.2 Research plan, Paper 1 and Paper 2 (PDF pp. 23-24), `05_discussion_plan.tex:45`** (Opus, Fable). The proposal to repeat programme 4476 appears in Section 4.4 (last paragraph, with the full details and "stars of different temperatures"), again with the same details in Paper 1 ("cooler stars"), at the end of Paper 2 ("cooler stars") and, for NIRSpec, in Paper 4. Options: keep all and only fix the Paper 1 grammar (ASTRA, the recommended entry 05-45); trim Paper 1 to "for several cooler stars (Section 4.4)" (Opus); cut the last sentence of Paper 2 (Fable item 85). Cuts are your call. Also check that "cooler" (Section 5) and "different temperatures" (Section 4.4) say what you mean.
38. **5.2 Research plan, Paper 2 (PDF p. 24), `05_discussion_plan.tex:69`** (Opus). HAT-P-26 b: does "NOVA's differences" mean the differences between NOVA's spectra and those of the other pipelines? Entry 05-69 and rewrite R6 assume so; if you meant differences from the published spectra, the wording should say that instead.
39. **5.2 Research plan, Paper 4 (PDF p. 24), `05_discussion_plan.tex:103`** (Opus). "Extend NOVA and the benchmark to NIRSpec, and validate each on injected data": the benchmark itself is checked against the real exposure (Section 4), not on injected data. Is "each" meant to cover the benchmark?
40. **5.2 Research plan, Paper 4 (PDF p. 24), `05_discussion_plan.tex:106`** (Opus). "Favour a possible water world" stacks two hedges ("favour" and "possible"). Damiano et al. say "potentially habitable water world". Would "favour a water world" or "are consistent with a water world" be closer to what you mean? Not proposed as a change because it alters the hedge.
41. **5.2 Research plan, Paper 5 (PDF p. 24), `05_discussion_plan.tex:113`** (Opus). "Whether a detector-level analysis also makes them more reliable": "also" presupposes that NOVA makes transit spectra more reliable, which Paper 1 has yet to show. Keep "also" or drop it? Entry 05-112 keeps it.
42. **5.2 Research plan, Figure 11 (Gantt chart, PDF p. 25), `05_discussion_plan.tex:164`** (Opus). Is the Gantt bar "Thesis integration" meant as turning the papers into thesis chapters? If so, entry 05-164 ("Thesis chapters from papers") says it without clashing with "integration" as a detector exposure; if it means something else, the label should say that. Fable found the labels fine as they are.
43. **Use of generative AI (unnumbered, PDF p. 25), `06_ai_use.tex:3`** (Fable). "OpenAI's ChatGPT (Astra 6)": Opus 5.5 and Fable 5.1 are public model names an examiner can look up. If "Astra 6" is not a public model name, "OpenAI's ChatGPT" alone, or the public model name, may be safer.

## 3. Tier 1: must fix (45)

### Section 1, Introduction

#### 1 Introduction and Literature Review (opening paragraph) · `01_introduction.tex:11` · repetition · proposed by Opus, Fable, ASTRA

Current:
```latex
themselves, and in the same fit it fits whatever background the earlier
```
Recommended:
```latex
themselves, and the same fit includes whatever background the earlier
```
Why: 'In the same fit it fits' repeats 'fit', and all three reviewers flagged it. The new wording keeps the key point that one fit covers both the transit and the background.

Note: I chose Opus's wording because Fable's 'together with' can be parsed as 'the pixels together with the background'. ASTRA's 'without first compressing' adds 'first', which suggests that NOVA compresses the images later, so it changes the meaning slightly. Also covered by rewrite intro-A-R1.

Other versions:
- Fable: themselves, together with whatever background the earlier
- ASTRA: (replaces lines 9-12 from 'NOVA does not') NOVA fits the transit directly to the detector pixels, without first compressing the images into spectra. The same fit includes any background left by the earlier subtraction.

<sub>id: intro-A-11</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:28` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
If the stellar disc were uniformly bright (in reality it dims towards its edge, an effect called limb darkening), the depth of a transit would be approximately
```
Recommended:
```latex
The stellar disc dims towards its edge, an effect called limb darkening. If the disc were instead uniformly bright, the depth of a transit would be approximately
```
Why: A parenthesis with its own appositive interrupts the condition that leads into Eq. 1. All three reviewers split it into the fact followed by the idealisation.

Note: I chose Opus's 'the disc ... instead' because 'it' could be read as 'its edge' or 'limb darkening'. Fable's 'In reality' comes before the idealisation it contrasts with.

Other versions:
- Fable: In reality the stellar disc dims towards its edge, an effect called limb darkening. If it were uniformly bright, the depth of a transit would be approximately
- ASTRA: The stellar disc dims towards its edge, an effect called limb darkening. If it were uniformly bright, the depth of a transit would be approximately

<sub>id: intro-A-28</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:71` · grammar · proposed by Opus, Fable, ASTRA

Current:
```latex
I start with transmission because a transit has a well-defined geometry that repeats with every orbit, making it a convenient test case of how the processing of the data affects the recovered spectrum.
```
Recommended:
```latex
I start with transmission spectroscopy because a transit has a well-defined geometry that repeats with every orbit. This makes a transit a convenient way to test how the processing of the data affects the recovered spectrum.
```
Why: 'Making it' dangles, since it could refer to the geometry, the orbit or the transit, and 'test case of how' is unidiomatic. All three reviewers split the sentence.

Note: Merger: Fable's 'transmission spectroscopy' names the technique, which matches 'one of three ways' earlier in the paragraph. Opus's 'This makes a transit' replaces the vague 'it'. The stated reason is unchanged; whether it singles out transmission is a separate question.

Other versions:
- Opus: I start with transmission because a transit has a well-defined geometry that repeats with every orbit. This makes a transit a convenient way to test how the processing of the data affects the recovered spectrum.
- Fable: I start with transmission spectroscopy because a transit has a well-defined geometry that repeats with every orbit. This makes it a convenient case for testing how the processing of the data affects the recovered spectrum.
- ASTRA: I start with transmission because a transit has a well-defined geometry that repeats with every orbit. This makes it a convenient test of how data processing affects the recovered spectrum.

<sub>id: intro-A-71</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:133` · clarity · proposed by ASTRA, Fable, Opus

Current:
```latex
An optical element called GR700XD, a grism (a prism carrying a diffraction grating) combined with a prism, spreads the light into several copies of the spectrum, called orders
\citep{AlbertEtAl2023}.
```
Recommended:
```latex
An optical element called GR700XD spreads the light into several copies of the spectrum, called orders \citep{AlbertEtAl2023}. It combines a grism, a prism carrying a diffraction grating, with a second prism.
```
Why: Thirteen words, including a parenthesis inside an appositive, sit between the subject and its verb, and 'prism' appears twice in the insertion. The new version says what GR700XD does first, then what it is, so it reads at once.

Note: The citation stays after the first sentence, where ASTRA and Fable put it. Opus moves it to the end of the second sentence. Either placement keeps Albert et al. on the GR700XD description.

Other versions:
- Opus: An optical element called GR700XD spreads the light into several copies of the spectrum, called orders. GR700XD combines a grism, which is a prism carrying a diffraction grating, with a second prism \citep{AlbertEtAl2023}.
- Fable: An optical element called GR700XD spreads the light into several copies of the spectrum, called orders \citep{AlbertEtAl2023}. It is a grism, a prism that carries a diffraction grating, combined with a second prism.

<sub>id: intro-A-133</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:140` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
cylindrical lens spreads the light over about 23 detector rows, so that bright stars can be observed without saturating the pixels, and so that small pointing jitter
```
Recommended:
```latex
cylindrical lens spreads the light over about 23 detector rows. Bright stars can then be observed without saturating the pixels, and small pointing jitter
```
Why: The sentence has 44 words, with two chained 'so that' clauses and a definition inside the second. All three reviewers split it.

Note: Opus and Fable gave the same wording, which I recommend here. ASTRA's version moves the flat-field definition to the end, so it no longer sits before the verb, but it opens with a vague 'This allows'. Either is acceptable.

Other versions:
- ASTRA: (replaces to the end of the sentence) cylindrical lens spreads the light over about 23 detector rows. This allows bright stars to be observed without saturating the pixels and reduces the effects of small pointing jitter and errors in the flat field, the map of each pixel's sensitivity \citep{AlbertEtAl2023,JDoxNIRISSSOSS2026}.

<sub>id: intro-A-140</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:172` · AI tell · proposed by Opus, Fable

Current:
```latex
SOSS is slitless out of necessity, not by choice.
```
Recommended:
```latex
SOSS is slitless out of necessity.
```
Why: 'Not by choice' is the banned 'not X, but Y' contrast reflex. The next sentence already gives the reason.

Note: I chose Opus's cut because it leaves the following sentence unchanged. Fable's merge makes one 40-word sentence.

Other versions:
- Fable: (replaces this sentence and the next) SOSS has no slit because a slit must sit where the optics form an image of the sky before the light is dispersed, and when SOSS was developed, NIRISS had no optics that form such an image \citep{AlbertEtAl2023}.

<sub>id: intro-A-172b</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:175` · LaTeX · proposed by Opus, Fable, ASTRA

Current:
```latex
Its level changes abruptly
near detector column 700 (Figure~\ref{fig:soss-detector-orders}), \citep{AlbertEtAl2023,LouieEtAl2025},
```
Recommended:
```latex
As Figure~\ref{fig:soss-detector-orders} shows, its level changes abruptly near detector column 700 \citep{AlbertEtAl2023,LouieEtAl2025},
```
Why: The stray comma before \citep prints '(Figure 2), (Albert et al., 2023; Louie et al., 2025), at about 2.15 µm', with two bracket groups in a row. Putting the figure first removes both problems and keeps each citation on the same claim.

Note: Merger adjustment of Opus's version: 'As Figure 2 shows, its level' keeps 'its' clearly referring to the background, not to the figure. I do not recommend Fable's version, because merging the two citations would also attribute the 2.15 µm value to Louie et al. ASTRA's version fixes the comma but leaves the figure and citation brackets side by side. The sentence continues unchanged with ', at about 2.15 µm in order 1 \citep{AlbertEtAl2023}.'

Other versions:
- Opus: Figure~\ref{fig:soss-detector-orders} shows that its level changes abruptly near detector column 700 \citep{AlbertEtAl2023,LouieEtAl2025},
- ASTRA: (replaces to the end of the sentence) Its level changes abruptly near detector column 700 (Figure~\ref{fig:soss-detector-orders}) \citep{AlbertEtAl2023,LouieEtAl2025}. In order 1, this corresponds to about $2.15\,\mu\mathrm{m}$ \citep{AlbertEtAl2023}.
- Fable: (replaces from 'near detector column 700' to the end of the sentence) near detector column 700, at about $2.15\,\mu\mathrm{m}$ in order 1 (Figure~\ref{fig:soss-detector-orders}) \citep{AlbertEtAl2023,LouieEtAl2025}.

<sub>id: intro-A-175</sub>

#### 1.3 How a transmission spectrum is obtained (Figure 3 caption, panel a) · `01_introduction.tex:239` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
A cosmic ray adds a jump, which
  the several groups make visible, so the count rate can be fitted from the
  unaffected differences between reads.
```
Recommended:
```latex
Because there are several groups, a cosmic ray shows up as a jump, and the count rate can be fitted from the unaffected differences between reads.
```
Why: "Which the several groups make visible" is hard to parse, and all three reviewers flagged it. The new sentence gives the cause first.

Note: Merger adjustment. This keeps Opus's structure but says "there are several groups" in place of "the detector is read several times", because the sentence just before it in the caption already says that. Fable's version changes "can be fitted" to "is fitted", so it is not preferred.

Other versions:
- Opus: Because the detector is read several times, a cosmic ray shows up as a jump, and the count rate can be fitted from the unaffected differences between reads.
- Fable: A cosmic ray adds a jump. With several groups the jump can be seen, and the count rate is fitted from the unaffected differences between reads.
- ASTRA: A cosmic ray produces a jump that is visible across the successive groups. The count rate can then be fitted from the unaffected differences between reads.

<sub>id: intro-B-239</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:497` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
None found evidence of an atmosphere, but two showed
weak candidate absorption features at different wavelengths, which retrievals
assigned to different gases, and the authors concluded that the features were not real astrophysical signals.
```
Recommended:
```latex
None found evidence of an atmosphere. Two, however, showed weak candidate absorption features at different wavelengths, which retrievals assigned to different gases. The authors concluded that these features were not real astrophysical signals.
```
Why: This 40-word sentence stacks four clauses and buries the authors' conclusion at the end. All three reviewers split it.

Note: Fable's "not real" drops "astrophysical signals" and so narrows what the authors concluded; it is not recommended. ASTRA's version is the same as the recommendation without "however".

Other versions:
- ASTRA: None found evidence of an atmosphere. Two showed weak candidate absorption features at different wavelengths, which retrievals assigned to different gases. The authors concluded that these features were not real astrophysical signals.
- Fable: None found evidence of an atmosphere. Two, however, showed weak candidate absorption features at different wavelengths, which retrievals assigned to different gases, and the authors concluded that the features were not real.

<sub>id: intro-B-497</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:522` · banned word · proposed by Opus, Fable, ASTRA

Current:
```latex
Crucially, a good fit
```
Recommended:
```latex
A good fit
```
Why: "Crucially" is on the banned list, and style_check flags it. The sentence makes its point without it.

<sub>id: intro-B-522</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:609` · consistency · proposed by Opus, Fable, ASTRA

Current:
```latex
outside the extraction aperture, the band of pixels that is combined into the spectrum, also called the extraction box.
```
Recommended:
```latex
outside the extraction box, the band of pixels that is combined into the spectrum.
```
Why: The end of the sentence stacks two names and a definition, and all three reviewers flagged it. Sections 3 and 4 use only "extraction box", and Section 2 uses "apertures" for NOVA's own pixel regions.

Note: This goes with intro-B-613. ASTRA's "how much starlight" also drops "of a star"; keeping one name is the clearer fix.

Other versions:
- Fable: outside the extraction aperture or box, the band of pixels that is combined into the spectrum.
- ASTRA: Replace from "That study could not" (line 608): That study could not determine how much starlight falls outside the extraction aperture. This aperture, also called the extraction box, is the band of pixels combined into the spectrum.

<sub>id: intro-B-609</sub>

#### 1.6 Research question and objectives (research question) · `01_introduction.tex:636` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
biases that fitting the transit without a background term, and extracting a spectrum first, can cause?
```
Recommended:
```latex
biases that can arise from extracting a spectrum first and fitting the transit without a background term?
```
Why: The verb "can cause" only comes after two gerund phrases set off by commas, so the research question has to be read twice. The fix keeps "can" and gives the two causes in the order the pipeline applies them.

Note: Fable's "caused by" drops "can" and so asserts that these biases occur; it is not recommended. ASTRA's split gives two questions after "The central research question of this project is:", which announces one, and it drops "the" before "background". All three reviewers independently put the two causes in pipeline order. Because this is the research question, see the question for Davide.

Other versions:
- ASTRA: Two questions, replacing the whole of lines 633-636: How accurately can a transmission spectrum be recovered from the detector images of a JWST NIRISS/SOSS transit observation? Does fitting the transit and background together, directly on the pixels, reduce the biases that can arise from extracting a spectrum first and fitting the transit without a background term?
- Fable: biases caused by extracting a spectrum first and fitting the transit without a background term?

<sub>id: intro-B-636</sub>

### Section 2, NOVA

#### 2.1 Detector processing · `02_nova.tex:23` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
To estimate it, the step subtracts from the group the median out-of-transit
image, scaled by a light curve measured from the data, and takes the median of
what is left in each column outside the trace cores, leaving out field stars
found in a separate exposure through the F277W filter. It then subtracts this
column offset from the original group. For this step only, it subtracts a
scaled background model beforehand and adds it back afterwards.
```
Recommended:
```latex
To estimate this noise, it subtracts from the group the median out-of-transit
image, scaled by a light curve measured from the data. It then takes the median
of what is left in each column outside the trace cores, leaving out field stars
found in a separate exposure through the F277W filter. This column offset is
subtracted from the original group. For this step only, a scaled background
model is subtracted beforehand and added back afterwards.
```
Why: All three reviewers flagged this. The first sentence is about 45 words long with three operations. 'The step' refers to nothing named before it, and the two 'it's in the last sentence refer to different things.

Note: Opus nova-23, Fable 29, ASTRA 25. ASTRA's paragraph P1 changes only these sentences, so this entry covers P1. The recommendation combines Opus's opening, which keeps 'from the group' (ASTRA drops it), with ASTRA's split into three sentences. Fable's version keeps 'the step' and leaves 'leaving out' dangling. ASTRA's 'first' is left out because the background model is subtracted before this ('beforehand').

Other versions:
- Opus: To estimate this noise, it subtracts from the group the median out-of-transit
image, scaled by a light curve measured from the data. It then takes the median of
what is left in each column outside the trace cores, leaving out field stars
found in a separate exposure through the F277W filter, and subtracts this
column offset from the original group. For this step only, a scaled background model is subtracted beforehand and added back afterwards.
- Fable: To estimate it, the step subtracts from the group the median out-of-transit image, scaled by a light curve measured from the data. Outside the trace cores, and leaving out field stars found in a separate exposure through the F277W filter, the median of what is left in each column is the column offset. The step subtracts this offset from the original group. For this step only, it subtracts a scaled background model beforehand and adds it back afterwards.
- ASTRA: To estimate the noise, it first subtracts the median out-of-transit image, scaled by a light curve measured from the data. It then takes the median of the remaining light in each column outside the trace cores, excluding field stars found in a separate exposure through the F277W filter. This column offset is subtracted from the original group. For this step only, a scaled background model is subtracted beforehand and added back afterwards.

<sub>id: nova-03</sub>

#### 2.2 The detector model · `02_nova.tex:52` · clarity · proposed by Opus

Current:
```latex
Four edge columns, the 51 reddest columns of
order~1 (Section~\ref{sec:transit}) and flagged samples are left out.
```
Recommended:
```latex
I leave out four edge columns, the 51 reddest columns of
order~1 (Section~\ref{sec:transit}) and flagged samples, where a sample is one
pixel in one integration.
```
Why: 'Four edge columns, the 51 reddest columns' first reads as if the second phrase described the first, and the reader sees that it is a list only when the verb arrives. 'Sample' is used later (2.5, 2.6) but never defined.

Note: Opus nova-52. See possible errors: Section 2.4 gives the 2.758 um cut but never the number 51.

<sub>id: nova-05</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:123` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
It
is represented by 160 top-hat bins from 0.62 to $2.84\,\mu\mathrm{m}$. Below
$2\,\mu\mathrm{m}$ the bins are about $0.01\,\mu\mathrm{m}$ wide and above it
$0.038\,\mu\mathrm{m}$, wider in the red, where the signal-to-noise ratio is
lower.
```
Recommended:
```latex
The spectrum
is represented by 160 top-hat bins from 0.62 to $2.84\,\mu\mathrm{m}$. The bins
are about $0.01\,\mu\mathrm{m}$ wide below $2\,\mu\mathrm{m}$ and
$0.038\,\mu\mathrm{m}$ wide above it. They are wider in the red, where the
signal-to-noise ratio is lower.
```
Why: All three reviewers flagged this. 'It' could mean the planet or D(lambda), and 'above it 0.038 um, wider in the red, where ...' piles up three short phrases.

Note: Opus nova-123 (adds 'The spectrum'), Fable 32, ASTRA 27. Merger adjustment of ASTRA's split: it keeps Davide's 'where' instead of ASTRA's 'because', so no causal claim is added. The bin widths, which Davide decided earlier, are unchanged.

Other versions:
- ASTRA: The bins are about $0.01\,\mu\mathrm{m}$ wide below $2\,\mu\mathrm{m}$ and $0.038\,\mu\mathrm{m}$ wide above it. They are wider in the red because the signal-to-noise ratio is lower.
- Opus: The spectrum
is represented by 160 top-hat bins from 0.62 to $2.84\,\mu\mathrm{m}$. The bins are about $0.01\,\mu\mathrm{m}$ wide below
$2\,\mu\mathrm{m}$ and $0.038\,\mu\mathrm{m}$ wide above it, in the red, where the signal-to-noise ratio is
lower.
- Fable: Below $2\,\mu\mathrm{m}$ the bins are about $0.01\,\mu\mathrm{m}$ wide, and above it $0.038\,\mu\mathrm{m}$, where the signal-to-noise ratio is lower.

<sub>id: nova-12</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:175` · clarity · proposed by Opus

Current:
```latex
The brightness of the star in each group is a straight line in time,
```
Recommended:
```latex
The continuum, the brightness of the star in each group, is a straight line in time,
```
Why: 'Continuum' is in the title of 2.5, in Figure 4 and in 2.6 ('continuum coefficients'), but the text never says that it means C_tg. A spectroscopist would read it as the part of a spectrum without lines.

Note: Opus nova-175.

<sub>id: nova-19</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:200` · flow · proposed by Opus, Fable, ASTRA

Current:
```latex
Field stars are also left out of the $1/f$ correction (Section~\ref{sec:detector-processing}), but NOVA does not yet treat field-star light that falls on the traces, which it cannot tell apart from the light of the target. A treatment of such light, for example with the positions of field-star spectra that Gaia predicts (Section~\ref{sec:measuring-star}), is future work, needed for both the benchmark and the WASP-17~b visit. The
maps are made orthonormal over these pixels. The maps and these pixels were
chosen once from the WASP-17 visit, where eight maps predicted held-out strips
of the off-trace image better than two or four. How well the maps
describe the background under the traces, and how much an error of the maps
there changes the depths, has not yet been tested.
```
Recommended:
```latex
The
maps are made orthonormal over these pixels. The maps and these pixels were
chosen once from the WASP-17~b visit, where eight maps predicted held-out strips
of the off-trace image better than two or four. I have not yet tested how well
the maps describe the background under the traces, or how much an error in the
maps there would change the depths.

Field stars are left out of the off-trace pixels and of the $1/f$ correction
(Section~\ref{sec:detector-processing}), but NOVA does not yet treat
field-star light that falls on the traces, which it cannot tell apart from the
light of the target. A treatment of such light, for example with the positions
of field-star spectra that Gaia predicts (Section~\ref{sec:measuring-star}),
is future work, needed for both the benchmark and the WASP-17~b visit.
```
Why: All three reviewers flagged this. The field-star sentences added on 9 October sit between the off-trace pixels and 'The maps are made orthonormal over these pixels', so 'these pixels' now points three sentences back. Moving them into a short paragraph of their own fixes this, and the edit also fixes the agreement error in 'How well ..., and how much ..., has'.

Note: Opus nova-200, Fable 35 and 3A, ASTRA 29 and P2. The recommended text is Opus's and makes five changes. (1) The field-star sentences become their own paragraph (Opus, ASTRA; Fable keeps one paragraph). (2) 'also' becomes 'left out of the off-trace pixels and of', because in a new paragraph 'also' has nothing close to refer to (Opus only). Davide agreed this sentence today, so this is also in the questions. (3) 'WASP-17 visit' becomes 'WASP-17~b visit' (Opus). (4) The agreement error is fixed with the active 'I have not yet tested ... or how much ... would change' (Opus). (5) 'error of the maps' becomes 'error in the maps' (Opus, ASTRA). Every fact, both \ref commands and 'for example ... Gaia predicts' are kept. Also covered by paragraph rewrite nova-PR2.

Other versions:
- Fable: Keep one paragraph: move the two field-star sentences, unchanged (with 'also'), to the end of the paragraph after 'has not yet been tested.' and change nothing else (Fable 35, paragraph 3A).
- ASTRA: As recommended, but keep 'Field stars are also left out of the $1/f$ correction', 'from the WASP-17 visit' and '..., has not yet been tested.', with 'error in the maps' and 'over these off-trace pixels' (P2).
- Opus: If the agreed field-star wording must stay exactly as it is: keep 'Field stars are also left out of the $1/f$ correction' and do not start a new paragraph; still fix 'WASP-17~b visit' and the agreement ('I have not yet tested how well the maps describe ..., or how much an error in the maps there would change the depths.').

<sub>id: nova-24</sub>

#### 2.6 The fit · `02_nova.tex:237` · LaTeX · proposed by Opus, Fable

Current:
```latex
\right\rangle_{o}\right],
```
Recommended:
```latex
\right\rangle_{o}\right].
```
Why: Eq. 8 ends with a comma, but the next line starts a new sentence ('The first term ...'), so the PDF reads '..., (8) The first term'. The comma is left over from an earlier 'where' clause.

Note: Opus nova-237, Fable 38. A visible error in the PDF.

<sub>id: nova-28</sub>

#### 2.9 A first spectrum of WASP-17 b · `02_nova.tex:316` · grammar · proposed by Opus

Current:
```latex
spectrum is deeper throughout. After interpolating the published spectrum to
the NOVA bins, NOVA is deeper by a median of about
```
Recommended:
```latex
spectrum is deeper at every wavelength. With the published spectrum interpolated
to the NOVA bins, the NOVA spectrum is deeper by a median of about
```
Why: 'After interpolating ..., NOVA is deeper' is a dangling participle: NOVA did not do the interpolating, and NOVA is a method, not a spectrum. 'Throughout' can also be read as 'throughout the range below 1.8 um'.

Note: Opus nova-316. 'At every wavelength' is the wording of the approved abstract and of 05:19-20.

<sub>id: nova-40</sub>

### Section 3, Building a benchmark

#### 3.1 What a benchmark needs (PDF p. 15) · `03_benchmark.tex:7` · AI tell · proposed by Opus, Fable, ASTRA

Current:
```latex
For a real planet the true spectrum is unknown. An injection test supplies a
truth: a known transmission spectrum is added to detector data, and the
spectrum that each method recovers is compared with it.
```
Recommended:
```latex
For a real planet the true spectrum is unknown, so an injection test supplies
one. It adds a known transmission spectrum to detector data and compares it
with the spectrum that each method recovers.
```
Why: "Supplies a truth: ..." is a colon reveal, and "a truth" is odd English. All three reviewers flagged it.

Note: Merger adjustment: Opus's "so ... supplies one" keeps the link that the test provides the missing truth (ASTRA's version drops it), with ASTRA's word order so the sentence ends on "the spectrum that each method recovers" instead of a trailing "with it".

Other versions:
- Opus: For a real planet the true spectrum is unknown, so an injection test supplies one. It adds a known transmission spectrum to detector data and compares the spectrum that each method recovers with it.
- Fable: For a real planet the true spectrum is unknown. An injection test supplies one. A known transmission spectrum is added to detector data, and the spectrum that each method recovers is compared with it.
- ASTRA: For a real planet the true spectrum is unknown. An injection test adds a known transmission spectrum to detector data and compares it with the spectrum recovered by each method.

<sub>id: abs-s3-s5-s6-preamble-03-7</sub>

#### 3.2 Injecting into the raw reads (PDF p. 15) · `03_benchmark.tex:32` · clarity · proposed by Opus, Fable

Current:
```latex
NOVA's root-mean-square error for the reference atmosphere
```
Recommended:
```latex
NOVA's root-mean-square error for one injected atmosphere, which I call the reference atmosphere,
```
Why: "The reference atmosphere" is used here, in Section 3.3 and in the Figure 6 caption, but is never introduced anywhere in the report.

Note: Opus's version keeps the exact name that the caption and Section 3.3 use; Fable's never states the name. Both only say what the abstract supports ("one injected atmosphere"). See the question on what the reference atmosphere is, which would allow a fuller gloss, and the question on 125 versus 124 ppm.

Other versions:
- Fable: (replacing "On the same data, NOVA's root-mean-square error for the reference atmosphere then rose") On the same data, with the one injected atmosphere that I use as a reference throughout this section, NOVA's root-mean-square error then rose

<sub>id: abs-s3-s5-s6-preamble-03-32</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:61` · clarity · proposed by Opus

Current:
```latex
The lower estimate counts as starlight near the traces only
the light explained by a model of the star.
```
Recommended:
```latex
In the first, the lower estimate, only the light that a model of the star
explains counts as starlight near the traces.
```
Why: Garden path: the object of "counts" is delayed by two modifiers, so the sentence has to be read twice. "In the first" also tells the reader this is the first of the three injections just announced.

Note: Merger adjustment: keeps Opus's "In the first," but puts "near the traces" at the end, so "that" cannot attach to "the traces" and the definition parallels the upper estimate's "counts all the light in the box as starlight". Also covered by rewrite R2.

Other versions:
- Opus: In the first, the lower estimate, only the part of the light near the traces that a model of the star explains counts as starlight.

<sub>id: abs-s3-s5-s6-preamble-03-61</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:64` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
through ATOCA's model of the detector, together with a smooth background made
of four of NOVA's eight background maps and held in place by the same
off-trace pixels (Section~\ref{sec:continuum}).
```
Recommended:
```latex
through ATOCA's model of the detector. The fit also included a smooth
background, made of four of NOVA's eight background maps and held in place by
the off-trace pixels that NOVA uses (Section~\ref{sec:continuum}).
```
Why: A 49-word sentence with four stacked modifiers, and "the same off-trace pixels" has nothing in this section to be the same as. All three reviewers split it.

Note: Opus's wording: "also" keeps the joint fit that "together with" expressed, "held in place" is Davide's own phrase (ASTRA's "constrained" is stiffer), and "that NOVA uses" says whose pixels they are. Also covered by rewrite R2.

Other versions:
- Fable: through ATOCA's model of the detector. The fit included a smooth background made of four of NOVA's eight background maps, held in place by the same off-trace pixels (Section~\ref{sec:continuum}).
- ASTRA: through ATOCA's model of the detector. The fit also included a smooth background made of four of NOVA's eight background maps, constrained by the same off-trace pixels (Section~\ref{sec:continuum}).

<sub>id: abs-s3-s5-s6-preamble-03-64</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:107` · grammar · proposed by Opus, Fable, ASTRA

Current:
```latex
by the same fraction as the centre; if part of it is background, the box dims less.
```
Recommended:
```latex
by the same fraction as the centre. If part of the light in the box is background, the box dims less.
```
Why: A 45-word sentence held together by a semicolon, with a vague "it". All three reviewers split it.

Note: Merger adjustment: ASTRA's explicit "the light in the box" replaces the vague "it", but Davide's "dims" is kept rather than ASTRA's "should dim". Also covered by rewrite R3.

Other versions:
- Opus: by the same fraction as the centre. If part of this light is background, the box dims less.
- Fable: by the same fraction as the centre. If part of it is background, the box dims less.
- ASTRA: (whole sentence) If the bright centre of the trace is almost pure starlight and all the light in the extraction box is starlight too, they should dim by the same fraction during transit. If the centre is almost pure starlight but part of the light in the box is background, the box should dim less.

<sub>id: abs-s3-s5-s6-preamble-03-107</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:108` · AI tell · proposed by Opus, Fable, ASTRA

Current:
```latex
repeated it on stretches without a transit: I fitted the same transit shape,
at a time when no transit happens, to the box and to the bright centre.
```
Recommended:
```latex
repeated it on stretches without a transit. I fitted the same transit shape to
the box and to the bright centre, at a time when no transit happens.
```
Why: The colon works as a reveal (Section 3 is over the colon target), and "at a time when no transit happens" splits "fitted ... to the box".

Note: Opus's word order. ASTRA also changes "To check how reliable this comparison is" to "To check the reliability of this comparison"; Davide's wording is plainer and is kept. Also covered by rewrite R3.

Other versions:
- Fable: repeated it on stretches without a transit. I fitted the same transit shape, at a time when no transit happens, to the box and to the bright centre.
- ASTRA: repeated it on stretches without a transit. I fitted the same transit shape to the box and the bright centre at a time when no transit happens.

<sub>id: abs-s3-s5-s6-preamble-03-108</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:110` · clarity · proposed by Opus

Current:
```latex
fitted depths should be zero. Instead, they differed
```
Recommended:
```latex
fitted depths should be zero, so they should agree. Instead, they differed
```
Why: The test is whether the two depths agree, but the sentence only says each should be zero, so "Instead, they differed" jumps a step.

Note: Merger adjustment: "so they should agree" echoes "agreed to within about 1%" two sentences earlier, so the reader compares the two results on the same footing. Opus called this a logic slip; it is readable as is, hence tier 2. Also covered by rewrite R3. Opus: promoted to tier 1, because it is a logic slip an examiner will notice.

Other versions:
- Opus: fitted depths should be zero, and so should their difference. Instead, the two depths differed
- Fable: No change proposed.
- ASTRA: No change (his rewrite keeps the sentence).

<sub>id: abs-s3-s5-s6-preamble-03-110</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:114` · AI tell · proposed by Opus, Fable, ASTRA

Current:
```latex
Only this range gives a clear answer: at 1.75 to $2.1\,\mu\mathrm{m}$ the measurement is too noisy to tell the cases apart, and at 2.1 to $2.8\,\mu\mathrm{m}$ the light appears
```
Recommended:
```latex
Only this range gives a clear answer. At 1.75 to $2.1\,\mu\mathrm{m}$, the measurement is too noisy to tell the cases apart. At 2.1 to $2.8\,\mu\mathrm{m}$, the light appears
```
Why: Colon reveal, flagged by all three. Each of the other two ranges then gets its own sentence.

Note: ASTRA's three-sentence version is chosen because the two ranges are separate findings. Also covered by rewrite R4.

Other versions:
- Opus: Only this range gives a clear answer. At 1.75 to $2.1\,\mu\mathrm{m}$ the measurement is too noisy to tell the cases apart, and at 2.1 to $2.8\,\mu\mathrm{m}$ the light appears
- Fable: Same as Opus.

<sub>id: abs-s3-s5-s6-preamble-03-114b</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:114` · AI tell · proposed by Opus, Fable

Current:
```latex
it depends on how the detector behaves: if the fit allows
```
Recommended:
```latex
it depends on how the detector behaves. If the fit allows
```
Why: Colon reveal, the second in this paragraph.

Note: Also covered by rewrite R4.

<sub>id: abs-s3-s5-s6-preamble-03-114c</sub>

### Section 4, The measured benchmark

#### 4.1 Measuring the star · `04_measured_benchmark.tex:20` · consistency · proposed by Opus, Fable

Current:
```latex
This second exposure has 150 integrations covering
2.68~h, and it is the one into which I inject the star.
```
Recommended:
```latex
This second exposure, which I call the moved exposure, has 150 integrations
covering 2.68~h. It is the one into which I inject the star.
```
Why: "The moved exposure" (Davide's term, used in the abstract, the Figure 9 and 10 captions and line 268) is never defined, and the text calls the same exposure "second", "moved" and "real". Name it here, where it is introduced.

Note: Merger: Fable's "which I call" (reads as a naming) with Opus's split. The follow-up renamings are measured-36, -54, -63, -145, -187 and -194. "The second" at line 25 stays because it pairs with "the first exposure". "The real exposure" at lines 227 and 233 contrasts real with injected light and can stay; line 269 is fixed by measured-267.

Other versions:
- Opus: This second exposure, the moved exposure, has 150 integrations covering
2.68~h. It is the one into which I inject the star.
- Fable: This second exposure, which I call the moved exposure, has 150 integrations covering 2.68~h, and it is the one into which I inject the star.

<sub>id: measured-20</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:47` · clarity · proposed by Opus

Current:
```latex
because they moved with the telescope
```
Recommended:
```latex
because their positions on the detector changed when the telescope moved
```
Why: Field sources are fixed on the sky; only their position on the detector changed. Read literally, "moved with the telescope" is physically wrong.

Note: Merger adjustment: avoids Opus's "moved ... moved". The figure reference that follows is unchanged.

Other versions:
- Opus: because they moved on the detector when the telescope moved

<sub>id: measured-47</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:67` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
Gaia, however, also tells me where
the spectra of known stars fall, which a search for compact spots cannot
find, even for stars that lie off the strip.
```
Recommended:
```latex
Gaia, however, also tells me where
the spectra of known stars fall, even for stars that lie off the strip. A
search for compact sources cannot find these spectra.
```
Why: "Which" can attach to Gaia or to where the spectra fall, and "even for stars off the strip" then attaches to the wrong verb. All three reviewers flagged it.

Note: Opus's version. It keeps "however", which ASTRA drops; the contrast with the previous sentence ("the images themselves are needed") is part of the meaning. "Compact sources" matches line 86 and the Figure 7 caption.

Other versions:
- Fable: Gaia, however, also tells me where the spectra of known stars fall, even for stars that lie off the strip, and a search for compact spots cannot find these spectra.
- ASTRA: Gaia also tells me where the spectra of known stars fall, even when the stars lie off the strip. A search for compact spots cannot locate these spectra.

<sub>id: measured-67</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:86` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
To locate the compact
sources, I first removed everything that is smooth along the rows, such as
the traces and the sky, by subtracting from each row a running median over 51
columns, and removed the $1/f$ stripes by subtracting the median of each
column. I then smoothed the result slightly, with a Gaussian of 1.5 pixels,
and flagged
```
Recommended:
```latex
To locate the compact
sources, I first subtracted a running median over 51 columns from each row.
This removed everything that is smooth along the rows, such as the traces and
the sky. I then removed the $1/f$ stripes by subtracting the median of each
column, smoothed the result slightly with a Gaussian of 1.5 pixels,
and flagged
```
Why: One sentence of more than 45 words with two "removed ... by" clauses, and the effect comes before the action. The split gives one step per clause. All three reviewers flagged it.

Note: Opus's structure with ASTRA's more natural word order ("subtracted X from each row"). Folding the smoothing into the 1/f sentence avoids ASTRA's two consecutive "I then". Also covered by rewrite measured-R1.

Other versions:
- Opus: To locate the compact
sources, I first subtracted from each row a running median over 51 columns.
This removed everything that is smooth along the rows, such as the traces and
the sky. I then removed the $1/f$ stripes by subtracting the median of each
column, smoothed the result slightly with a Gaussian of 1.5 pixels,
and flagged
- Fable: To locate the compact sources, I first removed everything that is smooth along the rows, such as the traces and the sky, by subtracting from each row a running median over 51 columns. I removed the $1/f$ stripes by subtracting the median of each column. I then smoothed the result slightly, with a Gaussian of 1.5 pixels, and flagged
- ASTRA: To locate the compact sources, I first subtracted a running median over 51 columns from each row. This removed everything smooth along the rows, such as the traces and the sky. I then removed the $1/f$ stripes by subtracting the median of each column. [followed by the current "I then smoothed ..."]

<sub>id: measured-86</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:105` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
Programme 4476 cannot provide such a fit: its field is
sparse, with 208 Gaia stars within $5.4'$ of the target against 1,455 around
WASP-17, and its strip contains the undispersed image of at most one, very
faint Gaia star.
```
Recommended:
```latex
Programme 4476 cannot provide such a fit. Its field is
sparse, with 208 Gaia stars within $5.4'$ of the target against 1,455 around
WASP-17. Its strip contains the undispersed image of at most one Gaia star,
which is very faint.
```
Why: A colon reveal followed by a 40-word sentence, and "at most one, very faint Gaia star" reads oddly. All three reviewers flagged the colon.

Note: ASTRA's split, which keeps the two reasons separate as in the original, with Opus's "which is very faint". Opus's "because its field is sparse" would make the strip fact a detail of the sparseness. Do not write "at most one very faint Gaia star" without the comma or the clause, because it would then mean "at most one of the very faint stars". Also covered by rewrite measured-R1.

Other versions:
- Opus: Programme 4476 cannot provide such a fit, because its field is
sparse. It has 208 Gaia stars within $5.4'$ of the target, against 1,455 around
WASP-17, and its strip contains the undispersed image of at most one Gaia
star, which is very faint.
- Fable: Programme 4476 cannot provide such a fit. Its field is sparse, with 208 Gaia stars within $5.4'$ of the target against 1,455 around WASP-17, and its strip contains the undispersed image of at most one, very faint Gaia star.
- ASTRA: Programme 4476 cannot provide such a fit. Its field is sparse, with 208 Gaia stars within $5.4'$ of the target against 1,455 around WASP-17. Its strip contains the undispersed image of at most one, very faint Gaia star.

<sub>id: measured-105</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:109` · clarity · proposed by Opus, Fable

Current:
```latex
Because NOVA may later use the same predictions, agreement between the two would not by itself show
```
Recommended:
```latex
Because NOVA may later use the same Gaia predictions, agreement between NOVA and the injector would not by itself show
```
Why: "The two" follows a sentence about the images and Gaia, so it can be read as that pair, which gives a different claim. The point is that NOVA and the injector could share errors.

Note: Opus's version changes only the ambiguous words; Fable's adds "about the field stars", which narrows the agreement slightly. Also covered by rewrite measured-R1.

Other versions:
- Fable: Because NOVA may later use the same predictions, agreement between the injector and NOVA about the field stars would not by itself show that their light was separated correctly.

<sub>id: measured-109</sub>

#### 4.1 Measuring the star (figure order) · `04_measured_benchmark.tex:111` · LaTeX · proposed by Opus

Current:
```latex
\begin{figure*}[t]
  \centering
  \includegraphics[width=\textwidth]{figures/w17_gaia_mapping.pdf}
```
Recommended:
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
Why: The text cites Figure 8 (programme 4476, line 48) before Figure 7 (the WASP-17 b Gaia map, line 76), so the PDF numbers the figures out of order. Placing the programme-4476 figure first fixes the numbering.

Note: This inserts the programme-4476 figure (lines 151-166, unchanged) before the Gaia figure; the original block at lines 151-166 must then be deleted. Apply measured-156 and measured-162 to the moved copy. After the move, Figures 7 and 8 swap numbers, and all references update automatically. Checked in main.aux: fig:w17-gaia is Figure 7 and fig:4476 is Figure 8.

<sub>id: measured-111</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:206` · clarity · proposed by Opus

Current:
```latex
\citep{BainesEtAl2023Wavelength}, and split the light where the orders overlap
with ATOCA
```
Recommended:
```latex
\citep{BainesEtAl2023Wavelength} and, where the orders overlap, split the
light with ATOCA
```
Why: Garden path: "where the orders overlap with ATOCA" first reads as the orders overlapping with ATOCA.

Note: Both citations are kept; the ATOCA citation that follows is unchanged. See the question on the tense of this paragraph.

<sub>id: measured-204</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:220` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
The detector does not record charge in proportion: as a pixel fills,
each additional electron raises the recorded value a little less.
```
Recommended:
```latex
The recorded value is not proportional to the charge. As a pixel fills,
each additional electron raises it a little less.
```
Why: "Does not record charge in proportion" leaves "in proportion to what?" open, and the colon works as a reveal. All three reviewers flagged it.

Note: Opus's version fixes both the phrase and the colon; Fable fixes only the colon, and ASTRA only the phrase.

Other versions:
- Fable: The detector does not record charge in proportion. As a pixel fills, each additional electron raises the recorded value a little less.
- ASTRA: The recorded value is not proportional to charge: as a pixel fills, each additional electron raises it a little less.

<sub>id: measured-220</sub>

#### 4.3 Testing the injector and the pipelines · `04_measured_benchmark.tex:279` · grammar · proposed by ASTRA, Opus

Current:
```latex
Each pipeline runs its own workflow on the same raw files, set up without
knowledge of the injected transit.
```
Recommended:
```latex
Each pipeline is set up without knowledge of the injected transit and runs
its own workflow on the same raw files.
```
Why: Misplaced modifier: "set up without knowledge" sits next to "raw files" and reads as describing them.

Note: ASTRA's version avoids the comma-fenced insertion between subject and verb.

Other versions:
- Opus: Each pipeline, set up without knowledge of the injected transit, runs its
own workflow on the same raw files.

<sub>id: measured-279</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:315` · clarity · proposed by Fable, Opus, ASTRA

Current:
```latex
It could be added by shifting
```
Recommended:
```latex
Such motion could be added by shifting
```
Why: "It" has no antecedent, because the previous sentence ends on "this". All three reviewers flagged it.

Note: "Motion" covers the shift, and the "stretching" in the same sentence covers the change of shape. ASTRA's version names both but is heavier and uses "motion" twice in one sentence.

Other versions:
- Opus: This motion could be added by shifting
- ASTRA: Such trace motion and shape changes could be added by shifting

<sub>id: measured-315</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:333` · flow · proposed by Opus, Fable, ASTRA

Current:
```latex
allows deviations from it; I still need to give NOVA a reference suited to this star. Both fit the limb darkening freely in the white-light curves.
```
Recommended:
```latex
allows deviations from it. Both fit the limb darkening freely in the white-light curves. I still need to give NOVA a reference suited to this star.
```
Why: All three reviewers flagged the semicolon. Swapping the last two sentences also puts "Both" right after the sentence that names exoTEDRF and NOVA, not after one about NOVA alone.

Note: Davide's own limb-darkening wording: only the punctuation and the sentence order change, and every word is kept. ASTRA's version (see dropped) is not recommended because it removes "In their spectral fits" from NOVA's sentence.

Other versions:
- Fable: allows deviations from it. I still need to give NOVA a reference suited to this star. Both fit the limb darkening freely in the white-light curves.

<sub>id: measured-333</sub>

### Section 5, Discussion and plan

#### 5.1 Discussion (PDF p. 22) · `05_discussion_plan.tex:8` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
has to decide which light
belongs to the star, stated or not, and its verdict holds only under that
decision.
```
Recommended:
```latex
has to decide, whether it says so or not, which light
belongs to the star. Its verdict holds only under that
decision.
```
Why: "Stated or not" dangles after "the star", so it is unclear what may be unstated. All three reviewers flagged it.

Note: Merger adjustment: Fable's position for the aside (after "the star", Opus's "it" could be read as the star) with ASTRA's full stop.

Other versions:
- Opus: has to decide which light belongs to the star, whether or not it says so, and its verdict holds only under that decision.
- Fable: has to decide, whether it says so or not, which light belongs to the star, and its verdict holds only under that decision.
- ASTRA: has to decide which light belongs to the star, whether or not this decision is stated. Its verdict holds only under that decision.

<sub>id: abs-s3-s5-s6-preamble-05-9</sub>

#### 5.2 Research plan, Paper 1 (PDF p. 23) · `05_discussion_plan.tex:41` · clarity · proposed by Opus, Fable

Current:
```latex
held back until NOVA is fixed.
```
Recommended:
```latex
held back until the improvements to NOVA are complete.
```
Why: Right after "improve NOVA", "fixed" reads as "repaired", whereas it means that NOVA stops changing (the sense of "fixed" in Paper 2).

Note: Fable's "improvements" echoes "I will improve NOVA" earlier in the same sentence.

Other versions:
- Opus: held back until the changes to NOVA are complete.

<sub>id: abs-s3-s5-s6-preamble-05-41</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:53` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
NOVA together with those pipelines of each visit's published reductions that
are publicly available, and run each of them on the benchmark as well, so that its errors on the same known case can be measured.
```
Recommended:
```latex
NOVA together with the publicly available pipelines used in each visit's
published reductions. I will also run each of these pipelines on the benchmark, so that its errors on the same known case can be measured.
```
Why: "Those pipelines of each visit's published reductions that are publicly available" is a noun pile with a delayed relative clause, and "each of them ... its" mixes plural and singular. All three reviewers split it.

Note: Opus's wording keeps Davide's "together with". Also covered by rewrite R6.

Other versions:
- Fable: NOVA alongside the publicly available pipelines behind each visit's published reductions. I will also run each of them on the benchmark, so that its errors on the same known case can be measured.
- ASTRA: NOVA alongside the publicly available pipelines used in each visit's published reductions. I will also run each pipeline on the benchmark, so that its errors on the same known case can be measured.

<sub>id: abs-s3-s5-s6-preamble-05-53</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:72` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
\citep{BellEtAl2023},
overlapping the red end of SOSS, where NOVA differs most for WASP-17~b, which
gives an independent check of NOVA's red end.
```
Recommended:
```latex
\citep{BellEtAl2023}.
This range overlaps the red end of SOSS, where NOVA differs most for
WASP-17~b, so it gives an independent check of NOVA's spectrum there.
```
Why: "Overlapping" dangles after the citation, "where ..., which ..." chains two clauses, and "red end" appears twice. All three reviewers split it.

Note: Opus's wording. Also covered by rewrite R6.

Other versions:
- Fable: \citep{BellEtAl2023}. This range overlaps the red end of SOSS, where NOVA differs most for WASP-17~b, and so gives an independent check there.
- ASTRA: \citep{BellEtAl2023}. This overlaps the red end of SOSS, where NOVA differs most for WASP-17~b, and gives an independent check of NOVA's red end.

<sub>id: abs-s3-s5-s6-preamble-05-72</sub>

### Preamble (bibliography layout)

#### Preamble (fixes the bibliography on PDF p. 26) · `preamble.tex:20` · LaTeX · proposed by ASTRA

Current:
```latex
\usepackage[colorlinks=true,allcolors=blue!55!black]{hyperref}
```
Recommended:
```latex
\usepackage{xurl}
\usepackage[colorlinks=true,allcolors=blue!55!black]{hyperref}
```
Why: The two JWST documentation URLs in the bibliography run past the right edge of the page. Loading xurl lets a URL break at any character without changing the address.

Note: Verified by compiling a scratch copy (no ESA file touched): without xurl the log shows overfull boxes of 57.5 pt and 79.3 pt at the two jwst-docs.stsci.edu URLs; with xurl there are no overfull boxes at all and the PDF stays at 26 pages. Opus and Fable did not raise it (Fable could not render the PDF).

<sub>id: abs-s3-s5-s6-preamble-pre-xurl</sub>

## 4. Tier 2: clear improvements (111)

### Section 1, Introduction

#### 1 Introduction and Literature Review (opening paragraph) · `01_introduction.tex:7` · clarity · proposed by Opus, Fable

Current:
```latex
Firstly, the background light is subtracted, and any background that remains is not modelled when the transit is fitted.
```
Recommended:
```latex
The first is the subtraction of the background light. Any background that remains is not modelled when the transit is fitted.
```
Why: After 'I focus on two of them', the sentence 'Firstly, the background light is subtracted' reads like the first processing step, not the first of the two error points. Naming the point directly makes the list clear.

Note: Merger adjustment: I dropped Opus's 'after this subtraction', because the next sentence already says 'An error in that subtraction'. Fable's version keeps 'Firstly' but still opens with the step. Apply this together with intro-A-07b so that the two points stay parallel. Also covered by rewrite intro-A-R1.

Other versions:
- Opus: The first is the subtraction of the background light. Any background that remains after this subtraction is not modelled when the transit is fitted.
- Fable: Firstly, the background is subtracted before the transit is fitted, and any background that remains is left out of the fit.

<sub>id: intro-A-07a</sub>

#### 1 Introduction and Literature Review (opening paragraph) · `01_introduction.tex:7` · clarity · proposed by Opus

Current:
```latex
Secondly, each image is compressed into a one-dimensional spectrum, which can lose
information that the later steps cannot recover.
```
Recommended:
```latex
The second is the compression of each image into a one-dimensional spectrum. This compression can lose information that the later steps cannot recover.
```
Why: As written, 'which' attaches to 'spectrum', but it is the compression that loses information. The new wording also matches intro-A-07a.

Note: Apply this only together with intro-A-07a. Otherwise 'The first is ...' would be followed by 'Secondly, ...'. Also covered by rewrite intro-A-R1.

<sub>id: intro-A-07b</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:25` · repetition · proposed by Opus, Fable

Current:
```latex
The atmosphere helps to distinguish between these possible compositions, and its composition can also hint
```
Recommended:
```latex
The atmosphere helps to distinguish between these possibilities, and its composition can also hint
```
Why: The sentence says 'compositions ... composition'. 'These possibilities' refers back to the different mixtures of rock, ice and gas.

Note: Merger adjustment: Fable's first half and the original second half. Because 'The atmosphere' is the subject, 'its' reads as the atmosphere's composition. Opus's version is more literal (observing it helps) but repeats 'atmosphere'. Fable's 'what it is made of' drops the register. The gas-loss sentence that follows is a separate question.

Other versions:
- Opus: Observing the atmosphere of a planet helps to distinguish between these possibilities, and the composition of the atmosphere can also hint
- Fable: The atmosphere helps to distinguish between these possibilities, and what it is made of can also hint

<sub>id: intro-A-25</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy (Figure 1 caption) · `01_introduction.tex:48` · consistency · proposed by Opus

Current:
```latex
hence the apparent radius of the
```
Recommended:
```latex
hence the effective radius of the
```
Why: The text calls R_p(λ) the 'effective radius' (lines 35-36), but the caption calls it the 'apparent radius'. One thing should have one name.

Note: Apply together with intro-A-48fig, the label inside the figure.

<sub>id: intro-A-48</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:54` · clarity · proposed by ASTRA, Opus

Current:
```latex
Only a thin ring of atmosphere around the planet filters the starlight, so the atmospheric signal, the part of the transit depth that changes with wavelength, is a small fraction of the stellar flux.
```
Recommended:
```latex
The atmospheric signal is the part of the transit depth that changes with wavelength. Only a thin ring of atmosphere around the planet filters the starlight, so this signal is a small fraction of the stellar flux.
```
Why: At present a definition sits between subject and verb after a 'so' clause. Giving the definition its own sentence lets the cause and its effect follow cleanly.

Note: I chose ASTRA's version because Opus's still puts the definition between subject and verb. It also continues naturally from the previous paragraph, which ends on the depth varying with wavelength.

Other versions:
- Opus: Only a thin ring of atmosphere around the planet filters the starlight. The atmospheric signal, the part of the transit depth that changes with wavelength, is therefore a small fraction of the stellar flux.

<sub>id: intro-A-54</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:58` · grammar · proposed by Opus, Fable

Current:
```latex
A class of planets that satisfies these
conditions is the so-called hot Jupiters, gas giants that orbit close to their
stars \citep{Brown2001,Madhusudhan2019}.
```
Recommended:
```latex
Hot Jupiters, gas giants that orbit close to their stars, satisfy these conditions \citep{Brown2001,Madhusudhan2019}.
```
Why: 'A class ... is the so-called hot Jupiters' mixes singular and plural and delays the subject, and 'so-called' sounds dismissive. The claim and the citations are the same.

Note: Opus and Fable proposed identical wording.

<sub>id: intro-A-58</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:77` · clarity · proposed by ASTRA, Opus

Current:
```latex
Inferring the atmosphere from its spectrum is an inverse problem, and it does not always have a unique answer, because different combinations
```
Recommended:
```latex
Inferring the atmosphere from its spectrum is an inverse problem that does not always have a unique answer. Different combinations
```
Why: The sentence runs to 40 words and is held together by 'and it ... because'. The split states the limitation first, then its cause.

Note: ASTRA's version also removes 'and it'. The cause stays clear from the order of the sentences, and the citations stay at the end of the second sentence.

Other versions:
- Opus: Inferring the atmosphere from its spectrum is an inverse problem, and it does not always have a unique answer. Different combinations

<sub>id: intro-A-77</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:103` · repetition · proposed by Opus

Current:
```latex
In 2002, HST found
sodium in the atmosphere of HD~209458~b \citep{CharbonneauEtAl2002}.
```
Recommended:
```latex
The detection of sodium in HD~209458~b, mentioned above, was made with HST in 2002 \citep{CharbonneauEtAl2002}.
```
Why: The same detection, with the same citation, is already given in Section 1.1 (lines 60-62). Acknowledging it adds only the new facts, HST and 2002, so it does not read as a new result.

Note: Leaving the sentence unchanged is also defensible, because the repetition sits in a historical narrative. See also the question on moving the detection paragraph.

<sub>id: intro-A-103</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:109` · consistency · proposed by Opus, Fable

Current:
```latex
such as $1.1$-$1.7\,\mu\mathrm{m}$
```
Recommended:
```latex
such as 1.1 to $1.7\,\mu\mathrm{m}$
```
Why: A hyphen between the numbers prints as a short hyphen, not a range dash. Sections 2-4 write every range as 'X to Y'.

Note: The same fix applies at lines 110, 123, 135 and 197 (see those entries) and at line 490 in Section 1.4.

<sub>id: intro-A-109</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:110` · clarity · proposed by Opus, Fable

Current:
```latex
spectrum, such as one over $0.3$-$5\,\mu\mathrm{m}$, therefore had to be
combined from observations with several instruments of HST and Spitzer, made
at different times
```
Recommended:
```latex
spectrum, such as one over 0.3 to $5\,\mu\mathrm{m}$, therefore had to be combined from observations made at different times with several instruments on HST and Spitzer
```
Why: At present 'made at different times' trails after the instruments and seems to describe them, and instruments are 'on' a telescope, not 'of' it. The range format is fixed as in intro-A-109.

Note: Fable proposed only the range fix here.

Other versions:
- Fable: spectrum, such as one over 0.3 to $5\,\mu\mathrm{m}$, therefore had to be
combined from observations with several instruments of HST and Spitzer, made
at different times

<sub>id: intro-A-110</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:114` · clarity · proposed by Opus, ASTRA

Current:
```latex
Like HST, it is used for exoplanets mainly to
characterise planets that are already known.
```
Recommended:
```latex
Like HST, it is used in exoplanet science mainly to characterise planets that are already known.
```
Why: 'Used for exoplanets mainly to characterise planets' is clumsy and says 'planets' twice.

Note: I chose Opus's wording because it keeps the scope next to 'used', so the sentence cannot be read as JWST being mainly an exoplanet telescope. ASTRA's puts the scope at the end, where it reads as an afterthought.

Other versions:
- ASTRA: Like HST, JWST is used mainly to characterise known planets in exoplanet research.

<sub>id: intro-A-114</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:123` · consistency · proposed by Opus, Fable

Current:
```latex
covers $0.6$-$2.8\,\mu\mathrm{m}$ in one observation
```
Recommended:
```latex
covers 0.6 to $2.8\,\mu\mathrm{m}$ in one observation
```
Why: Range format, as in intro-A-109.

<sub>id: intro-A-123</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:135` · consistency · proposed by Opus, Fable

Current:
```latex
$0.6$-$2.8\,\mu\mathrm{m}$ range mentioned above
```
Recommended:
```latex
range of 0.6 to $2.8\,\mu\mathrm{m}$ mentioned above
```
Why: Range format, as in intro-A-109. The sentence then reads 'Orders 1 and 2 together give the range of 0.6 to 2.8 µm mentioned above.'

Note: Both versions are fine. Opus's avoids the long pre-modifier '0.6 to 2.8 µm range'.

Other versions:
- Fable: 0.6 to $2.8\,\mu\mathrm{m}$ range mentioned above

<sub>id: intro-A-135</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b (Figure 2 caption) · `01_introduction.tex:146` · clarity · proposed by Opus

Current:
```latex
The arrows mark a field star whose light falls on the
  edge of the order-1 trace, and the step in the zodiacal background near
  column 700, to the right of which the background is brighter.
```
Recommended:
```latex
One arrow marks a field star whose light falls on the edge of the order-1 trace. The other marks the step in the zodiacal background near column 700, to the right of which the background is brighter.
```
Why: 'Falls on the edge of the order-1 trace, and the step ...' briefly reads as 'the edge of the trace and of the step'. One sentence per arrow removes the misreading.

Note: The figure has exactly two arrows (figures/plot_soss_detector_scene.py, lines 61-64), so 'one ... the other' is accurate.

<sub>id: intro-A-146</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:167` · AI tell · proposed by Opus, ASTRA

Current:
```latex
However, whilst SOSS measures light precisely, its data are difficult to
```
Recommended:
```latex
Although SOSS measures light precisely, its data are difficult to
```
Why: 'However, whilst' stacks two contrast words, and one is enough.

Note: This removes one 'whilst' only because it is stacked with 'However'. It is not a change of convention (see the cross-section note on whilst/while).

<sub>id: intro-A-167</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:172` · clarity · proposed by Opus

Current:
```latex
The spectra of other stars in the field of view, called field stars, therefore also fall on the detector, and some of them land on the traces of the target
```
Recommended:
```latex
Other stars in the field of view, called field stars, therefore also form spectra on the detector, and some of these spectra land on the traces of the target
```
Why: As written, 'called field stars' could name the spectra, and 'some of them' could mean the spectra or the stars. Making the stars the subject attaches the defined term to the right noun.

<sub>id: intro-A-172a</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:195` · flow · proposed by Opus, Fable

Current:
```latex
\citep{FeinsteinEtAl2023}. I focus on a hot Jupiter, WASP-17~b.
```
Recommended:
```latex
\citep{FeinsteinEtAl2023}.

I focus on the hot Jupiter WASP-17~b.
```
Why: The project's target appears in mid-paragraph, straight after the WASP-39 b example. A new paragraph marks the turn, and 'a hot Jupiter, WASP-17 b' reads as if any hot Jupiter would do.

Note: Fable marks the turn with word order and keeps one paragraph, whereas Opus's paragraph break marks it more clearly. Also covered by rewrite intro-A-R2, which also joins the following two-sentence 'However' paragraph to this one.

Other versions:
- Fable: \citep{FeinsteinEtAl2023}. The planet I focus on is the hot Jupiter WASP-17~b.

<sub>id: intro-A-195</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:197` · consistency · proposed by Opus, Fable

Current:
```latex
WASP-17~b over $0.3$-$5\,\mu\mathrm{m}$,
```
Recommended:
```latex
WASP-17~b over 0.3 to $5\,\mu\mathrm{m}$,
```
Why: Range format, as in intro-A-109.

Note: Also covered by rewrite intro-A-R2.

<sub>id: intro-A-197</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:209` · clarity · proposed by Opus

Current:
```latex
The three reductions were Ahsoka,
which Louie et al.\ introduced, \texttt{transitspectroscopy}
\citep{Espinoza2022TransitSpectroscopy} with the transit-fitting code
\texttt{juliet} \citep{EspinozaEtAl2019}, and supreme-SPOON
\citep{RadicaEtAl2023}, now distributed as exoTEDRF \citep{Radica2024}.
```
Recommended:
```latex
One reduction was Ahsoka, which Louie et al.\ introduced. Another was \texttt{transitspectroscopy} \citep{Espinoza2022TransitSpectroscopy} with the transit-fitting code \texttt{juliet} \citep{EspinozaEtAl2019}. The third was supreme-SPOON \citep{RadicaEtAl2023}, now distributed as exoTEDRF \citep{Radica2024}.
```
Why: The relative clause, the 'with' phrase and four citations are all separated by commas, so a first-time reader cannot tell whether the list has three items or four. One sentence per reduction removes the doubt, with the same names and citations.

Note: Merger adjustment: 'was' fits the current definition at line 208 ('A data reduction is the chain of software'). If Davide adopts the reduction/pipeline distinction in the question, Opus's 'used' fits better.

Other versions:
- Opus: One reduction used Ahsoka, which Louie et al.\ introduced. Another used \texttt{transitspectroscopy} \citep{Espinoza2022TransitSpectroscopy} with the transit-fitting code \texttt{juliet} \citep{EspinozaEtAl2019}. The third used supreme-SPOON \citep{RadicaEtAl2023}, now distributed as exoTEDRF \citep{Radica2024}.

<sub>id: intro-A-209</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:304` · clarity · proposed by Opus, Fable

Current:
```latex
In Ahsoka and supreme-SPOON, the images are then flat-field corrected with the JWST pipeline.
```
Recommended:
```latex
In Ahsoka and supreme-SPOON, the count-rate images were first flat-field corrected with the JWST pipeline.
```
Why: "Then" has nothing to follow, because the sentence before only points to the figure. The sentence describes two particular reductions, so the past tense matches "Ahsoka ... used" later in the paragraph.

Note: Both reviewers chose "first". The paragraph uses the present tense for the general steps and the past tense for particular reductions, and Fable's version stays in the present. See also the question on whether transitspectroscopy applied a flat field.

Other versions:
- Fable: In Ahsoka and supreme-SPOON, the images are first flat-field corrected with the JWST pipeline.

<sub>id: intro-B-304</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:343` · clarity · proposed by Opus

Current:
```latex
Both scaled the background model separately
```
Recommended:
```latex
Both reductions scaled the background model separately
```
Why: "Both" points back three sentences, past a passive sentence about the background, so for a moment it is unclear what it refers to.

<sub>id: intro-B-343</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:352` · clarity · proposed by Opus

Current:
```latex
Ahsoka, which used Eureka! \citep{BellEtAl2022} for its light-curve fits, fitted a linear trend in time together with
the transit model for each light curve, and scaled the expected noise by a
fitted factor.
```
Recommended:
```latex
Ahsoka used Eureka! \citep{BellEtAl2022} to fit each light curve with the transit model and a linear trend in time, and scaled the expected noise by a fitted factor.
```
Why: The "which" clause delays the verb, and the sentence says "fits ... fitted ... fitted". The content is unchanged.

Note: Line 518 also says that Ahsoka used Eureka!; see the cross-section notes.

<sub>id: intro-B-352</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:365` · repetition · proposed by Opus

Current:
```latex
The subtracted background and the extracted spectra are therefore both fixed before the transit fit begins, and the transit fit does not model any background that remains.
```
Recommended:
```latex
The subtracted background and the extracted spectra are therefore both fixed before the transit fit begins.
```
Why: Section 1.4 opens a few lines later with the same point ("Any background that remains after the subtraction is not modelled in the transit fit"), and there it leads on to its consequence.

<sub>id: intro-B-365</sub>

#### 1.4 Two steps where errors could enter · `01_introduction.tex:378` · repetition · proposed by Opus, Fable

Current:
```latex
In all three reductions of WASP-17~b,
the background was subtracted before the light curves were fitted, and the
transit fit held the subtracted background fixed \citep{LouieEtAl2025}. The
transit fit therefore could not correct an error in the subtraction.
```
Recommended:
```latex
In all three reductions of WASP-17~b, the transit fit held the subtracted background fixed \citep{LouieEtAl2025}, so it could not correct an error in the subtraction.
```
Why: Lines 362-365 and 370-371 already say that the background was subtracted before the fit. One sentence keeps the cited fact and its consequence.

Note: Fable's version replaces \citep{LouieEtAl2025} with a section reference, which drops the citation, so Opus's version is recommended. Opus's rewrite of lines 370-384 is just this entry combined with intro-B-372.

Other versions:
- Fable: In all three reductions of WASP-17~b the transit fit held the subtracted background fixed (Section~\ref{sec:detector-to-spectrum}), so it could not correct an error in the subtraction.

<sub>id: intro-B-378</sub>

#### 1.4 Two steps where errors could enter · `01_introduction.tex:417` · repetition · proposed by Fable, Opus

Current:
```latex
orders. ATOCA models
```
Recommended:
```latex
orders. It models
```
Why: Four sentences in a row begin with "ATOCA".

Note: Also covered by rewrite intro-B-R1.

<sub>id: intro-B-417</sub>

#### 1.4 Two steps where errors could enter · `01_introduction.tex:421` · repetition · proposed by Fable, Opus

Current:
```latex
\citep{DarveauBernierEtAl2022}. ATOCA needs
```
Recommended:
```latex
\citep{DarveauBernierEtAl2022}. It needs
```
Why: Four sentences in a row begin with "ATOCA".

Note: Merger adjustment. Line 420 keeps "ATOCA can therefore separate", so the paragraph alternates between "It" and "ATOCA" instead of using "It" three times. Also covered by rewrite intro-B-R1.

Other versions:
- Fable: Also change "ATOCA can therefore separate" (line 420) to "It can therefore separate".

<sub>id: intro-B-421</sub>

#### 1.4 Two steps where errors could enter · `01_introduction.tex:427` · repetition · proposed by Opus

Current:
```latex
afterwards \citep{LouieEtAl2025}. The transit therefore could not help to
separate the starlight from the background.
```
Recommended:
```latex
afterwards \citep{LouieEtAl2025}.
```
Why: This sentence repeats the end of the JExoRES paragraph almost word for word, and the next paragraph makes the same point a third time. The supreme-SPOON example already shows it.

Note: Also covered by rewrite intro-B-R1.

<sub>id: intro-B-427</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:490` · consistency · proposed by Opus, Fable

Current:
```latex
For example, NIRSpec measured the $3$-$5\,\mu\mathrm{m}$ spectrum of
WASP-39~b. For these data, differences between reductions changed the
```
Recommended:
```latex
For example, NIRSpec measured the 3 to $5\,\mu\mathrm{m}$ spectrum of WASP-39~b. Differences between reductions of these data changed the
```
Why: The hyphen prints as a hyphen, not a range dash, and Sections 2 to 5 write ranges with "to". The second sentence also no longer opens with a second "For".

Note: Merger adjustment. Opus's merged sentence speaks of "reductions of the ... spectrum", but a reduction is of the data, not of the spectrum. This entry is part of the report-wide range fix (Fable item 9). Intro lines 109, 110, 123, 135 and 197 belong to the intro-A part.

Other versions:
- Opus: For example, differences between reductions of the 3 to $5\,\mu\mathrm{m}$ NIRSpec spectrum of WASP-39~b changed the
- Fable: Fix the range only: For example, NIRSpec measured the 3 to $5\,\mu\mathrm{m}$ spectrum of WASP-39~b. For these data, differences between reductions changed the

<sub>id: intro-B-490</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:507` · repetition · proposed by Opus, Fable

Current:
```latex
Each subtracted the background from
the images and extracted a spectrum before it fitted the transit. They also
```
Recommended:
```latex
They also
```
Why: This repeats the definition of the extraction-first order that the sentence before has just referred to (Section 1.3).

<sub>id: intro-B-507</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:520` · repetition · proposed by Opus

Current:
```latex
they could also share an error. Their agreement could not reveal an error common to all three. Leaving any remaining background out of the transit fit could cause exactly such a shared error.
```
Recommended:
```latex
they could also share an error, and their agreement could not reveal it. Leaving any remaining background out of the transit fit could cause such a shared error.
```
Why: "An error common to all three" restates "share an error", and "exactly" adds emphasis but no meaning. Three "could"s in a row become two.

<sub>id: intro-B-520</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:525` · repetition · proposed by Opus, Fable

Current:
```latex
light curve, however, still has the shape of a transit, so it can still be
```
Recommended:
```latex
light curve, however, keeps the shape of a transit, so it can still be
```
Why: "Still" appears twice in one sentence.

<sub>id: intro-B-525</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:563` · flow · proposed by Opus, ASTRA

Current:
```latex
rates. Measured light has also been injected
```
Recommended:
```latex
rates.

Measured light has also been injected
```
Why: Half way through, the paragraph turns to a different field (direct imaging), and it runs to about 170 words. A paragraph break helps the reader.

<sub>id: intro-B-563</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:613` · consistency · proposed by Opus

Current:
```latex
aperture \citep{VolkEspinoza2023}.
```
Recommended:
```latex
extraction box \citep{VolkEspinoza2023}.
```
Why: This follows from intro-B-609, so that the extraction box has one name throughout. Line 609 already says that the two names mean the same thing, so the meaning does not change.

Note: Also covered by rewrite intro-B-R2.

<sub>id: intro-B-613</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:619` · consistency · proposed by Opus

Current:
```latex
a clean image of the star
```
Recommended:
```latex
a cleaned image of the star
```
Why: The abstract and Section 4 use "the cleaned image of the star" as the fixed name.

Note: Also covered by rewrite intro-B-R2.

<sub>id: intro-B-619</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:622` · consistency · proposed by Opus

Current:
```latex
apply the transit to the constructed image
```
Recommended:
```latex
apply the transit to the cleaned image
```
Why: "Constructed image" is a third name for the same image within one paragraph, and a reader may take it for a different object.

Note: Also covered by rewrite intro-B-R2.

<sub>id: intro-B-622</sub>

#### 1.6 Research question and objectives (objective 4) · `01_introduction.tex:653` · clarity · proposed by Opus, ASTRA

Current:
```latex
I will switch off its parts one at a time and measure how
  the recovery changes, to find out which of them an accurate spectrum
  needs.
```
Recommended:
```latex
I will find out which of its parts are needed for an accurate spectrum, by switching them off one at a time and measuring how the recovery changes.
```
Why: "Which of them an accurate spectrum needs" is back to front and ends the objective weakly. The goal now comes before the method, and the condition "If NOVA recovers spectra more accurately" is kept.

Other versions:
- ASTRA: I will switch off its components one at a time and measure how the recovery changes, to find out which are needed to recover an accurate spectrum.

<sub>id: intro-B-653</sub>

### Section 2, NOVA

#### 2 NOVA (opening paragraph) · `02_nova.tex:11` · consistency · proposed by Opus

Current:
```latex
a noise scale for each
pixel and the orbital geometry. The others are the same for every data set:
the depth bins, the limb-darkening reference, the apertures, the background
maps and two noise scales.
```
Recommended:
```latex
a noise factor for each
pixel and the orbital geometry. The others are the same for every data set:
the depth bins, the limb-darkening reference, the apertures, the background
maps and a noise factor for each order.
```
Why: A reader cannot tell what 'two noise scales' are. Section 2.5 calls both quantities 'the factor' (N_p has one value per order; s_p is per pixel), so this uses the same word and says what the two are.

Note: Opus nova-11. The facts are unchanged: s_p is measured on each data set, and N_p has one fixed value per order (3.07 and 4.19).

<sub>id: nova-01</sub>

#### 2.2 The detector model · `02_nova.tex:62` · clarity · proposed by Opus

Current:
```latex
$\bar{\mathcal{T}}_{tg}$ is the dimming of
the group's light by the transit
```
Recommended:
```latex
$\bar{\mathcal{T}}_{tg}$ is the fraction of
the group's light that remains during the transit
```
Why: T-bar multiplies the starlight and equals one out of transit, so 'the dimming', read literally, would be one minus T-bar. The new wording matches Section 4's r_p(t), 'the fraction of the star's light that remains'.

Note: Opus nova-62. Merger adjustment: 'that remains during the transit' instead of 'that the transit leaves', because 'leaves' can be misread as 'departs' and 'remains' is the word Section 4 uses (04:195).

Other versions:
- Opus: $\bar{\mathcal{T}}_{tg}$ is the fraction of
the group's light that the transit leaves

<sub>id: nova-07</sub>

#### 2.2 The detector model · `02_nova.tex:63` · clarity · proposed by Opus

Current:
```latex
$\gamma_t$ is a small,
fixed curvature of the baseline
```
Recommended:
```latex
$\gamma_t$ is a fixed factor,
close to one, that describes a slight curvature of the baseline
```
Why: gamma_t is a multiplying factor close to one, as Section 2.5 says. 'Small' suggests that it makes the starlight term small.

Note: Opus nova-63. Merger adjustment: 'that describes' instead of 'for', which reads more naturally.

Other versions:
- Opus: $\gamma_t$ is a fixed factor,
close to one, for a slight curvature of the baseline

<sub>id: nova-08</sub>

#### 2.3 The spatial profile · `02_nova.tex:88` · consistency · proposed by Opus, Fable, ASTRA

Current:
```latex
100~DN/s of starlight therefore dims by only about 1.5
to 2~DN/s during the transit, which is comparable to its noise in a single
integration. The measured $A_{pg}$, and so $q^\star_{pg}$, is therefore
noisy.
```
Recommended:
```latex
100~DN\,s$^{-1}$ of starlight dims by only about 1.5
to 2~DN\,s$^{-1}$ during the transit, which is comparable to its noise in a single
integration. The measured $A_{pg}$, and so $q^\star_{pg}$, is therefore
noisy.
```
Why: Sections 3 and 4 write DN\,s$^{-1}$ three times, and this is the only DN/s. Two consecutive sentences each use 'therefore'. The first one is the weaker, since 'for example' already links the illustration.

Note: On the units: Opus nova-88 and ASTRA 26, with Fable 76 making the opposite choice. On the double 'therefore': Opus nova-88 and Fable 31. DN\,s$^{-1}$ is recommended because two of the three reviewers chose it and it needs one edit instead of three. The second 'therefore' is kept because it carries the actual conclusion: A is noisy because the signal is comparable to the noise. ASTRA's version keeps both 'therefore's.

Other versions:
- ASTRA: A pixel that receives, for example, 100~DN\,s$^{-1}$ of starlight therefore dims by only about 1.5 to 2~DN\,s$^{-1}$ during the transit, which is comparable to its noise in a single integration.
- Fable: Keep 'DN/s' here and change 03:114, 04:37 and 04:140 to DN/s instead (item 76); remove the second 'therefore': 'The measured $A_{pg}$, and so $q^\star_{pg}$, is noisy.' (item 31)

<sub>id: nova-09</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:101` · clarity · proposed by Opus

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
Recommended:
```latex
It combines three public calibration
products. The PASTASOSS trace and wavelength calibration says where
each wavelength falls on the detector
\citep{BainesEtAl2023Trace,BainesEtAl2023Wavelength}. The line-spread kernel
describes how the light of one wavelength spreads over a few neighbouring
columns, and the throughput says how much of the light at each wavelength is
detected. NOVA builds $K_{g\lambda}$ from these products with ATOCA
```
Why: One sentence carries a colon, two semicolons and three 'which' clauses, and the next sentence repeats 'combines'. A calibration product does not itself spread light, so 'describes how the light ... spreads' is also more precise.

Note: Opus nova-101. Also covered by paragraph rewrite nova-PR1. Apply either the entries or the rewrite, not both.

<sub>id: nova-10</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:138` · clarity · proposed by Opus, Fable

Current:
```latex
where $\bar D$ is the overall, achromatic depth and $w_k$ are the bin widths,
```
Recommended:
```latex
where $D_j$ is the depth in bin $j$, $\bar D$ is the overall, achromatic depth and $w_k$ are the bin widths,
```
Why: D_j and the index j are never stated, although every other symbol of the equation is defined.

Note: Opus nova-138 adds D_j. Fable 33 proposed replacing 'achromatic' and itself called this a judgement call. 'Achromatic' is kept because it is standard, and 'the same at every wavelength' could be read as saying that the depths D_j are all equal.

Other versions:
- Fable: where $\bar D$ is the overall depth, the same at every wavelength, and $w_k$ are the bin widths,

<sub>id: nova-14</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:150` · clarity · proposed by ASTRA

Current:
```latex
The orbit is circular, with the period of \citet{LouieEtAl2025} and with the
mid-transit time $t_0$, scaled semi-major axis $a/R_\star$ and impact
parameter $b$, all computed from NOVA's white-light fit
(Section~\ref{sec:own-white}).
```
Recommended:
```latex
The orbit is circular, with the period of \citet{LouieEtAl2025}. The
mid-transit time $t_0$, scaled semi-major axis $a/R_\star$ and impact
parameter $b$ are all computed from NOVA's white-light fit
(Section~\ref{sec:own-white}).
```
Why: Separates the period, taken from the literature, from the three quantities that NOVA computes from its own white-light fit. 'With ... and with ..., all computed' is stacked.

Note: ASTRA 28.

<sub>id: nova-15</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:161` · clarity · proposed by Opus

Current:
```latex
u_2=\sqrt{q_1}\,(1-2q_2).
 \label{eq:kipping-coordinates}
\end{equation}
Limb darkening
```
Recommended:
```latex
u_2=\sqrt{q_1}\,(1-2q_2),
 \label{eq:kipping-coordinates}
\end{equation}
where $u_1$ and $u_2$ are the coefficients of the quadratic law. Limb darkening
```
Why: u_1 and u_2 are never defined but appear again in the priors of Section 2.7. Every other equation in the section is followed by its definitions.

Note: Opus nova-161. The full stop that ends the equation becomes a comma.

<sub>id: nova-17</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:168` · clarity · proposed by Opus

Current:
```latex
$\delta_{oc}(\lambda)=a_{oc}+b_{oc}\,\ell_o(\lambda)$, an offset and a slope in
$\ell_o$, the logarithm of wavelength centred on the order and scaled to a
largest magnitude of one.
```
Recommended:
```latex
$\delta_{oc}(\lambda)=a_{oc}+b_{oc}\,\ell_o(\lambda)$, with an offset $a_{oc}$
and a slope $b_{oc}$. Here $\ell_o$ is the logarithm of wavelength, centred on
the order and scaled so that its largest magnitude is one.
```
Why: Two appositives follow one another, so on first reading it is unclear what each one describes, and 'scaled to a largest magnitude of one' is awkward. The split names each symbol.

Note: Opus nova-166. The limb-darkening wording that Davide corrected on 23 September is in the previous sentence and is untouched.

<sub>id: nova-18</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:179` · repetition · proposed by Opus

Current:
```latex
A curvature is harder
than a straight line to measure from the integrations before and after the
transit,
```
Recommended:
```latex
From these integrations, a curvature is harder
to measure than a straight line,
```
Why: 'Harder than a straight line to measure' splits the comparison. 'The integrations before and after the transit' also appears twice in three sentences, with 'out-of-transit data' in the next one.

Note: Opus nova-179. Merger adjustment: 'From these integrations' is moved to the front, so it cannot be read as 'a straight line from these integrations'. 'These integrations' points back to 'the integrations before and after the transit' two sentences earlier.

Other versions:
- Opus: A curvature is harder
to measure than a straight line from these integrations,

<sub>id: nova-20</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:186` · grammar · proposed by Opus, Fable

Current:
```latex
as a factor close to one. $\gamma_t$ is the geometric mean
```
Recommended:
```latex
as a factor close to one. In the detector model, $\gamma_t$ is the geometric mean
```
Why: A printed sentence should not start with a symbol. The added phrase also reminds the reader where gamma_t came from (Eq. 2).

Note: Opus nova-186, Fable 34. Opus's version is preferred because Fable's puts 'factor' three times into two lines ('a factor close to one. The factor ... curvature factors').

Other versions:
- Fable: as a factor close to one. The factor $\gamma_t$ is the geometric mean

<sub>id: nova-21</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:200` · clarity · proposed by Opus, Fable, ASTRA

Current:
```latex
The 244,657 off-trace pixels, away from the traces, field stars and bad pixels, are assumed to see only background,
```
Recommended:
```latex
The 244,657 off-trace pixels lie away from the traces, field stars and bad pixels. They are assumed to see only background,
```
Why: 'Off-trace pixels, away from the traces' stutters. The 40-word sentence also both defines the set and states an assumption about it. Splitting it does each job cleanly.

Note: Opus nova-200a, Fable 36, ASTRA P2 (first sentence). ASTRA's split is chosen because it avoids Fable's added 'which' and Opus's inverted order. Also covered by paragraph rewrite nova-PR2.

Other versions:
- Opus: Away from the traces, field stars and bad pixels, 244,657 off-trace pixels are assumed to see only background,
- Fable: The 244,657 off-trace pixels, which lie away from the traces, field stars and bad pixels, are assumed to see only background,

<sub>id: nova-23</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:209` · clarity · proposed by Opus

Current:
```latex
is their strongest principal component that does not look like the transit,
with an absolute correlation of at most 0.25. On the real visit,
```
Recommended:
```latex
is the strongest of their principal components whose absolute correlation
with the transit is at most 0.25. On the real WASP-17~b visit,
```
Why: The criterion is stated twice, once loosely and once exactly, and the exact version does not say what the correlation is with. 'The real visit' has not yet been named in Section 2.

Note: Opus nova-209.

<sub>id: nova-25</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:218` · clarity · proposed by Opus

Current:
```latex
It was measured once on the WASP-17 visit, from
how well the model predicted held-out out-of-transit integrations, so it also
covers part of the model mismatch, treated as random noise. Measuring it again
with the current model, and for each data set, is future work.
```
Recommended:
```latex
It was measured once on the WASP-17~b visit, from
how well the model predicted out-of-transit integrations held out of the fit,
so it also covers part of the model mismatch, treated as random noise. I still
need to measure it again with the current model, and for each data set.
```
Why: 'Held-out out-of-transit' puts two 'out's side by side, and 'is future work' would otherwise appear twice in this subsection. 'WASP-17~b visit' matches the rest of the report.

Note: Opus nova-218. Merger adjustment: keeps Davide's 'covers part of the model mismatch, treated as random noise', which reads correctly. Opus's 'absorbs ... as if it were' puts two 'it's with different referents into one clause.

Other versions:
- Opus: It was measured once on the WASP-17~b visit, from
how well the model predicted out-of-transit integrations held out of the fit, so it also
absorbs part of the model mismatch, as if it were random noise. I still need to measure it again
with the current model, and for each data set.

<sub>id: nova-26</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:221` · clarity · proposed by Fable, ASTRA

Current:
```latex
The factor
$s_p\geq1$ is measured on each data set in a similar way, with a straight line
in time, and inflates single pixels that are noisier than the rest of their
order.
```
Recommended:
```latex
The factor
$s_p\geq1$ is measured on each data set in a similar way, with a straight line
in time. It inflates the uncertainty of single pixels that are noisier than the
rest of their order.
```
Why: A factor inflates an uncertainty, not a pixel. The split also separates how s_p is measured from what it does.

Note: Fable 37, ASTRA 30. Uses ASTRA's split with Fable's shorter wording.

Other versions:
- Fable: The factor
$s_p\geq1$ is measured on each data set in a similar way, with a straight line
in time, and inflates the uncertainty of single pixels that are noisier than the rest of their
order.
- ASTRA: The factor $s_p\geq1$ is measured on each data set in a similar way, with a straight line in time. It increases the uncertainty assigned to individual pixels that are noisier than the rest of their order.

<sub>id: nova-27</sub>

#### 2.6 The fit · `02_nova.tex:245` · jargon · proposed by Opus

Current:
```latex
which therefore do not
dominate. The second term is a background anchor.
```
Recommended:
```latex
which therefore do not
dominate the fit. The second term ties the background to the off-trace pixels.
```
Why: 'Background anchor' is working jargon, like the terms on the style rules' banned list. The new sentence says what the term does, and 'dominate' gets the object it needs.

Note: Opus nova-245.

<sub>id: nova-29</sub>

#### 2.6 The fit · `02_nova.tex:261` · flow · proposed by Opus, ASTRA

Current:
```latex
At every step, NOVA solves for the linear
coefficients exactly, by variable projection \citep{GolubPereyra1973}, and
the trust-region reflective method \citep{BranchColemanLi1999} adjusts the
nonlinear ones, with exact derivatives that use JAX for the transit model.
```
Recommended:
```latex
The trust-region reflective method \citep{BranchColemanLi1999} adjusts the
nonlinear parameters, using exact derivatives that JAX computes for the transit
model. At every step of this method, NOVA solves for the linear coefficients
exactly, by variable projection \citep{GolubPereyra1973}.
```
Why: 'At every step' comes before the reader knows which method has steps, and the 41-word sentence changes subject halfway. Derivatives do not 'use' JAX; JAX computes them.

Note: Opus nova-261, ASTRA 31 (second sentence). Both split the sentence. Opus's order is preferred because it introduces the optimiser before 'every step'. Both citations are kept.

Other versions:
- ASTRA: At every step, NOVA solves for the linear coefficients exactly by variable projection \citep{GolubPereyra1973}. The trust-region reflective method \citep{BranchColemanLi1999} adjusts the nonlinear parameters, with exact derivatives that use JAX for the transit model.

<sub>id: nova-33</sub>

#### 2.7 White-light geometry · `02_nova.tex:274` · clarity · proposed by Opus

Current:
```latex
two orders of the same data set.
```
Recommended:
```latex
two orders, from the same data set as the spectral fit.
```
Why: 'The same data set' leaves the reader asking 'the same as what?'. The point is that the geometry is NOVA's own, from the data it fits.

Note: Opus nova-274.

<sub>id: nova-35</sub>

#### 2.8 Uncertainties · `02_nova.tex:292` · clarity · proposed by Opus, Fable

Current:
```latex
I plan to estimate the uncertainty from the calibration products and the
geometry with an ensemble of simulated observations.
```
Recommended:
```latex
I plan to use an ensemble of simulated observations to estimate the uncertainty
that the calibration products and the geometry contribute to the spectrum.
```
Why: 'Estimate the uncertainty from the calibration products' can be read as using the products to estimate it, when it means the uncertainty that they contribute.

Note: Opus nova-292, Fable 39. Merger adjustment: Opus's word order with Fable's verb 'contribute', because 'add to the spectrum' could be read as adding to the depths. It is still planned work, as in the original.

Other versions:
- Opus: I plan to use an ensemble of simulated observations to estimate the uncertainty that the calibration products and the
geometry add to the spectrum.
- Fable: I plan to estimate the uncertainty that the calibration products and the geometry contribute, with an ensemble of simulated observations.

<sub>id: nova-38</sub>

#### 2.9 A first spectrum of WASP-17 b · `02_nova.tex:325` · consistency · proposed by Opus

Current:
```latex
This is why I build the benchmark of the
next two sections, which measures the errors of each method against a known,
injected truth.
```
Recommended:
```latex
This is why I am building the benchmark of the
next two sections, which is designed to measure the errors of each method
against a known, injected truth.
```
Why: 'I build' reads oddly for work in progress, and 'which measures' presents an unfinished benchmark as working. The abstract says 'I am therefore building', and Sections 1 and 5 say 'is designed to'.

Note: Opus nova-325. Merger adjustment: keeps 'the benchmark of the next two sections, which', so the relative clause stays next to its noun. Opus asks whether Davide wants to keep 'measures' (see questions).

Other versions:
- Opus: This is why I am building a benchmark, described in the
next two sections, that is designed to measure the errors of each method against a known,
injected truth.

<sub>id: nova-42</sub>

### Section 3, Building a benchmark

#### 3.2 Injecting into the raw reads (PDF p. 15) · `03_benchmark.tex:44` · clarity · proposed by Opus, Fable

Current:
```latex
I subtracted from the injected data the $1/f$ correction
calculated from the same data without the transit. There, the light curve is
```
Recommended:
```latex
I calculated the $1/f$ correction from the same data without
the transit and subtracted it from the injected data. Without the transit, the light curve is
```
Why: The object of "subtracted" arrives late, and "There" could point to either data set. The steps now come in the order they were done, and the case is named.

Note: Fable changed only "There"; Opus also put the two steps in order. Also covered by rewrite R1.

Other versions:
- Fable: I subtracted from the injected data the $1/f$ correction calculated from the same data without the transit. Without the transit, the light curve is

<sub>id: abs-s3-s5-s6-preamble-03-44</sub>

#### 3.2 Injecting into the raw reads (PDF p. 15) · `03_benchmark.tex:50` · AI tell · proposed by Opus

Current:
```latex
How much of the faint light outside the traces dims therefore matters.
To inject a transit correctly, I would need to know
```
Recommended:
```latex
To inject a transit correctly, I would therefore need to know
```
Why: "X therefore matters." is the short-closer pattern that style_check flags; the next sentence already makes the point concretely, so no content is lost.

Note: If rewrite R1 is applied, this follows directly on its new last sentence about the real data.

Other versions:
- Fable: No change proposed.
- ASTRA: No change proposed.

<sub>id: abs-s3-s5-s6-preamble-03-50</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:66` · clarity · proposed by Opus

Current:
```latex
this estimate leaves typically 0.4, 2.2 and 4.0\% of the light undimmed at 1.0 to 1.8, 1.8 to 2.3 and 2.3 to $2.8\,\mu\mathrm{m}$.
```
Recommended:
```latex
this estimate typically leaves 0.4\% of the light undimmed at 1.0 to $1.8\,\mu\mathrm{m}$, 2.2\% at 1.8 to $2.3\,\mu\mathrm{m}$ and 4.0\% at 2.3 to $2.8\,\mu\mathrm{m}$.
```
Why: Three numbers followed by three ranges make the reader pair them up by hand; "leaves typically" also has the adverb in the wrong place.

Note: No number or range changed. Also covered by rewrite R2.

<sub>id: abs-s3-s5-s6-preamble-03-66</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:68` · grammar · proposed by Opus, Fable

Current:
```latex
this faint light; it changed NOVA's spectrum by about 40~ppm.
```
Recommended:
```latex
this faint light. Dimming this light changed NOVA's spectrum by about 40~ppm.
```
Why: Removes a semicolon and says what changed the spectrum.

Note: Merger adjustment: "Dimming this light" names the cause, which "This" or "it" leaves open (the injection or the dimming). Also covered by rewrite R2.

Other versions:
- Fable: this faint light. This changed NOVA's spectrum by about 40~ppm.
- Opus: this faint light, and this changed NOVA's spectrum by about 40~ppm.

<sub>id: abs-s3-s5-s6-preamble-03-67a</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:68` · clarity · proposed by Opus

Current:
```latex
The upper
estimate instead counts all the light in the box as starlight and dims it,
and leaves the faint light beyond 80 pixels undimmed, like the lower estimate.
```
Recommended:
```latex
The third, the upper
estimate, instead counts all the light in the box as starlight and dims it.
Like the lower estimate, it leaves the faint light beyond 80 pixels undimmed.
```
Why: The paragraph announces three injections, but the reader has to work out that the upper estimate is the third. This also removes the stacked "and dims it, and leaves".

Note: Also covered by rewrite R2.

<sub>id: abs-s3-s5-s6-preamble-03-67b</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:91` · grammar · proposed by Opus, Fable

Current:
```latex
exoTEDRF counts all the light left in its box
after background subtraction as starlight, like the upper estimate, whereas
the lower estimate split the light
```
Recommended:
```latex
Like the upper estimate, exoTEDRF counts as starlight all the light left in
its box after background subtraction, whereas the lower estimate splits the light
```
Why: The sentence opens with a lower-case name, which looks like a typo in print, and "as starlight" is held back behind a long object.

Note: Opus also changes "split" to "splits" so both halves are in the present tense, as "counts" and "leaves" are elsewhere in the subsection; Fable keeps "split". Either is correct.

Other versions:
- Fable: Like the upper estimate, exoTEDRF counts all the light left in its box after background subtraction as starlight, whereas the lower estimate split the light

<sub>id: abs-s3-s5-s6-preamble-03-91</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:114` · clarity · proposed by Opus

Current:
```latex
but it cannot tell the injector how much of it to dim.
```
Recommended:
```latex
but the measurement cannot tell the injector how much of this light to dim.
```
Why: Two uses of "it" with different referents (the measurement, the light) in one clause.

Note: Rewrite R4 also moves this conclusion to the end of the paragraph, after its reasons.

<sub>id: abs-s3-s5-s6-preamble-03-114a</sub>

### Section 4, The measured benchmark

#### 4.1 Measuring the star · `04_measured_benchmark.tex:14` · clarity · proposed by Opus, ASTRA

Current:
```latex
TYC 4213-1116-1, an
A-type star that gives about 1.6 times as much light per detector column as
WASP-17, in two full-frame exposures taken about 25 minutes apart.
```
Recommended:
```latex
TYC~4213-1116-1 in two full-frame exposures taken about 25 minutes apart.
This A-type star gives about 1.6 times as much light per detector column as
WASP-17.
```
Why: The long description of the star sits between the verb and its object, so "in two full-frame exposures" first seems to belong to WASP-17. Two sentences put the observation first and the star second.

Note: Opus and ASTRA proposed the same split; the tilde (Opus) keeps the star's name on one line.

<sub>id: measured-14</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:17` · consistency · proposed by Opus

Current:
```latex
ten integrations of five groups
```
Recommended:
```latex
ten integrations of five reads
```
Why: The rest of Section 4 says "reads" (lines 214, 305, 309), and the Introduction defines a group as a read, so one word is enough.

Note: Also avoids a clash with Section 2, where a "group" is a set of pixels in one order and column.

<sub>id: measured-17</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:35` · consistency · proposed by Fable

Current:
```latex
reaches the strip in the
second exposure as a faint
```
Recommended:
```latex
reaches the strip in the
moved exposure as a faint
```
Why: One name for the exposure into which the star is injected, once measured-20 has introduced it.

Note: Depends on measured-20. Recommended because Davide asked for one name; Opus's narrower option keeps "second exposure" inside Section 4.1.

Other versions:
- Opus: reaches the strip in the
second exposure as a faint (keep: Opus renames only from Section 4.2 on, where "second" no longer pairs with "first")

<sub>id: measured-36</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:38` · clarity · proposed by Fable, Opus

Current:
```latex
The benchmark keeps this glow, because it is built on the second
exposure, so the total light out of transit is right, but the glow does not
dim during the transit.
```
Recommended:
```latex
The benchmark keeps this glow, because it is built on the moved exposure.
The total light out of transit is therefore right, but the glow does not
dim during the transit.
```
Why: One sentence chains "because ... so ... but". Splitting it gives the cause first, then its two consequences.

Note: Fable's version keeps the original order and the "but" contrast, which leads straight into the next sentence about the shallower depth. It also uses "moved exposure" (measured-20).

Other versions:
- Opus: The benchmark is built on the second exposure, so it keeps this glow,
and the total light out of transit is right. The glow, however, does not
dim during the transit.

<sub>id: measured-38</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:42` · clarity · proposed by Opus, Fable

Current:
```latex
The full frames show this halo at 700 to 800 rows from the
moved star, and with its measured fall-off it can be extrapolated to the
strip, so I can correct the image of the star by adding this model of the
halo.
```
Recommended:
```latex
The full frames show this halo at 700 to 800 rows from the
moved star. Extrapolating its measured fall-off to the strip gives a model of
the halo there, and I can correct the image of the star by adding this model.
```
Why: A 43-word "and ... so" chain, and "this model of the halo" refers to a model the sentence never introduces. The rewrite introduces the model and then uses it.

Note: "I can correct" is kept, so the correction is still described as possible, not done (the captions say the image shown was made before it).

Other versions:
- Fable: The full frames show this halo at 700 to 800 rows from the moved star. With its measured fall-off, it can be extrapolated to the strip, so I can correct the image of the star by adding this model of the halo.

<sub>id: measured-42</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:54` · clarity · proposed by Opus, Fable

Current:
```latex
A dark spot would cancel the field source in the
benchmark out of transit and let part of it reappear during the transit, so
at its pixels I subtract an estimate of the sky alone instead of the second
exposure.
```
Recommended:
```latex
A dark spot in the injected star would cancel the field source in the
benchmark out of transit, and part of the source would reappear during the
transit. At its pixels, I therefore subtract an estimate of the sky alone
instead of the moved exposure.
```
Why: The chain "and let ... so at its pixels" is hard to parse. The rewrite parallels the bright-spot sentence ("part of the injected star") and states the fix in its own sentence.

Note: Opus's sentence with Fable's "moved exposure" (measured-20). Merger adjustment: "At its pixels" keeps the original pronoun and mirrors "I replace its pixels" in the bright-spot sentence, whereas "these pixels" has no pixels to point back to.

Other versions:
- Opus: A dark spot in the injected star would cancel the field source in the
benchmark out of transit, and part of the source would reappear during the
transit. At these pixels, I therefore subtract an estimate of the sky alone
instead of the second exposure.

<sub>id: measured-54</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:63` · clarity · proposed by Opus, Fable

Current:
```latex
I find the dark spots in the second exposure, where the star is not in the
way, and the bright spots as compact bumps that the neighbouring columns of
the trace do not have.
```
Recommended:
```latex
I find the dark spots in the moved exposure, where the star is not in the
way. The bright spots show up as compact bumps that the neighbouring columns
of the trace do not have.
```
Why: The two halves are not parallel ("find X in Y" against "find X as Z"), so the second half has to be reread. Two sentences fix this.

Note: Includes Fable's "moved exposure" (measured-20).

<sub>id: measured-63</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:93` · grammar · proposed by Opus, Fable

Current:
```latex
are left over from their removal; a source counts as real if
```
Recommended:
```latex
are left over from their removal. A source counts as real if
```
Why: The semicolon joins a problem to the rule that answers it; two sentences are clearer, and the section is over the semicolon target.

Note: Also covered by rewrite measured-R1.

<sub>id: measured-93</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:109` · clarity · proposed by Opus

Current:
```latex
the WASP-17~b fit for programme 4476, and I will check the faint spectra that it predicts in both pointings.
```
Recommended:
```latex
the WASP-17~b fit for programme 4476. I will check the faint spectra that this fit predicts in both pointings.
```
Why: "It" can be read as programme 4476 or as the fit; the fit is meant.

Note: Opus proposed this only inside his paragraph rewrite. Also covered by rewrite measured-R1.

<sub>id: measured-109a</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:129` · clarity · proposed by Opus

Current:
```latex
combining the pipeline's error estimates for the two exposures, which agree
with the actual scatter between neighbouring pixels to within 10\%.
```
Recommended:
```latex
combining the pipeline's error estimates for the two exposures. These
estimates agree with the actual scatter between neighbouring pixels to within
10\%.
```
Why: "Which agree" can be read as referring to the two exposures; it is the error estimates that agree with the scatter.

Note: Also covered by rewrite measured-R2.

<sub>id: measured-129</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:134` · clarity · proposed by Opus, Fable

Current:
```latex
The shape of the wings is set by the
optics and changes only slowly with wavelength, so beyond 40 rows from the
nearest trace I replace each pixel
```
Recommended:
```latex
The shape of the wings is set by the
optics and changes only slowly with wavelength. Beyond 40 rows from the
nearest trace, I therefore replace each pixel
```
Why: A sentence of about 53 words; splitting it separates the reason from the method.

Note: Opus and Fable proposed the same text. Also covered by rewrite measured-R2.

<sub>id: measured-134</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:141` · consistency · proposed by Opus

Current:
```latex
the weight of this
model rises linearly
```
Recommended:
```latex
the weight of this
far-wing model rises linearly
```
Why: The text never calls the median a model before this point; "far-wing model" is the name used in the Figure 9 caption.

Note: Also covered by rewrite measured-R2, which names the model one sentence earlier and then writes "its weight".

<sub>id: measured-141</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:145` · consistency · proposed by Fable

Current:
```latex
the reads of the second
exposure across the whole strip
```
Recommended:
```latex
the reads of the moved
exposure across the whole strip
```
Why: One name for the exposure into which the star is injected (measured-20).

Note: Also covered by rewrite measured-R2.

Other versions:
- Opus: the reads of the second
exposure across the whole strip (keep: Opus renames only from Section 4.2 on, and kept "second" here in his rewrite)

<sub>id: measured-145</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:147` · clarity · proposed by Fable, Opus

Current:
```latex
so the wings change
slowly enough for this.
```
Recommended:
```latex
so the wings change
slowly enough across the 61 columns for the median to stand in for each pixel.
```
Why: "For this" is vague, and the sentence justifies the 61-column median, not the blending that now comes just before it.

Note: This entry only rewords the sentence in place. Fable and Opus would also move it next to the assumption it supports; that move is done in rewrite measured-R2, because one entry cannot both delete and insert. Merger adjustment: "the 61 columns" instead of Fable's "these columns", because in place the 61 columns are several sentences back.

Other versions:
- Fable: Move the whole sentence "On average, the model differs ... 40 to 100 rows" to directly after "... which span about $0.06\,\mu\mathrm{m}$ in order~1." and end it "so the wings change slowly enough across these columns for the median to stand in for each pixel."

<sub>id: measured-146</sub>

#### 4.1 Measuring the star (Figure 9 caption) · `04_measured_benchmark.tex:174` · clarity · proposed by ASTRA, Opus

Current:
```latex
and the cleaned image of the star (blue;
  dashed where the far-wing model is used, which depends on the distance from
  the nearest trace).
```
Recommended:
```latex
and the cleaned image of the star (blue). The blue curve is dashed where the
  far-wing model is used. Where it is used depends on the distance from the
  nearest trace.
```
Why: "Which depends on the distance" can mean that the model is a function of distance, or that where it applies depends on distance; the second is what the dashing shows.

Note: Merger adjustment: ASTRA's reading without the semicolon. Opus raised the same ambiguity as a question, so Davide should confirm this reading (see questions).

Other versions:
- ASTRA: and the cleaned image of the star (blue). The blue curve is dashed where the far-wing model is used; its use depends on the distance from the nearest trace.

<sub>id: measured-176</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:187` · consistency · proposed by Opus, Fable

Current:
```latex
the raw reads of
the second exposure.
```
Recommended:
```latex
the raw reads of
the moved exposure.
```
Why: From Section 4.2 on, the abstract, the captions and Section 4.3 say "moved exposure", and Eq. (10) is where a reader will look the term up.

<sub>id: measured-187</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:194` · consistency · proposed by Opus, Fable

Current:
```latex
$O_p(t)$ is the count rate of the second exposure
```
Recommended:
```latex
$O_p(t)$ is the count rate of the moved exposure
```
Why: Same reason as measured-187; Figure 10 labels O as the moved exposure.

<sub>id: measured-194</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:233` · clarity · proposed by Opus, ASTRA

Current:
```latex
The two share the real exposure and every photon that the transit did not remove, so they differ only by the removed light, and the only noise left in their difference is the small photon noise of that light.
```
Recommended:
```latex
The two share the real exposure and every photon that the transit did not remove. They differ only by the removed light, so the only noise left in their difference is the small photon noise of that light.
```
Why: A 40-word sentence joined by "so ... and the only"; two sentences are easier to follow. The next sentence keeps its "therefore".

Note: ASTRA's version comes from its whole-paragraph replacement P4 (see dropped). Its "Both cases" would call the copy without the transit a "case", a word the text keeps for transit cases.

Other versions:
- ASTRA: Both cases share the real exposure and every photon that the transit did not remove. They therefore differ only by the removed light, whose small photon noise is the only noise left in their difference.

<sub>id: measured-233</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:244` · clarity · proposed by Fable, Opus

Current:
```latex
Further tests would be needed to isolate the faint light.
```
Recommended:
```latex
Further tests would then be needed to find out whether the faint light is the cause.
```
Why: Read literally, "isolate the faint light" means separating the light itself, which is what the cleaning does. The point is to find out whether the faint light causes the difference.

Note: Both keep the meaning. Fable's is plainer; Opus's stays closer to the current words.

Other versions:
- Opus: Further tests would be needed to isolate the effect of the faint light.

<sub>id: measured-244</sub>

#### 4.3 Testing the injector and the pipelines · `04_measured_benchmark.tex:268` · consistency · proposed by Opus

Current:
```latex
the injected data, made of the moved exposure plus the injected star,
should look like the real exposure with the star at its usual position.
```
Recommended:
```latex
the moved exposure plus the injected star should look like the first
exposure, in which the star was at its usual position.
```
Why: Removes the definition squeezed between commas. Also, "the real exposure" means the moved exposure at lines 227 and 233, but the other exposure here.

<sub>id: measured-267</sub>

#### 4.3 Testing the injector and the pipelines · `04_measured_benchmark.tex:275` · clarity · proposed by Opus, Fable

Current:
```latex
Neither
comparison can show that the cleaned image is the true star; that rests on the
cleaning
```
Recommended:
```latex
Neither
test can show that the cleaned image is the true star. That rests on the
cleaning
```
Why: The paragraph describes two tests, and the checks of the code are not a comparison, so "neither comparison" does not fit both. The semicolon also goes.

Other versions:
- Fable: Neither
comparison can show that the cleaned image is the true star. That rests on the
cleaning

<sub>id: measured-275</sub>

#### 4.3 Testing the injector and the pipelines · `04_measured_benchmark.tex:284` · clarity · proposed by Opus

Current:
```latex
spectrum, which gives the total error that a user would get.
```
Recommended:
```latex
spectrum. This comparison gives the total error that a user would get.
```
Why: "Which" can be read as referring to the injected spectrum.

Note: Merger adjustment: "This comparison" instead of a bare "This".

Other versions:
- Opus: spectrum. This gives the total error that a user would get.

<sub>id: measured-284</sub>

#### 4.3 Testing the injector and the pipelines · `04_measured_benchmark.tex:285` · repetition · proposed by Opus, Fable

Current:
```latex
on the copy without the transit and
compare the two runs after every step that the pipeline saves, such as the
$1/f$ correction or the extraction. Because the two runs differ only by the light that the transit removed, each comparison shows the transit as that step passed it on. Knowing
```
Recommended:
```latex
on the copy without the transit (Section~\ref{sec:injecting-star}) and
compare the two runs after every step that the pipeline saves, such as the
$1/f$ correction or the extraction. Knowing
```
Why: The cut sentence repeats Section 4.2 (line 233) almost word for word, including "shows the transit as that step passed it on". The cross-reference keeps the explanation one click away.

Note: Opus cuts the sentence; Fable cuts it and adds a pointer. Merger adjustment: the pointer goes after "the copy without the transit", so that it does not read as pointing to where the extraction is described.

Other versions:
- Opus: on the copy without the transit and
compare the two runs after every step that the pipeline saves, such as the
$1/f$ correction or the extraction. Knowing
- Fable: ... such as the $1/f$ correction or the extraction (Section~\ref{sec:injecting-star}). Knowing

<sub>id: measured-287</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:299` · clarity · proposed by Opus, ASTRA

Current:
```latex
hosts that SOSS had observed by October 2026, whose median temperature is 4,870~K.
```
Recommended:
```latex
hosts that SOSS had observed by October 2026. The median temperature of these hosts is 4,870~K.
```
Why: "Whose" comes straight after "October 2026", far from "hosts".

Note: Same split. ASTRA repeats the number 51, which is correct but not needed.

Other versions:
- ASTRA: hosts that SOSS had observed by October 2026. The median temperature of those 51 hosts is 4,870~K.

<sub>id: measured-299</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:319` · grammar · proposed by Opus, Fable

Current:
```latex
Fourthly, the injection adds light but no response of the detector's
electronics to the change in light. If the detector itself reacts when the star dims, as the faint light outside the traces may suggest (Section~\ref{sec:real-data-test}), the benchmark does not contain this.
```
Recommended:
```latex
Fourthly, the injection adds light, but it does not add any response of the
detector's electronics to the change in light. If the detector itself reacts when the star dims, as the faint light outside the traces may suggest (Section~\ref{sec:real-data-test}), the benchmark does not contain this reaction.
```
Why: "Adds light but no response" makes one verb do two jobs, and "does not contain this" lacks a noun.

Note: Opus fixes both halves; Fable fixes only the second. "Reaction" echoes "reacts" in the same sentence.

Other versions:
- Fable: ... the benchmark does not contain that response.

<sub>id: measured-319</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:324` · clarity · proposed by Opus, ASTRA

Current:
```latex
Fifthly, the exposure lasts only 2.68~h, so the injected transit lasts
51.5~minutes, to leave time before and after it. A planet crossing the centre
of this star would take hours, so with the one-day orbit that I chose, the
shape of this short transit corresponds to an unphysical star, about a hundred
times denser than this one.
```
Recommended:
```latex
Fifthly, the exposure lasts only 2.68~h, so the injected transit is
51.5~minutes long, to leave time before and after it. A planet crossing the
centre of this star would take hours. With the one-day orbit that I chose, the
shape of this short transit corresponds to an unphysical star, about a hundred
times denser than this one.
```
Why: The first sentence uses "lasts" twice, and the second runs to 40 words through "so with ... the shape".

Note: Opus's version. ASTRA keeps a "therefore", which would sit next to the "therefore" of the following sentence.

Other versions:
- ASTRA: A planet crossing the centre of this star would take hours. With the one-day orbit that I chose, the shape of this short transit therefore corresponds to an unphysical star, about a hundred times denser than this one.

<sub>id: measured-324</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:336` · repetition · proposed by Opus, Fable

Current:
```latex
the benchmark, and it rests on a single star.
```
Recommended:
```latex
the benchmark.
```
Why: "Rests on one star" opens the limitations at line 297, and the next sentence already asks for several stars.

<sub>id: measured-335</sub>

### Section 5, Discussion and plan

#### 5.1 Discussion (PDF p. 22) · `05_discussion_plan.tex:14` · clarity · proposed by Opus, Fable

Current:
```latex
It
is designed to measure which kinds of error each method makes when the
injected light curve is known, and where in its processing they arise.
```
Recommended:
```latex
The
benchmark is designed to measure, against a known injected light curve, which
kinds of error each method makes and where in its processing they arise.
```
Why: After "The price is a different star, field and readout", "It" seems to point to the price or the readout. "When the injected light curve is known" also reads like a condition, although it is always known.

Note: Fable changes only "It"; Opus also fixes the condition reading. "Is designed to" (a plan, not a result) is kept.

Other versions:
- Fable: The benchmark is designed to measure which kinds of error each method makes when the injected light curve is known, and where in its processing they arise.

<sub>id: abs-s3-s5-s6-preamble-05-14</sub>

#### 5.1 Discussion (PDF p. 22) · `05_discussion_plan.tex:20` · grammar · proposed by Opus, ASTRA

Current:
```latex
wavelength, and most in the red (Section~\ref{sec:nova-real}), and its
uncertainty is not yet validated.
```
Recommended:
```latex
wavelength, most in the red (Section~\ref{sec:nova-real}). Its
uncertainty is not yet validated.
```
Why: Two "and"s in a row; the limitation then gets its own sentence, as in the abstract.

Note: Combines Opus's wording, which is the abstract's ("deeper at every wavelength, most in the red"), with ASTRA's split. Also covered by rewrite R5.

Other versions:
- Opus: wavelength, most in the red (Section~\ref{sec:nova-real}), and its uncertainty is not yet validated.
- ASTRA: wavelength, with the largest difference in the red (Section~\ref{sec:nova-real}). Its uncertainty is not yet validated.
- Fable: No change (her rewrite 3C keeps this line).

<sub>id: abs-s3-s5-s6-preamble-05-20</sub>

#### 5.1 Discussion (PDF p. 22) · `05_discussion_plan.tex:21` · clarity · proposed by Opus, Fable

Current:
```latex
An injection test shows how accurately each method recovers a known spectrum, which is the best guide to which real spectrum to trust, and an injector built from the WASP-17~b data alone cannot provide it.
```
Recommended:
```latex
An injection test shows how accurately each method recovers a known spectrum. This is the best guide to which real spectrum to trust, but an injector built from the WASP-17~b data alone cannot provide it.
```
Why: "Which ... which" in one sentence, followed by an "it" with two candidates (the test or the guide).

Note: Opus's version: "it" now points to "the best guide". Fable's "cannot provide such a test" reads literally as if Section 3 had made no injection tests. Also covered by rewrite R5.

Other versions:
- Fable: An injection test shows how accurately each method recovers a known spectrum, and this is the best guide to which real spectrum to trust. An injector built from the WASP-17~b data alone cannot provide such a test.

<sub>id: abs-s3-s5-s6-preamble-05-21</sub>

#### 5.2 Research plan, Paper 1 (PDF p. 23) · `05_discussion_plan.tex:36` · grammar · proposed by ASTRA

Current:
```latex
transmission spectrum, and whether NOVA changes the conclusions about
```
Recommended:
```latex
transmission spectrum, and to test whether NOVA changes the conclusions about
```
Why: "The aim is to measure ... whether" pairs "measure" with a yes/no question; a second verb restores the parallel.

<sub>id: abs-s3-s5-s6-preamble-05-36</sub>

#### 5.2 Research plan, Paper 1 (PDF p. 23) · `05_discussion_plan.tex:42` · clarity · proposed by Opus

Current:
```latex
will refit NOVA's spectrum of the real WASP-17~b visit, with uncertainties
from an ensemble of simulated observations, and compare it with the three
```
Recommended:
```latex
will refit the real WASP-17~b visit with NOVA, estimate the uncertainties
from an ensemble of simulated observations, and compare the spectrum with the three
```
Why: One refits data, not a spectrum, and "with uncertainties from ..." hangs loosely. Three verbs for the three real steps read more cleanly.

<sub>id: abs-s3-s5-s6-preamble-05-42</sub>

#### 5.2 Research plan, Paper 1 (PDF p. 23) · `05_discussion_plan.tex:45` · grammar · proposed by ASTRA, Opus

Current:
```latex
for several cooler stars, read
out as a SOSS time series and with more integrations at the usual position.
```
Recommended:
```latex
for several cooler stars, with the exposures read
out as a SOSS time series and with more integrations at the usual position.
```
Why: As written, "read out as a SOSS time series" attaches to the stars.

Note: ASTRA's fix keeps every detail. Opus instead cuts the details to a cross-reference, because the last paragraph of Section 4.4 gives them a page earlier; that is a content cut, so it is offered as an alternative and raised as a question.

Other versions:
- Opus: for several cooler stars
(Section~\ref{sec:benchmark-limits}).

<sub>id: abs-s3-s5-s6-preamble-05-45</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:56` · clarity · proposed by Opus

Current:
```latex
including supreme-SPOON, now exoTEDRF, and \texttt{transitspectroscopy},
```
Recommended:
```latex
including supreme-SPOON (now exoTEDRF) and \texttt{transitspectroscopy},
```
Why: Four commas and two "and"s in a row make it unclear where the list ends; brackets take the aside out.

Note: Also covered by rewrite R6.

Other versions:
- ASTRA: No change (his rewrite P5 keeps the commas).

<sub>id: abs-s3-s5-s6-preamble-05-56</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:58` · consistency · proposed by Opus, Fable

Current:
```latex
while the fall in depth
```
Recommended:
```latex
whilst the fall in depth
```
Why: House spelling: Sections 1 and 2 use "whilst" nine times and "while" never.

Note: Also covered by rewrite R6. Section 4, line 305, has the only other "while".

Other versions:
- ASTRA: while the fall in depth (unchanged in his rewrite P5)

<sub>id: abs-s3-s5-s6-preamble-05-58b</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:58` · clarity · proposed by Opus, Fable

Current:
```latex
This is in the red range where NOVA's spectrum of WASP-17~b differs most from Ahsoka's
```
Recommended:
```latex
This fall lies in the red, where NOVA's spectrum of WASP-17~b differs most from Ahsoka's
```
Why: "This" has three possible referents (the metallicity, the clouds, the 2 to 2.3 um range).

Note: Also covered by rewrite R6.

Other versions:
- Fable: This fall lies in the red range where NOVA's spectrum of WASP-17~b differs most from Ahsoka's

<sub>id: abs-s3-s5-s6-preamble-05-58a</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:62` · clarity · proposed by Opus, Fable

Current:
```latex
while another analysis does not
\citep{WangEtAl2026}.
```
Recommended:
```latex
whilst another analysis finds none
\citep{WangEtAl2026}.
```
Why: After "and favour an explanation ...", the bare "does not" can attach to "favour" instead of "find"; "whilst" is the house spelling.

Note: Also covered by rewrite R6.

Other versions:
- Fable: whilst another analysis does not \citep{WangEtAl2026}.
- ASTRA: while another analysis does not \citep{WangEtAl2026}. (unchanged)

<sub>id: abs-s3-s5-s6-preamble-05-62</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:63` · clarity · proposed by Opus, ASTRA

Current:
```latex
Both sides suggest differences in reduction as possible causes, and NOVA's reduction will show which of the two its spectrum supports.
```
Recommended:
```latex
Both sides suggest differences in reduction as possible causes of the disagreement, and I will test which side NOVA's spectrum supports.
```
Why: "NOVA's reduction will show which of the two its spectrum supports" is circular and hard to parse, and "causes" needs an object.

Note: Merger adjustment: "which side" instead of "which of the two", so the reader knows the two are the two sides. The plan stays in the future tense.

Other versions:
- Opus: Both sides suggest differences in reduction as possible causes of the disagreement, and I will test which of the two NOVA's spectrum supports.
- ASTRA: Both sides suggest differences in reduction as possible causes, and NOVA's reduction will show whether its spectrum supports the presence or absence of this slope.

<sub>id: abs-s3-s5-s6-preamble-05-63</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:64` · clarity · proposed by Opus

Current:
```latex
The HAT-P-18~b visit contains a spot crossed by the planet during the transit
and a field star on the order-1 trace whose brightness changes, probably an
eclipsing binary \citep{FuEtAl2022}. It therefore tests how NOVA handles light
that its transit model does not describe, and Paper~3 returns to this visit
```
Recommended:
```latex
The HAT-P-18~b visit contains a spot that the planet crosses during the
transit, and a variable field star on the order-1 trace, probably an
eclipsing binary \citep{FuEtAl2022}. This visit therefore tests how NOVA handles light
that its transit model does not describe, and Paper~3 returns to it
```
Why: "The order-1 trace whose brightness changes" attaches "whose" to the trace, and "It" after the field star is ambiguous. "Variable" is the standard word.

Note: "returns to it" avoids "This visit ... this visit". Also covered by rewrite R6.

Other versions:
- ASTRA: No change (his rewrite P5 keeps this sentence).

<sub>id: abs-s3-s5-s6-preamble-05-64</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:69` · clarity · proposed by Opus

Current:
```latex
so it tests whether NOVA's
differences still matter
```
Recommended:
```latex
so it tests whether the differences between NOVA and the other pipelines
still matter
```
Why: "NOVA's differences" does not say differences from what.

Note: Assumes the reading in the question to Davide; confirm before applying. Also covered by rewrite R6.

Other versions:
- ASTRA: No change (his rewrite P5 keeps "NOVA's differences").

<sub>id: abs-s3-s5-s6-preamble-05-69</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:77` · grammar · proposed by Opus

Current:
```latex
which is again tested on the benchmark
```
Recommended:
```latex
which will again be tested on the benchmark
```
Why: The tense should match the plan ("will go into a later version").

Note: Also covered by rewrite R6.

<sub>id: abs-s3-s5-s6-preamble-05-77</sub>

#### 5.2 Research plan, Paper 3 (PDF p. 24) · `05_discussion_plan.tex:82` · AI tell · proposed by Opus, Fable

Current:
```latex
This matters most for
small planets around cool stars.
```
Recommended:
```latex
These questions matter most for
small planets around cool stars.
```
Why: "This matters" is flagged by style_check, and "This" is vague after a two-part aim.

Note: Plural, because the aim has two parts.

Other versions:
- Fable: The question is most pressing for small planets around cool stars.

<sub>id: abs-s3-s5-s6-preamble-05-82</sub>

#### 5.2 Research plan, Paper 3 (PDF p. 24) · `05_discussion_plan.tex:85` · flow · proposed by Opus, ASTRA

Current:
```latex
\citep{RackhamEtAl2018}, and they change, as do flares, from one visit to the
next.
```
Recommended:
```latex
\citep{RackhamEtAl2018}. These regions change from one visit to the next, and so
do flares.
```
Why: The aside "as do flares" splits the verb from its phrase, and "they" could mean the false features.

Note: Merger adjustment: ASTRA's "These regions" in Opus's word order.

Other versions:
- Opus: \citep{RackhamEtAl2018}. They change from one visit to the next, and so do flares.
- ASTRA: \citep{RackhamEtAl2018}. These regions, and flares, change from one visit to the next.

<sub>id: abs-s3-s5-s6-preamble-05-85</sub>

#### 5.2 Research plan, Paper 3 (PDF p. 24) · `05_discussion_plan.tex:89` · clarity · proposed by Opus

Current:
```latex
to test whether spots on the star that the planet does not cross explain this rise, as \citet{FournierTondreauEtAl2024} propose, rather than a haze \citep{FuEtAl2022}.
```
Recommended:
```latex
to test whether this rise comes from spots on the star that the planet does not cross, as \citet{FournierTondreauEtAl2024} propose, or from a haze \citep{FuEtAl2022}.
```
Why: "Rather than a haze" is cut off from "spots" by the "as ... propose" aside and dangles; "whether ... or from" puts the two explanations side by side.

<sub>id: abs-s3-s5-s6-preamble-05-89</sub>

#### 5.2 Research plan, Paper 3 (PDF p. 24) · `05_discussion_plan.tex:95` · clarity · proposed by Opus

Current:
```latex
in the out-of-transit SOSS data, which would
feed directly into this paper.
```
Recommended:
```latex
in the out-of-transit SOSS data, and their results would
feed directly into this paper.
```
Why: "Which" grammatically points to the SOSS data, not to the projects.

<sub>id: abs-s3-s5-s6-preamble-05-95</sub>

#### 5.2 Research plan, Paper 5 (PDF p. 24) · `05_discussion_plan.tex:112` · clarity · proposed by Opus, Fable

Current:
```latex
These signals are weak, and it would be
interesting to see whether a detector-level analysis also makes them more
reliable.
```
Recommended:
```latex
These signals are weak, and I would test whether a detector-level analysis
also makes them more reliable.
```
Why: "It would be interesting to see" is conversational for a plan.

Note: Opus's version keeps the open question; Fable's turns it into a hedged claim ("may make"), which changes the meaning. "Also" is kept (see the question to Davide).

Other versions:
- Fable: These signals are weak, and a detector-level analysis may make them more reliable as well.

<sub>id: abs-s3-s5-s6-preamble-05-112</sub>

#### 5.2 Research plan, Figure 11 (Gantt chart and caption, PDF p. 25) · `05_discussion_plan.tex:172` · grammar · proposed by Opus, ASTRA

Current:
```latex
The research phase ends on approximately 27 April
2029, and
```
Recommended:
```latex
The research phase ends around 27 April
2029, and
```
Why: "Ends on approximately" is awkward; "around" carries the same approximation.

<sub>id: abs-s3-s5-s6-preamble-05-172</sub>

### transmission_spectroscopy_schematic.tex

#### 1.1 Exoplanet atmospheres and transmission spectroscopy (Figure 1 label) · `transmission_spectroscopy_schematic.tex:87` · consistency · proposed by Opus

Current:
```latex
larger apparent radius
```
Recommended:
```latex
larger effective radius
```
Why: This is the same term inside the Figure 1 drawing, which should match the text and the caption.

Note: The new label is one letter longer. Check after compiling that it still fits its position.

<sub>id: intro-A-48fig</sub>

## 5. Tier 3: polish and taste (91)

### Abstract

#### Abstract (approved by Davide this evening) · `00_abstract.tex:16` · grammar · proposed by Opus

Current:
```latex
but must decide which of the observed light belongs to the star.
```
Recommended:
```latex
but must decide which part of the observed light belongs to the star.
```
Why: "Which of" with the mass noun "light" is slightly unidiomatic; the Introduction says "which part of the recorded light".

Note: Approved text: change only if Davide wants to reopen the abstract. Pairs with entry 03-13, which makes the same change in Section 3.1.

Other versions:
- Fable: No change (abstract approved).
- ASTRA: No change (abstract approved).

<sub>id: abs-s3-s5-s6-preamble-00-16</sub>

#### Abstract (approved by Davide this evening) · `00_abstract.tex:17` · clarity · proposed by Opus

Current:
```latex
exoTEDRF reversed with the
```
Recommended:
```latex
exoTEDRF reversed when I changed the
```
Why: "Reversed with the share" can be read as if the ranking and the share reversed together.

Note: Approved text: optional. The result reads "the ranking of NOVA and exoTEDRF reversed when I changed the share of faint light taken to be starlight, which the WASP-17~b data cannot determine."

Other versions:
- Fable: No change (abstract approved).
- ASTRA: No change (abstract approved).

<sub>id: abs-s3-s5-s6-preamble-00-17</sub>

#### Abstract (approved by Davide this evening) · `00_abstract.tex:20` · clarity · proposed by Opus

Current:
```latex
It observed a star at its usual position and again moved off the SOSS
```
Recommended:
```latex
It observed a star at its usual position and again with the star moved off the SOSS
```
Why: "And again moved off" can be misread as "moved off again".

Note: Approved text: optional.

Other versions:
- Fable: No change (abstract approved).
- ASTRA: No change (abstract approved).

<sub>id: abs-s3-s5-s6-preamble-00-20</sub>

### Section 1, Introduction

#### 1 Introduction and Literature Review (opening paragraph) · `01_introduction.tex:8` · clarity · proposed by Opus

Current:
```latex
I have therefore developed
Nonlinear Order-coupled Variable-projection Analysis (NOVA).
```
Recommended:
```latex
I have therefore developed a method called Nonlinear Order-coupled Variable-projection Analysis (NOVA).
```
Why: 'Developed Nonlinear ... Analysis' can read as a general technique. 'A method called' shows at once that NOVA is a name.

Note: Rewrite intro-A-R1 also starts a new paragraph at this sentence.

<sub>id: intro-A-08</sub>

#### 1 Introduction and Literature Review (opening paragraph) · `01_introduction.tex:12` · flow · proposed by Opus

Current:
```latex
Whether NOVA or the established methods give the
more accurate spectrum cannot be decided from real data, because the true
spectrum of a real planet is unknown.
```
Recommended:
```latex
Real data cannot decide whether NOVA or the established methods give the more accurate spectrum, because the true spectrum of a real planet is unknown.
```
Why: The current subject is a 13-word 'whether' clause with a passive verb. The active version reads at once and echoes the Section 3.4 title, 'The real data cannot decide'.

Note: Also covered by rewrite intro-A-R1.

<sub>id: intro-A-12</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:21` · grammar · proposed by Opus

Current:
```latex
temperatures and orbits, many with no
```
Recommended:
```latex
temperatures and orbits, and many have no
```
Why: 'Orbits, many with no counterpart' can attach to 'orbits'. The edit makes the planets the ones that have no counterpart.

<sub>id: intro-A-21</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:27` · repetition · proposed by Fable, ASTRA

Current:
```latex
that is, passes in front of its star
```
Recommended:
```latex
that is, crosses the face of its star
```
Why: The sentence uses 'passes in front' and then 'passes through'.

Note: Fable's minimal fix keeps the paragraph opening on 'The atmosphere', which links it to the previous paragraph. ASTRA's split defines the transit first, but it keeps 'passes ... passes' and ends on a trailing 'allowing' clause.

Other versions:
- ASTRA: (replaces the whole sentence) A planet transits when it passes in front of its star. Some starlight then passes through the planet's atmosphere, allowing the atmosphere to be studied.

<sub>id: intro-A-27</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:66` · repetition · proposed by Opus

Current:
```latex
the drop in light isolates the light
```
Recommended:
```latex
the drop in brightness isolates the light
```
Why: 'Light ... light' within four words reads clumsily.

<sub>id: intro-A-66</sub>

#### 1.1 Exoplanet atmospheres and transmission spectroscopy · `01_introduction.tex:82` · repetition · proposed by Opus

Current:
```latex
propagate into the retrieval.
```
Recommended:
```latex
carry over into the retrieved atmosphere.
```
Why: 'Propagate into' already appears four lines earlier. Objective 4 itself says the errors 'carry over into the atmospheric properties that a retrieval infers'.

<sub>id: intro-A-82</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:130` · flow · proposed by Opus

Current:
```latex
In this project, I use a mode of NIRISS, called Single Object Slitless
```
Recommended:
```latex
In this project, I use this mode of NIRISS, called Single Object Slitless
```
Why: The previous paragraph has just introduced 'a mode' covering 0.6 to 2.8 µm. Saying 'a mode' again reads as if it were a different one.

<sub>id: intro-A-130</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:136` · consistency · proposed by Opus

Current:
```latex
$\lambda/\Delta\lambda$ of the first order is about 650 at
```
Recommended:
```latex
$\lambda/\Delta\lambda$ of order 1 is about 650 at
```
Why: The report says 'order 1' everywhere else, including the previous sentence.

<sub>id: intro-A-136</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b (Figure 2 caption) · `01_introduction.tex:145` · clarity · proposed by ASTRA

Current:
```latex
Out-of-transit median image of the WASP-17~b SOSS visit, in count rates before the background and the $1/f$ noise of the readout (Section~\ref{sec:detector-to-spectrum}) are removed.
```
Recommended:
```latex
Out-of-transit median image of the WASP-17~b SOSS visit, in count rates, before the background and the $1/f$ noise of the readout are removed (Section~\ref{sec:detector-to-spectrum}).
```
Why: At present the section reference sits between the subject and 'are removed'. Moving it to the end and adding a comma lets the clause read in one go.

Note: Merger adjustment: ASTRA's version uses 'integrations', which is defined only in Section 1.3, and the noun 'removal'. See the question on defining 'visit', which first appears in this caption.

Other versions:
- ASTRA: Median count-rate image from the out-of-transit integrations of the WASP-17~b SOSS visit, before removal of the background and the $1/f$ noise of the readout (Section~\ref{sec:detector-to-spectrum}).

<sub>id: intro-A-145</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:156` · repetition · proposed by Opus

Current:
```latex
tested during commissioning, the test period before science operations, on
```
Recommended:
```latex
measured during commissioning, the test period before science operations, on
```
Why: 'Tested ... the test period' repeats the word, and the precision was in fact measured.

<sub>id: intro-A-156</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:162` · flow · proposed by Opus

Current:
```latex
The spectrum, in contrast to the white-light curve,
```
Recommended:
```latex
Unlike the white-light curve, the spectrum
```
Why: The contrast comes first, and the subject then sits next to its verb ('the spectrum is measured in channels').

<sub>id: intro-A-162</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:183` · clarity · proposed by Opus

Current:
```latex
the background is therefore almost only
```
Recommended:
```latex
the background is therefore almost entirely
```
Why: 'Almost only first-order light' is unidiomatic, and 'almost entirely' is the natural phrase.

<sub>id: intro-A-183</sub>

#### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex:215` · flow · proposed by Opus

Current:
```latex
The SOSS data also tightened the constraint on the water
abundance, compared with the HST and Spitzer data, and placed the abundance
above the solar value
```
Recommended:
```latex
The SOSS data also constrained the water abundance more tightly than the HST and Spitzer data, and placed it above the solar value
```
Why: 'Compared with ...' is wedged between the two verbs and breaks the sentence. The comparison now sits with the verb it belongs to, and 'abundance' is no longer said twice.

Note: Merger adjustment: Opus's fronted 'Compared with ...' would also cover 'placed it above the solar value', which widens the comparison. The recommended wording keeps the comparison on the tighter constraint only. \citep{LouieEtAl2025} follows unchanged.

Other versions:
- Opus: Compared with the HST and Spitzer data, the SOSS data also tightened the constraint on the water abundance and placed it above the solar value

<sub>id: intro-A-215</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:250` · consistency · proposed by Opus

Current:
```latex
All three reductions used for WASP-17~b turned
```
Recommended:
```latex
All three reductions of WASP-17~b turned
```
Why: "Reductions of WASP-17~b" is the phrase the report uses everywhere else.

Note: Opus proposed the signpost and also asked Davide whether he wants one here, offering this minimal change as the fallback. The style rules recommend signposts but also say "In this section" should not be added for its own sake. The section heading and Figure 3 already announce the topic, so I recommend the minimal change. The signpost is there if Davide wants it.

Other versions:
- Opus: Signpost version, replacing the whole sentence from "All three reductions used" to "\citep{LouieEtAl2025}." (lines 250-252): In this section, I follow the chain of steps that turns the raw detector data into a transmission spectrum, to show where errors could enter. All three reductions of WASP-17~b used the same basic chain \citep{LouieEtAl2025}.

<sub>id: intro-B-250</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:266` · repetition · proposed by ASTRA, Fable

Current:
```latex
These drifts are measured with reference pixels, pixels that receive no light.
```
Recommended:
```latex
These drifts are measured with reference pixels, which receive no light.
```
Why: "Pixels, pixels" stutters.

Note: Fable's version rejoins two sentences that were split on purpose. Without the comma, "reference pixels that receive no light" also suggests that only some reference pixels receive no light. ASTRA's version keeps the definition.

Other versions:
- Fable: Replace "They also remove slow drifts in the readings. These drifts are measured with reference pixels, pixels that receive no light." with "They also remove slow drifts in the readings, measured with reference pixels that receive no light."

<sub>id: intro-B-266</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:272` · grammar · proposed by ASTRA

Current:
```latex
The readout also adds a correlated noise called $1/f$ noise.
```
Recommended:
```latex
The readout also adds correlated noise called $1/f$ noise.
```
Why: "Noise" reads more naturally here without "a".

<sub>id: intro-B-272</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:278` · repetition · proposed by Fable

Current:
```latex
the pixels of each detector column are read one after
another
```
Recommended:
```latex
the pixels of each detector column are read in sequence
```
Why: "One after another" also ends the sentence before.

Note: Merger adjustment. "Runs down" gives a direction of readout that the report does not otherwise claim. "In sequence" removes the echo without adding a direction. The echo may be deliberate, because it ties the general point to SOSS, so keeping the current text is also reasonable.

Other versions:
- Fable: the readout runs down each detector column

<sub>id: intro-B-278</sub>

#### 1.3 How a transmission spectrum is obtained · `01_introduction.tex:338` · flow · proposed by Opus

Current:
```latex
pixels combined in extraction and the treatment of limb darkening. A further
choice is the model of slow instrumental trends in the light curves, meaning
changes in brightness caused by the instrument rather than by the planet.
```
Recommended:
```latex
pixels combined in extraction, the treatment of limb darkening and the model of slow instrumental trends in the light curves. These trends are changes in brightness caused by the instrument rather than by the planet.
```
Why: "Examples are ... Other choices are ... A further choice is ..." spreads one list over three sentences.

Note: Merger adjustment. Opus's single sentence runs to about 42 words, and its definition hangs off the last item in the list. A short second sentence keeps the definition clear.

Other versions:
- Opus: pixels combined in extraction, the treatment of limb darkening and the model of slow instrumental trends in the light curves, meaning changes in brightness caused by the instrument rather than by the planet.

<sub>id: intro-B-338</sub>

#### 1.4 Two steps where errors could enter · `01_introduction.tex:372` · repetition · proposed by Opus

Current:
```latex
remains in the data after the subtraction. If the residual background is
```
Recommended:
```latex
remains in the data. If this background is
```
Why: "After the subtraction" repeats the second sentence of the paragraph, and "residual background" appears in two sentences in a row.

Note: Opus's rewrite of lines 370-384 only combines this entry with intro-B-378, so it is not repeated as a separate rewrite.

<sub>id: intro-B-372</sub>

#### 1.4 Two steps where errors could enter · `01_introduction.tex:430` · flow · proposed by ASTRA

Current:
```latex
Neither JExoRES nor ATOCA, nor any of the three reductions of WASP-17~b, fits
the background and the transit together in one fit to the detector pixels
```
Recommended:
```latex
JExoRES, ATOCA and the three reductions of WASP-17~b do not fit the background and the transit together on the detector pixels
```
Why: This removes the stacked "neither ... nor ..., nor" and the "fits ... in one fit" repetition.

Note: "Together" keeps the meaning of "in one fit". The citation that follows is unchanged.

<sub>id: intro-B-430</sub>

#### 1.4 Two steps where errors could enter · `01_introduction.tex:468` · repetition · proposed by Fable

Current:
```latex
and could bias the NOVA
spectrum.
```
Recommended:
```latex
and could bias the spectrum.
```
Why: "Could ... bias the NOVA spectrum" also ends the first sentence of the paragraph, four lines earlier.

<sub>id: intro-B-468</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:500` · repetition · proposed by Opus

Current:
```latex
disagreement of this kind shows that a result depends on the reduction. It
does not show which reduction, if any, recovered the true spectrum.
```
Recommended:
```latex
disagreement of this kind does not show which reduction, if any, recovered the true spectrum.
```
Why: Lines 489-490 have just said that a disagreement shows the spectrum depends on the analysis. Only the second half of this pair adds something new.

Note: The current pair of sentences ("shows ... does not show") is a clear contrast and is not wrong. This is a cut for length, so it is Davide's choice.

<sub>id: intro-B-500</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:514` · cut · proposed by Opus

Current:
```latex
Science Institute (STScI), although
```
Recommended:
```latex
Science Institute, although
```
Why: The abbreviation STScI is never used again in the report.

<sub>id: intro-B-514</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:530` · clarity · proposed by Opus, Fable

Current:
```latex
Historically, known test signals have been supplied in two ways.
```
Recommended:
```latex
Earlier studies have supplied known test signals in two ways.
```
Why: "Historically" is a slightly grand opener for examples that run from 2007 to 2026.

Note: Opus's version is active and says who supplied the signals. Fable's is shorter and also fine.

Other versions:
- Fable: Known test signals have been supplied in two ways.

<sub>id: intro-B-530</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:538` · grammar · proposed by Opus

Current:
```latex
also used simulated data, to study
```
Recommended:
```latex
also used simulated data to study
```
Why: The comma makes the purpose clause read like an afterthought.

<sub>id: intro-B-538</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:573` · cut · proposed by ASTRA

Current:
```latex
Data challenges go one step further and score the methods of several teams
against the same known signal.
```
Recommended:
```latex
Data challenges score the methods of several teams against the same known signal.
```
Why: "Go one step further" is a vague way of saying that something comes next, and the rest of the sentence already says what that step is.

<sub>id: intro-B-573</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:581` · consistency · proposed by Fable

Current:
```latex
eight real datasets
```
Recommended:
```latex
eight real data sets
```
Why: Section 2 writes "data set" seven times.

Note: This is a report-wide choice; see the cross-section notes (Section 4, line 237 has "dataset" too).

<sub>id: intro-B-581</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:592` · consistency · proposed by Opus

Current:
```latex
complete pipelines should recover the spectrum, and each should learn the
injected truth only after it has delivered its final result.
```
Recommended:
```latex
complete pipelines should recover the spectrum, each without knowing the injected truth until it has delivered its final result.
```
Why: A pipeline that "learns" reads as personification. Sections 3 and 4 say "without knowing" the truth.

<sub>id: intro-B-592</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:594` · clarity · proposed by Opus

Current:
```latex
combines these four things.
```
Recommended:
```latex
combines all four.
```
Why: "Things" is vague right after a paragraph that calls them needs.

<sub>id: intro-B-594</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:601` · flow · proposed by Opus

Current:
```latex
A transit dims only the starlight. An
injector, the tool that adds the transit to the data, must therefore know
```
Recommended:
```latex
Because a transit dims only the starlight, an injector, the tool that adds the transit to the data, must know
```
Why: The Introduction has already said three times (lines 370, 442 and 474) that a transit dims only the starlight. Given as the reason, it no longer stands out as a short, dramatic sentence.

Note: Opus's rewrite of lines 601-610 combines this entry with intro-B-609 and "That study" -> "It" (dropped). It is not repeated as a separate rewrite.

<sub>id: intro-B-601</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:616` · repetition · proposed by Opus

Current:
```latex
This
difference greatly reduces
```
Recommended:
```latex
This measurement greatly reduces
```
Why: "Difference" appears in four sentences in a row.

Note: Also covered by rewrite intro-B-R2.

<sub>id: intro-B-616</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:618` · consistency · proposed by Opus

Current:
```latex
I will build the benchmark from this
difference
```
Recommended:
```latex
I am building the benchmark from this difference
```
Why: The next two sentences are in the present tense, and the abstract and Section 4 say "I am building". The benchmark is still described as work in progress, not as finished.

Note: Also covered by rewrite intro-B-R2.

<sub>id: intro-B-618</sub>

#### 1.5 Which spectrum is right? · `01_introduction.tex:619` · consistency · proposed by Opus

Current:
```latex
smoothing the faint outer wings.
```
Recommended:
```latex
smoothing the faint far wings.
```
Why: Section 4 calls this region "the far wings", including in the figure captions and in "far-wing model".

Note: Also covered by rewrite intro-B-R2.

<sub>id: intro-B-619b</sub>

#### 1.6 Research question and objectives (objective 2) · `01_introduction.tex:644` · consistency · proposed by Opus

Current:
```latex
adds a known transit to the detector reads of
```
Recommended:
```latex
adds a known transit to the raw reads of
```
Why: Everywhere else the report says "raw reads" (lines 590 and 620, the abstract and Sections 3 and 4).

<sub>id: intro-B-644</sub>

### Section 2, NOVA

#### 2 NOVA (opening paragraph) · `02_nova.tex:14` · repetition · proposed by Opus

Current:
```latex
In this section, I describe NOVA as it is currently
implemented, and end with a first, preliminary spectrum of WASP-17~b.
```
Recommended:
```latex
In this section, I describe NOVA as it is currently
implemented and compare its first, preliminary spectrum of WASP-17~b with the
published Ahsoka spectrum.
```
Why: The roadmap at the end of the Introduction (01:658-659) uses almost the same words about one page earlier. This version keeps the scope phrase and says what Section 2.9 actually does.

Note: Opus nova-14. Merger adjustment: dropped 'part by part', which adds nothing. Change only one of the two places (here or the Introduction roadmap), not both.

Other versions:
- Opus: In this section, I describe NOVA as it is currently
implemented, part by part, and then compare its first, preliminary spectrum of WASP-17~b with the published Ahsoka spectrum.
- Opus: Leave 02:14-15 as it is and shorten the roadmap sentence at 01:658-659 instead.

<sub>id: nova-02</sub>

#### 2.2 The detector model (Figure 4 caption) · `02_nova.tex:40` · grammar · proposed by Fable

Current:
```latex
(a sketch, not data); the fitted apertures
```
Recommended:
```latex
(a sketch, not data). The fitted apertures
```
Why: Replaces a semicolon in the caption with a full stop. Semicolons are above the style target.

Note: Fable 30.

<sub>id: nova-04</sub>

#### 2.2 The detector model · `02_nova.tex:60` · clarity · proposed by Opus

Current:
```latex
in the group $g$ of pixel $p$,
```
Recommended:
```latex
in the group $g$ that contains pixel $p$,
```
Why: 'The group g of pixel p' is hard to parse on first reading.

Note: Opus nova-60.

<sub>id: nova-06</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:110` · clarity · proposed by Opus

Current:
```latex
The group is therefore dimmed by the transit at the wavelengths
of its column,
```
Recommended:
```latex
The fraction of a group's light that remains during the transit is therefore
the mean of the transit light curve over the wavelengths of its column,
weighted by the light that each wavelength contributes,
```
Why: Says in words what the equation computes (a weighted mean of the transit light curve) before the reader meets the symbols, and uses the same wording as nova-07.

Note: Opus nova-110. Merger adjustment: 'remains during the transit', to match nova-07 and Section 4. Also covered by paragraph rewrite nova-PR1. The current sentence is not wrong, so this is polish.

Other versions:
- Opus: The fraction of a group's light that the transit leaves is therefore the mean of the transit light curve over the wavelengths
of its column, weighted by the light that each wavelength contributes,

<sub>id: nova-11</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:128` · clarity · proposed by Opus

Current:
```latex
The two reddest bins receive no light in the model: order~2 does
not reach them, and order~1 is cut at
```
Recommended:
```latex
The two reddest bins receive no light in the model, because order~2 does
not reach them and order~1 is cut at
```
Why: The colon introduces a reason, so 'because' is plainer. It also lowers the colon count, which is above target.

Note: Opus nova-128, first half only. Opus also proposed changing 'this calibration' to 'the PASTASOSS calibration'. That may change the referent, so it is a question for Davide and not part of this entry.

<sub>id: nova-13</sub>

#### 2.4 The transit and the spectrum · `02_nova.tex:154` · repetition · proposed by Opus

Current:
```latex
transit is computed with jaxoplanet
```
Recommended:
```latex
transit light curve is evaluated with jaxoplanet
```
Why: 'Computed' appears in two consecutive sentences, and 'transit light curve' is more precise.

Note: Opus nova-154. Independent of nova-15; both can be applied.

<sub>id: nova-16</sub>

#### 2.5 The continuum, the background and the noise · `02_nova.tex:193` · clarity · proposed by Opus

Current:
```latex
an amplitude that follows one time
pattern $G(t)$,
```
Recommended:
```latex
an amplitude that follows one time
pattern $G(t)$, shared by all maps,
```
Why: 'One time pattern' can be read as one pattern per map. The equation shows that G has no index k.

Note: Opus nova-193.

<sub>id: nova-22</sub>

#### 2.6 The fit · `02_nova.tex:250` · grammar · proposed by Opus

Current:
```latex
increase of the $\chi^2$ of those pixels
```
Recommended:
```latex
increase in the $\chi^2$ of those pixels
```
Why: The idiom is 'an increase in' a quantity, and this avoids 'of ... of'.

Note: Opus nova-250.

<sub>id: nova-30</sub>

#### 2.6 The fit · `02_nova.tex:256` · clarity · proposed by Opus

Current:
```latex
The second limits the curvature of the
deviation in wavelength
```
Recommended:
```latex
The second limits the curvature $\delta''_{oc}$ of the
deviation in wavelength
```
Why: delta'' appears in Eq. 8, but the prose never names it.

Note: Opus nova-256.

<sub>id: nova-31</sub>

#### 2.6 The fit · `02_nova.tex:260` · clarity · proposed by Opus, ASTRA

Current:
```latex
nonlinear in 166 numbers:
```
Recommended:
```latex
nonlinear in 166 parameters:
```
Why: 'Parameters' is the standard term, and the next sentence speaks of 'the nonlinear ones'.

Note: Opus nova-260, ASTRA 31 (first sentence).

<sub>id: nova-32</sub>

#### 2.6 The fit · `02_nova.tex:265` · clarity · proposed by Opus

Current:
```latex
Huber loss is minimised by reweighting. The weights
$w_{tp}=\min(1,\,1.345/|r_{tp}|)$ depend on the residuals, so they are
recomputed after each fit,
```
Recommended:
```latex
Huber loss is minimised by repeated reweighting. Each sample is given the weight
$w_{tp}=\min(1,\,1.345/|r_{tp}|)$. The weights depend on the residuals, so they are
recomputed after each fit,
```
Why: 'The weights w_tp' appear without saying what they weight. Saying that each sample gets a weight makes the loop clear before the stopping rule.

Note: Opus nova-264.

<sub>id: nova-34</sub>

#### 2.7 White-light geometry · `02_nova.tex:276` · clarity · proposed by Opus

Current:
```latex
Whether using
$q^\star_{pg}$ here instead would change the geometry has not been tested.
```
Recommended:
```latex
I have not tested whether using
$q^\star_{pg}$ as the profile instead would change the geometry.
```
Why: The long 'Whether ...' subject delays the verb and hides who has not tested it. No 'yet' is added, so the scope is unchanged.

Note: Opus nova-276.

<sub>id: nova-36</sub>

#### 2.7 White-light geometry · `02_nova.tex:286` · clarity · proposed by Opus

Current:
```latex
accepted only if it gives little weight
```
Recommended:
```latex
accepted only if its posterior gives little weight
```
Why: A fit does not give weight to orbits; its sampled posterior does (the fit is sampled with dynesty).

Note: Opus nova-286.

<sub>id: nova-37</sub>

#### 2.9 A first spectrum of WASP-17 b · `02_nova.tex:312` · clarity · proposed by Opus

Current:
```latex
from a reduction of 18 September 2026
```
Recommended:
```latex
from a reduction made on 18 September 2026
```
Why: 'A reduction of 18 September' can be read as a reduction of data taken on that date.

Note: Opus nova-312.

<sub>id: nova-39</sub>

#### 2.9 A first spectrum of WASP-17 b · `02_nova.tex:323` · flow · proposed by Opus

Current:
```latex
because there the starlight is faintest
```
Recommended:
```latex
because the starlight is faintest there
```
Why: Putting 'there' first sounds stilted, and the plain word order reads more naturally.

Note: Opus nova-323. See the question on 'matters most'.

<sub>id: nova-41</sub>

### Section 3, Building a benchmark

#### 3.1 What a benchmark needs (PDF p. 15) · `03_benchmark.tex:11` · consistency · proposed by Opus

Current:
```latex
injection into the raw reads,
and several pipelines
```
Recommended:
```latex
injection into the raw reads
and several pipelines
```
Why: The rest of the report writes lists as "A, B and C" with no comma before "and".

Note: From Opus's cross-section notes. Fable makes the same point for Section 6 (entry 06-3).

<sub>id: abs-s3-s5-s6-preamble-03-11</sub>

#### 3.1 What a benchmark needs (PDF p. 15) · `03_benchmark.tex:13` · grammar · proposed by Opus

Current:
```latex
the injector has to decide which of the observed light is
```
Recommended:
```latex
the injector has to decide which part of the observed light is
```
Why: "Which of" with the mass noun "light" is slightly unidiomatic; the Introduction (line 603) says "which part of the recorded light".

Note: Same change as abstract entry 00-16; this one can be made even if the abstract stays as approved.

<sub>id: abs-s3-s5-s6-preamble-03-13</sub>

#### 3.1 What a benchmark needs (PDF p. 15) · `03_benchmark.tex:19` · flow · proposed by Opus

Current:
```latex
and this section describes
what they taught me.
```
Recommended:
```latex
and in this section I describe
what they taught me.
```
Why: Uses the first-person signpost of the style rules ("In this section, I ...") instead of the section as subject.

<sub>id: abs-s3-s5-s6-preamble-03-19</sub>

#### 3.2 Injecting into the raw reads (PDF p. 15) · `03_benchmark.tex:26` · repetition · proposed by Opus

Current:
```latex
This is simple, but it adds the transit
only after the steps
```
Recommended:
```latex
This is simple, but the transit then does not pass through the steps
```
Why: The previous sentence already says "after the detector stages"; this removes the second "adds the transit ... after".

Note: Merger adjustment: "does not pass through" instead of Opus's "skips", because a transit that "skips" steps reads oddly.

Other versions:
- Opus: This is simple, but the transit then skips the steps

<sub>id: abs-s3-s5-s6-preamble-03-26</sub>

#### 3.2 Injecting into the raw reads (PDF p. 15) · `03_benchmark.tex:41` · clarity · proposed by Fable

Current:
```latex
Near the traces, this model matched the real images, but outside them, at
```
Recommended:
```latex
Near the traces, this model matched the real images. Outside them, at
```
Why: Splits a 35-word sentence into the part that worked and the part that did not.

Note: Also covered by rewrite abs-s3-s5-s6-preamble-R1.

Other versions:
- Opus: No split (his paragraph rewrite keeps the sentence whole).

<sub>id: abs-s3-s5-s6-preamble-03-41</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:59` · AI tell · proposed by Opus

Current:
```latex
To see how much this matters, I made three
```
Recommended:
```latex
To see how strongly the recovered spectra depend on this, I made three
```
Why: Second "matters" in two paragraphs (style_check flags "this matters"); the new wording says what is being measured.

Note: Taste. Also covered by rewrite R2.

Other versions:
- Fable: No change: Fable judged this "this matters" a legitimate use.

<sub>id: abs-s3-s5-s6-preamble-03-59</sub>

#### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex:88` · consistency · proposed by Opus

Current:
```latex
Under the upper estimate the order
reversed
```
Recommended:
```latex
Under the upper estimate, the ranking
reversed
```
Why: The abstract and Section 5.1 call this "the ranking"; the comma matches "Under the lower estimate," one sentence earlier.

<sub>id: abs-s3-s5-s6-preamble-03-88</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:114` · repetition · proposed by Fable

Current:
```latex
I also measured how much the faint light outside the traces dims
```
Recommended:
```latex
I then measured how much the faint light outside the traces dims
```
Why: The previous paragraph also opens "I also".

Note: Also covered by rewrite R4.

<sub>id: abs-s3-s5-s6-preamble-03-114-then</sub>

#### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex:114` · consistency · proposed by Fable, Opus, ASTRA

Current:
```latex
$0.033\pm0.007$~DN\,s$^{-1}$ per pixel
```
Recommended:
```latex
$0.033\pm0.007$~DN\,s$^{-1}$ per pixel
```
Why: No change here. The unit is written DN\,s$^{-1}$ in Sections 3 and 4 (three times) but DN/s in Section 2 (twice); the fewest edits make Section 2 match.

Note: Opus asked for one form without choosing; ASTRA (item 26, Section 2) converts Section 2 to DN\,s$^{-1}$; Fable prefers DN/s everywhere. Recommended: DN\,s$^{-1}$ throughout, so the change belongs in Section 2.

Other versions:
- Fable: $0.033\pm0.007$~DN/s per pixel (and DN/s in Section 4 too)

<sub>id: abs-s3-s5-s6-preamble-03-114-unit</sub>

### Section 4, The measured benchmark

#### 4 A Benchmark with Measured Starlight (opening paragraph) · `04_measured_benchmark.tex:5` · consistency · proposed by Opus

Current:
```latex
once moved away
from the strip that SOSS time series read out.
```
Recommended:
```latex
once moved off
the strip that SOSS time series read out.
```
Why: The abstract and the Introduction both say "moved off the strip"; use the same words here.

<sub>id: measured-5</sub>

#### 4 A Benchmark with Measured Starlight (opening paragraph) · `04_measured_benchmark.tex:7` · flow · proposed by Opus

Current:
```latex
so the injector depends
much less on a fitted split between starlight and background.
```
Recommended:
```latex
so the injector depends
much less on a fitted split between starlight and background. In this
section, I describe how I turn this difference into a cleaned image of the
star and inject it with a known transit, how I will test the injector and the
pipelines, and the limitations of the benchmark.
```
Why: Section 4 has no signpost, unlike Section 2; one sentence naming the four subsections tells the reader where the long Section 4.1 is heading.

Note: Matter of taste: Opus also raised this as a question (Sections 3 and 4 have no 'In this section' opening). The style rules ask for signposts but warn against adding 'In this section' just to hit a number. The list has four items because there are four subsections.

<sub>id: measured-7</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:32` · cut · proposed by Opus

Current:
```latex
do not cancel, because they change from moment to moment.
```
Recommended:
```latex
do not cancel.
```
Why: The reason repeats the subject: offsets "that vary in time" fail to cancel "because they change from moment to moment".

Note: Keep the clause if Davide wants the reason spelled out for the read noise too, which the subject does not describe as varying in time.

<sub>id: measured-31</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:37` · consistency · proposed by Fable

Current:
```latex
0.05~DN\,s$^{-1}$ per pixel
```
Recommended:
```latex
0.05~DN\,s$^{-1}$ per pixel
```
Why: The report writes the count-rate unit two ways: DN/s in Section 2 (twice) and DN\,s$^{-1}$ in Sections 3 and 4 (three times). One form should be used throughout.

Note: No change in Section 4 under the recommended choice. DN\,s$^{-1}$ is the usual form in astronomy journals and already the majority form, so ASTRA's item 26 (change the two DN/s in Section 2) is the fix. Fable prefers DN/s everywhere, which would change lines 37 and 140 here and 03:114. Davide's call.

Other versions:
- Fable: 0.05~DN/s per pixel (and "0.017~DN/s" at line 140)

<sub>id: measured-37</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:41` · clarity · proposed by Opus

Current:
```latex
this makes the depth 2 to 19~ppm shallower
```
Recommended:
```latex
the undimmed glow makes the depth 2 to 19~ppm shallower
```
Why: Names what makes the depth shallower instead of "this".

Note: After measured-38, "this" directly follows "the glow does not dim", so the change is optional.

<sub>id: measured-41</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:69` · consistency · proposed by Opus

Current:
```latex
I move each star's catalogue
```
Recommended:
```latex
I update each star's catalogue
```
Why: "Move" already names the moved exposure and the moved star; "update ... to the date of the observation" is the plain verb for a catalogue position.

<sub>id: measured-69</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:72` · repetition · proposed by Opus

Current:
```latex
The grism slightly rotates and stretches this pattern, and each field star's
spectra are those of the target, moved by the star's offset from it.
```
Recommended:
```latex
The grism slightly rotates and stretches this pattern of positions.
```
Why: The second clause is repeated, more precisely, after Eq. (9) a few lines later ("The spectra of star i are those of the target, moved by A Delta_i").

Note: Optional: the clause works as a plain-language preview before the equation, and the cut removes it. Keep it if Davide likes the preview.

<sub>id: measured-72</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:86` · consistency · proposed by Opus

Current:
```latex
target, moved by $\mathbf{A}\,\boldsymbol{\Delta}_i$.
```
Recommended:
```latex
target, shifted by $\mathbf{A}\,\boldsymbol{\Delta}_i$.
```
Why: Keeps "moved" for the moved exposure and the moved star, and uses "shifted" for a change of position on the detector.

Note: Also covered by rewrite measured-R1 (Opus proposed it only inside his paragraph rewrite).

<sub>id: measured-86a</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:125` · flow · proposed by Opus

Current:
```latex
Thirdly, the far wings are noisy.
```
Recommended:
```latex
Thirdly, the far wings of the difference are noisy.
```
Why: "Secondly" is a page and a figure earlier; "of the difference" links back to the three reasons announced at line 34.

Note: Also covered by rewrite measured-R2.

<sub>id: measured-125</sub>

#### 4.1 Measuring the star · `04_measured_benchmark.tex:130` · clarity · proposed by ASTRA

Current:
```latex
Dividing
each pixel by its uncertainty
```
Recommended:
```latex
Dividing
each pixel's count rate by its uncertainty
```
Why: Names the quantity that is divided, instead of dividing "each pixel".

Note: Also covered by rewrite measured-R2.

<sub>id: measured-130</sub>

#### 4.1 Measuring the star (Figure 8 caption) · `04_measured_benchmark.tex:158` · clarity · proposed by Opus

Current:
```latex
far wings smoothed (a preliminary version, made before the corrections for
  the sky and the halo of the moved star).
```
Recommended:
```latex
far wings smoothed. It is a preliminary version, made before the corrections
  for the sky and the halo of the moved star.
```
Why: The panel description runs to 45 words and ends in a long parenthesis; the caveat reads better as its own sentence, as it already is in the Figure 9 caption.

Note: If measured-111 is applied, make this change in the moved copy (which becomes Figure 7). See also the question on which sky correction is meant.

<sub>id: measured-156</sub>

#### 4.1 Measuring the star (Figure 8 caption) · `04_measured_benchmark.tex:162` · consistency · proposed by Opus

Current:
```latex
the predictions are moved by 10
```
Recommended:
```latex
the predictions are shifted by 10
```
Why: Avoids another "moved" in a caption about the moved exposure.

Note: If measured-111 is applied, make this change in the moved copy.

<sub>id: measured-162</sub>

#### 4.1 Measuring the star (Figure 9 caption) · `04_measured_benchmark.tex:179` · clarity · proposed by Opus

Current:
```latex
negative values are kept
```
Recommended:
```latex
negative values can be shown
```
Why: "Kept" suggests a processing step; the point is that the axis can display negative values.

<sub>id: measured-179</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:223` · grammar · proposed by Opus

Current:
```latex
behaves as real light
```
Recommended:
```latex
behaves like real light
```
Why: "As" can read as "in the role of", but the meaning is "in the same way as". Section 3.4 already says "behaves like starlight".

<sub>id: measured-223</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:226` · grammar · proposed by Fable

Current:
```latex
Nothing else is added: the bias
```
Recommended:
```latex
Nothing else is added. The bias
```
Why: Replaces a colon with a full stop; the section is above the colon target.

<sub>id: measured-226</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:233` · repetition · proposed by Fable

Current:
```latex
Comparing this with the injected transit shows whether and where the
```
Recommended:
```latex
Comparing this with the injected transit reveals whether and where the
```
Why: "Shows" appears in three consecutive sentences.

<sub>id: measured-234</sub>

#### 4.2 Injecting the star · `04_measured_benchmark.tex:237` · consistency · proposed by Opus, Fable

Current:
```latex
A single dataset with a transit
```
Recommended:
```latex
A single data set with a transit
```
Why: Section 2 writes "data set" seven times; this and 01:581 are the only "dataset".

Note: Fable also changes 01:581 ("eight real datasets"), which belongs to the Introduction part.

<sub>id: measured-237</sub>

#### 4.2 Injecting the star (Figure 10 caption) · `04_measured_benchmark.tex:256` · clarity · proposed by Opus

Current:
```latex
stay there and do not transit
```
Recommended:
```latex
stay in the data and do not transit
```
Why: "There" has no clear place to refer to.

Note: Taste: "there" can be read as "in the moved exposure", which is also correct.

<sub>id: measured-256</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:305` · consistency · proposed by Fable

Current:
```latex
series, while its $1/f$ noise is similar.
```
Recommended:
```latex
series, whilst its $1/f$ noise is similar.
```
Why: Sections 1 and 2 use "whilst" throughout, and the style rules list it; this is one of only three "while"s in the report.

Note: Opus noted the same inconsistency without proposing a change here. ASTRA's Section 5 rewrite keeps "while". Recommended: "whilst" everywhere (04:305, 05:58, 05:62).

<sub>id: measured-305</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:309` · clarity · proposed by Opus

Current:
```latex
the star's light in
its box.
```
Recommended:
```latex
the star's light in
the exoTEDRF extraction box.
```
Why: "Its box" can be read as the star's box.

<sub>id: measured-309</sub>

#### 4.4 Limitations · `04_measured_benchmark.tex:330` · grammar · proposed by Fable

Current:
```latex
uses such a prior: each fits the shape
```
Recommended:
```latex
uses such a prior. Each fits the shape
```
Why: Replaces a colon; the section is above the colon target.

Note: Merger adjustment: a full stop keeps the second clause as the explanation, whereas Fable's ", and" turns it into a second, separate claim.

Other versions:
- Fable: uses such a prior, and each fits the shape

<sub>id: measured-330</sub>

### Section 5, Discussion and plan

#### 5.1 Discussion (PDF p. 22) · `05_discussion_plan.tex:22` · grammar · proposed by Fable

Current:
```latex
I will then use it to test NOVA and the other
pipelines and to improve NOVA, and only then refit WASP-17~b.
```
Recommended:
```latex
I will then use it to test NOVA and the other
pipelines, improve NOVA, and only then refit WASP-17~b.
```
Why: Removes the "and ... and ... and" chain.

Note: The comma before "and only then" is deliberate emphasis, not a serial comma. Also covered by rewrite R5.

<sub>id: abs-s3-s5-s6-preamble-05-22</sub>

#### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex:74` · flow · proposed by Opus, ASTRA

Current:
```latex
I will analyse all five visits
with the same version of NOVA
```
Recommended:
```latex
I will analyse all five visits
with the same version of NOVA
```
Why: A paragraph break separates the reasons for each visit from the rule on the NOVA version; the Paper 2 paragraph currently runs for almost a full column.

Note: One break (Opus) is recommended; ASTRA's per-target paragraphs would leave several two-sentence paragraphs. Also covered by rewrite R6.

Other versions:
- ASTRA: Six paragraphs: the design, then one paragraph per target, then the version rule.

<sub>id: abs-s3-s5-s6-preamble-05-74</sub>

#### 5.2 Research plan, Paper 3 (PDF p. 24) · `05_discussion_plan.tex:91` · repetition · proposed by Fable

Current:
```latex
and one for the spots and bright
regions that the planet does not cross.
```
Recommended:
```latex
and one for the spots and bright
regions outside the planet's path across the star.
```
Why: "That the planet does not cross" is the third use in this paragraph.

Note: Merger adjustment: "across the star" added so "path" cannot be read as the orbit.

Other versions:
- Fable: and one for the spots and bright regions outside the planet's path.

<sub>id: abs-s3-s5-s6-preamble-05-91</sub>

#### 5.2 Research plan, Paper 3 (PDF p. 24) · `05_discussion_plan.tex:93` · clarity · proposed by Opus

Current:
```latex
flares and such stellar signals into the benchmark
```
Recommended:
```latex
flares and the signals of such spots and bright regions into the benchmark
```
Why: "Such stellar signals" is vague, and flares are stellar signals too.

<sub>id: abs-s3-s5-s6-preamble-05-93</sub>

#### 5.2 Research plan, Figure 11 (Gantt chart and caption, PDF p. 25) · `05_discussion_plan.tex:154` · clarity · proposed by Opus

Current:
```latex
{Instrument and geometry extensions}
```
Recommended:
```latex
{Extensions to NIRSpec and eclipses}
```
Why: "Geometry extensions" makes a reader think of transit geometry, not secondary eclipses; the new label matches the plan's own summary.

Other versions:
- Fable: No change: Fable found the Gantt labels fine.

<sub>id: abs-s3-s5-s6-preamble-05-154</sub>

#### 5.2 Research plan, Figure 11 (Gantt chart and caption, PDF p. 25) · `05_discussion_plan.tex:164` · consistency · proposed by Opus

Current:
```latex
{Thesis integration}
```
Recommended:
```latex
{Thesis chapters from papers}
```
Why: In this report "integration" is a detector exposure, used dozens of times, so a bar called "Thesis integration" makes the reader pause.

Note: Depends on what the bar means; see the question to Davide.

Other versions:
- Fable: No change: Fable found the Gantt labels fine.

<sub>id: abs-s3-s5-s6-preamble-05-164</sub>

### Use of generative AI

#### Use of generative AI (unnumbered, PDF p. 25) · `06_ai_use.tex:1` · consistency · proposed by Fable

Current:
```latex
\section*{Use of generative AI}
```
Recommended:
```latex
\section*{Use of Generative AI}
```
Why: Every other section title is in title case.

Other versions:
- Opus: No change to Section 6.
- ASTRA: No change to Section 6.

<sub>id: abs-s3-s5-s6-preamble-06-1</sub>

#### Use of generative AI (unnumbered, PDF p. 25) · `06_ai_use.tex:3` · consistency · proposed by Fable

Current:
```latex
coding, and
wording.
```
Recommended:
```latex
coding and
wording.
```
Why: The report writes lists as "A, B and C" elsewhere.

Note: Taste: here the comma does separate "literature searches and summaries" from the last two items, so keeping it is defensible.

Other versions:
- Opus: No change to Section 6.
- ASTRA: No change to Section 6.

<sub>id: abs-s3-s5-s6-preamble-06-3</sub>

### conventional_reduction_workflow.tex

#### 1.3 How a transmission spectrum is obtained (Figure 3a, label beside the ramp) · `conventional_reduction_workflow.tex:48` · clarity · proposed by Opus

Current:
```latex
{fit clean slopes\\to retain rate}
```
Recommended:
```latex
{rate fitted on\\either side}
```
Why: "Fit clean slopes to retain rate" is hard to understand. The new label says plainly that the rate is fitted on either side of the jump, which is what the panel draws.

Note: Merger adjustment. Opus's label repeats the caption's wording, but it is too wide. In the figure's \scriptsize font, "unaffected differences" is about 79 pt wide. Only about 59 pt fit between the start of the label (x = 2.78 cm) and the frame of panel (a) at x = 4.95 cm, so the label would cross into panel (b). "rate fitted on" is 49 pt and "either side" is 38 pt; the current lines are 55 pt and 50 pt. I measured the widths with pdflatex in a scratch file, not in the report itself.

Other versions:
- Opus: {rate fitted from\\unaffected differences}
- ASTRA: Keep the current label (ASTRA found no wording change needed in the diagram labels).

<sub>id: intro-B-fig3-label</sub>

## 6. Paragraph rewrites (alternatives to the listed entries)

### 3.2 Injecting into the raw reads (PDF p. 15) · `03_benchmark.tex`, lines 41-48 · proposed by Opus, Fable

Starts: "My injector, however, dimmed only its model of the star.". Replaces entries: abs-s3-s5-s6-preamble-03-41, abs-s3-s5-s6-preamble-03-44.

```latex
My injector, however, dimmed only its model of the star. Near the traces,
this model matched the real images. Outside them, at 0.85 to
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
correction assumes (Section~\ref{sec:real-data-test}), so a large part of this
faint light seems to behave like starlight.
```
Why: Opus's reorder: the real-data sentence now comes after the cause and its 'therefore' consequence instead of between them, so 'To confirm this' points to the mechanism, and the sentence becomes a preview of Section 3.4 with a pointer. Adds Fable's split of the first long sentence and the 03-44 fix. Merger adjustment: 'so much of this faint light' becomes 'so a large part of this faint light', because 'so much' first reads as an intensifier; Fable's split of the 'removed it from the whole column, so ...' sentence is not used (see dropped). No number or condition changes. Pairs well with entry 03-50.

### 3.3 Which light belongs to the star (PDF p. 16) · `03_benchmark.tex`, lines 58-70 · proposed by Opus, Fable, ASTRA

Starts: "The WASP-17~b data alone cannot say how much of this light is starlight, not". Replaces entries: abs-s3-s5-s6-preamble-03-59, abs-s3-s5-s6-preamble-03-61, abs-s3-s5-s6-preamble-03-64, abs-s3-s5-s6-preamble-03-66, abs-s3-s5-s6-preamble-03-67a, abs-s3-s5-s6-preamble-03-67b.

```latex
The WASP-17~b data alone cannot say how much of this light is starlight, not
even inside the extraction box. To see how strongly the recovered spectra
depend on this, I made three injections. All three dim the measured light in
the wings, 16 to 80 pixels from the traces. In the first, the lower estimate,
only the light that a model of the star explains counts as starlight near the
traces. I made this model by fitting the star's spectrum, with a slow change
in time, to the out-of-transit images through ATOCA's model of the detector.
The fit also included a smooth background, made of four of NOVA's eight
background maps and held in place by the off-trace pixels that NOVA uses
(Section~\ref{sec:continuum}). In exoTEDRF's 40-row extraction box, this
estimate typically leaves 0.4\% of the light undimmed at 1.0 to
$1.8\,\mu\mathrm{m}$, 2.2\% at 1.8 to $2.3\,\mu\mathrm{m}$ and 4.0\% at 2.3
to $2.8\,\mu\mathrm{m}$. The lower estimate also leaves the faint light beyond
80 pixels undimmed. The second injection is the same, except that it also
dims this faint light. Dimming this light changed NOVA's spectrum by about
40~ppm. The third, the upper estimate, instead counts all the light in the box
as starlight and dims it. Like the lower estimate, it leaves the faint light
beyond 80 pixels undimmed.
```
Why: The hardest paragraph in this part to read on a first pass. Based on Opus's rewrite, with the fit sentence split as all three reviewers proposed and the semicolon removed as Opus and Fable proposed: the three injections are numbered as announced, the delayed definition of the lower estimate and the four-modifier fit sentence are untangled, and each percentage sits next to its range. Merger adjustments as in entries 03-61 and 03-67a; 'The lower estimate also leaves' is kept as written (Opus had 'It also leaves'). No number, range or condition changes.

### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex`, lines 106-112 · proposed by Opus, Fable, ASTRA

Starts: "I also tried to measure the share of starlight directly from the real data.". Replaces entries: abs-s3-s5-s6-preamble-03-107, abs-s3-s5-s6-preamble-03-108, abs-s3-s5-s6-preamble-03-110.

```latex
I also tried to measure the share of starlight in the box directly from the
real data. If the bright centre of the trace is almost pure starlight, and all
the light in the extraction box is starlight too, the box dims during the
transit by the same fraction as the centre. If part of the light in the box is
background, the box dims less. In the red part of order~1, the two fractions
typically agreed to within about 1\%, which would favour the upper estimate.
To check how reliable this comparison is, I repeated it on stretches without
a transit. I fitted the same transit shape to the box and to the bright
centre, at a time when no transit happens. Both fitted depths should be zero,
so they should agree. Instead, they differed by up to about 11\% of the real
transit depth, ten times more than the 1\% needed to tell the two estimates
apart. The real data therefore cannot decide.
```
Why: Merges Opus's rewrite and ASTRA's P3 with Fable's items 47 and 48: the semicolon and the colon reveal go, the two conditions are stated separately (ASTRA), 'the share of starlight in the box' and 'the two fractions' say what is measured and compared (Opus), and the null test says the two depths should agree (merger adjustment, see entry 03-110). ASTRA's 'should dim' and 'To check the reliability of' are not used; Davide's 'dims' and 'how reliable' are kept. The closing sentence is unchanged.

### 3.4 The real data cannot decide (PDF p. 16) · `03_benchmark.tex`, lines 114 · proposed by Opus, Fable, ASTRA

Starts: "I also measured how much the faint light outside the traces dims during the real transit,". Replaces entries: abs-s3-s5-s6-preamble-03-114-then, abs-s3-s5-s6-preamble-03-114a, abs-s3-s5-s6-preamble-03-114b, abs-s3-s5-s6-preamble-03-114c.

```latex
I then measured how much the faint light outside the traces dims during the
real transit, on the pixels that the $1/f$ correction uses. At 0.85 to
$1.75\,\mu\mathrm{m}$ in order~1, it dimmed by
$0.033\pm0.007$~DN\,s$^{-1}$ per pixel, as much as if all the light left
there after background subtraction were starlight. This suggests that most of
this light behaves like starlight. Only this range gives a clear answer,
however. At 1.75 to $2.1\,\mu\mathrm{m}$, the measurement is too noisy to tell
the cases apart. At 2.1 to $2.8\,\mu\mathrm{m}$, the light appears to dim
about four times more than even starlight would, which I cannot explain. Even
where the answer is clear, it depends on how the detector behaves. If the fit
allows the detector's level to change during the transit, the share of this
light that dims like starlight ranges from about half to all of it. The
measurement cannot tell the injector how much of this light to dim.
```
Why: Removes both colon reveals (all three reviewers flagged the first, Opus and Fable the second) and the double 'it', gives the two other ranges their own sentences (ASTRA), opens with 'I then' (Fable) and, following Opus, moves the conclusion that the measurement cannot tell the injector how much to dim from the middle, where it came before its reasons, to the end. No 'therefore' is added, so no new causal claim is made. Every number and range is unchanged.

### 5.1 Discussion (PDF p. 22) · `05_discussion_plan.tex`, lines 18-23 · proposed by Fable, Opus, ASTRA

Starts: "This lesson sets the order of the work.". Replaces entries: abs-s3-s5-s6-preamble-05-20, abs-s3-s5-s6-preamble-05-21, abs-s3-s5-s6-preamble-05-22.

```latex
This lesson sets the order of the work. NOVA's first spectrum of the real
WASP-17~b visit is deeper than the published Ahsoka spectrum at every
wavelength, most in the red (Section~\ref{sec:nova-real}). Its uncertainty is
not yet validated. An injection test shows how accurately each method
recovers a known spectrum. This is the best guide to which real spectrum to
trust, but an injector built from the WASP-17~b data alone cannot provide it.
I am therefore finishing the benchmark first. I will then use it to test NOVA
and the other pipelines, improve NOVA, and only then refit WASP-17~b.
```
Why: Merges Fable's 3C with Opus's items 05-20 and 05-21 and ASTRA's item 51: the double 'and' and the 'which ... which ... it' chain go, the uncertainty limitation gets its own sentence as in the abstract, and the wording 'at every wavelength, most in the red' matches the abstract. Fable's 'cannot provide such a test' is not used (see entry 05-21).

### 5.2 Research plan, Paper 2 (PDF pp. 23-24) · `05_discussion_plan.tex`, lines 50-79 · proposed by Opus, ASTRA, Fable

Starts: "\paragraph{Paper 2: Five further SOSS visits.} The aim is to find out whether". Replaces entries: abs-s3-s5-s6-preamble-05-53, abs-s3-s5-s6-preamble-05-56, abs-s3-s5-s6-preamble-05-58b, abs-s3-s5-s6-preamble-05-58a, abs-s3-s5-s6-preamble-05-62, abs-s3-s5-s6-preamble-05-63, abs-s3-s5-s6-preamble-05-64, abs-s3-s5-s6-preamble-05-69, abs-s3-s5-s6-preamble-05-72, abs-s3-s5-s6-preamble-05-74, abs-s3-s5-s6-preamble-05-77.

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
causes of the disagreement, and I will test which side NOVA's spectrum
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
Why: The paragraph runs for almost a full column, and most of its sentences have comma or 'which' problems. Based on Opus's rewrite, merged with ASTRA's P5 and Fable's items 70, 82, 83 and 84 and with the merger adjustment of entry 05-63. One paragraph break (Opus) separates the per-visit reasons from the rule on the NOVA version; ASTRA's one-paragraph-per-target layout is offered in entry 05-74 instead. The last sentence is kept (Fable would cut it; see questions). The 'NOVA's differences' change assumes the reading in the question to Davide. All citations, targets, numbers and hedges are unchanged.

### 1 Introduction and Literature Review (opening paragraph) · `01_introduction.tex`, lines 4-16 · proposed by Opus

Starts: "The transmission spectrum of an exoplanet is the depth of its transit". Replaces entries: intro-A-07a, intro-A-07b, intro-A-08, intro-A-11, intro-A-12.

```latex
The transmission spectrum of an exoplanet is the depth of its transit, the
fraction of starlight that the planet blocks, at each wavelength. It is
obtained from a time series of detector images through a chain of processing
steps. Errors could enter at many points in this chain, and I focus on two of
them. The first is the subtraction of the background light. Any background
that remains is not modelled when the transit is fitted. An error in that
subtraction can bias the fitted transit depth, even when the transit model
fits the data well. The second is the compression of each image into a
one-dimensional spectrum. This compression can lose information that the
later steps cannot recover.

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
Why: This rewrite splits the 200-word opening into the problem (the two error points) and the response (NOVA, then the benchmark), and it applies the merged wording of the five entries. Every fact, scope word and term ('the established methods', 'a known truth') is kept. Apply either this rewrite or its entries, not both.

### 1.2 JWST, NIRISS/SOSS and WASP-17 b · `01_introduction.tex`, lines 193-205 · proposed by Opus

Starts: "Despite these difficulties, SOSS has delivered detailed spectra. For example,". Replaces entries: intro-A-195, intro-A-197.

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
Why: This rewrite gives the project's target its own paragraph and folds in the two-sentence 'However, that spectrum ...' paragraph, since both describe WASP-17 b before SOSS. It also fixes the hyphenated range. All citations and claims are unchanged. Apply either this rewrite or intro-A-195 and intro-A-197, not both.

### 1.4 Two steps where errors could enter · `01_introduction.tex`, lines 417-428 · proposed by Opus, Fable

Starts: "The second method, ATOCA, addresses the overlap of the orders. ATOCA models". Replaces entries: intro-B-417, intro-B-421, intro-B-427.

```latex
The second method, ATOCA, addresses the overlap of the orders. It models every pixel as the sum of the light of both orders. Because the two orders are copies of the same stellar spectrum, one spectrum has to explain both. ATOCA can therefore separate the two orders during the extraction \citep{DarveauBernierEtAl2022}. It needs the profile of each order across the detector, and the APPLESOSS package can estimate these profiles from the observation itself \citep{RadicaEtAl2022}. Like JExoRES, however, ATOCA still extracts the spectrum before the transit is fitted. In the supreme-SPOON reduction of WASP-17~b, for example, the background was subtracted before the ATOCA extraction, and the transit was fitted to the extracted light curves afterwards \citep{LouieEtAl2025}.
```
Why: This combines the three entries. "It" and "ATOCA" now alternate, so four sentences in a row no longer start with "ATOCA", and the closing sentence that repeats the JExoRES paragraph is cut. All three citations are kept. Opus's rewrite also merged the "Because ..." and "ATOCA can therefore ..." sentences; that merge is left out (see dropped). Apply this rewrite or its three entries, not both.

### 1.5 Which spectrum is right? · `01_introduction.tex`, lines 612-625 · proposed by Opus

Starts: "Calibration programme 4476 was designed to measure the light outside the". Replaces entries: intro-B-613, intro-B-616, intro-B-618, intro-B-619, intro-B-619b, intro-B-622.

```latex
Calibration programme 4476 was designed to measure the light outside the extraction box \citep{VolkEspinoza2023}. In a SOSS time series, only a strip of the detector is read out. Programme 4476 observed a star at its usual position on this strip, and then again with the star moved off the strip. On the strip, the difference between the two exposures measures the light of the star. This measurement greatly reduces the need to split the observed light into starlight and background with a fit. I am building the benchmark from this difference (Section~\ref{sec:measured-benchmark}). I first turn it into a cleaned image of the star, by removing the field sources (field stars and any other objects in the field) and smoothing the faint far wings. I then dim this image with a known transit and add it to the raw reads of the exposure in which the star was moved off the strip. The noise, the background and the field stars of that exposure are real. Because I apply the transit to the cleaned image myself, the injected signal will be known exactly for that image. The benchmark is designed to show whether the established pipelines recover a known transit without a detectable bias, and whether NOVA improves on them.
```
Why: This is Opus's rewrite, checked sentence by sentence against the current text. It gives the extraction box, the cleaned image and the far wings one name each, uses "difference" two times instead of four, and makes the tenses consistent ("am building", "turn", "will be known"). Its only extra change is "I first turn the difference into" -> "I first turn it into". "Will be known" stays because the benchmark is not built yet. Both the citation and the cross-reference are kept. Apply this rewrite or its six entries, not both.

### 2.4 The transit and the spectrum · `02_nova.tex`, lines 99-121 · proposed by Opus

Starts: "Each column records light from a range of wavelengths.". Replaces entries: nova-10, nova-11.

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
group's own order is modelled. The fraction of a group's light that remains
during the transit is therefore the mean of the transit light curve over the
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
Why: This is the paragraph with nova-10 and nova-11 applied, so it can be read as a whole. Apply either the two entries or this rewrite. It removes a colon, two semicolons and three 'which' clauses, avoids repeating 'combines', and says in words what Eq. 4 computes.

### 2.5 The continuum, the background and the noise · `02_nova.tex`, lines 200-205 · proposed by Opus, Fable, ASTRA

Starts: "The 244,657 off-trace pixels, away from the traces, field stars and bad pixels,". Replaces entries: nova-23, nova-24.

```latex
The 244,657 off-trace pixels lie away from the traces, field stars and bad
pixels. They are assumed to see only background, although some starlight from
the faint wings of the traces may reach them (Section~\ref{sec:which-light}).
The maps are made orthonormal over these pixels. The maps and these pixels
were chosen once from the WASP-17~b visit, where eight maps predicted held-out
strips of the off-trace image better than two or four. I have not yet tested
how well the maps describe the background under the traces, or how much an
error in the maps there would change the depths.

Field stars are left out of the off-trace pixels and of the $1/f$ correction
(Section~\ref{sec:detector-processing}), but NOVA does not yet treat
field-star light that falls on the traces, which it cannot tell apart from the
light of the target. A treatment of such light, for example with the positions
of field-star spectra that Gaia predicts (Section~\ref{sec:measuring-star}),
is future work, needed for both the benchmark and the WASP-17~b visit.
```
Why: Merges the three reviewers' rewrites of this passage (Opus lines 190-205, Fable 3A, ASTRA P2). The off-trace pixels, their maps and the untested point now stand together, and the field-star limitation agreed today gets its own short paragraph. Apply either nova-23 and nova-24 or this rewrite. The equation and the sentences before it (lines 190-199) are untouched, and nova-22 is separate.

### 4.1 Measuring the star · `04_measured_benchmark.tex`, lines 75-109 · proposed by Opus, Fable, ASTRA

Starts: "I fitted this rotation and stretch on the WASP-17~b data". Replaces entries: measured-86a, measured-86, measured-93, measured-105, measured-109a, measured-109.

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

To locate the compact sources, I first subtracted a running median over 51
columns from each row. This removed everything that is smooth along the rows,
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

Programme 4476 cannot provide such a fit. Its field is sparse, with 208 Gaia
stars within $5.4'$ of the target against 1,455 around WASP-17. Its strip
contains the undispersed image of at most one Gaia star, which is very faint.
Both observations used the same instrument setting, so I use the WASP-17~b fit
for programme 4476. I will check the faint spectra that this fit predicts in
both pointings. The injector finds field sources from the images, with Gaia
guiding the search. Because NOVA may later use the same Gaia predictions,
agreement between NOVA and the injector would not by itself show that the
field-star light was separated correctly.
```
Why: The paragraph runs to about 600 words and does four jobs (the mapping, the detection of compact sources, the matching and fit, and the use of the fit for programme 4476). The rewrite breaks it at those three points (Fable proposed two of the breaks, Opus all three) and applies the six listed entries; no number, citation or claim changes.

### 4.1 Measuring the star · `04_measured_benchmark.tex`, lines 125-149 · proposed by Opus, Fable, ASTRA

Starts: "Thirdly, the far wings are noisy.". Replaces entries: measured-125, measured-129, measured-130, measured-134, measured-141, measured-145, measured-146.

```latex
Thirdly, the far wings of the difference are noisy. The subtraction removes
the sky, so the image shows the light of the star far from the traces, where
it is fainter than the sky (Figure~\ref{fig:4476-profiles}). The first
exposure, however, has only ten integrations. I estimate the uncertainty of
each pixel by combining the pipeline's error estimates for the two exposures.
These estimates agree with the actual scatter between neighbouring pixels to
within 10\%. Dividing each pixel's count rate by its uncertainty gives a
signal-to-noise ratio of 112 to 675 in the cores of the traces, 10 to 73 at 20
to 40 rows from them, and only 2 to 3 at 40 to 200 rows from order~1 in the
red. Injected as it is, this noise would become a fixed pattern in the star.

The shape of the wings is set by the optics and changes only slowly with
wavelength. Beyond 40 rows from the nearest trace, I therefore replace each
pixel by the median of the pixels at the same distance from the trace in the
61 neighbouring columns, which span about $0.06\,\mu\mathrm{m}$ in order~1.
Where the wings of several orders overlap, the nearest order dominates this
estimate. On average, this far-wing model differs from the measured pixels by
only about 0.16\% at 40 to 100 rows, so the wings change slowly enough across
the 61 columns for the median to stand in for each pixel. The model lowers the
noise per pixel from about 0.10 to about 0.017~DN\,s$^{-1}$, and it also
removes the $1/f$ stripes left in the difference. Between 30 and 40 rows, its
weight rises linearly from zero to one, so that the image passes smoothly from
the data to the model. Nearer the traces, I keep the measured light, with its
noise and stripes. These are fixed in the image of the star, whereas the real,
changing $1/f$ noise of the benchmark comes from the reads of the moved
exposure across the whole strip. The result is the cleaned image of the star,
$S$, a count rate per pixel (Figure~\ref{fig:4476}c).
```
Why: Splits the problem (noisy far wings) from the fix (the far-wing model), and moves the 0.16% check next to the assumption it supports, as Opus and Fable both proposed. It names the model once and applies the seven listed entries; no number changes.

## 7. Possible errors noticed in passing (not wording)

- Section 3.2, lines 33 and 43: "about 90 ppm too deep" against "the transit became about 1 to 2% too deep". For a transit of about 1.5%, 1 to 2% too deep is about 150 to 300 ppm, more than the total 90 ppm bias, and the correction caused only about half of the RMSE increase. Consistent only if the 1 to 2% refers to a limited wavelength range or another quantity; please check the source (Opus).
- Sections 3.2 and 3.3, lines 33 and 88: 125 ppm (count-rate injection) and then 124 ppm (lower estimate on the raw reads) look like the same number to a reader, and the fall from 182 to 124 ppm is not explained in the text (Fable).
- "The reference atmosphere" (Section 3.2 line 32, Section 3.3 line 87, Figure 6 caption line 76) is used but never defined anywhere in the report (Opus, Fable).
- PDF page 26: the two jwst-docs.stsci.edu URLs in the bibliography run past the right margin (ASTRA). Confirmed on a scratch compile: overfull boxes of 57.5 pt and 79.3 pt, removed by loading xurl (entry pre-xurl).
- Section 3.4, line 110: "Both fitted depths should be zero. Instead, they differed" jumps from "each should be zero" to "they differ"; the test is their agreement (Opus; entry 03-110).
- Paper 1, line 41: "held back until NOVA is fixed" reads as "until NOVA is repaired", whereas the meaning is "until NOVA stops changing" (Opus, Fable; entry 05-41).
- Gantt chart, line 164: "Thesis integration" clashes with "integration" as a detector exposure, and "Instrument and geometry extensions" (line 154) does not obviously cover secondary eclipses (Opus).
- Lines 175-176: a stray comma before the citation prints '(Figure 2), (Albert et al., 2023; Louie et al., 2025), at about 2.15 µm'. All three reviewers flagged it, and intro-A-175 fixes it.
- Line 190 says 'a single constant level', whereas line 345 says 'a single scale factor for the background' (the transitspectroscopy reduction). If these are meant to be the same alternative, the wording differs. If they are different, a reader may confuse them (Opus; see the question).
- The HST sodium detection in HD 209458 b (Charbonneau et al. 2002) is told twice, at lines 60-62 and 103-104. This is a visible repetition, not a factual error (Opus; see intro-A-103).
- Line 201 says the HST and Spitzer spectrum 'could not constrain' the water abundance, and line 215 says the SOSS data 'tightened the constraint' compared with those data. A careful reader may ask what constraint was tightened. If Louie et al. (2025) describe the HST/Spitzer result as weak or model-dependent, the wording at line 201 could say so. I noticed this during the merge; no reviewer raised it, and no wording change is proposed.
- Figure 3a draws six groups (G1-G6), but line 256 says that each WASP-17 b integration had eight groups (and Section 4 gives five reads for programme 4476). As a sketch this is not wrong, but the caption does not say it is schematic; adding "schematic" to the caption, or drawing eight points, would remove the question. Raised by Opus.
- Line 304 implies that transitspectroscopy applied no flat field, since only Ahsoka and supreme-SPOON are named, and archive count-rate files are not flat-fielded. Worth checking against Louie et al. (2025); see the question. Raised by Opus.
- Opus's proposed Figure 3a label, "rate fitted from / unaffected differences", would run past the frame of panel (a) into panel (b): at the figure's \scriptsize font it measures about 79 pt against about 59 pt of space. I found this while merging (pdflatex width check in a scratch file); see intro-B-fig3-label for a label that fits.
- 02:52-53 points to Section 2.4 for 'the 51 reddest columns of order 1', but 2.4 gives only the 2.758 um cut and never the number 51, so the reader cannot match the two (Opus).
- 02:48 'Within one detector column, the pixels of a trace see nearly the same wavelength' and 02:99 'Each column records light from a range of wavelengths' read as a contradiction until 02:108-109 ('In this calibration, all pixels of a column see the same wavelengths'). Both are true, and a few words could link them (Opus).
- 02:7-8 says the fit estimates 'the brightness of the star in each column', but the model has one brightness per group (order and column). The difference is minor, since groups are defined only later (Opus).
- The same letter is used for two symbols within a page: b and b_oc, a/R_star and a_oc, l_p and l_o, w_k and w_tp, s_lambda and s_p. N_p has a pixel index but one value per order (Opus; see questions).
- Eq. 8 ends with a comma before a new sentence (fixed by nova-28). At 02:203-205, 'How well ..., and how much ..., has not yet been tested' has a plural subject with a singular verb (fixed by nova-24) (Opus, Fable).
- Figure order: the text cites Figure 8 (fig:4476, line 48) before Figure 7 (fig:w17-gaia, line 76); main.aux confirms this numbering. The fix is measured-111.
- Line 47: "field sources do not cancel, because they moved with the telescope" is physically wrong if read literally. Field sources are fixed on the sky, and only their positions on the detector changed (measured-47).
- Lines 100-102: "seven of the nine predicted images" at the best position, then "the eight pairs found this way". As written, the sliding search did not find eight pairs (see questions). Opus reports that both numbers match the source file.
- The captions of Figures 8 and 9 refer to a correction of the cleaned image "for the sky" that the text does not describe (see questions).
- Line 269: "the real exposure with the star at its usual position" means the first exposure, whereas "the real exposure" at lines 227 and 233 means the moved exposure (measured-267).
- Lines 210 and 333 may disagree on whether the injected limb darkening has already been chosen (see questions).
- Labels inside the figure graphics do not match the text, as reported by Opus and not checked in the PDF here. Figure 8 panel titles say "Star at the normal position" and "Star moved 1,026 rows away" (text: "usual position", "lower"). The Figure 9 legend says "normal exposure", "cleaned source" and "cleaned source, far-wing model", and Figure 10 says "normal exposure N" (text: "usual position", "cleaned image of the star"). These need the figure scripts, not the .tex.

## 8. Proposals we decided against

- **Fable**, sections/03_benchmark.tex:17-18 (3.1): "A measured image of the star avoids this particular risk." -> "A measured image of the star avoids this risk." (item 41) *Why not:* "Particular" is a scope word: it says the measured image avoids only this risk, and Section 4.4 lists others. Cutting it narrows the hedge.
- **ASTRA**, sections/05_discussion_plan.tex:14 (5.1): "The price is a different star, field and readout." -> "This measurement uses a different star, field and readout." (item 50) *Why not:* Loses the trade-off that "the price" states (the separate measurement costs a different star, field and readout); "the price is" is plain English, not a confusing metaphor.
- **Fable**, sections/03_benchmark.tex:42-43 (3.2, part of 3B): "... removed it from the whole column, so the transit became about 1 to 2\% too deep." -> "... removed it from the whole column. The transit became about 1 to 2\% too deep." *Why not:* Removes the "so" that states the cause. A "This made the transit ..." repair would put two different "this"s in a row before "To confirm this". The 37-word sentence reads in one pass as it is, so rewrite R1 keeps it.
- **ASTRA**, sections/03_benchmark.tex:107-108 (3.4, part of P3): "the box dims during the transit by the same fraction" -> "they should dim by the same fraction during transit"; "the box dims less" -> "the box should dim less"; "To check how reliable this comparison is" -> "To check the reliability of this comparison" *Why not:* "Should" turns the stated relation into an expectation, "during transit" drops the article used everywhere else, and "the reliability of" is stiffer than Davide's wording. ASTRA's other P3 changes are kept in entry 03-107 and rewrite R3.
- **Opus**, sections/03_benchmark.tex:66-67 (3.3, part of his rewrite S3 L58-70): "The lower estimate also leaves the faint light beyond 80 pixels undimmed." -> "It also leaves ..." *Why not:* With the three injections now numbered, naming "the lower estimate" again helps the reader before "Like the lower estimate" two sentences later; nothing needs fixing.
- **Fable**, sections/01_introduction.tex:490 (part of Fable item 9): '$3$-$5\,\mu\mathrm{m}$' -> '3 to $5\,\mu\mathrm{m}$' *Why not:* Line 490 is in Section 1.4, outside this part (lines 1-229). The same range convention applies there and should be handled in the intro-B merge.
- **Opus**, 01_introduction.tex:608 (inside Opus's rewrite of lines 601-610): "That study could not determine" -> "It could not determine" *Why not:* "That study" is clearer straight after a sentence that names the commissioning study, and no other reviewer proposed the change.
- **Opus**, 01_introduction.tex:370-384: Paragraph rewrite of lines 370-384 *Why not:* It only combines intro-B-372 and intro-B-378, which are kept as entries, so a separate rewrite would add nothing.
- **Opus**, 01_introduction.tex:601-610: Paragraph rewrite of lines 601-610 *Why not:* It only combines intro-B-601, intro-B-609 and "That study" -> "It" (dropped above). The first two are kept as entries.
- **Opus**, 01_introduction.tex:419-421 (inside Opus's rewrite of lines 417-428): Merge "Because the two orders are copies of the same stellar spectrum, one spectrum has to explain both." and "ATOCA can therefore separate ..." into one sentence joined by "so" *Why not:* The two short sentences read well and keep the causal step visible, and Fable kept them separate. Rewrite intro-B-R1 keeps the other changes from Opus's rewrite.
- **Opus**, 02:130 (nova-128, second half): 'this calibration' -> 'the PASTASOSS calibration' *Why not:* It could narrow the referent from K as a whole to PASTASOSS alone, so it was moved to the questions for Davide.
- **ASTRA**, 02:201 (P2): 'The maps are made orthonormal over these off-trace pixels' *Why not:* After the move, 'these pixels' directly follows the sentence that defines them, so the extra word is no longer needed.
- **ASTRA**, 02:23 (P1): 'it first subtracts the median out-of-transit image' *Why not:* 'First' conflicts with the scaled background model, which is subtracted 'beforehand'. The rest of ASTRA's split is used in nova-03.
- **Opus**, 02:14 (nova-14): 'part by part' *Why not:* Filler. The rest of the sentence is kept in nova-02.
- **Opus**, 04:27 (4.1, the difference paragraph), item measured-27: "whatever is the same at the same pixels cancels: the zodiacal background," -> "everything that is the same at the same pixels cancels. This includes the zodiacal background," *Why not:* The colon introduces a two-item list, which is a normal use, not a reveal. "This includes" would make the full list of what cancels sound like examples, a small change of meaning.
- **ASTRA**, 04:230-238 (4.2), paragraph replacement P4 (item 43): Whole-paragraph replacement of the copy-without-the-transit paragraph. *Why not:* Its main gain, splitting the 40-word sentence, is kept in measured-233, where ASTRA's two sentences are listed as an alternative, and its "data set" is in measured-237. The rest is not adopted. "Both cases share" calls the copy without the transit a case. "I run a pipeline on both cases and subtract its results at each step to show the transit" drops the "therefore" that ties the shared photons to what the subtraction shows. "Is made by removing photons from this copy" adds words without gain. With the other changes made as entries, the paragraph needs no rewrite.
- **ASTRA**, 04:333 (4.4), item 48: "In its spectral fit, exoTEDRF uses fixed coefficients from a 7,000~K model. NOVA, as currently set up, keeps its WASP-17 reference and allows deviations from it. I still need to give NOVA a reference suited to this star." *Why not:* It removes "In their spectral fits" and the "whereas" contrast from NOVA's half, so NOVA's reference no longer reads as limited to the spectral fit. This is Davide's own limb-darkening wording, and that scope matters there. The semicolon fix is in measured-333.

## 9. Notes from the merge on consistency across sections

- Unit of count rate: use DN\,s$^{-1}$ throughout. Sections 3 and 4 already use it three times (03:114, 04:37, 04:140); only Section 2 (02:88-89, "DN/s") would change. ASTRA (item 26) chose DN\,s$^{-1}$, Fable prefers DN/s everywhere, Opus asked for one form without choosing.
- "whilst", not "while": Sections 1 and 2 use "whilst" nine times and "while" never; change 05:58 and 05:62 (entries 05-58b, 05-62) and 04:305 in Section 4. ASTRA kept "while"; Opus and Fable both proposed "whilst", which is also in the style rules.
- "The ranking ... reversed" (abstract, Section 5.1): use "ranking" in Section 3.3 too, instead of "the order reversed" (entry 03-88).
- "Which part of the observed/recorded light belongs to the star": the Introduction (line 603) has "which part of"; change Section 3.1 (entry 03-13), and the abstract only if Davide reopens it (entry 00-16). Section 5.1's "which light belongs to the star" is idiomatic and can stay.
- Lists as "A, B and C" with no serial comma: 03:11 (entry 03-11) and 06:3 (entry 06-3) are the only exceptions in this part.
- "Fixed" only in the sense "no longer changed" (Paper 2, line 75); Paper 1 line 41 becomes "until the improvements to NOVA are complete" (entry 05-41).
- "The reference atmosphere": introduce it once where it first appears (Section 3.2, entry 03-32) and keep exactly that name in Section 3.3 and the Figure 6 caption.
- "The lower estimate" / "the upper estimate" (Davide's terms) are kept everywhere; rewrite R2 only adds the ordinals "In the first," and "The third," so the three announced injections can be counted.
- "The moved exposure" (abstract and captions): Section 4 should use it in the body too, and name it where the exposure is introduced (Opus measured-20, Fable item 52, in another part), so the abstract's term is defined in the text.
- "Deeper at every wavelength, most in the red": the abstract's wording; Section 5.1 should use the same phrase (entry 05-20).
- Section titles in title case, including the unnumbered "Use of Generative AI" (entry 06-1).
- Abstract (approved) says "repeated transits and stellar variability", while Section 5 and the Gantt chart say "repeated visits"; close but not identical. Noted only (Opus).
- Abstract (approved) uses "the SOSS strip" without defining it; Section 1.6 and Section 4 define it. Acceptable in an abstract (Opus, noted only).
- Repetitions noted by Opus with no change proposed: "where NOVA's spectrum of WASP-17 b differs most" appears twice in the Paper 2 paragraph and again in Sections 2.9 and 5.1; "rests on a single/one star" appears twice in Section 4.4 and in Paper 1; secondary eclipses are defined in Section 1.1 and again in Paper 5 (a harmless reminder).
- Number ranges: write 'X to $Y\,\mu\mathrm{m}$' in prose, as Sections 2-4 do. This part has five hyphen ranges (lines 109, 110, 123, 135 and 197), and Section 1.4 has one more (line 490). Opus mentioned an en dash ('--') as the other option; Opus and Fable both recommend 'to'.
- 'whilst' versus 'while': keep 'whilst' throughout. The Introduction uses it seven times and Section 2 once, while 04:305, 05:58 and 05:62 use 'while'. Fable recommends 'whilst', and Opus only flagged the mix. intro-A-167 removes one 'whilst' because it is stacked with 'However', not as a change of convention.
- Use 'effective radius' for R_p(λ) everywhere: in the text (lines 35-36), the Figure 1 caption (line 48, intro-A-48) and the Figure 1 label (transmission_spectroscopy_schematic.tex line 87, intro-A-48fig).
- Write 'order 1', not 'the first order' (line 136, intro-A-136).
- 'Reduction' versus 'pipeline': Sections 3-5 use 'pipeline' for the software and 'reduction' for a published analysis, but line 208 defines a reduction as software and 'pipeline' is never defined (see the question). The choice also decides between 'was' and 'used' in intro-A-209.
- 'Visit' is used from the Figure 2 caption onward and is never defined (see the question).
- Flat field: keep the definition at line 140 ('the map of each pixel's sensitivity') and shorten the second definition at lines 304-306 to a plain use (Opus; that change belongs to intro-B).
- The point that leftover background is not modelled in the transit fit is made at line 7 and again at lines 365, 370-371, 378, 480-482 and 522-526. Keep the full statement in the opening and use brief back-references later (Opus; the later instances are intro-B items).
- Firstly/Secondly: the opening (line 7) changes to 'The first is ... The second is ...' because those sentences name error points, not processing steps. The 'Firstly ... Secondly ... Finally' sequence for the three difficulties of SOSS (lines 168-174) stays as Ben's connectives.
- Wavelength ranges: write "3 to $5\,\mu\mathrm{m}$" everywhere, as Sections 2 to 5 already do. The Introduction's "$a$-$b$" forms (lines 109, 110, 123, 135, 197 and 490) print as hyphens. Recommended: "to" (Opus, Fable). An en dash would be the typographic alternative, but "to" matches the rest of the report.
- "whilst" vs "while": the Introduction and Section 2 use only "whilst", whereas Section 4 line 305 and Section 5 lines 58 and 62 use "while". Recommended: "whilst" throughout (Fable; it is also in the style rules' list of connectives).
- "data set" vs "dataset": Section 2 uses "data set" seven times, whereas intro line 581 and Section 4 line 237 use "dataset". Recommended: "data set" (Fable; noted by Opus).
- The band of pixels summed in extraction should have one name, "extraction box" (Sections 3 and 4), not "extraction aperture" or "aperture" (intro 609 and 613). Section 2 uses "apertures" for NOVA's own fitted pixel regions (intro-B-609, intro-B-613).
- The image built from programme 4476 should be "the cleaned image of the star" (abstract, Section 4), not "clean image" or "constructed image" (intro 619 and 622). Its outer region should be "far wings" (Section 4), not "outer wings" (intro 619). Section 4 line 34 ("not yet a clean image of the star") is descriptive and can stay.
- "raw reads" (abstract; intro 590 and 620; Sections 3 and 4), not "detector reads" (objective 2, intro 644).
- "the moved exposure": intro lines 620-621 describe it ("the exposure in which the star was moved off the strip"), and the abstract and the Section 4 captions use the name. If Section 4 gives the name where the exposure is first described (Opus measured-20, Fable 52), the Introduction's description can stay. No reviewer proposed a change in the Introduction.
- Geometry: the report says "transit geometry" (intro 475, where the term is defined), "orbital geometry" (Section 2 lines 12 and 273) and "white-light geometry" (Section 2.8 heading). I recommend "transit geometry", the defined term, unless the Section 2 merge decides otherwise (Opus noted this; no replacement was proposed).
- The background left after subtraction is called "residual background", "background that remains", "remaining background" and "background left". Opus suggests using "residual background" by default after its first use.
- The point that the background is subtracted before the transit fit, so the fit cannot correct it, appears at intro 7, 357-360, 364-365, 370-371, 378-381, 413-415, 424-428, 430-432, 507-508 and 520. Entries intro-B-365, -378, -427 and -507 remove four of these; Opus judges that each of the others does its own job.
- The flat field is defined twice, at intro 140 ("the map of each pixel's sensitivity") and at 304-306 ("a reference image of how sensitive each pixel is relative to the others"). The second could be shortened to a reminder (Opus; no replacement proposed).
- "Where the two orders overlap, their light must be separated" appears at intro 170-171 and again at 404-405 (Opus).
- Ahsoka's use of Eureka! is stated at intro 352 and 518, and its use of the supreme-SPOON bad-pixel step at 310 and 515 (Opus).
- The roadmap at intro 658-659 repeats the last sentence of the Section 2 opener almost word for word (Opus).
- "For a real planet, the true spectrum is unknown" opens Section 1.5 (line 487), and Section 3 opens with almost the same sentence. Section 3 could refer back to 1.5 instead (Opus).
- "without knowing the injected truth" (Sections 3 and 4): intro 592 is brought into line by intro-B-592.
- Count-rate unit: write DN\,s$^{-1}$ everywhere, as 03:114, 04:37 and 04:140 already do. Only 02:88-89 changes (nova-09; Opus, ASTRA). Fable prefers DN/s, which would need three edits instead of one.
- Use 'WASP-17~b visit' for the observation and 'WASP-17' only for the star, as Section 4 does. This changes 02:202 and 02:218 (nova-24, nova-26), and 'the real visit' at 02:210 becomes 'the real WASP-17~b visit' (nova-25).
- Write 'data set' as two words, as Section 2 does seven times: change 01:581 'datasets' and 04:237 'dataset' (Fable 66, Opus).
- 'learned' (01:660, 02:207) against 'learnt' (05:76): use one form. 'learned' needs one edit (05:76) and is also standard British usage (Opus).
- Use 'whilst', not 'while'. Section 2 uses only 'whilst' (caption, line 43), but 04:305, 05:58 and 05:62 use 'while' (Fable 70).
- Write ranges with 'to' or 'between ... and', as Section 2 does throughout. The Introduction's hyphenated ranges ($0.6$-$2.8\,\mu\mathrm{m}$) print as hyphens (Fable 9, Opus).
- 'deeper at every wavelength' is the wording of the approved abstract and of 05:19-20; nova-40 replaces 'deeper throughout' at 02:316 with it.
- Transit factor: 04:195 defines r_p(t) as 'the fraction of the star's light that remains', and nova-07 and nova-11 use the same words for T-bar.
- Benchmark status: the abstract and Sections 1, 4 and 5 say 'I am building' and 'is designed to measure'; nova-42 brings 02:325 into line.
- Within Section 2, use 'noise factor' for both N_p and s_p (nova-01).
- If Section 2.6 gets \label{sec:fit}, point 03:66 ('held in place by the same off-trace pixels') there instead of to sec:continuum (Opus; see questions).
- 'The real data cannot ...' appears at 02:324, in the title of 3.4 and at 03:112. Each use is fine on its own, but avoid adding a fourth (Opus).
- The exoTEDRF 1/f correction is described at 01:287-301, 02:22-28 and 03:34-39. Section 3 already points back to 2.1. No change is proposed, because Section 3 was agreed today (Opus).
- The moved exposure: define it at 04:20 (measured-20) and use it for every later mention of the second exposure in Section 4, except "the second" at 04:25, which pairs with "the first". The abstract's "the moved exposure's raw reads" then matches. Keep "the real exposure" only where it contrasts real with injected light (04:227, 04:233), never for the first exposure (04:269, measured-267).
- Count-rate unit: recommend DN\,s$^{-1}$ throughout. 03:114, 04:37 and 04:140 already use it; change 02:88-89 (ASTRA item 26). Fable prefers DN/s everywhere.
- "whilst" rather than "while" as the contrast connective: change 04:305, 05:58 and 05:62 (Sections 1 and 2 already use "whilst"; the style rules list it).
- "data set" rather than "dataset": change 04:237 and 01:581 (Section 2 uses "data set" seven times).
- "Moved off the strip" (abstract, 01:615, 01:621) should also be used at 04:5 (measured-5).
- "Compact sources" as the single name for the undispersed field objects (04:68 "compact spots", 04:48 and 04:65 "compact blobs"; Figure 7 uses "compact sources"). "Bright/dark spots" stays for their imprints in the difference.
- "Reads" rather than "groups" for the reads of a ramp within Section 4 (04:17), since Section 2 uses "group" for a set of pixels in one order and column.
- "Shifted" for changes of position (the A Delta_i offset at 04:86, the 10 rows in the Figure 8 caption), keeping "moved" for the moved exposure and the moved star.
- "Far-wing model" as the one name for the median replacement of the far wings (04:141, Figure 9 caption).
- "Cleaned image of the star" (abstract, Section 4) against "a clean image of the star" at 01:619: use "cleaned" (04:34's "not yet a clean image" is fine, because it means the target state).
- "Rests on one/a single star" appears at 04:297, 04:336 and in Section 5 (Paper 1). Keep 04:297 only in Section 4 (measured-335), and consider letting Paper 1 refer back to Section 4.4 for the repeat of programme 4476.
- Labels inside the figure graphics should use the text's terms ("usual position", "moved exposure", "cleaned image of the star"); this needs the figure scripts.
- Subsection numbering: Limitations is Section 4.4 (main.aux). Fable's Q6 refers to it as 4.5.