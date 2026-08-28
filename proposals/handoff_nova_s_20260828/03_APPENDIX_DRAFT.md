# Technical Appendix draft

## A. Provenance and immutability

NOVA-S Science R1 is authenticated by
`05_REPRODUCIBILITY/FROZEN_NOVA_S_SCIENCE_R1/NOVA_S_RELEASE_MANIFEST.json`.
The audit script verifies 419 frozen files.  Internal V50 names are retained in
the code so that the certified run remains byte-traceable.  Diagnostics and
candidate models live outside the frozen directory.

The benchmark cube is the V45 method-neutral WASP-17 rateints cube.  It contains
229 integrations, of which indices 51--177 form the synthetic event.  The V50
curvature calibration therefore uses 102 event-complement integrations.  The
V47 q-star build uses 101 authenticated OOT integrations because its timing and
quality manifest excludes one additional sample.  These counts refer to
different fixed calibration masks and should not be conflated.

## B. Detector support and common reporting bins

The initial mapping contained 2,726 native groups.  The final fit excludes group
indices `[0,1,2020,2021,2724,2725]`, corresponding to order-1 columns 23, 24,
and 2043 and order-2 columns 974, 1677, and 1678, leaving 2,720 groups.  The
V47 q-star product also records eight unsupported q-star groups
`[325,556,591,679,2020,2084,2132,2195]`; the runtime support logic and mapping
manifests determine which detector elements contribute to each fit.

PASTASOSS order-1 training anchors end at detector coordinate
`x=73.62893`, corresponding to 2.75977449 micrometres for this visit.  Detector
columns 38--73 therefore rely on polynomial extrapolation.  The R7 paper rule
excludes any reporting bin with partial or complete use of these columns.  Bin
147 is 71.743% inside the direct domain but is excluded as a whole; bins 148 and
149 are outside or structurally unsupported.  Bin 146 is the last retained
whole bin and ends at 2.740018 micrometres.  The rule is instrument-defined,
fixed across methods, and applied only after recovery.

## C. Positive shared-spectrum parameterization

Let `w_j` be frozen basis-width weights and let `H_v` span the subspace
orthogonal to the constant gauge.  The physical depths are

```text
D_j = D_global exp[(H_v v)_j] / sum_k w_k exp[(H_v v)_k] .
```

This separates the mean transit level from chromatic morphology, preserves
positive depths, and makes the same 160 physical coefficients available to
both orders.  The small positive floor on `D_global` is `1e-6 + 1e-8 ppm` in
the internal transformed parameterization.  The optional two-coordinate
order-discrepancy block is fixed to numerical zero (`+/-1e-12` bounds).

## D. Q-star construction and known limitation

For each order, a robust median of baseline-normalized bright-pixel residuals
defines a depth-free event template `phi_o(t)`.  A pixel qualifies when at least
95% of its OOT samples are valid, its baseline is positive, and it lies above
the 35th percentile of eligible baseline brightness.  After removal of constant
and linear terms, the template is normalized to minimum -1.

For each pixel, the amplitude in

```text
y_p(t)=a0_p+a1_p tau(t)+A_p phi_o(t)
```

is estimated with four Huber solve/reweight iterations (`delta=1.345`).  Folds
alternate within each transit phase, preventing a fold from representing only
one portion of the event.  Per-group response weights are normalized to unit
sum.  Candidate second-difference penalties are ranked by opposite-fold
chi-squared, followed by fixed A/B stability gates.

The frozen V47 smoother operates on integer `trace_relative_rank`, rather than
the continuous coordinate `y-y_PASTASOSS(x)`.  Subsequent audits found 14
centroid resets greater than 0.5 pixel, a median 0.234-pixel registration
difference relative to the delivered V45 source, and approximately 0.9--1.9%
excess in-mask red response amplitude at the faintest columns.  The direct
operator decrement ratio is 0.98906, with cosine similarity 0.9965.  This
produces a dilution-like red bias because the continuum fixes native-group
brightness while q-star fixes spatial response.  The V51 continuous-coordinate
candidate improved red morphology but degraded order 2 and the headline score,
so it was not promoted.

## E. E13b background construction

Eight raw spatial maps comprise a standardized CRDS anchor plus seven broad
polynomials.  They are orthonormalized using authenticated off-trace pixels.
Ranks 2, 4, and 8 and competing families are assessed by blocked off-trace
cross-validation.  The selected rank 8 is the smallest rank with worst-fold
RMSE within 5% of the family minimum.

The eight spatial coefficients measured across OOT integrations are centered
and decomposed by SVD.  The first of the leading eight temporal singular vectors
with absolute transit-reference correlation no greater than 0.25 is selected;
this is component 1 with correlation -0.0734687.  A constant and this component
give two temporal modes.  Their Kronecker product with the eight spatial modes
gives 16 additive coefficients.  The OOT normal matrix supplies the quadratic
anchor used in the joint continuum/background VarPro solve.

## F. Common source-curvature selection

