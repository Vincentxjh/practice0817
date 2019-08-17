#第三个练习 - 遍历目录
import os
tuple1 = os.walk(r"G:\PycharmProjects\testcontents")
print(tuple(tuple1))
tuple1 = os.walk(r"G:\PycharmProjects\testcontents")
for i in tuple1:
    print(i, "\n")
