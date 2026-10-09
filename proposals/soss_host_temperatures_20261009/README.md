# SOSS exoplanet host temperatures (queried 2026-10-09 UTC)

Source of the ESA §4.4 sentence: "At 7,548 K, the star is also hotter than 50 of the 51 exoplanet hosts that SOSS had observed by October 2026, whose median temperature is 4,870 K."

- `soss_exoplanet_hosts_teff.csv`: one row per host (51 executed, 23 planned-only), with programmes, Teff (NASA Exoplanet Archive pscomppars st_teff) and status. First agent.
- `soss_exoplanet_observations.csv`: one row per observation. First agent.
- `soss_exoplanet_hosts_teff_check2.csv` (if present): the independent checker's table, which reproduced the counts (51 executed hosts; only WASP-189, 8000 K, hotter than 7548 K; median 4870 K).
- `query_log.jsonl`: every MAST (Mast.Caom.Filtered, Mast.Jwst.Filtered.Niriss with exp_type NIS_SOSS) and Exoplanet Archive TAP request, with timestamps.

"Executed" means real NIS_SOSS science exposures of at least 1 h in MAST. Calibration-only stars, brown dwarfs and sky fields are excluded (listed in the workflow result). The benchmark star's 7548 K is TIC v8.2 (TIC 219102650).
