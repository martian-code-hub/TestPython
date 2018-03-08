# 切片
# L = ['Jordon','Kobe','James','AI','Tmc','Wade','Tomas','Carter','Lrving','Curry','Durant','Thompson']
# t = (0,1,2,3,4,5,6,7,8,9)
# s = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ'
# print (L[0:3])
# print (L[4:6])
# print (L[:5])
# print (L[5:])
# print (L[:])
# print (L[-1])
# print (L[-5:-1])
# print (L[::2])
# print (t[:3])
# print (s[:3])


# 迭代
# d = {'a':1,'b':2,'c':3,'d':4,'e':5}
# for key in d:
    # print(key)
# for value in d.values():
    # print (value)
# for k,v in d.items():
    # print (k,v)
# for ch in s:
    # print (ch)

#判断是否是可迭代对象
# from collections import Iterable
# print (isinstance(s,Iterable))

# enumerate
# for i,value in enumerate(L):
    # print (i,value)

#列表生成式
# print ([x*x for x in range(1,11)])
# print ([x*x for x in range(1,11) if x%2 == 0])
# print ([m+n for m in 'ABCD' for n in "XYZ"])


#生成器
# L = [x*x for x in range(10)]
# print (L)
# g = (x*x for x in range(10))
# print (next(g),next(g),next(g),next(g),next(g))
# for x in g:
    # print (x)