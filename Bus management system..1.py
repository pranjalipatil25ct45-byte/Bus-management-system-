import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# -----------------------------
# Bus Reservation System
# -----------------------------

root = tk.Tk()
root.title("Bus Reservation System")
root.geometry("700x600")
root.resizable(False, False)

# -----------------------------
# Functions
# -----------------------------

def book_ticket():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    source = source_entry.get()
    destination = destination_entry.get()
    date = date_entry.get()
    bus = bus_entry.get()
    seat = seat_entry.get()

    if name == "" or age == "" or gender == "" or source == "" or \
       destination == "" or date == "" or bus == "" or seat == "":
        messagebox.showerror("Error", "Please fill all details!")
        return

    try:
        int(age)
        int(seat)
    except ValueError:
        messagebox.showerror("Error", "Age and Seat Number must be numbers!")
        return

    result = (
        "========== BUS RESERVATION ==========\n\n"
        f"Passenger Name : {name}\n"
        f"Age            : {age}\n"
        f"Gender         : {gender}\n"
        f"From           : {source}\n"
        f"To             : {destination}\n"
        f"Travel Date    : {date}\n"
        f"Bus Name       : {bus}\n"
        f"Seat Number    : {seat}\n\n"
        "Ticket Status  : BOOKED\n"
        "======================================"
    )

    output.delete("1.0", tk.END)
    output.insert(tk.END, result)

    messagebox.showinfo("Success", "Bus ticket booked successfully!")


def clear_data():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    source_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    bus_entry.delete(0, tk.END)
    seat_entry.delete(0, tk.END)
    output.delete("1.0", tk.END)


# -----------------------------
# Heading
# -----------------------------

title = tk.Label(
    root,
    text="BUS RESERVATION SYSTEM",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)


# -----------------------------
# Input Frame
# -----------------------------

frame = tk.Frame(root)
frame.pack()

# Passenger Name
tk.Label(frame, text="Passenger Name:", font=("Arial", 11)).grid(
    row=0, column=0, padx=10, pady=7, sticky="w"
)
name_entry = tk.Entry(frame, width=35)
name_entry.grid(row=0, column=1, padx=10, pady=7)


# Age
tk.Label(frame, text="Age:", font=("Arial", 11)).grid(
    row=1, column=0, padx=10, pady=7, sticky="w"
)
age_entry = tk.Entry(frame, width=35)
age_entry.grid(row=1, column=1, padx=10, pady=7)


# Gender
tk.Label(frame, text="Gender:", font=("Arial", 11)).grid(
    row=2, column=0, padx=10, pady=7, sticky="w"
)
gender_entry = tk.Entry(frame, width=35)
gender_entry.grid(row=2, column=1, padx=10, pady=7)


# From
tk.Label(frame, text="From:", font=("Arial", 11)).grid(
    row=3, column=0, padx=10, pady=7, sticky="w"
)
source_entry = tk.Entry(frame, width=35)
source_entry.grid(row=3, column=1, padx=10, pady=7)


# To
tk.Label(frame, text="To:", font=("Arial", 11)).grid(
    row=4, column=0, padx=10, pady=7, sticky="w"
)
destination_entry = tk.Entry(frame, width=35)
destination_entry.grid(row=4, column=1, padx=10, pady=7)


# Travel Date
tk.Label(frame, text="Travel Date:", font=("Arial", 11)).grid(
    row=5, column=0, padx=10, pady=7, sticky="w"
)
date_entry = tk.Entry(frame, width=35)
date_entry.grid(row=5, column=1, padx=10, pady=7)


# Bus Name
tk.Label(frame, text="Bus Name:", font=("Arial", 11)).grid(
    row=6, column=0, padx=10, pady=7, sticky="w"
)
bus_entry = tk.Entry(frame, width=35)
bus_entry.grid(row=6, column=1, padx=10, pady=7)


# Seat Number
tk.Label(frame, text="Seat Number:", font=("Arial", 11)).grid(
    row=7, column=0, padx=10, pady=7, sticky="w"
)
seat_entry = tk.Entry(frame, width=35)
seat_entry.grid(row=7, column=1, padx=10, pady=7)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

book_button = tk.Button(
    button_frame,
    text="BOOK TICKET",
    font=("Arial", 11, "bold"),
    command=book_ticket,
    width=15
)
book_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 11, "bold"),
    command=clear_data,
    width=15
)
clear_button.grid(row=0, column=1, padx=10)


# -----------------------------
# Output
# -----------------------------

tk.Label(
    root,
    text="Reservation Details",
    font=("Arial", 14, "bold")
).pack()

output = tk.Text(
    root,
    height=10,
    width=65,
    font=("Courier New", 10)
)
output.pack(pady=8)


# -----------------------------
# Run Application
# -----------------------------

root.mainloop()