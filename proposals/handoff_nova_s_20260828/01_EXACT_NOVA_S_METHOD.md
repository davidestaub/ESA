# Exact NOVA-S Science R1 method

## 1. Frozen identity and reporting domain

NOVA-S Science R1 is the immutable internal V50/QE/FULL lineage applied to the
V45 WASP-17 benchmark cube.  It uses the current PASTASOSS reference
`jwst_niriss_pastasoss_0002.asdf` (SHA-256 begins `b011d78`) and WebbKernel;
legacy SPECTRACE products are forbidden.  The recovery model has one shared
physical transmission spectrum for orders 1 and 2, unchanged STAGGER
limb-darkening reference profiles, the V47 current-cube FULL q-star response,
the QE OOT uncertainty guard, native linear continua, the E13b additive
background, and a frozen OOT-only common source-curvature factor.

The certified release score retained 143 R=100 bins.  The subsequent R7
paper-wide reporting amendment excludes whole bins 147--149 whenever any of
their support lies beyond the direct PASTASOSS training domain.  Bin 149 was
already structurally excluded.  The R7 score therefore uses 141 bins and does
not alter fitting, predictions, or uncertainties.

## 2. Input detector time series

The public V45 cube contains 229 integrations assembled from real out-of-transit
rateints from WASP-17 visit `01353101001`.  A synthetic event occupies indices
`[51,178)`, giving 127 event and 102 complement integrations.  Stage-2 SCI, ERR,
and DQ values are read directly.  There is no frozen background subtraction and
restoration: the recorded background-subtraction count is zero.  Valid samples
have finite positive ERR and do not carry the `DO_NOT_USE` bit.

The selected detector matrix contains 97,557 pixels per integration.  Six edge
groups without reliable mapping are removed: order-1 columns 23, 24, and 2043,
and order-2 columns 974, 1677, and 1678.  The final detector model contains 2,720
native `(order, detector-column)` groups.  Recovery retains the historical
disjoint order supports; the two order predictions are nevertheless summed in
detector space before residual evaluation.

## 3. Forward model

For integration `t` and detector pixel `p`, NOVA-S predicts

```text
m[t,p] = sum_o { R_o [ g(t) T_o(t; D, u_o) Psi_o c_o(t) ] }[p]
         + [H alpha][t,p] .
```

Here `o` denotes spectral order, `R_o` is the frozen order response containing
the PASTASOSS wavelength/trace geometry, WebbKernel line-spread mapping, and
V47 q-star spatial redistribution; `Psi_o` maps native column amplitudes onto
the fine wavelength representation; `T_o` is the exact exposure-integrated
transit model; `g(t)` is the frozen common source-curvature factor; `c_o(t)` is
the native per-column stellar continuum; and `H alpha` is the additive E13b
background.  The source/transit terms from both orders are added before the
residual is formed.  The additive background is never multiplied by `g` or by
the transit.

## 4. Shared physical transmission spectrum

The spectrum is represented by `K=160` shared adaptive physical basis
coefficients.  A signed bounded optimizer coordinate `v` is mapped to positive
depths using

```text
D_j = D_global * exp[(H_v v)_j]
      / sum_k w_k exp[(H_v v)_k] ,
```

where `w` contains frozen basis-width weights and `H_v` removes the constant
gauge.  The morphology has zero weighted mean, while `D_global` carries the
achromatic depth and has a small positive floor.  Orders 1 and 2 use this same
`D(lambda)`.  The two optional order-discrepancy coordinates are numerically
fixed within `+/-1e-12`; their terminal values are at this numerical scale and
have no physical freedom.  No atmospheric template, wavelength-local smoother,
or truth-informed spectral prior is used.

The fixed orbital geometry is:

- period 3.73548546 d;
- `a/R_star = 17.59002069137651`;
- impact parameter 0.33859071787462686;
- mid-transit time 60023.52874613816 BJD_TDB;
- eccentricity 0 and argument of periastron 0.

