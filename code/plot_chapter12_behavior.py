"""
Chapter 12 图：行为金融学常见误区可视化
1. 损失厌恶：涨5%和跌5%的感受不对称
2. 散户 vs 市场的真实收益率差（长期持有 vs 频繁交易）
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
fp = fm.FontProperties(family=FONT)

# 左图：损失厌恶 - 前景理论价值函数
ax1 = axes[0]
x_gain = np.linspace(0, 100, 200)
x_loss = np.linspace(-100, 0, 200)

# 卡尼曼-特沃斯基价值函数
v_gain = x_gain ** 0.88
v_loss = -2.25 * ((-x_loss) ** 0.88)

ax1.plot(x_gain, v_gain, color='#2ecc71', linewidth=3, label='盈利时的愉悦感')
ax1.plot(x_loss, v_loss, color='#e74c3c', linewidth=3, label='亏损时的痛苦感')
ax1.axhline(y=0, color='black', linewidth=1)
ax1.axvline(x=0, color='black', linewidth=1)

# 标注不对称
ax1.annotate('', xy=(50, v_gain[100]), xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=1.5))
ax1.annotate('', xy=(-50, v_loss[100]), xytext=(0, 0),
             arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=1.5))
ax1.text(55, v_gain[100]+2, f'+{v_gain[100]:.0f}', fontsize=10, color='#2ecc71', fontweight='bold')
ax1.text(-95, v_loss[100]-5, f'{v_loss[100]:.0f}', fontsize=10, color='#e74c3c', fontweight='bold')
ax1.text(30, 30, '赚50元的快乐', fontsize=9, color='#2ecc71', fontproperties=fp)
ax1.text(-90, -80, '亏50元的痛苦\n是赚50的2.25倍', fontsize=9, color='#e74c3c', fontproperties=fp)

ax1.set_xlabel('金额变化', fontsize=10)
ax1.set_ylabel('心理感受强度', fontsize=10)
ax1.set_title('损失厌恶：亏损的痛苦 > 同等盈利的快乐\n（卡尼曼前景理论）', fontsize=11, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.2)

# 右图：持有期收益率 vs 实际获得收益率（行为差距）
ax2 = axes[1]
years_list = [1, 3, 5, 10, 20]
fund_return = [8, 8, 8, 8, 8]      # 基金实际年化
investor_return = [2, 4, 5, 6, 7]  # 投资者实际获得（频繁进出造成损耗）

x = np.arange(len(years_list))
w = 0.35

bars1 = ax2.bar(x - w/2, fund_return, width=w, color='#3498db', label='基金实际年化收益', edgecolor='white')
bars2 = ax2.bar(x + w/2, investor_return, width=w, color='#e74c3c', label='散户实际获得收益\n（因频繁操作损耗）', edgecolor='white')

ax2.set_xticks(x)
ax2.set_xticklabels([f'{y}年' for y in years_list], fontproperties=fp)
ax2.set_ylabel('年化收益率（%）', fontsize=10)
ax2.set_title('基金收益 vs 散户实际获得收益\n（持有期越长，差距越小）', fontsize=11, fontweight='bold')
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.2, axis='y', linestyle='--')
ax2.set_ylim(0, 12)

for bar in bars1:
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f'{bar.get_height():.0f}%', ha='center', va='bottom', fontsize=9, color='#3498db')
for bar in bars2:
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
             f'{bar.get_height():.0f}%', ha='center', va='bottom', fontsize=9, color='#e74c3c')

fig.tight_layout(pad=2)
fig.savefig('./pic/chapter12_behavior.png', dpi=150, bbox_inches='tight')
print("saved: chapter12_behavior.png")
