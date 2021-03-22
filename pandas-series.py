import pandas as pd
# data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"])
# print(data)
# print("data type",data.dtype)
# print("data size",data.size)
# print("data index",data.index)

# print(data[2])
# print(data["b"])

# print(data.max())
# print(data.sum())
# print(data.std())
# print(data.median())
# print(data.nlargest(3))#最大的3個數

data=pd.Series(["您好","Python","Pandas"])
# print(data.str.lower())
# print(data.str.len())
# print(data.str.cat(sep="幹"))
# print(data.str.contains("P"))
print(data.str.replace("您好","yoyo"))
