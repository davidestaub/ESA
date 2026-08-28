# Injector evolution, current design, and fairness programme

## 1. Why the injector changed

The earliest injector was useful for engineering but too structurally aligned
with legacy NOVA.  It reused masks and response assumptions close to NOVA's own
model.  When PASTASOSS support and source morphology changed, the old mask could
assign source light to background or fail to dim supported flux.  This produced
the historical 1.03--1.10 micrometre gap and could preferentially reward NOVA.

The V45 lineage was built to make the detector cube method-neutral: all recovery
pipelines receive the same opaque cube; the injector cannot inspect their
apertures, q-star, recovered spectra, or truth residuals; and transit dimming is
applied only to the estimated target source.

## 2. Frozen V45 rateints benchmark

The source-free temporal baseline is constructed from real WASP-17 OOT rateints,
preserving realized detector noise, additive background, field stars, order-3
structure, and time variability.  A denoised target-source expectation is
decomposed by spectral order.  Per-order ATOCA fractional transit factors are
then applied to those expectations and summed into a detector deficit.  The
public cube is

```text
Y_injected(t,p) = Y_real_OOT(t,p)
                  + sum_o S_emp,o(t,p) [f_o(t,p)-1] .
```

Only the target expectation `S_emp,o` is multiplied by the transit factor.
Additive background and unrelated contaminants remain non-transiting, and the
realized noise is not artificially multiplied by the transit.  The source
expectation is denoised rather than copied from raw pixels, preventing the
injector from dimming a particular noise realization.

The V45 writer uses current PASTASOSS/WebbKernel geometry, flux-conserving wings,
and fail-closed support logic.  Significant empirical target light without a
valid model response is an error; it is not silently clipped or assigned
`f=1`.  Stage-2 SCI/ERR/DQ products are preserved, and one output cube is
consumed unchanged by NOVA, Ahsoka, and the planned comparison pipelines.

## 3. Current two-injector interpretation

There are presently two benchmark *lineages*, not two equally certified science
benchmarks:

1. **Frozen V45 rateints benchmark:** the current reproducible control used to
   freeze NOVA-S and obtain its certified scores.
2. **Paired group-stage/rateints fairness candidate:** a prospective experiment
   that begins from a common group-level baseline and makes matched injection
   realizations for testing whether authentic group-level 1/f correction changes
   method rankings.  It is not promoted until all delivery, identity, and
   cross-pipeline gates pass.

Calling both “final injectors” would be premature.  The paper may ultimately
retain V45 and report the paired experiment as a sensitivity test, or reissue
the benchmark if group-level preprocessing has a material effect.

## 4. Why group-stage testing is necessary

Ahsoka and supreme-SPOON/exoTEDRF perform their characteristic 1/f correction
on detector groups before ramp fitting.  A public rateints cube contains no
groups, so these pipelines cannot apply that stage authentically.  Poor red-end
performance on a rateints-only cube could therefore mix extraction quality with
a preprocessing handicap.

The preregistered fairness comparison is:

- construct one authenticated common group-level baseline;
- inject the same physical target deficit at group level and propagate through
  ramp fitting;
- construct the matched rateints-stage realization from the same source model;
- run NOVA and Ahsoka on both, with each pipeline's truth-blind preprocessing;
- compare zero-injection identity, delivered detector deficit, white-light
  scatter, red-end spectrum, and common-bin RMSE.

NOVA will also be run after the same group-level 1/f correction.  This tests
whether the preprocessing helps NOVA rather than granting it only to comparison
methods.  If the difference is small (prospectively around <=30 ppm in the red),
the rateints benchmark can remain with an explicit limitation.  If it is
material, a combined benchmark reissue and full rescore are required.

## 5. Per-order delivery and current ablation result

The modern writer reconstructs the target expectation separately for O1 and O2
and applies the corresponding fractional factors before summation.  This avoids
trusting one static scale for an order mixture that changes across the detector.
An exact ablation showed that the independent O1/O2 reconstruction itself is
machine-equivalent to frozen V45: relative L1 difference `2.8458e-15` and
maximum absolute difference `5.55e-14`.  Event relabelling changes signal mass
only at `2.7865e-6` relative scale.  These are numerical passes, not new
scientific effects.

