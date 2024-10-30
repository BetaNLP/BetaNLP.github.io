

import pandas as pd
from datetime import datetime
publications = pd.read_csv("publications.tsv", sep="\t", header=0)
publications


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    return "".join(html_escape_table.get(c,c) for c in text)

import os
for row, item in publications.iterrows():



    date_str = datetime.strptime(str(item.pub_date), "%Y/%m/%d").strftime("%Y-%m-%d")

    md_filename = date_str + "-" + item.url_slug + ".md"
    html_filename = date_str + "-" + item.url_slug
    year = item.pub_date[:4]
    
    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename

    md += "\nexcerpt: ''"
    
    md += "\ndate: " + date_str
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    if len(str(item.paper_url)) > 5:
        md += "\npaperurl: '" + item.paper_url + "'"
    
    md += "\ncitation: '" + html_escape(item.citation) + "'"
    
    md += "\n---"

    
    md+= "\n&emsp;&emsp;"
        
    md += "\n" + item.abstract
    
    md_filename = os.path.basename(md_filename)
       
    with open("../_publications/" + md_filename, 'w', encoding='utf-8') as f:
        f.write(md)


