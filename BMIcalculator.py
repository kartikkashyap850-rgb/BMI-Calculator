import tkinter as tk
from tkinter import messagebox

# ===== FUNCTIONS =====
def calculate_bmi():
    try:
        weight = float(entry_weight.get().strip())
        height = float(entry_height.get().strip())

        if weight <= 0 or height <= 0:
            raise ValueError("Inputs must be positive numbers.")

        bmi = weight / (height ** 2)
        bmi_rounded = round(bmi, 2)
        category = bmi_category(bmi)

        label_result.config(text=f"BMI: {bmi_rounded}  —  {category}")

    except Exception as e:
        messagebox.showerror(
            "Input Error",
            f"Please enter valid numbers.\nDetails: {e}"
        )

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def clear_fields():
    entry_weight.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    label_result.config(text="BMI: -  —  -")

# ===== GUI SETUP =====
root = tk.Tk()
root.title("Styled BMI Calculator")
root.geometry("400x300")
root.configure(bg="#f0f4f7")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="BMI Calculator",
    font=("Helvetica", 20, "bold"),
    bg="#f0f4f7",
    fg="#333"
).pack(pady=15)

# Weight Input
frame_weight = tk.Frame(root, bg="#f0f4f7")
tk.Label(
    frame_weight,
    text="Weight (kg):",
    font=("Helvetica", 12),
    bg="#f0f4f7"
).pack(side=tk.LEFT, padx=5)

entry_weight = tk.Entry(
    frame_weight,
    font=("Helvetica", 12),
    width=10,
    bd=2,
    relief="groove"
)
entry_weight.pack(side=tk.LEFT, padx=5)
frame_weight.pack(pady=5)

# Height Input
frame_height = tk.Frame(root, bg="#f0f4f7")
tk.Label(
    frame_height,
    text="Height (m):",
    font=("Helvetica", 12),
    bg="#f0f4f7"
).pack(side=tk.LEFT, padx=5)

entry_height = tk.Entry(
    frame_height,
    font=("Helvetica", 12),
    width=10,
    bd=2,
    relief="groove"
)
entry_height.pack(side=tk.LEFT, padx=5)
frame_height.pack(pady=5)

# Buttons
frame_buttons = tk.Frame(root, bg="#f0f4f7")
tk.Button(
    frame_buttons,
    text="Calculate BMI",
    font=("Helvetica", 12, "bold"),
    bg="#D79F27",
    fg="white",
    width=15,
    bd=0,
    command=calculate_bmi
).pack(side=tk.LEFT, padx=5)

tk.Button(
    frame_buttons,
    text="Clear",
    font=("Helvetica", 12, "bold"),
    bg="#19b121",
    fg="white",
    width=8,
    bd=0,
    command=clear_fields
).pack(side=tk.LEFT, padx=5)

frame_buttons.pack(pady=15)

# Result
label_result = tk.Label(
    root,
    text="BMI: -  —  -",
    font=("Helvetica", 14),
    bg="#f0f4f7",
    fg="#222"
)
label_result.pack(pady=10)

# Tip
tk.Label(
    root,
    text="Enter weight in kg and height in meters.\nExample: 70 kg, 1.75 m",
    font=("Helvetica", 10),
    bg="#f0f4f7",
    fg="#555"
).pack(pady=5)

root.mainloop()
