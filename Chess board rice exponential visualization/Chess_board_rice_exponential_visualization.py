import tkinter as tk

def create_chessboard():
    root = tk.Tk()
    num = 1
    for i in range(8):
        for j in range(8):
            color = "white" if (i + j) % 2 == 0 else "grey"
            # Format the number in scientific notation with 2 decimal places if it's >= 1000
            text = str(num) if num < 1000 else "{:.2e}".format(num)
            label = tk.Label(root, text=text, bg=color, width=10, height=5)
            label.grid(row=i, column=j)
            num *= 2
    root.mainloop()

create_chessboard()
