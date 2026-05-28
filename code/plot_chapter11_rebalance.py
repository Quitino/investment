"""
Chapter 11 图2：再平衡效果示意
股债60/40组合再平衡 vs 不再平衡
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(55)
years = 20
n = years * 12

# 股票月收益
stock_ret = np.random.normal(0.08/12, 0.18/np.sqrt(12), n)
# 债券月收益（与股票负相关）
bond_ret = np.random.normal(0.04/12, 0.05/np.sqrt(12), n)

# 再平衡组合（每年初调回60/40）
stock_val = 60000
bond_val  = 40000
rebalanced = [100000]

for i in range(n):
    stock_val *= (1 + stock_ret[i])
    bond_val  *= (1 + bond_ret[i])
    total = stock_val + bond_val
    if i > 0 and i % 12 == 0:  # 每年再平衡
        stock_val = total * 0.6
        bond_val  = total * 0.4
    rebalanced.append(total)

# 不再平衡组合（任其漂移）
stock_val2 = 60000
bond_val2  = 40000
no_rebal = [100000]

for i in range(n):
    stock_val2 *= (1 + stock_ret[i])
    bond_val2  *= (1 + bond_ret[i])
    no_rebal.append(stock_val2 + bond_val2)

t = np.arange(0, years + 1/12, 1/12)[:len(rebalanced)]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, np.array(rebalanced)/10000, color='#2ecc71', linewidth=2.5, label=f'每年再平衡（终值{rebalanced[-1]/10000:.0f}万）')
ax.plot(t, np.array(no_rebal)/10000, color='#e74c3c', linewidth=2, linestyle='--',
        label=f'不再平衡（终值{no_rebal[-1]/10000:.0f}万）', alpha=0.8)

ax.set_xlabel('年数', fontsize=11)
ax.set_ylabel('资产价值（万元）', fontsize=11)
ax.set_title('60/40组合：再平衡 vs 不再平衡（20年模拟）\n再平衡降低风险，长期收益更稳定', fontsize=12, fontweight='bold', pad=10)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.25, linestyle='--')
ax.set_xlim(0, years)

# 标注再平衡时间点
for yr in range(1, years):
    ax.axvline(x=yr, color='grey', linewidth=0.4, alpha=0.3)
ax.text(1.1, max(rebalanced)/10000*0.92, '↑每年再平衡时机', fontsize=7.5, color='grey',
        fontproperties=fm.FontProperties(family=FONT))

fig.tight_layout()
fig.savefig('./pic/chapter11_rebalance.png', dpi=150, bbox_inches='tight')
print("saved: chapter11_rebalance.png")
