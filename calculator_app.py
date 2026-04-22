import tkinter as tk
from tkinter import messagebox

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")

        result_var.set(f"Result: {result:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Select operation:").grid(row=2, column=0)

operation_var = tk.StringVar(value='+')
tk.Radiobutton(root, text="+", variable=operation_var, value='+').grid(row=2, column=1, sticky='w')
tk.Radiobutton(root, text="-", variable=operation_var, value='-').grid(row=2, column=2, sticky='w')
tk.Radiobutton(root, text="*", variable=operation_var, value='*').grid(row=2, column=3, sticky='w')
tk.Radiobutton(root, text="/", variable=operation_var, value='/').grid(row=2, column=4, sticky='w')

tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=5)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row=4, column=0, columnspan=5)

# Run the application
root.mainloop()
