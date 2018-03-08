# map
# def odd(x):
    # return x*x
# r = list(range(0,5))
# L = list(map(odd,r))
# print (L)

# reduce
# from functools import reduce
# def add(x,y):
    # return x+y
# r = list(range(0,10))
# print (reduce(add,r))

# filter
# def is_odd(x):
     # return x%2==0
# r = list(range(0,10))
# print (list(filter(is_odd,r)))


# sorted
# r = [36,-5,46,-81,57,2]
# s = ['bob', 'about', 'Zoo', 'Credit']
# print (sorted(r))
# print (sorted(r,key=abs))
# print (sorted(str))
# print (sorted(s,key=str.lower))
# print (sorted(s,key=str.lower,reverse=True))

# def count():
    # fs = []
    # for i in range(1, 4):
        # def f():
             # return i*i
        # fs.append(f)
    # return fs

# f1, f2, f3 = count()
# print (f1())

#匿名函数 lambda
# print (list(map(lambda x:x*x,list(range(1,10)))))

#装饰器 Decorator
# def now():
    # print ('2018-1-17')
# f = now
# f()
# print (f.__name__)
# print (now.__name__)


# import functools
# def log(func):
    # @functools.wraps(func)
    # def wrapper(*args,**kw):
        # print ('call %s():'%func.__name__)
        # return func(*args,**kw)
    # return wrapper
# def log(text):
    # def decorator(func):
        # @functools.wraps(func)
        # def wrapper(*args,**kw):
            # print ('%s %s():'%(text,func.__name__))
            # return func(*args,**kw)
        # return wrapper
    # return decorator
# @log('excute')
# def now():
    # print ('

#偏函数
# print (int('123456'))
# print (int('123456',base=8))
# print (int('123456',base=16))
# def int2(x,base=2):
     # return int(x,base)
# print (int2('1000'))

# import functools
# int2 = functools.partial(int,base=2)
# print (int2('100100'))

