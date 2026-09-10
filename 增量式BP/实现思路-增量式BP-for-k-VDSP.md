---
title: k-VDSP 增量式 BP 实现思路
date: 2026-09-10
tags: [research, belief-propagation, 增量式BP, k-VDSP, 实现]
status: 草案
paper_id: 22
base_paper: (9)2022[Dai, Guo, ..] - Iterative message passing alg for vertex disjoint shortest paths
---

# k-VDSP 增量式 BP：实现思路

> 目标：在 Dai 2022（k-VDSP，第 22 篇）的 Min-Sum BP 框架上，叠加增量式机制——图/参数发生局部变化时复用旧消息，避免从零重跑。
> 依赖论文：[[增量式BP/(1)2006[Elidan, ..] - Residual Belief Propagation Informed Scheduling for Asynchronous Message Passing.pdf|RBP(2006)]]、[[增量式BP/(2)2007[Sutton, ..] - Improved Dynamic Schedules for Belief Propagation.pdf|动态调度(2007)]]、[[增量式BP/(9)2015[Gatterbauer, ..] - Linearized and Single-Pass Belief Propagation.pdf|单遍线性化(2015)]]、[[增量式BP/(10)2010[Nath, ..] - Efficient Belief Propagation for Utility Maximization and Repeated Inference.pdf|EFBP 重复推理复用(2010)]]、[[增量式BP/(3)2021[Wu, ..] - Streaming Belief Propagation for Community Detection.pdf|流式 BP(2021)]]。

## 1. 问题与基线（Dai 2022）速览

**IP 形式**：有向图 G=(V,E,w)，w_e ≥ 0，源 s、汇 t，求 k 条内部顶点不相交的 s-t 路径使总权最小。

- 变量 x_e ∈ {0,1}（弧 e 是否被选）
- 流量守恒：Σ_{j∈N+ᵢ} x_ij − Σ_{j∈N−ᵢ} x_ji = f_i，f_s = k，f_t = −k，其余 f_i = 0
- 顶点不相交（度约束）：内部顶点 Σ_out x + Σ_in x ≤ 2
- 目标：min Σ w_e·x_e

**因子图**：变量节点 = 弧 e；因子节点 = 顶点 i（约束 ψ_i）；边 (e,i) 当 e 与 i 关联。φ_e(x_e) = w_e·x_e（0/1 否则 +∞）。

**消息（min-sum）**：对弧 e = (i,j)，
- m_{e→j}(x_e) = φ_e(x_e) + m_{i→e}(x_e)
- m_{i→e}(x_e) = min_{x_{E_i\e}} [ ψ_i(x_{E_i}) + Σ_{e′∈E_i\e} m_{e′→i}(x_{e′}) ]

**信念**：b_e(x_e) = m_{e→i}(x_e) + m_{e→j}(x_e) − φ_e(x_e)；解码 x_e = argmin b_e。

**收敛定理（Thm 1）**：唯一最优 x* 时，同步调度 Q ≥ (⌈U/(2o(x*))⌉+1)n 轮收敛到 x*；整数权时 O(n²·w_max) 伪多项式轮。（U = 残差网络 G^x* 中最重简单路径，o(x*) = 最轻有向环。）

## 2. 关键化简：消息只需一个标量 δ

消息 m_{i→e}(x_e) 只取 x_e = 0/1 两个值，绝对偏移不影响信念差，故每条**有向半消息**只存一个 δ：

- δ_{i→e} := m_{i→e}(1) − m_{i→e}(0)（顶点 i → 弧 e）
- δ_{e→i} := m_{e→i}(1) − m_{e→i}(0) = w_e + δ_{j→e}（弧 e → 顶点 i，j 为另一端点）

**局部闭式更新**（核心）：

内部顶点 i（in = out 且 in+out ≤ 2，即不用或用 1 进 1 出）：
令 p_in = min{δ_{a→i} : a ∈ IN_i}，p_out = min{δ_{b→i} : b ∈ OUT_i}；上标 −e 表示排除 e。

- 若 e ∈ IN_i：δ_{i→e} = p_out − min(0, p_in⁻ᵉ + p_out)
- 若 e ∈ OUT_i：δ_{i→e} = p_in − min(0, p_in + p_out⁻ᵉ)

