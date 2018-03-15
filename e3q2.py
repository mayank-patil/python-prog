# calculatinf Factorial of a no.
num = int(input("enter a no : "))
fact =1
for i in range(1,num+1):
    fact = fact*i
print("the factorial of " + str(num) +" is",fact)
