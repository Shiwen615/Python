import pandas as pd

# data=pd.Series([20,10,15])
# print(data)
# print(data.max())
# print(data.median())
# data*=2
# print(data)

# data=data==20
# print(data)


data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[200,500,300]
},index=["a","b","c"])
print(data)
print("===========================")
# print(data["name"])
# print(data.iloc[0])
# print("第二列\n",data.iloc[1])
# print("第c列\n",data.loc["c"])#自訂索引用loc取值 不是iloc
# print("取欄位\n",data["name"])

#如果只取一欄或是一列 資料格式會變成Series
# names=data["name"]
# print(names.str.upper())
# salaries=data["salary"]
# print(salaries.mean())

# data["revenue"]=[100000,200000,30000]
# data["rank"]=pd.Series([3,6,1],index=["b","a","c"])
# data["cp"]=data["revenue"]/data["salary"]
# print(data)