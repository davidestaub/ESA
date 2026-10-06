"""Regional mean recovery error of NOVA and exoTEDRF on the reference atmosphere,
under the lower and the upper estimate of the starlight in the WASP-17 b injector.

Source of every number: NOVA_ASTRA_EXECUTION_20260905_R1/reports/OVERNIGHT_CLAUDE_LOG_20260925.md,
lines 100-117 (regional mean errors; RMSE 124.0/319.1 lower, 358.1/150.2 upper).
Error = recovered minus injected depth, so positive means too deep.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

edges = [0.63, 1.0, 1.6, 1.8, 2.1, 2.3, 2.5, 2.81]
err = {
    ('NOVA', 'lower'): [38, 55, 12, 20, 112, 112, 8],
    ('NOVA', 'upper'): [107, 99, 220, 359, 603, 744, 726],
    ('exoTEDRF', 'lower'): [-94, -108, -256, -532, -481, -456, -535],
    ('exoTEDRF', 'upper'): [-39, -68, -56, -208, -20, 149, 162],
}
rmse = {('NOVA', 'lower'): 124, ('NOVA', 'upper'): 358, ('exoTEDRF', 'lower'): 319, ('exoTEDRF', 'upper'): 150}
colour = {'NOVA': '#2a78d6', 'exoTEDRF': '#eb6834'}
style = {'lower': '-', 'upper': (0, (4, 2))}
name = {'lower': 'lower', 'upper': 'upper'}

plt.rcParams.update({'font.family': 'serif', 'font.size': 7.5, 'axes.linewidth': 0.6,
                     'xtick.major.width': 0.6, 'ytick.major.width': 0.6})
fig, ax = plt.subplots(figsize=(3.35, 2.75))
ax.axhline(0, color='#888888', lw=0.6, zorder=1)
for pipe in ['NOVA', 'exoTEDRF']:
    for est in ['lower', 'upper']:
        y = err[(pipe, est)]
        ax.stairs(y, edges, color=colour[pipe], ls=style[est], lw=1.4, zorder=3, baseline=None,
                  label=f'{pipe}, {name[est]} ({rmse[(pipe, est)]} ppm)')
ax.set_xlim(0.6, 2.85)
ax.set_xlabel(r'Wavelength ($\mu$m)')
ax.set_ylabel('Mean error (ppm)')
ax.grid(axis='y', color='#e3e3e3', lw=0.5, zorder=0)
for s in ['top', 'right']:
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=6.8, loc='lower left', bbox_to_anchor=(-0.16, 1.0), ncol=2, columnspacing=0.6, handlelength=2.2, handletextpad=0.4)
fig.subplots_adjust(left=0.17, right=0.98, bottom=0.15, top=0.82)
fig.savefig('benchmark_flip_regional_errors.pdf', bbox_inches='tight', pad_inches=0.02)
fig.savefig('/private/tmp/claude-501/-Users-davidestaub-Desktop-ICL-PHD/3826395b-face-443e-b4ef-9d4376b4a9cf/scratchpad/benchmark_flip_preview.png', dpi=160, bbox_inches='tight', pad_inches=0.02)
print('saved')
