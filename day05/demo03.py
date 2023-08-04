"""
《百钱百鸡》问题
百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？翻译成现代文是：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
Version: 0.1
Author: 
"""
for i in range(0, 20):
    for j in range(0, 33):
        k = 100 - i - j
        if 5 * i + 3 * j + k / 3 == 100:
            print("公鸡%d只，母鸡%d只，小鸡%d只" % (i, j, k))
