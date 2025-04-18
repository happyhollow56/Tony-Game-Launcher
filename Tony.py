import tkinter as tk
import os
import sys
import webbrowser
import subprocess
from typing import Callable


GW2 = r"C:\Guild Wars 2\Gw2-64.exe"
GW2WIKI = "https://wiki.guildwars2.com/wiki/Main_Page"
GW2EFF = "https://gw2efficiency.com"
RL = r"C:\Program Files (x86)\Steam\steamapps\common\rocketleague\Binaries\Win64\RocketLeague.exe"
BMOD = r"C:\Program Files\BakkesMod\BakkesMod.exe"
SATIS = r"C:\Program Files (x86)\Steam\steamapps\common\Satisfactory\FactoryGameSteam.exe"

def rootcfg() -> tk.Tk:
    root = tk.Tk()
    root.title('config Launcher')
   
    root.configure(bg='black')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.geometry('1100x700')
    return root



def successful_launch(title: str, root: tk.Tk) -> None: 
    success_win = tk.Toplevel(root)
    root.attributes('-topmost',True)
    success_win.title("Success")
    success_win.geometry("250x100")
    success_win.configure(bg="lightgreen")
    tk.Label(success_win, text=f"{title} Launch Successful!", bg="lightgreen", font=("Arial", 12)).pack(pady=20)
    success_win.after(1500, success_win.destroy)


def open_app(gamepath: str, title: str, root: tk.Tk) -> None:
    try:
        if sys.platform == 'win32':
            os.startfile(gamepath)
            successful_launch(title, root)
        else:
            print("Unsupported OS")
    except Exception as e:
        print(f"An error has occurred: {e}")


def open_url(URL: str, URLtitle: str, root:tk.Tk) -> None:
    try:
        webbrowser.open(URL)
        successful_launch(URLtitle, root)
    except Exception as e:
        print(f"An error has occured: {e}")


def getFrame(config:tk.Tk, framecolor: str, gRow:int) -> tk.Frame:
    frame = tk.Frame(config, bg= framecolor, padx=10, pady=10)
    frame.grid(row=gRow, column=0, sticky="news", padx=5, pady=5)
    frame.columnconfigure((0, 1), weight=1)
    frame.rowconfigure((0, 1, 2), weight=1) 

    return frame

def addLabel(frame: tk.Frame, title: str, lblcolors: tuple[str,str]) -> None:
    label = tk.Label(frame, text= title, bg= lblcolors[0], fg= lblcolors[1], font=('Arial', 14))
    label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")


def addButton(frame:tk.Frame, title: str, path: str, config: tk.Tk, buttcolors: tuple[str,str], open_func: Callable[[str,str,tk.Tk], None], bRow:int=1, bCol:int=0, padx:int=0, pady:int=10) -> None:
    tk.Button(frame, text= title, width=20, bg= buttcolors[0], fg= buttcolors[1], command=lambda: open_func(path, title, config)).grid(row=bRow, column=bCol, padx=padx, pady=pady, sticky="nsew")


def assemble(config: tk.Tk, framecolor:str, gRow:int, lblcolors: tuple[str,str], title:str) -> tk.Frame: 
    temp = getFrame(config=config, framecolor=framecolor, gRow=gRow)
    addLabel(temp, title=title, lblcolors=lblcolors)

    return temp


def main() -> None:
    root = rootcfg()
   
    gw_btn, gw_lbl, gw_frame = ("black", "white"), ("red", "black"), 'red'
    gw2=assemble(root, gw_frame, 0, gw_lbl, "Guild Wars 2")
    addButton(gw2, "Guild Wars 2", GW2, root, gw_btn, open_app)
    addButton(gw2, "Guild Wars 2 Wiki", GW2WIKI, root, gw_btn, open_url, 1, 1, 10, 10)
    addButton(gw2, "Guild Wars 2 Efficiency", GW2EFF, root, gw_btn, open_url, 2, 1, 10, 10)
    
    rl=assemble(root, "blue", 1, ("blue","light blue"), "Rocket League")
    addButton(rl, "Rocket League", RL, root, ("black","light blue"), open_app)

    satis=assemble(root, "orange", 2, ("orange", "White"), "Satifactory")
    addButton(satis, "Satisfactory", SATIS, root, ("black", "orange"), open_app)
    
    
    
    
    
    root.mainloop()

main()
