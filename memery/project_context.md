---
name: investment-tutorial-project
description: 投资理财中文教程项目的完整上下文，面向程序员读者
metadata:
  type: project
---

# 项目：投资理财入门教程（写给程序员）

## 目标
编写一本零基础中文投资理财教程，面向金融认知为零的程序员群体。

**Why:** 程序员群体有逻辑思维但缺乏金融基础认知，需要从第一性原理出发系统讲解。

**How to apply:** 写作时保持简洁、逻辑清晰，类比程序员熟悉的概念，避免金融行业黑话堆砌。

---

## 目录结构

```
/mnt/data2/investment/
├── doc/          # 所有 Markdown 文档（index.md + chapter*.md + appendix*.md）
├── pic/          # 生成的图像（.png）
├── code/         # 绘图 Python 脚本（plot_chapterN_*.py）
└── memery/       # 本记忆文件夹（注意拼写为 memery）
```

---

## 章节列表

| 文件 | 内容 |
|------|------|
| doc/index.md | 目录总览 |
| doc/chapter1.md | 为什么要投资（通胀、复利） |
| doc/chapter2.md | 金融市场全景图 |
| doc/chapter3.md | 必懂的基础概念 |
| doc/chapter4.md | 股票 |
| doc/chapter5.md | 基金 |
| doc/chapter6.md | 黄金 |
| doc/chapter7.md | 债券与其他资产 |
| doc/chapter8.md | 宏观经济与市场节奏 |
| doc/chapter9.md | 信息获取与工具 |
| doc/chapter10.md | 开户与实操流程 |
| doc/chapter11.md | 投资策略与资产配置 |
| doc/chapter12.md | 投资心理与常见误区 |
| doc/appendix_a.md | 推荐书单 |
| doc/appendix_b.md | 术语速查表 |

---

## 技术约定

- **中文字体**：matplotlib 使用 `Noto Sans CJK JP`（已验证可用）
- **图像格式**：PNG，dpi=150，存放于 `pic/`
- **代码命名**：`code/plot_chapter{N}_{描述}.py`
- **图像命名**：`pic/chapter{N}_{描述}.png`
- **文档引用图**：`![描述](./pic/chapter{N}_{描述}.png)`

---

## 写作风格要求

- 面向读者：程序员，金融认知为零
- 语言：中文，简洁，意简言赅
- 结构：先宏观，再具体细节
- 图文结合：重要概念配图说明
- 引用：多引用有公信力的方法论（巴菲特、指数投资、行为金融学等）
- 不写代码示例（纯金融教育内容）

---

## 状态（最后更新：2026-05）

- [x] 目录结构创建
- [x] index.md 完成
- [x] chapter1-12 全部完成
- [x] appendix_a（书单）、appendix_b（术语表）完成
- [x] 16张配图全部生成（Python 绘图，Noto Sans CJK JP 字体）
- [x] 16个 Python 绘图脚本存入 code/

## 图片清单

| 图片文件 | 对应章节 | 内容 |
|----------|---------|------|
| chapter1_inflation.png | Ch1 | 通胀侵蚀购买力（20年对比） |
| chapter1_compound.png | Ch1 | 复利增长曲线（30年4种收益率） |
| chapter2_asset_map.png | Ch2 | 资产风险-收益散点图 |
| chapter2_market_radar.png | Ch2 | A股/港股/美股雷达对比图 |
| chapter3_risk_return.png | Ch3 | 不同资产收益分布（正态分布） |
| chapter3_pe_ratio.png | Ch3 | PE市盈率直觉说明 |
| chapter4_kline.png | Ch4 | K线图基础讲解 |
| chapter4_stock_vs_index.png | Ch4 | 个股 vs 指数波动对比 |
| chapter5_active_vs_passive.png | Ch5 | 主动 vs 被动基金费率侵蚀 |
| chapter5_dca.png | Ch5 | 定投平摊成本原理 |
| chapter6_gold.png | Ch6 | 黄金与美元指数 + 四种投资方式 |
| chapter7_bonds.png | Ch7 | 债券价格-利率关系 + 类型对比 |
| chapter8_cycle.png | Ch8 | 经济周期四阶段 + 利率与股市 |
| chapter11_portfolio.png | Ch11 | 三种典型配置方案饼图 |
| chapter11_rebalance.png | Ch11 | 再平衡效果模拟 |
| chapter12_behavior.png | Ch12 | 损失厌恶曲线 + 行为差距 |
