"""
案例：装饰器入门，本质是闭包函数，在不改变原有函数的基础上，对其功能做增强
前提条件：
1. 闭包函数
2.有引用
3.有返回
4.有额外方法

语法糖：在被装饰的原函数上，直接写@装饰器名，之后直接调用原函数即可
"""



# def fn_outer(comment):
#     def fn_inner():
#         print("登录校验中——————")
#         comment()
#     return fn_inner
# @fn_outer
# def comment():
#     print("发表评论中————")

# # # 装饰器语法的传统方式
# # comment = fn_outer(comment)
# # comment()


# print("-------------------------")


# #语法糖方式
# comment()



"""
1.一个装饰器的参数只有一个、
2.如果装饰器有多个参数，可以在该装饰器的外面再包裹一层，把该装饰器当作其内部函数返回即可
"""

def flag(flag):
    def fn_outer(fn):
        def fn_inner(a,b):
            if flag == 1:
                print("开始加法执行")
            if flag == 2:
                print("开始减法执行")
            return fn(a,b)
        
        return fn_inner
    return fn_outer



@flag(1)
def sum(a,b):
    return a+b
def decade(a,b):
    return a-b

a = sum(1,2)
print(a)