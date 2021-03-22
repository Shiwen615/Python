# if False:
#     print("True")
# else:
#     print("False")

# x=input("請輸入: ")
# x=int(x)

# if x>200:
#     print("bigger than 200")
# elif x>100:
#     print("bigger than 100")
# else:
#     print("smaller than 100")

n1=int(input("input num1: "))
op=input("input + - * /: ")
n2=int(input("input num2: "))

if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援")
    