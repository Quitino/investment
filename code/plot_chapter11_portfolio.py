"""
Chapter 11 图1：资产配置经典组合对比（柱状图+饼图）
60/40 vs 全天候 vs 纯股票
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 3, figsize=(14, 5))

fp = fm.FontProperties(family=FONT)

# 三种组合的资产配置
portfolios = {
    '纯股票组合': {'A股指数': 60, '美股指数': 40},
    '经典60/40': {'A股指数': 40, '美股指数': 20, '债券': 35, '现金': 5},
    '全天候组合\n(Bridgewater)': {'股票': 30, '长期债券': 40, '中期债券': 15, '黄金': 7.5, '大宗商品': 7.5},
}
colors_p = ['#3498db', '#2ecc71', '#e74c3c', '#f1c40f', '#9b59b6', '#e67e22']

for ax, (name, alloc) in zip(axes, portfolios.items()):
    labels = list(alloc.keys())
    sizes = list(alloc.values())
    cols = colors_p[:len(labels)]
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=cols, autopct='%1.0f%%',
        startangle=90, pctdistance=0.75,
        wedgeprops=dict(edgecolor='white', linewidth=2),
        textprops=dict(fontsize=8.5, fontproperties=fp)
    )
    for at in autotexts:
        at.set_fontsize(8)
    ax.set_title(name, fontsize=11, fontweight='bold', pad=10,
                 fontproperties=fp)

fig.suptitle('三种典型资产配置方案对比', fontsize=13, fontweight='bold', y=1.02,
             fontproperties=fp)
fig.tight_layout(pad=2)
fig.savefig('./pic/chapter11_portfolio.png', dpi=150, bbox_inches='tight')
print("saved: chapter11_portfolio.png")
