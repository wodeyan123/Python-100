list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 称号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello','hello','hello']
# 计算列表长度（元素个数）
print(len(list1)) # 5
# 下标（索引）运算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5]) # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]
# 通过循环用下标便利列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环便利列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理里诶啊哦之后在便利可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

str1 = '*' * 100
print(str1)
list1 = [1, 3, 5, 7, 100]
# 添加元素
list1.append(200) # [1, 3, 5, 7, 100, 200]
list1.insert(1,400) # [1, 400, 3, 5, 7, 100, 200]
# 合并两个列表
# list1.extend([1000,2000])
list1 += [1000, 2000]
print(list1) # # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
print(len(list1)) # 9 
# 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list1.remove(1234)
print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# 从制定的位置删除元素
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1) # [400, 5, 7, 100, 200, 1000]
# 清空列表元素
list1.clear()
print(list1) # []













