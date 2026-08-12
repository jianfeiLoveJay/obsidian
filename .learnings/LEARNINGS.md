# Learnings

Corrections, insights, and knowledge gaps captured during development.

**Categories**: correction | insight | knowledge_gap | best_practice

---

## [LRN-20260812-001] correction

**Logged**: 2026-08-12T00:00:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
处理 PDF/图片文字提取前，必须先检查并优先调用 `pdf-image-text-extractor` 技能，不能跳过技能直接自写脚本。

### Details
用户要求提取论文 PDF（Factor Graphs and the Sum-Product Algorithm）文字。当时流程错误：
1. 先加载 `markdown-converter` 技能 → `uvx` 未安装，路径失败；
2. 失败后**没有回头检查其他技能**，直接手动 `pip install pypdf` 写脚本提取；
3. 用户指出：可用技能里有 `pdf-image-text-extractor`（覆盖"PDF 文字提取"，自带 PyMuPDF 脚本），却未被调用。

正确流程应为：
1. 检查可用技能列表，命中 `pdf-image-text-extractor`（触发词：PDF/图片提取文字、OCR）；
2. 优先调用技能自带脚本 `scripts/pdf_text_extractor.py`；
3. 不满意再 fallback 自写脚本并对比。

结果对比（本文）：技能版（PyMuPDF）96,793 字符，带标题层级检测（>16pt 标 `##`），但对 IEEE 双栏对齐排版有逐词断行问题；自写 pypdf 版 95,942 字符，文本连续性更好。最终入库为 pypdf 版。

### Suggested Action
涉及"PDF/图片/OCR 提取文字"任务时，第一步检查技能列表并优先调用 `pdf-image-text-extractor`，仅在技能输出不理想时自写脚本对比；调用该技能脚本前需设 `PYTHONIOENCODING=utf-8`（见 ERR-20260812-001）。

### Metadata
- Source: user_feedback
- Related Files: C:\Users\26058\.config\opencode\skills\pdf-image-text-extractor\SKILL.md
- Tags: pdf, text_extraction, skill_usage, process
- See Also: ERR-20260812-001

---
