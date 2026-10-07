#!/usr/bin/env python3
"""Figure 2: the WASP-17 b SOSS detector scene, before and after background subtraction.

(a) Out-of-transit median before the zodiacal background is subtracted (the
    background-off control of the pre-1/f calibration images). The step in the
    zodiacal background near column 700 and the field-star light identified in
    the F277W exposure are marked.
(b) The Stage-2 (background-subtracted) out-of-transit median with the pixel
    supports that NOVA fits for orders 1 and 2 (as in the earlier Figure 2).
All arrays are local copies already on this machine; nothing is fetched.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path("/Users/davidestaub/Desktop/ICL_PHD")
V47 = ROOT / "NOVA_SP_E14_RESPONSE_AWARE_RECOVERY_20260819_R1"
IMAGE = V47 / "products/plots/v47_detector/v47_oot_median_detector.npz"
FOOTPRINTS = V47 / "products/plots/v47_detector/v47_exact_response_footprints.npz"
LAYOUT = V47 / "runtime/frozen_inputs/historical_active_layout_and_profiles.npz"
PRE1F = ROOT / "NOVA_ASTRA_EXECUTION_20260905_R1/products/pre1f_calibration_arrays_r1/NATIVE_PRE1F_CALIBRATION_IMAGES.npz"
FIELDS = ROOT / "NOVA_ASTRA_EXECUTION_20260905_R1/products/fixed_primary_family_20260920_r1_package/freeze/FAMILY_FIELDS.npz"
OUT = Path(__file__).resolve().parent / "niriss_soss_detector_scene"


def asinh_norm(img, lo=0.2, hi=99.97, width=2.5):
    finite = img[np.isfinite(img)]
    vmin, vmax = np.percentile(finite, [lo, hi])
    return mpl.colors.AsinhNorm(linear_width=width, vmin=vmin, vmax=vmax)


def main() -> None:
    cmap = mpl.colormaps["magma"].copy()
    cmap.set_bad("black")
    with np.load(IMAGE, allow_pickle=False) as a:
        stage2 = np.asarray(a["image"], dtype=float)
    with np.load(PRE1F, allow_pickle=False) as a:
        order = list(a["all_half_even_odd_median_order"])
        raw = np.asarray(a["background_off_control_medians"][order.index("all")], dtype=float)
    with np.load(FIELDS, allow_pickle=False) as a:
        f277w = np.asarray(a["native_F277W_mask"], dtype=bool)
    with np.load(FOOTPRINTS, allow_pickle=False) as a:
        bounds = {o: (np.asarray(a[f"order{o}_lower_y"], float), np.asarray(a[f"order{o}_upper_y"], float)) for o in (1, 2)}
    with np.load(LAYOUT, allow_pickle=False) as a:
        centres = {o: np.asarray(a[f"order{o}_trace_y_by_x"], float) for o in (1, 2)}

    ny, nx = stage2.shape
    ext = (-0.5, nx - 0.5, -0.5, ny - 0.5)
    mpl.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.titlesize": 13, "axes.labelsize": 12,
                         "xtick.labelsize": 10, "ytick.labelsize": 10})
    fig, axes = plt.subplots(2, 1, figsize=(15.2, 7.9), constrained_layout=True, sharex=True)

    # (a) before background subtraction
    ax = axes[0]
    im = ax.imshow(raw, origin="lower", interpolation="nearest", aspect="auto", cmap=cmap,
                   norm=asinh_norm(raw), extent=ext, rasterized=True)
    ax.contour(np.arange(nx), np.arange(ny), f277w.astype(float), levels=[0.5],
               colors="#00E5FF", linewidths=1.0)
    ax.plot([], [], color="#00E5FF", lw=1.2, label="Field-star light identified in the F277W exposure")
    ax.axvline(700, ymin=0.70, ymax=0.98, color="white", lw=1.6, ls=(0, (5, 3)))
    ax.annotate("Step in the zodiacal\nbackground (column 700)", xy=(700, 232), xytext=(330, 228),
                color="white", fontsize=10.5, va="center",
                arrowprops=dict(arrowstyle="->", color="white", lw=1.3))
    ax.set_title("(a) Before the background and 1/f corrections", loc="left", fontweight="semibold")
    ax.legend(loc="lower right", frameon=True, facecolor="black", edgecolor="white",
              framealpha=0.72, labelcolor="white", fontsize=10)
    cb = fig.colorbar(im, ax=ax, pad=0.012, fraction=0.025, aspect=14)
    cb.set_label(r"Count rate (DN s$^{-1}$)")

    # (b) background-subtracted, with NOVA supports
    ax = axes[1]
    im = ax.imshow(stage2, origin="lower", interpolation="nearest", aspect="auto", cmap=cmap,
                   norm=asinh_norm(stage2), extent=ext, rasterized=True)
    styles = {1: ("Order 1", "#64F5FF"), 2: ("Order 2", "#B9FF66")}
    for o, (label, color) in styles.items():
        lo, up = bounds[o]
        c = centres[o]
        x = np.arange(lo.size, dtype=float)
        use = np.isfinite(lo) & np.isfinite(up) & np.isfinite(c)
        lhw = np.median(c[use] - lo[use]); uhw = np.median(up[use] - c[use])
        for k, y in enumerate((c - lhw, c + uhw)):
            u = use & np.isfinite(y)
            ax.plot(x[u], y[u], color="black", lw=2.7, alpha=0.74, ls=(0, (6, 4)))
            ax.plot(x[u], y[u], color=color, lw=1.35, ls=(0, (6, 4)), label=label if k == 0 else None)
    ax.set_title("(b) After detector processing and background subtraction, with the regions fitted by NOVA", loc="left", fontweight="semibold")
    ax.legend(loc="upper left", ncols=2, frameon=True, facecolor="black", edgecolor="white",
              framealpha=0.72, labelcolor="white")
    cb = fig.colorbar(im, ax=ax, pad=0.012, fraction=0.025, aspect=14)
    cb.set_label(r"Count rate (DN s$^{-1}$)")

    for ax in axes:
        ax.set_xlim(ext[0], ext[1]); ax.set_ylim(ext[2], ext[3])
        ax.set_ylabel("Detector row")
    axes[1].set_xlabel("Detector column")
    fig.savefig(OUT.with_suffix(".pdf"), dpi=220, facecolor="white")
    fig.savefig(OUT.with_suffix(".png"), dpi=110, facecolor="white")
    print(OUT.with_suffix(".pdf"))
    for x0, x1 in ((600, 690), (710, 800)):
        print(f"off-trace median rows 225-250, x {x0}-{x1}: raw {np.nanmedian(raw[225:250, x0:x1]):.2f}  stage2 {np.nanmedian(stage2[225:250, x0:x1]):.2f}")


if __name__ == "__main__":
    main()
