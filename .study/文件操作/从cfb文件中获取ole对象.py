import olefile

# 指定需要解析的CFB文件路径
cfb_file_path = r"D:\本地资源\洲洲机电\入职流程与资料\洲洲新进人员流程表20230227 - 副本\xl\embeddings\oleObject1.bin"

# 打开CFB文件，获取OLE对象
ole = olefile.OleFileIO(cfb_file_path)

# 遍历所有的流
for stream in ole.listdir(streams=True, storages=False):
    print('Stream:', stream)

# 遍历所有的对象
for obj in ole.listdir(streams=False, storages=True):
    print('Object:', obj)

# 关闭OLE对象
ole.close()
