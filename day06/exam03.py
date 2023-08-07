"""
判断一个数是不是素数
"""
def is_prime(num):
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return false
    return True if num != 1 else False
