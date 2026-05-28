"""
Chapter 1 图1：通货膨胀侵蚀购买力
10万元在不同通胀率下，20年后的实际购买力
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

years = np.arange(0, 21)
principal = 100000

rates = {
    '通胀率 2%（温和）': 0.02,
    '通胀率 3%（常态）': 0.03,
    '通胀率 5%（偏高）': 0.05,
}
colors = ['#2ecc71', '#f39c12', '#e74c3c']

fig, ax = plt.subplots(figsize=(9, 5))

for (label, r), color in zip(rates.items(), colors):
    values = principal / (1 + r) ** years
    ax.plot(years, values / 10000, label=label, color=color, linewidth=2.5, marker='o', markersize=3)
    ax.annotate(f'{values[-1]/10000:.1f}万', xy=(20, values[-1]/10000),
                xytext=(20.2, values[-1]/10000), fontsize=9, color=color,
                fontproperties=fm.FontProperties(family=FONT))

ax.axhline(y=10, color='#3498db', linestyle='--', linewidth=1.5, alpha=0.6, label='初始 10 万元')
ax.set_xlabel('年数', fontsize=11)
ax.set_ylabel('实际购买力（万元）', fontsize=11)
ax.set_title('10万元在不同通胀率下的购买力侵蚀（20年）', fontsize=13, fontweight='bold', pad=12)
ax.set_xlim(0, 22)
ax.set_ylim(0, 12)
ax.legend(loc='lower left', fontsize=9)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xticks(range(0, 21, 5))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}万'))

fig.tight_layout()
fig.savefig('../pic/chapter1_inflation.png', dpi=150, bbox_inches='tight')
print("saved: chapter1_inflation.png")
