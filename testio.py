f = open(r'F:\python\file.txt','r',encoding='utf-8')
# print (f.read())
# while True:
#     l = f.readline()
#     if l == '':
#         break
#     print(l.strip())

with open(r'F:\python\file.txt','r',encoding='utf-8') as f:
    print(f.read())