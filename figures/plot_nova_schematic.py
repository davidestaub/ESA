"""Schematic of NOVA's detector forward model (Section 2, Eq. nova-forward). (a) Retained detector pixels
grouped by order and column (sketch, not data). (b) The model of each pixel: the stellar term,
gamma_t C_tg Tbar_tg q*_pg, is dimmed by the transit; the background B_tp is not. The spatial
profile q* and the geometry Omega are estimated beforehand; D and u are shared by both orders."""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
plt.rcParams.update({'font.family': 'serif', 'font.size': 7.2})
fig = plt.figure(figsize=(3.35, 3.3))
# (a) sketch of traces and pixel groups
ax = fig.add_axes([0.03, 0.60, 0.94, 0.36])
x = np.linspace(0, 10, 300)
y1 = 2.0 + 0.012 * (x - 6) ** 2; y2 = 4.9 + 0.05 * (x - 3) ** 2 - 0.02 * x
for y, c, lab in ((y1, '#2a78d6', 'order 1'), (y2, '#eb6834', 'order 2')):
    ax.fill_between(x, y - 0.45, y + 0.45, color=c, alpha=0.25, lw=0)
    ax.plot(x, y, color=c, lw=1.0); ax.text(0.15, y[0] + 0.6, lab, color=c, ha='left', fontsize=7)
xc = 4.0
for y, c in ((y1, '#2a78d6'), (y2, '#eb6834')):
    yc = np.interp(xc, x, y)
    for k in range(-3, 4):
        ax.add_patch(Rectangle((xc - 0.12, yc + 0.13 * k - 0.065), 0.24, 0.13, fill=False, ec=c, lw=0.6))
ax.annotate('one group $g$: the pixels $P_g$\nof one order in one column', xy=(xc + 0.15, np.interp(xc, x, y1)), xytext=(5.2, 0.35),
            fontsize=6.8, arrowprops=dict(arrowstyle='->', lw=0.6, color='#333333'))
ax.set_xlim(0, 10); ax.set_ylim(0, 7.8); ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel('detector column', fontsize=7); ax.set_ylabel('row', fontsize=7)
ax.set_title('(a) retained pixels, grouped by order and column (sketch)', fontsize=7.2, loc='left', pad=2)
# (b) model terms
bx = fig.add_axes([0.0, 0.0, 1.0, 0.54]); bx.set_xlim(0, 10); bx.set_ylim(0, 6); bx.axis('off')
bx.text(0.15, 5.7, '(b) model of each pixel (schematic)', fontsize=7.2, va='top')
def box(xy, w, h, txt, fc, fs=6.3):
    bx.add_patch(FancyBboxPatch(xy, w, h, boxstyle='round,pad=0.05,rounding_size=0.15', fc=fc, ec='#666666', lw=0.6))
    bx.text(xy[0] + w / 2, xy[1] + h / 2, txt, ha='center', va='center', fontsize=fs)
box((0.15, 3.45), 3.1, 1.55, 'fitted, shared by' + '\n' + r'both orders:' + '\n' + r'spectrum $D(\lambda)$', '#e3eefb')
box((3.45, 3.45), 3.1, 1.55, 'fitted: limb darkening' + '\n' + r'per order, continuum' + '\n' + r'$C_{tg}$, background $B_{tp}$', '#e3eefb')
box((6.75, 3.45), 3.1, 1.55, 'estimated beforehand:' + '\n' + r'profile $q^\star_{pg}$, geometry,' + '\n' + r'curvature $\gamma_t$', '#eeeeee')
box((0.6, 1.2), 8.8, 1.5, r'$\widehat Y_{tp} = \gamma_t\, C_{tg}\, \bar{\mathcal{T}}_{tg}\, q^\star_{pg} \;+\; B_{tp}$' + '\n'
    'starlight, dimmed by the transit  +  background, not dimmed', '#fff6ee', fs=6.6)
for x0 in (1.7, 5.0, 8.3):
    bx.annotate('', xy=(min(max(x0, 2.0), 8.0), 2.75), xytext=(x0, 3.55), arrowprops=dict(arrowstyle='->', lw=0.6, color='#333333'))
bx.text(5.0, 0.55, 'fitted to the count rate $Y_{tp}$ of every retained pixel', ha='center', fontsize=6.8)
fig.savefig('nova_schematic.pdf', bbox_inches='tight', pad_inches=0.02)
fig.savefig('/private/tmp/claude-501/-Users-davidestaub-Desktop-ICL-PHD/3826395b-face-443e-b4ef-9d4376b4a9cf/scratchpad/nova_schematic_preview.png', dpi=200, bbox_inches='tight')
print('saved')
