import os
# 操作系统类型
# print(os.name)

# 在操作系统中定义的环境变量
# print(os.environ)
# print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join(path,textDir))
# 然后创建一个目录:
# os.mkdir(r'F:\python\textDir')
# 删掉一个目录:
# os.rmdir(r'F:\python\textDir')

# print(os.listdir('.'))
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])