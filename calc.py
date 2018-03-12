from PIL import Image, ImageTk
import datetime
import tkinter as tk
#app window
win = tk.Tk()

win.geometry("400x400")

win.title("Age calculator")

#labels
day_label = tk.Label(text="Day")
day_label.grid(column=0, row=1)

month_label = tk.Label(text="Month")
month_label.grid(column=0, row=2)

year_label = tk.Label(text="Year")
year_label.grid(column=0, row=3)

#Entry
day_entry = tk.Entry()
day_entry.grid(column=1, row=1)

month_entry = tk.Entry()
month_entry.grid(column=1, row=2)

year_entry = tk.Entry()
year_entry.grid(column=1, row=3)


def calculate_age():
    print(day_entry.get())
    print(month_entry.get())
    print(year_entry.get())
    mat = person("mayu",datetime.date(int(year_entry.get()),
                                      int(month_entry.get()),
                                      int(day_entry.get())
                                     )
                )
    print(mat.age())
    print("button got clicked")
#text box
    age_dis = tk.Text(master=win, height=20, width=30)
    age_dis.grid(column=1,row =5)
    age_dis.insert(tk.END,f" is Your Age : {mat.age()} ")

#Buttons
age_button = tk.Button(text="Calculate", command=calculate_age)
age_button.grid(column=1,row = 4)


class person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age

image = Image.open("445989.jpg")
image.thumbnail((100,100),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(image=photo)
img_label.grid(column=1,row=0)
#may = person('mayank', datetime.date(1940,8,20))
#print(may.name)
#print(may.birthdate)
#print(may.age())

win.mainloop()
