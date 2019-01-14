from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#  urllib
url="https://dantri.com.vn/"
# 1.download the page

# 1.1 open connection
conn = urlopen(url)

# 1.2 read data
raw_data = conn.read()

# 1.3 decode data
content = raw_data.decode("utf8")

# print(content)
# chi doc
# f =open("dantri.html")

# doc va sua du lieu
f =open("dantri.html","wb")
f.write(raw_data)

f.close()

# 2.find roi
soup= BeautifulSoup(content,"html.parser")
# print(soup.prettify())

ul_news =soup.find("ul","ul1 ulnew")
# print(ul_news.prettify())

# 3.copy and save
li_list = ul_news.find_all("li")

# li=li_list[0]  # in mot lan

news_list = []
for li in li_list:

    # walking
    h4=li.h4
    a = h4.a
    link = url+a["href"]
    # print(link)
    title = a.string
    # print("----------------------------")
    # print(title,link)
    news =OrderedDict({
        "title " : title ,
        "link" : link ,
    }),
    # print(news)
    # print("--------------------------")
    news_list.append(news)
pyexcel.save_as(records=news,dest_file_name="check_dantri.xls")
print(news_list)



