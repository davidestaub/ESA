# Fable: wording review of the whole ESA at b50eb10

Date: 9 October 2026, 22:05 UTC. Written before reading ASTRA's or Opus's reviews.

Scope: all seven section files at commit b50eb10 (00 3e4f9d1a, 01 aeb7ff35, 02 cbbea3c0, 03 25a55550, 04 9f6f963a, 05 7efc7cc8, 06 1e97cbbc), read sentence by sentence, including captions, the research question, the objectives and the Gantt labels. `proposals/style_check.py` was run on every section, and a script listed every sentence over 35 words and counted connectives and repeated terms. pdftoppm is not installed on this Mac, so the LaTeX items come from the source, not from the rendered PDF.

Rules followed: no replacement changes a fact, number, condition, scope or citation. Where a better sentence would change the meaning, it is a question in Part 4. Davide's earlier decisions (the limb-darkening wording, the bin widths, the NOVA reference sentence, the dropped sentences) are not reopened; one item (76) only replaces a semicolon in a sentence Davide wrote, leaving his words intact.

Measurements from `style_check.py` (median sentence length / share over 35 words / commas per 1000 / "which" per 1000 / banned words):

| Section | median | >35 | commas | which | banned |
|---|---|---|---|---|---|
| 00 | 19 | 0% | 62 | 6.2 | none |
| 01 | 19 | 3% | 57 | 3.4 | "crucially" |
| 02 | 21 | 10% | 67 | 4.5 | none |
| 03 | 23 | 15% | 61 | 6.3 | "this matters" (a real use, item 88 covers the Section 5 one) |
| 04 | 24 | 13% | 67 | 5.0 | none |
| 05 | 23.5 | 11% | 61 | 8.7 | "this matters" |

All sections meet the sentence-length targets. The remaining long sentences are listed below with splits.

---

## Part 1. Items by file and line

Format: `file:line`; current text (short); replacement (LaTeX-ready); reason; category.

### 00_abstract.tex

No changes. It was agreed by all three and approved by Davide this evening.

### 01_introduction.tex

1. `01:7` "Firstly, the background light is subtracted, and any background that remains is not modelled when the transit is fitted." → "Firstly, the background is subtracted before the transit is fitted, and any background that remains is left out of the fit." The current sentence reads as if subtracting were the error; the error is what the fit leaves out. clarity.

2. `01:10–12` "It fits the transit to the detector pixels themselves, and in the same fit it fits whatever background the earlier subtraction has left behind." → "It fits the transit to the detector pixels themselves, together with whatever background the earlier subtraction has left behind." "fits ... it fits" in one sentence. repetition.

3. `01:25` "The atmosphere helps to distinguish between these possible compositions, and its composition can also hint at where and how the planet formed" → "The atmosphere helps to distinguish between these possibilities, and what it is made of can also hint at where and how the planet formed". "compositions ... composition". repetition.

