"""
Chapter 4 图2：A股集中度 - 个股 vs 指数风险对比
展示单只股票 vs 指数 的历史走势方差差异（示意）
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

FONT = 'Noto Sans CJK JP'
plt.rcParams['font.family'] = FONT
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(99)
years = 10
days = years * 252

t = np.linspace(0, years, days)

# 指数：年化8%，波动20%
idx_returns = np.random.normal(0.08/252, 0.20/np.sqrt(252), days)
idx_path = 100 * np.exp(np.cumsum(idx_returns))

# 个股A：年化10%，波动40%（好股票）
stk_a_r = np.random.normal(0.10/252, 0.40/np.sqrt(252), days)
stk_a = 100 * np.exp(np.cumsum(stk_a_r))

# 个股B：年化-5%，波动40%（坏股票，散户很可能碰到）
stk_b_r = np.random.normal(-0.05/252, 0.40/np.sqrt(252), days)
stk_b = 100 * np.exp(np.cumsum(stk_b_r))

fig, ax = plt.subplots(figsize=(11, 5))

ax.plot(t, idx_path, linewidth=2.5, color='#2ecc71', label=f'沪深300指数（年化8%，波动20%）→ 终值{idx_path[-1]:.0f}元')
ax.plot(t, stk_a, linewidth=1.5, color='#3498db', alpha=0.8, label=f'个股A·幸运（年化10%，波动40%）→ 终值{stk_a[-1]:.0f}元', linestyle='--')
ax.plot(t, stk_b, linewidth=1.5, color='#e74c3c', alpha=0.8, label=f'个股B·不幸（年化-5%，波动40%）→ 终值{stk_b[-1]:.0f}元', linestyle='--')

ax.axhline(y=100, color='grey', linewidth=1, linestyle=':', alpha=0.5)
ax.text(0.1, 102, '初始本金100元', fontsize=8, color='grey',
        fontproperties=fm.FontProperties(family=FONT))

ax.set_xlabel('年数', fontsize=11)
ax.set_ylabel('资产价值（元）', fontsize=11)
ax.set_title('指数 vs 个股：高波动不等于高收益，分散才能稳定复利', fontsize=12, fontweight='bold', pad=12)
ax.legend(fontsize=8.5, loc='upper left')
ax.grid(True, alpha=0.2, linestyle='--')
ax.set_xlim(0, years)

fig.tight_layout()
fig.savefig('../pic/chapter4_stock_vs_index.png', dpi=150, bbox_inches='tight')
print("saved: chapter4_stock_vs_index.png")
