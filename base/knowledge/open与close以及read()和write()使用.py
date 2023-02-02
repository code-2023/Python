f=open("../../study&test/1.txt", 'w', encoding="utf-8")
f.write("第一行\n")
l=["第二行\n","第三行\n","第四行\n","第五行\n",
   "第六行\n","第七行\n","第八行\n","第九行\n"]
f.writelines(l)  #写入多行
f.close()

f=open("../../study&test/1.txt", 'r', encoding="utf-8")
print(f.readline(),end='')
print("准备读第一个字符:",end='')
print(f.read(5),end='')  #读取5个字符
print("到此已经读完五个字符")
print(f.readline(),end='')
print(f.readlines(),end='')
f.close()
