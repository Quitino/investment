"""
Chapter 7 图：债券价格与利率反向关系 + 债券类型收益风险对比
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

# 左图：利率变化对债券价格的影响
# 固定票面利率5%，面值100，剩余期限10年
def bond_price(face, coupon_rate, ytm, n):
    coupon = face * coupon_rate
    price = sum(coupon / (1+ytm)**t for t in range(1, n+1))
    price += face / (1+ytm)**n
    return price

ytm_range = np.linspace(0.01, 0.12, 200)
prices_10y = [bond_price(100, 0.05, y, 10) for y in ytm_range]
prices_3y  = [bond_price(100, 0.05, y, 3) for y in ytm_range]
prices_1y  = [bond_price(100, 0.05, y, 1) for y in ytm_range]

ax1 = axes[0]
ax1.plot(ytm_range * 100, prices_10y, color='#e74c3c', linewidth=2.5, label='10年期债券（久期长）')
ax1.plot(ytm_range * 100, prices_3y,  color='#f39c12', linewidth=2.5, label='3年期债券')
ax1.plot(ytm_range * 100, prices_1y,  color='#2ecc71', linewidth=2.5, label='1年期债券（久期短）')
ax1.axhline(y=100, color='grey', linewidth=1, linestyle=':', alpha=0.6)
ax1.axvline(x=5, color='grey', linewidth=1, linestyle=':', alpha=0.6)
ax1.text(5.1, 60, '票面利率=5%\n（此时债券价格=面值100）', fontsize=8, color='grey',
         fontproperties=fm.FontProperties(family=FONT))
ax1.set_xlabel('市场利率（%）', fontsize=10)
ax1.set_ylabel('债券价格（元）', fontsize=10)
ax1.set_title('利率上升 → 债券价格下跌\n久期越长，价格波动越大', fontsize=11, fontweight='bold')
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.2, linestyle='--')
ax1.set_xlim(1, 12)

# 右图：债券类型风险收益对比
bond_types = ['活期存款', '国债\n（10年期）', '银行定期\n（3年）', '公司债\n（AA级）', '高收益债\n（垃圾债）', '可转债']
risk_scores = [0.5, 1, 1.5, 3.5, 6, 5]
return_scores = [0.35, 2.5, 2.8, 5, 8, 7]
colors_b = ['#95a5a6', '#3498db', '#2980b9', '#27ae60', '#e74c3c', '#9b59b6']

ax2 = axes[1]
for name, r, ret, col in zip(bond_types, risk_scores, return_scores, colors_b):
    ax2.scatter(r, ret, s=160, color=col, edgecolors='white', linewidth=1.5, zorder=5)
    ax2.annotate(name, xy=(r, ret), xytext=(r + 0.1, ret + 0.2), fontsize=8.5, color=col,
                 fontproperties=fm.FontProperties(family=FONT))

ax2.set_xlabel('信用风险（0=无风险）', fontsize=10)
ax2.set_ylabel('预期年化收益率（%）', fontsize=10)
ax2.set_title('债券类型：信用风险 vs 预期收益', fontsize=11, fontweight='bold')
ax2.grid(True, alpha=0.2, linestyle='--')
ax2.set_xlim(-0.3, 7.5)
ax2.set_ylim(0, 10)

fig.tight_layout(pad=2)
fig.savefig('../pic/chapter7_bonds.png', dpi=150, bbox_inches='tight')
print("saved: chapter7_bonds.png")
