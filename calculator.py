# Standard GUI libary for Python.

import tkinter as tk

# Function to handle clicking a button.

def button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, text)


# Main application window and dimensions.

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Display widget (Entry) shows input and results.

display = tk.Entry(root, font=("Arial",24), borderwidth=2, relief="solid", justify="right")
display.pack(pady=10, padx=10, fill="both")

# A grid of buttons for numbers and different operators.

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

buttons = {
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
}

row_val = 0
col_val = 0

for button in buttons:
    b = tk.Button(button_frame, text=button, font=("Arial", 18), relief="solid", borderwidth=1)
    b.grid(row=row_val, column=col_val, ipadx=10, ipady=10, sticky="nsew")
    b.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
    button_frame.grid_rowconfigure(i, weight=1)

root.mainloop()
    