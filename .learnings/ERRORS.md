# Errors

Command failures and integration errors.

---

## [ERR-20260812-001] pdf_text_extractor.py / markitdown

**Logged**: 2026-08-12T00:00:00+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
两条工具链问题：(1) `uvx markitdown` 在环境中不存在；(2) `pdf-image-text-extractor` 技能的脚本在中文 Windows 控制台（GBK）下因字符编码崩溃。

### Error
```
uvx : 无法将"uvx"项识别为 cmdlet...（CommandNotFoundException）

UnicodeEncodeError: 'gbk' codec can't encode character '\xa9' in position 6768: illegal multibyte sequence
```

### Context
- 命令/操作：`uvx markitdown <pdf> -o out.md`；`python scripts/pdf_text_extractor.py <pdf>`
- 环境：Windows 11 + PowerShell 5.1 + Python 3.13（系统 locale GBK）
- PDF 含 © 等非 GBK 字符，`print(json.dumps(...))` 输出到重定向管道时触发编码错误
- 另：PowerShell 5.1 的 `>` 重定向默认写 UTF-16，后续用 `json.load(open(..., encoding='utf-8'))` 会报 `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff`（BOM），应改用 `$env:PYTHONIOENCODING="utf-8"` + Python 内部处理或 `Out-File -Encoding utf8`

### Suggested Fix
- 技能脚本调用前先设 `$env:PYTHONIOENCODING="utf-8"`
- 需要转换文档时优先用 `pip install markitdown` 安装后调用 CLI，或直接使用 `pypdf`/`pymupdf` 脚本
- PowerShell 重定向到文件用 `Out-File -Encoding utf8`，避免 UTF-16

### Metadata
- Reproducible: yes
- Related Files: C:\Users\26058\.config\opencode\skills\pdf-image-text-extractor\scripts\pdf_text_extractor.py
- See Also: LRN-20260812-001

---
