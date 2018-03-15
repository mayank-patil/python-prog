# getting User input
num=input("enter a no.: ")
#slicing the string for Two Digit no.
a = int(num[0])
b = int(num[1])
#creating Dictionaries

one={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

two={10:"TEN",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
17:"seventeen",18:"eighteen",19:"ninteen"}

three={20:"twenty",30:"thirty",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninty"}

four={2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninty"}
# if else conditions for Digit
if len(num) == 1:
    print(one.get(int(num)))
elif len(num) == 2 and int(num) < 20:
    print(two.get(int(num)))
elif len(num) == 2 and int(num) >= 20 and  num.endswith("0"):
    print(three.get(int(num)))
elif len(num) == 2 and int(num) > 20:
    print(four.get(int(a)),one.get(int(b)))
else:
    print("Digit is out of range")
