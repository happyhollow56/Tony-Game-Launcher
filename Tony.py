# M08_Final Project
# 2025-04-18 (JAC)
# psuedo code making a  modular frame that can add games as needed.
# NO AI
###


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
SATISPRINT = "https://satisfactory-calculator.com/en/blueprints"
SATISMAP = 'https://satisfactory-calculator.com/en/interactive-map'


def rootcfg() -> tk.Tk:
    """
    Initializing tk object, setting program title, setting program background to black, configuring the window parameters for the program.
   
     Parameters: 
        None
   
     Returns:
        tk.Tk
    """
    root = tk.Tk()
    root.title('Tony Launcher')
    root.configure(bg='black')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.geometry('1920x1080')
    return root



def successful_launch(title: str, root: tk.Tk) -> None: 
    """
    Shows a success window when you have successfully launched a game from the program, and then destroys itself.
       
         Parameters:
            title(str): Title of the function
            root(tk.TK): tk.Tk object from which I am instantiating a new window
       
         Returns:
            None
    """
    success_win = tk.Toplevel(root)
    root.attributes('-topmost',True)
    success_win.title("Success")
    success_win.geometry("250x100")
    success_win.configure(bg="lightgreen")
    tk.Label(success_win, text=f"{title} Launch Successful!", bg="lightgreen", font=("Arial", 12)).pack(pady=20)
    success_win.after(1500, success_win.destroy)


def open_app(gamepath: str, title: str, root: tk.Tk) -> None:
    """
    Tries to launch game if it fails it prints Unsupported OS with an exception for Error handling.
       
         Parameters:
            gamepath(str): File location of selected game
            title(str): Title of selected game
            root(tk.TK): Configuration for successful_launch
       
         Returns:
            None
    """
    try:
        if sys.platform == 'win32':
            os.startfile(gamepath)
            successful_launch(title, root)
        else:
            print("Unsupported OS")
    except Exception as e:
        print(f"An error has occurred: {e}")


def open_url(URL: str, URLtitle: str, root:tk.Tk) -> None:
    """
    Tries to open selected url with and exception for Error handling.
       
         Parameters:
            URL(str): Url of selected website
            URLtitle(Str): Shows the title of selected website
            root(tk.TK): Configuration for successful_launch
       
         Returns:
            None
    """
    try:
        webbrowser.open(URL)
        successful_launch(URLtitle, root)
    except Exception as e:
        print(f"An error has occured: {e}")


def getFrame(config:tk.Tk, framecolor: str, gRow:int) -> tk.Frame:
    """
    Configures frames for each game.
       
         Parameters:
            config(tk.Tk): Configuration for the frame
            framecolor(str): configures the color of the frame
            gRow(int): configures the grid row
       
         Returns:
            tk.Frame
    """
    frame = tk.Frame(config, bg= framecolor, padx=10, pady=10)
    frame.grid(row=gRow, column=0, sticky="news", padx=5, pady=5)
    frame.columnconfigure((0, 1), weight=1)
    frame.rowconfigure((0, 1, 2), weight=1) 

    return frame

def addLabel(frame: tk.Frame, title: str, lblcolors: tuple[str,str]) -> None:
    """
    Adds a label as need to the program for each game.
       
         Parameters:
            frame(tk.Tk): Configuration for the frame
            title(str): Sets the title of the label
            lblcolors(tuple[str.str]): Sets the colors for the label
        
        Returns:
            None
    """
    label = tk.Label(frame, text= title, bg= lblcolors[0], fg= lblcolors[1], font=('Arial', 14))
    label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")


def addButton(frame:tk.Frame, title: str, path: str, config: tk.Tk, buttcolors: tuple[str,str], open_func: Callable[[str,str,tk.Tk], None], bRow:int=1, bCol:int=0, padx:int=0, pady:int=10) -> None:
    """
    Adds a button as needed for either website links or games. 
       
         Parameters:
            frame(tk.Tk): Configuration for the frame
            title(str): Sets the title of the button
            path(str): game path or URL
            config(tk.Tk): configuration for the button
            buttcolors(tuple[str,str]): configures the colors for the button
            open_func(Callable[[str,str,tk.Tk]): adds a function to the button that opens game or URL 
            bRow(int): configure which row the button is in. default = 1
            bCol(int): configure which column the button is in. default = 0
            padx(int): configures the size of the border of the button on x axis. default = 0 
            pady(int): configures the size of the border of the button on y axis. default = 10
       
         Returns:
            None

    """
    tk.Button(frame, text= title, width=20, bg= buttcolors[0], fg= buttcolors[1], command=lambda: open_func(path, title, config)).grid(row=bRow, column=bCol, padx=padx, pady=pady, sticky="nsew")


def assemble(config: tk.Tk, framecolor:str, gRow:int, lblcolors: tuple[str,str], title:str) -> tk.Frame: 
    """
    Utility function that creates a frame and the label
        Parameters:
            config(tk.Tk): configures the frame
            framecolor(str): Configures the color of the frame 
            gRow(int): configures the number of rows the grid starts with
            lblcolors(tuple[str,str]): Adds colors to lbls
            title(str): Adds title to frame
        Returns:
            tk.Frame
    """
    temp = getFrame(config=config, framecolor=framecolor, gRow=gRow)
    addLabel(temp, title=title, lblcolors=lblcolors)

    return temp


def main() -> None:
    """
    Assembles frames, buttons, and labels for each application and website as needed.
        Parameters:
            None
        Returns:
            None
    """
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
    addButton(satis,"Statisfactory Blueprints", SATISPRINT, root, ("black", "orange"),open_url, 1, 1, 10, 10)
    addButton(satis,"Statisfactory Interactive Map", SATISMAP, root, ("black", "orange"),open_url, 2, 1, 10, 10)
    
    
    root.mainloop()

main()
