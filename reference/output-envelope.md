# 输出信封

最终回复只能包含下面三段，不要使用 Markdown 代码围栏。

```text
===POSTERS===
{json}
===NOTES===
每条来源一行：标题 | URL | 从中取用的具体方法
===MANIFEST===
posters: 6
sources: N
```

`===POSTERS===` 是一个 JSON 数组，固定 6 个对象，顺序即展示顺序，把最强的一张放在第一个：

```json
[
  {
    "title": "概念名，中文不超过 8 个字或英文不超过 5 个词",
    "style": "风格名，取自 styles.md，例如 Risograph 双色印刷",
    "has_text": false,
    "asset": "主资产，例如 球架护垫",
    "fusion": "一句话说清双重读法：它是什么，同时又是什么",
    "logoman": "Logoman 的放法与位置，例如 印在前景球架护垫上",
    "prompt": "实际发给 img2.5 的完整英文 prompt",
    "content_url": "results.json 里该张的 content_url"
  }
]
```

- `has_text` 表示成图里是否有可读文字。
- `content_url` 原样填写，不要改写、缩短或重新托管。它约 30 分钟失效，最后一次生成完成后尽快返回信封。
- 某张没有拿到 `content_url` 时重做该张，不要留空。
- 生图脚本整体无法运行（例如缺少 `AIHUBMIX_API_KEY`）时，`===POSTERS===` 返回 `[]`，`===NOTES===` 只写错误原文。
