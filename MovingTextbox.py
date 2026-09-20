import tkinter as tk

def move_window():
    root = tk.Tk()
    root.title("")
    root.geometry("300x200+0+300")

    screen_height = root.winfo_screenheight()

    width = 300
    height = 200

    x = 300
    y = screen_height - height
    speed = -2

    root.geometry(f"{width}x{height}+{x}+{y}")

    def move():
        nonlocal y, speed
        y += speed

        if y >= screen_height - height:
            speed = -2

        if y <= 0:
            speed = 2

        root.geometry(f"{width}x{height}+{x}+{y}")

        root.after(10, move)

    move()
    root.mainloop()

move_window()


