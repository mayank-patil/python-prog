import time as tp
start = tp.localtime()
print(f"{tp.strftime('%X',start)}")
input("enter any Key to stop")
stop = tp.localtime()
df = tp.mktime(stop)-tp.mktime(start)
print(df)