The R7 PASTASOSS calibrated-domain exclusion removes 0.4326% of delivered signal
mass.  In contrast, the current broad full-column scene exclusion removes
9.8836%.  That explains why the current scene-enabled candidate recovers around
138 ppm rather than the frozen V45 control near 119 ppm on the same 127-event
comparison: it deletes genuine target support along with contaminants.  The
per-order decomposition and event timing are not responsible.

## 6. Scene contaminants and order 3

Scene treatment must be visit-adaptive but algorithmically fixed.  Detection
locations may change between visits; thresholds and model classes may not depend
on injected truth or recovered depths.  The required algorithm combines:

- OOT-only connected/multi-ridge detection;
- target-trace protection using current PASTASOSS geometry;
- detector-fixed versus dispersed-source checks across visits/roll angles;
- Gaia association where available;
- explicit dispersed-contaminant templates using a stellar model, empirical
  throughput, and translated target profile;
- separate treatment of order-3 structure in background training;
- a quantitative order-3 leakage bound when no authenticated response is used.

Broad removal of every detector column intersecting a scene candidate is not
acceptable because it removes target signal.  The current 9.8836% loss is a
diagnostic failure to repair, not evidence that contaminants should be ignored.

## 7. Fairness gates

The injector must quantify fairness as a delivered ppm budget through every
public extraction support, rather than simply label a cube fair.  Required
engineering cubes are zero injection, flat 500 ppm, flat 15,000 ppm, and a
structured spectrum.  Required checks include:

- zero-injection identity;
- per-order and summed detector-deficit closure;
- red-local block closure for x<=230;
- order-crossing and blue-edge closure;
- wing-flux closure at faint columns;
- null/non-transiting contaminant behavior;
- stability to oversampling choice;
- no significant empirical light without model support;
- identical opaque cube and reporting bins for every recovery pipeline.

If a fairness change moves red delivery by more than approximately 30 ppm at a
15,300 ppm depth, every pipeline must be rescored on the reissued cube.

## 8. Structural-neutrality tests

V45 and NOVA share a forward-model family: PASTASOSS geometry, WebbKernel/ATOCA
spectral mixing, and related spatial-response assumptions.  This is an inverse-
crime risk even though they do not share exact code or q-star.  The paper must
therefore inject deliberately mismatched models, varying at least spatial
profile, wavelength map, LSF, throughput, background morphology, and temporal
systematics.  NOVA's advantage must remain across these mismatches and across
held-out visits and atmospheric spectra.

## 9. Cross-pipeline programme

On the sealed fair cube(s), run:

- NOVA-S and any prospectively promoted NOVA successor;
- Ahsoka;
- supreme-SPOON/exoTEDRF;
- transitspectroscopy;
- JExoRES;
- Eureka! where a reproducible SOSS path is available.

Each method may choose its aperture and detrending settings using only its own
truth-blind OOT diagnostics.  All methods use common physical reporting bins and
the same primary RMSE convention.  Plot both Ahsoka orders separately in the
overlap and define its single headline spectrum using its documented/public
order selection, not an invented NOVA-style combination.

## 10. Multi-visit requirement

WASP-17 is a development visit, not sufficient validation.  Every additional
dataset must first pass an admission audit confirming target identity, visit
identity, mode/filter, OOT coverage, integration chronology, data quality,
background structure, field stars, and order-3 morphology.  Similar integration
counts do not establish that two products are distinct visits.  No dataset is
used merely because files are present on the cluster.

The first multi-visit campaign may use one common injected GCM, as requested,
but the paper-ready programme later requires additional spectra/GCMs and a held-
out visit that was never used to choose NOVA branches.

## 11. Honest current status

The frozen V45 benchmark remains the control.  The group/rateints injection core
and per-order writer exist, but the scene-enabled candidate currently removes
too much target signal and must not be promoted.  Authentic group-level 1/f
comparisons, the full pipeline matrix, multi-seed uncertainty ensemble, and
multi-visit sealed scores remain incomplete at the date of this handoff.
