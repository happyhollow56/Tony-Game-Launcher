from tkinter import *
from tkinter import filedialog


root = Tk()
root.title('Tony Launcher')
root.geometry("600x400")

def open_gw2():
    guild_Wars= filedialog.askopenfilename()
    

button_1= Button(root, text="Open Guild Wars 2", command=open_gw2)
button_1.pack(pady=20)


root.mainloop()
