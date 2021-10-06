#自訂建構子:constructor.py:具有參考的建構子
class Pikachu():
    count=0
    def __init__(self,level):   #def __init__(self):預設
        self.level=level            #pass
        Pikachu.count+=1
if __name__=='__main__':
    p1=Pikachu(100)
    p2=Pikachu(500)
    print(f'p1.level={p1.level}')
    print(f'p2.level={p2.level}')
    print(f'目前共有{Pikachu.count}隻皮卡丘')
    #print(f'目前共有{p1.count}隻皮卡丘')<---p1.count由物件名存取類別變數 不可用
    #print(f'目前共有{p2.count}隻皮卡丘')<---p2.count由物件名存取類別變數 不可用
#類別變數:為所有物件共同擁有,如同太陽是所有人類的太陽
#Pikachu.count:由類別名存取類別變數
#p1.count由物件名存取類別變數
#p2.count由物件名存取類別變數
#p1.count為初期物件導向設計錯誤 雖可用,但嚴格禁止(Java/Python可用)但(C#)已修正,不可用

class Pikachu():
    count=0
    def __init__(self,level=1):
        self.level=level
if __name__=='__main__':
    p3=Pikachu()
    P4=Pikachu(100)

#二元樹(Binary Tree)排序法
#1.左邊小,右邊大
#2.左中右,中間取值  (資料愈亂，速度愈快)
