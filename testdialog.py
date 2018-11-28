from tkinter import *
from tkinter import filedialog

root = Tk()
def call():
    name = filedialog.askopenfilename()

    print(name)
    text = Text(width=20,height=1,wrap=WORD)
    text.pack()
    text.insert(0.0,name)
    label =Label(text =name )
    label.pack()
button =Button(text='btn',command = call)

button.pack()





root.mainloop()
