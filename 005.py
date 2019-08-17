#第五个练习 - 获取文件基本信息
import os
#获取文件基本信息
fileinfo = os.stat(r"G:\PycharmProjects\testcontents\message.txt")
print("文件完整路径：", os.path.abspath(r"G:\PycharmProjects\testcontents\message.txt"))
#输出文件的基本信息
print("索引号：", fileinfo.st_ino)
print("设备号：", fileinfo.st_dev)
print("文件大小：", fileinfo.st_size, "字节")
print("最后一次访问时间：", fileinfo.st_atime)
print("最后一次修改时间：", fileinfo.st_mtime)
print("最后一次状态变化时间：", fileinfo.st_ctime)

#将文件基本信息里面的文件大小和访问时间格式化
#格式化时间
def formatTime(longtime):
    '''
    功能：格式化日期时间的函数
    longtime: 要格式化的时
    return:标准时间格式
    '''
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(longtime))

#格式化文件大小
def formatByte(byte):
    kb = 1024
    mb = 1024*1024
    gb = 1024*1024*1024
    tb = 1024*1024*1024*1024
    if byte < kb:
        return '%d B'%byte
    elif kb <= byte < mb:
        return '%.2f KB'%(byte / kb)
    elif mb <= byte < gb:
        return '%.2f MB'%(byte / mb)
    elif gb <= byte < tb:
        return '%.2f GB'%(byte / (gb))
    elif tb <= byte:
        return '%.2f GB'%(byte / (tb))

#获取文件基本信息
fileinfo = os.stat(r"G:\PycharmProjects\testcontents\message.txt")
print("文件完整路径：", os.path.abspath(r"G:\PycharmProjects\testcontents\message.txt"))
#输出文件的基本信息
print("索引号：", fileinfo.st_ino)
print("设备号：", fileinfo.st_dev)
print("文件大小：", formatByte(fileinfo.st_size))
print("最后一次访问时间：", formatTime(fileinfo.st_atime))
print("最后一次修改时间：", formatTime(fileinfo.st_mtime))
print("最后一次状态变化时间：", formatTime(fileinfo.st_ctime))