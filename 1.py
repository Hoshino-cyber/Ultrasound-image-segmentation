import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(12,6))

# Modules as rectangles
modules = [
    ("输入图像", (0, 0)),
    ("特征提取模块", (2, 0)),
    ("注意力定位模块", (4, 0)),
    ("对抗擦除模块", (6, 0)),
    ("主分类模块", (8, 1)),
    ("辅助分类模块", (8, -1)),
    ("多任务联合优化模块", (10, 0))
]

for name, (x, y) in modules:
    rect = mpatches.FancyBboxPatch((x, y-0.4), 1.8, 0.8,
                                   boxstyle="round,pad=0.1", fc="#cce5ff", ec="black")
    ax.add_patch(rect)
    ax.text(x+0.9, y, name, ha="center", va="center", fontsize=10)

# Arrows between modules
arrows = [
    ((1.8, 0), (2, 0)),
    ((3.8, 0), (4, 0)),
    ((5.8, 0), (6, 0)),
    ((7.8, 0.2), (8, 0.8)),
    ((7.8, -0.2), (8, -0.8)),
    ((9.8, 1), (10, 0.2)),
    ((9.8, -1), (10, -0.2))
]

for (x1, y1), (x2, y2) in arrows:
    ax.annotate("", xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle="->", lw=1.5))

ax.set_xlim(-1, 12)
ax.set_ylim(-2, 2)
ax.axis("off")
plt.show()