Stable trace columns are integrated per order after subtraction of the E13b OOT
expectation for calibration only.  On each 51-integration fold, a weighted
quadratic in time is divided by its weighted affine approximation.  Positive
fold candidates are normalized to unit training-fold mean and evaluated on the
opposite fold.

Held-out standardized chi-squared was 3.26065 for null, 3.21178 for common, and
3.15235 for per-order.  Selection gates required common to improve null by at
least 1%; per-order additionally had to improve common by at least 2% and improve
each order.  The order-2 per-order score (1.0226) was worse than its common score
(0.99964), hence common was selected.  Its OOT mean is one, its range is
0.999866573--1.000079673, its event-mean correction is -111.390 ppm, its maximum
excursion is 133.427 ppm, and the fold correlation is 0.999921.

## G. Exact profiled robust solve

For fixed nonlinear state `theta` and Huber weights `W`, the linear nuisance
problem is

```text
min_(beta,alpha) 1/2 ||W^(1/2)[y-X(theta)beta-Halpha]||^2
                 + 1/2 (alpha-alpha_off)^T N_off
                         (alpha-alpha_off).
```

The equilibrated sparse continuum normal block is factorized.  The background
coupling is reduced to a 16-dimensional Schur complement.  The profiled
residual and Jacobian include the response of the exact inner optimum to the
nonlinear coordinates.  Sufficient statistics are streamed to avoid storing a
dense detector Jacobian.

The nonlinear solve uses bounded trust-region reflective least squares inside
Huber IRLS.  Huber weights are updated outside the inner least-squares solve,
ensuring exact M-estimation rather than combining incompatible robust losses.
The threshold is 1.345.  Convergence requires maximum absolute weight change
below 0.001, relative objective change below `1e-8`, shared-spectrum changes
below fixed RMS tolerances, scale-aware KKT below `1e-6`, first-order optimality
below 0.002, agreement of deterministic starts, and a final fixed-weight
confirmation.  The soft and hard cycle caps are 25 and 50.

## H. Deterministic starts and evaluation

Start 0 uses the frozen white-light mean, zero chromatic morphology, and the
theory limb-darkening reference.  Start 1 uses the same mean, a predetermined
weighted-zero-mean 250 ppm morphology, and predetermined small limb-darkening
perturbations.  Starts are independent and exchange no optimizer state.

Truth values are unavailable to all preprocessing, fitting, starting, response
selection, mask construction, and convergence code.  After a terminal detector
prediction is immutable, the evaluation sidecar computes absolute RMSE, mean
bias, and morphology RMSE.  Because the fitted objective is detector-space
Huber likelihood, truth RMSE can rise between cycles without indicating that the
optimizer is moving backwards.

## I. Rejected or unpromoted model classes

- independent or priored per-order atmospheric-depth discrepancy;
- per-column priors on continuum coefficients;
- aggregate order-contrast priors;
- residual-location recentering with wavelength slopes;
- constant-recentering families superseded by V50;
- OOT-median source profiles vulnerable to background contamination;
- extra background temporal modes;
- global narrow-response smoothing and local wavelength hard-coding;
- recovery-side explicit order-overlap modelling;
- local transit-amplitude templates at the red end;
- V51 continuous-coordinate q-star, because local improvement accompanied O2
  and headline degradation;
- V54/V54-R2 response profiles, which improved morphology but did not satisfy
  all bias and promotion gates.

## J. Red-end causal result and remaining admissible test

NOVA-S closes its own noiseless flat detector model to approximately 1.3 ppm in
the red, while a noiseless flat generated through the fair injector retains a
-299.07 ppm red bias.  This proves a deterministic forward-operator mismatch.
The direct split attributes -167.36 ppm to the frozen response/operator and
-131.72 ppm to nuisance projection and nonlinear inversion.  Q-star carries a
median 0.999993 share of the two-term response-centroid attribution.  Order-2
overlap, rather than causing the defect, mitigates approximately 110 ppm of it.

An OOT-derived per-column amplitude scale with median 0.98870 reduced the direct
operator diagnostic to +0.57 ppm.  This licenses a prospective model family,
not the diagnostic result itself.  The final admissible candidate must apply one
global rule to all columns, use A/B OOT folds, be selected by held-out OOT
likelihood, preserve flux, and be sealed before transit RMSE is read.  It must
also preserve order-2 and headline performance.  No data beyond the PASTASOSS
training endpoint are eligible for paper scoring.

## K. Recommended uncertainty and covariance reporting

The final paper should report unweighted common-bin RMSE as the primary metric,
with weighted RMSE as a sensitivity measure, per-bin normalized residuals
`z=(D_hat-D_true)/sigma`, and morphology after removal of each spectrum's mean
bias.  A shared multi-seed injection ensemble should estimate RMSE sampling
uncertainty.  NOVA's spectral covariance should be published from the profiled
Jacobian/normal system, including the correlations induced by the shared basis,
background, and order overlap.
