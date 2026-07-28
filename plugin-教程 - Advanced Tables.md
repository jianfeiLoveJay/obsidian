﻿---
created: 2026-07-28
plugin-id: table-editor-obsidian
plugin-name: Advanced Tables
plugin-author: tgrosinger
rank: "#5"
downloads: 3,054,959
tags: [plugin-tutorial, table, markdown]
---

# Advanced Tables 浣跨敤鏁欑▼

> **鎺掑悕 #5 / 6,081** 路 涓嬭浇閲?**3,054,959** 路 浣滆€咃細tgrosinger

---

## 馃搵 绠€浠?
Advanced Tables锛堟浘鐢ㄥ悕锛歍able Editor锛夎浣犵殑 Markdown 琛ㄦ牸鎿嶄綔鍍?Excel 涓€鏍锋祦鐣呫€傛敮鎸佽嚜鍔ㄦ牸寮忓寲銆佽/鍒楁搷浣溿€佸叕寮忚绠椼€佸唴瀹瑰榻愩€丆SV 瀵煎嚭绛夊姛鑳姐€?
> 馃幆 **鏍稿績瀹氫綅**锛氬皢 Obsidian 鐨?Markdown 琛ㄦ牸鍙樻垚杞婚噺绾х殑鐢靛瓙琛ㄦ牸缂栬緫鍣ㄣ€?
---

## 馃殌 蹇€熶笂鎵?
### 鍒涘缓琛ㄦ牸

杈撳叆 `|鍒楀悕1|鍒楀悕2|` 鐒跺悗鎸?`Tab`锛屾彃浠朵細鑷姩鏍煎紡鍖栬〃鏍肩粨鏋勶紝骞剁户缁坊鍔犱笅涓€鍒椼€?
缁х画杈撳叆 `Tab` 瀹屾垚鍒楁爣棰橈紝鎸?`Enter` 杩涘叆绗竴琛屾暟鎹崟鍏冩牸銆備箣鍚庢瘡涓?`Enter` 鍒涘缓鏂拌銆?
### 鏍稿績蹇嵎閿?
| 蹇嵎閿?| 鍔熻兘 |
|--------|------|
| `Tab` | 璺宠浆鍒颁笅涓€涓崟鍏冩牸 / 鍦ㄦ渶鍚庝竴鍒楄嚜鍔ㄦ柊澧炲垪 |
| `Shift+Tab` | 璺宠浆鍒颁笂涓€涓崟鍏冩牸 |
| `Enter` | 鍦ㄥ綋鍓嶈涓嬫柟鏂板涓€琛?|
| `Ctrl+Shift+D` | 鎵撳紑琛ㄦ牸鎺у埗渚ц竟鏍?|
| 鍦ㄨ〃鏍煎鎸?`Enter` | 閫€鍑鸿〃鏍兼ā寮?|

### 琛ㄦ牸鎺у埗渚ц竟鏍?
鐐瑰嚮琛ㄦ牸宸ュ叿鏍忓浘鏍囨垨鎸?`Ctrl+Shift+D`锛屾墦寮€鎺у埗闈㈡澘锛?- 鎻掑叆/鍒犻櫎鍒?鈥?鍦ㄥ厜鏍囦綅缃墠鍚庢搷浣?- 绉诲姩鍒?鈥?宸︾Щ鎴栧彸绉?- 鎺掑簭鍒?鈥?A鈫抁 鎴?Z鈫扐
- 瀵归綈鏂瑰紡 鈥?宸?涓?鍙冲榻?
---

## 馃幆 鏍稿績鍔熻兘

### 1锔忊儯 鍏紡绯荤粺锛圫preadsheet Formulas锛?
杩欐槸 Advanced Tables 鏈€寮哄ぇ鐨勫姛鑳解€斺€斿湪 Markdown 琛ㄦ牸涓娇鐢ㄥ叕寮忥紒

```markdown
| 椤圭洰     | 閲戦   |
| -------- | ------ |
| 鏀跺叆     | 5000   |
| 鏀嚭     | 3000   |
| 缁撲綑     | =C2-C3 |
| 澧炲€肩◣   | =C4*0.13 |
```

**鏀寔鐨勫嚱鏁帮細**

| 鍑芥暟 | 璇存槑 | 绀轰緥 |
|------|------|------|
| `=SUM(start:end)` | 姹傚拰 | `=SUM(C2:C4)` |
| `=AVG(start:end)` | 骞冲潎鍊?| `=AVG(D2:D10)` |
| `=MAX(start:end)` | 鏈€澶у€?| `=MAX(C2:C10)` |
| `=MIN(start:end)` | 鏈€灏忓€?| `=MIN(C2:C10)` |
| `=COUNT(start:end)` | 璁℃暟锛堟暟瀛楀崟鍏冩牸锛?| `=COUNT(A2:A10)` |
| `=ROUND(value)` | 鍥涜垗浜斿叆 | `=ROUND(C5)` |
| 鍥涘垯杩愮畻 | 鍔?鍑?涔?闄?| `=C2*0.15` |

