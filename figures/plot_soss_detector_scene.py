#!/usr/bin/env python3
"""Figure 2: the WASP-17 b SOSS detector scene in one labelled panel.

Out-of-transit median count rates before the 1/f and background corrections
(the background-off control of the pre-1/f calibration images), so that the
step in the zodiacal background near column 700 is visible. Labelled: the
traces of orders 1-3, one prominent field star and the background step.
All arrays are local copies already on this machine; nothing is fetched.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path("/Users/davidestaub/Desktop/ICL_PHD")
PRE1F = ROOT / "NOVA_ASTRA_EXECUTION_20260905_R1/products/pre1f_calibration_arrays_r1/NATIVE_PRE1F_CALIBRATION_IMAGES.npz"
OUT = Path(__file__).resolve().parent / "niriss_soss_detector_scene"

# Label positions (0-based detector x, y), read off the image itself.
ORDER_LABELS = {"Order 1": (1640, 72), "Order 2": (1240, 150), "Order 3": (330, 196)}
FIELD_STAR = (778, 34)      # bright field-star image on the lower edge of the order-1 trace
STEP = (700, 228)           # the step in the zodiacal background, off the traces


def main() -> None:
    with np.load(PRE1F, allow_pickle=False) as a:
        order = list(a["all_half_even_odd_median_order"])
        image = np.asarray(a["background_off_control_medians"][order.index("all")], dtype=float)

    # Flagged (NaN) pixels are filled with the mean of their valid 5x5
    # neighbours for display only; the caption says so.
    from scipy import ndimage
    finite = image[np.isfinite(image)]
    vmin, vmax = np.percentile(finite, [0.2, 99.97])   # stretch from the measured pixels only
    bad = ~np.isfinite(image)
    filled = np.where(bad, 0.0, image)
    weight = ndimage.uniform_filter((~bad).astype(float), size=5)
    smooth = ndimage.uniform_filter(filled, size=5)
    image = np.where(bad, np.divide(smooth, weight, out=np.zeros_like(smooth), where=weight > 0), image)
    norm = mpl.colors.AsinhNorm(linear_width=2.5, vmin=vmin, vmax=vmax)
    cmap = mpl.colormaps["magma"].copy()
    cmap.set_bad("black")

    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.labelsize": 12, "xtick.labelsize": 10, "ytick.labelsize": 10})
    ny, nx = image.shape
    ext = (-0.5, nx - 0.5, -0.5, ny - 0.5)
    fig, ax = plt.subplots(figsize=(15.2, 4.4), constrained_layout=True)
    im = ax.imshow(image, origin="lower", interpolation="nearest", aspect="auto",
                   cmap=cmap, norm=norm, extent=ext, rasterized=True)

    outline = [pe.withStroke(linewidth=3, foreground="black")]
    for text, (x, y) in ORDER_LABELS.items():
        ax.text(x, y, text, color="white", fontsize=12, fontweight="semibold",
                ha="center", va="center", path_effects=outline)

    arrow = dict(arrowstyle="->", color="white", lw=1.6)
    ax.annotate("Field star", xy=FIELD_STAR, xytext=(985, 16), color="white", fontsize=11.5,
                va="center", arrowprops=arrow, path_effects=outline)
    ax.annotate("Step in the zodiacal background", xy=STEP, xytext=(190, 236),
                color="white", fontsize=11.5, va="center", arrowprops=arrow, path_effects=outline)

    ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
    ax.set_xlabel("Detector column")
    ax.set_ylabel("Detector row")
    cb = fig.colorbar(im, ax=ax, pad=0.012, fraction=0.025, aspect=18)
    cb.set_label(r"Count rate (DN s$^{-1}$)")
    fig.savefig(OUT.with_suffix(".pdf"), dpi=220, facecolor="white")
    fig.savefig(OUT.with_suffix(".png"), dpi=110, facecolor="white")
    print(OUT.with_suffix(".pdf"))


if __name__ == "__main__":
    main()