源点 s（恰好 k 条出弧）：δ_{s→e} = T(k−1, OUT_s\{e}) − T(k, OUT_s\{e})
其中 T(j, S) = S 中 j 个最小 δ 之和（|S| < j 则 +∞）。汇点 t 对称（用 IN_t）。

**信念差**：Δ_e := b_e(1) − b_e(0) = w_e + δ_{i→e} + δ_{j→e}
解码：x_e = 1 ⇔ Δ_e < 0（平局取 0）。

> 复杂度：每个半消息 O(deg)；工程上用“顶点级排序缓存”（每顶点维护 IN/OUT 的 δ 排序表、top-2、前缀和），单次更新 O(log deg)，s/t 的 top-k 用带后缀和的小根堆 O(log deg)。

## 3. 增量式三个档位（论文 → 机制映射）

| 档位 | 触发 | 用的论文 | 机制 |
|---|---|---|---|
| A | 收敛太慢（有环/异步） | RBP(1)、动态调度(2) | 残差驱动异步调度：每次只更新最大残差的消息 |
| B | 图局部变化（权变、加删边/点） | EFBP(10)、单遍(9) | warm-start 旧 δ + 影响区域传播 |
| C | 参数变化（k→k±1、多源汇 f 变化） | 增量推理(4)、流式(3) | 只重算直接受 f 影响的顶点（s、t），其余全部复用 |

**关键认识**：调度策略不改变不动点，只改变到达速度；warm-start 不改变不动点，只减少无效初始消息。所以三档可自由叠加，正确性仍由 sync-BP 的 Dai 定理兜底。

## 4. 主循环：残差驱动 + 影响队列（伪代码）

```
数据结构：
  delta[(dir)]          # 半消息 δ：dir ∈ {(i→e), (e→i)}
  PQ                    # 最大堆，键 = 残差 r = |δ_new − δ_old|
  eps                   # 停止阈值（如 1e-9 · 权数量级）
  lambda                # 阻尼（0.5），抑制循环振荡

初始化：
  # 冷启动：全部 δ = 0，所有 (i→e) 入队（残差 +∞）
  # 热启动：载入缓存 δ；只有“受影响半消息”入队（见 §5）

主循环：
  while PQ 非空:
    (i→e) = PQ.pop()
    old = delta[i→e]
    delta_new[i→e] = 局部更新(i, e)      # §2 闭式公式
    if |delta_new − old| <= eps: continue
    delta[i→e] = damp(old, delta_new)    # (1−λ)·old + λ·new
    # 传播：对偶半消息 + 邻居
    push(e→j, r = |Δδ|)                  # δ_{e→j} = w_e + δ_{i→e}
    for e′ in E_j \ {e}: push(j→e′, 由重算测得残差)

停止判定：
  PQ 空 或 max residual < eps 时：
    x = 解码(Δ_e)
    if 可行(x): return x
    else: 继续跑（降 eps）或加多轮同步兜底
```

## 5. 三种增量触发的“受影响集”

**A. 单条弧权重变化** w_e → w_e + Δ
直接改 δ_{e→i} += Δ、δ_{e→j} += Δ（等价于 w_e 变了），两条半消息以残差 |Δ| 入队 → RBP 自行扩散。局部扰动时扩散范围通常远小于全图。

**B. 加边/删边（或加点/删点）**
- 加弧 e=(i,j)：给 i、j 的 IN/OUT 集插入 e，初始化 δ = 0，把 i、j 的所有出半消息 (i→·)、(j→·) 以大残差入队。
- 删弧：先从 IN/OUT 集移除，再把 i、j 受影响消息入队。
- 注意维护顶点级排序缓存（删除可用 lazy deletion）。

**C. k 变化（或需求向量 f 变化）**
- f 只在 ψ_s、ψ_t 里出现，内部顶点公式不含 f！
- k→k+1：只重算 δ_{s→e}（OUT_s 全部）与 δ_{t→e}（IN_t 全部），入队 → 扩散。
- 多源/多汇扩展（Dai §V）：源点 f_i = 1 改“恰好选 1 条出弧”等，T(j,S) 的 j 换成 |f_i|，其余不变。结论：f 稀疏变化 ⇒ 复用收益最大。

