from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url="https://www.apple.com/itunes/charts/songs/"

#1.download page
#1.1open connection
conn=urlopen(url)

#1.2 read data
raw_data=conn.read()

#1.3decode data
content=raw_data.decode("utf8")

#file du lieu
f=open("i_tune.html","wb")
f.write(raw_data)
f.close

#2.find roi
soup=BeautifulSoup(content,"html.parser")

ul_news=soup.find("section", "section chart-grid")
# print(ul_news)
ul_news_son=ul_news.find("div", "section-content")
# print(ul_news_son)

# 3.copy and save
li_list=ul_news_son.find_all("li")

song_list = []
for li in li_list:
    names=li.h3.string
    artists=li.h4.string
    songs=OrderedDict({
        "names" :  names ,
        "artists" : artists ,
    })
    song_list.append(songs)
    # print(song_list)
pyexcel.save_as(records =song_list,dest_file_name="itune_song.xlsx")



options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download([names +  artists])