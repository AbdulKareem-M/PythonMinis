from tkinter import *
from tkcalendar import *

root = Tk()
root.title("calendar")
root.geometry("600x400")

cal = Calendar(root, year=2024, month=1, day=5)
cal.pack(pady=0)

root.mainloop()
