## 课题组学术主页编辑方式

### 学术成果（publications）
需要添加新的论文时，在**markdown_generator**文件夹中，
使用excel打开publications.tsv，
在pub_date中填写论文发表的时间，
在title中填写论文的题目，
在venue中填写论文发表的会议，
在paper_url中填写论文链接，
在abstract中填写论文摘要。

然后，将其另存为txt文件，再用txt打开后重新另存为publications.tsv，注意选择编码方式为utf-8。

在**markdown_generator**文件夹中，运行publications.py即可生成Markdown文件。

### 新闻（news）
需要添加新的新闻时，在**markdown_generator**文件夹中，
使用excel打开news.tsv，
在pub_date中填写新闻发布的时间，
在title中填写新闻的标题，
在content中填写新闻正文。

然后，将其另存为txt文件，再用txt打开后重新另存为news.tsv，注意选择编码方式为utf-8。