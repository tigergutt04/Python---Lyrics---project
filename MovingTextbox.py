import tkinter as tk

root = tk.Tk()
root.title("Lyrics Project")
root.geometry("300x200")

root.pack_propagate(False) 

label = tk.Label(root, text="Hei, verden!")
label.pack(expand=True)  

root.mainloop()
