import tkinter as tk
import math


root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x520")
root.configure(bg="black")



display = tk.Entry(
    root,
    width=25,
    font=("Arial", 22),
    bd=5,
    relief="solid",
    justify="right",
    bg="black",
    fg="white",
    insertbackground="white"
)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)



def on_click(text):
    if text == "=":
        calculate()

    elif text == "C":
        display.delete(0, tk.END)

    elif text == "π":
        display.insert(tk.END, "pi")

    elif text == "^":
        display.insert(tk.END, "**")

    elif text in ["sin", "cos", "tan", "sqrt", "log"]:
        display.insert(tk.END, text + "(")

    else:
        display.insert(tk.END, text)


def calculate():
    expression = display.get()

    try:
        result = eval(
            expression,
            {
                "__builtins__": None,
                "sin": lambda x: math.sin(math.radians(x)),
                "cos": lambda x: math.cos(math.radians(x)),
                "tan": lambda x: math.tan(math.radians(x)),
                "sqrt": math.sqrt,
                "log": math.log10,
                "pi": math.pi,
                "e": math.e,
                "abs": abs,
                "pow": pow
            }
        )

        display.delete(0, tk.END)
        display.insert(tk.END, str(result))

    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")




buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),("sqrt",1,4),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),("^",2,4),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),("log",3,4),
    ("0",4,0),(".",4,1),("+",4,2),("sin",4,3),("cos",4,4),
    ("tan",5,0),("(",5,1),(")",5,2),("π",5,3),("=",5,4),
    ("C",6,2)
]

for text, row, col in buttons:
    tk.Button(
        root,
        text=text,
        width=8,
        height=2,
        font=("Arial",16),
        bg="#222222",
        fg="white",
        activebackground="#444444",
        activeforeground="white",
        command=lambda t=text: on_click(t)
    ).grid(row=row, column=col, padx=2, pady=2)

root.mainloop()