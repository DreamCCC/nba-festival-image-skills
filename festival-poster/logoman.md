# 官方 Logoman

每张图都必须出现一次 NBA 官方 Logoman，由 img2.5 在生成时直接设计进画面。`scripts/generate.py` 会把官方参考图 `assets/logoman-reference.png` 随每次请求一起发送。你要做的是在 prompt 里告诉模型它是什么、放在哪里、以什么形式出现。

## 三种放法

按画面选一种，六张里至少用到两种。

| 放法 | 适合的风格 | 做法 |
|---|---|---|
| 品牌标记 | 字体海报、印刷品、极简几何 | 平面、原色，放在角落或对齐网格，占画面高度 5% 到 8% |
| 真实载体 | 摄影、静物、票根 | 出现在现实中本来就印着 Logoman 的地方：球架护垫、球衣后领口、票面、场刊封面、记分台 |
| 仪式位置 | 东方留白、版画、节日物件 | 放在节日仪式里本该有标记的位置：水墨画的印章位、红包封口、礼盒封签 |

## 规则

- 每张只出现一个 Logoman，保持官方原色：左蓝、右红、白色剪影、白色描边。不改色、不风格化、不做成单色浮雕。
- 放在平整、正对镜头的表面上。避免强曲面、大角度透视和运动模糊。
- 至少占画面高度 5%，完整不裁切，不被主体、文字或阴影遮挡。
- Logoman 不压住机关和主体，也不抢走主体的位置。
- 不画任何仿制标志，不拿 Logoman 的剪影做创意主体，也不出现 NBA 字标。

## 标准句

每段 prompt 都要写一句下面这样的话。把方括号换成这张图的具体放法：

```text
The attached image is the official NBA Logoman. [It is printed on the flat front face of the stanchion padding / Place it small in the lower-right corner as the brand mark] exactly as supplied - correct proportions, blue left half, red right half, white dribbling-player silhouette, thin white outline - flat full colour, sharp, upright and undistorted, about [7]% of the image height. Do not redraw, restyle or recolour it. No other logos.
```

## 已验证的放法

| 画面 | 放法 | 结果 |
|---|---|---|
| Risograph 中圈满月 | 右下角品牌标记，约 7% | 准确 |
| 散场球馆纪实摄影 | 印在前景球架护垫上，约 8% | 准确，且最自然 |
| HOME 字体海报 | 右上角对齐网格，约 6% | 准确 |
| 复古票根 | 印在票面左端 | 准确 |
| 球衣背面平铺 | 绣在后领口中央 | 准确，尺寸偏小但可辨认 |
| 水墨三分弧线 | 落在右下角印章位 | 准确 |

## 验收

把成图里的 Logoman 和参考图逐项比对：比例、左蓝右红、剪影姿态、白色描边。有任何一项不一致，或者出现了第二个标志，就重做该张。
