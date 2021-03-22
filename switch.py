score = int(input("輸入0~10 : "))

{
    10 : lambda : print("A"),
    9 : lambda : print("B"),
    8 : lambda : print("C"),
    7 : lambda : print("D"),
    6 : lambda : print("E"),
}.get(score, lambda : print("F"))()