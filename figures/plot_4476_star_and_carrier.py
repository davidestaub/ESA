"""Programme 4476: the SOSS strip with the star at its normal position, the same strip with
the star moved 1,026 rows away (the real carrier), and the measured star (normal minus moved,
with field sources cleaned). Outlines mark the field sources found in each exposure.

Inputs (public MAST data and the local template build of 30 Sep 2026):
  NOVA_ASTRA_EXECUTION_20260905_R1/products/pid4476_testcase_20260930/inputs/*_rate.fits
  .../checks/E_template/S_clean.npy and S_clean_masks.npz (bit 2 = normal-field source;
  offset_source_excess_DNps > 0 = moved-pointing field source)
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from astropy.io import fits

root = '/Users/davidestaub/Desktop/ICL_PHD/NOVA_ASTRA_EXECUTION_20260905_R1/products/pid4476_testcase_20260930/'
N = fits.getdata(root + 'inputs/jw04476002001_03102_00001_nis_rate.fits', 'SCI')[1792:2048].astype(float)
O = fits.getdata(root + 'inputs/jw04476003001_03103_00001_nis_rate.fits', 'SCI')[1792:2048].astype(float)
S = np.load(root + 'checks/E_template/S_clean.npy')
m = np.load(root + 'checks/E_template/S_clean_masks.npz')
normal_src = (m['bitmask'] & (1 << 2)) > 0
offset_src = m['offset_source_excess_DNps'] > 0
import json
gdir = root + 'checks/I_gaia/'
gtr = np.load(gdir + 'i04_predicted_field_traces.npz'); gmeta = json.load(open(gdir + 'i04_predicted_field_traces.json'))['traces']

plt.rcParams.update({'font.family': 'serif', 'font.size': 8.5})
fig, axs = plt.subplots(3, 1, figsize=(6.3, 3.5), sharex=True)
norm = LogNorm(vmin=0.3, vmax=300)
panels = [(N, normal_src, '(a) Star at the usual position'),
          (O, offset_src, '(b) Star moved 1,026 rows lower'),
          (S, None, '(c) Cleaned image of the star')]
for ax, (img, mask, title) in zip(axs, panels):
    im = ax.imshow(np.clip(img, 0.3, None), origin='lower', aspect='auto', cmap='Greys', norm=norm,
                   extent=(-0.5, 2047.5, 1791.5, 2047.5), interpolation='nearest')
    if mask is not None:
        ax.contour(np.arange(2048), np.arange(1792, 2048), mask.astype(float), levels=[0.5],
                   colors='#eb6834', linewidths=0.7)
    lab = {0: 'N', 1: 'O'}.get(list(axs).index(ax))
    if lab is not None:
        for t in gmeta:
            if t['exposure'] == lab:
                ax.plot(gtr[t['key'] + '_x'], gtr[t['key'] + '_y'], color='#2a78d6', lw=0.8, ls=(0, (3, 2)))
        ax.set_ylim(1791.5, 2047.5)
    ax.set_title(title, fontsize=8.5, loc='left', pad=2)
    ax.set_ylabel('Row', fontsize=8)
    ax.tick_params(labelsize=7.5)
axs[-1].set_xlabel('Column')
cb = fig.colorbar(im, ax=axs, fraction=0.025, pad=0.01)
cb.set_label('DN s$^{-1}$', fontsize=8); cb.ax.tick_params(labelsize=7.5)
fig.savefig('pid4476_star_and_carrier.pdf', dpi=300, bbox_inches='tight')
fig.savefig('/private/tmp/claude-501/-Users-davidestaub-Desktop-ICL-PHD/3826395b-face-443e-b4ef-9d4376b4a9cf/scratchpad/pid4476_preview.png', dpi=150, bbox_inches='tight')
print('saved', int(normal_src.sum()), int(offset_src.sum()))
