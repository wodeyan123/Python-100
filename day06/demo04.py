# 在参数名前面的 * 表示 args 是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
    

# 在调用 add 函数时可以传入 0 个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
