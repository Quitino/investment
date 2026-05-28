"""
Chapter 3 图2：市盈率(PE)直觉示意
用"回本年数"解释PE的含义
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左图：PE对比柱状图
markets = ['A股\n（沪深300）', '港股\n（恒生指数）', '美股\n（标普500）', 'A股\n（创业板）']
pe_values = [12, 10, 22, 35]
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']

bars = axes[0].bar(markets, pe_values, color=colors, edgecolor='white', linewidth=1.5, width=0.6)
axes[0].axhline(y=15, color='grey', linestyle='--', linewidth=1.5, alpha=0.7, label='历史合理中枢≈15')
axes[0].set_ylabel('市盈率（PE）', fontsize=11)
axes[0].set_title('主要市场市盈率参考\n（2024年大致水平）', fontsize=11, fontweight='bold')
axes[0].legend(fontsize=9)
axes[0].set_ylim(0, 45)

for bar, val in zip(bars, pe_values):
    axes[0].text(bar.get_x() + bar.get_width()/2, val + 0.8, f'PE={val}',
                 ha='center', va='bottom', fontsize=10, fontweight='bold',
                 fontproperties=fm.FontProperties(family=FONT))

axes[0].grid(True, alpha=0.25, linestyle='--', axis='y')

# 右图：PE=回本年数的直觉图
pe = 20
years = np.arange(1, pe + 1)
cumulative = np.cumsum([100 / pe] * pe)

axes[1].bar(years, [100/pe]*pe, color='#3498db', alpha=0.7, edgecolor='white', linewidth=0.5)
axes[1].axhline(y=100/pe, color='#e74c3c', linestyle='-', linewidth=1.5, alpha=0.8)
axes[1].set_xlabel('年数', fontsize=11)
axes[1].set_ylabel('每年利润占买价比例（%）', fontsize=11)
axes[1].set_title(f'PE={pe} 的直觉：需要约{pe}年"回本"\n（假设利润不增长）', fontsize=11, fontweight='bold')
axes[1].text(pe/2, 100/pe + 0.3, f'每年赚 {100/pe:.1f}%', ha='center', fontsize=10,
             color='#e74c3c', fontproperties=fm.FontProperties(family=FONT))
axes[1].grid(True, alpha=0.25, linestyle='--', axis='y')

fig.tight_layout(pad=2)
fig.savefig('../pic/chapter3_pe_ratio.png', dpi=150, bbox_inches='tight')
print("saved: chapter3_pe_ratio.png")
