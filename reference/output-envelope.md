# 输出信封

最终回复只能包含下面三段，不要使用 Markdown 代码围栏。

```text
===POSTERS===
{json}
===NOTES===
检索摘要。每条来源一行：标题 | URL | 从中取用的具体方法。
===MANIFEST===
posters: 6
sources: N
```

`===POSTERS===` 是一个 JSON 数组，固定 6 个对象：

```json
[
  {
    "title": "概念名，中文不超过 8 个字或英文不超过 5 个词",
    "style": "风格名，例如 Risograph 双色印刷",
    "has_text": false,
    "fusion": "同一个物体如何同时是 NBA 资产和节日符号",
    "logo_position": "top-right",
    "prompt": "实际发给 img2.5 的完整英文 prompt",
    "content_url": "接口返回的 content_url，没有则为空字符串",
    "b64_json": "仅当没有 content_url 时填写，否则为空字符串"
  }
]
```

- `has_text` 表示成图里是否有可读文字。
- `logo_position` 只能是 `top-left`、`top-right`、`bottom-left`、`bottom-right`、`top-center`、`bottom-center` 之一，并且必须和该张 prompt 里预留的区域一致。
- `content_url` 约 30 分钟失效。生成完成后立刻把地址写入信封，不要改写、缩短或重新托管。
