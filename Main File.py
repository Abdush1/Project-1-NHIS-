from tkinter import*
from math import*

#For Back Space
def BackSpace():
    ex=screen.get()
    if ex:
        ex=ex[:-1] # Remove Last character
        screen.delete(0,END)
        screen.insert(0,ex)

def getvals(event):
    value = event.widget.cget('text')
    if value == 'AC':
        sc_variable.set(' ')
    elif value == '=':
        try:
            ex = screen.get()
            ex = ex.replace('÷', '/')
            ex = ex.replace('%', '/100')
            sc_variable.set(eval(ex)) 
            screen.update()
        except Exception as e:
            sc_variable.set('Error')
            screen.update()
    else:
        sc_variable.set(f'{sc_variable.get()}{value}')




root = Tk()
root.geometry('430x490')
root.title('My 1st Calcii')
root.resizable(False, False)


sc_variable = StringVar()
screen = Entry(root, textvariable=sc_variable, font=('Helvetica', 35,'bold'), fg='black', bg='white', borderwidth=5, justify=RIGHT)
screen.pack(pady=5)

# 1st Button Frame (AC , ( , ), ÷ , ←)

f=Frame(root)
f.pack()
b1=Button(f,text='AC',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='Red', width=3)
b2=Button(f,text='(',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b3=Button(f,text=')',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b4=Button(f,text='÷',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5 = Button(f, text=' ← ', font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='Red', width=3, command=BackSpace)

buttons=[b1,b2,b3,b4,b5]
count=0
for i in range(5):
    buttons[count].grid(row=1, column=i)
    count += 1

# 2nd Button Frame (7, 8, 9, *, Sin)

f=Frame(root)
f.pack()
b1=Button(f,text='7',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b2=Button(f,text='8',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b3=Button(f,text='9',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b4=Button(f,text='*',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='sin',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5]
count=0
for i in range(5):
    buttons[count].grid(row=2, column=i)
    count += 1

# 3rd Button Frame (4, 5, 6, -, cos ) 
f=Frame(root)
f.pack()

b1=Button(f,text='4',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b2=Button(f,text='5',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b3=Button(f,text='6',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b4=Button(f,text='-',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='cos',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5]
count=0
for i in range(5):
    buttons[count].grid(row=3, column=i)
    count += 1

# 4th Button Frame (1, 2, 3, +, tan ) 

f=Frame(root)
f.pack()
b1=Button(f,text='1',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b2=Button(f,text='2',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b3=Button(f,text='3',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b4=Button(f,text='+',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='tan',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5]
count=0
for i in range(5):
    buttons[count].grid(row=4, column=i)
    count += 1

# 5th Button Frame (., 0, 00, %, = ) 

f=Frame(root)
f.pack()
b1=Button(f,text='.',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b2=Button(f,text='0',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='white', bg='black', width=3)
b3=Button(f,text='00',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b4=Button(f,text='%',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='=',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5]
count=0
for i in range(5):
    buttons[count].grid(row=5, column=i)
    count += 1



root.mainloop()