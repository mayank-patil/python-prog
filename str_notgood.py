"""a = input("enter a str : ")
str1 = "The lyrics is not that poor!"
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')


  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
"""
str1 = "The lyrics is not that poor"
print(str1)
str2 = str1.find('not')
str3 = str1.find('poor')
if str3 > str2 and str2 > 0 and str3 > 0:
    str1 =  str1.replace(str1[str2:(str3+4)],"good")
print(str1)
