# I will be using functions for organization and modularization purposes as this will continue to become more indepth as i continue to use it after class. I do know that i can make the buttons launch the applications directly instead of calling functions
import tkinter as tk
import os
import sys
import webbrowser
import subprocess


GW2 = r"C:\Guild Wars 2\Gw2-64.exe"
GW2WIKI = "https://wiki.guildwars2.com/wiki/Main_Page"
GW2EFF = "https://gw2efficiency.com"
RL = r"C:\Program Files (x86)\Steam\steamapps\common\rocketleague\Binaries\Win64\RocketLeague.exe"
BMOD = r"C:\Program Files\BakkesMod\BakkesMod.exe"
SATIS = r"C:\Program Files (x86)\Steam\steamapps\common\Satisfactory\FactoryGameSteam.exe"


def rootcfg():
    root = tk.Tk()
    root.title('Tony Launcher')
    root.attributes('-topmost',True)
    root.configure(bg='black')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.geometry('1100x700')
    return root



def successful_launch(title): # Although unnecessary adding this for the second window requirement 
    success_win = tk.Toplevel(root)
    success_win.title("Success")
    success_win.geometry("250x100")
    success_win.configure(bg="lightgreen")
    tk.Label(success_win, text=f"{title} Launch Successful!", bg="lightgreen", font=("Arial", 12)).pack(pady=20)
    success_win.after(1500, success_win.destroy)


def open_gw2(gw2_path):  # Opens First game 
    try:
        if sys.platform == "win32":
            os.startfile(gw2_path)
            successful_launch("Guild Wars 2")
        else:
            print("Unsupported OS")
    except Exception as e:
        print(f"An error has occurred: {e}")


def open_gw2Wiki(wikiURL): # Opens wiki for Guild Wars 2
    try:
        webbrowser.open(wikiURL)
    except Exception as e:
        print(f"An error has occured: {e}")


def open_gw2EFF(effURL): # Opens a website that tracks my progress in game for Guild wars 
    try:
        webbrowser.open(effURL)
    except Exception as e:
        print(f"An error has occured: {e}")


def open_rocketleague(BMOD, RL): # Opens game 2 with a mod that changes
    try:
        subprocess.Popen([BMOD])
        subprocess.Popen([RL]) 
        successful_launch("Rocket League")
    except FileNotFoundError as e:
        print(f"Error: One or more applications are invalid.")
    except Exception as e:
        print(f"An unexpected error has occured:{e}")


def open_satisfactory(Satis_path):
    try:
        if sys.platform == 'win32':
            os.startfile(Satis_path)
            successful_launch("Satisfactory")
        else:
            print("Unsupported OS")
    except Exception as e:
        print(f"An error has occured: {e}")


def gw2_frame(Tony):
    frame = tk.Frame(Tony, bg='red')
    frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    frame.columnconfigure((0, 1), weight=1)
    frame.rowconfigure((0, 1, 2), weight=1)

    label = tk.Label(frame, text="Guild Wars 2", bg='red', fg='black', font=('Arial', 14))
    label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

    tk.Button(frame, text="Guild Wars 2", width=20, bg='black', fg='white', command=lambda: open_gw2(GW2)).grid(row=1, column=0, pady=10, sticky="nsew")

    tk.Button(frame, text="Guild Wars 2 Wiki", width=20, bg='black', fg='white', command=lambda: open_gw2Wiki(GW2WIKI)).grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    tk.Button(frame, text="Guild Wars 2 Efficiency", width=20, bg='black', fg='white', command=lambda: open_gw2EFF(GW2EFF)).grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    return frame


def Rocketleague_frame(Tony):
    frame = tk.Frame(Tony, bg='blue', padx=10, pady=10)
    frame.grid(row=1, column=0, sticky="news", padx=5, pady=5)
    frame.columnconfigure((0, 1), weight=1)
    frame.rowconfigure((0, 1, 2), weight=1)

    label = tk.Label(frame, text="Rocket League", bg='blue', fg='light blue', font=('Arial', 14))
    label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

    tk.Button(frame, text="Rocket League", width=20, bg='black', fg='light blue', command=lambda: open_rocketleague(RL,BMOD)).grid(row=1, column=0, pady=10, sticky="nsew")

    return frame


def satisfactory_frame(Tony):
    frame = tk.Frame(Tony, bg='orange', padx=10, pady=10)
    frame.grid(row=2, column=0, sticky='news', padx=5)
    frame.columnconfigure((0, 1), weight=1)
    frame.rowconfigure((0, 1, 2), weight=1)

    label = tk.Label(frame, text="Satisfactory",bg='orange', fg='white', font=('Arial', 14))
    label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

    tk.Button(frame, text='Satisfactory', width=20, bg='black', fg='orange', command=lambda: open_satisfactory(SATIS)).grid(row=1, column=0, pady=10, sticky="nsew")


root = rootcfg()

gw2_frame(root)
Rocketleague_frame(root)
satisfactory_frame(root)

root.mainloop()



