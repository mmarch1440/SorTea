from tkinter import *

class MyApp(object):
    def __init__(self, parent, tea_provider):
        self.root = parent
        self.root.title("Main frame")
        Lb1 = Listbox(self.root)
        for key in sorted(tea_provider.companies):
            Lb1.insert(END, key)
        Lb1.bind('<<ListboxSelect>>', self.onselect)
        Lb1.pack()
        self.frame = Frame(parent)
        self.frame.pack()

    def onselect(self, evt):
        w = evt.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item %d: "%s"' % (index, value))

def LoadWindow(tea_provider):
    root = Tk()
    root.geometry("800x600")
    app = MyApp(root, tea_provider)
    root.mainloop()