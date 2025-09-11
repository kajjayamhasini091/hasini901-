import tkinter as tk
from tkinter import filedialog, messagebox
import os

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notepad")
        self.root.geometry("800x600")

        self.filename = None

        # Text Area
        self.text_area = tk.Text(self.root, undo=True, wrap="word")
        self.text_area.pack(fill="both", expand=True)

        # Scrollbar
        scroll = tk.Scrollbar(self.text_area)
        scroll.pack(side="right", fill="y")
        scroll.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scroll.set)

        # Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit Menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_command(label="Undo", command=lambda: self.text_area.event_generate("<<Undo>>"))
        edit_menu.add_command(label="Redo", command=lambda: self.text_area.event_generate("<<Redo>>"))

        # Help Menu
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

    def set_title(self, name=None):
        if name:
            self.root.title(f"{os.path.basename(name)} - Notepad")
        else:
            self.root.title("Untitled - Notepad")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.set_title()

    def open_file(self):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if self.filename:
            self.text_area.delete(1.0, tk.END)
            with open(self.filename, "r") as file:
                self.text_area.insert(1.0, file.read())
            self.set_title(self.filename)

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.set_title(self.filename)
        else:
            self.save_as_file()

    def save_as_file(self):
        self.filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
        )
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.set_title(self.filename)

    def about(self):
        messagebox.showinfo("About Notepad", "Simple Notepad made with Python Tkinter")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    Notepad(root)
    root.mainloop()
