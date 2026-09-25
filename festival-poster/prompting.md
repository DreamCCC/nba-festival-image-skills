# 写 prompt

`gpt-image-2.5-sunburst` 读得懂完整的句子和因果关系。把 prompt 写成一段给摄影师或印刷师的制作说明，而不是一串关键词。

## 结构

每段 prompt 用英文，150 到 250 词，按下面的顺序写：

1. **画幅与媒介**：`Vertical 2:3` 加上具体媒介，例如 `documentary photograph on 35mm colour film`。
2. **创意**：主体是什么，以及它为什么同时是节日符号。用 `so it reads as ... and ... at once` 把双重读法直接告诉模型。
3. **构图**：主体的位置和大小，留白在哪里。
4. **材料与工艺**：纸张、油墨、胶片、织物、磨损。
5. **光线与色彩**：光源方向，以及不超过三种直接写出名字的主色。
6. **文案**：引号里写精确原文加 `exactly and only`，并写明字体气质、大小和位置，中文写明 `in Simplified Chinese characters`。见 [copy.md](copy.md)。
7. **Logoman**：[logoman.md](logoman.md#标准句) 的标准句。
8. **排除项**：一句短的排除，只写这张图真正可能出错的东西，例如 `No other logos, no team marks, no other text`。

## 写法

- 用具体名词，少用形容词。`a navy padded stanchion base` 胜过 `a beautiful basketball element`。
- 一段只写一个画面、一个机关。
- 不写 [design.md](design.md#去-ai-味) 里列出的 AI 味词汇。
- 排除项写短。长串的 `no ...` 反而会把那些东西带进画面。

## 范例

下面两段已经实际生成并通过验收，第二段在原版基础上补了一行文案。只学结构，不要照抄概念和文案。

**瑞士字体海报，文案是主标题，品牌标记**

```text
Vertical 2:3 Swiss International Style typographic poster for the NBA Mid-Autumn Festival, printed in two flat inks, deep navy and warm moon ivory, on smooth matte paper. One word dominates the grid: "HOME" set in an enormous condensed bold grotesk, tightly kerned, spanning the full width across the middle of the poster. The letter O is not drawn as a letter: it is the round orange NBA regulation rim seen straight from below, the white net hanging inside it, and through the rim glows a pale full moon - so the word reads as home court, coming home for the reunion, and the moon at once. Below, in small light grotesk aligned to the left margin, the exact line "MID-AUTUMN 2026". Strict grid, generous margins, no other text. Brand mark: the attached image is the official NBA Logoman. Reproduce it exactly as supplied - tall rounded rectangle, blue left half, red right half, white dribbling-player silhouette, thin white outline - flat and full colour, not redrawn or restyled, small in the top-right corner at about 6% of the poster height, aligned to the grid. No other logos, no team marks.
```

**纪实摄影，文案是底部一行小字，真实载体**

```text
Vertical 2:3 documentary sports photograph on 35mm colour film, an empty NBA arena late at night after the Mid-Autumn Festival game. All house lights are off except one round work light high above center court; its reflection on the polished maple hardwood forms a soft full moon on the floor. In the right foreground, slightly out of focus, stands the navy padded base of the basket stanchion. The attached image is the official NBA Logoman: it is printed on the flat front face of this padding exactly as supplied - correct proportions, blue left, red right, white player silhouette, thin white outline - sharp, upright and undistorted, about 8% of the frame height, the way it appears on real arena padding. In the dark lower margin, one small restrained line in Simplified Chinese characters, set in a light sans serif like a newspaper photo caption: "最后一盏灯，留给月亮" exactly and only. Quiet, restrained, available light, natural film grain, no people, no other logos, no team marks, no other text.
```
