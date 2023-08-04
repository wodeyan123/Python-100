"""
输出100以内所有的素数。
说明：素数指的是只能被1和自身整除的正整数（不包括1）。
"""
import math

flag = True
for i in range(2,100):
    flag = True
    if i == 2 or i == 3 :
        print("%d是素数" % i)
    else:
        k = int(math.sqrt(i))
        for j in range(2, k + 1):
            if i % j == 0:
                flag = False
                break
        if flag == True :
            print("%d是素数" % i)
