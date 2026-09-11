# KEY_MAP — draft keys → repo keys (future-work section)

Verified 2026-09-11 by Claude against Crossref (`api.crossref.org`), arXiv abstract pages,
OUP/MNRAS pages and the STScI JDox site. IOP and ADS pages block automated fetches, so
volume/page data for AAS journals come from Crossref (which is the publisher-deposited record).

Status legend: **EXISTING** = already in `references.bib` (use that key, add nothing);
**VERIFIED** = located, metadata confirmed, entry written to `references.future_work.claude-v1.bib`;
**VERIFIED (claim flagged)** = the work exists and is in the .bib, but what the draft attributes to it
does not match the paper — see note; **NOT FOUND** = no entry written.

Summary: 9 EXISTING, 25 VERIFIED (of which 3 carry a claim/year flag), 0 NOT FOUND, 0 AMBIGUOUS.

| Draft key | Use this key | Status | Note (what was found) |
|---|---|---|---|
| `louie2025` | `LouieEtAl2025` | EXISTING | Louie et al. 2025, AJ 169, 86, doi:10.3847/1538-3881/ad9688 (WASP-17 b SOSS, JWST-TST DREAMS). |
| `espinoza2022` | `Espinoza2022TransitSpectroscopy` | EXISTING | transitspectroscopy, Zenodo 10.5281/zenodo.6960924. |
| `radica2024exotedrf` | `Radica2024` | EXISTING | exoTEDRF, JOSS 9(100), 6898, doi:10.21105/joss.06898. |
| `holmberg2023` | `HolmbergMadhusudhan2023` | EXISTING | MNRAS 524, 377, doi:10.1093/mnras/stad1580 (JExoRES; field-star contamination). |
| `feinstein2023` | `FeinsteinEtAl2023` | EXISTING | Nature 614, 670, doi:10.1038/s41586-022-05674-1. |
| `rackham2018` | `RackhamEtAl2018` | EXISTING | ApJ 853, 122, doi:10.3847/1538-4357/aaa08c (TLSE I, M dwarfs). |
| `darveau2022` | `DarveauBernierEtAl2022` | EXISTING | ATOCA, PASP 134, 094502, doi:10.1088/1538-3873/ac8a77. |
| `sing2016` | `SingEtAl2016` | EXISTING | Nature 529, 59, doi:10.1038/nature16068. |
| `gressier2024` | `GressierEtAl2024` | EXISTING | arXiv:2410.08149 (WASP-17 b SOSS eclipse; repo entry is arXiv-only). |
| `taylor2023` | `TaylorEtAl2023` | VERIFIED | Taylor, Radica, Welbanks et al. 2023, "Awesome SOSS: atmospheric characterization of WASP-96 b using the JWST early release observations", MNRAS 524, 817–834, doi:10.1093/mnras/stad1547, arXiv:2305.16887. Abstract: SOSS short-wavelength data "best explained by the presence of an enhanced Rayleigh scattering slope" — draft claim confirmed. |
| `wang2025` | `WangEtAl2026` | VERIFIED (year flagged) | First author IS Le-Chris Wang (with Rustamkulov, Sing, Lothringer, McCreery …). "A Comprehensive Analysis of the Panchromatic Transmission Spectrum of the Hot-Saturn WASP-96 b: Nondetection of Haze, …", AJ 171, 147 (2026), doi:10.3847/1538-3881/ae231b, arXiv:2511.16771 (Nov 2025). Published year is **2026**, so the key is WangEtAl2026; cite as "Wang et al. (2026)" (or 2025 only if citing the preprint). No-haze claim confirmed. |
| `liu2025` | `LiuEtAl2025` | VERIFIED | Liu, Rongrong; Wang; Rustamkulov; Sing 2025, "Unveiling the atmosphere of the super-Jupiter HAT-P-14 b with JWST NIRISS and NIRSpec", arXiv:2504.08903 — **arXiv-only**, no journal record found as of today. Paper text confirms: grazing (b = 1.014); SOSS saturation from NGROUP = 3 (all order-1 pixels 0.9–1.5 µm by NGROUP = 6); updated `jwst` pipeline does not reproduce the blue-end slope reported by Albert et al. 2023. Draft claims confirmed. |
| `keers2024` | `KeersEtAl2024` | VERIFIED | Spelling "Keers" is correct: Keers, Shapiro, Kostogryz, Glidden, Niraula et al. 2024, "Reliable Transmission Spectrum Extraction with a Three-parameter Limb-darkening Law", ApJL 977, L7, doi:10.3847/2041-8213/ad8b51, arXiv:2410.18617. |
| `sing2026` | `SingEtAl2026` | VERIFIED (claim to check) | Sing, Lothringer, Valenti, Allen, Bennett et al. 2026, "A JWST transiting survey of FGK stellar limb darkening: empirical evidence for quadratic laws and atmospheric model comparisons", arXiv:2609.00263 (31 Aug 2026), accepted in AJ — **arXiv-only entry** (no volume yet). NB the paper's finding is that the *quadratic* law is empirically preferred for FGK stars (~14 ppm depth bias); if the draft cites it as motivating non-quadratic laws, that is backwards. |
| `piaulet2024` | `PiauletGhorayebEtAl2024` | VERIFIED | Piaulet-Ghorayeb, Benneke, Radica et al. 2024, "JWST/NIRISS Reveals the Water-rich 'Steam World' Atmosphere of GJ 9827 d", ApJL 974, L10, doi:10.3847/2041-8213/ad6f00, arXiv:2410.03527. Abstract confirms "two transit observations with NIRISS/SOSS". |
| `rackham2019` | `RackhamEtAl2019` | VERIFIED | Rackham, Apai, Giampapa 2019, "The Transit Light Source Effect. II. … Planets Orbiting Broadly Sun-like Stars", AJ 157, 96, doi:10.3847/1538-3881/aaf892. |
| `cadieux2024` | `CadieuxEtAl2024` | VERIFIED | Cadieux, Doyon, MacDonald, Turbet, Artigau et al. 2024, ApJL 970, L2, doi:10.3847/2041-8213/ad5afa, arXiv:2406.15136 (LHS 1140 b SOSS; H2-rich rejected, N2-rich favoured at 2.3σ). |
| `gressier2026` | `GressierEtAl2026` | VERIFIED | Gressier, Cadieux, Doyon, Coulombe, Allart et al. 2026, "No Persistent Helium Absorption in LHS 1140 b: Four JWST/NIRISS SOSS Transits and Multi-epoch Stellar He I Variability", arXiv:2608.19120, submitted to ApJL — **arXiv-only entry**. Helium non-detection confirmed. |
| `bennett2026` | `BennettEtAl2026` | VERIFIED | Bennett, Katherine A.; Gascón; Lustig-Yaeger; Fu; Sing et al. 2026, "No Helium Detected in LHS 1140 b from Four JWST NIRISS/SOSS Transits", arXiv:2608.13473, submitted to AAS journals — **arXiv-only entry**. (Beware the adjacent id arXiv:2608.13470 — Radica 2026, "Strict Limits on Helium Absorption from LHS 1140 b from Four JWST NIRISS Transits" — a third independent paper on the same data; not cited by the draft.) |
| `lim2026` | `LimEtAl2026` | VERIFIED | Lim, Doyon, MacDonald, Artigau, Radica et al. 2026, "Atmospheric Reconnaissance of TRAPPIST-1 f with JWST NIRISS SOSS: No Evidence for the Transit Light Source Effect", AJ 172, 200, doi:10.3847/1538-3881/ae990a, arXiv:2608.17207. Five transits, ≥1 flare per visit, no TLSE contamination — draft claims confirmed. |
| `tsiaras2018` | `TsiarasEtAl2018` | VERIFIED | Tsiaras, Waldmann, Zingales, Rocchetto et al. 2018, "A Population Study of Gaseous Exoplanets", AJ 155, 156, doi:10.3847/1538-3881/aaaf75, arXiv:1704.05413 (30 planets, HST/WFC3). |
| `saba2025` | `SabaEtAl2025` | VERIFIED (scope flagged) | Saba, Thompson, Yip, Ma et al. 2025, "A Population Analysis of 20 Exoplanets Observed from Optical to Near-infrared Wavelengths with the Hubble Space Telescope: Evidence for Widespread Stellar Contamination", ApJS 276, 70, doi:10.3847/1538-4365/ad8c3c, arXiv:2404.15505. It IS a uniform population reanalysis (16 WFC3 + >50 STIS datasets) — but **HST only, not JWST**, and its headline is stellar contamination. Wording in the draft should not imply JWST. |
| `fournier2024` | `FournierTondreauEtAl2024` | VERIFIED | Fournier-Tondreau, MacDonald, Radica, Lafrenière et al. 2024, "Near-infrared transmission spectroscopy of HAT-P-18 b with NIRISS: disentangling planetary and stellar features in the era of JWST", MNRAS 528, 3354–3377, doi:10.1093/mnras/stad3813, arXiv:2310.14950. |
| `fournier2025` | `FournierTondreauEtAl2025` | VERIFIED | Fournier-Tondreau, Pan, Morel, Lafrenière, MacDonald et al. 2025, "Transmission spectroscopy of WASP-52 b with JWST NIRISS: water and helium atmospheric absorption, alongside prominent star-spot crossings", MNRAS 539, 422–438, doi:10.1093/mnras/staf489, arXiv:2412.17072. Note: the stellar signal here is *occulted* spot crossings (two events, ~2.4 % coverage) plus unocculted-heterogeneity modelling. |
| `taylor2025` | `TaylorEtAl2025` | VERIFIED | First author is Jake Taylor: Taylor, Radica, Chatterjee, Hammond, Meier et al. 2025, "JWST NIRISS transmission spectroscopy of the super-Earth GJ 357b, a favourable target for atmospheric retention", MNRAS 540, 3677–3692, doi:10.1093/mnras/staf894, arXiv:2505.24462. (A separate 2025 COMPASS NIRSpec/G395H GJ 357 b paper also exists — different work.) |
| `radica2024ltt` | `RadicaEtAl2024` | VERIFIED | Year is 2024: Radica, Coulombe, Taylor, Albert et al., "Muted Features in the JWST NIRISS Transmission Spectrum of Hot Neptune LTT 9779b", ApJL 962, L20, doi:10.3847/2041-8213/ad20e4, arXiv:2401.15548. Key `RadicaEtAl2024` does not clash with existing `Radica2024` (single-author exoTEDRF). |
| `schmidt2025` | `SchmidtEtAl2025` | VERIFIED | Schmidt, MacDonald, Tsai, Radica et al. 2025, "A Comprehensive Reanalysis of K2-18 b's JWST NIRISS+NIRSpec Transmission Spectrum", AJ 170, 298, doi:10.3847/1538-3881/ae019a, arXiv:2501.18477 (60 data treatments, >250 retrievals). |
| `baines2025` | `BainesEtAl2025` | VERIFIED | Baines, Carter, Espinoza, Volk, Filippazzo, Albert 2025, "Empirical Modeling of Zodiacal Backgrounds to Improve JWST NIRISS/SOSS Data Reduction", STScI technical report JWST-STScI-009046 (4 Sep 2025), arXiv:2509.08870. It is the *background* paper (zodiacal background dispersed across overlapping orders); entered as @techreport to match the existing `BainesEtAl2023Trace/Wavelength` entries. |
| `dholakia2026` | `DholakiaEtAl2026` | VERIFIED | Dholakia, Shashank; Dholakia, Shishir; Pope; Desdoigts; Ray et al. 2026, "Calibration of an Analog-to-Digital Conversion Nonlinearity in JWST/NIRISS", arXiv:2606.11983 (10 Jun 2026), submitted to PASP — **arXiv-only entry**. Flux-dependent ADC integral nonlinearity periodic in raw counts (period 1024 ADU), seen in AMI and SOSS; correctable in post-processing. Draft claim confirmed. |
| `fu2025` | `FuEtAl2025` | VERIFIED (claim flagged) | Fu, Stevenson, Sing, Mukherjee, Welbanks, Thorngren et al. 2025, "Statistical Trends in JWST Transiting Exoplanet Atmospheres", ApJ 986, 1, doi:10.3847/1538-4357/ad7bb8, arXiv:2501.02081. This is the only plausible match, but it is a trends study of **eight gas giants** (not all hot Jupiters; includes GJ 3470 b, WASP-107 b) using band-averaged feature metrics (H2O, CH4, CO2, SO2) with **cloud-free** forward models; clouds are mentioned only as a source of scatter. It does **not** establish "cloud diversity of hot Jupiters". Rephrase the draft or find a different reference. |
| `ih2021` | `IhKempton2021` | VERIFIED | Ih & Kempton 2021, "Understanding the Effects of Systematics in Exoplanetary Atmospheric Retrievals", AJ 162, 237, doi:10.3847/1538-3881/ac173b, arXiv:2106.12358 (correlated noise → overfitting, degraded retrieval accuracy). |
| `carter2024` | `CarterEtAl2024` | VERIFIED | Carter, May, Espinoza, Welbanks et al. (80 authors) 2024, "A benchmark JWST near-infrared spectrum for the exoplanet WASP-39 b", Nature Astronomy 8, 1008–1019, doi:10.1038/s41550-024-02292-x. |
| `damiano2024` | `DamianoEtAl2024` | VERIFIED | Damiano, Bello-Arufe, Yang, Hu 2024, "LHS 1140 b Is a Potentially Habitable Water World", ApJL 968, L22, doi:10.3847/2041-8213/ad5204, arXiv:2403.13265 (two transits, NIRSpec G235H + G395H, 1.7–5.2 µm). |
| `stsci2026` | `JDoxNIRSpecBOTS2026` | VERIFIED | @misc. STScI JDox page "NIRSpec BOTS Wavelength Ranges and Gaps" (title confirmed from the served HTML on 2026-09-11; the page tabulates disperser/filter combinations incl. G395H/F290LP). URL in the entry. A sibling page, "NIRSpec Dispersers and Filters" (…/nirspec-instrumentation/nirspec-dispersers-and-filters), gives the general filter/grating list; cite that one instead if the draft's numbers come from there. Table rows as served today (first cells): |

