# 实现最大公约数 和 最小公倍数的函数

# 最大公约数
def com_divissor(a, b):
    if a > b :
        a, b = b, a
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
            
            
# 最小公倍数
def com_multiple(a, b):
    return (a * b // com_divissor(a, b))
    

m = int(input("m ="))
n = int(input("n ="))
print("%d和%d的最大公约数为：%d" % (m, n, com_divissor(m, n)))
print("%d和%d的最小公倍数为：%d" % (m, n, com_multiple(m, n)))
