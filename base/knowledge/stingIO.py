from io import StringIO
from io import BytesIO
def outputstring():
    return 'string \nfrom \noutputstring \nfunction'

#调用函数并用变量s接收字符串返回值,注意字符串共有36个字符
s = outputstring()
print("字符串s长度：",len(s))

# 在内存中读取函数返回的字符串,同时初始化IO对象
#sio = StringIO(s)

# 调用StringIO本身的方法
# print(sio.getvalue())

#sio是一个类文件对象
#s = sio.readlines()
#for i in s:
#    print(i.strip())

sio=StringIO()
print(type(sio))
sio.write(s)
print("向IO对象写入字符串后的文件指针变为",sio.tell())
print("getvalue()返回值类型是",type(sio.getvalue()))
#print(sio.getvalue())
##sio=list(sio)
##print(type(sio))

#此时，文件指针尚未调整，读不到数据
lines = sio.readlines()
print(lines)
#调整文件指针到文件开头
sio.seek(0,0)
print(sio.tell())
#读取若干字符
print(sio.read(6))
#读取剩余所有行
print(sio.readlines())

#读取字节型的数据
bio = BytesIO()
bytes_data=s.encode('utf-8')
print("打印经utf-8编码后的字节串形式：",bytes_data)
bio.write(bytes_data)
print("getvalue()返回值类型是",type(bio.getvalue()))
bio.seek(-36,1)
print(bio.tell())
print(bio.readlines())
