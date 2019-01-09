from random import *
from gmail  import *
import datetime
to = "qhuydtvt@gmail.com"
sick_ness = ["cảm lạnh", "cảm cúm","đau bụng","tiêu chảy"]

html='''
<p>Ch&agrave;o anh</p>
<p>H&ocirc;m qua l&agrave; một ng&agrave;y đẹp trời .Nhưng do đi chơi nhiều n&ecirc;n em <span style="text-decoration: underline; color: #0000ff;"><em><strong>cảm thấy kh&ocirc;ng được khỏe</strong></em></span> . B&aacute;c sĩ bảo em <span style="text-decoration: underline; color: #ff0000;"><em><strong>bị ốm</strong></em></span> . Em xin ph&eacute;p được nghỉ ạ .</p>
<p>ps: ho&agrave;ng</p>
'''
x=choice(sick_ness)
html_content=html.replace("bị ốm",x)
print(html_content)

gmail=GMail('phoangbk1998@gmail.com','hoangpro9x')
msg=Message('Test Message',to='phoangbk1998@gmail.com',html=html_content)
gmail.send(msg)

now = datetime.datetime.now()
if now.hour > 7:
    gmail.send(msg)
else:
    print("After 7 AM")