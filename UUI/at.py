#闭包的作用：
#内部函数调用外部函数的成员变量就是闭包，有嵌入，有引用，有返回
def fun_outer():
    out_var = 10
    def fun_inner():
        nonlocal out_var
        out_var = out_var + 1
        print(out_var)

    return fun_inner

fun_inner = fun_outer()
fun_inner()
fun_inner()
fun_inner()