from tkinter import *
try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *


root = Tk()
def drop():
    root=Tk()
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Add", command=drop)
subMenu.add_command(label="Open", command=drop)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=drop)
root.title('Tech Wizards')
root.geometry('{}x{}'.format(460, 350))






def create_window():

    window = Tk()

    window.title("Create Swarm")
    v=Label(window, text="Select file from directory")
    e1 = Entry(window)
    v.pack()
    e1.pack()
    R3 = Radiobutton(window, text="Public", value=0)
    R3.pack(padx=5, pady=5)
    R4 = Radiobutton(window, text="Private", value=1)
    R4.pack(padx=5, pady=5)
    button10 = Button(window, text="Cancel")
    button10.pack(padx=5, pady=10, side=LEFT)
    button11= Button(window, text="Create")
    button11.pack(padx=5, pady=10, side=LEFT)

    window.mainloop()

def table():

        table = Tk()
        table.title("Search")
        tv = Treeview(table)
        tv['columns'] = ('Filename', 'Peers', 'Size', 'Progress', 'Status')
        tv.heading("#0", text='S.No', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Filename', text='Filename')
        tv.column('Filename', anchor='center', width=200)
        tv.heading('Peers', text='Peers')
        tv.column('Peers', anchor='center', width=100)
        tv.heading('Size', text='Size')
        tv.column('Size', anchor='center', width=100)
        tv.heading('Progress', text='Progress')
        tv.column('Progress', anchor='center', width=100)
        tv.heading('Status', text='Status')
        tv.column('Status', anchor='center', width=100)
        tv.grid(sticky=(N, S, W, E))
        table.treeview = tv
        tv.insert("","end",text = "1", values = ("1","2","3","4","5"))

        table.grid_rowconfigure(0, weight=1)
        table.grid_columnconfigure(0, weight=1)
        button2 = Button(table,text="Download")
        button2.grid_configure()


def table1():
    table1 = Tk()
    table1.title("List of available swarm files")
    tv = Treeview(table1)
    tv['columns'] = ('Filename', 'Peers', 'Size', 'Progress', 'Status')
    tv.heading("#0", text='S.No', anchor='w')
    tv.column("#0", anchor="w")
    tv.heading('Filename', text='Filename')
    tv.column('Filename', anchor='center', width=100)
    tv.heading('Peers', text='Peers')
    tv.column('Peers', anchor='center', width=100)
    tv.heading('Size', text='Size')
    tv.column('Size', anchor='center', width=100)
    tv.heading('Progress', text='Progress')
    tv.column('Progress', anchor='center', width=100)
    tv.heading('Status', text='Status')
    tv.column('Status', anchor='center', width=100)
    tv.grid(sticky=(N, S, W, E))
    table1.treeview = tv

    table1.grid_rowconfigure(0, weight=1)
    table1.grid_columnconfigure(0, weight=1)
    button5 = Button(table1, text="Download")
    button5.grid_configure()
    button6 = Button(table1, text="Delete")
    button6.grid_configure()


button3 = Button(text="List", command=table1)
button3.pack(padx=5, pady=10, side=TOP)
button1 = Button(text="upload", command=create_window)
button1.pack(padx=5, pady=10, side=TOP)
button4 = Button(text="Search", command=table)
button4.pack(padx=5, pady=10, side=TOP)
e5 = Entry()
e5.pack(padx=5, pady=10, side=TOP)




root.mainloop()

