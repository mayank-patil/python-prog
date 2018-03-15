#str1="this_is_my_day"
str1="you are a fool and a blood murderer"
c=str1[::-1]
n=str1.replace(str1[0],c[0],1)
str2 = c.replace(c[0],str1[0],1)
str3=str2[::-1]
nstr=n[:-1]+str3[-1]
print(str1)
print(c)
print(n)
print(str2)
print(str3)
print(nstr)
