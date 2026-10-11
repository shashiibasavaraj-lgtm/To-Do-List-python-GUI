import tkinter as tk
import os

FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

def save_tasks():
    with open(FILE, 'w') as f:
        tasks = listbox.get(0, tk.END)
        for t in tasks:
            f.write(t + "\n")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        listbox.delete(listbox.curselection())
        save_tasks()
    except:
        pass

root = tk.Tk()
root.title("My To-Do List")
root.geometry("400x450")

tk.Label(root, text="To-Do List", font=("Arial", 18, "bold")).pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task, bg="black", fg="white", width=20).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_task, bg="red", fg="white", width=20).pack(pady=5)

listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 11))
listbox.pack(pady=10)

load_tasks()
root.mainloop()