## 6. 解码、可行性校验与后处理

1. 解码：x_e = 1 ⇔ w_e + δ_{i→e} + δ_{j→e} < 0。
2. 校验：
   - s 出度 = k，t 入度 = k；
   - 内部顶点 in = out 且 in+out ≤ 2；
   - 从 s 做 DFS/BFS 追出 k 条 s-t 简单路径。
3. 后处理：非负权下最优解必不含环，但 BP 中途（残差未清零时）可能解码出孤立有向环——把环从答案中剔除（有向环检测，如 Kahn/DFS 找环并删去）。
4. 若解码不可行：继续迭代（降 eps）或 λ 阻尼重跑；仍失败 → 同步全扫几轮兜底（Dai 定理的调度形式）。

## 7. 工程实现步骤（建议顺序）

1. 数据结构层：顶点弧表、IN/OUT 集、半消息 δ 数组、顶点级排序缓存。
2. 局部闭式更新：内部顶点（top-2 公式）、s/t（top-k 公式）——先用朴素 O(deg²) 验证正确性，再优化。
3. 同步 BP（Dai Alg.1 复现）：确认能复现论文收敛（小图 + 唯一最优）。
4. RBP 调度：优先队列版，与同步版对拍（应收敛到同一结果）。
5. Warm-start + 受影响集：实现 §5 三类触发。
6. 解码 + 校验 + 环剔除。
7. 实验与基线（§8）。

## 8. 验证方案

**精确基线（重要）**：无路径长度约束的 k-VDSP 本身是**多项式可解**的——顶点拆点（每内部顶点拆 v_in→v_out，容量 1）+ 最小费用流（networkx min_cost_flow 或 scipy milp）即得精确最优（Suurballe 思路）。论文中“强 NP-难”论断源自它引用的 Itai et al. 1982（带长度/预算约束的变体或最大化版本），论文自己也承认运行时间不优于现有算法（§VI）。因此：

- 正确性对照：小图随机权重，BP 解代价 vs 最小费用流最优代价，必须相等。
- 效率对照（增量卖点）：把二者在“变化后重解”场景对比，BP 热启动只重算影响区域；费用流必须全图重跑（除非上动态最短路，那是另一条技术路线）。
- 图类型：Erdős–Rényi 有向图、分层 grid、随机加权有环图；规模 n = 20/50/100。
- 变化类型：单边权变、10% 边权变、加删边、k → k+1。
- 指标：消息更新次数、等效迭代轮数（= 更新数/消息总数）、墙钟时间、代价差、可行率；冷启动 vs 热启动对比。
- 消融：λ 阻尼开/关；同步 vs RBP vs RBP+热启动。

## 9. 理论边界与风险

- **不动点不变**：调度与 warm-start 都只是“到达路径”不同，Dai 定理的最坏轮数上界仍适用（sync 调度是保底）。
- **唯一最优假设**：多最优时 BP 可能振荡/不收敛；实验上加极小微扰打破对称。
- **RBP 收敛性**：循环图上无普遍保证，λ 阻尼是标准缓解手段；Sutton-McCallum(2) 的“信念变化”调度可作备选调度器。
- **δ 标量化的正确性**：绝对偏移被丢弃，只影响信念差，不影响 argmin；实现时先完整 2 值消息对拍再切换 δ。
- **数值**：δ 可正可负、量级随迭代增长；用浮点 + 相对残差阈值，必要时对 δ 做整体平移（减去公共均值）防溢出。

## 10. 与将来的衔接

- 若图本身是“流式到达”（节点随时间加入）：用 (3) 的思想——每到达一个节点只做常数次更新（受限预算），再周期性后台 full sweep 修正。
- 若消息数量爆炸：用 (9) 的线性化思路，把 δ 更新写成单遍线性近似（牺牲精度换吞吐）。
- 与导师 Dai 2022 主线对齐：增量场景可直接做成“k-VDSP 动态图上的 BP with warm start”小论文实验章。

---
*待办：先跑通 §7 第 3 步同步 BP 复现，再进增量。*
