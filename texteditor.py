import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=1, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Word Count", command=self.word_count)

        self.status_bar = tk.Label(self.root, text="Ready", anchor='w')
        self.status_bar.pack(side='bottom', fill='x')

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.status_bar.config(text="New File")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                               filetypes=[("Text Documents", "*.txt"), 
                                                          ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.status_bar.config(text=f"Opened: {file_path}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text Documents", "*.txt"), 
                                                            ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.status_bar.config(text=f"Saved: {file_path}")

    def exit_editor(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

    def word_count(self):
        text_content = self.text_area.get(1.0, tk.END)
        word_count = len(text_content.split())
        self.status_bar.config(text=f"Word Count: {word_count}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()

