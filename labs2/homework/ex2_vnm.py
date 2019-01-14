from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf8")

f = open("cafef.html", "wb")
f.write(raw_data)
f.close()

soup = BeautifulSoup(page_content,"html.parser")
table = soup.find("table", id = "tableContent")


tr_list_1 = table.find_all("tr", "r_item")
tr_list_2 = table.find_all("tr", "r_item_a")
a = len(tr_list_1)
if a < len(tr_list_2):
    a = len(tr_list_2)
tr_list = []
for i in range(0, a):
    tr_list.append(tr_list_1[i])
    tr_list.append(tr_list_2[i])
# print(tr_list)
cell_list = []
for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    
    cells = OrderedDict({
        "name": td_list[0].string,
        "Quy 4-2017": td_list[1].string,
        "Quy 1-2018": td_list[2].string,
        "Quy 2-2018": td_list[3].string,
        "Quy 3-2018": td_list[4].string,
    })
    cell_list.append(cells)
pyexcel.save_as(records = cell_list, dest_file_name = "baocaoVNM.xlsx")
