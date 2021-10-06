'''
import random
datas=[]
for i in range(7):#已確定要跑幾圈
    flag=True
    while True:  #不確定要跑幾圈
        n=random.randint(1,49)
        for i in datas:
            if i == n:
                flag=False
                break
        if flag:
            datas.append(n)
print(datas)
'''

#Dict版大樂透-正確版本
import random
datas={}#空字典
while len(datas)<7:
    n=random.randint(1,49)
    datas[n]=n
for key in datas.keys():
    print(key)




