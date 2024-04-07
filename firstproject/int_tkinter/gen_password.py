
import string
from tkinter import *
import random

def gen_pass():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(random.choice(all_chars) for x in range (random.randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("Password Generator")
window.geometry("1080x720")
#window.iconbitmap("firstproject\int_tkinter\logo.ico")
window.config(bg='white')

frame = Frame(window, bg='white')

width = 720
height = 480
#image = PhotoImage(file="firstproject\int_tkinter\sandtroopers.png").zoom(35).subsample(32)
canevas = Canvas(frame, width=width, height=height, bg='white', bd=0, highlightthickness=0)
#canevas.create_image(width/2, height/2, image=image)
canevas.grid(row=0,column=0, sticky=W)

right_frame = Frame(frame, bg='white')

label_title = Label(right_frame, text="Password", font=("Helvetica", 20), bg='white', fg='black')
label_title.pack()

password_entry = Entry(right_frame, font=("Helvetica", 20), bg='white', fg='black')
password_entry.pack()

btn_gen_title = Button(right_frame, text="Generate", font=("Helvetica", 20), bg='white', fg='black', command=gen_pass)
btn_gen_title.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=gen_pass)
file_menu.add_command(label="Quit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)

window.mainloop()