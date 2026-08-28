# Current status, limitations, and ordered path to a paper-ready result

## 1. What is complete

- NOVA-S Science R1 is frozen, authenticated, and reproducible.
- Both deterministic starts reached strict final-weight-confirmed convergence.
- The current paper-wide PASTASOSS calibrated-domain rule is fixed and rescored.
- The 1.03--1.10 micrometre support gap was repaired in the modern injector.
- The broad order offset and crossing-region failure were substantially reduced.
- The red-end error has been causally localized to a deterministic O1 response
  mismatch dominated by the V47 q-star; overlap, limb darkening, curvature,
  random noise, optimizer failure, and red field-star contamination are ruled out.
- Recovery-side explicit overlap modelling has been tested and archived as a
  negative result.
- V54/V54-R2 and F277W have supplied improved/profile-independent information,
  but no successor passed the complete promotion gates.
- A modern per-order injector writer and a paired group/rateints experiment are
  implemented sufficiently for ablation, and the per-order rebuild is proven
  numerically identical to V45 when no new masks are applied.
- The current scene regression is understood: broad column exclusions delete
  9.8836% of target signal.

## 2. Frozen scientific result

NOVA-S remains the science control.  Its R7 paper-domain score is:

- 115.973387 ppm absolute RMSE;
- +8.828131 ppm mean bias;
- 115.636891 ppm morphology RMSE;
- 141 retained common bins;
- last fully supported bin ending at approximately 2.740018 micrometres.

The historical 143-bin release score remains part of provenance but should not
be mixed with the paper-wide R7 comparison.  Report the domain beside every
number.

## 3. Remaining supported red-end experiment

One scientifically distinct test remains before ending red-end development:

1. Freeze the V54-R2 continuous-coordinate, flux-conserving spatial profile
   construction.
2. Add a response-amplitude calibration using one global rule for every eligible
   detector column.  Estimate it only from OOT A/B folds; do not use the event,
   truth, recovered depths, or wavelength-local thresholds.
3. Gate the response on opposite-fold detector likelihood, scale agreement,
   flux conservation, centroid stability, response mass, and conditioning.
4. Run exact self-closure and fair-injector noiseless-flat recovery.
5. Seal the candidate, run both deterministic atmospheric starts once, and read
   transit RMSE only after terminal convergence.
6. Promote only if it improves or preserves the R7 headline, bias, O1, O2, and
   crossing-region metrics.  A local red improvement cannot compensate for O2
   or global degradation.

This is not a repeat of V36.  V36 constrained continuum coefficients; the new
test calibrates the detector response before continuum fitting.  It is also not
a replacement for VarPro.  Matched noiseless self-closure proves that VarPro is
working as designed.

If this experiment fails, stop modifying q-star for this benchmark.  Report the
frozen model, the supported domain, the red noise/identifiability floor, and the
negative result.  Do not invent a local wavelength correction.

## 4. Injector repair before final scoring

1. Replace full-column scene deletion with target/contaminant separation.
2. Detect field stars and order-3 structures from OOT data using fixed,
   visit-independent rules and visit-dependent locations.
3. Fit non-transiting contaminant templates where possible; protect the target
   trace and quantify residual leakage.
4. Close zero, flat-500, flat-15000, and structured per-order delivery gates,
   including red-local and wing-flux budgets.
5. Complete the paired group-stage/rateints injection and authentic group-level
   1/f comparison for NOVA and Ahsoka.
6. Decide prospectively whether V45 stays the benchmark or whether a combined
   group-level/fairness reissue is required.  If reissued, rerun every pipeline.

## 5. NOVA improvements orthogonal to red bias

- Test a VarPro-eliminable per-integration column-offset/1/f nuisance anchored
  by off-trace or other-order pixels.  Rank by held-out OOT likelihood.  This can
  improve morphology but cannot explain the existing noiseless bias.
- Complete the per-bin Fisher/identifiability table: response mass, usable pixel
  count, conditioning, expected uncertainty, and noise-only RMSE.
- Propagate and publish the shared-spectrum covariance.
- Add connected-region outlier handling under a prospective OOT-only contract.
- Audit the E13b basis across the x~700 pick-off-mirror step and across visits.

## 6. Multi-visit and cross-pipeline validation

1. Authenticate each candidate visit and OOT segment before injection.
2. Freeze one development visit and at least one held-out visit.
3. Run the same injected GCM first across all admitted visits.
4. On each sealed cube run NOVA, Ahsoka, supreme-SPOON/exoTEDRF,
   transitspectroscopy, JExoRES, and Eureka! where feasible.
5. Preserve each pipeline's authentic truth-blind OOT tuning; do not import
   NOVA masks or apertures.
6. Report separate O1/O2 spectra wherever a pipeline provides them, in addition
   to the preregistered headline spectrum.
7. Repeat with at least eight method-neutral noise seeds to estimate RMSE
   uncertainty.
8. Add different GCM/spectral morphologies after the first one-GCM campaign.

## 7. Structural-neutrality and real-data checks

- Injector adjoint self-recovery with the injector's own forward operator.
- Cross-pipeline concordance of red residuals on the same cube.
- Real-data OOT null injection with a fake ephemeris.
- Deliberately mismatched injector/recovery spatial profile, wavelength map,
  LSF, throughput, background, and temporal systematics.
- Group-level versus integration-level 1/f A/B on the real visit.
- Published accounting of rateints limitations and any preprocessing handicap.

## 8. Scoring contract before sealed evaluation

- Primary: unweighted RMSE over common prospectively supported R=100 bins.
- Report mean bias and morphology RMSE separately.
- Report O1, O2, overlap/crossing, and supported-red subregions.
- Report weighted RMSE only as a sensitivity statistic.
- Calibrate uncertainties using per-bin normalized residuals.
- Attach RMSE uncertainty from the shared seed ensemble.
- Use the identical R7 PASTASOSS support rule for all methods.
- Keep engineering flat/noiseless cubes separate from sealed science scoring.

## 9. Paper deliverables

- Frozen NOVA-S source and configuration archive.
- Fair injector release with delivery/fairness budget and identity tests.
- Complete methods and appendix text.
- Development/negative-result table.
- Multi-visit detector images and admission table.
- All-pipeline spectra, residuals, uncertainties, and common-bin scores.
- Noise-seed and mismatched-forward-model sensitivity figures.
- Background/1/f design-choice sensitivity figure.
- Spectrum covariance products.
- Machine-readable provenance, exact software environments, and checksums.

## 10. Stop conditions

The programme is paper-ready only when the benchmark is sealed, all admitted
pipelines have run on the same opaque cube(s), the held-out visit and structural-
neutrality tests are complete, and the scoring convention is frozen.  A local
NOVA improvement alone is not sufficient.  Conversely, the project should stop
tuning a region when a preregistered candidate fails and the residual is at the
measured identifiability/noise floor; that outcome is scientifically reportable.
