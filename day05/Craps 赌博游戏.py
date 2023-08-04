"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
Version: 0.1
Author: 
"""
import random

money = 1000
count = 0
first_time = 0
flag = False
success = 0
fail = 0
while money > 0:
    count += 1
    flag = True
    while flag:
        x = random.randint(1,6)
        y = random.randint(1,6)
        time = x + y
        if count == 1:
            first_time = time
            if first_time == 7 or first_time == 11:
                money += 100
                success += 1
                flag = False
            elif first_time == 2 or first_time == 3 or first_time == 12:
                money -= 100
                fail += 1
                flag = False
        else:
            if time == 7:
                money -= 100
                fail += 1
                flag = False
            elif time == first_time:
                money += 100
                success += 1
                flag = False    
print("总共玩了%d次，赢了%d次，输了%d次" % (count, success, fail))         
        
