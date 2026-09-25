---
name: festival-poster
description: 为一个已确定的中美节日制作一批 6 张 NBA 主视觉。从节日里真实的人的行为出发，让 NBA 资产与节日变成同一个画面，六张六种风格，由 gpt-image-2.5-sunburst 参照官方 Logoman 直接生成。
---

# 节日主视觉

一次任务只做一个节日的一批 6 张图。目标是内部同事愿意直接发布的主视觉：一眼是 NBA，再看是这个节日，而且不俗。

## 工作流

复制这份清单，逐项完成：

```text
- [ ] 1. 读任务：节日、补充要求、此前概念、此前来源
- [ ] 2. 检索：至少 6 个真实页面，写下 3 条节日洞察
- [ ] 3. 概念卡：六张各一张卡，通过自检表
- [ ] 4. 写 prompt：每张一段英文 prompt
- [ ] 5. 生图：scripts/generate.py
- [ ] 6. 验收：逐张看图，不合格就重做该张
- [ ] 7. 回信封
```

### 1. 读任务

任务里会给出节日名称、日期、地区、含义，以及两段附加信息：

- **同事的补充要求**：本批必须落实。落实方式见 [design.md](design.md#补充要求)。
- **此前批次的概念与来源**：本批的概念、机关、主资产组合都不能重复，来源尽量换新。

### 2. 检索

按 [research.md](research.md) 检索。产出 3 条节日洞察：这个节日里人们真实在做的事，而不是节日符号。

### 3. 概念卡

按 [design.md](design.md) 为每张图写一张卡：

| 字段 | 内容 |
|---|---|
| 洞察 | 取自第 2 步的哪条洞察 |
| 主资产 | 一个 NBA 资产 |
| 机关 | 一句话说清双重读法：它是什么，同时又是什么 |
| 风格 | 从 [styles.md](styles.md) 选一种 |
| 文字 | 精确原文，或"无" |
| Logoman | 放法与位置，见 [logoman.md](logoman.md) |

写完六张卡后过一遍自检表，任何一项不满足就改卡，不要带着问题去生图：

- [ ] 六个机关互不重复，也不重复此前批次
- [ ] 主资产至少四种
- [ ] 六种风格互不相同，主色调至少三组
- [ ] 带字和无字的作品各至少两张
- [ ] 每张的节日含义都由 NBA 资产本身承担，没有并排摆放的节日符号
- [ ] 有补充要求时，六张都落实了

### 4. 写 prompt

按 [prompting.md](prompting.md) 的结构写英文 prompt。每张都必须包含 [logoman.md](logoman.md#标准句) 里的 Logoman 标准句。

### 5. 生图

把六段 prompt 写进 `prompts.json`，格式为 `[{"id": 1, "prompt": "..."}]`，然后运行：

```bash
python festival-poster/scripts/generate.py prompts.json results.json --out-dir /tmp/posters
```

脚本做四件事：

- 调用 `gpt-image-2.5-sunburst`，尺寸 `1024x1536`。
- 自动附上官方 Logoman 参考图 `assets/logoman-reference.png`。
- 三路并发，失败的自动重试一次。
- 把成图存到 `--out-dir` 供你查看，`content_url` 写入 `results.json`。

密钥只从环境变量 `AIHUBMIX_API_KEY` 读取。任务若以 `AIHUBMIX_API_KEY=` 单独给出，先 `export` 到当前 shell 再运行脚本。不要回显、保存或复述密钥。

### 6. 验收

逐张打开 `--out-dir` 里的图，对照下表检查：

| 检查项 | 不合格的样子 |
|---|---|
| 机关 | 需要解释才看懂，或者变成了元素并排 |
| NBA 辨识 | 只是一张普通篮球图 |
| Logoman | 比例、左蓝右红、白色剪影、白色描边与参考图不一致；被裁切、遮挡、变形；出现第二个标志 |
| 文字 | 错字、多字、乱码，或无字作品里冒出字符 |
| 质感 | 塑料感、过度光效、漂浮物体、廉价渐变 |
| 风格 | 和同批另一张撞了 |

不合格就改 prompt，把该张单独写进一个新的 prompts 文件重跑。重跑后仍保持六张。`content_url` 约 30 分钟失效，最后一次生成完成后尽快回信封。

### 7. 回信封

按 [reference/output-envelope.md](../reference/output-envelope.md) 返回，信封之外不输出任何内容。
