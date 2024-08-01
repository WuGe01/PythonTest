def say(msg="Hello"):
    print(msg)

# say()
# say("呼拉拉")

# 名稱可以自己定義
def divide(n1,n2):
    print(n1/n2)

# divide(4,2)
# divide(n2=4,n1=2) #這應該是特別的功能

# 無限(不定)長度參數 
def add(*s):
    n=0
    for a in s:
        n+=a
    print(n)

add(11,100,11,12,19)