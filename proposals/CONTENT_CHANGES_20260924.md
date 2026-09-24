# Content changes to the ESA Introduction and Methods (24 Sept 2026)

Every place where the rewrite changed what the text says (not just wording), with the audit verdict.
Verdicts come from independent verifiers who were told to defend the ORIGINAL text against the code.
NEW = the new text is right; PARTLY = merged (both had something right); OLD = the original was already right, the change is a clarification.

| # | Where (current file:line) | Topic | Original said | Now says | Audit |
|---|---|---|---|---|---|
| C1 | sections/02_methods.tex:306 | Background subtraction before NOVA | "No fixed background is subtracted at any stage" | exoTEDRF Stage 2 subtracts a scaled background model before NOVA; NOVA's background term models what remains | NEW |
| C2 | sections/02_methods.tex:889 | Injected orbit | control-file orbit, "duration matched to that file" | control-file P and b kept; a/R* and i rescaled so T14 = 1.74 h fits integrations 51-177 | NEW |
| C36 | sections/02_methods.tex:899 | t0 prior (disclosure) | "no recovery receives these values" | t0 prior of every white fit centred on the window midpoint = injected t0; P, e, omega shared | NEW |
| C3 | sections/02_methods.tex:502 | Start agreement | starts "must agree to within 0.1 and 0.5 ppm" | lowest-objective strict start selected; agreement reported, not required (current code) | NEW |
| C4 | sections/02_methods.tex:481 | Convergence tests | stationary on "two spectral summaries" | names the 40- and 96-bin grids and adds the weight/objective tolerances | OLD (clarification) |
| C5 | sections/02_methods.tex:489 | Cauchy/Gauss-Newton descent audit | required for acceptance | only in the July factorial optimiser; production solver (August and now) does not run it | PARTLY (merged) |
| C6 | sections/02_methods.tex:384 | Uncertainty scale | per detector row, 280/70 split | per pixel, two-way alternating folds (175/175) | NEW |
| C7 | sections/02_methods.tex:226 | q* pixel cuts | 95%/35th-percentile cuts decide which pixels are fitted | cuts only choose the template pixels; every support pixel is fitted | NEW |
| C8 | sections/02_methods.tex:253 | q* folds and smoothing | two folds give independent estimates | full-data fit, smoothing strength chosen by cross-fold prediction; folds gate; wing mixing added | NEW |
| C10 | sections/02_methods.tex:269 | Red-end q* bias | stated as a current property | same cause kept; numbers from the earlier release audits, not re-measured per input | PARTLY (merged) |
| C19 | sections/02_methods.tex:97 | Order overlap | overlapping pixels summed over both orders | order supports share no pixel | NEW |
| C20 | sections/02_methods.tex:161 | Order-difference term | single offset +-Delta | offset and slope, fixed at exactly zero (reason kept) | PARTLY (merged) |
| C22 | sections/02_methods.tex:370 | Curvature fold-correlation gate | real reference only | real visit and injected inputs; diagnostic for ensemble | NEW |
| C24 | sections/02_methods.tex:138 | Spectral basis and reporting map | "160 for each of the two orders" | 160 shared top-hats; 2x160 was two starts; overlap-weighted mean, rank 128 explained | NEW |
| C49 | sections/02_methods.tex:593 | b handoff | median of whole posterior | b computed from medians of a/R* and i | NEW |
| C50 | sections/02_methods.tex:552 | Reason for nested sampling | emcee did not reach 50 autocorrelation lengths | same reason, plus stranded walkers (~12% grazing found later) | PARTLY (merged) |
| C53 | sections/02_methods.tex:525 | White-light curves | "built from the retained samples" | optimal (profile-weighted) extraction per column; noted as the one place NOVA extracts | NEW |
| C15 | sections/02_methods.tex:584 | v7 rule provenance | "fixed before it was calibrated" | fifth revision; written after the real grazing mass was known to be zero | NEW |
| C16 | sections/02_methods.tex:595 | Real-visit geometry | nested sampling "throughout" | real reference spectrum fitted at an earlier emcee geometry; nested fit reproduces it | NEW |
| C17 | sections/02_methods.tex:660 | Failed ensemble realisations | "stays in the denominator" | covariance only formed when all 288 complete; failures stay in denominator for block-length sets | PARTLY (merged) |
| C11 | sections/02_methods.tex:998 | Per-order accounting | "per-order accounting exactly" | orders summed before transport; no exact per-order check | NEW |
| C12 | sections/02_methods.tex:919 | Rate-level control tables | integration-level packets of the rate control | rate control uses per-read tables; integration tables are the reference check | NEW |
| C56 | sections/02_methods.tex:923 | Integration-0 round-off | set to exactly 1 (general) | only for the three pilot tables, with approval; new tables: failure | NEW |
| C34 | sections/02_methods.tex:995 | Newton target, float writing | finds "the raw count" | finds the linearity-step input value; ramps written as floats | NEW |
| C31 | sections/02_methods.tex:978 | Flat-field coefficient | reference-file value | effective flat (flagged = 1); range on original 507,606-pixel support kept | PARTLY (merged) |
| C35 | sections/02_methods.tex:1033 | NOVA detector chain | chain without versions | exoTEDRF 2.4.3, no dark step, Stage 2 background/flat/bad-pixel, first/last 50 integrations as OOT reference | NEW |
| C13 | sections/02_methods.tex:1051 | Comparator input | pilot comparisons at rate level | comparators run on the injected raw frames (your request) | NEW |
| C14 | sections/02_methods.tex:1191 | transitspectroscopy | "keeps its authors' fit structure" | joint white fit declared as your departure; LD grid switch after its white fit, before any score | NEW |
| C28 | sections/02_methods.tex:838 | m_x upper bound | upper bound | upper bound pending the pre-1/f repeat (merged) | PARTLY (merged) |
| C29 | sections/02_methods.tex:828 | m_x denominator | "real white transit depth" 0.0136288893 | mean fractional decrement of the white model over 315 integrations (same number, restated) | OLD (clarification) |
| C30 | sections/02_methods.tex:802 | Wing/far source estimate | band sums preserved in the wings | one estimate over whole outer region; band sums preserved over that region | NEW |
| C41 | sections/02_methods.tex:841 | Ineligible outer pixels | F277W pixels keep modelled light | 10,838 F277W + 4,600 other outer pixels keep modelled light | PARTLY (merged) |
| C42 | sections/02_methods.tex:1087 | Grey delivery test | 2,188 "columns" | 2,188 order-column pairs; gain definition given | NEW |
| C43 | sections/02_methods.tex:1068 | Delivery checks | compressed list | spelled out; aperture-sum check placed in the 1/f step | OLD (clarification) |
| C40 | sections/02_methods.tex:1150 | Per-visit checks | "core and wing checks" | five core regions, 0.15%/0.25% wing limits, exceptions declared | OLD (clarification) |
| C39 | sections/02_methods.tex:1132 | Envelope wording | validated/usable rule | same rule, glossed (RMS); envelope is NOVA's sensitivity only | OLD (clarification) |
| C44 | sections/02_methods.tex:1119 | Pilot atmospheres | undefined | Goyal et al. 2019 grid, both atmospheres' parameters | NEW |
| C45 | sections/02_methods.tex:931 | Transit spans | 50-178 and 51-177 stated | same numbers, with the reason (radius ratio) | OLD (clarification) |
| C25 | sections/02_methods.tex:1255 | Injected depth per bin | not stated | unweighted average over the bin | NEW |
| C26 | sections/02_methods.tex:1253 | Missing bins | bin reported as missing | method recorded as a failure, not scored | NEW |
| C27 | sections/02_methods.tex:1250 | Coverage rule | same rule for all | complete coverage for NOVA; comparator coverage reported | NEW |
| I1 | sections/01_introduction.tex:785 | Intro: what the injector does | "generates" background, noise, flags | writes into the raw data of real pre-transit integrations | NEW |
| I3 | sections/01_introduction.tex:665 | Intro: separating source and background | "time-independent background"; in/out-of-transit separates | single-pixel degeneracy; separation needs many pixels sharing one depth | NEW |
| I4 | sections/01_introduction.tex:352 | Intro: why SOSS orders curve/overlap | "slitless, cross-dispersed design" | prism dispersion and mechanical clearance (Albert et al. 2023) | NEW |
| I7 | sections/01_introduction.tex:563 | Intro: Constantinou claim | "about one order of magnitude" | "up to about", 3-5 um data | NEW |
| I9 | sections/01_introduction.tex:611 | Intro: ATOCA additions | not present | ATOCA 10 ppm and ~1% overlap bias (box extraction) | NEW |
| I5 | sections/01_introduction.tex:341 | Intro: instrument citation | Gardner 2006 | Rigby 2023 (Gardner predates NIRISS) | NEW |
