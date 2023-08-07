"""
实现判断一个数是不是回文数的函数。
"""
def if_palindromic(num):
    # print("num = %d" % num)
    temp = num
    y = 0
    while temp > 0:
        y = y * 10 + temp % 10
        temp = temp // 10
    # print("y = %d" % y)
    # print(num == y)
    return num == y
        
        
# num = int(input("num ="))
# # print(if_palindromic(num))
# if if_palindromic(num):
    # print("%d是一个回文数" % num)
# else:
    # print("%d不是一个回文数" % num)
