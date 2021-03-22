# n=0
# while n<5:
#     if n==3:
#         break
#     print(n)
#     n+=1
# print("last n: ",n)

# n=0
# for x in range(4):
#     if x%2==0:
#         continue
#     print(x)
#     n+=1
# print("last n: ",n)

# sum=0
# for n in range(11):
#     sum+=n
# else:
#     print(sum)

n=int(input("input num: "))
for i in range(n):
    if i*i==n:
        print("平方根: ",i)
        break#不會執行else
else:
    print("沒有平方根")