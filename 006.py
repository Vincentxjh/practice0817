#第六个练习 - 根据当前时间创建文件
import os, time
def getTime():
    '''
    获取当前时间并转换成不带符号格式
    return:不带符号格式的当前时间
    '''
    gettime = time.strftime('%Y%m%d%H%M%S', time.localtime())
    return gettime

#创建目录
if not os.path.exists('G:/testcontest'):
    os.mkdir('G:/testcontest')
    # 以当前时间作为文件名在当前目录下新建文件
    doc_num = int(input("请输入需要生成的文件数："))
    for i in range(doc_num):
        filename = 'G:/testcontest/' + getTime() + '.txt'
        with open(filename, 'w') as file:
            print('file {}:'.format(i + 1), getTime(), '.txt')
        time.sleep(1)
    print("文件创建成功！")
else:
    print("该目录已存在")
