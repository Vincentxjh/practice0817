#第二个练习 - 目录的基本操作
import os, shutil
print(os.name)  #获取操作系统类型
print(os.linesep)   #获取当前操作系统换行符
print(os.sep)   #获取当前操作系统路径分隔符
print(os.getcwd())  #获取当前工作目录
with open("message.txt", "r") as file:  #通过相对路径形式打开当前文件夹下的message.txt文件
    print(file.read())
print(os.path.abspath("001.py"))    #获取文件001.py的绝对路径
print(os.path.join("G:/", "message2.txt"))  #拼接路径
print(os.path.exists("venv"))    #判断目录是否存在
print(os.path.exists("G:/message2.txt"))    #判断文件是否存在
os.mkdir("testcontents")    #创建一级目录testcontents
os.makedirs("G:/PycharmProjects/untitled10/testcontents1/test")    #创建多级目录
os.rmdir("testcontents")    #删除目录（只可删除不为空的目录）
shutil.rmtree("testcontents1")  #删除不为空的目录
