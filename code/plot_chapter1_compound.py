"""
Chapter 1 图2：复利的力量
10万元在不同收益率下，30年后的增长曲线
对比：存银行（1.5%）vs 货币基金（3%）vs 指数基金（8%）vs 理想股票（12%）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

years = np.arange(0, 31)
principal = 100000

scenarios = {
    '存银行 1.5%': (0.015, '#95a5a6'),
    '货币基金 3%': (0.03, '#3498db'),
    '指数基金 8%': (0.08, '#2ecc71'),
    '优质股票 12%': (0.12, '#e74c3c'),
}

fig, ax = plt.subplots(figsize=(10, 6))

for label, (r, color) in scenarios.items():
    values = principal * (1 + r) ** years
    ax.plot(years, values / 10000, label=label, color=color, linewidth=2.5)
    final = values[-1] / 10000
    ax.annotate(f'{final:.0f}万', xy=(30, final),
                xytext=(30.3, final), fontsize=9.5, color=color,
                va='center',
                fontproperties=fm.FontProperties(family=FONT))

ax.set_xlabel('年数', fontsize=11)
ax.set_ylabel('资产（万元）', fontsize=11)
ax.set_title('复利的力量：10万元在不同收益率下30年的增长', fontsize=13, fontweight='bold', pad=12)
ax.set_xlim(0, 34)
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_xticks(range(0, 31, 5))

# 添加注释
ax.annotate('同样是10万元\n30年后相差近30倍', xy=(28, 250), fontsize=9,
            color='#7f8c8d', ha='center',
            fontproperties=fm.FontProperties(family=FONT))

fig.tight_layout()
fig.savefig('../pic/chapter1_compound.png', dpi=150, bbox_inches='tight')
print("saved: chapter1_compound.png")
