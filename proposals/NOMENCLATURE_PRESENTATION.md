# NOVA nomenclature extracted from Davide's group presentation

Extracted 2026-08-28 from `NOVA_group_presentation_reduced_size.html`
(20 slides, rendered and read slide by slide). Davide's directive: the ESA
Methods and appendix must stick as close as possible to this notation. The
presentation predates some changes, so the HANDOFF remains the factual truth
for what the frozen method does; this document fixes only the SYMBOLS.

## Master forward model (slides 11, 12, 15, 17)

For integration t and pixel p, with g = g(p) the wavelength group of pixel p
and P_g the pixels of group g:

    Yhat_tp = C_tg * T_tg(D_g, u_g; Omega) * qstar_pg + B_tp

- C_tg = beta_0g + beta_1g * tau_t   (continuum: level + slope per group;
  tau_t is the normalised time coordinate; 2 coefficients per group)
- T_tg: exposure-integrated transit factor (calligraphic T in the slides);
  T = 1 outside transit, T < 1 during transit
- qstar_pg: fixed spatial fraction, normalised Sum_{p in P_g} qstar_pg = 1
- B_tp = Sum_{k=1..8} Phi_pk [ alpha_k0 + alpha_k1 * G1(t) ]
  (8 fixed spatial maps Phi_k; temporal patterns G0(t)=1 and G1(t);
  16 coefficients alpha_km)
- Generalised overlap-ready form (slide 17):
  Yhat_tp = Sum_{g in G(p)} qstar_pg F_tg(theta) (beta_g0 + tau_t beta_g1)
            + Sum_k Sum_m Phi_pk T_tm alpha_km
- Inverse-problem framing (slide 11): forward map F, inverse map I;
  fitted quantities carry hats (Dhat(lambda), uhat, Chat, Bhat).

## Transit model (slide 13)

- Omega = (P, a/R_star, e, omega_peri, b, t0)  — fixed orbital parameters
- D_g = D(lambda_g); u_g = (u_{1,g}, u_{2,g})
- T_g^inst(s; D_g, u_g, Omega): light remaining at one instant
  (limb-darkened occultation integral; computed with jaxoplanet)
- T_tg = exposure average of T_g^inst over [t^-, t^+], evaluated with
  21 weighted model evaluations: T_tg ~ (1/2) Sum_{j=1..21} w_j T^inst(s_tj)

## Q-star estimation (slide 14)

Per-pixel weighted linear fit on the public cube:

    Y_tp = A_pg * phi_tg + m_p + n_p * tau_t + eps_tp

- phi_tg: fixed, shared transit timing + shape template (depth-free)
- A_pg: fitted transit-correlated amplitude in pixel p; m_p level;
  n_p tau_t drift
- qstar_pg = A_pg / Sum_{p' in P_g} A_p'g   (unit sum per group)
- Motto: "the transit reveals where the starlight lands";
  "instrument background does not follow the transit template".

## Background estimation (slide 15)

- Spatial basis Phi_pk selected by hold-out on off-trace pixels
  ("stellar trace masked, held-out band, hold out -> predict").
- Per-integration amplitudes: ahat_t = arg min_a Sum_{p in off}
  (Y_tp - Sum_k Phi_pk a_tk)^2 / sigma_tp^2, giving A = [ahat_tk] (229 x 8);
  centred A_c = U Sigma V^T; G1(t) = first principal component with
  |corr(U_j, phi_t)| <= 0.25.
- alphahat_off = arg min_alpha (ERR-weighted LS over all t, valid p in off);
  "estimate + uncertainty saved as a data-derived prior for the inverse
  fit"; N_off: fixed off-trace precision.

## Complete objective (slide 16)

    r_tp = [ Y_tp - Yhat_tp(D, u, beta, alpha, Delta ; qstar, Omega) ] / sigma_tp

(semicolon separates fitted parameters from frozen inputs)

    (Dhat, uhat, betahat, alphahat, Deltahat) =
      arg min_{D,u,beta,alpha,Delta} {
          Sum_{(t,p) in M} rho_1.345( r_tp )            <- detector mismatch
        + 1/2 (alpha - alpha_off)^T N_off (alpha - alpha_off)
                                                        <- off-trace anchor
        + 1/2 ||r_LD,theory(u)||^2 + 1/2 ||r_LD,curv(u)||^2
                                                        <- limb darkening
        + 1/2 ||r_order(Delta)||^2 }                    <- order discrepancy

- M: the retained sample mask; rho_1.345: Huber loss
- Order discrepancy sign convention: order 1 sees D(lambda) + Delta,
  order 2 sees D(lambda) - Delta. (In NOVA-S, Delta is pinned to zero.)

## Nested solver (slides 17, 18)

- theta = (D, u, Delta) nonlinear; (beta, alpha) linear
- min_theta TRF [ min_{beta,alpha} VARPRO  Q_w^(l)(theta, beta, alpha) ]
- VARPRO: (betahat, alphahat) = arg min [ 1/2 Sum w_tp/sigma_tp^2
  (Y_tp - Yhat_tp)^2 + 1/2 (alpha - alphahat_off)^T N_off (...) ];
  "linear least squares -> SVD -> exact inner minimum"
- TRF: r_prof(theta_k + s; w^(l)) ~ r_k + J_k s; bounded trust-region
  subproblem with region Delta_k, ratio rho_k = actual/predicted, shrink
  0.25x / grow 2x rules; scaled coordinates; SVD of J_k.
- Huber-IRLS: e_tp^(l) = (Y_tp - Yhat_tp^(l))/sigma_tp;
  w_tp^(l+1) = min(1, 1.345/|e_tp^(l)|); w frozen during each TRF solve;
  at most 50 cycles.
- Slide-18 stop tolerances: gtol = 1e-6 (gradient), ftol = 1e-9 (cost),
  xtol = 1e-8 (step). NOTE: reconcile with the handoff's convergence-gate
  numbers from the frozen configuration before using either set.
- Starts theta_A (zero morphology) and theta_B (deterministic
  perturbation); final selection s_star = arg min_{s in {A,B}} L_star_s.

## Injector (slide 20)

    Yinj_tp = YOOT_tp + [ A_1 { s_t ⊙ (Ttrue_t - 1) } ]_p
                       + [ A_2 { s_t ⊙ (Ttrue_t - 1) } ]_p

- YOOT: 229 authenticated OOT integrations ("real background, real noise,
  known transit"); s_t: target-source expectation; Ttrue_t: known injected
  transit factor; A_o: per-order detector projection operator;
  Dinj(lambda): injected spectrum.

## Reconciliation notes (presentation vs current frozen method)

1. g is the GROUP INDEX in the presentation. The handoff's common
   source-curvature factor "g(t)" therefore needs a different symbol in the
   ESA; suggest gamma_t (it multiplies only the C*T source bundle).
2. The presentation's recovery model has no explicit response operator R_o
   or fine-grid map Psi_o: response structure appears as qstar_pg within
   groups plus the group mapping itself. The ESA text should keep the
   per-pixel group form and describe the PASTASOSS/WebbKernel geometry and
   kernel as what defines the groups, wavelength assignment, and qstar
   support, rather than introducing new operator symbols.
3. beta (continua) and alpha (background) match the adopted Methods
   notation already; sigma_tp, N_off, alpha_off also match.
4. The presentation fits Delta (order discrepancy); NOVA-S pins it to
   numerical zero. Keep the symbol, state the pin.
5. Slide-18 tolerances vs handoff gates must be reconciled from the frozen
   configuration (both sets quoted above).
