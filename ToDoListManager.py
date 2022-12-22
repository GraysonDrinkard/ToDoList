import tkinter as tk
from tkinter import filedialog
from tkinter import Button
from ToDoList import ToDoList
import tempfile
import os

class ToDoListManager():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("To-Do List Hub")
        self.lists = {}
        self.current_list = None
        self.create_button = tk.Button(self.window, text = "Create New List", command = self.create_list)
        self.create_button.pack()
        self.open_button = tk.Button(self.window, text = 'Open List', command = self.open_list)
        self.open_button.pack()
        self.buttons = []

    def create_list(self):
        dialog = tk.Toplevel(self.window)
        dialog.title("Enter List name")
        label = tk.Label(dialog, text ='List Name:')
        label.pack(side ='left')
        entry = tk.Entry(dialog)
        entry.pack(side="left")
        # Create a button to create the list
        button = tk.Button(dialog, text="Create", command=lambda: self._create_list(dialog, entry))
        button.pack(side="left")
    
    def _create_list(self, dialog, entry):
        # Get the list name from the entry widget
        list_name = entry.get()
        if not list_name:
         return
        # Choose the file location
        file_location = "C:/Users/grayg/PythonScripts/tkinter_play"
        file_path = f"{file_location}/{list_name}.txt"
        # Open the file in write mode
        file = tempfile.NamedTemporaryFile(mode="w", delete=False)
        # Write some content to the file
        file.write("Write your to-do items here, one per line.\n")
        # Close the file
        file.close()
        # Rename the file to the desired file name
        os.rename(file.name, file_path)
        # Create a new ToDoList instance with the file name
        self.current_list = ToDoList(file_path)
        self.lists[file_path] = self.current_list
        # Close the dialog window
        dialog.destroy()




    def open_list(self):
        for widget in self.window.pack_slaves():
            if isinstance(widget, tk.Button):
                if not (widget.cget('text') == 'Create New List' or widget.cget('text') == 'Open List'):
                    widget.destroy()
        self.create_button.pack()
        self.open_button.pack()
        file_location = "C:/Users/grayg/PythonScripts/tkinter_play"
        file_names = [file for file in os.listdir(file_location) if file.endswith(".txt")]
        for file_name in file_names:
                button = Button(self.window, text=file_name, command = lambda file = file_name: self._open_list(file))
                button.pack()
            
        
    def _open_list(self, name):
        file_location = "C:/Users/grayg/PythonScripts/tkinter_play"
        file_path = f"{file_location}/{name}"
        self.current_list = ToDoList(file_path)
        self.lists[file_path] = self.current_list

manager = ToDoListManager()
manager.window.mainloop()

