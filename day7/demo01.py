s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以拆行
s3 = """
hello,
world!
"""
# print(s1, s2, s3, end='')

s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')

s1 = '\141\142\143\x61\x63\x63'
s2 = '\u5ED6\u7115'
# print(s1, s2, end='')

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

s1 = 'hello ' * 3
print(s1)   # hello hello hello

s2 = 'world'
s1 += s2
print(s1)   # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
str2 = 'abc123456'
# 从字符串中取出指定位置的字符（下标运算）
print(str2[2]) # c
# 字符串切片（从制定的开始索引到指定的结束索引）
print(str2[2:5])    # c12
print(str2[2:])    # c123456
print(str2[2::2])    # c246
print(str2[::2])    # ac246
print(str2[::-1])    # 654321cba
print(str2[-3:-1])    # 45

print("**************************************************************************")
str1 = "hello, world!"
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
#检查字符串是否以制定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否已制定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串已指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*')) # ******************hello, world!*******************
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))  #                                      hello, world!
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit()) # False
# 检查字符串是否以字母构成
print(str2.isalpha()) # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum()) # True
str3 = '  jacfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

print("**************************************************************************")
a, b = 5, 10
print("%d * %d = %d" % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')






