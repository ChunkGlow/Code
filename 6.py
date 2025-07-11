import tkinter as tk
from tkinter import ttk
import re

def check_strength(password):
    length = len(password) >= 8
    lower = re.search(r"[a-z]", password) is not None
    upper = re.search(r"[A-Z]", password) is not None
    digit = re.search(r"\d", password) is not None
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length, lower, upper, digit, special])
    if score == 0:
        return ("", "Enter a password", "#cccccc")
    elif score <= 2:
        return ("Weak", "Try adding uppercase, digits, and symbols", "#ff4d4d")
    elif score == 3 or score == 4:
        return ("Medium", "Good! Make it longer or add more variety", "#ffa500")
    else:
        return ("Strong", "Excellent password!", "#4caf50")

def on_key_release(event):
    pwd = password_var.get()
    strength, message, color = check_strength(pwd)
    strength_label.config(text=strength, foreground=color)
    message_label.config(text=message, foreground=color)
    style.configure("TEntry", fieldbackground=color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x220")
root.configure(bg="#222831")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#222831", foreground="#eeeeee", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 12), fieldbackground="#393e46", foreground="#eeeeee")
style.configure("TButton", font=("Segoe UI", 12), background="#00adb5", foreground="#eeeeee")

title_label = ttk.Label(root, text="Enter your password:", font=("Segoe UI", 14, "bold"))
title_label.pack(pady=(20, 10))

password_var = tk.StringVar()
password_entry = ttk.Entry(root, textvariable=password_var, show="*", width=30)
password_entry.pack(ipady=5)
password_entry.bind("<KeyRelease>", on_key_release)

strength_label = ttk.Label(root, text="", font=("Segoe UI", 13, "bold"))
strength_label.pack(pady=(15, 5))

message_label = ttk.Label(root, text="", font=("Segoe UI", 11))
message_label.pack(pady=(0, 20))

root.mainloop()