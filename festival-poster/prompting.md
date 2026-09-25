# 写 prompt

`gpt-image-2.5-sunburst` 读得懂完整的句子和因果关系。把 prompt 写成一段给摄影师或印刷师的制作说明，而不是一串关键词。

## 结构

每段 prompt 用英文，150 到 250 词，按下面的顺序写：

1. **画幅与媒介**：`Vertical 2:3` 加上具体媒介，例如 `sports photograph with high-speed flash`。
2. **创意**：主体是什么，以及它为什么同时是节日符号。用 `so it reads as ... and ... at once` 把双重读法直接告诉模型。
3. **构图**：主体的位置和大小，动势朝哪个方向。
4. **材料与工艺**：纸张、油墨、胶片、织物、磨损。
5. **光线与色彩**：明亮的光源，以及不超过三种直接写出名字的明亮主色，见 [design.md](design.md#品牌调性)。
6. **文字**：主文案和节日落款各一句，分别用引号写精确原文加 `exactly and only`，写明字体、大小、位置和对齐方式，中文写明 `in Simplified Chinese characters`，并写上 `no outline, no shadow, no glow`。见 [copy.md](copy.md#版式)。
7. **Logoman**：[logoman.md](logoman.md#标准句) 的标准句。
8. **排除项**：一句短的排除，只写这张图真正可能出错的东西，例如 `No other logos, no team marks, no other text`。

## 写法

- 用具体名词，少用形容词。`a red padded stanchion base` 胜过 `a beautiful basketball element`。
- 一段只写一个画面、一个机关。
- 不写 [design.md](design.md#去-ai-味) 里列出的 AI 味词汇。
- 排除项写短。长串的 `no ...` 反而会把那些东西带进画面。

## 篮球

写实画面里出现篮球时，按 [design.md](design.md#nba-资产) 写成 Wilson 官方比赛用球，并把排除项里的 `No other logos` 改成例外写法：

```text
an official Wilson NBA game ball - deep orange-brown pebbled leather, black channels, the black Wilson script wordmark crisply printed on the panel facing the camera, the ball's own league logo turned away out of view
```

```text
No other logos except the Wilson script on the ball.
```

## 范例

下面两段是按品牌调性写成的结构范例：明亮、克制、一个主体，主文案不复述机关。只学结构，不要照抄概念和文案。

**瑞士字体海报，字就是机关，落款对齐网格，品牌标记**

```text
Vertical 2:3 Swiss International Style typographic poster for the NBA Mid-Autumn Festival, printed in two bright flat inks, NBA red and sunny yellow, on crisp white paper. One word dominates the grid: "HOME" set in an enormous condensed bold grotesk, tightly kerned, tilted slightly upward as if in motion, spanning the full width across the middle of the poster. The letter O is not drawn as a letter: it is the round orange NBA regulation rim seen straight from below, the white net swinging inside it, and through the rim sits a warm golden full moon - so the word reads as home court, coming home for the reunion, and the moon at once. The word itself is the headline. Below it, aligned to the left margin, small and widely letter-spaced in NBA red Song-style Simplified Chinese characters: "八月十五 · 中秋快乐" exactly and only, no outline, no shadow, no glow. Strict grid, at least a third of the sheet left as clean white paper. Brand mark: the attached image is the official NBA Logoman. Reproduce it exactly as supplied - tall rounded rectangle, blue left half, red right half, white dribbling-player silhouette, thin white outline - flat and full colour, not redrawn or restyled, small in the top-right corner at about 6% of the poster height, aligned to the grid. No other logos, no team marks, no other text.
```

**高速运动摄影，底部左对齐文字，Wilson 比赛用球，真实载体**

```text
Vertical 2:3 sports photograph with high-speed flash, a brightly lit NBA arena during the Mid-Autumn Festival game, shot from a low angle on the baseline. One player seen only from behind, in a bright red home jersey, rises for a two-handed dunk; at the top of the leap the ball sits exactly inside the round orange rim, lit warm gold, so it reads as a dunk and a full harvest moon at once. The ball is an official Wilson NBA game ball - deep orange-brown pebbled leather, black channels, the black Wilson script wordmark crisply printed on the panel facing the camera, the ball's own league logo turned away out of view. The arena behind is a soft warm blur with no readable faces; the upper third of the frame is clean, bright out-of-focus light. In the lower-right foreground stands the red padded base of the basket stanchion. The attached image is the official NBA Logoman: it is printed on the flat front face of this padding exactly as supplied - correct proportions, blue left, red right, white player silhouette, thin white outline - sharp, upright and undistorted, about 7% of the frame height. In the lower-left corner, left-aligned and modest in size, about half the frame width: the headline in a refined white Song-style typeface, "今晚，谁都不缺席" exactly and only, in Simplified Chinese characters; below it, smaller and widely letter-spaced in a white serif, "HAPPY MID-AUTUMN FESTIVAL" exactly and only; no outline, no shadow, no glow. League red and warm gold on bright arena light, crisp motion detail, natural grain. No identifiable faces, no team marks, no other text. No other logos except the Wilson script on the ball.
```
