"""
输入M和N计算C(M,N)

Version: 0.1
Author:
"""
def fac(num):
    """求阶乘"""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


m = int(input("m ="))
n = int(input("n ="))

fm = fac(m)
fn = fac(n)
fm_n = fac(m-n)

print(fm // fn // fm_n)
