import pandas as pd

# data=pd.Series([30,14,20])
# condition=[True,False,True]
# # print(data[condition])
# condition=data>20
# # print(data[condition])
# data=pd.Series(["您好","Python","Pandas"])
# condition=[False,False,True]
# print(data[condition])
# condition=data.str.contains("P")
# print(data[condition])

data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[200,500,300]
})
print(data)
print("===============")
condition=[False,True,True]
print(data[condition])
condition=data["salary"]>300
print(data[condition])
condition=data["name"]=="Amy"
print(data[condition])