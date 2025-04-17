import tkinter as tk
import os
import sys
import webbrowser


GW2 = r"C:\Guild Wars 2\Gw2-64.exe"
GW2WIKI = "https://wiki.guildwars2.com/wiki/Main_Page"
GW2EFF = "https://gw2efficiency.com"


root = tk.Tk()
root.title('Tony Launcher')
root.attributes('-topmost',True)

def open_gw2(gw2_path):  # Opens First game 
    try:
        if sys.platform == "win32":
            os.startfile(gw2_path)
        else:
            print("Unsupported OS")
    except Exception as e:
        print(f"An error has occurred: {e}")

def open_gw2Wiki(wikiURL):
    try:
        webbrowser.open(wikiURL)
    except Exception as e:
        print(f"An error has occured: {e}")

def open_gw2EFF(effURL):
    try:
        webbrowser.open(effURL)
    except Exception as e:
        print(f"An error has occured: {e}")




# Frame 1
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, padx=10, pady=10)

# Guild wars 2 launch button
gw2_btn = tk.Button(frame1, text="Open Guild Wars 2", command=lambda: open_gw2(GW2))
gw2_btn.grid(row=0, column=0, pady=10)

# Guild wars 2 wiki launch button
gw2Wiki_btn = tk.Button(frame1, text="Launch Wiki", width=20 , command= lambda: open_gw2Wiki(GW2WIKI))
gw2Wiki_btn.grid(row=0, column=1, padx=10 , pady=10, sticky="e")

# Guild wars 2 efficiency launch button
gw2EFF_btn = tk.Button(frame1, text="Launch GW2 Efficiency", width=20 , command= lambda: open_gw2EFF(GW2EFF))
gw2EFF_btn.grid(row=1, column=1, padx=10 , pady=10, sticky="e")



root.mainloop()




