"""Programme 4476: median cross-dispersion profiles, across the trace of order 1, of the normal exposure,
the moved exposure (real background at the same pixels) and the cleaned image of the star, in three
wavelength bands. Shows that the star's light far from the trace is measured, down to below the sky level.

Inputs (local): pid4476_testcase_20260930/inputs/*_rate.fits (public MAST data),
checks/E_template/S_clean.npy and S_clean_masks.npz (far_model_weight), checks/A_static/traces_measured.npz
(order-1 centre per column, yfitN_o1). Band edges and wavelengths as in checks/E_template/figures/E4.
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from astropy.io import fits

root = '/Users/davidestaub/Desktop/ICL_PHD/NOVA_ASTRA_EXECUTION_20260905_R1/products/pid4476_testcase_20260930/'
N = fits.getdata(root + 'inputs/jw04476002001_03102_00001_nis_rate.fits', 'SCI')[1792:2048].astype(float)
O = fits.getdata(root + 'inputs/jw04476003001_03103_00001_nis_rate.fits', 'SCI')[1792:2048].astype(float)
S = np.load(root + 'checks/E_template/S_clean.npy')
fw = np.load(root + 'checks/E_template/S_clean_masks.npz')['far_model_weight']
yc = np.load(root + 'checks/A_static/traces_measured.npz')['yfitN_o1'] - 1792   # order-1 centre, strip rows

bands = [((1661, 1789), '1.08–1.20 $\\mu$m'), ((1279, 1406), '1.45–1.57 $\\mu$m'), ((131, 259), '2.58–2.70 $\\mu$m')]
d = np.arange(-50, 201)
plt.rcParams.update({'font.family': 'serif', 'font.size': 7.5, 'axes.linewidth': 0.6})
fig, axs = plt.subplots(1, 3, figsize=(6.3, 2.2), sharey=True)
for ax, ((c0, c1), lab) in zip(axs, bands):
    prof = {k: [] for k in 'NOSWT'}
    for c in range(c0, c1 + 1):
        rows = np.round(yc[c] + d).astype(int)
        ok = (rows >= 4) & (rows < 252)          # exclude the reference rows at both strip edges
        for k, img in (('N', N), ('O', O), ('S', S), ('W', fw), ('T', N - O)):
            v = np.full(d.size, np.nan); v[ok] = img[rows[ok], c]; prof[k].append(v)
    med = {k: np.nanmedian(np.array(v), axis=0) for k, v in prof.items()}
    model = med['W'] > 0.5
    ax.plot(d, med['N'], color='#888888', lw=1.0, label='normal exposure')
    ax.plot(d, med['T'], color='#222222', lw=0.6, label='difference (measured)')
    ax.plot(d, med['O'], color='#eb6834', lw=1.0, label='moved exposure (background)')
    ax.plot(d, np.where(~model, med['S'], np.nan), color='#2a78d6', lw=1.4, label='cleaned source')
    ax.plot(d, np.where(model, med['S'], np.nan), color='#2a78d6', lw=1.4, ls=(0, (3, 1.5)), label='cleaned source, far-wing model')
    ax.set_yscale('asinh', linear_width=0.3); ax.set_ylim(-0.5, 2000)
    ax.set_yticks([0, 1, 10, 100, 1000]); ax.set_yticklabels(['0', '1', '10', '100', '1000']); ax.minorticks_off(); ax.set_xlim(-50, 200); ax.set_xticks([0, 50, 100, 150])
    ax.set_title(lab, fontsize=7.5, pad=2)
    ax.set_xlabel('Rows from the centre of order 1')
    ax.grid(color='#e6e6e6', lw=0.4)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
axs[0].set_ylabel('Count rate (DN s$^{-1}$)')
axs[0].legend(frameon=False, fontsize=6.2, loc='lower left', bbox_to_anchor=(0.0, 1.08), ncol=5, columnspacing=0.8, handlelength=1.8)
for ax, pk in zip(axs, [[(165, 'order 2')], [(90, 'order 2')], [(65, 'order 3'), (148, 'order-4 band')]]):
    for x_, t_ in pk:
        ax.text(x_, 1300, t_, fontsize=6.3, ha='center', color='#444444')

fig.subplots_adjust(left=0.08, right=0.99, bottom=0.2, top=0.8, wspace=0.08)
fig.savefig('pid4476_profiles.pdf', bbox_inches='tight', pad_inches=0.02)
fig.savefig('/private/tmp/claude-501/-Users-davidestaub-Desktop-ICL-PHD/3826395b-face-443e-b4ef-9d4376b4a9cf/scratchpad/profiles_preview.png', dpi=170, bbox_inches='tight')
print('saved')
