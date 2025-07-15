import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Global variables
current_file = None
current_theme = "Light"


def update_title():
    if current_file:
        root.title(f"{os.path.basename(current_file)} -  Text Editor")
    else:
        root.title("Untitled - Text Editor")

def new_file():
    global current_file
    text.delete(1.0, tk.END)
    current_file = None
    update_title()
    
def open_file():
    global current_file
    file_path = filedialog.askopenfilename(defaultextension = ".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
        current_file = file_path
        update_title()

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully!")
    else:
        save_as()
         
def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text.get(1.0, tk.END))
            current_file = file_path
            update_title()
            messagebox.showinfo("Info", "File saved successfully!")
        except:
            messagebox.showerror(title="Oops!", message="Unable to save file.")
        
def apply_theme():
    """Apply the current theme to the Text widget."""
    if current_theme == "Light":
        text.config(bg="white", fg="black", insertbackground="black")
    else:
        text.config(bg="black", fg="red", insertbackground="red")

def toggle_theme():
    """Switch between Light and Dark theme."""
    global current_theme
    if current_theme == "Light":
        current_theme = "Dark"
    else:
        current_theme = "Light"
    apply_theme()

root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)

# File menu
file_menu = tk.Menu(menu, tearoff=0)

menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Theme menu
theme_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Toggle theme", command=toggle_theme)

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12))
text.pack(expand=tk.YES, fill=tk.BOTH)


apply_theme()
update_title()

root.mainloop()