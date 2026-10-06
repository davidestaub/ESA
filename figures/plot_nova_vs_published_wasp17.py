"""Preliminary NOVA transmission spectrum of the real WASP-17 b visit (18 Sep 2026 reference
reduction; conditional Gauss-Newton errors) next to the published Ahsoka spectrum of
Louie et al. (2025), R = 100, orders 1 and 2 plotted separately.

Inputs: NOVA_ASTRA_EXECUTION_20260905_R1/outputs/four_spectra_20260924_r1/WASP17_FOUR_SPECTRA/
03_REAL_WASP17_NOVA_PRELIMINARY.csv and 04_REAL_WASP17_AHSOKA_PUBLISHED.csv (unmodified).
Lower panel: NOVA minus Ahsoka interpolated to NOVA's bin centres, with regional medians; one point near
2.06 um (interpolated onto a published point far below its neighbours) is drawn at the top edge with its value.
"""
import csv, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

d = '/Users/davidestaub/Desktop/ICL_PHD/NOVA_ASTRA_EXECUTION_20260905_R1/outputs/four_spectra_20260924_r1/WASP17_FOUR_SPECTRA/'
nova = list(csv.DictReader(open(d + '03_REAL_WASP17_NOVA_PRELIMINARY.csv')))
ahs = list(csv.DictReader(open(d + '04_REAL_WASP17_AHSOKA_PUBLISHED.csv')))
nl = np.array([(float(r['lower_um']) + float(r['upper_um'])) / 2 for r in nova])
nd = np.array([float(r['depth_ppm']) for r in nova]); ne = np.array([float(r['depth_error_ppm']) for r in nova])
A = {o: np.array([[float(r['wavelength_um']), float(r['depth_ppm']), float(r['depth_error_ppm'])]
                  for r in ahs if r['order'] == str(o)]) for o in (1, 2)}
for o in (1, 2):
    A[o] = A[o][np.argsort(A[o][:, 0])]

# regional mean differences: order 1 above 0.85 um, order 2 below
interp = np.where(nl >= 0.86, np.interp(nl, A[1][:, 0], A[1][:, 1], left=np.nan, right=np.nan),
                  np.interp(nl, A[2][:, 0], A[2][:, 1], left=np.nan, right=np.nan))
for lo, hi in [(0.63, 1.0), (1.0, 1.6), (1.6, 1.8), (1.8, 2.3), (2.3, 2.81), (0.63, 2.81)]:
    s = (nl >= lo) & (nl < hi) & np.isfinite(interp)
    print(f'{lo:.2f}-{hi:.2f} um: n={s.sum():3d}  mean NOVA-Ahsoka = {np.mean(nd[s]-interp[s]):+7.0f} ppm')

plt.rcParams.update({'font.family': 'serif', 'font.size': 7.5, 'axes.linewidth': 0.6})
fig, (ax, ax2) = plt.subplots(2, 1, figsize=(6.3, 3.5), sharex=True, gridspec_kw=dict(height_ratios=[2.2, 1], hspace=0.08))
for o, mk in ((1, 'o'), (2, 's')):
    ax.errorbar(A[o][:, 0], A[o][:, 1], yerr=A[o][:, 2], fmt=mk, ms=2.2, lw=0.6, color='#eb6834',
                label=f'Ahsoka, published (order {o})', zorder=2, alpha=0.9)
ax.errorbar(nl, nd, yerr=ne, fmt='o', ms=2.2, lw=0.6, color='#2a78d6', label='NOVA, preliminary', zorder=3)
ax.set_ylabel('Transit depth (ppm)')
diff = nd - interp
ax2.axhline(0, color='#888888', lw=0.6)
top = 1100.0
ax2.plot(nl[diff <= top], diff[diff <= top], 'o', ms=1.8, color='#555555', zorder=2)
for x_, y_ in zip(nl[diff > top], diff[diff > top]):
    ax2.plot([x_], [top * 0.97], '^', ms=3.0, color='#555555', zorder=2)
    ax2.annotate(f'{y_:.0f}', (x_, top * 0.97), xytext=(4, -3), textcoords='offset points', fontsize=6.3, color='#555555')
ax2.set_ylim(-100, top)
for lo, hi in [(0.63, 1.0), (1.0, 1.6), (1.6, 1.8), (1.8, 2.3), (2.3, 2.81)]:
    sel = (nl >= lo) & (nl < hi) & np.isfinite(diff)
    ax2.plot([lo, hi], [np.median(diff[sel])] * 2, color='#2a78d6', lw=1.6, zorder=3)
ax2.set_ylabel('NOVA $-$ published' + chr(10) + '(ppm)')
ax2.set_xlabel(r'Wavelength ($\mu$m)')
ax2.grid(axis='y', color='#e3e3e3', lw=0.5, zorder=0)
for s_ in ['top', 'right']:
    ax2.spines[s_].set_visible(False)
ax.grid(axis='y', color='#e3e3e3', lw=0.5, zorder=0)
for s in ['top', 'right']:
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=7, loc='lower left', bbox_to_anchor=(0, 1.0), ncol=3)
fig.savefig('nova_vs_published_wasp17_preliminary.pdf', bbox_inches='tight', pad_inches=0.02)
fig.savefig('/private/tmp/claude-501/-Users-davidestaub-Desktop-ICL-PHD/3826395b-face-443e-b4ef-9d4376b4a9cf/scratchpad/nova_real_preview.png', dpi=160, bbox_inches='tight')
print('saved')
