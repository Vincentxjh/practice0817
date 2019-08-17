#第四个练习 - 高级文件操作
import os

#在当前目录下创建文件
with open("message1.txt", "w") as file1:
    pass
with open("message2.txt", "w") as file2:
    pass
#删除文件操作
if os.path.exists("message1.txt"):
    os.remove("message1.txt")
    print("文件删除完毕！")
else:
    print("文件不存在！")

#重命名文件
src = "message2.txt"
dst = "message.txt"
os.rename(src, dst)

#重命名目录
src = r"G:\PycharmProjects\testcontents"
dst = r"G:\PycharmProjects\testfiles"
os.rename(src, dst)

