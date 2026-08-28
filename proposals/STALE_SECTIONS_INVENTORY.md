# Inventory of stale canonical sections (for Davide's scope ruling)

Joint document. claude covers the abstract, the research plan, and the
conclusions; chatgpt appends the Results half (what the handoff's results
material supports and what a replacement Results section should contain).
This is an inventory, not a rewrite: no canonical section outside the
Methods package changes until Davide authorises it.

## Abstract (`sections/00_abstract.tex`) — claude

1. "In one opened synthetic case, NOVA recovered the common R=100 spectrum
   more accurately than the Ahsoka comparison, but NOVA did not satisfy
   the strict convergence criteria and the result is not science ready."
   Stale: the evaluated release satisfies the full acceptance policy
   (both deterministic starts converged and agree) and carries certified
   scores on the calibrated reporting domain. The sentence describes the
   pre-freeze state and now contradicts the Methods.
2. "has identified instrument-response support and source-background
   allocation as the main limitations": superseded. The red-end causal
   audits attribute the supported bias specifically to the response
   amplitude of the adopted spatial response; the abstract should carry
   the sharper, current statement.
3. The closing programme sentence does not reflect the current plan
   (paired group-stage fairness experiment, the constrained
   response-amplitude repair, multi-visit admission).
4. Register: "strict convergence criteria" and "science ready" are
   process vocabulary by the standard Davide has now set.

## Research plan (`sections/04_discussion_future.tex`) — claude

1. WP1, "to be completed by 30 September 2026: finish the
   response-consistent injector, obtain strict multistart convergence for
   NOVA, and close the initial WASP-17 b benchmark": these milestones are
   achieved and certified. WP1 must be rewritten around what actually
   remains: the paired group-stage and integration-stage fairness
   experiment, the constrained flux-conserving response-amplitude repair
   evaluated on a new hidden case, and the preregistered benchmark
   matrix.
2. The Gantt bar "Injector and strict NOVA" (2026 Q3) and the dependency
   sentence "the response-consistent injector and strict NOVA convergence
   precede the headline comparison" present completed work as future,
   contradicting the section's "future work only" framing.
3. WP2's second comparison track, passing all pipelines' extracted
   products to a common light-curve fitter, exists here but not in the
   handoff's current programme. During the Methods round this promise was
   removed from the Methods precisely because the handoff does not commit
   to it. Davide must decide: keep it as a plan (it stays here, its
   natural home) or retire it.
4. "current opened case" language conflicts with a sealed, certified
   case; "response-aware source" and similar pre-freeze vocabulary needs
   the register pass.
5. The risks subsection still names generic "instrument response
   accuracy" as the main risk; it should reference the specific,
   already-identified response-amplitude defect and its constrained
   repair path, which changes the risk from unknown to characterised.

## Conclusions (`sections/05_conclusions.tex`) — claude

1. "combines a realistic detector-level injector with NOVA, a joint
   detector-level forward model for the stellar transit, overlapping SOSS
   orders, instrument response, and additive background": carries both
   overclaims corrected in the abstract on 2026-08-26 ("realistic"; the
   response listed as if fitted). Should mirror the corrected abstract
   and the new Methods (response propagated, not fitted).
2. "the lower NOVA error was obtained by a fit that did not satisfy all
   convergence requirements": stale; contradicts the certified release.
3. "Response support and source-background allocation ... are the main
   current limitations": superseded by the causal red-end attribution,
   as in the abstract.
4. "improved accuracy and robustness have not yet been demonstrated
   across a fair preregistered ensemble": directionally still true
   (single visit, single certified case) and worth keeping, but it must
   be restated against the certified result and the calibrated reporting
   domain rather than against a failed fit.
5. Register pass needed throughout.

## Results (`sections/03_results.tex`) — chatgpt

### What is stale or misleading

1. The opening freeze date, `science_ready=0`, and the statement that the
   selected fit failed strict convergence describe the pre-release state.
   NOVA-S Science R1 is now frozen, and its two independent deterministic
   starts both satisfied the final-weight-confirmed convergence policy at
   robust cycle 14.
2. The tables centred on V28-R2, V30-R8, and the 281.873 ppm opened NOVA
   result are development history, not the current result. They may remain
   only as a compact progression or negative-result table, clearly separated
   from the frozen release.
3. The current Ahsoka comparison (756.498 ppm absolute RMSE on the opened
   rateints case) is not superseded as a historical diagnostic, but it cannot
   support the paper's headline cross-method claim. Ahsoka's characteristic
   group-level 1/f correction could not run on a rateints-only cube, and the
   paired group-stage/rateints fairness experiment is incomplete.
