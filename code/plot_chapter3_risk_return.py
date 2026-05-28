"""
Chapter 3 图1：风险与收益的权衡示意
正态分布展示：低波动（债券）vs 高波动（股票）的收益分布
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from scipy import stats

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 5))

x = np.linspace(-50, 70, 500)

scenarios = [
    ('货币基金（极低风险）', 2.5, 1, '#3498db', '-'),
    ('债券基金（低风险）',   4.5, 5, '#27ae60', '-'),
    ('指数基金（中等风险）', 9.0, 18,'#f39c12', '-'),
    ('个股（高风险）',       12,  30,'#e74c3c', '--'),
]

for label, mu, sigma, color, ls in scenarios:
    y = stats.norm.pdf(x, mu, sigma)
    ax.plot(x, y, linewidth=2.5, color=color, linestyle=ls, label=label)
    # 标注均值
    ax.axvline(x=mu, color=color, linewidth=0.8, linestyle=':', alpha=0.6)

ax.axvline(x=0, color='black', linewidth=1.5, linestyle='-', alpha=0.4)
ax.text(0.5, 0.38, '盈亏平衡线', fontsize=8, color='black', alpha=0.5,
        fontproperties=fm.FontProperties(family=FONT))

ax.set_xlabel('年化收益率（%）', fontsize=11)
ax.set_ylabel('概率密度', fontsize=11)
ax.set_title('风险即"不确定性"：不同资产的收益分布', fontsize=13, fontweight='bold', pad=12)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.25, linestyle='--')
ax.set_xlim(-50, 70)

# 阴影：个股亏损区域
x_loss = x[x < 0]
y_loss = stats.norm.pdf(x_loss, 12, 30)
ax.fill_between(x_loss, y_loss, alpha=0.15, color='#e74c3c', label='亏损概率（个股）')

fig.tight_layout()
fig.savefig('../pic/chapter3_risk_return.png', dpi=150, bbox_inches='tight')
print("saved: chapter3_risk_return.png")
