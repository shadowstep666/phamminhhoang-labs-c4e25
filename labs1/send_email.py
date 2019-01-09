from gmail  import *

# m=str
# '''
# <p>hello&nbsp;</p>
# <p><span style="text-decoration: underline;"><strong>it is nice day .</strong></span></p>
# <p>&nbsp;</p>
# '''



from random import *
to = "qhuydtvt@gmail.com"
sick_ness = ["thuong han", "om","cam"]

html_template='''
<p>hello&nbsp;</p>
<p><span style="text-decoration: underline;"><strong>it is nice day .</strong></span></p>
<p>&nbsp;</p>
<p>em thay khong khoe</p>
<p>I am sickness</p>
'''
x=choice(sick_ness)
html_content = html.replace("sickness",x)
print(html_content)


gmail=GMail('jace17071998@gmail.com','0914085273')
msg=Message('Test Message',to='jace17071998@gmail.com',html=html_content)
gmail.send(msg)

