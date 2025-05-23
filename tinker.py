import tkinter as tk

root=tk.Tk()
root.title("tonybalony")


def add_to_list(entry, text_list):
    text = entry.get()
    if text:
        text_list.insert(tk.END, text)
        entry.delete(0, tk.END)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)


# frame 1
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)

button_1=tk.Button(root, text="Open Guild Wars 2",)


#frame 2

frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)

entry2=tk.Entry(frame2)
entry2.grid(row=0, column=0, sticky="ew")

entry2.bind("<Return>", lambda event: add_to_list(entry2, text_list2))

entry2_btn=tk.Button(frame2, text="add", command=lambda: add_to_list(entry2, text_list2))
entry2_btn.grid(row=0, column=1)

text_list2 = tk.Listbox(frame2)
text_list2.grid(row=1, column=0, columnspan=2, sticky="nsew")

root.mainloop()