4. `01:25` "Some planets are also observed to lose gas from their upper atmosphere \citep{VidalMadjarEtAl2003}." → cut. Nothing later uses it, and the paragraph is about why atmospheres are studied. cut (Davide's call, see Part 4).

5. `01:27` "that is, passes in front of its star, because part of the starlight then passes through the atmosphere" → "that is, crosses the face of its star, because part of the starlight then passes through the atmosphere". "passes ... passes". repetition.

6. `01:28` "If the stellar disc were uniformly bright (in reality it dims towards its edge, an effect called limb darkening), the depth of a transit would be approximately" → "In reality the stellar disc dims towards its edge, an effect called limb darkening. If it were uniformly bright, the depth of a transit would be approximately". A 58-word sentence with a parenthesis inside the condition. clarity.

7. `01:58–60` "A class of planets that satisfies these conditions is the so-called hot Jupiters, gas giants that orbit close to their stars" → "Hot Jupiters, gas giants that orbit close to their stars, satisfy these conditions". "So-called" and "a class of planets that" delay the subject. clarity.

8. `01:71` "I start with transmission because a transit has a well-defined geometry that repeats with every orbit, making it a convenient test case of how the processing of the data affects the recovered spectrum." → "I start with transmission spectroscopy because a transit has a well-defined geometry that repeats with every orbit. This makes it a convenient case for testing how the processing of the data affects the recovered spectrum." "Transmission" alone names the mechanism, not the technique; "test case of how" is not idiomatic. grammar.

9. `01:109, 110, 123, 135, 197, 490` "$1.1$-$1.7\,\mu\mathrm{m}$", "$0.3$-$5\,\mu\mathrm{m}$", "$0.6$-$2.8\,\mu\mathrm{m}$" (twice), "$0.3$-$5\,\mu\mathrm{m}$", "$3$-$5\,\mu\mathrm{m}$" → "1.1 to $1.7\,\mu\mathrm{m}$", "0.3 to $5\,\mu\mathrm{m}$", "0.6 to $2.8\,\mu\mathrm{m}$", "0.3 to $5\,\mu\mathrm{m}$", "3 to $5\,\mu\mathrm{m}$". A hyphen between numbers prints as a hyphen, not a range dash, and Sections 2 to 5 write every range with "to". LaTeX, consistency.

10. `01:133` "An optical element called GR700XD, a grism (a prism carrying a diffraction grating) combined with a prism, spreads the light into several copies of the spectrum, called orders \citep{AlbertEtAl2023}." → "An optical element called GR700XD spreads the light into several copies of the spectrum, called orders \citep{AlbertEtAl2023}. It is a grism, a prism that carries a diffraction grating, combined with a second prism." "A grism (a prism ...) combined with a prism" makes the reader count prisms, and the verb comes 20 words after the subject. clarity.

11. `01:139–140` "A weak cylindrical lens spreads the light over about 23 detector rows, so that bright stars can be observed without saturating the pixels, and so that small pointing jitter and errors in the flat field, the map of each pixel's sensitivity, matter less" → "A weak cylindrical lens spreads the light over about 23 detector rows. Bright stars can then be observed without saturating the pixels, and small pointing jitter and errors in the flat field, the map of each pixel's sensitivity, matter less". 44 words with two "so that" clauses. clarity.

12. `01:172` "SOSS is slitless out of necessity, not by choice. A slit must sit where the optics form an image of the sky before the light is dispersed, and when SOSS was developed, NIRISS had no optics that form such an image \citep{AlbertEtAl2023}." → "SOSS has no slit because a slit must sit where the optics form an image of the sky before the light is dispersed, and when SOSS was developed, NIRISS had no optics that form such an image \citep{AlbertEtAl2023}." "Out of necessity, not by choice" is the contrast reflex of the style rules, and the next sentence already gives the reason. AI tell.

13. `01:176` "near detector column 700 (Figure~\ref{fig:soss-detector-orders}), \citep{AlbertEtAl2023,LouieEtAl2025}, at about $2.15\,\mu\mathrm{m}$ in order 1 \citep{AlbertEtAl2023}." → "near detector column 700, at about $2.15\,\mu\mathrm{m}$ in order 1 (Figure~\ref{fig:soss-detector-orders}) \citep{AlbertEtAl2023,LouieEtAl2025}." The comma before \citep prints as "(Figure 2), (Albert et al. 2023; Louie et al. 2025), at", and Albert is cited twice in one sentence. LaTeX.

14. `01:195` "I focus on a hot Jupiter, WASP-17~b." → "The planet I focus on is the hot Jupiter WASP-17~b." The sentence follows the WASP-39~b example with no link; putting the subject first marks the turn. flow.

15. `01:240` (caption) "A cosmic ray adds a jump, which the several groups make visible, so the count rate can be fitted from the unaffected differences between reads." → "A cosmic ray adds a jump. With several groups the jump can be seen, and the count rate is fitted from the unaffected differences between reads." "Which the several groups make visible" is hard to parse. clarity.

16. `01:266` "They also remove slow drifts in the readings. These drifts are measured with reference pixels, pixels that receive no light." → "They also remove slow drifts in the readings, measured with reference pixels that receive no light." Two clipped sentences for one idea. flow.

17. `01:278–279` "In SOSS, the pixels of each detector column are read one after another, so the offsets appear as stripes along the columns" → "In SOSS, the readout runs down each detector column, so the offsets appear as stripes along the columns". "One after another" also closes the previous sentence. repetition.

18. `01:304` "In Ahsoka and supreme-SPOON, the images are then flat-field corrected with the JWST pipeline." → "In Ahsoka and supreme-SPOON, the images are first flat-field corrected with the JWST pipeline." "Then" has nothing before it in this paragraph. clarity.

19. `01:378–381` "In all three reductions of WASP-17~b, the background was subtracted before the light curves were fitted, and the transit fit held the subtracted background fixed \citep{LouieEtAl2025}. The transit fit therefore could not correct an error in the subtraction." → "In all three reductions of WASP-17~b the transit fit held the subtracted background fixed (Section~\ref{sec:detector-to-spectrum}), so it could not correct an error in the subtraction." The same point is made at 01:365, here and at 01:508. repetition.

20. `01:417–421` "ATOCA models every pixel as the sum of the light of both orders. ... ATOCA can therefore separate the two orders during the extraction \citep{DarveauBernierEtAl2022}. ATOCA needs the profile of each order across the detector, and ..." → "It models every pixel as the sum of the light of both orders. ... It can therefore separate the two orders during the extraction \citep{DarveauBernierEtAl2022}. It needs the profile of each order across the detector, and ...". ATOCA opens four sentences in a row. repetition.

21. `01:468–469` "and could bias the NOVA spectrum." → "and could bias the spectrum." The phrase already ends the paragraph's first sentence. repetition.

22. `01:497–499` "None found evidence of an atmosphere, but two showed weak candidate absorption features at different wavelengths, which retrievals assigned to different gases, and the authors concluded that the features were not real astrophysical signals." → "None found evidence of an atmosphere. Two, however, showed weak candidate absorption features at different wavelengths, which retrievals assigned to different gases, and the authors concluded that the features were not real." 44 words; "real astrophysical signals" says "real" twice over. clarity.

23. `01:507–508` "Each subtracted the background from the images and extracted a spectrum before it fitted the transit." → cut. It restates the definition of extraction-first given in the section cited in the previous sentence. repetition.

24. `01:522` "Crucially, a good fit to the extracted light curves does not show that the background was subtracted correctly." → "A good fit to the extracted light curves does not show that the background was subtracted correctly." "Crucially" is on the banned list. AI tell.

25. `01:525` "The light curve, however, still has the shape of a transit, so it can still be fitted well." → "The light curve, however, keeps the shape of a transit, so it can still be fitted well." "still ... still". repetition.

26. `01:530` "Historically, known test signals have been supplied in two ways." → "Known test signals have been supplied in two ways." The word adds nothing; both ways are current. cut.

27. `01:609` "the extraction aperture, the band of pixels that is combined into the spectrum, also called the extraction box" → "the extraction aperture or box, the band of pixels that is combined into the spectrum". Two appositions in a row. clarity.

28. `01:633–636` (research question) "and does fitting the transit and the background together, directly on the pixels, reduce the biases that fitting the transit without a background term, and extracting a spectrum first, can cause?" → "and does fitting the transit and the background together, directly on the pixels, reduce the biases caused by extracting a spectrum first and fitting the transit without a background term?" The ending stacks two gerund subjects in front of "can cause" and has to be read twice; the content is unchanged. clarity.

### 02_nova.tex

29. `02:23–27` "To estimate it, the step subtracts from the group the median out-of-transit image, scaled by a light curve measured from the data, and takes the median of what is left in each column outside the trace cores, leaving out field stars found in a separate exposure through the F277W filter. It then subtracts this column offset from the original group." → "To estimate it, the step subtracts from the group the median out-of-transit image, scaled by a light curve measured from the data. Outside the trace cores, and leaving out field stars found in a separate exposure through the F277W filter, the median of what is left in each column is the column offset. The step subtracts this offset from the original group." 50 words carrying three operations. clarity.

30. `02:40` (caption) "(a sketch, not data); the fitted apertures" → "(a sketch, not data). The fitted apertures". Semicolon. grammar.

31. `02:90` "The measured $A_{pg}$, and so $q^\star_{pg}$, is therefore noisy." → "The measured $A_{pg}$, and so $q^\star_{pg}$, is noisy." "Therefore" in two consecutive sentences. repetition.

32. `02:125–127` "Below $2\,\mu\mathrm{m}$ the bins are about $0.01\,\mu\mathrm{m}$ wide and above it $0.038\,\mu\mathrm{m}$, wider in the red, where the signal-to-noise ratio is lower." → "Below $2\,\mu\mathrm{m}$ the bins are about $0.01\,\mu\mathrm{m}$ wide, and above it $0.038\,\mu\mathrm{m}$, where the signal-to-noise ratio is lower." "Wider in the red" repeats the numbers just given; the widths stay. cut.

33. `02:138` "where $\bar D$ is the overall, achromatic depth" → "where $\bar D$ is the overall depth, the same at every wavelength". The one technical word in a plain sentence. clarity (judgement; "achromatic" is standard and may stay).

34. `02:186` "$\gamma_t$ is the geometric mean of the two orders' curvature factors, normalised to one out of transit." → "The factor $\gamma_t$ is the geometric mean of the two orders' curvature factors, normalised to one out of transit." A sentence should not open with a symbol. LaTeX.

35. `02:200–201` Move the two field-star sentences ("Field stars are also left out of the $1/f$ correction ... needed for both the benchmark and the WASP-17~b visit.") to the end of the paragraph, after "has not yet been tested." At present they separate "The 244,657 off-trace pixels ..." from "The maps are made orthonormal over these pixels", so "these pixels" loses its antecedent. flow. Full text in Part 3A.

36. `02:200` "The 244,657 off-trace pixels, away from the traces, field stars and bad pixels, are assumed" → "The 244,657 off-trace pixels, which lie away from the traces, field stars and bad pixels, are assumed". "Off-trace ... away from the traces" stutters without "which lie". grammar.

37. `02:222–224` "and inflates single pixels that are noisier than the rest of their order" → "and inflates the uncertainty of single pixels that are noisier than the rest of their order". A factor inflates an uncertainty, not a pixel. grammar.

38. `02:237` The objective equation ends "\right]," and the next line begins a new sentence ("The first term compares ..."). → end the equation "\right]." It prints as "], The first term". LaTeX.

39. `02:292–293` "I plan to estimate the uncertainty from the calibration products and the geometry with an ensemble of simulated observations." → "I plan to estimate the uncertainty that the calibration products and the geometry contribute, with an ensemble of simulated observations." "The uncertainty from ... with" can be read as estimating from the products. clarity.

### 03_benchmark.tex

40. `03:7–9` "An injection test supplies a truth: a known transmission spectrum is added to detector data, and the spectrum that each method recovers is compared with it." → "An injection test supplies one. A known transmission spectrum is added to detector data, and the spectrum that each method recovers is compared with it." Colon, and "a truth" is odd English. grammar.

41. `03:17–18` "A measured image of the star avoids this particular risk." → "A measured image of the star avoids this risk." cut.

42. `03:32–33` "On the same data, NOVA's root-mean-square error for the reference atmosphere then rose from 125 to 182~ppm" → "On the same data, with the one injected atmosphere that I use as a reference throughout this section, NOVA's root-mean-square error then rose from 125 to 182~ppm". "The reference atmosphere" is used here, at 03:87 and in the caption without being introduced. clarity.

43. `03:41–48` Sentence splits in the mechanism paragraph; full text in Part 3B. clarity.

44. `03:63–66` "I made this model by fitting the star's spectrum, with a slow change in time, to the out-of-transit images through ATOCA's model of the detector, together with a smooth background made of four of NOVA's eight background maps and held in place by the same off-trace pixels (Section~\ref{sec:continuum})." → "I made this model by fitting the star's spectrum, with a slow change in time, to the out-of-transit images through ATOCA's model of the detector. The fit included a smooth background made of four of NOVA's eight background maps, held in place by the same off-trace pixels (Section~\ref{sec:continuum})." 49 words. clarity.

45. `03:68` "it also dims this faint light; it changed NOVA's spectrum by about 40~ppm." → "it also dims this faint light. This changed NOVA's spectrum by about 40~ppm." Semicolon. grammar.

46. `03:91–94` "exoTEDRF counts all the light left in its box after background subtraction as starlight, like the upper estimate, whereas ..." → "Like the upper estimate, exoTEDRF counts all the light left in its box after background subtraction as starlight, whereas ...". A sentence should not start with a lower-case name. grammar.

47. `03:107` "the box dims during the transit by the same fraction as the centre; if part of it is background, the box dims less." → "the box dims during the transit by the same fraction as the centre. If part of it is background, the box dims less." A 45-word sentence held by a semicolon. grammar.

48. `03:108` "I repeated it on stretches without a transit: I fitted the same transit shape, at a time when no transit happens, to the box and to the bright centre." → "I repeated it on stretches without a transit. I fitted the same transit shape, at a time when no transit happens, to the box and to the bright centre." Colon. grammar.

49. `03:114` "I also measured how much the faint light outside the traces dims" → "I then measured how much the faint light outside the traces dims". "I also" opens 03:106 as well. repetition.

50. `03:114` "Only this range gives a clear answer: at 1.75 to $2.1\,\mu\mathrm{m}$ the measurement" → "Only this range gives a clear answer. At 1.75 to $2.1\,\mu\mathrm{m}$ the measurement". Colon. grammar.

51. `03:114` "Even where the answer is clear, it depends on how the detector behaves: if the fit allows" → "Even where the answer is clear, it depends on how the detector behaves. If the fit allows". Colon. grammar.

### 04_measured_benchmark.tex

52. `04:20–21` "This second exposure has 150 integrations covering 2.68~h, and it is the one into which I inject the star." → "This second exposure, which I call the moved exposure, has 150 integrations covering 2.68~h, and it is the one into which I inject the star." Then at `04:36, 57, 63, 145, 188, 194` "second exposure" → "moved exposure". The abstract and all three captions say "moved exposure"; the text says "second exposure". One name for one thing. consistency.

53. `04:38–40` "The benchmark keeps this glow, because it is built on the second exposure, so the total light out of transit is right, but the glow does not dim during the transit." → "The benchmark keeps this glow, because it is built on the moved exposure. The total light out of transit is therefore right, but the glow does not dim during the transit." "Because ... so ... but" in one sentence. clarity.

54. `04:42–45` "The full frames show this halo at 700 to 800 rows from the moved star, and with its measured fall-off it can be extrapolated to the strip, so I can correct the image of the star by adding this model of the halo." → "The full frames show this halo at 700 to 800 rows from the moved star. With its measured fall-off, it can be extrapolated to the strip, so I can correct the image of the star by adding this model of the halo." 43 words. clarity.

55. `04:67–69` "Gaia, however, also tells me where the spectra of known stars fall, which a search for compact spots cannot find, even for stars that lie off the strip." → "Gaia, however, also tells me where the spectra of known stars fall, even for stars that lie off the strip, and a search for compact spots cannot find these spectra." "Which" and "even for stars" attach to the wrong words. clarity.

56. `04:75–109` Split the paragraph in three: after "moved by $\mathbf{A}\,\boldsymbol{\Delta}_i$." (04:86) and after "the errors are 1.5 columns and 7.8 rows." (04:105). One 430-word paragraph carries the mapping, the detection recipe and the application to programme 4476. flow.

57. `04:86–90` "To locate the compact sources, I first removed everything that is smooth along the rows, such as the traces and the sky, by subtracting from each row a running median over 51 columns, and removed the $1/f$ stripes by subtracting the median of each column." → "To locate the compact sources, I first removed everything that is smooth along the rows, such as the traces and the sky, by subtracting from each row a running median over 51 columns. I removed the $1/f$ stripes by subtracting the median of each column." 45 words. clarity.

58. `04:92–95` "Many of these detections lie along the traces and are left over from their removal; a source counts as real if" → "Many of these detections lie along the traces and are left over from their removal. A source counts as real if". Semicolon. grammar.

59. `04:105–106` "Programme 4476 cannot provide such a fit: its field is sparse, with 208 Gaia stars" → "Programme 4476 cannot provide such a fit. Its field is sparse, with 208 Gaia stars". Colon. grammar.

60. `04:109` "Because NOVA may later use the same predictions, agreement between the two would not by itself show that the field-star light was separated correctly." → "Because NOVA may later use the same predictions, agreement between the injector and NOVA about the field stars would not by itself show that their light was separated correctly." "The two" has no clear antecedent. clarity.

61. `04:134–138` "The shape of the wings is set by the optics and changes only slowly with wavelength, so beyond 40 rows from the nearest trace I replace each pixel by the median of the pixels at the same distance from the trace in the 61 neighbouring columns, which span about $0.06\,\mu\mathrm{m}$ in order~1." → "The shape of the wings is set by the optics and changes only slowly with wavelength. Beyond 40 rows from the nearest trace, I therefore replace each pixel by the median of the pixels at the same distance from the trace in the 61 neighbouring columns, which span about $0.06\,\mu\mathrm{m}$ in order~1." 53 words. clarity.

62. `04:146–148` "On average, the model differs from the measured pixels by only about 0.16\% at 40 to 100 rows, so the wings change slowly enough for this." → move this sentence to directly after "... which span about $0.06\,\mu\mathrm{m}$ in order~1." and end it "so the wings change slowly enough across these columns for the median to stand in for each pixel." It justifies the 61-column median, not the blending that now precedes it, and "for this" is vague. flow, clarity.

63. `04:220–221` "The detector does not record charge in proportion: as a pixel fills, each additional electron raises the recorded value a little less." → "The detector does not record charge in proportion. As a pixel fills, each additional electron raises the recorded value a little less." Colon. grammar.

64. `04:226–227` "Nothing else is added: the bias, read noise and $1/f$ noise of the real exposure stay as they are." → "Nothing else is added. The bias, read noise and $1/f$ noise of the real exposure stay as they are." Colon reveal. grammar.

65. `04:233–234` "Comparing this with the injected transit shows whether and where the pipeline distorts it." → "Comparing this with the injected transit reveals whether and where the pipeline distorts it." "Shows" in three consecutive sentences. repetition.

66. `04:237` "A single dataset with a transit" → "A single data set with a transit"; and `01:581` "eight real datasets" → "eight real data sets". Section 2 writes "data set" seven times. consistency.

67. `04:244` "Further tests would be needed to isolate the faint light." → "Further tests would then be needed to find out whether the faint light is the cause." "Isolate the faint light" does not say from what. clarity.

68. `04:276–277` "Neither comparison can show that the cleaned image is the true star; that rests on the cleaning described in Section~\ref{sec:measuring-star}." → "Neither comparison can show that the cleaned image is the true star. That rests on the cleaning described in Section~\ref{sec:measuring-star}." Semicolon. grammar.

69. `04:284–289` "To find where an error arises, I also run each pipeline on the copy without the transit and compare the two runs after every step that the pipeline saves, such as the $1/f$ correction or the extraction. Because the two runs differ only by the light that the transit removed, each comparison shows the transit as that step passed it on." → "To find where an error arises, I also run each pipeline on the copy without the transit and compare the two runs after every step that the pipeline saves, such as the $1/f$ correction or the extraction (Section~\ref{sec:injecting-star})." The second sentence repeats 04:233 in substance. repetition.

70. `04:305` "while its $1/f$ noise is similar" → "whilst its $1/f$ noise is similar"; `05:58` and `05:62` "while" → "whilst". The Introduction and Section 2 use "whilst" nine times and "while" never. consistency.

71. `04:315` "It could be added by shifting and stretching the image of the star" → "Such motion could be added by shifting and stretching the image of the star". "It" points back past "this". clarity.

72. `04:320` "the benchmark does not contain this" → "the benchmark does not contain that response". clarity.

73. `04:329–331` "None of the four pipelines, as set up for the benchmark, uses such a prior: each fits the shape of the transit freely." → "None of the four pipelines, as set up for the benchmark, uses such a prior, and each fits the shape of the transit freely." Colon. grammar.

74. `04:333` "keeps its WASP-17 reference and allows deviations from it; I still need to give NOVA a reference suited to this star." → "keeps its WASP-17 reference and allows deviations from it. I still need to give NOVA a reference suited to this star." Semicolon only; Davide's words unchanged. grammar.

75. `04:335–336` "With the existing data, this is as close to a real observation as I can make the benchmark, and it rests on a single star." → "With the existing data, this is as close to a real observation as I can make the benchmark." "Rests on one star" opened the limitations at 04:297. repetition.

76. `03:114, 04:37, 04:140` "DN\,s$^{-1}$" and `02:88–89` "DN/s" → one form throughout; I suggest "DN/s", the plainer one and the first used. consistency.

### 05_discussion_plan.tex

77. `05:8–10` "Every injection test on real SOSS data has to decide which light belongs to the star, stated or not, and its verdict holds only under that decision." → "Every injection test on real SOSS data has to decide, whether it says so or not, which light belongs to the star, and its verdict holds only under that decision." "Stated or not" dangles after "star". clarity.

78. `05:15` "It is designed to measure which kinds of error" → "The benchmark is designed to measure which kinds of error". "It" follows "The price is ...". clarity.

79. `05:21` "An injection test shows how accurately each method recovers a known spectrum, which is the best guide to which real spectrum to trust, and an injector built from the WASP-17~b data alone cannot provide it." → "An injection test shows how accurately each method recovers a known spectrum, and this is the best guide to which real spectrum to trust. An injector built from the WASP-17~b data alone cannot provide such a test." "Which ... which", and an "it" with two candidates. clarity.

80. `05:22–23` "I will then use it to test NOVA and the other pipelines and to improve NOVA, and only then refit WASP-17~b." → "I will then use it to test NOVA and the other pipelines, improve NOVA, and only then refit WASP-17~b." "And ... and ... and". grammar.

81. `05:41` "held back until NOVA is fixed" → "held back until the improvements to NOVA are complete". "Fixed" reads as "repaired". clarity.

82. `05:52–54` "As in Paper~1, I will run NOVA together with those pipelines of each visit's published reductions that are publicly available, and run each of them on the benchmark as well, so that its errors on the same known case can be measured." → "As in Paper~1, I will run NOVA alongside the publicly available pipelines behind each visit's published reductions. I will also run each of them on the benchmark, so that its errors on the same known case can be measured." "Those pipelines of each visit's published reductions that" is a noun pile. clarity.

83. `05:58` "This is in the red range where NOVA's spectrum of WASP-17~b differs most from Ahsoka's" → "This fall lies in the red range where NOVA's spectrum of WASP-17~b differs most from Ahsoka's". "This" has three possible referents. clarity.

84. `05:71–74` "For WASP-80~b, NIRCam has measured methane between 2.4 and $4\,\mu\mathrm{m}$ \citep{BellEtAl2023}, overlapping the red end of SOSS, where NOVA differs most for WASP-17~b, which gives an independent check of NOVA's red end." → "For WASP-80~b, NIRCam has measured methane between 2.4 and $4\,\mu\mathrm{m}$ \citep{BellEtAl2023}. This range overlaps the red end of SOSS, where NOVA differs most for WASP-17~b, and so gives an independent check there." A "which" chain ending in "red end ... red end". clarity.

85. `05:77–79` "Since the errors measured in Paper~1 come from a hotter star, a repeat of programme 4476 on cooler stars would make this comparison firmer." → cut. The repeat is already proposed at 04:336–342 and 05:44–46. repetition.

86. `05:82–83` "This matters most for small planets around cool stars." → "The question is most pressing for small planets around cool stars." The checker flags "this matters"; the sentence is fine in itself, so this is a judgement call. AI tell.

87. `05:91–92` "and one for the spots and bright regions that the planet does not cross" → "and one for the spots and bright regions outside the planet's path". "That the planet does not cross" appears three times in the paragraph (05:83, 89, 92). repetition.

88. `05:112–114` "These signals are weak, and it would be interesting to see whether a detector-level analysis also makes them more reliable." → "These signals are weak, and a detector-level analysis may make them more reliable as well." "It would be interesting to see" is conversational for the register. clarity (judgement).

### 06_ai_use.tex

89. `06:1` "\section*{Use of generative AI}" → "\section*{Use of Generative AI}". The other section titles are in title case. consistency.

90. `06:3` "coding, and wording" → "coding and wording". No serial comma anywhere else ("A, B and C"). consistency.

### Captions and labels (all files)

91. `04:158` and `04:180` Both captions say "made before the corrections for the sky and the halo of the moved star". The text describes the halo correction (04:42–45) but no separate correction for the sky. See Part 4, Q3.

92. `05:144–158` Gantt labels are fine. "HWO2026, Paris (30 Nov)" matches 05:47.

---

## Part 2. If Davide changes only ten things

1. Item 28, the research question: "reduce the biases caused by extracting a spectrum first and fitting the transit without a background term?"
2. Item 9, the six wavelength ranges in the Introduction written with "to", as in every other section.
3. Item 13, the stray comma and double citation at 01:176, which prints as "(Figure 2), (Albert ...), at".
4. Item 24, remove "Crucially".
5. Item 12, remove "out of necessity, not by choice".
6. Item 35, move the field-star sentences to the end of the background paragraph in Section 2.5.
7. Item 42, introduce "the reference atmosphere" where it is first used in Section 3.2.
8. Item 52, one name, "the moved exposure", through Section 4.
9. Item 56, split the Gaia paragraph of Section 4.1 in three.
10. Item 69, cut the repeated explanation of the copy comparison in Section 4.3.

If there is an eleventh: item 38, the comma that closes the objective equation.

---

## Part 3. Whole-paragraph replacements

### 3A. 02:190–205, the background paragraph (items 35 and 36; order changed, every sentence kept)

```latex
The background left after Stage~2 is modelled with eight fixed spatial maps:
the zodiacal-light model that Stage~2 subtracted, and seven smooth polynomials
in detector position ($1$, $y$, $x$, $xy$, $y^2$, $x^2$ and $xy^2$). Each map
$\Phi_{pk}$ has a constant amplitude and an amplitude that follows one time
pattern $G(t)$,
\begin{equation}
 B_{tp}=\sum_{k=1}^{8}\Phi_{pk}
 \left[\alpha_{k0}+\alpha_{k1}\,G(t)\right].
 \label{eq:background-model}
\end{equation}
The 244,657 off-trace pixels, which lie away from the traces, field stars and bad pixels, are assumed to see only background, although some starlight from the faint wings of the traces may reach them (Section~\ref{sec:which-light}). The
maps are made orthonormal over these pixels. The maps and these pixels were
chosen once from the WASP-17 visit, where eight maps predicted held-out strips
of the off-trace image better than two or four. How well the maps
describe the background under the traces, and how much an error of the maps
there changes the depths, has not yet been tested. Field stars are also left out of the $1/f$ correction (Section~\ref{sec:detector-processing}), but NOVA does not yet treat field-star light that falls on the traces, which it cannot tell apart from the light of the target. A treatment of such light, for example with the positions of field-star spectra that Gaia predicts (Section~\ref{sec:measuring-star}), is future work, needed for both the benchmark and the WASP-17~b visit.
```

Reason: the definition of the off-trace pixels, their orthonormal maps and the untested point about the traces now stand together, and the field-star aside closes the paragraph instead of interrupting it.

### 3B. 03:41–48, the $1/f$ mechanism paragraph (item 43; sentence splits only)

```latex
My injector, however, dimmed only its model of the star. Near the traces, this model matched the real images. Outside them, at 0.85 to $1.75\,\mu\mathrm{m}$ in order~1, it held only about a third of the light that the correction expects to dim. In the real data, the dimming there was consistent with what the correction assumes, so much of this faint light seems to behave like starlight. During the transit, the correction therefore found too much light left outside the traces, mistook it for $1/f$ noise and removed it from the whole column. The transit became about 1 to 2\% too deep. To confirm this, I subtracted from the injected data the $1/f$ correction calculated from the same data without the transit. Without the transit, the light curve is flat, so the correction removes the same stripes but has no transit to react to. NOVA's error then fell to 150~ppm, so the correction caused about half of the increase.
```

Reason: the two 40-word sentences each carried two steps of the argument; "There" at the start of the control sentence now says what it refers to.

### 3C. 05:18–23, the order-of-work paragraph (items 79 and 80)

```latex
This lesson sets the order of the work. NOVA's first spectrum of the real
WASP-17~b visit is deeper than the published Ahsoka spectrum at every
wavelength, and most in the red (Section~\ref{sec:nova-real}), and its
uncertainty is not yet validated. An injection test shows how accurately each method recovers a known spectrum, and this is the best guide to which real spectrum to trust. An injector built from the WASP-17~b data alone cannot provide such a test. I am therefore
finishing the benchmark first. I will then use it to test NOVA and the other
pipelines, improve NOVA, and only then refit WASP-17~b.
```

Reason: removes "which is the best guide to which" and the "it" that could mean the test or the injector.

---

## Part 4. Questions for Davide (a better sentence would change the meaning) and one possible error

Q1. `03:33` gives 125~ppm and `03:88` gives 124~ppm. The fact sheet records these as different runs (124.8 for the count-rate injection, 124.0 for the lower estimate on the raw reads), but a reader sees "125 to 182" and then "124" and will ask whether 124 is the 125 again, and why the error fell from 182 to 124. If the reason is that the three injections of Section 3.3 dim the measured wings, unlike the first raw injector, one clause saying so at the start of Section 3.3 would close the gap. If the reason is something else, that is the clause to add. I have not changed either number.

Q2. `04:210–211` says the limb darkening for the spectral cases "is still to be chosen", whilst `04:333` says "the injected limb darkening follows one quadratic law computed from PHOENIX models of the star". If 04:333 describes the grey case, "For the grey case, the injected limb darkening follows ..." would reconcile them. If both sentences describe the same thing, one of them needs to change.

Q3. `04:158` and `04:180` (item 91): the captions refer to "the corrections for the sky and the halo of the moved star". Section 4.1 describes the halo correction but no sky correction; the only sky statement is that the two zodiacal levels agree to within about 1\%. Either the text should say what the sky correction is, in one sentence after 04:31, or the captions should say "the correction for the halo of the moved star" only.

Q4. Item 4 (the gas-loss sentence) is a cut, so it is Davide's decision, not a wording fix.

Q5. `06:2` "OpenAI's ChatGPT (Astra 6)": Opus 5.5 and Fable 5.1 are public model names that an examiner can look up. If "Astra 6" is not a public name, "OpenAI's ChatGPT" alone may be safer. I do not know the answer.

Q6. Section 4.5 uses "Firstly ... Fifthly, Finally" for six limitations. If Davide finds "Fourthly" and "Fifthly" heavy, the fourth and fifth can open "The injection also adds light but no response ..." and "The exposure also lasts only 2.68~h ..." with no change of content. Judgement, not a correction.

No factual errors were found in this read. The Ahsoka line at 01:310 ("Ahsoka, for example, used the bad-pixel step of supreme-SPOON") and 01:515 overlap, but 01:310 introduces the description of the step, so I did not propose a cut there.

---

Only this file was written. No ESA section was edited.
