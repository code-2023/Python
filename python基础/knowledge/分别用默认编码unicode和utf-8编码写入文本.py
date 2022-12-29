from io import StringIO
from io import BytesIO

sio=StringIO()
bio=BytesIO()

#字符串用unicode编码，是字符串类型str
s="\u4E2D\u6587\u4F60\u597D"
#unicode编码被转化为utf-8编码，同时生成字节类型bytes的数据
s1=s.encode('utf-8')
# print(s)
sio.write(s)
bio.write(s1)

with open("C:\\Users\\zengpeng\\Desktop\\3.txt","w") as f:
    print("获取unicode编码的字符串：",s)
    f.write(s)
with open("C:\\Users\\zengpeng\\Desktop\\4.txt","wb") as f:
    print("查看utf-8编码的字节串：",s1)
    f.write(s1)

