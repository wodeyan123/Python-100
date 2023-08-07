# 定义元祖
t = ('廖焕', 24, True, '湖北黄冈')
print(t)
# 获取元祖中的元素
print(t[0])
print(t[3])
# 便利元祖中的值
for member in t:
    print(member)
# 重新给元祖复制
# t[0] = '王大锤' # TypeError
# 变量 t 重新引用了新的元祖原来的元祖将被垃圾回收
t = ('王大锤', 20, True, "云南昆明")
print(t)
# 将元祖转换成列表
person = list(t)
print(person)
# 列表是可以修改它的元素的
person[0] = '李小龙'
person[1] = '25'
print(person)
# 将列表转换成元祖
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)









