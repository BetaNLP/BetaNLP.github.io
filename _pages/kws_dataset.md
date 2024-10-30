---
layout: archive
title: "KWS噪声数据集"
permalink: /datasets/kws_dataset
author_profile: true
---

<div style="text-align: center;">
<img src="/images/1.jpeg" alt="img" width="500">
</div>
&emsp;&emsp;大多数KWS数据集是在安静条件下收集，通常是对这些数据集使用数据增强的方法来提高KWS系统在嘈杂场景中的鲁棒性。然而，这些方法可能会丢失现实世界中噪声音频的特征，从而导致失真。为了弥补这一差距，NoiseComm数据集采集了不同的噪声场景。由于GSC数据集被广泛视为KWS数据集的基准，NoiseComm数据集遵循其构建标准来保持KWS数据集的一致性。表1对GSC和NoiseComm数据集进行了详细对比，除了GSC中的35个关键字外，NoiseComm还额外提供了6个附加关键字以及相应的纯背景噪声，有利于进一步的实验和分析。

&emsp;&emsp;本数据集用于构建[语音关键词检测系统](https://95739cbadc79c80f22.gradio.live)

&emsp;&emsp;数据集下载链接：https://github.com/sheunghung/NoiseKWS/tree/main