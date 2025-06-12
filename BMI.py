#BMI calculator code
import tkinter as tk
from tkinter import messagebox

# This is the main application window
def calculate_bmi(*args):
    try:
        weight = weight_var.get().strip() #Takes weight as input From user in Kilogram(kg)
        height = height_var.get().strip() #Takes Height as input From user in Centimeter(Cm)
        if not weight or not height:
            result_label.config(text="")  # clears if any field empty
            return

        weight = float(weight) 
        height_m = float(height) / 100  # cm → m
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            cat, color = "Underweight", "#E57373"  # soft red color text
        elif bmi < 24.9:
            cat, color = "Normal weight", "#81C784"  # soft green color text
        elif bmi < 29.9:
            cat, color = "Overweight", "#FFD54F"  # amber color text
        else:
            cat, color = "Obese", "#E57373"  # soft  color text

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {cat}",
            fg=color
        )
    except ValueError:
        # ignore non-numeric until they finish typing
        result_label.config(text="")


def reset_fields():
    """Clear both entries and the result label."""
    weight_var.set("")
    height_var.set("")
    result_label.config(text="")

# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("420x300")
root.configure(bg="#F3F4F6")  # light gray background

# Make rows/cols expandable for responsiveness
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Style variables
label_font = ("Segoe UI", 12)
entry_font = ("Segoe UI", 12)
button_font = ("Segoe UI", 12, "bold")

# Heading
tk.Label(root, text="BMI Calculator",
         font=("Segoe UI", 18, "bold"),
         bg="#F3F4F6",
         fg="#333333").grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(10, 5))

# Weight input
tk.Label(root, text="Weight (kg):", font=label_font, bg="#F3F4F6").grid(row=1, column=0, padx=10, pady=5, sticky="e")
weight_var = tk.StringVar()
weight_entry = tk.Entry(root, textvariable=weight_var, font=entry_font, bd=2, relief="groove")
weight_entry.grid(row=1, column=1, padx=10, pady=5, sticky="we")

# Height input
tk.Label(root, text="Height (cm):", font=label_font, bg="#F3F4F6").grid(row=2, column=0, padx=10, pady=5, sticky="e")
height_var = tk.StringVar()
height_entry = tk.Entry(root, textvariable=height_var, font=entry_font, bd=2, relief="groove")
height_entry.grid(row=2, column=1, padx=10, pady=5, sticky="we")

# Trace entries for live update
weight_var.trace_add('write', calculate_bmi)
height_var.trace_add('write', calculate_bmi)

# Buttons: Calculate & Reset
calc_btn = tk.Button(root,
                     text="Calculate",
                     command=calculate_bmi,
                     font=button_font,
                     bg="#1976D2",
                     fg="white",
                     activebackground="#1565C0",
                     relief="ridge",
                     bd=3)
calc_btn.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

reset_btn = tk.Button(root,
                      text="Reset",
                      command=reset_fields,
                      font=button_font,
                      bg="#757575",
                      fg="white",
                      activebackground="#616161",
                      relief="ridge",
                      bd=3)
reset_btn.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

# Result label
result_label = tk.Label(root,
                        text="",
                        font=("Segoe UI", 14, "bold"),
                        bg="#F3F4F6",
                        fg="#333333",
                        justify="center")
result_label.grid(row=4, column=0, columnspan=2, padx=10, sticky="nsew", pady=(5, 15))

root.mainloop()