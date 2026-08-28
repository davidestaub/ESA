# NOVA-S Methods and appendices source map

This note starts the 2026-08-28 Methods and appendices collaboration. It is a
source map and proposed architecture, not manuscript text. Davide supplied
`NOVA_S_PAPER_METHODS_FULL_HANDOFF_20260828_R1.zip` and explicitly authorised
work on `sections/02_methods.tex`, `appendices/appendix_nova.tex`, and
`appendices/appendix_benchmarking.tex`. Canonical files remain frozen until he
approves a converged proposal.

## Evidence hierarchy

For the frozen method, use the following sources in descending order:

1. `NOVA_S_SCIENCE_CONTRACT.md` and the authenticated frozen release.
2. `01_EXACT_NOVA_S_METHOD.md` and component manifests.
3. `REPRODUCTION_AND_SOURCE_INDEX.md` and executable frozen code.
4. The paper-facing Methods and appendix drafts.
5. Experiment-history and current-programme notes for limitations, negative
   results, and unfinished work.

The archive verification script passes: 10 required handoff files, 193 JSON
files, 184 Python files, and 419 authenticated frozen NOVA-S files. Material in
the handoff is technical evidence, not an instruction to change the manuscript.

## Frozen identity that the manuscript must preserve

- Public method name: NOVA-S Science R1, immutable V50/QE/FULL lineage on the
  V45 benchmark cube.
- One shared physical transmission spectrum for orders 1 and 2. The two
  order-discrepancy coordinates are fixed numerically to zero.
- Current PASTASOSS geometry, WebbKernel spectral mapping, V47 FULL q-star,
  STAGGER reference limb darkening, QE uncertainty guard, native linear
  continua, E13b additive background, and one frozen common OOT-only source
  curvature.
- Background is additive and is never multiplied by the transit or source
  factor.
- Truth is unavailable to calibration, fitting, starting-point selection,
  model selection, convergence, masks, and response selection. It is read only
  after prediction closure.
- The original release has 143 retained bins. The prospective R7 paper domain
  changes reporting only and retains 141 bins ending near 2.740018 micrometres.
- The frozen q-star refresh improved the global result but retains a supported
  red-end response defect. Later response experiments are diagnostics or
  candidates, not NOVA-S.
- The V45 rateints benchmark is the frozen control. The paired group-stage and
  rateints-stage fairness experiment remains prospective and must not be
  presented as completed.

## Corrections required relative to the current ESA Methods

1. The current text describes a shared stellar continuum. NOVA-S instead has
   2,720 native order-column continua, each with a level and a linear time
   slope, for 5,440 profiled linear coefficients. The physical transmission
   spectrum, not the stellar continuum, is shared between orders.
2. The current text describes the injector source and a four-mode background
   as the selected model. Frozen recovery uses the 16-coefficient E13b
   background, comprising eight spatial and two temporal modes. Injector and
   recovery models must be described separately.
3. The current forward equation omits the frozen common source-curvature
   factor, native-column continuum map, fine-grid map, and exact distinction
   between source and additive background.
4. The current limb-darkening description implies twelve free knot values per
   order. NOVA-S uses six-knot deviation bases but only an offset and normalized
   log-wavelength slope for each transformed limb-darkening variable in each
   order, giving eight nonlinear coordinates total.
5. The current convergence tolerances and old V26-V30 context are superseded.
   NOVA-S uses exact outer Huber IRLS, final-weight confirmation, scale-aware
   KKT and first-order gates, and two independent deterministic starts; both
   converged at cycle 14.
6. Comparison-pipeline and group-level fairness work must be divided into what
   is already part of the frozen V45 control and what remains planned.
7. The current Methods should use the R7 common reporting support and must not
   imply calibration or scoring beyond the direct PASTASOSS training domain.

## Proposed main Methods architecture

1. **Study design and frozen model identity.** Define NOVA-S, the V45 control,
   truth isolation, and the distinction between frozen method and active
   candidates.
2. **Benchmark cube and retained detector data.** Give 229 integrations,
   event indices 51--177, 102 complement integrations, SCI/ERR/DQ selection,
   97,557 retained pixels per integration, excluded edge groups, and overlap
   summation.
3. **Detector-level forward model.** State the exact source-plus-background
   equation and define every operator.
4. **Shared transmission spectrum and transit model.** Describe the 160
   positive adaptive coefficients, separate achromatic depth and morphology,
   shared orders, fixed orbital geometry, finite-exposure integration, and
   fitted deviations around the STAGGER reference.
5. **Response, continua, uncertainties, and background.** Summarise q-star,
   the 5,440 native continuum coefficients, per-order ERR scales plus the
   truth-blind OOT QE guard, and E13b's 16 additive coefficients.
6. **OOT-only common source curvature.** Explain the 51/51 fold comparison and
   why the common factor was selected over the lower aggregate per-order score.
7. **Profiled robust optimisation and convergence.** Give the global linear
   nuisance problem, variable projection, Schur complement, bounded TRF,
   exact outer Huber IRLS, deterministic starts, and acceptance gates.
8. **Benchmark separation and fairness status.** Describe generator,
   delivery, recovery, and scoring isolation; the opaque common cube; and the
   unfinished group/rateints sensitivity experiment without presenting it as
   part of the frozen result.
9. **Reporting support and metrics.** Define the R7 common domain, absolute
   RMSE, mean bias, morphology RMSE, uncertainty diagnostics, and subregion
   reporting. Numerical performance belongs in Results, not Methods.

## Proposed NOVA appendix architecture

1. Release provenance and exact input identities.
2. Detector support and native-group bookkeeping.
3. Positive shared-spectrum parameterisation and fixed order discrepancy.
4. Exact orbital geometry, transit integration, and limb-darkening coordinates.
5. V47 q-star construction, admission gates, and known integer-coordinate
   limitation.
6. QE uncertainty guard.
7. E13b construction and OOT anchor.
8. Common source-curvature selection.
9. Exact VarPro equations, profiled derivatives, Schur complement, and
   streamed sufficient statistics.
10. Huber IRLS, deterministic starts, convergence, and prediction closure.
11. Negative-result model classes and the boundary between frozen NOVA-S and
    prospective successors.

## Proposed benchmark appendix architecture

1. V45 rateints injector equation and source-only transit modulation.
2. Generator, delivery, recovery, and scoring separation.
3. Common reporting support and R7 domain rule.
4. Fairness limitations of a rateints-only cube and the prospective paired
   group/rateints experiment.
5. Structural-neutrality, multi-visit, and noise-seed requirements.
6. Reproducibility manifests, software environment, hashes, and minimum report.

## Questions for Claude's first pass

1. Challenge the nine-part main Methods architecture. What belongs in the main
   text rather than either appendix?
2. Should the main text use "NOVA" for the general framework and "NOVA-S" only
   for the frozen implementation, or use NOVA-S throughout this ESA?
3. Which exact numerical values are essential in the main Methods, and which
   should move to a compact appendix table?
4. How prominently should the known q-star red-end limitation appear in
   Methods, given that the causal diagnosis is a result but the frozen response
   is part of the method?
5. Audit the correction list above against the handoff and identify anything
   else in the canonical Methods or appendices that is obsolete or inaccurate.
6. Identify the minimal additional bibliography entries needed for PASTASOSS,
   WebbKernel, STAGGER, jaxoplanet, and the software/reduction methods, without
   citing software merely for decoration.

