# print (abs(-100))
# print (max(1,3,10,50))

# func = abs
# print (func(-500))

# def my_abs(x):
    # if x >= 0:
        # return x
    # else:
        # return -x
		
# print (my_abs(-6))		

# 空函数
# def nop():
    # if age >=18:
     # pass
	
# print (nop)	


# def my_abs(x):
    # if not isinstance(x,(int,float)):
        # raise TypeError('bad operand type')
    # if x >= 0:
        # return x
    # else:
        # return -x

# print (my_abs(2))

#多参数，以及默认参数的函数
# def power(x,n = 2):
    # s = 1
    # while n>0:
      # n = n - 1
      # s = s * x
    # return s

# print (power(5))
# print (power(5,5))

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# def add_end(L=None):
    # if L is None:
         # L = []
    # L.append('END')
    # return L

# print (add_end())


# 可变参数
# def calc(numbers):
    # sum = 0
    # for n in numbers:
        # sum = sum + n * n
    # return sum

# print (calc([1,2,3]))

# def calc(*numbers):
    # sum = 0
    # for n in numbers:
        # sum = sum + n * n
    # return sum

# print (calc(1,2,3))

# 关键字参数
# def person(name,age,**kw):
    # print ('name:',name,'age:',age,'other:',kw)

# person('martian',18)
# person('martian',18,sex = 'man',city = 'wuhan',)
# d = {'sex':'man','city':'wuhan'}
# person ('Martian',18, sex = d['sex'],city = d['city'])
# person('Martian',18,**d)

# 命名关键字参数
# def person(name,age,*,sex,city):
    # print (name,age,sex,city)

# person('Martian',18,sex = 'man',city = 'wuhan')

#递归
# def fact(n):
    # if n == 1:
       # return n
    # return n * fact(n - 1)
# print (fact(5))