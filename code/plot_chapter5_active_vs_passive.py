"""
Chapter 5 图1：主动基金 vs 被动指数基金 长期收益率对比（示意）
费率侵蚀效应可视化
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

# 假设市场年化8%
market_return = 0.08

# 被动指数ETF：管理费0.1%，总费率约0.15%
passive = principal * (1 + market_return - 0.0015) ** years

# 平均主动基金：管理费1.5%，总费率约2%
# 且大多数跑不赢指数，假设超额收益+1%（乐观估计）
active_ok = principal * (1 + market_return + 0.01 - 0.02) ** years     # 跑赢1%但扣费后
active_avg = principal * (1 + market_return - 0.0 - 0.02) ** years      # 和市场持平扣费
active_bad = principal * (1 + market_return - 0.02 - 0.02) ** years     # 跑输2%再扣费

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, passive / 10000, linewidth=3, color='#2ecc71',
        label=f'指数ETF（年化{(market_return-0.0015)*100:.2f}%，费率0.15%）→ {passive[-1]/10000:.0f}万')
ax.plot(years, active_ok / 10000, linewidth=2, color='#3498db', linestyle='--',
        label=f'优秀主动基金（年化{(market_return+0.01-0.02)*100:.2f}%）→ {active_ok[-1]/10000:.0f}万')
ax.plot(years, active_avg / 10000, linewidth=2, color='#f39c12', linestyle='--',
        label=f'普通主动基金（年化{(market_return-0.02)*100:.2f}%）→ {active_avg[-1]/10000:.0f}万')
ax.plot(years, active_bad / 10000, linewidth=2, color='#e74c3c', linestyle=':',
        label=f'落后主动基金（年化{(market_return-0.02-0.02)*100:.2f}%）→ {active_bad[-1]/10000:.0f}万')

ax.axhline(y=10, color='grey', linewidth=1, linestyle=':', alpha=0.5)
ax.text(0.3, 10.5, '初始10万', fontsize=8, color='grey',
        fontproperties=fm.FontProperties(family=FONT))

ax.set_xlabel('年数', fontsize=11)
ax.set_ylabel('资产（万元）', fontsize=11)
ax.set_title('主动基金 vs 指数ETF：30年后费率的差距\n（假设市场年化8%）', fontsize=12, fontweight='bold', pad=12)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.25, linestyle='--')

fig.tight_layout()
fig.savefig('../pic/chapter5_active_vs_passive.png', dpi=150, bbox_inches='tight')
print("saved: chapter5_active_vs_passive.png")
