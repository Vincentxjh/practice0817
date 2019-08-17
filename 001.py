#第一个练习 - 文件创建、读写、关闭练习
file = open('G:/message.txt', 'w')
file.close()
with open('G:/message1.txt', 'w') as file1:
    pass

file = open('G:/message.txt', 'w')
file.write("你好啊！\n")
file.close()

with open('G:/message.txt', 'a') as file:
    file.write("你好啊！\n")

with open('G:/message.txt', 'r') as file:
    string = file.read()
    print(string)

with open('G:/message.txt', 'r') as file:
    file.seek(4)
    string = file.read(8)
    print(string)

with open('G:/message.txt', 'r') as file:
    while True:
        string = file.readline()
        print(string)
        if string == "":
            break

with open('G:/message.txt', 'r') as file:
    string = file.readlines()
    for i in string:
        print(i)