The implementation uses `JaxoplanetKeplerianTransitEngine`, backend quadrature
order 10, and 21-point finite-exposure quadrature.

## 5. Limb darkening

“STAGGER unchanged” means that the wavelength-dependent native-column quadratic
STAGGER theory reference is unchanged; it does not mean that all limb-darkening
coefficients are fixed.  For each order, six knots describe each of the two
Kipping-like internal variables `q1` and `q2`.  NOVA-S uses the
`offset_log_slope` variant: for each order and each of `q1` and `q2`, a constant
offset and a normalized log-wavelength slope are fitted.  This gives eight
nonlinear limb-darkening coordinates, projected into the six-knot deviation
basis.  The profiled priors use theory scale 0.5 in logit space and curvature
scale 2.0 per micrometre squared.  Fine nodes outside the valid theory support
are excluded rather than extrapolated.

## 6. Native continua

Each of the 2,720 native order-column groups has a level and a linear time
slope,

```text
c_g(t) = beta[g,0] + tau(t) beta[g,1] ,
```

giving 5,440 continuum coefficients.  These coefficients are linear nuisance
parameters and are eliminated exactly at every nonlinear evaluation.  The
group continuum controls total group brightness; q-star controls only the
within-group spatial distribution.  This separation explains why a one per
cent q-star amplitude error relative to the delivered source can produce an
approximately one per cent multiplicative depth bias.

## 7. V47 FULL q-star response

Q-star is a normalized cross-dispersion response within each native
`(order,x)` group.  It is not an additional transmission spectrum.

The V47 refresh uses only the public V45 recovery cube and forbids injected
truth, generator-private signals, and previous q-star products.  A per-pixel
weighted OOT intercept-plus-slope baseline is estimated.  Pixels must have at
least 95% valid OOT samples and positive baseline flux; the brightest 65% are
used to construct a robust median fractional-residual template.  Constant and
linear trends are removed and the template is normalized to define a depth-free
time morphology `phi_o(t)`.  The q-star timing mask contains 101 authenticated
OOT integrations after its additional timing/quality exclusion; this differs
from the 102 integrations used by the V50 curvature calibration.

Folds A and B alternate integrations within pre-OOT, ingress, full-transit,
egress, and post-OOT phases.  Each pixel is robustly fitted as

```text
y_p(t) = a0_p + a1_p tau(t) + A_p phi_o(t)
```

with Huber threshold 1.345 and four solve/reweight cycles.  Per-group amplitudes
are normalized to `q_p=A_p/sum_p A_p`.  A robust second-difference penalty
smooths the response along detector column and integer trace-relative rank; its
strength is chosen by opposite-fold chi-squared.  FULL is admitted only after
A/B stability gates, including p95 half-L1 <= 0.15 and centroid difference
<=0.5 pixel.

This refresh was beneficial overall, but the integer-rank coordinate is now a
known limitation.  It creates 14 centroid resets larger than 0.5 pixel and a
red-column amplitude mismatch.  This is documented as a defect of the frozen
response, not silently repaired in NOVA-S.

## 8. Detector uncertainties and the QE guard

FITS ERR values are first multiplied by frozen per-order scales:

- order 1: 3.0746905465;
- order 2: 4.1917779190.

The QE arm then derives one additional scale for each detector row using only
OOT data.  Alternating OOT folds fit a weighted level plus slope and predict the
opposite fold in both directions.  The scale is

```text
s_p = max[1, sqrt(sum r_cv^2 / max(n_cv-4,1))] .
```

No wavelength, injected truth, or recovered spectrum enters this rule.  The
final uncertainty is `sigma[t,p] = ERR[t,p] N_o s_p`.

## 9. E13b additive background

E13b contains eight spatial modes and two temporal modes, hence 16 linear
coefficients.  The selected `crds_anchored_low_rank` family begins with a
standardized CRDS background map and broad polynomial spatial modes
`1, y, x, xy, y^2, x^2, x y^2`, orthonormalized on authenticated safe off-trace
pixels.  Candidate ranks 2, 4, and 8 were assessed by blocked off-trace
cross-validation; rank 8 was the smallest whose worst-fold RMSE lay within 5%
of the family minimum.

