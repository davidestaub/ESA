"""Programme 4476: dilution of a 1.5% transit by the field sources that remain in the moved exposure,
per reporting bin, for a fixed 40-row extraction box. Depth error = 0.015 x field-only non-transiting light
(light-ppm) in the box; bin 109 (1.874-1.893 um) gives 108 depth-ppm. Source (local):
pid4476_testcase_20260930/checks/E_template/dilution_147bin.csv, column field_only_ppm, box_rows = 40.
Only the field-source term is shown (not the halo or sky terms, which are in light-ppm in that table)."""
import csv, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p = '/Users/davidestaub/Desktop/ICL_PHD/NOVA_ASTRA_EXECUTION_20260905_R1/products/pid4476_testcase_20260930/checks/E_template/dilution_147bin.csv'
rows = [r for r in csv.DictReader(open(p)) if r['box_rows'] == '40']
lo = np.array([float(r['lower_um']) for r in rows]); hi = np.array([float(r['upper_um']) for r in rows])
dep = 0.015 * np.array([float(r['field_only_ppm']) for r in rows])
order = np.array([int(r['order']) for r in rows])
i = np.argmax(dep); print('max', dep[i], lo[i], hi[i], 'n>10ppm-depth', int((dep > 10).sum()), 'bins', len(rows))
plt.rcParams.update({'font.family': 'serif', 'font.size': 7.5, 'axes.linewidth': 0.6})
fig, ax = plt.subplots(figsize=(3.35, 1.9))
for o, c in ((1, '#2a78d6'), (2, '#eb6834')):
    s = order == o
    ax.bar(0.5 * (lo[s] + hi[s]), dep[s], width=(hi[s] - lo[s]), color=c, edgecolor='none', label=f'order {o}')
ax.set_xlabel('Wavelength ($\\mu$m)'); ax.set_ylabel('Predicted depth dilution (ppm)')
ax.set_xlim(0.6, 2.85)
ax.grid(axis='y', color='#e6e6e6', lw=0.4)
for s in ['top', 'right']:
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=7, loc='upper left')
fig.savefig('pid4476_field_dilution.pdf', bbox_inches='tight', pad_inches=0.02)
fig.savefig('/private/tmp/claude-501/-Users-davidestaub-Desktop-ICL-PHD/3826395b-face-443e-b4ef-9d4376b4a9cf/scratchpad/dilution_preview.png', dpi=170, bbox_inches='tight')