**鍏紡寮曠敤璇硶锛?*
- 鍒楀瓧姣嶏細`A`, `B`, `C`...
- 琛屾暟瀛楋細`1`, `2`, `3`...
- 鑼冨洿锛歚C2:C10`锛堜粠 C2 鍒?C10锛?
### 2锔忊儯 CSV 瀵煎叆/瀵煎嚭

- **瀵煎叆**锛氫粠 Excel / Google Sheets 澶嶅埗鏁版嵁锛屽湪 Obsidian 涓洿鎺ョ矘璐达紝鑷姩杞负 Markdown 琛ㄦ牸
- **瀵煎嚭**锛氬懡浠ら潰鏉?鈫?"Advanced Tables: Export to CSV" 鈫?淇濆瓨涓?`.csv` 鏂囦欢

### 3锔忊儯 鍒楀榻愭帶鍒?
浣跨敤鍒嗛殧琛屼腑鐨?`:` 鏍囪鎺у埗瀵归綈锛?```markdown
| 宸﹀榻?| 灞呬腑 | 鍙冲榻?|
| :----- | :--: | -----: |
| 鏂囨湰   | 鏂囨湰 | 鏂囨湰   |
```

---

## 馃挕 绉诲姩绔娇鐢?
Obsidian 绉诲姩鐗堟棤娉曚娇鐢?`Tab` / `Enter` 瀵艰埅锛岃В鍐虫柟娉曪細
1. 鎵撳紑鍛戒护闈㈡澘 鈫?鎼滅储 "Advanced Tables"
2. 灏?**Next Cell** 鍜?**Next Row** 鍛戒护娣诲姞鍒扮Щ鍔ㄧ宸ュ叿鏍?3. 鎴栦娇鐢ㄤ晶杈规爮鐨勫鑸寜閽?
---


## ⚙️ 设置选项详解

在 Obsidian 设置 → 社区插件 → Advanced Tables 下可配置：

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Auto-formatting** | ✅ 开启 | 自动对齐列宽，保持表格美观 | ✅ 开启 |
| **Auto-continue list** | ✅ 开启 | 行尾按 Enter 自动新增行 | ✅ 开启 |
| **Table toolbar** | ✅ 开启 | 在编辑器顶部显示表格工具栏 | ✅ 开启 |
| **Format on paste** | ✅ 开启 | 粘贴时自动格式化粘贴的表格数据 | ✅ 开启 |
| **Tab key behavior** | 
ext_cell | Tab 键行为：
ext_cell（下一格）/ insert_row（插入行）/ insert_column（插入列） | 
ext_cell |
| **Enter key behavior** | 
ext_row | Enter 键行为：
ext_row（下一行）/ alse（不操作） | 
ext_row |
| **Auto cell selection** | ✅ 开启 | 进入表格时自动选中首个单元格 | ✅ 开启 |

### 公式引擎设置

| 设置项 | 默认值 | 说明 | 推荐 |
|--------|--------|------|------|
| **Enable formulas** | ✅ 开启 | 启用 =SUM(C2:C10) 公式计算 | ✅ 开启 |
| **Formula precision** | 2 | 公式计算结果的小数位数 | 2 |
| **Formula error display** | ERROR | 公式出错时的显示文字 | ERROR |

### CSV 导入/导出

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **CSV delimiter** | CSV 文件的分隔符，默认 , | ,（逗号分隔） |
| **Export with header** | 导出 CSV 时包含表头行 | ✅ 开启 |

### 移动端设置

| 设置项 | 说明 | 推荐 |
|--------|------|------|
| **Mobile toolbar** | 在移动端编辑器显示表格工具栏按钮 | ✅ 开启 |
| **Mobile swipe to navigate** | 在移动端通过滑动在单元格间导航 | ✅ 开启 |

---

## 馃敆 璧勬簮

| 璧勬簮 | 閾炬帴 |
|------|------|
| GitHub 浠撳簱 | https://github.com/tgrosinger/advanced-tables-obsidian |
| 鍏紡浣跨敤甯姪 | https://github.com/tgrosinger/advanced-tables-obsidian/blob/main/docs/help.md |
| 闂鍙嶉 | https://github.com/tgrosinger/advanced-tables-obsidian/issues |

---

> 馃摑 鏈枃妗ｇ敱 Claudian 妫€绱㈠畼鏂规枃妗ｅ悗琛ュ厖瀹屾暣 路 鏈€鍚庢洿鏂?2026-07-28

