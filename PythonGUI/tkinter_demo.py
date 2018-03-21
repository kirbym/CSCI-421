import Tkinter as tk
master = tk.Tk()

def onClick(event=None):
    b["text"] = "button clicked"

b = tk.Button(master, text="asdf")
b.grid(column = 0, row = 0)
b.bind('<Button>', onClick)

tk.mainloop()
