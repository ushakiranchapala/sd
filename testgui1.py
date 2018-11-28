from tkinter import *
from tkinter import filedialog
from tkinter import ttk

class Clientgui(Frame):
    """ initilize the frame """
    def __init__(self,master):
        ttk.Frame.__init__(self,master)
        mainframe = ttk.Frame(self)
        menu = Menu(self)
        root.config(menu=menu)
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Add")
        subMenu.add_command(label="Open")
        subMenu.add_separator()
        subMenu.add_command(label="Exit")
        root.title('Tech Wizards')
        root.geometry('{}x{}'.format(460, 350))
        self.grid()
        self.mainwindow()




    def create_window(self):
        self.window = Tk()

        self.window.title("Create Swarm")
        v = Label(self.window, text="Select file from directory")

        def callback():
            name = filedialog.askopenfilename()
            print
            name
        filebutton = Button(self.window,text='File Open', command=callback).pack()
        e1 = Entry(self.window)
        v.pack()
        e1.pack()
        R3 = Radiobutton(self.window, text="Public", value=0)
        R3.pack(padx=5, pady=5)
        R4 = Radiobutton(self.window, text="Private", value=1)
        R4.pack(padx=5, pady=5)
        button10 = Button(self.window, text="Cancel")
        button10.pack(padx=5, pady=10, side=LEFT)
        button11 = Button(self.window, text="Create")
        button11.pack(padx=5, pady=10, side=LEFT)



        self.window.mainloop()

    def table(self):
        table = Tk()
        table.title("Search")
        tv = ttk.Treeview(table)
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
        tv.bind('<ButtonRelease-1>')
        tv.grid(sticky=(N, S, W, E))
        table.treeview = tv
        #def progressbar(self):
        #progressbar = ttk.Progressbar(tv,'hotizontal',mode='determinate')
        #progressbar.grid()
        tv.insert("", "end", text="1", values=("1", "2", "3",'4', "5"))

        table.grid_rowconfigure(0, weight=1)
        table.grid_columnconfigure(0, weight=1)
        button2 = Button(table, text="Download")
        button2.grid_configure()

    def table1(self):
        table1 = Tk()
        table1.title("List of available swarm files")
        tv = ttk.Treeview(table1)
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
        #tv.bind('<ButtonRelease-1>',self.create_window())
        tv.grid(sticky=(N, S, W, E))
        table1.treeview = tv

        table1.grid_rowconfigure(0, weight=1)
        table1.grid_columnconfigure(0, weight=1)
        button5 = Button(table1, text="Download")
        button5.grid_configure()
        button6 = Button(table1, text="Delete")
        button6.grid_configure()

    def mainwindow(self):
        self.button3 = Button(self,text="List", command=self.table1).grid()
       # self.button3.pack(padx=5, pady=10, side=TOP)
        self.button1 = Button(self,text="upload", command=self.create_window).grid()
        #self.button1.pack(padx=5, pady=10, side=TOP)
        self.button4 = Button(self,text="Search", command=self.table).grid()
        #self.button4.pack(padx=5, pady=10, side=TOP)
        self.e5 = Entry(self).grid()
        #self.e5.pack(padx=5, pady=10, side=TOP)
        self.tv = ttk.Treeview(root)
        #tv = ttk.Treeview(self)
        self.tv['columns'] = ('Filename', 'Peers', 'Size', 'Progress', 'Status')
        self.tv.heading("#0", text='S.No', anchor='w')
        self.tv.column("#0", anchor="w")
        self.tv.heading('Filename', text='Filename')
        self.tv.column('Filename', anchor='center', width=200)
        self.tv.heading('Peers', text='Peers')
        self.tv.column('Peers', anchor='center', width=100)
        self.tv.heading('Size', text='Size')
        self.tv.column('Size', anchor='center', width=100)
        self.tv.heading('Progress', text='Progress')
        self.tv.column('Progress', anchor='center', width=100)
        self.tv.heading('Status', text='Status')
        self.tv.column('Status', anchor='center', width=100)
        self.tv.bind('<ButtonRelease-1>')
        self.tv.grid()
        self.treeview = self.tv
        # def progressbar(self):
        # progressbar = ttk.Progressbar(tv,'hotizontal',mode='determinate')
        # progressbar.grid()
        self.tv.insert("", "end", text="1", values=("1", "2", "3", '4', "5"))






root = Tk()

app = Clientgui(root)


root.mainloop()
