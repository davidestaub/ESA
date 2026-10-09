"""WASP-17 b: the SOSS strip (median out-of-transit image, CLEAR) with
  - orange circles: compact sources found in the image (MVI Stage A5 detections, all 94);
  - red crosses: undispersed images of Gaia DR3 stars predicted with the fitted mapping;
  - blue plus signs: the same predicted with the a-priori ExoCTK model, without the fit.

Inputs (read only):
  products/pre1f_calibration_arrays_r1/NATIVE_PRE1F_CALIBRATION_IMAGES.npz
      background_off_control_medians[0]  (the image used by A5 for the CLEAR fit)
  products/mission_validated_injector_20260925/stageA/A5/outputs/
      A5_PREDICTED_CONTAMINANT_IMAGES.npz  background_column_DN_s (subtracted as in A5)
      A5_CONTAMINANT_TABLE_GAIA.csv        dX_sky_px, dY_sky_px, o0_x, o0_y, matched_CLEAR_det
      A5_DETECTIONS_CLEAR.csv              x, y of the detected compact sources
      a5_03_state.json                     fit_CLEAR A, T; exoctk_prior A, T
All coordinates are SUBSTRIP256 pixels; rows are shown as full-frame rows (+1792).
"""
import csv, json
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

E = '/Users/davidestaub/Desktop/ICL_PHD/NOVA_ASTRA_EXECUTION_20260905_R1/products/'
A5 = E + 'mission_validated_injector_20260925/stageA/A5/outputs/'
C = np.load(E + 'pre1f_calibration_arrays_r1/NATIVE_PRE1F_CALIBRATION_IMAGES.npz')['background_off_control_medians'][0]
P = np.load(A5 + 'A5_PREDICTED_CONTAMINANT_IMAGES.npz')
img = C - P['background_column_DN_s'][None, :]
gaia = list(csv.DictReader(open(A5 + 'A5_CONTAMINANT_TABLE_GAIA.csv')))
detall = {int(r['det']): (float(r['x']), float(r['y'])) for r in csv.DictReader(open(A5 + 'A5_DETECTIONS_CLEAR.csv'))}
# real compact sources only: the 8 detections matched to Gaia, plus the detections that A5 classified as
# 'real_source_in_both_images_no_gaia_match' (seen in CLEAR and F277W); trace residuals and
# single-image detections are not shown
matched_ids = [int(r['matched_CLEAR_det']) for r in gaia if r['matched_CLEAR_det'] not in ('', 'None')]
cls = json.load(open(A5 + 'a5_04_state.json'))['classification']['CLEAR']['unmatched_detection_categories']
real_ids = [d['det'] for d in cls if d['category'].startswith('real_source_in_both_images_no_gaia_match')]
det = np.array([detall[i] for i in matched_ids + real_ids])
s = json.load(open(A5 + 'a5_03_state.json'))
A, T = np.array(s['fit_CLEAR']['A']), np.array(s['fit_CLEAR']['T'])
A0, T0 = np.array(s['exoctk_prior']['A']), np.array(s['exoctk_prior']['T'])

D = np.array([[float(r['dX_sky_px']), float(r['dY_sky_px'])] for r in gaia])
fit = D @ A.T + T
std = D @ A0.T + T0
assert np.allclose(fit, [[float(r['o0_x']), float(r['o0_y'])] for r in gaia], atol=1e-6)

Y0 = 1792  # SUBSTRIP256 starts at full-frame row 1792, as in the programme 4476 figure
on = lambda p: (p[:, 0] > -0.5) & (p[:, 0] < 2047.5) & (p[:, 1] > -0.5) & (p[:, 1] < 255.5)
plt.rcParams.update({'font.family': 'serif', 'font.size': 8.5})
fig, ax = plt.subplots(figsize=(6.3, 1.75))
im = ax.imshow(np.clip(img, 0.3, None), origin='lower', aspect='auto', cmap='Greys',
               norm=LogNorm(vmin=0.3, vmax=300), extent=(-0.5, 2047.5, Y0 - 0.5, Y0 + 255.5),
               interpolation='nearest')
ax.scatter(det[:, 0], Y0 + det[:, 1], s=70, facecolors='none', edgecolors='#eb6834', linewidths=0.8,
           label='compact sources', zorder=3)
m = on(std)
ax.scatter(std[m, 0], Y0 + std[m, 1], s=28, marker='+', color='#2a78d6', linewidths=1.0,
           label='Gaia, standard model', zorder=4)
m = on(fit)
ax.scatter(fit[m, 0], Y0 + fit[m, 1], s=24, marker='x', color='#d62728', linewidths=1.1,
           label='Gaia, fitted mapping', zorder=5)
ax.set_xlim(-0.5, 2047.5); ax.set_ylim(Y0 - 0.5, Y0 + 255.5)
ax.set_ylabel('Row', fontsize=8); ax.set_xlabel('Column', fontsize=8)
ax.tick_params(labelsize=7.5)
ax.legend(loc='lower left', bbox_to_anchor=(0, 1.0), ncol=3, fontsize=7, frameon=False,
          handletextpad=0.3, columnspacing=1.2, borderaxespad=0.2)
cb = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.01)
cb.set_label('DN s$^{-1}$', fontsize=8); cb.ax.tick_params(labelsize=7.5)
fig.savefig('w17_gaia_mapping.pdf', dpi=300, bbox_inches='tight')
fig.savefig('w17_gaia_mapping_preview.png', dpi=200, bbox_inches='tight')
print('matched', len(matched_ids), 'real non-Gaia', len(real_ids), 'fitted on strip', int(on(fit).sum()), 'standard on strip', int(on(std).sum()))
# rms offsets of the matched Gaia predictions from their detected sources (quoted in Section 4.1)
mi = [i for i, r in enumerate(gaia) if r['matched_CLEAR_det'] not in ('', 'None')]
obs = np.array([detall[int(gaia[i]['matched_CLEAR_det'])] for i in mi])
for lab, pred in (('fitted mapping', fit), ('standard ExoCTK model as published', std)):
    d = pred[mi] - obs
    print(f'{lab}: rms {np.sqrt((d[:, 0] ** 2).mean()):.2f} columns, {np.sqrt((d[:, 1] ** 2).mean()):.2f} rows over {len(mi)} matched sources')
