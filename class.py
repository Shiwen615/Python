class FirstClass:
    # """My first class in python."""
    str1 = "Apple"
    str2 = "IBM"
    def __init__(self, str1="參數1", str2="參數2"):
        self.str1 = str1
        self.str2 = str2
    # def __init__(self):
    #     self.str1 = "Banana"
    #     self.str2 = "Orange"
 
    def fun(self):
        return "Hello world."
 
my_obj = FirstClass()
print(my_obj.str1)
print(my_obj.str2)
print("===分隔線===")
my_obj2 = FirstClass("我是參數1")
print(my_obj2.str1)
print(my_obj2.str2)
print("===分隔線===")
my_obj3 = FirstClass("我是參數1", "我是參數2")
print(my_obj3.str1)
print(my_obj3.str2)


