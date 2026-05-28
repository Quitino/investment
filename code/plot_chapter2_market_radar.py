"""
Chapter 2 图2：A股 / 港股 / 美股 三市场对比雷达图
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

categories = ['开户便利性', '市场规模', '监管透明度', '国际化程度', '波动性（越低越好）', '信息获取难度（越低越好）']
N = len(categories)

# 评分 1-5，越高越优（波动和难度取反，即低分=差）
a_share  = [5, 4, 3, 2, 2, 3]
hk_share = [3, 3, 4, 4, 3, 3]
us_share = [3, 5, 5, 5, 4, 2]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

for data, label, color in [
    (a_share, 'A股（沪深）', '#e74c3c'),
    (hk_share, '港股', '#3498db'),
    (us_share, '美股', '#2ecc71'),
]:
    values = data + data[:1]
    ax.plot(angles, values, 'o-', linewidth=2, color=color, label=label)
    ax.fill(angles, values, alpha=0.12, color=color)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10,
                   fontproperties=fm.FontProperties(family=FONT))
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(['1', '2', '3', '4', '5'], fontsize=7, color='grey')
ax.set_title('A股 / 港股 / 美股 特征对比', fontsize=13, fontweight='bold', pad=20,
             fontproperties=fm.FontProperties(family=FONT))
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)
ax.grid(True, alpha=0.3)

fig.tight_layout()
fig.savefig('../pic/chapter2_market_radar.png', dpi=150, bbox_inches='tight')
print("saved: chapter2_market_radar.png")
