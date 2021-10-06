#物件導向--類別classtest.py
import random
class Pokemo():   #()內，沒寫就是預設繼承object類別
    def  __init__(self):
        print('神奇寶貝出生了')
if __name__=='__main__':
    p1=Pokemo()  #實例化物件

class Pokemo():   #()內，沒寫就是預設繼承object類別
    def  __init__(self):
        print('神奇寶貝出生了')
        self.level=10
        self.left=f'左腳:{random.randint(1,10)}公分'
if __name__=='__main__':
    p1=Pokemo()
    print(p1.left)#  (p1.left) 的.=的
    p2=Pokemo()
    print(p2.left)

'''1.class Pokemon():
      預設繼承object類別
   2.def __init__(self):    #Construction營造
        預設建構子(Construction)
        產生物件時(實例化物件instance)
        會自動執行的方法(Method,也就是函數)
   3.self:標識此方法或變數為物件方法(變數)     
    '''

class Pokemo():   #()內，沒寫就是預設繼承object類別
    count=0
    def  __init__(self):
        print('神奇寶貝出生了')
        self.level=10
        self.left=f'左腳:{random.randint(1,10)}公分'
        Pokemo.count+=1
if __name__=='__main__':
    p1=Pokemo()
    print(p1.left)#  (p1.left) 的.=的
    p2=Pokemo()
    print(p2.left)
    print(p1)  #16個字美自4bit=64bit
#P類別名稱大寫  使用類別變數,前面需加類別名:Pokemon.count+=1
    #p1.right=f'右腳:{random.randint(1,10)公分}'
    #print(p1.right)
    #print(p2.right)


