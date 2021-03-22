# import urllib.request as req
# url="https://www.ptt.cc/bbs/movie/index.html"
# with req.urlopen(url) as response:
#     data=response.read().decode("utf-8")
# print(data)

import urllib.request as req
def getData(url):
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    # print(root.title.string)
    # titles=root.find("div",class_="title")
    # print(titles.a.string)
    titles=root.find_all("div",class_="title")
    for titl in titles:
        if titl.a != None:
            print(titl.a.string)
    #抓取網頁資料，request看起來像個人不然會被forbiddne，解析資料(安裝beautifulSoup)，篩選想要的部分
    nextLink=root.find("a",string="‹ 上頁")
    # print(nextLink)
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
# print(getData(pageURL))
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    py+=1

