
import pandas as pd
from datetime import datetime
news = pd.read_csv("news.tsv", sep="\t", header=0)
news


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    return "".join(html_escape_table.get(c ,c) for c in text)

import os
for row, item in news.iterrows():



    date_str = datetime.strptime(str(item.pub_date), "%Y/%m/%d").strftime("%Y-%m-%d")

    md_filename = date_str + "-" + item.url_slug + ".md"
    html_filename = date_str + "-" + item.url_slug
    year = item.pub_date[:4]

    ## YAML variables

    md = "---\ntitle: \""   + item.title + '"\n'

    md += "\ndate: " + date_str


    md += """\npermalink: /news/""" + html_filename


    md += "\ntags:\n - cool posts\n - category1\n - category2"

    md += "\n---"

    md += "\n" + item.content

    md_filename = os.path.basename(md_filename)

    with open("../_news/" + md_filename, 'w', encoding='utf-8') as f:
        f.write(md)


