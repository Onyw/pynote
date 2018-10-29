#coding=utf-8
import tkinter
import tkinter.messagebox
import tkinter
import tkinter.messagebox
import tkinter.ttk
import sqlite3
x=0
con = sqlite3.connect('d:/users.db')
root = tkinter.Tk()
def Luru():
    root = tkinter.Tk()
    root.title('Selection widgets')
    root['height'] = 400
    root['width'] = 400
    varName = tkinter.StringVar()
    varName.set('')
    varSno=tkinter.StringVar()
    varSno.set('')
    labelName = tkinter.Label(root, text='Name:',justify=tkinter.RIGHT,width=50)
    labelName.place(x=10, y=5, width=50, height=20)
    
    entryName = tkinter.Entry(root, width=120,textvariable=varName)
    entryName.place(x=70, y=5, width=120, height=20)
    
    labelSno = tkinter.Label(root, text='Sno:', justify=tkinter.RIGHT, width=50)
    labelSno.place(x=10, y=40, width=50, height=20)
    
    entrySno = tkinter.Entry(root, width=100,textvariable=varSno)
    entrySno.place(x=70, y=40, width=100, height=20)    
    
    labelDept = tkinter.Label(root, text='Dept:', justify=tkinter.RIGHT, width=50)
    labelDept.place(x=200, y=40, width=40, height=20)
    dept=['cs','ma','en']
    comboDept = tkinter.ttk.Combobox(root, width=40,values=tuple(dept))
    comboDept.place(x=260, y=40, width=40, height=20)
    
    labelSex = tkinter.Label(root, text='Sex:', justify=tkinter.RIGHT, width=50)
    labelSex.place(x=10, y=70, width=50, height=20)
    
    sex = tkinter.IntVar()
    sex.set(1)
    
    radioMan = tkinter.Radiobutton(root,variable=sex,value=1,text='Man')
    radioMan.place(x=70, y=70, width=50, height=20)
    
    radioWoman = tkinter.Radiobutton(root,variable=sex,value=0,text='Woman')
    radioWoman.place(x=130, y=70, width=70, height=20)
    
    def addInformation():
        global x
        x+=1
        y=0
        stu=[]
        stu.append(entrySno.get())
        stu.append(entryName.get())
        if sex.get()==1:
            stu.append("男")
        else:
            stu.append("女")
        stu.append(comboDept.get())
        con.execute("insert into student values(?,?,?,?)",stu)
        result=con.execute("select * from student")
        for i in result:
            y+=1
            if x==y:
                listboxStudents.insert(0,i)
            
    buttonAdd = tkinter.Button(root, text='录入',width=40, command=addInformation)
    buttonAdd.place(x=130, y=100, width=40, height=20)
    
    
    listboxStudents = tkinter.Listbox(root, width=300)
    listboxStudents.place(x=10, y=130, width=300, height=200)
    
    root.mainloop()        

varName = tkinter.StringVar()
varName.set('')
varPwd = tkinter.StringVar()
varPwd.set('')

labelName = tkinter.Label(root, text='User Name:', justify=tkinter.RIGHT, width=80)

labelName.place(x=10, y=5, width=80, height=20)

entryName = tkinter.Entry(root, width=80,textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

labelPwd = tkinter.Label(root, text='User Pwd:', justify=tkinter.RIGHT, width=80)
labelPwd.place(x=10, y=30, width=80, height=20)

entryPwd = tkinter.Entry(root, show='*',width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)

def login():
    
    mz=[]
    mm=[]
    name=entryName.get()
    pwd=entryPwd.get()
    result=con.execute("select name,password from users")
    for i in result:
        mz.append(i[0])
        mm.append(i[1])
    if name in mz:
        if pwd in mm:
            Luru()
        else:
            tkinter.messagebox.showinfo(title='Python tkinter',message='密码错误')
    else:
        tkinter.messagebox.showinfo(title='Python tkinter',message='用户名不存在')
buttonOk = tkinter.Button(root, text='Login', command=login)
buttonOk.place(x=30, y=70, width=50, height=20)

def cancel():
    
    varName.set('')
    varPwd.set('')
buttonCancel = tkinter.Button(root, text='Cancel', command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)

root.mainloop()
