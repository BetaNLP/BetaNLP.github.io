---
title: "先提取后调整：自动术语提取的两阶段方法"
collection: publications
permalink: /publication/2023-10-03-paper-title-number-3
excerpt: ''
date: 2023-10-03
venue: '第十二届自然语言处理与中文计算国际会议(NLPCC 2023)'
paperurl: 'https://softconf.com/nlpcc/Main-2023/user/scmd.cgi?scmd=aLogin&passcode=402X-H2D9C4P2G6'
citation: 'Your Name, You. (2015). &quot;Paper Title Number 3.&quot; <i>Journal 1</i>. 1(3).'
---
&emsp;&emsp;
自动术语提取（Automatic Term Extraction，简称ATE）是一项基本的自然语言处理任务，用于从特定领域的文本中提取相关术语。现有的基于Transformer的技术在这一领域取得了显著的进展。然而，我们观察到，即使是最先进的提取器也存在边界错误问题，即候选术语的起始或结束位置不正确。这些候选术语和真实术语之间的微小差异会导致显著的性能下降。为了解决边界错误问题，我们提出了一种两阶段的提取方法。首先，我们设计了一个基于跨度的提取器来提供高质量的候选术语，然后我们调整候选术语的边界以获得更好的性能。实验结果表明，我们的方法能够有效识别并修正候选术语中的边界错误，性能优于之前的最先进模型。