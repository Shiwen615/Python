# def power(base,exp=0):
#     print(base**exp)

# power(2,3)
# power(4)

# def divide(n1,n2):
#     print(n1/n2)

# divide(4,2)
# divide(n2=4,n1=2)

def avg(*ns):
    sum=0
    for x in ns:
        sum+=x
    print(sum/len(ns))

avg(1,2,3)
avg(5,7)