JDox BOTS wavelength table rows extracted from the saved HTML (best effort, for cross-checking the draft's numbers):

    Disperser-filter | SUB2048 | SUB1024A | SUB1024B | SUB512 or SUB512S
    G140M/F070LP | 0.70–1.27 | 0.70 – 1.22 | 1.22 – 1.27 | 1.22 – 1.27
    G140H/F070LP | 0.82 – 1.27 | 0.82 – 1.07 | 1.07 – 1.27 | 1.07 – 1.19
    G140M/F100LP | 0.97 – 1.87 | 0.97 – 1.22 | 1.22 – 1.87 | 1.22 – 1.55
    G140H/F100LP | 0.97 – 1.31, 1.35 – 1.83 | 0.97 – 1.07 , 1.59 – 1.83 | 1.07 – 1.31 , 1.35 – 1.59 | 1.07 – 1.19, 1.47 – 1.59
    G235M/F170LP | 1.66 – 3.12 | 1.66 – 2.03 | 2.03 – 3.12 | 2.03 – 2.58
    G235H/F170LP | 1.66 – 2.20, 2.27 – 3.07 | 1.66 – 1.79 , 2.67 – 3.07 | 1.79 – 2.20 , 2.27 – 2.67 | 1.79 – 2.00, 2.47 – 2.67
    G395M/F290LP | 2.87 – 5.18 | 2.87 – 3.35 | 3.35 – 5.18 | 3.35 – 4.27
    G395H/F290LP | 2.87 – 3.72, 3.82 – 5.18 | 2.87 – 3.03 , 4.51 – 5.18 | 3.03 – 3.72 , 3.82 – 4.51 | 3.03 – 3.38, 4.17 – 4.51
    PRISM/CLEAR | 0.60 – 5.30 | N/A † | 0.60 – 5.30 | 0.60 – 5.30

## Key-collision check

`bibtex` was run on `\nocite{*}` of the new file alone (25 items) and on the new file together with a
scratch copy of `references.bib` (85 items, i.e. 60 + 25). No duplicate-key warnings, no errors.
Potential near-misses that are NOT collisions: `RadicaEtAl2024` vs existing `Radica2024`; `GressierEtAl2026`
vs existing `GressierEtAl2024`; `BainesEtAl2025` vs existing `BainesEtAl2023Trace/Wavelength`;
`SingEtAl2026` vs existing `SingEtAl2016`; `TaylorEtAl2023/2025` (none existing).

## Entries that are arXiv-only today (may gain journal metadata later)

`LiuEtAl2025` (2504.08903), `SingEtAl2026` (2609.00263, accepted AJ), `GressierEtAl2026` (2608.19120),
`BennettEtAl2026` (2608.13473), `DholakiaEtAl2026` (2606.11983, submitted PASP), `BainesEtAl2025` (tech report + 2509.08870).

## Style notes

Author lists follow the repo pattern: first three authors + `and others` when the paper has more than four authors,
full list otherwise. Accents are LaTeX-escaped (`Ren{\'e}`, `Bj{\"o}rn`, …); the file is pure ASCII.
Existing repo entries are inconsistent on this (e.g. `Loic` vs `Lo{\"i}c`); the new entries use the accented forms.
