"""
Property属性实现方式：作用是把函数名当变量直接使用

方式1：装饰器
方式2：类属性
"""

# #装饰器方式
# class Student():
#     def __init__(self):
#         self.__age = 20

#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         self.__age = age

# if __name__ == '__main__':
#     s = Student()
#     print(s.age)


"""
类属性方式
类属性名 = property(获取值的函数名, 设置值的函数名)
"""
class Student():
    def __init__(self):
        self.__age = 20

    
    def get_age(self):
        return self.__age
    
    
    def set_age(self, age):
        self.__age = age
    age = property(get_age, set_age)
if __name__ == '__main__':
    s = Student()
    s.age = 30
    print(s.age)