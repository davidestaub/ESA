"""Schematic of the 4476 benchmark construction (Section 4, Eq. 4476), drawn with thumbnails of the real
images: normal exposure N minus moved exposure O gives, after cleaning, the declared image of the star S;
photon arrivals from S are drawn for successive time intervals and added to the raw reads of O; the
transit case keeps a fraction r(t) of the photons, the copy without the transit keeps them all. The light curve is schematic.
Inputs (local): pid4476_testcase_20260930/inputs/*_rate.fits, checks/E_template/S_clean.npy."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from astropy.io import fits
root = '/Users/davidestaub/Desktop/ICL_PHD/NOVA_ASTRA_EXECUTION_20260905_R1/products/pid4476_testcase_20260930/'
N = fits.getdata(root + 'inputs/jw04476002001_03102_00001_nis_rate.fits', 'SCI')[1792:2048].astype(float)
O = fits.getdata(root + 'inputs/jw04476003001_03103_00001_nis_rate.fits', 'SCI')[1792:2048].astype(float)
S = np.load(root + 'checks/E_template/S_clean.npy')
norm = LogNorm(vmin=0.5, vmax=300)
plt.rcParams.update({'font.family': 'serif', 'font.size': 7.5})
fig = plt.figure(figsize=(6.3, 2.05))
W, H, y0 = 0.205, 0.30, 0.55
boxes = [(0.0, 'normal exposure $N$\n(star + background)', N), (0.265, 'moved exposure $O$\n(background and field stars)', O), (0.53, 'cleaned, smoothed star $S$\n($N-O$, field sources removed)', S)]
for x, lab, img in boxes:
    ax = fig.add_axes([x, y0, W, H]); ax.imshow(np.clip(img, 0.5, None), origin='lower', aspect='auto', cmap='Greys', norm=norm)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_title(lab, fontsize=7, pad=2)
fig.text(0.233, y0 + H / 2, '$-$', fontsize=12, ha='center', va='center')
fig.text(0.498, y0 + H / 2, '$\\rightarrow$', fontsize=12, ha='center', va='center')
fig.text(0.875, y0 + H / 2 + 0.05, 'photons drawn\nfrom $S$ for each\ninterval between\ntwo reads', fontsize=6.6, ha='center', va='center')
fig.text(0.875, y0 + H / 2 - 0.17, 'added as charge\nto the reads of $O(t)$', fontsize=6.6, ha='center', va='center')
fig.text(0.768, y0 + H / 2, '$\\rightarrow$', fontsize=12, ha='center', va='center')
# light curves
ax = fig.add_axes([0.08, 0.06, 0.86, 0.26])
t = np.linspace(-1, 1, 400)
r = np.where(np.abs(t) < 0.35, 1 - 0.015 * np.clip((0.35 - np.abs(t)) / 0.07, 0, 1), 1.0)
ax.plot(t, np.ones_like(t), color='#eb6834', lw=1.4, label='copy without the transit: keeps all photons ($r=1$)')
ax.plot(t, r, color='#2a78d6', lw=1.4, label='transit case: keeps a fraction $r(t)$ of the same photons')
ax.axvspan(-1, -0.35, color='#f0f0f0', zorder=0); ax.axvspan(0.35, 1, color='#f0f0f0', zorder=0)
ax.text(-0.67, 0.9915, '$r=1$', fontsize=6.8, ha='center', color='#555555'); ax.text(0.67, 0.9915, '$r=1$', fontsize=6.8, ha='center', color='#555555')
ax.set_ylim(0.982, 1.004); ax.set_xlim(-1, 1); ax.set_yticks([]); ax.set_xticks([])
ax.set_xlabel('time (schematic)', fontsize=7); ax.set_ylabel('stellar factor $r(t)$', fontsize=6.6)
for s in ['top', 'right']:
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=6.8, loc='lower center', ncol=2, bbox_to_anchor=(0.5, 0.98))
fig.savefig('pid4476_construction.pdf', bbox_inches='tight', pad_inches=0.02, dpi=300)
fig.savefig('/private/tmp/claude-501/-Users-davidestaub-Desktop-ICL-PHD/3826395b-face-443e-b4ef-9d4376b4a9cf/scratchpad/construction_preview.png', dpi=170, bbox_inches='tight')
print('saved')