Weighted spatial coefficients are measured for each OOT integration, centered,
and decomposed by SVD.  Among the first eight temporal singular vectors, the
first whose absolute correlation with the fixed transit-reference vector was
at most 0.25 was selected.  The chosen component was index 1, with transit
correlation -0.0734687 and control correlation -0.0556236.  The two temporal
modes are the constant and this normalized component.

The OOT expectation `alpha_off` and normal matrix `N_off` form a prior anchor.
At fixed nonlinear parameters, NOVA-S solves

```text
min_(beta,alpha) 1/2 ||W^(1/2)(y-X beta-H alpha)||^2
                 + 1/2 ||L(alpha-alpha_off)||^2,
                 with L^T L = N_off .
```

Continuum and background are therefore fitted jointly.  There is no frozen
background subtraction and there are no extra gamma variables.

## 10. Frozen common source curvature

The V50 calibration uses all 102 event-complement integrations, split 51/51.
After subtracting only the E13b OOT expectation for this calibration step,
stable trace flux is integrated per order.  Weighted quadratic and affine time
models are compared, and their positive ratio defines a candidate curvature.
Null, common, and per-order candidates are ranked by held-out standardized
chi-squared.  The scores were 3.26065, 3.21178, and 3.15235 respectively.  The
per-order candidate failed the requirement that both individual orders improve:
order 2 was worse than the common model.  The common candidate was therefore
selected and applied identically to both orders.

The frozen factor has OOT mean 1, range 0.999866573--1.000079673, and event-mean
correction -111.390 ppm.  Fold correlation is 0.999921.  It multiplies only the
stellar/transit source bundle and its derivatives, not the background.  It adds
zero fitted parameters.

## 11. VarPro, robust likelihood, and convergence

At fixed nonlinear parameters and fixed robust weights, all 5,440 continuum
and 16 background coefficients are solved as one global sparse linear problem.
The equilibrated continuum block is factorized and the 16-dimensional
background coupling is handled by a Schur complement.  The profiled Jacobian
differentiates through the exact inner optimum and is accumulated with streamed
sufficient statistics.

The outer nonlinear optimizer is bounded trust-region reflective least squares.
Robustness is implemented as exact outer Huber IRLS with threshold 1.345; the
inner solver therefore retains a linear least-squares loss.  Weight stability,
relative objective change, shared-spectrum changes, KKT scale, first-order
optimality, and final-weight confirmation are all required.  Soft and hard IRLS
caps are 25 and 50 cycles.  Both deterministic starts converged at cycle 14.

Start A uses the frozen white-light mean depth, zero morphology, and theory
limb darkening.  Start B uses the same mean depth, a fixed zero-mean 250 ppm
morphology perturbation, and small fixed limb-darkening perturbations.  There is
no cross-start state transfer.  The selected solution is determined under the
prospective convergence policy, not by transit-truth RMSE.

## 12. Certified results

Historical release domain, 143 bins:

| Metric | ppm |
|---|---:|
| Absolute RMSE | 117.830915108 |
| Mean bias | +6.822110979 |
| Morphology RMSE | 117.633257870 |
| O1 morphology, 0.90--2.60 um excluding gap | 98.438905250 |
| O2 morphology below 0.84 um | 61.310060737 |
| Broad O1-minus-O2 mean bias | -8.359507728 |

R7 calibrated PASTASOSS reporting domain, 141 bins:

| Metric | ppm |
|---|---:|
| Absolute RMSE | 115.973386776 |
| Mean bias | +8.828130955 |
| Morphology RMSE | 115.636890931 |

Truth is read only after the immutable detector prediction is closed.  The
optimizer minimizes robust detector likelihood, not truth RMSE; consequently
intermediate truth RMSE need not decrease monotonically even when the fitted
detector objective improves.
