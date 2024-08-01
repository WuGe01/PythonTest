# # break 強制結束迴圈
# n=1
# while n < 5:
#     if n==3:
#         break
#     n+=1
# print(n)

# # continue 強制進入下一圈
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:
#         continue
#     n+=1 #continue 會忽略這個動作
# print(n)

# #else 迴圈跑完最後執行
# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum)

x=input("請輸入一個整數")
x=int(x)
for i in range(x):
    if i*i==x:
        print("整數平方根",i)
        break #break強制結束的時候 不會去跑 else
else:
    print("沒有整數平方根")

