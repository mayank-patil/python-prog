import datetime

D = int(input("day :"))
M = int(input("month :"))
Y = int(input("year :"))
DOB = datetime.date(Y,M,D)
print(DOB)
today = datetime.date.today()
age = today.year - DOB.year
print(age)
