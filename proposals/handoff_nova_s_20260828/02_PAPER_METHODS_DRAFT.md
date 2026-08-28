# Paper Methods draft: NOVA-S detector-level joint inference

## Overview

We developed NOVA-S, a detector-level inference framework for JWST/NIRISS SOSS
transit spectroscopy.  Rather than extracting the two spectral orders
independently, NOVA-S predicts their two-dimensional detector contributions and
fits one shared physical transmission spectrum.  The final science release was
frozen prospectively before the diagnostic work described below.  All
calibration and model-selection operations use only the observed detector data,
instrument references, and out-of-transit information; injected truth is read
only after a detector prediction has been closed for evaluation.

## Detector data and response

The benchmark time series comprised 229 Stage-2 rateints integrations from the
WASP-17 NIRISS/SOSS observation, arranged as a method-neutral injected cube with
a 127-integration synthetic event.  We used Stage-2 SCI, ERR, and DQ arrays
directly and retained finite samples with positive uncertainties and without the
`DO_NOT_USE` flag.  No frozen background was subtracted from the science data.
The source model used the current PASTASOSS wavelength and trace solution and
WebbKernel line-spread response.  Legacy SPECTRACE products were not used.

For integration `t` and detector pixel `p`, the model was the sum of the
order-1 and order-2 source predictions and an additive background,

```text
m_tp = sum_o R_o { g_t T_o[D(lambda),u_o] Psi_o c_o(t) }_p + (H alpha)_tp .
```

Here `R_o` includes the order geometry, spectral mixing, and empirical
cross-dispersion response; `T_o` is the finite-exposure transit model; `g_t` is
a frozen common source-curvature factor; `c_o(t)` describes the native-column
stellar continua; and `H alpha` is the background.  The background is additive
and is never modulated by the transit or source-curvature factor.

## Shared spectrum and transit model

The transmission spectrum was described by 160 positive adaptive basis
coefficients.  A separate coordinate represented the wavelength-averaged
depth, while the remaining coordinates described a weighted-zero-mean spectral
morphology.  The same physical `D(lambda)` generated both orders; optional
order-discrepancy coordinates were fixed numerically to zero.  We imposed no
atmospheric template and no wavelength-local smoothing prior.

We fixed the orbital period to 3.73548546 d, `a/R_star` to
17.59002069137651, impact parameter to 0.33859071787462686, mid-transit time to
60023.52874613816 BJD_TDB, and eccentricity to zero.  Transit light curves were
computed with an exact Keplerian implementation and 21-point finite-exposure
quadrature.  The wavelength-dependent STAGGER quadratic limb-darkening profiles
were retained as the theory reference.  Eight fitted coordinates allowed a
constant offset and a log-wavelength slope for each of the two transformed
limb-darkening variables in each order, with theory and curvature regularization.

## Empirical spatial response

Within each native order-column group, an empirical q-star response redistributed
the group flux across detector rows.  The response was rebuilt from the current
public cube without access to injected truth or generator-private products.
Pixel time series were fitted with a level, linear trend, and a depth-free event
morphology under robust loss.  Alternating phase-stratified folds provided
independent response estimates, and the full response was accepted only after
cross-fold flux-distribution and centroid stability tests.  Response totals
were normalized within every native group, leaving total group brightness to
the fitted continuum.

## Continua, uncertainties, and additive background

After excluding six unsupported detector-edge groups, the fit contained 2,720
native order-column continua, each with a level and linear time slope.  These
5,440 coefficients were linear nuisance parameters.  FITS uncertainties were
multiplied by fixed per-order scales and by a truth-blind, per-detector-row guard
derived from bidirectional OOT cross-validation.

The E13b background contained eight spatial modes and two temporal modes.  Its
spatial rank and family were chosen by blocked cross-validation on authenticated
off-trace pixels.  The temporal mode was chosen from the leading singular
vectors of the OOT spatial-coefficient time series subject to a fixed maximum
absolute correlation of 0.25 with the transit-reference vector.  The selected
correlation was -0.0735.  Background coefficients were solved jointly with the
source continua and anchored by their OOT expectation and normal matrix.

## OOT-only source curvature

We calibrated a small wavelength-independent temporal source-curvature factor
from the 102 integrations outside the synthetic event.  Null, common, and
per-order quadratic-to-affine corrections were compared by 51/51 held-out OOT
folds.  Although the per-order candidate had the lowest aggregate score, it
failed the preregistered requirement that both orders improve.  We therefore
selected the common factor.  It was normalized to unit OOT mean, applied
identically to both orders, and introduced no fitted parameters.

## Profiled robust optimization

At every nonlinear evaluation, NOVA-S eliminated all continuum and background
coefficients exactly using variable projection.  The sparse continuum block was
factorized and coupled to the 16 background coefficients through a Schur
complement.  Nonlinear parameters were optimized with bounded trust-region
reflective least squares.  Detector outliers were handled by outer Huber
iteratively reweighted least squares with threshold 1.345 and a final-weight
confirmation step.  Two deterministic starts were run independently: a flat
spectrum at the white-light depth and a fixed zero-mean 250 ppm morphology
perturbation.  Both starts converged after 14 robust cycles.

## Reporting support and benchmark score

The immutable release originally retained 143 common R=100 bins and achieved
117.831 ppm absolute RMSE, +6.822 ppm mean bias, and 117.633 ppm morphology
RMSE.  For all paper-wide comparisons we subsequently applied one instrument-
defined reporting rule: any bin whose detector support extended beyond the
direct PASTASOSS training domain was excluded in full.  This rule changes no fit
or prediction and leaves 141 bins ending at approximately 2.740 micrometres.
On that domain NOVA-S achieved 115.973 ppm absolute RMSE, +8.828 ppm mean bias,
and 115.637 ppm morphology RMSE.

## Development and negative-result policy

All candidate changes were first compared through truth-blind OOT detector
diagnostics.  A candidate was not promoted if it improved a local region while
degrading order 2 or the headline result.  We report important negative results,
including independent order-depth freedom, continuum priors, aggregate
order-contrast priors, wavelength-dependent recentering, extra background
temporal modes, a global narrow-response swap, explicit recovery-side overlap
modelling, and continuous-coordinate q-star variants that failed the full
promotion gates.  The frozen release remained unchanged throughout these tests.

## Benchmark-fairness statement

The science benchmark uses one opaque detector cube for every recovery method.
The injector does not consume NOVA q-star, NOVA masks, recovered spectra, or
injected-truth residuals.  Its source deficit is built independently for each
order using the same public instrument references and is applied only to the
target-source expectation; additive background and contaminating sources remain
non-transiting.  Because the principal comparison pipelines perform their most
distinctive 1/f correction at group level, the paper programme additionally
includes paired group-stage and rateints-stage injections.  These constitute a
fairness sensitivity experiment rather than a replacement of the frozen
rateints benchmark unless the preregistered reissue gates are met.

> Author note: insert citations for PASTASOSS, WebbKernel/ATOCA, STAGGER,
> jaxoplanet, VarPro, Huber loss, Ahsoka, supreme-SPOON/exoTEDRF, JExoRES,
> transitspectroscopy, and the JWST pipeline in the journal manuscript.
