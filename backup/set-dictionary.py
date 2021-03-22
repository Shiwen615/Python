# s1={2,3,4}
# print(3 in s1)
# print(3 not in s1)

# s2={3,4,5,6}
# s3=s1&s2
# print(s3)
# print(s1|s2)
# print(s1-s2)#差集
# print(s2-s1)
# print(s1^s2)#反交集

# s=set("hello")#拆解為集合
# print(s)
# print("e" in s)

dic={"apple":"蘋果","bug":"蟲"}
print(dic)
print(dic["apple"])
print("apple" in dic)
print("蘋果" in dic)#只能查key不能查value

del dic["apple"]
print(dic)

dic={x : x*2 for x in [2,3,4]}
print(dic)