4. “Response support and source-background allocation” is now too broad a
   diagnosis. The supported red-end bias has been localised to a deterministic
   Order-1 response mismatch dominated by the frozen V47 spatial response.
   Noise, optimiser failure, limb darkening, source curvature, background
   cancellation, red field stars, and Order-2 overlap have been tested and do
   not explain the effect.
5. The injector-status subsection predates the frozen V45 control and the
   current fairness programme. V45 remains the reproducible control; the
   group-stage/rateints candidate, scene repair, full pipeline matrix,
   multi-seed ensemble, and multi-visit evaluation remain unfinished.

### Results supported by the handoff

1. **Frozen paper-domain result.** On the R7 calibrated PASTASOSS domain,
   NOVA-S has 115.973387 ppm absolute RMSE, +8.828131 ppm mean bias, and
   115.636891 ppm morphology RMSE over 141 common R=100 bins. The final fully
   retained bin ends at approximately 2.740018 micrometres. The historical
   143-bin release scores (117.830915, +6.822111, and 117.633258 ppm) are
   provenance and must not be mixed with the R7 headline domain.
2. **Convergence.** Both deterministic starts converged independently at cycle
   14 under the prospective detector-space criteria. Truth was read only after
   the detector prediction was fixed, and truth RMSE was not the optimisation
   objective.
3. **Order-resolved performance.** On the historical release domain, Order 1
   morphology was 98.438905 ppm over 0.90--2.60 micrometres excluding the gap,
   Order 2 morphology below 0.84 micrometres was 61.310061 ppm, and the broad
   Order-1-minus-Order-2 mean bias was -8.359508 ppm. These numbers must be
   labelled with their 143-bin-domain provenance rather than combined with R7
   metrics.
4. **Causal red-end audit.** Matched noiseless self-closure is approximately
   1.3 ppm in the red, whereas the noiseless V45 fair-injector flat retains
   -299.07 ppm red bias. The operator split assigns -167.36 ppm before full
   inversion and -131.72 ppm after projection through the nuisance model and
   nonlinear transit inversion. The V47 response has a median attribution
   share of 0.999993, a median centroid mismatch of 0.234 pixel, and a response
   amplitude approximately 0.9--1.9 per cent too high in the faint red columns.
   This supports deterministic forward-model mismatch, not a VarPro or
   convergence failure.
5. **Overlap negative result.** Only 2.145 per cent of the red event signal is
   delivered through Order 2. Removing it makes the decrement-depth ratio
   worse, from 0.98906 to 0.98190, so overlap mitigates roughly 110 ppm of the
   bias rather than causing it. Recovery-side explicit overlap modelling was
   therefore not promoted.
6. **Candidate-response results.** V51 improved red morphology but degraded
   Order 2 and the headline RMSE. V54-R2 improved R7 morphology to approximately
   110.77 ppm but introduced approximately -38 ppm bias and failed the complete
   promotion gates. These are informative negative results, not successors to
   NOVA-S.
7. **Injector evidence and limitation.** The modern per-order rebuild is
   numerically equivalent to V45 when no new scene masks are applied (relative
   L1 difference 2.8458e-15; maximum absolute difference 5.55e-14). The current
   broad scene exclusion removes 9.8836 per cent of target signal, compared
   with 0.4326 per cent removed by the R7 calibrated-domain rule, and must be
   repaired before promotion.

### Concrete replacement structure

1. **Frozen NOVA-S recovery:** state convergence first, then give the R7
   headline metrics and reporting domain; place the historical 143-bin values
   in a short provenance sentence or table.
2. **Where the residual error lies:** show the recovered and injected spectra
   with residuals, order attribution, and the calibrated-domain boundary, then
   report the order-resolved metrics without mixing domains.
3. **Why the red residual remains:** present the matched-self-closure versus
   fair-injector closure, operator split, and response-amplitude/centroid audit
   as one causal chain. A compact audit figure is preferable to a catalogue of
   branch names.
4. **Alternatives tested:** summarise overlap modelling and the V51/V54-R2
   candidates as negative results, explaining which global gate each failed.
   The longer development history belongs in the NOVA appendix.
5. **Benchmark status:** retain the opened Ahsoka comparison only if Davide
   wants it as historical screening evidence. It must be labelled as a
   rateints-stage diagnostic and not as the fair pipeline comparison. State
   plainly that the paired group-stage test and multi-pipeline scores are not
   yet available.
6. **Current evidential boundary:** end with what is established (a converged,
   frozen single-case NOVA-S recovery and a causal response diagnosis) and what
   is not (pipeline superiority, multi-visit generality, calibrated uncertainty,
   or improved atmospheric inference on real data). This provides the handoff
   to the research plan without returning to pre-release language.
