"""
Chapter 6 图：黄金价格与美元指数的反向关系（示意）+ 黄金四种投资方式对比
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# 左图：黄金 vs 美元指数（示意走势，概念图）
np.random.seed(12)
months = 60
t = np.arange(months)
usd_index = 100 + np.cumsum(np.random.normal(0, 0.5, months))
gold_price = 1800 - 8 * (usd_index - 100) + np.cumsum(np.random.normal(0, 10, months))

ax1 = axes[0]
color_usd = '#3498db'
color_gold = '#f1c40f'

l1, = ax1.plot(t, gold_price, color=color_gold, linewidth=2.5, label='黄金价格（美元/盎司）')
ax1.set_ylabel('黄金价格（美元/盎司）', fontsize=10, color=color_gold)
ax1.tick_params(axis='y', labelcolor=color_gold)

ax1b = ax1.twinx()
l2, = ax1b.plot(t, usd_index, color=color_usd, linewidth=2, linestyle='--', label='美元指数（DXY）')
ax1b.set_ylabel('美元指数', fontsize=10, color=color_usd)
ax1b.tick_params(axis='y', labelcolor=color_usd)

ax1.set_title('黄金 vs 美元指数：通常反向波动\n（示意）', fontsize=11, fontweight='bold')
ax1.set_xlabel('月份', fontsize=10)
ax1.legend(handles=[l1, l2], fontsize=9, loc='upper left')
ax1.grid(True, alpha=0.2, linestyle='--')

# 右图：四种投资黄金方式对比（气泡图）
methods = ['实物黄金\n（金条/金币）', '纸黄金\n（银行账户）', '黄金ETF\n（场内基金）', '黄金股\n（矿业公司股票）']
liquidity = [1, 3, 5, 5]
cost = [1, 4, 5, 4]   # 成本便利性（越高越方便）
risk = [3, 3, 3, 5]   # 风险（越高风险越大）
colors = ['#f1c40f', '#f39c12', '#e67e22', '#e74c3c']

ax2 = axes[1]
for i, (m, l, c, r, col) in enumerate(zip(methods, liquidity, cost, risk, colors)):
    ax2.scatter(l, c, s=r*200, color=col, alpha=0.85, edgecolors='white', linewidth=2, zorder=5)
    ax2.annotate(m, xy=(l, c), xytext=(l, c - 0.4), ha='center', fontsize=9,
                 fontproperties=fm.FontProperties(family=FONT))

ax2.set_xlabel('流动性（1=低，5=高）', fontsize=10)
ax2.set_ylabel('买入便利性（1=麻烦，5=方便）', fontsize=10)
ax2.set_title('四种黄金投资方式对比\n（气泡大小 = 风险程度）', fontsize=11, fontweight='bold')
ax2.set_xlim(0, 6.5)
ax2.set_ylim(0, 6.5)
ax2.grid(True, alpha=0.25, linestyle='--')
ax2.text(5.5, 0.3, '气泡越大=风险越高', fontsize=8, color='grey',
         fontproperties=fm.FontProperties(family=FONT))

fig.tight_layout(pad=2)
fig.savefig('../pic/chapter6_gold.png', dpi=150, bbox_inches='tight')
print("saved: chapter6_gold.png")
