import random
class Pokemon(): #()內，沒寫就是預設繼承object類別
    def __init__(self):
        print('神奇寶貝出生了')
if __name__ == '__main__':
    p1 = Pokemon() #實例化物件


class Pokemon(): #()內，沒寫就是預設繼承object類別
    count = 0
    def __init__(self):
        print('神奇寶貝出生了')
        self.level = 10
        self.left = f'左腳：{random.randint(1,10)}公分'
        self.right = f'右腳：{random.randint(1,10)}公分'
        Pokemon.count += 1
if __name__ == '__main__':
    p1 = Pokemon()
    print(p1.left)
    p2 = Pokemon()
    print(p2.left)
if __name__ == '__main__':
    p1.right = Pokemon()
    print(p1.right)
    p2 = Pokemon()
    print(p2.right)

class Pikachu():
    count = 0
    def __init__(self,level):
        self.level = level
        Pikachu.count += 1
def __init__(self): #預設
    pass
if __name__ == '__main__':
    p1 = Pikachu(100)
    p2 = Pikachu(500)
    print(f'p1.level = {p1.level}')
    print(f'p2.level = {p2.level}')
    print(f'目前共有{Pikachu.count}隻皮卡丘')
    print(f'目前共有{p1.count}隻皮卡丘')
    print(f'目前共有{p2.count}隻皮卡丘')

class Pikachu():
    count = 0
    def __init__(self):
        self.level = 1
    def __init__(self,level=1):
        self.level = level

if __name__ == '__main__':
    p3 = Pikachu() #沒參數就預設為1
    p4 = Pikachu(100)
#http://web.ntnu.edu.tw/~algo/