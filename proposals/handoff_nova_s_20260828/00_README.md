# NOVA-S paper and methods handoff — 2026-08-28 R1

This archive is the compact, self-contained handoff for understanding the
frozen NOVA-S Science R1 method, its benchmark injector, the development
history, the unsuccessful experiments, the red-end diagnosis, and the work
that remains before paper-wide claims are sealed.

## Read this first

The name **NOVA-S** refers only to the immutable V50/QE/FULL release in
`05_REPRODUCIBILITY/FROZEN_NOVA_S_SCIENCE_R1`.  Later experiments such as
V51, V54, V54-R2, overlap branches, adaptive response tests, and the current
injector factorial are candidates or diagnostics; none is NOVA-S unless a new
prospective release is certified.

The frozen model's certified historical score was 117.830915 ppm absolute RMSE
over 143 bins.  The paper-wide PASTASOSS training-domain rule introduced later
does not refit the model: it removes every bin that uses detector columns beyond
the direct PASTASOSS calibration domain.  Under this prospective reporting
rule, NOVA-S has 115.973387 ppm absolute RMSE, +8.828131 ppm mean bias, and
115.636891 ppm morphology RMSE over 141 bins.  The last fully retained bin ends
at approximately 2.740018 micrometres.  No claim is made for the extrapolated
detector columns beyond approximately 2.760 micrometres.

## Directory map

- `01_PAPER_TEXT/01_EXACT_NOVA_S_METHOD.md`: exact model and implementation.
- `01_PAPER_TEXT/02_PAPER_METHODS_DRAFT.md`: paper-ready Methods draft.
- `01_PAPER_TEXT/03_APPENDIX_DRAFT.md`: appendix-ready technical detail.
- `02_EXPERIMENT_HISTORY/EXPERIMENTAL_HISTORY_AND_NEGATIVE_RESULTS.md`:
  chronological decisions, improvements, failures, and settled diagnostics.
- `02_EXPERIMENT_HISTORY/RED_END_CAUSAL_AUDITS/`: executable audit code and
  machine-readable causal evidence.
- `03_INJECTOR_FAIRNESS/INJECTOR_EVOLUTION_AND_FAIRNESS.md`: what the old and
  current injectors do, fairness limitations, and the rateints/group-stage plan.
- `04_CURRENT_PROGRAMME/CURRENT_STATUS_LIMITATIONS_NEXT_STEPS.md`: honest
  current status and ordered paper-readiness plan.
- `05_REPRODUCIBILITY/REPRODUCTION_AND_SOURCE_INDEX.md`: provenance, hashes,
  source layout, and verification instructions.
- `05_REPRODUCIBILITY/FROZEN_NOVA_S_SCIENCE_R1/`: complete authenticated frozen
  NOVA-S release, including code, configuration, predictions, and audit script.

## Non-negotiable scientific boundaries

1. No injected truth or recovered-depth residual may construct or select a
   response, mask, nuisance model, threshold, or correction.
2. NOVA fits one shared physical transmission spectrum for both orders.  The
   order-discrepancy coordinates are fixed to zero.
3. The STAGGER limb-darkening reference is unchanged.
4. Background is additive and is not multiplied by the transit or source term.
5. The benchmark is one opaque cube consumed unchanged by every pipeline.
6. OOT-derived calibrations are fold-validated and ranked first by held-out OOT
   detector likelihood.
7. NOVA-S remains the control until a candidate passes a new prospective
   contract and a sealed evaluation.

## Important interpretation of q-star

The V47 q-star refresh was a major net improvement: it replaced a stale
response with one estimated from the current public V45 cube and reduced the
global spectral error substantially.  It is also the main identified source of
the remaining supported red-end bias.  Its integer trace-relative coordinate
causes centroid resets, and its red-column response amplitude is about one per
cent too high relative to the delivered source.  Because each native-column
continuum sets the group brightness, that response over-amplitude makes the
recovered transit too shallow.  These statements are not contradictory: the
refresh improved most of the spectrum while leaving a local calibration defect.

The admissible remaining experiment is a continuous-coordinate, flux-conserving
profile plus a global OOT-only, A/B-validated per-column response-amplitude
calibration.  A diagnostic version removed the direct operator bias, but that
diagnostic informed the hypothesis after the red problem was known; only the
prospectively fixed truth-blind implementation may be evaluated for promotion.

## Archive scope

Large raw JWST cubes and the 31 MB E13b basis array are omitted to keep this
handoff below 50 MB.  Their exact hashes and provenance are retained.  The
complete frozen code and all small products needed to understand the method are
included.  This is sufficient for paper writing and code review; full detector
reruns additionally require the authenticated cluster inputs listed in the
source index.
