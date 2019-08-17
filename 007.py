#第七个练习 - 批量添加文件夹
import os
def creatcontents(con,num):
    '''
    创建文件
    con:指定的目录
    num:创建个数
    '''
    name = con + '/' + num
    os.makedirs(name)
    print("文件夹", num, "创建成功！")

num = input("请输入需要生成的文件夹个数：")
the_path = 'G:/practice10'
for i in range(int(num)):
    creatcontents(the_path,str(i+1))