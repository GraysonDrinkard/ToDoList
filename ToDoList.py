import tkinter as tk


class ToDoList:
    def __init__ (self, name):
        self.name = name
        self.window = tk.Tk()
        self.window.title(name)
        self.listbox = tk.Listbox(self.window)
        self.listbox.config(bg = 'black', font = ('didot', 11), fg = 'white')
        self.listbox.pack()
        self.entry = tk.Entry(self.window)
        self.entry.config(bg = 'black', font = ('didot', 11), fg = 'white')
        self.entry.pack()
        self.add_button = tk.Button(self.window, text="Add", command=self._add_item)
        self.add_button.config(bg = 'blue', font = ('didot', 11), fg = 'white')
        self.add_button.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.save_button = tk.Button(self.window, text ='Save', command= self._save)
        self.save_button.config(bg = 'red', font = ('didot', 11), fg = 'white')
        self.save_button.pack(side = "bottom")
        self.del_button = tk.Button(self.window, text = 'Delete', command = self._del_item)
        self.del_button.config(bg = 'green', font = ('didot', 11), fg = 'white')
        self.del_button.pack(side = 'bottom')
        self._load()

    def _save(self):
        with open(self.name, "w") as file:
            print("in _save")
            print(self.listbox.get(0,0)[0])
            if self.listbox.get(0,0)[0] == 'Write your to-do items here, one per line.':
                print('in the if statement')
                
                for item in self.listbox.get(1,tk.END):
                    file.write( item + '\n')
            else:
                print('in the else statement')
                for item in self.listbox.get(0,tk.END):
                    file.write( item + '\n')
            
            self.window.destroy()

    def _load(self):
        with open(self.name, 'r') as file:
            for line in file:
                self.listbox.insert(tk.END, line.strip())


    def _add_item(self):
        item = self.entry.get()
        if not item:
            self.entry.delete(0,tk.END)
            return
        for index in range(self.listbox.size()):
            value = self.listbox.get(index)
            if value == item:
                self.entry.delete(0,tk.END)
                return
        self.listbox.insert(tk.END, item)
        self.entry.delete(0, tk.END)

    def on_closing(self):
        with open(f"{self.name}.txt", "w") as f:
            print("in on_closing")
            print(self.listbox.get(0,0))

            if self.listbox.get(0,0)[0] == 'Write your to-do items here, one per line.':
                for item in self.listbox.get(1,tk.END):
                    f.write( item + '\n')
            else:
                for item in self.listbox.get(0,tk.END):
                    f.write( item + '\n')
        self.window.destroy()

    def _del_item(self):
        item = self.entry.get()
        if not item:
            self.entry.delete(0,tk.END)
            return
        for index in range(self.listbox.size()):
            value = self.listbox.get(index)
            if value == item:
                self.listbox.delete(index)
            self.entry.delete(0,tk.END)
            

        


