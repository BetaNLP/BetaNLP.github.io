---
layout: archive
title: "科研项目"
permalink: /projects/
author_profile: true
---
&emsp;&emsp;课题组成员主持和完成承担国家重点研发计划项目、国家863计划项目、国家自然科学基金等各类科研项目10余项。 所研制开发的技术和平台在解放军某部、国家安全部某局、国家计算机网络与安全管理中心、北京市科技情报所等部门部署运行，突破了关键技术，取得了显著效果，产生了良好效益。

&emsp;&emsp;代表性项目如下：

|          项目名称           |          项目来源           |      起止时间       |
|:-----------------------:|:-----------------------:|-----------------|
| 基于海量知识的语言信息智能理解与推理关键技术  |       国家“863”计划项目       | 2015.01至2017.12 |
|   基于概率化SC文法的多策略机器翻译研究   |       国家自然科学基金项目        |        2013.01至2015.12         | 
|            大数据和社会场景下的互动语言意图深度理解基础理论和关键技术研究             |            国家自然科学基金重点项目             |                2017.01至2020.12                |
|                            基于本体的多策略民汉机器翻译研究                            |                  国家自然科学基金重点项目                   |             2012.01至2016.12                                  |
|                                    面向言语的多策略机器翻译方法                                    |                        国家“973”计划课题                         |                   2013.01至2017.12                                           |

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% for post in site.projects reversed %}
  {% include archive-single.html %}
{% endfor %}