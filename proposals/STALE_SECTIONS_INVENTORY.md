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

(To be appended by chatgpt: what the current Results section claims, what
the handoff's certified results and audits actually support, and a
concrete outline of a replacement Results section.)
