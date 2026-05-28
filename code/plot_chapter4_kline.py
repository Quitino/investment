"""
Chapter 4 图1：K线图基础讲解
绘制一段示例K线（OHLC + 成交量）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.patches as mpatches
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)
n = 20
dates = range(n)

# 生成合理的 OHLC 数据
closes = [100]
for _ in range(n - 1):
    closes.append(closes[-1] * (1 + np.random.uniform(-0.03, 0.035)))
closes = np.array(closes)

opens  = np.roll(closes, 1); opens[0] = 100
highs  = np.maximum(opens, closes) + np.random.uniform(0.5, 2, n)
lows   = np.minimum(opens, closes) - np.random.uniform(0.5, 2, n)
volumes = np.random.randint(500, 3000, n)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), gridspec_kw={'height_ratios': [3, 1]})

for i in range(n):
    color = '#e74c3c' if closes[i] >= opens[i] else '#2ecc71'
    # 蜡烛实体
    ax1.bar(i, abs(closes[i] - opens[i]), bottom=min(opens[i], closes[i]),
            color=color, width=0.6, edgecolor='white', linewidth=0.5)
    # 上下影线
    ax1.plot([i, i], [lows[i], min(opens[i], closes[i])], color=color, linewidth=1.2)
    ax1.plot([i, i], [max(opens[i], closes[i]), highs[i]], color=color, linewidth=1.2)
    # 成交量颜色
    ax2.bar(i, volumes[i], color=color, alpha=0.8, width=0.6)

# 标注K线结构（第5根）
i = 5
ax1.annotate('', xy=(i, highs[i] + 0.3), xytext=(i + 2, highs[i] + 2),
             arrowprops=dict(arrowstyle='->', color='#2c3e50'))
ax1.text(i + 2.1, highs[i] + 2, '上影线\n（最高价）', fontsize=8, color='#2c3e50',
         fontproperties=fm.FontProperties(family=FONT))
ax1.annotate('', xy=(i, lows[i] - 0.2), xytext=(i + 2, lows[i] - 2),
             arrowprops=dict(arrowstyle='->', color='#2c3e50'))
ax1.text(i + 2.1, lows[i] - 2.5, '下影线\n（最低价）', fontsize=8, color='#2c3e50',
         fontproperties=fm.FontProperties(family=FONT))

red_patch = mpatches.Patch(color='#e74c3c', label='阳线（收盘 > 开盘，上涨）')
green_patch = mpatches.Patch(color='#2ecc71', label='阴线（收盘 < 开盘，下跌）')
ax1.legend(handles=[red_patch, green_patch], fontsize=9, loc='upper left')

ax1.set_title('K线图基础：每根蜡烛代表一个交易周期的四个价格', fontsize=12, fontweight='bold', pad=10)
ax1.set_ylabel('价格（元）', fontsize=10)
ax1.grid(True, alpha=0.2, linestyle='--')
ax1.set_xlim(-1, n)

ax2.set_ylabel('成交量（手）', fontsize=9)
ax2.grid(True, alpha=0.2, linestyle='--')
ax2.set_xlim(-1, n)
ax2.set_xlabel('交易日', fontsize=10)

fig.tight_layout(pad=1.5)
fig.savefig('../pic/chapter4_kline.png', dpi=150, bbox_inches='tight')
print("saved: chapter4_kline.png")
