---
name: festival-poster
description: 为已确定的中美节日制作 NBA 主视觉。先检索当下成型的设计方法，再让 NBA 资产与节日符号变成同一个物体，最后调用 gpt-image-2.5-sunburst。
---

# 节日主视觉

输入只有任务里的一个节日：名称、公历日期、所属国家、节日含义。不要自行改期，也不要另找节日。

## 设计标准

目标是一张内部同事愿意拿去继续制作的主视觉，不是元素拼贴。

- 第一眼必须能认出 NBA，而不是一张普通篮球海报。优先使用这些联盟资产：奥布莱恩冠军奖杯、Logoman 的运球轮廓、30 支球队的主场、24 秒进攻时钟、官方红蓝与深蓝场地。每次只用一个资产。
- 节日符号必须和这个资产是同一个物体。奖杯的金球本身成为满月，是融合；奖杯旁边再放一个月亮，是堆砌。
- 一个画面只留一个机关，三张图使用三个不同机关。
- 参考对象应是近年获奖海报、品牌战役和仍在使用的设计系统。先看它解决了什么问题，再决定能否迁移，不搬它的纹样。
- 画面要像实拍装置、印刷品或可制作的实物。保留材料、磨损、印刷错位和留白。
- 不要巨月、灯笼、祥云、宫殿、玉兔和节日符号的直接叠加。
- 不要生成可读正文。数字只有在它本身就是创意机关时才允许出现，例如 08:15 与 24 秒。
- 竖版 3:4，尺寸 `1024x1536`。

## 检索

至少打开 4 个真实页面，覆盖两类：

1. 这个节日近两年被品牌认真做过的视觉，避开模板站和生图提示词合集。
2. 当下仍有效的平面与体育战役方法：真实摄影、印刷质感、强字体系统、本地文化转译。

每条来源记录标题、最终 URL，以及你实际采用的一个方法。检索结果决定三张图的差异，不要先想好画面再找文章配。

## 生图

只使用下面这个接口，模型固定为 `gpt-image-2.5-sunburst`。

```python
import json
import os
from urllib.request import Request, urlopen

request = Request(
    "https://aihubmix.com/ai/v1/images/generations",
    data=json.dumps({
        "model": "gpt-image-2.5-sunburst",
        "prompt": prompt,
        "async": False,
        "n": 1,
        "output_format": "png",
        "size": "1024x1536",
    }).encode(),
    headers={
        "Authorization": "Bearer " + os.environ["AIHUBMIX_API_KEY"],
        "Content-Type": "application/json",
    },
    method="POST",
)
with urlopen(request, timeout=600) as response:
    payload = json.loads(response.read().decode())
```

密钥只从环境变量 `AIHUBMIX_API_KEY` 读取。任务若以 `AIHUBMIX_API_KEY=` 单独给出，先写入当前进程环境变量，再调用接口。不要回显密钥，不要把它写入仓库、提示词或信封。

每次调用 `n` 固定为 1。三张图分三次调用。返回体里的 `content_url` 原样进入信封；只有没有地址时才保留 `b64_json`。

生成后检查：品牌资产是否一眼可辨、节日含义是否由同一个物体承担、是否出现假 Logo、乱码或明显塑料感。有问题就改 prompt 重做该张，总数仍保持 3 张。
