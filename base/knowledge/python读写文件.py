"""
r：只读模式打开文件，读文件内容的指针会放在文件的开头
w：以只写模式打开文件，若该文件存在，打开时会清空文件中原有的内容；反之，则创建新文件
a：以追加模式打开一个文件，对文件只有写入权限，如果文件已经存在，文件指针将放在文件的末尾；反之，则会创建新文件
read()函数用于读取文件中指定数量的字符，函数参数接受指定数量
readline()函数用于读取文件中的一行(转义字符\n表示一行的末尾)，返回值类型是字符串
readlines()函数用于读取文件中的所有行，该函数的返回值是字符串列表(可迭代)，其中每个元素为文件中的一行内容
write()函数用于向文件中写入指定内容
writelines()函数可以实现将包含多行字符串的列表写入文件
"""

# 使用readlines()和writelines()方法，读多行写多行
with open('../output.txt', 'w', encoding='utf-8') as file:
    with open('../my_file.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()  # readlines()的返回值类型是列表
        print(lines)  # 查看readlines()读取的行
        file.writelines(lines)  # writelines()可以接收列表，而write()只能接收字符串

# 使用readline()和write()方法，读一行写一行
with open('../write()写入.txt', 'w', encoding='utf-8') as file:
    with open('../my_file.txt', 'r', encoding='utf-8') as f:
        for i in range(5):
            line = f.readline()  # 返回值类型是字符串
            print('当前读取的行是：%s' % line)
            file.write(line)
            if i == 4:
                print("readline()返回值类型：%s" % (type(line)))
