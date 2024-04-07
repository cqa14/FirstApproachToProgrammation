
from tkinter import *

def test_com():
    print("Hello")

window = Tk()

window.title("Test")
window.geometry("1080x720")
window.iconbitmap("firstproject\int_tkinter\logo.ico")
window.resizable(False, False)
window.config(background='#3F73FF')

frame = Frame(window, bg='#3F73FF')

label_title = Label(frame, text = ":-)", font=("Arial", 40), bg='#3F73FF', fg='BLACK')
label_title.pack()

label_subtitle = Label(frame, text = "Hihi", font=("Arial", 25), bg='#3F73FF', fg='BLACK')
label_subtitle.pack()

first_btn = Button(frame, text="Hello", font=("Arial, 25"), bg='GREEN', fg='BLACK', command=test_com)
first_btn.pack(pady=25, fill=X)

frame.pack(expand=YES)

window.mainloop()
