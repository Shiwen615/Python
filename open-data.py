# import urllib.request as req
# src="https://www.ntu.edu.tw/"
# with req.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)

import urllib.request as req
import json
src="http://117.56.59.17/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
with req.urlopen(src) as response:
    data=json.load(response)
# print(data)
slist=data["data"]
# print(slist)
# for stName in slist:
#     print(stName["stationName"])
with open("data.txt","w",encoding="utf-8") as file:
    for st in slist:
        file.write(st["stationName"]+"\n")