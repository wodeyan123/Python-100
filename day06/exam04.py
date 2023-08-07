from exam02 import if_palindromic
from exam03 import is_prime

if __name__ == '__main__':
    num = int(input("请输入正整数："))
    if if_palindromic(num) and is_prime(num):
        print('%d是回文素数' % num)
