# def 定義函式(終於看到重點拉)

def sayHello():
    print("hello") # 函式沒有呼叫不會執行

def say(msg):
    print(msg)

def add(n1,n2):
    a=n1+n2
    print(a)

def add2(n1,n2):
    a=n1+n2
    return a #回傳資料

x = add2(10,3)
print(x)

# 程式包裝