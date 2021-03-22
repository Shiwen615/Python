import random

# data=random.choice([1,2,5,6,7,8,9])
# print(data)
# data=random.sample([1,2,5,6,7,8,9],3)
# print(data)

# data=[1,2,5,6,7,8,9]
# random.shuffle(data)
# print(data)

# data=random.random()
# print(data)

# data=random.uniform(60,100)
# print(data)

# data=random.normalvariate(100,10)#平均數:100, 標準差:10
# print(data)

import statistics as stat
data=stat.median([1,2,4,5,6,7,100])
print(data)

data=stat.stdev([1,2,4,5,6,7,100])
print(data)

data=stat.mean([1,2,4,5,6,7,100])
print(data)