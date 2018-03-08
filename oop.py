#面向对象的编程
# class Student(object):
      # def __init__(self,name,age,score):
           # self.name = name
           # self.age = age
           # self.score = score
      # def print_info(self):
           # print('%s,%s,%s'%(self.name,self.age,self.score))

# sA = Student('Jordon',50,100)
# sB = Student('Kobe',38,99)
# sC = Student('James',32,98)
# sA.print_info()
# sB.print_info()
# sC.print_info()

#继承
# class Animal(object):
    # def run(self):
        # print('Animal is running...')

# class Dog(Animal):
    # pass

# class Cat(Animal):
    # pass

# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()

# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：



#__slots__
# class Student(object):
# 用tuple定义允许绑定的属性名称
      # __slots__ = ('name', 'age') 
      # s = Student() 
      # s.name = 'Michael' 
      # s.age = 25 
      # s.score = 99 


# 多重继承


# class Student(object):
    # def __init__(self, name):
        # self.name = name
    # def __str__(self):
        # return 'Student object (name=%s)' % self.name
    # __repr__ = __str__

# s = Student('Martian')
# print (s)


#__iter__
# class Fib(object):
    # def __init__(self):
    # 初始化两个计数器a，b
        # self.a, self.b = 0, 1 

    # def __iter__(self):
    # 实例本身就是迭代对象，故返回自己
        # return self 

    # def __next__(self):
    # 计算下一个值
        # self.a, self.b = self.b, self.a + self.b 
    # 退出循环的条件
        # if self.a > 100000: 
            # raise StopIteration()
    # 返回下一个值
        # return self.a 

# for n in Fib():
     # print(n)

#__getitem__
#__call__



#枚举类
# from enum import Enum,unique

# @unique
# class Weekday(Enum):
      # Sun = 0
      # Mon = 1
      # Tue = 2
      # Wed = 3
      # Thu = 4
      # Fri = 5
      # Sat = 6
# print (Weekday.Sun)
