# nba-festival-image-skills

NBA 内部节日主视觉的固定方法库。网站每生成一批图，就新建一个 Cursor Cloud Agent（Claude Opus 5.5），把本仓库作为唯一绑定仓库。Agent 按这里的方法检索、构思，并调用 `gpt-image-2.5-sunburst` 出图。本仓库不保存密钥、节日日历或成图。

## 分工

| | 网站工程仓 | 本仓库 |
|---|---|---|
| 内容 | 节日日历、每日扫描、刷新批次、历史记录、页面、成图存储 | 设计方法、风格池、Logoman 用法、检索纪律、生图脚本 |
| 读者 | 内部同事 | Cursor Agent |
| Agent 可见 | 否 | 是，只读 |
| 变更节奏 | 跟随产品迭代 | 方法定稿并实测后才改 |

## 结构

```text
AGENTS.md                      Agent 契约：开工顺序与不可让步的规则
festival-poster/
  SKILL.md                     工作流与验收
  research.md                  检索：三条线、来源、记录方式
  design.md                    融合公式、机关类型、NBA 资产、免俗、补充要求、去 AI 味
  styles.md                    风格池与各风格的文案位置
  copy.md                      每张一句应景文案的写法
  logoman.md                   Logoman 的三种放法、标准句、已验证案例
  prompting.md                 prompt 结构与范例
  scripts/generate.py          调用 img2.5，自动附上 Logoman 参考图
assets/logoman-reference.png   官方 Logoman 参考图
reference/output-envelope.md   返回给网站的信封格式
```

## 一批图怎么来

1. 网站把节日、同事的补充要求、此前批次的概念与来源写进任务，新建 Agent。
2. Agent 做两轮并行检索，列 10 个候选，选出六张写成概念卡，自检通过后写 prompt。每张都有巧妙结合、一句文案和官方 Logoman。
3. `generate.py` 带着 Logoman 参考图调用 img2.5，Logoman 在生成时直接进入画面。
4. Agent 看图验收，不合格的重做，最后返回信封。
5. 网站下载成图并存档。

每次刷新都是新的 Agent，不共用会话。防止风格重复靠网站把此前批次的概念和来源写进任务，而不是依赖聊天记录。

## 铁律

1. 只放稳定方法。API Key、成图、运行日志不进仓库。唯一的图片是 Logoman 参考图。
2. 仓库保持 private。网站绑定 `main`，推送前先在一个真实节日上跑通。
3. Agent 只读本仓库。产物通过文本信封返回网站，不提交、不开 PR。
4. 网站创建 Agent 时固定 `autoCreatePR: false`。
