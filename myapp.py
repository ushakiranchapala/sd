from tkinter import *
from tkinter import filedialog
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
root.geometry('{}x{}'.format(800, 450))






def create_window():

    window = Tk()

    window.title("Create Swarm")
    v=Label(window, text="Select file from directory")

    def callback():
        name = filedialog.askopenfilename()

        filename = str(name)
        filetext.insert(0.0,filename)

    filetext = Text(window, width=20, height=1, wrap=WORD)
    filebutton = Button(window, text='File Open', command=callback).pack()
    e1 = Entry(window)
    v.pack()

    #filetext.insert(0,0,callback.name)
    filetext.pack()
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

def searchtable():

        searchtable = Tk()
        searchtable.title("Search")
        tv = Treeview(searchtable)
        tv['columns'] = ('Filename', 'size', 'ipaddress')
        tv.heading("#0", text='S.No', anchor='w')
        tv.column("#0", anchor="w")
        tv.heading('Filename', text='Filename')
        tv.column('Filename', anchor='center', width=200)
        tv.heading('size', text='size')
        tv.column('size', anchor='center', width=100)
        tv.heading('ipaddress', text='ipaddress')
        tv.column('ipaddress', anchor='center', width=100)
        #tv.heading('Progress', text='Progress')
        #tv.column('Progress', anchor='center', width=100)
        #tv.heading('Status', text='Status')
        #tv.column('Status', anchor='center', width=100)
        tv.grid(sticky=(N, S, W, E))
        searchtable.treeview = tv
        def searchfiles():
            files = tv.get_children()
            for elements in files:
                tv.delete(elements)
            #database connect
            """dbrows =run_query(query)
            for row in drows:
                tv,insert('',0,text=i,values=row[1],row[2],row[3])"""

        def defdownload():

            pass




        searchtable.grid_rowconfigure(0, weight=1)
        searchtable.grid_columnconfigure(0, weight=1)
        button2 = Button(searchtable,text="Download",command=defdownload)
        button2.grid_configure()
        def defdestroy():
            searchtable.destroy()
        cancelbtn = Button(searchtable,text="cancel",command=defdestroy)
        cancelbtn.grid_configure()


def listtable():
    #display list of swarm files created
    listtable = Tk()
    listtable.title("List of available swarm files")
    tv = Treeview(listtable)
    tv['columns'] = ('Filename', 'ipaddress', 'Size')
    tv.heading("#0", text='S.No', anchor='w')
    tv.column("#0", anchor="w")
    tv.heading('Filename', text='Filename')
    tv.column('Filename', anchor='center', width=100)
    tv.heading('ipaddress', text='ipaddress')
    tv.column('ipaddress', anchor='center', width=100)
    tv.heading('Size', text='Size')
    tv.column('Size', anchor='center', width=100)
    
    tv.grid(sticky=(N, S, W, E))
    listtable.treeview = tv

    listtable.grid_rowconfigure(0, weight=1)
    listtable.grid_columnconfigure(0, weight=1)

    def uploadfile():
        pass

    uploadbtn = Button(listtable,text="upload", command=uploadfile)
    uploadbtn.grid()

    def defdelete():
        pass

    button5 = Button(listtable, text="delete",command = defdelete)
    button5.grid_configure()
    def defcancel():
        listtable.destroy()
    button6 = Button(listtable, text="cancel",command = defcancel)
    button6.grid_configure()


def setvisible():
    pass
def setdark():
    pass

button3 = Button(text="List", command=listtable).place(x=20,y=20)
#button3.pack(padx=5, pady=10, side=TOP)
button1 = Button(text="Create", command=create_window).place(x=100,y=20)
#button1.pack(padx=5, pady=10, side=TOP)
button4 = Button(text="Search", command=searchtable).place(x=180,y=20)
#button4.pack(padx=5, pady=10, side=TOP)
visiblebtn =Button(text='visible',command = setvisible).place(x=260,y=20)
#visiblebtn.pack()
uplabel =Label(text="upload progress")
uplabel.place(x=620,y=50)
downlabel = Label(text="download progress")
downlabel.place(x=490,y=50)
darkbtn =Button(text='set dark',command = setdark).place(x=340,y=20)
downprog = Progressbar(orient ='horizontal',length =100,mode="determinate")
downprog.place(x=490,y=70)
uploadprog = Progressbar(orient ='horizontal',length=100,mode="determinate")
uploadprog.place(x=620,y=70)

tv = Treeview(root)
tv['columns'] = ('Filename', 'size', 'ipaddress', 'status')
tv.heading("#0", text='S.No', anchor='w')
tv.column("#0", anchor="w")
tv.heading('Filename', text='Filename')
tv.column('Filename', anchor='center', width=100)

tv.heading('size', text='size')
tv.column('size', anchor='center', width=100)
tv.heading('ipaddress', text='ipaddress')
tv.column('ipaddress', anchor='center', width=100)
tv.heading('status', text='status')
tv.column('status', anchor='center', width=100)
tv.place(x=50,y=100)
root.treeview = tv


#e5 = Entry()
#e5.pack(padx=5, pady=10, side=TOP)




root.mainloop()
