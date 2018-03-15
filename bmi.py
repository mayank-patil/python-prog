def gather_info():
    h = float(input("enter h : "))
    w = float(input("enter w : "))
    s = input("enter s : ").lower().strip()
    return (h,w,s)
def cal(h,w,s='metric'):
    if s == 'metric':
        bmi = (w/(h**2))
    else:
        bmi = 703 * (w/(h**2))
    return bmi
while True:
    h,w,s=gather_info()
    if s.startswith('i'):
        bmi = cal(h,w,s=s)
        print(f"your bmi is {bmi}")
        break
    elif s.startswith('m'):
        bmi= cal(h,w)
        print(f"bmi  is  {bmi}")
        break
    else:
        print("use bmi m or i")
