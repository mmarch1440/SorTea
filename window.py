import tkinter as tk
from tkinter import ttk

class TeaWindow(object):
    def __init__(self, parent, tea_provider):
        self.tea_provider = tea_provider
        self.root = parent
        self.listframe = ttk.Frame(self.root, width=200)
        self.listframe.grid(row=0, column=0, padx=10, pady=5)
        self.listframe.pack(anchor=tk.W, fill=tk.Y, expand=False, side=tk.LEFT)
        self._initList()
        self.tableframe = ttk.Frame(self.root, height=600)
        self.tableframe.pack(anchor=tk.S, fill=tk.BOTH, expand=True)
        self.teaTable = TeaTable(self.tableframe)

    def _onselectCompany(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.teaTable.displayCompaniesTeas(self.tea_provider.companies[value])

    def _initList(self):
        scrollbar = ttk.Scrollbar(self.listframe, orient="vertical")
        self.companyListBox = tk.Listbox(self.listframe, yscrollcommand=scrollbar.set, relief=tk.SUNKEN)
        scrollbar.config(command=self.companyListBox.yview)
        scrollbar.pack(side="left", fill="y")
        for key in sorted(self.tea_provider.companies):
            self.companyListBox.insert(tk.END, key)
        self.companyListBox.bind('<<ListboxSelect>>', self._onselectCompany)
        self.companyListBox.pack(fill="y", expand=True)
        
    def _resetList(self):
        self.companyListBox.delete(0,tk.END)
        for key in sorted(self.tea_provider.companies):
            self.companyListBox.insert(tk.END, key)
        
class TeaDisplay(object):
    def __init__(self, parent):
        self.root = parent

class TeaTable(object):
    def __init__(self, parent):
        self.root = parent
        self._initTeaDisplay()
        self._initTeasTable()

    def _initTeasTable(self):
        self.columns = ('Name', 'Score')
        self.teaTable = ttk.Treeview(self.root, columns=self.columns, show='headings')
        self.teaTable.heading('Name', text='Name')
        self.teaTable.heading('Score', text='Score')
        self.teaTable.pack(fill=tk.X, expand=True)
        self.teaTable.bind("<ButtonRelease-1>", self._on_table_click)

    def _initTeaDisplay(self):
        self.label = tk.Label(self.root,
            text="Pick a tea",
            width=10,
            height=10
        )
        self.label.pack(anchor=tk.N,  fill=tk.BOTH)

    def _displayTea(self, name):
        selectedTea = None
        for tea in self.currentCompany.teas:
            if tea.name == name:
                selectedTea = tea
        if selectedTea != None:
            self.label['text'] = selectedTea.name

    def displayCompaniesTeas(self, teaCompany):
        self.currentCompany = teaCompany
        self.teaTable.delete(*self.teaTable.get_children())
        for tea in teaCompany.teas:
            self.teaTable.insert('', tk.END, values=(tea.name, tea.score))

    def _on_table_click(self, event):
        region = self.teaTable.identify("region", event.x, event.y)
        if region == "heading":
            print("HEADING clicked")
        elif region == "cell":
            content = self.teaTable.item(self.teaTable.focus())
            self._displayTea(content['values'][0])


def LoadWindow(tea_provider):
    root = tk.Tk()
    style = ttk.Style(root)
    root.tk.call('source', 'forest-dark.tcl')
    style.theme_use("forest-dark")
    root.title("SorTea")
    root.geometry("800x600")
    teaWindow = TeaWindow(root, tea_provider)
    root.mainloop()