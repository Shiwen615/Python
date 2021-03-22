# class Point:
#     def __init__(self):
#         self.x=3
#         self.y=4
# p1=Point()
# print(p1.x,p1.y)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# p2=Point(5,6)
# print(p2.x,p2.y)

# class FullName:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# name1=FullName("S.W","Hsu")
# print(name1.first,name1.last)

# name1=FullName("S.B","Q")
# print(name1.first,name1.last)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetX,targetY):
#         return ((self.x-targetX)**2+(self.y-targetY)**2)**0.5

# p=Point(3,4)
# p.show()
# print(p.distance(0,0))

class File:
    def __init__(self,name):
        self.name=name
        self.file=None
    def openfile(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    def readfile(self):
        return self.file.read()
f1=File("data1.txt")
f1.openfile()
data=f1.readfile()
print(data)

f2=File("data2.txt")
f2.openfile()
data=f2.readfile()
print(data)
