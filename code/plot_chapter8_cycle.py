"""
Chapter 8 图：经济周期四阶段 + 各阶段受益资产（轮盘图）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# 左图：经济周期轮盘（饼图改造）
ax1 = axes[0]
phases = ['复苏期\n(GDP↑ 通胀低)', '扩张期\n(GDP↑ 通胀↑)', '过热期\n(GDP见顶 通胀高)', '衰退期\n(GDP↓ 通胀↓)']
colors_c = ['#2ecc71', '#f1c40f', '#e67e22', '#e74c3c']
sizes = [25, 25, 25, 25]

wedges, texts = ax1.pie(sizes, labels=phases, colors=colors_c,
                         startangle=90, wedgeprops=dict(width=0.5, edgecolor='white', linewidth=2),
                         textprops=dict(fontsize=9, fontproperties=fm.FontProperties(family=FONT)))

# 中心文字
ax1.text(0, 0, '经济\n周期', ha='center', va='center', fontsize=13, fontweight='bold',
         fontproperties=fm.FontProperties(family=FONT))

# 标注各阶段受益资产
annotations = [
    (0.75, 0.75, '受益：\n股票（早）\n债券（末）', '#2ecc71'),
    (0.75, -0.75, '受益：\n股票（主）\n大宗商品', '#f1c40f'),
    (-0.75, -0.75, '受益：\n黄金\n大宗商品\n通胀债', '#e67e22'),
    (-0.75, 0.75, '受益：\n债券\n防御股票\n现金', '#e74c3c'),
]
for ax_x, ax_y, text, color in annotations:
    ax1.text(ax_x, ax_y, text, ha='center', va='center', fontsize=8,
             color=color, fontweight='bold',
             fontproperties=fm.FontProperties(family=FONT))

ax1.set_title('经济周期四阶段与资产轮动', fontsize=12, fontweight='bold', pad=15)

# 右图：美联储利率周期与市场影响（示意）
ax2 = axes[1]
t = np.linspace(0, 4*np.pi, 300)
fed_rate = 3 + 2.5 * np.sin(t)
stock_market = 100 * np.exp(0.08/52 * np.arange(300) + 0.3 * np.cumsum(np.random.normal(0, 0.02, 300)))
stock_market = stock_market / stock_market[0] * 100

# 重设随机种子确保可复现
np.random.seed(42)
stock_market = 100 + 30*np.sin(t - 0.5) + np.cumsum(np.random.normal(0, 0.5, 300))

ax2_twin = ax2.twinx()
ax2.plot(t, fed_rate, color='#e74c3c', linewidth=2.5, label='美联储基准利率（%）')
ax2_twin.plot(t, stock_market, color='#3498db', linewidth=2, linestyle='--', alpha=0.8, label='股市指数（示意）')

ax2.set_xlabel('时间（周期示意）', fontsize=10)
ax2.set_ylabel('基准利率（%）', fontsize=10, color='#e74c3c')
ax2_twin.set_ylabel('股市指数', fontsize=10, color='#3498db')
ax2.tick_params(axis='y', labelcolor='#e74c3c')
ax2_twin.tick_params(axis='y', labelcolor='#3498db')
ax2.set_title('利率周期与股市关系（概念示意）\n降息→股市通常上涨，加息→股市承压', fontsize=11, fontweight='bold')

lines1, labels1 = ax2.get_legend_handles_labels()
lines2, labels2 = ax2_twin.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper right')
ax2.grid(True, alpha=0.2, linestyle='--')

fig.tight_layout(pad=2)
fig.savefig('../pic/chapter8_cycle.png', dpi=150, bbox_inches='tight')
print("saved: chapter8_cycle.png")
