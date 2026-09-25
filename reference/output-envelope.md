# 输出信封

最终回复只能包含下面三段，不要使用 Markdown 代码围栏。

```text
===POSTERS===
{json}
===NOTES===
检索摘要。每条来源一行：标题 | URL | 从中取用的具体方法。
===MANIFEST===
posters: 3
sources: N
```

`===POSTERS===` 是一个 JSON 数组，固定 3 个对象：

```json
[
  {
    "title": "四个字以内的概念名",
    "fusion": "同一个物体如何同时是 NBA 资产和节日符号",
    "prompt": "实际发给 img2.5 的完整英文 prompt",
    "content_url": "接口返回的 content_url，没有则为空字符串",
    "b64_json": "仅当没有 content_url 时填写，否则为空字符串"
  }
]
```

`content_url` 约 30 分钟失效。生成完成后立刻把地址写入信封，不要改写、缩短或重新托管。
