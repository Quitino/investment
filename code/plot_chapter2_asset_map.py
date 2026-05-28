"""
Chapter 2 图1：主要资产类别风险-收益散点图
横轴：风险（波动率），纵轴：预期年化收益率
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

assets = {
    '现金/活期': (1, 0.5, '#95a5a6'),
    '货币基金': (2, 2.5, '#3498db'),
    '国债': (3, 3.5, '#2980b9'),
    '黄金': (10, 7, '#f1c40f'),
    '债券基金': (5, 4.5, '#27ae60'),
    '房产': (8, 6, '#e67e22'),
    '沪深300\n指数基金': (18, 9, '#2ecc71'),
    '个股': (30, 12, '#e74c3c'),
    '加密货币': (60, 20, '#9b59b6'),
}

fig, ax = plt.subplots(figsize=(10, 6))

for name, (risk, ret, color) in assets.items():
    ax.scatter(risk, ret, s=180, color=color, zorder=5, edgecolors='white', linewidth=1.5)
    offset_x = 1.5
    offset_y = 0.3
    if name == '现金/活期':
        offset_y = -0.7
    elif name == '货币基金':
        offset_y = 0.5
    ax.annotate(name, xy=(risk, ret), xytext=(risk + offset_x, ret + offset_y),
                fontsize=9, color=color,
                fontproperties=fm.FontProperties(family=FONT))

# 有效前沿示意曲线
x_curve = np.linspace(1, 65, 200)
y_curve = 2.5 * np.log(x_curve / 0.8)
ax.plot(x_curve, y_curve, '--', color='#bdc3c7', linewidth=1.5, alpha=0.6, label='理论有效前沿（示意）')

ax.set_xlabel('风险（波动率 %）', fontsize=11)
ax.set_ylabel('预期年化收益率（%）', fontsize=11)
ax.set_title('主要资产类别：风险与收益的位置', fontsize=13, fontweight='bold', pad=12)
ax.set_xlim(-2, 75)
ax.set_ylim(-1, 25)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.25, linestyle='--')
ax.axhline(y=3, color='#e74c3c', linestyle=':', linewidth=1, alpha=0.5)
ax.text(65, 3.3, '通胀线≈3%', fontsize=8, color='#e74c3c', ha='right',
        fontproperties=fm.FontProperties(family=FONT))

fig.tight_layout()
fig.savefig('../pic/chapter2_asset_map.png', dpi=150, bbox_inches='tight')
print("saved: chapter2_asset_map.png")
