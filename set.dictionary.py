# 集合的運算
s1={3,4,5}
s2={4,5,6,7}
# print(4 in s1)
# print(10 not in s1)
# s3=s1&s2
# print(s3) #交集，兩個集合中取的相同的資料
# s3=s1|s2
# print(s3) #聯集，兩個集合的所有資料，但是不重複
# s3=s1-s2 #差集從s1刪除與s2有重複的地方
# print(s3)
# s3=s1^s2 #反交集s1與s2有不重複的地方
# print(s3)
s=set("Hello") # set(字串) 把字串拆解為集合
print("H" in s)

# 字典的運算

# dic={"apple":"蘋果","bug":"蟲子"}
# dic["apple"]="小蘋果"
# print(dic["apple"])

# print("apple" in dic)
# print("蟲子" in dic)

# del dic["apple"] #刪除功能
# print(dic)

dic={x:x*2 for x in [1,2,3,4,5]} # 混和 list 功能作業 
print(dic)
