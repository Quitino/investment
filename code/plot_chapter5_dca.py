"""
Chapter 5 图2：定投平摊成本（Dollar Cost Averaging）示意
展示定期固定金额买入如何平滑成本
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(7)
months = 24
t = np.arange(months)

# 模拟价格走势：先跌后涨
price = np.array([10 + 3*np.sin(i*np.pi/8) + np.random.uniform(-0.5, 0.5)
                  for i in range(months)])
price = np.clip(price, 5, 16)

# 每月定投1000元
monthly = 1000
shares_list = []
total_shares = 0
total_invested = 0
avg_cost_list = []

for p in price:
    shares = monthly / p
    total_shares += shares
    total_invested += monthly
    avg_cost_list.append(total_invested / total_shares)
    shares_list.append(shares)

avg_cost = np.array(avg_cost_list)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 7), sharex=True)

# 上图：价格走势 + 平均成本
ax1.plot(t, price, linewidth=2.5, color='#3498db', label='基金净值（元）', zorder=5)
ax1.plot(t, avg_cost, linewidth=2, color='#e74c3c', linestyle='--', label='定投平均成本（元）', zorder=4)
ax1.fill_between(t, price, avg_cost, where=(price >= avg_cost), alpha=0.15, color='#2ecc71', label='盈利区间')
ax1.fill_between(t, price, avg_cost, where=(price < avg_cost), alpha=0.15, color='#e74c3c', label='亏损区间')
ax1.set_ylabel('净值/成本（元）', fontsize=10)
ax1.set_title(f'定投24个月：每月1000元，总投入{months*monthly/10000:.1f}万元\n定投在下跌中积累更多份额，拉低平均成本', fontsize=11, fontweight='bold', pad=8)
ax1.legend(fontsize=9, loc='upper right')
ax1.grid(True, alpha=0.2, linestyle='--')

# 下图：每月买入份额
ax2.bar(t, shares_list, color=['#2ecc71' if price[i] < avg_cost[i] else '#3498db' for i in t],
        alpha=0.8, width=0.7)
ax2.set_ylabel('本月买入份数', fontsize=10)
ax2.set_xlabel('月份', fontsize=10)
ax2.set_title('价格低时自动买入更多份额（同样1000元）', fontsize=10, pad=5)
ax2.grid(True, alpha=0.2, linestyle='--', axis='y')

# 最终收益标注
final_value = total_shares * price[-1]
profit = final_value - total_invested
ax1.text(months - 1, price[-1] + 0.3,
         f'终值{final_value:.0f}元\n收益{profit:+.0f}元',
         fontsize=8.5, ha='right', color='#2c3e50',
         fontproperties=fm.FontProperties(family=FONT))

fig.tight_layout(pad=1.5)
fig.savefig('../pic/chapter5_dca.png', dpi=150, bbox_inches='tight')
print("saved: chapter5_dca.png")
