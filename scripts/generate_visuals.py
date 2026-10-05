from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

levels = [1, 2, 3, 4, 5]
names = ["Initial", "Managed", "Defined", "Quantitatively\nManaged", "Optimizing"]

fig, ax = plt.subplots(figsize=(10, 5.6))
ax.barh(names, levels)
ax.set_xlabel("Maturity progression")
ax.set_title("CMMI Maturity Progression")
ax.set_xlim(0, 5.5)
ax.grid(axis="x", alpha=0.25)
for y, value in enumerate(levels):
    ax.text(value + 0.08, y, f"Level {value}", va="center")
fig.tight_layout()
fig.savefig(ASSETS / "maturity-progression.png", dpi=180, bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots(figsize=(9.5, 5.4))
ax.plot(levels, levels, marker="o")
ax.set_xticks(levels, names)
ax.set_ylabel("Relative process capability (conceptual)")
ax.set_title("Conceptual Process Capability Across CMMI Maturity Levels")
ax.grid(alpha=0.25)
ax.text(
    0.02, -0.18,
    "Conceptual visualization based on the source's progression from reactive to optimized processes.",
    transform=ax.transAxes, fontsize=9
)
fig.tight_layout()
fig.savefig(ASSETS / "process-capability-concept.png", dpi=180, bbox_inches="tight")
plt.close(fig)

counts = [0, 2, 2, 2, 2]
fig, ax = plt.subplots(figsize=(9.5, 5.2))
ax.bar(levels, counts)
ax.set_xticks(levels, [f"L{i}" for i in levels])
ax.set_ylabel("Example process areas explicitly listed")
ax.set_xlabel("Maturity level")
ax.set_title("Process Areas Mentioned by Maturity Level")
ax.set_ylim(0, 2.5)
ax.grid(axis="y", alpha=0.25)
for x, y in zip(levels, counts):
    ax.text(x, y + 0.06, str(y), ha="center")
fig.tight_layout()
fig.savefig(ASSETS / "process-areas-by-level.png", dpi=180, bbox_inches="tight")
plt.close(fig)

print("Visualizations generated in:", ASSETS)
