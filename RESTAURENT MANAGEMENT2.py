import tkinter
from functools import partial
import pickle
from tkinter import END,messagebox
import mysql.connector as mysql
from tkinter import *
from datetime import datetime
from PIL import ImageTk, Image

ext,x,w,l,lp,mng,orderd,bgp,orderprint,smp,pr,itn=[],[],[],[],[],[],[],[],[],[],[],[]

#master window
root=tkinter.Tk()

#FUNCTION RESPONSIBLE FOR CONNECTING PYTHON WITH MYSQL
def conn():
    f=mysql.connect(host="localhost",user="root",password="dan123",database="Restaurant")
    if f.is_connected():
        return [1,f]
    else:
        l1=tkinter.messagebox.showwarning(Warning,"CAN'T CONNECT TO DATABASE PLEASE TRY AGAIN LATER OR CONTACT THE ADMINISTRATOR")
        exit()

#FUNCTION RESPONSIBLE FOR CHECKING WHETHER THE ENTERED USERNAME IS OF STAFF OR ADMIN AND LETS THEM INTO THE DESIRED WINDOW
def ck(n,n1):
    a,b=n.get(),n1.get()
    wel.withdraw()
    con,f=conn()
    
    if con==1:
        cb=f.cursor()
        cb.execute("select * from staff;")
        v=cb.fetchall()
        cb.execute("select * from admin;")
        ad=cb.fetchall()
        
        y=0
        h=0
        for i in range(0,len(v)):
            if a==v[i][0]:
                if b == v[i][1]:
                    h=2
                    
            else:
                for j in range(0,len(ad)):
                    if a==ad[j][0]:
                        if b==ad[j][1]:
                            h=3
                    else:
                        y=1
        f.close()
        if h==0 and y==1:
            l1=tkinter.messagebox.showwarning(Warning,'WRONG USERNAME OR PASSWORD PLEASE TRY AGAIN')
            lgp()
        elif h==3:
            adminmode()
            wel.withdraw()
        elif h==2:
            mng.append(a)
            mng.append(b)
            tabledisp()
            wel.withdraw()

#FUNCTION RESPONSIBLE FOR LOGGING INTO SCREEN
def lgp():
    for i in range(3):
        try:
            if True==bool(pri.winfo_exists()):
                pri.withdraw()
            else:
                pass
        except NameError:
            pass   
        try:
            if True==bool(vw.winfo_exists()):
                vw.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(chb.winfo_exists()):
                chb.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(amn.winfo_exists()):
                amn.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(mna.winfo_exists()):
                mna.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(mnre.winfo_exists()):
                mnre.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(men.winfo_exists()):
                men.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(mnf.winfo_exists()):
                mnf.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(mnre.winfo_exists()):
                mnre.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(rems.winfo_exists()):
                rems.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(rema.winfo_exists()):
                rema.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(total.winfo_exists()):
                total.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(blp2.winfo_exists()):
                blp2.withdraw()
            else:
                pass
        except NameError:
            pass

        try:
            if True==bool(chpas.winfo_exists()):
                chpas.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(disadmin.winfo_exists()):
                disadmin.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(disstaff.winfo_exists()):
                disstaff.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(addmin.winfo_exists()):
                addmin.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(stf.winfo_exists()):
                stf.withdraw()
            else:
                pass
        except NameError:
            pass

        try:
            if True==bool(total1.winfo_exists()):
                total1.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(ords.winfo_exists()):
                ords.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(blp.winfo_exists()):
                blp.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(table.winfo_exists()):
                table.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(adm.winfo_exists()):
                adm.withdraw()
            else:
                pass
        except NameError:
            pass
        try:
            if True==bool(cha.winfo_exists()):
                cha.withdraw()
            else:
                pass
        except NameError:
            pass
    global wel
    root.withdraw()
    wel=Toplevel(root)
    wel.title('LOGIN')
    wel.geometry("350x400")
    wel.minsize(350,400)
    wel.maxsize(350,400)
    wel.configure(bg='#2D00FF')
    
    n= tkinter.StringVar()
    n1= tkinter.StringVar()

    
    lg1=tkinter.Label(wel,text='WELCOME TO RESTAURANT',bg='#2D00FF',fg='cyan',font=('Arial bold',14),).place(x=45,y=10)
    
    lg2=tkinter.Label(wel,text='Enter your login id and password',bg='#2D00FF',fg='cyan',font=('Arial bold',11)).place(x=65,y=60)
    lg3=tkinter.Label(wel,text='User Id',bg='#2D00FF',fg='cyan',font=('Arial bold',11)).place(x=25,y=120)
    lg3=tkinter.Label(wel,text='Password',bg='#2D00FF',fg='cyan',font=('Arial bold',11)).place(x=10,y=150)

    
    eg1=tkinter.Entry(wel,textvariable=n,bg='#E1FBFF',fg='black',bd=2,font=('open sans',11)).place(x=90,y=120)
    eg2=tkinter.Entry(wel,textvariable=n1,bg='#E1FBFF',fg='black',bd=2,font=('open sans',11),show='*').place(x=90,y=150)

    ckw=partial(ck,n,n1)
    bg2=tkinter.Button(wel,text='login',command=lambda:ckw(),bg='green',fg='white',font=('Arial',11)).place(x=120,y=200)

#FUNCTION RESPONSIBLE FOR UPDATING THE INFORMATION INTO A FILE
def savepass(name,pas):
    con,f=conn()
    
    if con==1:
        cb=f.cursor()
        cb.execute("select * from staff;")
        lod=cb.fetchall()
        cb.execute("select * from admin;")
        lods=cb.fetchall()
    

        h,a,b=0,0,0

        for i in range(0,len(lods)):
            if name.get()==lods[i][0]:
                b=1

        for i in range(0,len(lod)):
            if name.get()==lod[i][0]:
                a=1
            else:
                h+=1
        
        if pas.get()=='':
            b=2
        if name.get()=='':
            b=3

        if h==len(lod) and b==0:
            qu="insert into staff values(%s,%s)"
            vl=(name.get(),pas.get())
            cb.execute(qu,vl)
            f.commit()
            messagebox.showinfo("information","THE PERSON IS ADDED")
            adminmode()

        if b==2:
            wstf=tkinter.messagebox.showwarning(Warning,' PASSWORD NOT ENTERED')
            try:
                if True==bool(stf.winfo_exists()):
                    stf.withdraw()
                else:
                    pass
            except NameError:
                pass    
            addstaff()
        if b==3:
            wstf=tkinter.messagebox.showwarning(Warning,' USERNAME NOT ENTERED')
            try:
                if True==bool(stf.winfo_exists()):
                    stf.withdraw()
                else:
                    pass
            except NameError:
                pass    
            addstaff()
        if a==1 or b==1:
            wstf=tkinter.messagebox.showwarning(Warning,' USERNAME ALREADY TAKEN')
            try:
                if True==bool(stf.winfo_exists()):
                    stf.withdraw()
                else:
                    pass
            except NameError:
                pass    
            f.close()
            addstaff()
            
#FUNCTION RESPONSIBLE FOR ADDING STAFFS
def addstaff():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass
    global stf
    stf=Toplevel(root)
    stf.title('STAFF ADDING')
    stf.geometry("500x300")
    stf.minsize(500,300)
    stf.maxsize(500,300)
    stf.configure(bg='#02FFBF')

    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(stf,image=nimg)
    illg.photo=nimg
    button= Button(stf,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=460,y=0)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(stf,image=nimg1)
    illg1.photo=nimg1
    button1= Button(stf,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF',).place(x=0,y=0)

    lst1=tkinter.Label(stf,text='WELCOME TO STAFF ADDING MENU',fg='#0015ff',bg='#02FFBF',font=('Algerian',11)).place(x=100,y=0)
    lst2=tkinter.Label(stf,text="Enter the Staff 's username",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',10)).place(x=20,y=100)
    lst3=tkinter.Label(stf,text="Enter the Staff 's password",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',10)).place(x=20,y=140)

    stnames,stpassw=tkinter.StringVar(),tkinter.StringVar()

    est1=tkinter.Entry(stf,textvariable=stnames,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).place(x=190,y=101)
    est2=tkinter.Entry(stf,textvariable=stpassw,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).place(x=190,y=141)

    savepas=partial(savepass,stnames,stpassw)
    bst1=tkinter.Button(stf,text='CREATE',command=lambda:savepas(),fg='#000C7B',bg='#FF8181',font=('Arial',11)).place(x=190,y=220)

#FUNCTION RESPONSIBLE FOR UPDATING THE ADMINS IN THE FILE
def saveadpass():
    con,f=conn()
    
    if con==1:
        cb=f.cursor()
        cb.execute("select * from staff;")
        lod=cb.fetchall()
        cb.execute("select * from admin;")
        lods=cb.fetchall()
        h,b=0,0

        for i in range(0,len(lods)):
            if adname.get()==lods[i][0]:
                b=1

        for i in range(0,len(lod)):
            if adname.get()==lod[i][0]:
                h=1
        
        if adpass.get()=='':
            b=2
        if adname.get()=='':
            b=3

        if h==0 and b==0:
            qu="INSERT INTO ADMIN VALUES(%s,%s)"
            vl=(adname.get(),adpass.get())
            cb.execute(qu,vl)
            f.commit()
            messagebox.showinfo("information","THE PERSON IS ADDED")  
            adminmode()

        if b==3:
            wstf=tkinter.messagebox.showwarning(Warning,'USERNAME NOT ENTERED')
            try:
                if True==bool(addmin.winfo_exists()):
                    addmin.withdraw()
                else:
                    pass
            except NameError:
                pass    
            addadmin()

        if b==2:
            wstf=tkinter.messagebox.showwarning(Warning,'PASSWORD NOT ENTERED')
            try:
                if True==bool(addmin.winfo_exists()):
                    addmin.withdraw()
                else:
                    pass
            except NameError:
                pass    
            addadmin()

        if h==1 or b==1:
            try:
                if True==bool(addmin.winfo_exists()):
                    addmin.withdraw()
                else:
                    pass
            except NameError:
                pass    
            wstf=tkinter.messagebox.showwarning(Warning,' USERNAME ALREADY TAKEN')
            f.close()
            addadmin()

#FUNCTION RESPONSIBLE TOO CHECK WHETHER THE PASSWORD IS RIGHT OR NOT
def chkpa(ds):
    b=ds.get()
    con,f=conn()
    
    if con==1:
        cb=f.cursor()
        cb.execute("select * from admin;")
        g=cb.fetchall()
        h=0
        a='DAKSHIN'
        for i in range(0,len(g)):
            if a==g[i][0]:
                if b==g[i][1]:
                    h=1

        if h==0:
            rsm=tkinter.messagebox.showwarning(Warning,' WRONG PASSWORD')
            try:
                if True==bool(cha.winfo_exists()):
                    cha.withdraw()
                else:
                    pass
            except NameError:
                pass
            chka()
        elif h==1:
            f.close()
            saveadpass()

#FUNCTION RESPONSIBLE FOR ENTERING THE MANAGER PASSWORD BEFORE ADDING AN ADMIN
def chka():
    global cha
    cha=Toplevel(root)
    cha.title('PASSWORD')
    cha.geometry("250x100")
    cha.minsize(250,100)
    cha.maxsize(250,100)
    cha.configure(bg='black')

    strw=tkinter.StringVar()

    erad2=tkinter.Entry(cha,textvariable=strw,fg='#3305ff',bg='#00ff2a',font=('Bahnschrift SemiLight',11)).place(x=80,y=10)
    lrad1=tkinter.Label(cha,text='Password',fg='white',bg='black',font=('Arial bold',11)).place(x=0,y=10)
    cpa=partial(chkpa,strw)
    brad1=tkinter.Button(cha,text='ADD',fg='#000C7B',bg='#FF8181',font=('Arial',11),command=lambda:cpa()).place(x=90,y=40)
    
#FUNCTION RESPONSIBLE FOR ADDING ADMINS
def addadmin():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(cha.winfo_exists()):
            cha.withdraw()
        else:
            pass
    except NameError:
        pass
    global addmin
    addmin=Toplevel(root)
    addmin.title('ADMIN ADDING')
    addmin.geometry("500x300")
    addmin.minsize(500,300)
    addmin.maxsize(500,300)
    addmin.columnconfigure(0,minsize=50)
    addmin.rowconfigure([0,1],minsize=30)
    addmin.configure(bg='#02FFBF')

    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(addmin,image=nimg)
    illg.photo=nimg
    button= Button(addmin,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=460,y=0)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(addmin,image=nimg1)
    illg1.photo=nimg1
    button1= Button(addmin,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)

    laddm1=tkinter.Label(addmin,text='WELCOME TO ADMIN ADDING MENU',fg='#0015ff',bg='#02FFBF',font=('ALGERIAN',11)).place(x=110,y=0)
    laddm2=tkinter.Label(addmin,text="Enter the Admin 's username",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',10)).grid(row=3,column=1)
    laddm3=tkinter.Label(addmin,text="Enter the Admin 's password",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',10)).grid(row=4,column=1)

    global adname,adpass
    adname,adpass=tkinter.StringVar(),tkinter.StringVar()

    eaddm1=tkinter.Entry(addmin,textvariable=adname,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).grid(row=3,column=4,padx=0,pady=10)
    eaddm2=tkinter.Entry(addmin,textvariable=adpass,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).grid(row=4,column=4,padx=0,pady=10)

    baddm1=tkinter.Button(addmin,text='CREATE',command=lambda:chka(),fg='#000C7B',bg='#FF8181',font=('Arial',11)).grid(row=6,column=1,padx=10,pady=10)

#FUNCTION RESPONSIBLE FOR DISPLAYING ALL THE STAFF MEMEBERS
def displaystaff():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    
    con,f=conn()
    
    if con==1:

        global disstaff
        disstaff=Toplevel(root)
        disstaff.title('STAFF DISPLAY')
        disstaff.geometry("250x500")
        disstaff.minsize(250,500)
        disstaff.maxsize(250,500)
        disstaff.configure(bg='#02FFBF')
        cb=f.cursor()
        cb.execute("select * from staff;")
        prt=cb.fetchall()
        rt=60

        img= Image.open("logof.png")
        rimg= img.resize((30,25))
        nimg= ImageTk.PhotoImage(rimg)
        illg= Label(disstaff,image=nimg)
        illg.photo=nimg
        button= Button(disstaff,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=210,y=0)

        img1= Image.open("back.png")
        rimg1= img1.resize((30,25))
        nimg1= ImageTk.PhotoImage(rimg1)
        illg1= Label(disstaff,image=nimg1)
        illg1.photo=nimg1
        button1= Button(disstaff,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)

        ldst1=tkinter.Label(disstaff,text='STAFF MEMBERS',bg='#02FFBF',fg='#000C7B',font=('Algerian',11)).place(x=34,y=0)
        for i in range(0,len(prt)):
            ldst2=tkinter.Label(disstaff,text=prt[i][0],fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',12)).place(x=60,y=rt)
            rt+=20
        f.close()

#FUNCTION RESPONSIBLE FOR UPDATING THE PASSWORD CHANGES
def scpspass(cpsname,cpspass):
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        con,f=conn()
        
        if con==1:
            cb=f.cursor()
            cb.execute("select * from staff;")
            lod=cb.fetchall()
            h,b,e=0,0,0
            for i in range(0,len(lod)):
                if cpsname.get()==lod[i][0]:
                    h=1
            if cpsname.get()=='':
                b=1
            if cpspass.get()=='':
                e=1
            if h==0 and b==0 and e==0:
                wcps=tkinter.messagebox.showwarning(Warning,' WRONG USERNAME')
                try:
                    if True==bool(chpas.winfo_exists()):
                        chpas.withdraw()
                    else:
                        pass
                except NameError:
                    pass    
                changepass()
            if h==1 and b==0 and e==0:
                t1=(cpspass.get())
                t2=(cpsname.get())
                cb.execute(f"update staff set password='{t1}' where name='{t2}';")
                f.commit()
                f.close()
                messagebox.showinfo("information","THE PASSWORD IS CHANGED")
                adminmode()
            if b==1:
                wcps=tkinter.messagebox.showwarning(Warning,'NO USERNAME ENTERED')
                try:
                    if True==bool(chpas.winfo_exists()):
                        chpas.withdraw()
                    else:
                        pass
                except NameError:
                    pass    
                changepass()

            if e==1 and b==0:
                wcps=tkinter.messagebox.showwarning(Warning,'NO PASSWORD ENTERED')

#FUNCTION RESPONSIBLE FOR DISPLAYING ADMINS
def displayadmin():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    
    
    con,f=conn()
    
    if con==1:

        global disadmin
        disadmin=Toplevel(root)
        disadmin.title('ADMIN DISPLAY')
        disadmin.geometry("250x500")
        disadmin.minsize(250,500)
        disadmin.maxsize(250,500)
        disadmin.configure(bg='#02FFBF')
        cb=f.cursor()
        cb.execute("select * from admin")
        prt=cb.fetchall()
        rt=40

        img= Image.open("logof.png")
        rimg= img.resize((30,25))
        nimg= ImageTk.PhotoImage(rimg)
        illg= Label(disadmin,image=nimg)
        illg.photo=nimg
        button= Button(disadmin,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=210,y=0)

        img1= Image.open("back.png")
        rimg1= img1.resize((30,25))
        nimg1= ImageTk.PhotoImage(rimg1)
        illg1= Label(disadmin,image=nimg1)
        illg1.photo=nimg1
        button1= Button(disadmin,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)

        ldst1=tkinter.Label(disadmin,text='ADMIN MEMBERS',bg='#02FFBF',fg='#000C7B',font=('Algerian',11)).place(x=60,y=0)
        for i in range(0,len(prt)):
            ldst2=tkinter.Label(disadmin,text=prt[i][0],fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',13)).place(x=70,y=rt)
            rt+=20
        f.close()

#FUNCTION RESPONSIBLE FOR CHANGING THE PASSWORD
def changepass():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    

    global chpas
    chpas=Toplevel(root)
    chpas.title('CHANGE PASSWORD')
    chpas.geometry("500x300")
    chpas.minsize(500,300)
    chpas.maxsize(500,300)
    chpas.configure(bg='#02FFBF')



    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(chpas,image=nimg)
    illg.photo=nimg
    button= Button(chpas,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=460,y=0)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(chpas,image=nimg1)
    illg1.photo=nimg1
    button1= Button(chpas,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)

    lcpass1=tkinter.Label(chpas,text='WELCOME TO PASSWORD CHANGE MENU',fg='#0015ff',bg='#02FFBF',font=('ALGERIAN',14)).place(x=50,y=0)
    lcpass2=tkinter.Label(chpas,text="Enter the employee's username",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=45,y=100)

    lcpass3=tkinter.Label(chpas,text="Enter the employee's new password",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=25,y=140)

    cpsname,cpspass=tkinter.StringVar(),tkinter.StringVar()

    ecpass1=tkinter.Entry(chpas,textvariable=cpsname,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).place(x=290,y=100)
    ecpass2=tkinter.Entry(chpas,textvariable=cpspass,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).place(x=290,y=140)

    scpspas=partial(scpspass,cpsname,cpspass)
    bcpass1=tkinter.Button(chpas,text='CHANGE',command=lambda:scpspas(),fg='#000C7B',bg='#FF8181',font=('Arial',11)).place(x=200,y=200)

#FUNCTION RESETS THE VALUE TO 0 IF THE END OF ALL THE BILLS IS REACHED
def reset():
    bgp.clear()
    a=0
    bdsp(a)

#FUNCTION RESPONSIBLE FOR DISPLAYING THE REQUIRED BILL
def bdf():
    con,f=conn()
    if con==1:
        global total
        total=Toplevel(root)
        total.title('Bills so far....')
        total.geometry("300x900")
        total.minsize(300,900)
        total.maxsize(300,900)
        total.configure(bg='white')
        
        cb=f.cursor()
        cb.execute("SELECT * FROM BILLS1;")
        g=cb.fetchall()
        
        ln='----'*17
        t=bgp.count(1)
        k=bgp.count(-1)
        b=t-k
        temp=0
        if b>0:
            b=b-1
        if b<len(g):
            if b>-len(g):
                lbp1=tkinter.Label(total,text='DAN RESTAURANTS',font=('Arial bold',13),fg='black',bg='white').place(x=70,y=20)
                lbp2=tkinter.Label(total,text='7/6,Mahalingapuram main road,Nungambakkam',font=('Arial ',8),fg='black',bg='white').place(x=40,y=40)
                lbp3=tkinter.Label(total,text='Chennai 600-034',font=('Arial ',8),fg='black',bg='white',height=0).place(x=105,y=55)
                lbp4=tkinter.Label(total,text='Ph No. - 9003087815,28250390',font=('Arial ',10),fg='black',bg='white').place(x=55,y=75)
                lbp5=tkinter.Label(total,text='GSTIN : 6564354355W34U8',font=('Arial',10),fg='black',bg='white').place(x=60,y=95)
                lbp6=tkinter.Label(total,text='INVOICE DATE :',font=('Arial',10),fg='black',bg='white',height=0).place(x=10,y=125)
                lbp7=tkinter.Label(total,text=str(g[b][2])+g[b][-1],font=('Arial',10),fg='black',bg='white',height=0).place(x=196,y=125)
                lbp8=tkinter.Label(total,text='BILL NO. :',font=('Arial',10),fg='black',bg='white',height=0).place(x=10,y=145)
                lbp9=tkinter.Label(total,text=g[b][-2],font=('Arial',10),fg='black',bg='white',height=0).place(x=200,y=145)
                lbp10=tkinter.Label(total,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=165)
                lbp11=tkinter.Label(total,text='ITEM',font=('Arial',10),fg='black',bg='white',height=0).place(x=10,y=185)
                lbp12=tkinter.Label(total,text='QTY',font=('Arial',10),fg='black',bg='white',height=0).place(x=150,y=185)
                lbp13=tkinter.Label(total,text='RATE',font=('Arial',10),fg='black',bg='white',height=0).place(x=190,y=185)
                lbp14=tkinter.Label(total,text='TOTAL',font=('Arial',10),fg='black',bg='white',height=0).place(x=240,y=185)
                lbp15=tkinter.Label(total,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=205)
                plcy=225

                cb.execute(f"SELECT * FROM BILLS2 WHERE INVOICE_NO='{g[b][-2]}';")
                h=cb.fetchall()
                for i in range(0,len(h)):
                    lbp16=tkinter.Label(total,text=h[i][1],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=12,y=plcy)
                    lbp17=tkinter.Label(total,text=h[i][2],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=152,y=plcy)
                    lbp18=tkinter.Label(total,text=h[i][3],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=194,y=plcy)
                    lbp19=tkinter.Label(total,text=h[i][4],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=plcy)
                    plcy+=20
                    temp+=h[i][4]
                temp=temp+((temp*5)/100)
                lbp31=tkinter.Label(total,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=plcy)
                lbp32=tkinter.Label(total,text='TOTAL',font=('Arial',10),fg='black',bg='white',height=0).place(x=140,y=plcy+20)
                lbp33=tkinter.Label(total,text=temp,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=plcy+20)

#FUNCTION RESPONSIBLE FOR CALCULATING THE BILL TO BE DISPLAYED
def bdsp(a):
    try:
        if True==bool(total.winfo_exists()):
            total.withdraw()
        else:
            pass
    except NameError:
        pass    
    
    con,f=conn()
    cb=f.cursor()
    cb.execute("SELECT * FROM BILLS1;")
    g=cb.fetchall()
    bgp.append(a)
    t=bgp.count(1)
    k=bgp.count(-1)
    b=t-k
    if b>0:
        b=b-1
    if b<len(g) and b>-len(g):
        bdf()
    elif b>-len(g) and b<len(g):
        bdf()   
    else:
        bad1=Button(total1,text='GO TO FIRST',command=lambda:reset(),fg='#000C7B',bg='#FF8181',font=('Arial',11),width=11,height=1).place(x=260,y=10)

#FUNCTION RESPONSIBLE FOR SHOWING THE BILLS
def amtpaid():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    

    global total1
    total1=Toplevel(root)
    total1.title('Bills so far....')
    total1.geometry("650x80")
    total1.minsize(650,50)
    total1.maxsize(650,50)
    total1.configure(bg='#02FFBF')


    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(total1,image=nimg)
    illg.photo=nimg
    button= Button(total1,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=610,y=0)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(total1,image=nimg1)
    illg1.photo=nimg1
    button1= Button(total1,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)
    a,h=1,-1
    bap1=Button(total1,text='>',command=lambda:bdsp(a),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=1,width=9).place(x=460,y=10)
    bap2=Button(total1,text='<',command=lambda:bdsp(h),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=1,width=9).place(x=50,y=10)
    bad1=Button(total1,text='GO TO FIRST',command=lambda:reset(),fg='#000C7B',bg='#FF8181',font=('Arial',11),width=11,height=1).place(x=260,y=10)

#FUNCTION RESPONSIBLE FOR UPDATING THE REMOVED ADMIN
def remoadd():
    try:
        if True==bool(chb.winfo_exists()):
            chb.withdraw()
        else:
            pass
    except NameError:
        pass
    con,f=conn()
    if con==1:
        h=0
        a=stra.get()
        v='DAKSHIN'
        cb=f.cursor()
        cb.execute("select * from admin;")
        g=cb.fetchall()
        if v==a:
            h=2
        else:
            for i in range(0,len(g)):
                if a==g[i][0]:
                    h=1

        if h==0:
            rsm2=tkinter.messagebox.showwarning(Warning,' WRONG USERNAME')
        elif h==1:
            
            cb.execute(f"DELETE FROM ADMIN WHERE NAME='{a}';")
            f.commit()
            messagebox.showinfo("information","THE PERSON IS REMOVED")
            try:
                if True==bool(rema.winfo_exists()):
                    rema.withdraw()
                else:
                    pass
            except NameError:
                pass    
            adminmode()
            f.close()
        elif h==2:
            rsm=tkinter.messagebox.showwarning(Warning,' CANNOT REMOVE')

#FUNCTION RESPONSIBLE TO CHECK WHETHER THE PASSWORD IS RIGHT OR NOT
def chkp(ds):
    b=ds.get()
    con,f=conn()
    if con==1:
        cb=f.cursor()
        cb.execute("SELECT * FROM ADMIN;")
        g=cb.fetchall()
        h=0
        a='DAKSHIN'
        for i in range(0,len(g)):
            if a==g[i][0]:
                if b==g[i][1]:
                    h=1

        if h==0:
            rsm=tkinter.messagebox.showwarning(Warning,' WRONG PASSWORD')
            try:
                if True==bool(chb.winfo_exists()):
                    chb.withdraw()
                else:
                    pass
            except NameError:
                pass
            chka()
        elif h==1:
            remoadd()
            
        f.close()

#FUNCTION RESPONSIBLE FOR ENTERING THE MANAGER PASSWORD BEFORE REMOVING AN ADMIN
def chk():
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        global chb
        chb=Toplevel(root)
        chb.title('PASSWORD')
        chb.geometry("250x100")
        chb.minsize(250,100)
        chb.maxsize(250,100)
        chb.configure(bg='black')

        strw=tkinter.StringVar()

        erad2=tkinter.Entry(chb,textvariable=strw,fg='#3305ff',bg='#00ff2a',font=('Bahnschrift SemiLight',11)).place(x=80,y=10)
        lrad1=tkinter.Label(chb,text='Password',fg='white',bg='black',font=('Arial bold',11)).place(x=0,y=10)
        cp=partial(chkp,strw)
        brad1=tkinter.Button(chb,text='DELETE',fg='#000C7B',bg='#FF8181',font=('Arial',11),command=lambda:cp()).place(x=90,y=40)

#FUNCTION RESPONSIBLE FOR REMOVING AN ADMIN
def remadd():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    
    try:
        if True==bool(chb.winfo_exists()):
            chb.withdraw()
        else:
            pass
    except NameError:
        pass

    global rema
    rema=Toplevel(root)
    rema.title('REMOVE ADMIN')
    rema.geometry("600x300")
    rema.minsize(600,300)
    rema.maxsize(600,300)
    rema.configure(bg='#02FFBF')

    global stra
    stra=tkinter.StringVar()

    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(rema,image=nimg)
    illg.photo=nimg
    button= Button(rema,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=560,y=0)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(rema,image=nimg1)
    illg1.photo=nimg1
    button1= Button(rema,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)
    
    lad1=tkinter.Label(rema,text='WELCOME TO ADMIN REMOVAL MENU',fg='#0015ff',bg='#02FFBF',font=('Algerian',11)).place(x=150,y=10)
    erad2=tkinter.Entry(rema,textvariable=stra,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',11)).place(x=400,y=80)
    lrad1=tkinter.Label(rema,text='ENTER THE NAME OF THE ADMIN TO BE REMOVED',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=0,y=80)
    
    brad1=tkinter.Button(rema,text='DELETE',fg='#000C7B',bg='#FF8181',font=('Arial',11),command=lambda:chk()).place(x=280,y=150)

#FUNCTION FOR UPDATING THE REMOVED STAFF IN THE FILE
def remostf(stre):
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        con,f=conn()
        if con==1:
            cb=f.cursor()
            cb.execute("SELECT * FROM STAFF;")
            g=cb.fetchall()
            h=0
            a=stre.get()
            for i in range(0,len(g)):
                if a==g[i][0]:
                    h=1

            if h==0:
                rsm2=tkinter.messagebox.showwarning(Warning,' WRONG USERNAME')
            elif h==1:
                cb.execute(f"DELETE FROM STAFF WHERE NAME='{a}';")
                f.commit()
                messagebox.showinfo("information","THE PERSON IS REMOVED")  
                try:
                    if True==bool(rema.winfo_exists()):
                        rema.withdraw()
                    else:
                        pass
                except NameError:
                    pass    
                adminmode()
                f.close()

#FUNCTION RESPONSIBLE FOR REMOVING STAFF
def remstf():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    

    global rems
    rems=Toplevel(root)
    rems.title('REMOVE STAFF')
    rems.geometry("600x300")
    rems.minsize(600,300)
    rems.maxsize(600,300)
    rems.configure(bg='#02FFBF')

    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(rems,image=nimg)
    illg.photo=nimg
    button= Button(rems,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=560,y=0)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(rems,image=nimg1)
    illg1.photo=nimg1
    button1= Button(rems,image=nimg1,command=lambda:adminmode(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)

    stre=tkinter.StringVar()
    
    lrd1=tkinter.Label(rems,text='WELCOME TO STAFF REMOVAL MENU',fg='#0015ff',bg='#02FFBF',font=('algerian',11)).place(x=150,y=10)
    erd2=tkinter.Entry(rems,textvariable=stre,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',10)).place(x=400,y=80)
    lad1=tkinter.Label(rems,text='ENTER THE NAME OF THE STAFF TO BE REMOVED',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',10)).place(x=20,y=80)
    rs=partial(remostf,stre)
    brd1=tkinter.Button(rems,text='DELETE',fg='#000C7B',bg='#FF8181',font=('Arial',11),command=lambda:rs()).place(x=300,y=150)

#FUNCTION RESPONSIBLE FOR SAVING THE REPLACED MENU
def repmenu(rmn1,rmn2,rmn3):
    a,b,c=rmn1.get(),rmn2.get(),rmn3.get()
    a=a.upper()
    b=b.upper()
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        con,f=conn()
        if con==1:
            cb=f.cursor()
            cb.execute("SELECT * FROM MENU;")
            g=cb.fetchall()
            h,w,o=0,0,0
            for i in range(0,len(g)):
                if a==g[i][0]:
                    h=1

            if b=='':
                w=1
            if a=='':
                o=1

            if w==1 and o==0 or w==1 and o==1:
                wcps=tkinter.messagebox.showwarning(Warning,'ITEM NOT ENTERED')
            if h==0 and w==0 and o==0:
                rsm2=tkinter.messagebox.showwarning(Warning,' INVALID ITEM NAME')
            elif h==1 and w==0 and o==0:
                cb.execute(f"DELETE FROM MENU WHERE NAME='{a}';")
                f.commit()
                cb.execute(f"INSERT INTO MENU VALUES('{b}',{c});")
                f.commit()
                messagebox.showinfo("information","THE ITEM IS REPLACED")
                chngemenu()

#FUNCTION RESPONSIBLE FOR REPLACING A PARTICULAR ITEM
def chme():
    try:
        if True==bool(men.winfo_exists()):
            men.withdraw()
        else:
            pass
    except NameError:
        pass    

    global amn
    amn=Toplevel(root)
    amn.title('ITEM REPLACING MENU')
    amn.geometry("550x400")
    amn.minsize(550,400)
    amn.maxsize(550,400)
    amn.configure(bg='#02FFBF')


    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(amn,image=nimg)
    illg.photo=nimg
    button= Button(amn,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=510,y=2)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(amn,image=nimg1)
    illg1.photo=nimg1
    button1= Button(amn,image=nimg1,command=lambda:chngemenu(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=2)

    rmn1,rmn2,rmn3=tkinter.StringVar(),tkinter.StringVar(),tkinter.IntVar()
    lrm1=tkinter.Label(amn,text='WELCOME TO ITEM REPLACING MENU',fg='#0015ff',bg='#02FFBF',font=('Algerian',18)).place(x=35,y=9)


    erm1=tkinter.Entry(amn,textvariable=rmn1,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',11)).place(x=270,y=80)
    lrm2=tkinter.Label(amn,text='ENTER THE ITEM TO BE REMOVED',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=9,y=80)
    erm2=tkinter.Entry(amn,textvariable=rmn2,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',11)).place(x=270,y=120)
    lrm3=tkinter.Label(amn,text='ENTER THE ITEM TO BE REPLACED AS',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=9,y=120)
    erm3=tkinter.Entry(amn,textvariable=rmn3,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',11)).place(x=270,y=160)
    lrm4=tkinter.Label(amn,text='ENTER THE PRICE OF THE ITEM',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=9,y=160)

    repmen=partial(repmenu,rmn1,rmn2,rmn3)

    brm1=tkinter.Button(amn,text='CREATE',fg='#000C7B',bg='#FF8181',relief='groove',command=lambda:repmen(),font=('Arial',11)).place(x=220,y=205)

#FUNCTION RESPONSIBLE FOR SAVING THE REMOVED ITEM
def rmenu(rmn1):
    a=rmn1.get()
    a=a.upper()
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        con,f=conn()
        if con==1:
            cb=f.cursor()
            cb.execute("SELECT * FROM MENU;")
            g=cb.fetchall()
            h=0
            for i in range(0,len(g)):
                if a==g[i][0]:
                    h=1

            if h==0:
                rsm2=tkinter.messagebox.showwarning(Warning,' INVALID ITEM NAME')
            elif h==1:
                messagebox.showinfo("information","THE ITEM IS REMOVED")  
                cb.execute(f"DELETE FROM MENU WHERE NAME='{a}'")
                f.commit()
                try:
                    if True==bool(mnre.winfo_exists()):
                        mnre.withdraw()
                    else:
                        pass
                except NameError:
                    pass   
                f.close() 
                chngemenu()

#FUNCTION RESPONSIBLE FOR REMOVING A PARTICULAR ITEM
def chmer():
    try:
        if True==bool(men.winfo_exists()):
            men.withdraw()
        else:
            pass
    except NameError:
        pass    

    global mnre
    mnre=Toplevel(root)
    mnre.title('ITEM REMOVING MENU')
    mnre.geometry("550x200")
    mnre.minsize(550,200)
    mnre.maxsize(550,200)
    mnre.configure(bg='#02FFBF')


    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(mnre,image=nimg)
    illg.photo=nimg
    button= Button(mnre,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=510,y=2)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(mnre,image=nimg1)
    illg1.photo=nimg1
    button1= Button(mnre,image=nimg1,command=lambda:chngemenu(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=2)

    rmn1=tkinter.StringVar()
    lrm1=tkinter.Label(mnre,text='WELCOME TO ITEM REMOVING MENU',fg='#0015ff',bg='#02FFBF',font=('Algerian',18)).place(x=55,y=9)


    erm1=tkinter.Entry(mnre,textvariable=rmn1,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',11)).place(x=270,y=80)
    lrm2=tkinter.Label(mnre,text='ENTER THE ITEM TO BE REMOVED',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=9,y=80)

    remen=partial(rmenu,rmn1)

    brm1=tkinter.Button(mnre,text='REMOVE',fg='#000C7B',bg='#FF8181',relief='groove',command=lambda:remen(),font=('Arial',11)).place(x=220,y=155)

#FUNCTION RESPONSIBLE FOR SAVING THE ADDED ITEM
def admenu(rmn2,rmn3):
    b,c=rmn2.get(),rmn3.get()
    b=b.upper()
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        con,f=conn()
        if con==1:
            cb=f.cursor()
            cb.execute("SELECT * FROM MENU;")
            g=cb.fetchall()
            h=0
            for i in range(0,len(g)):
                if b==g[i][0]:
                    h=1
            if b=='':
                h=2
            if h==1:
                rsm2=tkinter.messagebox.showwarning(Warning,'EXIST ALREADY')
            elif h==0:
                messagebox.showinfo("information","THE ITEM HAS BEEN ADDED")  
                cb.execute(f"INSERT INTO MENU VALUES('{b}',{c});")
                f.commit()
                try:
                    if True==bool(rema.winfo_exists()):
                        rema.withdraw()
                    else:
                        pass
                except NameError:
                    pass   
                f.close() 
                chngemenu()
            elif h==2:
                rs=tkinter.messagebox.showwarning(Warning,'NO VALUE ENTERED')

#FUNCTION RESPONSIBLE FOR ADDING AN ITEM
def chmea():
    try:
        if True==bool(men.winfo_exists()):
            men.withdraw()
        else:
            pass
    except NameError:
        pass    

    global mna
    mna=Toplevel(root)
    mna.title('ITEM ADDING MENU')
    mna.geometry("550x400")
    mna.minsize(550,400)
    mna.maxsize(550,400)
    mna.configure(bg='#02FFBF')

    con,f=conn()
    cb=f.cursor()
    cb.execute("SELECT COUNT(NAME) FROM MENU;")
    b=cb.fetchall()
    b=32-b[0][0]


    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(mna,image=nimg)
    illg.photo=nimg
    button= Button(mna,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=510,y=2)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(mna,image=nimg1)
    illg1.photo=nimg1
    button1= Button(mna,image=nimg1,command=lambda:chngemenu(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=2)

    rmn2,rmn3=tkinter.StringVar(),tkinter.IntVar()
    lrm1=tkinter.Label(mna,text='WELCOME TO ITEM ADDING MENU',fg='#0015ff',bg='#02FFBF',font=('Algerian',18)).place(x=55,y=9)
    lrm5=tkinter.Label(mna,text='NOTE:-ITEM CAN BE ADDED ONLY    MORE TIME(S)',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',10)).place(x=105,y=355)
    lrm6=tkinter.Label(mna,text=b,fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED JPAN',10)).place(x=289,y=355)



    erm2=tkinter.Entry(mna,textvariable=rmn2,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',11)).place(x=270,y=120)
    lrm3=tkinter.Label(mna,text='ENTER THE ITEM TO BE ADDED',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=9,y=120)
    erm3=tkinter.Entry(mna,textvariable=rmn3,fg='#CE0241',bg='#CDD6DC',font=('Bahnschrift SemiLight',11)).place(x=270,y=160)
    lrm4=tkinter.Label(mna,text='ENTER THE PRICE OF THE ITEM',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=9,y=160)

    admen=partial(admenu,rmn2,rmn3)

    brm1=tkinter.Button(mna,text='CREATE',fg='#000C7B',bg='#FF8181',relief='groove',command=lambda:admen(),font=('Arial',11)).place(x=220,y=205)

#FUNCTION RESPONSIBLE FOR SAVING THE ENTIRE MENU
def nmen():
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        con,f=conn()
        if con==1:
            cb=f.cursor()
            h,c=0,0
            a=[pnf1.get(),pnf2.get(),pnf3.get(),pnf4.get(),pnf5.get(),pnf6.get(),pnf7.get(),pnf8.get(),pnf9.get(),pnf10.get(),pnf11.get(),pnf12.get(),pnf13.get(),pnf14.get(),pnf15.get(),pnf16.get(),pnf17.get(),pnf18.get(),pnf19.get(),pnf20.get(),pnf21.get(),pnf22.get(),pnf23.get(),pnf24.get()]
            b=[mnn1.get(),mnn2.get(),mnn3.get(),mnn4.get(),mnn5.get(),mnn6.get(),mnn7.get(),mnn8.get(),mnn9.get(),mnn10.get(),mnn11.get(),mnn12.get(),mnn13.get(),mnn14.get(),mnn15.get(),mnn16.get(),mnn17.get(),mnn18.get(),mnn19.get(),mnn20.get(),mnn21.get(),mnn22.get(),mnn23.get(),mnn24.get()]
            for i in a:
                if i=='':
                    h=1
            for i in b:
                if i=='':
                    c=1
            if h==1:
                wstf=tkinter.messagebox.showwarning(Warning,'ALL MENU DETAILS ARE NOT ENTERED')
            if c==1:
                wstf=tkinter.messagebox.showwarning(Warning,'PRICE FOR ALL ITEMS ARE NOT ENTERED')
            if h==0 and c==0:
                cb.execute("DELETE FROM MENU;")
                f.commit()
                for i in range(0,len(b)):
                    b[i]=b[i].upper()
                    cb.execute(f"INSERT INTO MENU VALUES('{b[i][0:25]}',{a[i]});")
                    f.commit()
                messagebox.showinfo("information","THE ITEMS HAVE BEEN CHANGED")
                try:
                    if True==bool(mnf.winfo_exists()):
                        mnf.withdraw()
                    else:
                        pass
                except NameError:
                        pass     
                adminmode()

#FUNCTION RESPONSIBLE FOR CHANGING THE ENTIRE MENU
def  chmef():
    try:
        if True==bool(men.winfo_exists()):
            men.withdraw()
        else:
            pass
    except NameError:
        pass    

    global mnf
    mnf=Toplevel(root)
    mnf.title('CHANGING MENU')
    mnf.geometry("600x850")
    mnf.minsize(600,850)
    mnf.maxsize(600,850)
    mnf.configure(bg='#02FFBF')


    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(mnf,image=nimg)
    illg.photo=nimg
    button= Button(mnf,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=560,y=2)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(mnf,image=nimg1)
    illg1.photo=nimg1
    button1= Button(mnf,image=nimg1,command=lambda:chngemenu(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=2)

    
    global pnf1,pnf2,pnf3,pnf4,pnf5,pnf6,pnf7,pnf8,pnf9,pnf10,pnf11,pnf12,pnf13,pnf14,pnf15,pnf16,pnf17,pnf18,pnf19,pnf20,pnf21,pnf22,pnf23,pnf24,mnn1,mnn2,mnn3,mnn4,mnn5,mnn6,mnn7,mnn8,mnn9,mnn10,mnn11,mnn12,mnn13,mnn14,mnn15,mnn16,mnn17,mnn18,mnn19,mnn20,mnn21,mnn22,mnn23,mnn24

    pnf1,pnf2,pnf3,pnf4,pnf5,pnf6,pnf7,pnf8,pnf9,pnf10,pnf11,pnf12,pnf13,pnf14,pnf15,pnf16,pnf17,pnf18,pnf19,pnf20,pnf21,pnf22,pnf23,pnf24=tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar(),tkinter.IntVar()
    mnn1,mnn2,mnn3,mnn4,mnn5,mnn6,mnn7,mnn8,mnn9,mnn10,mnn11,mnn12,mnn13,mnn14,mnn15,mnn16,mnn17,mnn18,mnn19,mnn20,mnn21,mnn22,mnn23,mnn24=tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar(),tkinter.StringVar()
    et=[mnn1,mnn2,mnn3,mnn4,mnn5,mnn6,mnn7,mnn8,mnn9,mnn10,mnn11,mnn12,mnn13,mnn14,mnn15,mnn16,mnn17,mnn18,mnn19,mnn20,mnn21,mnn22,mnn23,mnn24,pnf1,pnf2,pnf3,pnf4,pnf5,pnf6,pnf7,pnf8,pnf9,pnf10,pnf11,pnf12,pnf13,pnf14,pnf15,pnf16,pnf17,pnf18,pnf19,pnf20,pnf21,pnf22,pnf23,pnf24]

    lfm1=tkinter.Label(mnf,text='WELCOME TO MENU CHANGE WINDOW',fg='#0015ff',bg='#02FFBF',font=('Algerian',16)).place(x=110,y=10)

    lfm2=tkinter.Label(mnf,text='ITEM',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=90,y=41)
    lfm3=tkinter.Label(mnf,text='PRICE',fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=320,y=41)
    xc,yc,c=40,70,0
    for i in range(0,48):
        efm1=tkinter.Entry(mnf,textvariable=et[i],fg='#CE0241',bg='#CDD6DC',font=('Arial',11)).place(x=xc,y=yc)
        c+=1
        yc+=30
        if c==24:
            yc=70
            xc=270
    
    bfm1=tkinter.Button(mnf,text='CREATE',fg='#000C7B',bg='#FF8181',relief='groove',command=lambda:nmen(),font=('Arial',11)).place(x=500,y=365)

#FUNCTION REPONSIBLE FOR SAVING THE PRICE
def prc(cps1,cps2):
    a,b=cps1.get(),cps2.get()
    a=a.upper()  
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        con,f=conn()
        if con==1:
            cb=f.cursor()
            cb.execute("SELECT * FROM MENU;")
            g=cb.fetchall()
            h,w,o=0,0,0
            for i in range(0,len(g)):
                if a == g[i][0]:
                    h=1

            if a=='':
                o=1

            if b==0 and o==0 and h==1:
                r=messagebox.askyesno("CONFIRM","ARE YOU SURE YOU WANT TO CONTINUE WITH 0 ?") 
                if r==True:
                    w=0
                else:
                    w=1
                    

            if o==1:
                wcps=tkinter.messagebox.showwarning(Warning,'ITEM NOT ENTERED')
            if h==0 and w==0 and o==0:
                rsm2=tkinter.messagebox.showwarning(Warning,' INVALID ITEM NAME')
            if h==1 and w==0 and o==0:
                try:
                    if True==bool(pri.winfo_exists()):
                        pri.withdraw()
                    else:
                        pass
                except NameError:
                    pass       
                cb.execute(f"UPDATE MENU SET PRICE={b} WHERE NAME='{a}' ;")
                f.commit()
                messagebox.showinfo("information","THE PRICE HAS BEEN CHANGED")
                f.close()
                adminmode()

#FUNCTION RESPONSIBLE FOR CHANGING THE PRICE
def price():
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    
    try:
        if True==bool(men.winfo_exists()):
            men.withdraw()
        else:
            pass
    except NameError:
        pass    

    global pri
    pri=Toplevel(root)
    pri.title('PRICE CHANGE')
    pri.geometry("500x300")
    pri.minsize(500,300)
    pri.maxsize(500,300)
    pri.configure(bg='#02FFBF')

    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(pri,image=nimg)
    illg.photo=nimg
    button= Button(pri,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=460,y=0)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(pri,image=nimg1)
    illg1.photo=nimg1
    button1= Button(pri,image=nimg1,command=lambda:chngemenu(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=0)

    lcpass1=tkinter.Label(pri,text='WELCOME TO PRICE CHANGE MENU',fg='#0015ff',bg='#02FFBF',font=('ALGERIAN',14)).place(x=50,y=0)
    lcpass2=tkinter.Label(pri,text="Enter the Item Name",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=25,y=100)

    lcpass3=tkinter.Label(pri,text="Enter the Price",fg='#0015ff',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=25,y=140)

    cps1,cps2=tkinter.StringVar(),tkinter.IntVar()

    ecpass1=tkinter.Entry(pri,textvariable=cps1,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).place(x=190,y=100)
    ecpass2=tkinter.Entry(pri,textvariable=cps2,bg='#CDD6DC',fg='#CE0241',font=('Bahnschrift SemiLight',9)).place(x=190,y=140)

    prca=partial(prc,cps1,cps2)
    bcpass1=tkinter.Button(pri,text='CHANGE',command=lambda:prca(),fg='#000C7B',bg='#FF8181',font=('Arial',11)).place(x=200,y=200)

#FUNCTION RESPONSIBLE FOR VIEWING THE ENTIRE MENU
def  view():
    try:
        if True==bool(men.winfo_exists()):
            men.withdraw()
        else:
            pass
    except NameError:
        pass    
    
    con,f=conn()
    if con==1:
    
        global vw
        vw=Toplevel(root)
        vw.title('CURRENT MENU')
        vw.geometry("600x300")
        vw.minsize(600,300)
        vw.maxsize(600,300)
        vw.configure(bg='#02FFBF')
        cb=f.cursor()
        cb.execute("SELECT * FROM MENU;")
        g=cb.fetchall()
        cb.execute("SELECT COUNT(NAME) FROM MENU;")
        b=cb.fetchall()
        b=b[0][0]

        if b<25:
            img= Image.open("logof.png")
            rimg= img.resize((30,25))
            nimg= ImageTk.PhotoImage(rimg)
            illg= Label(vw,image=nimg)
            illg.photo=nimg
            button= Button(vw,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=560,y=2)

        img1= Image.open("back.png")
        rimg1= img1.resize((30,25))
        nimg1= ImageTk.PhotoImage(rimg1)
        illg1= Label(vw,image=nimg1)
        illg1.photo=nimg1
        button1= Button(vw,image=nimg1,command=lambda:chngemenu(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=0,y=2)



        lfm1=tkinter.Label(vw,text='MENU',fg='#0015ff',bg='#02FFBF',font=('Algerian',16)).place(x=110,y=10)

        xc,yc,c=40,70,0
        for i in range(0,b):
            efm1=tkinter.Label(vw,text=g[i][0],fg='#CE0241',bg='#02FFBF',font=('HP SIMPLIFIED HANS',11)).place(x=xc,y=yc)
            c+=1
            yc+=20
            if c%8==0:
                yc=70
                xc+=200
        if b>24:
            vw.minsize(800,300)
            vw.maxsize(800,300)
            img= Image.open("logof.png")
            rimg= img.resize((30,25))
            nimg= ImageTk.PhotoImage(rimg)
            illg= Label(vw,image=nimg)
            illg.photo=nimg
            button= Button(vw,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='#02FFBF').place(x=760,y=2)

#FUNCTION RESPONSIBLE FOR CHANGING MENU WINDOW
def chngemenu():
    try:
        if True==bool(vw.winfo_exists()):
            vw.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(mnre.winfo_exists()):
            mnre.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(mna.winfo_exists()):
            mna.withdraw()
        else:
            pass
    except NameError:
        pass   
    try:
        if True==bool(amn.winfo_exists()):
            amn.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(adm.winfo_exists()):
            adm.withdraw()
        else:
            pass
    except NameError:
        pass    
    try:
        if True==bool(mnf.winfo_exists()):
            mnf.withdraw()
        else:
            pass
    except NameError:
        pass    
    try:
        if True==bool(pri.winfo_exists()):
            pri.withdraw()
        else:
            pass
    except NameError:
        pass  
    con,f=conn()
    if con==1:  
        global men
        men=Toplevel(root)
        men.title('MENU DETAILS')
        men.geometry("650x310")
        men.minsize(650,310)
        men.maxsize(650,310)
        
        img2= Image.open("adminpg.jpg")
        rimg2= img2.resize((650,310))
        nimg2= ImageTk.PhotoImage(rimg2)
        illg2= Label(men,image=nimg2)
        illg2.photo=nimg2
        illg2.place(x=0,y=0)
        bgimg=tkinter.Label(men,image=nimg2).place(x=0,y=0)

        img= Image.open("logof.png")
        rimg= img.resize((30,25))
        nimg= ImageTk.PhotoImage(rimg)
        illg= Label(men,image=nimg)
        illg.photo=nimg
        button= Button(men,image=nimg,command=lambda:lgp(),bg='black',relief='flat',activebackground='black').place(x=610,y=2)

        img1= Image.open("back.png")
        rimg1= img1.resize((30,25))
        nimg1= ImageTk.PhotoImage(rimg1)
        illg1= Label(men,image=nimg1)
        illg1.photo=nimg1
        button1= Button(men,image=nimg1,command=lambda:adminmode(),bg='black',relief='flat',activebackground='black').place(x=0,y=2)

        lmn1=tkinter.Label( men,text='CHOOSE ONE OF THE BELOW',fg='#0015ff',bg='#02FFBF',font=('Arial bold',18)).place(x=50,y=30)

        cb=f.cursor()
        cb.execute("SELECT COUNT(NAME) FROM MENU;")
        b=cb.fetchall()
        if b[0][0]>32:
            bmn6=tkinter.Button(men,text='Change the price',command=lambda:price(),state='disabled',relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=450,y=140)

        else:
            bmn6=tkinter.Button(men,text='Change the price',command=lambda:price(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=450,y=140)
        bmn1=tkinter.Button(men,text='Change the menu',command=lambda:chmef(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=250,y=190)
        bmn2=tkinter.Button(men,text='Replace an item',command=lambda:chme(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=250,y=90)
        bmn3=tkinter.Button(men,text='Add an item',command=lambda:chmea(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=50,y=90)
        bmn4=tkinter.Button(men,text='Remove an item',command=lambda:chmer(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=50,y=190)
        bmn5=tkinter.Button(men,text='Click here to view the menu',command=lambda:view(),fg='#FF8181',bg='BLACK',font=('Arial',14),height=1).place(x=173,y=282)

#FUNCTION RESPONSIBLE FOR DISPLAYING THE ADMINMODE WINDOW
def adminmode():
    try:
        if True==bool(pri.winfo_exists()):
            pri.withdraw()
        else:
            pass
    except NameError:
        pass   
    try:
        if True==bool(vw.winfo_exists()):
            vw.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(amn.winfo_exists()):
            amn.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(cha.winfo_exists()):
            cha.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(mna.winfo_exists()):
            mna.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(mnre.winfo_exists()):
            mnre.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(men.winfo_exists()):
            men.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(mnf.winfo_exists()):
            mnf.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(rems.winfo_exists()):
            rems.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(rema.winfo_exists()):
            rema.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(total.winfo_exists()):
            total.withdraw()
        else:
            pass
    except NameError:
        pass

    try:
        if True==bool(chpas.winfo_exists()):
            chpas.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(disadmin.winfo_exists()):
            disadmin.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(disstaff.winfo_exists()):
            disstaff.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(addmin.winfo_exists()):
            addmin.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(chb.winfo_exists()):
            chb.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(stf.winfo_exists()):
            stf.withdraw()
        else:
            pass
    except NameError:
        pass

    try:
        if True==bool(total1.winfo_exists()):
            total1.withdraw()
        else:
            pass
    except NameError:
        pass

    
    global adm
    adm=Toplevel(root)
    adm.title('ADMIN MODE')
    adm.geometry("600x600")
    adm.minsize(600,600)
    adm.maxsize(600,600)
    adm.configure(bg='tan')

    
    img2= Image.open("adminpg.jpg")
    rimg2= img2.resize((600,600))
    nimg2= ImageTk.PhotoImage(rimg2)
    illg2= Label(adm,image=nimg2)
    illg2.photo=nimg2
    illg2.place(x=0,y=0)
    bgimg=tkinter.Label(adm,image=nimg2).place(x=0,y=0)

    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    illg= Label(adm,image=nimg)
    illg.photo=nimg
    button= Button(adm,image=nimg,command=lambda:lgp(),bg='black',relief='flat',activebackground='black').place(x=560,y=2)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(adm,image=nimg1)
    illg1.photo=nimg1
    button1= Button(adm,image=nimg1,command=lambda:lgp(),bg='black',relief='flat',activebackground='black',state='disabled').place(x=0,y=2)

    lad1=tkinter.Label(adm,text='WELCOME TO ADMIN MODE',fg='#0015ff',bg='#02FFBF',font=('Arial bold',18)).place(x=120,y=30)
    
    bad1=tkinter.Button(adm,text='Add a Staff',command=lambda:addstaff(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=11).place(x=50,y=185)
    bad2=tkinter.Button(adm,text='Add an Admin',command=lambda:addadmin(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=11).place(x=50,y=90)
    bad3=tkinter.Button(adm,text='Display all the Bills ',command=lambda:amtpaid(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=350,y=375)
    bad4=tkinter.Button(adm,text='Change Menu Details',command=lambda:chngemenu(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=18 ).place(x=50,y=375)
    bad6=tkinter.Button(adm,text='Change Password',command=lambda:changepass(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=14).place(x=50,y=470)
    bad7=tkinter.Button(adm,text='Display all Staff Members',command=lambda:displaystaff(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=20).place(x=350,y=280)
    bad8=tkinter.Button(adm,text='Display the other Admins',command=lambda:displayadmin(),relief='groove',fg='#000C7B',bg='#FF8181',font=('Arial',14),height=2,width=20).place(x=50,y=280)
    bad9=tkinter.Button(adm,text='Remove a Staff',fg='#000C7B',bg='#FF8181',relief='groove',command=lambda:remstf(),font=('Arial',14),height=2,width=14).place(x=350,y=185)
    bad10=tkinter.Button(adm,text='Remove an Admin',fg='#000C7B',bg='#FF8181',relief='groove',command=lambda:remadd(),font=('Arial',14),height=2,width=14).place(x=350,y=90)

#FUNCTION RESPONSIBLE FOR SAVING THE BILL IN A FILE
def pblp():
    dt=datetime.now()
    d=messagebox.askyesno("CONFIRM","ARE YOU SURE ?") 
    if d==True:
        dt=datetime.now()
        con,f=conn()
        if con==1:
            cb=f.cursor()
            p=dt.time()
            l=dt.date()
            p=p.strftime("%H:%M")
            cb.execute("SELECT * FROM BILLS1;")
            g=cb.fetchall()
            bn=len(g)+1
            cb.execute(f"INSERT INTO BILLS1 VALUES({bn},{tablenumber},'{l}','{inv}','{p}');")
            f.commit()
            for i in smp:
                cb.execute(f"INSERT INTO BILLS2 VALUES('{inv}','{i[1]}',{i[2]},{i[3]},{i[4]});")
                f.commit()
            try:
                if True==bool(blp.winfo_exists()):
                    blp.withdraw()
                else:
                    pass
            except NameError:
                pass
            try:
                if True==bool(ords.winfo_exists()):
                    ords.withdraw()
                else:
                    pass
            except NameError:
                pass
            smp.clear()
            tabledisp()

#FUNCTION RESPONSIBLE FOR DISPLAYING BILLS
def billprint(a):
    global blp
    blp=Toplevel(root)
    blp.title('BILL')
    blp.geometry("300x900")
    blp.minsize(300,900)
    blp.maxsize(300,900)
    blp.configure(bg='white')
    
    dt=datetime.now()
    ln='----'*17
    global inv
    con,f=conn()
    cb=f.cursor()
    cb.execute("SELECT * FROM BILLS1;")
    g=cb.fetchall()
    inv=str(tablenumber)+str(mng[0][0:2])+str(dt.year)+str(mng[1][0])+str(len(g)+1)
    temp=0
    
    lbp1=tkinter.Label(blp,text='DAN RESTAURANTS',font=('Arial bold',13),fg='black',bg='white').place(x=70,y=20)
    lbp2=tkinter.Label(blp,text='7/6,Mahalingapuram main road,Nungambakkam',font=('Arial ',8),fg='black',bg='white').place(x=40,y=40)
    lbp3=tkinter.Label(blp,text='Chennai 600-034',font=('Arial ',8),fg='black',bg='white',height=0).place(x=105,y=55)
    lbp4=tkinter.Label(blp,text='Ph No. - 9003087815,28250390',font=('Arial ',10),fg='black',bg='white').place(x=55,y=75)
    lbp5=tkinter.Label(blp,text='GSTIN : 6564354355W34U8',font=('Arial',10),fg='black',bg='white').place(x=60,y=95)
    lbp6=tkinter.Label(blp,text='INVOICE DATE :',font=('Arial',10),fg='black',bg='white',height=0).place(x=10,y=125)
    lbp7=tkinter.Label(blp,text=dt,font=('Arial',10),fg='black',bg='white',height=0).place(x=196,y=125)
    lbp8=tkinter.Label(blp,text='BILL NO. :',font=('Arial',10),fg='black',bg='white',height=0).place(x=10,y=145)
    lbp9=tkinter.Label(blp,text=inv,font=('Arial',10),fg='black',bg='white',height=0).place(x=200,y=145)
    lbp10=tkinter.Label(blp,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=165)
    lbp11=tkinter.Label(blp,text='ITEM',font=('Arial',10),fg='black',bg='white',height=0).place(x=10,y=185)
    lbp12=tkinter.Label(blp,text='QTY',font=('Arial',10),fg='black',bg='white',height=0).place(x=150,y=185)
    lbp13=tkinter.Label(blp,text='RATE',font=('Arial',10),fg='black',bg='white',height=0).place(x=190,y=185)
    lbp14=tkinter.Label(blp,text='TOTAL',font=('Arial',10),fg='black',bg='white',height=0).place(x=240,y=185)
    lbp15=tkinter.Label(blp,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=205)
    plcy=225
    c=0
    if a==1:
        lbp36=tkinter.Label(blp,text='NO ITEM ORDERD',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=70,y=255)

    else:
        
        for i in orderprint:   
            lbp16=tkinter.Label(blp,text=i[1],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=12,y=plcy)
            lbp17=tkinter.Label(blp,text=i[2],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=152,y=plcy)
            lbp18=tkinter.Label(blp,text=i[3],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=194,y=plcy)
            lbp19=tkinter.Label(blp,text=i[4],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=plcy)
            plcy+=20
            c+=1

        if c<14:
            lbp31=tkinter.Label(blp,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=plcy+100)
            lbp34=tkinter.Label(blp,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=plcy+140)
            lbp35=tkinter.Label(blp,text='CASHIER:-',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=95,y=plcy+180)
            lbp37=tkinter.Label(blp,text=mng[0],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=165,y=plcy+180)
            lbp38=tkinter.Label(blp,text='THANK YOU PLEASE VISIT AGAIN',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=45,y=plcy+240)
            lbp39=tkinter.Label(blp,text='HAVE A NICE DAY',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=80,y=plcy+260)

            bbp1=tkinter.Button(blp,text='SAVE',font=('Arial',10),bg='white',fg='black',command=lambda:pblp()).place(x=120,y=plcy+280)
            for i in orderprint:
                temp+=i[-1]            
            lbp23=tkinter.Label(blp,text='TABLE NO.',font=('Arial',10),fg='black',bg='white',height=0).place(x=100,y=plcy+160)
            lbp24=tkinter.Label(blp,text=orderprint[0][0],font=('Arial',10),fg='black',bg='white',height=0).place(x=180,y=plcy+160)
            lbp21=tkinter.Label(blp,text=' SUB TOTAL',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=140,y=plcy)
            temp1=(temp*2.5)/100
            lbp22=tkinter.Label(blp,text=temp,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=plcy)
            lbp22=tkinter.Label(blp,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=plcy+20)
            lbp25=tkinter.Label(blp,text='CGST @2.5%',font=('Arial ',10),fg='black',bg='white',height=0).place(x=140,y=plcy+40)
            lbp26=tkinter.Label(blp,text='SGST @ 2.5%',font=('Arial',10),fg='black',bg='white',height=0).place(x=140,y=plcy+60)
            lbp27=tkinter.Label(blp,text=temp1,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=240,y=plcy+40)
            lbp28=tkinter.Label(blp,text=temp1,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=240,y=plcy+60)
            lbp29=tkinter.Label(blp,text=' NET TOTAL',font=('Arial',10),fg='black',bg='white',height=0).place(x=140,y=plcy+80)
            lbp30=tkinter.Label(blp,text=round((temp1+temp+temp1),2),font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=plcy+80)
            temp2=round((temp1+temp+temp1),0)
            lbp32=tkinter.Label(blp,text='TOTAL',font=('Arial',10),fg='black',bg='white',height=0).place(x=140,y=plcy+120)
            lbp33=tkinter.Label(blp,text=temp2,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=plcy+120)
        else:
            global blp2
            blp2=Toplevel(root)
            blp2.title('BILL')
            blp2.geometry("300x500")
            blp2.minsize(300,500)
            blp2.maxsize(300,500)
            blp2.configure(bg='white')
            lbp23=tkinter.Label(blp2,text='TABLE NO.',font=('Arial',10),fg='black',bg='white',height=0).place(x=100,y=190)
            lbp24=tkinter.Label(blp2,text=orderprint[0][0],font=('Arial',10),fg='black',bg='white',height=0).place(x=180,y=190)
            for i in orderprint:
                temp+=i[-1]
            lbp21=tkinter.Label(blp2,text=' SUB TOTAL',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=140,y=30)
            lbp22=tkinter.Label(blp2,text=temp,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=30)
            lbp22=tkinter.Label(blp2,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=50)
            lbp25=tkinter.Label(blp2,text='CGST @2.5%',font=('Arial ',10),fg='black',bg='white',height=0).place(x=140,y=70)
            lbp26=tkinter.Label(blp2,text='SGST @ 2.5%',font=('Arial',10),fg='black',bg='white',height=0).place(x=140,y=90)
            temp1=(temp*2.5)/100
            lbp27=tkinter.Label(blp2,text=temp1,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=240,y=70)
            lbp28=tkinter.Label(blp2,text=temp1,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=240,y=90)
            lbp29=tkinter.Label(blp2,text=' NET TOTAL',font=('Arial',10),fg='black',bg='white',height=0).place(x=140,y=110)
            lbp30=tkinter.Label(blp2,text=round((temp1+temp+temp1),2),font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=110)

            lbp31=tkinter.Label(blp2,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=130)
            lbp34=tkinter.Label(blp2,text=ln,font=('Arial',10),fg='black',bg='white',height=0).place(x=9,y=170)
            lbp35=tkinter.Label(blp2,text='CASHIER:-',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=95,y=210)
            lbp37=tkinter.Label(blp2,text=mng[0],font=('Arial bold',10),fg='black',bg='white',height=0).place(x=165,y=210)
            lbp38=tkinter.Label(blp2,text='THANK YOU PLEASE VISIT AGAIN',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=45,y=230)
            lbp39=tkinter.Label(blp2,text='HAVE A NICE DAY',font=('Arial bold',10),fg='black',bg='white',height=0).place(x=80,y=250)
            temp2=round((temp1+temp+temp1),0)
            lbp32=tkinter.Label(blp2,text='TOTAL',font=('Arial',10),fg='black',bg='white',height=0).place(x=140,y=150)
            lbp33=tkinter.Label(blp2,text=temp2,font=('Arial bold',10),fg='black',bg='white',height=0).place(x=242,y=150)
            
            
            bbp1=tkinter.Button(blp2,text='SAVE',font=('Arial',10),bg='white',fg='black',command=lambda:pblp()).place(x=120,y=270)
    for i in orderprint:
        smp.append(i)
    orderprint.clear()

#FUNCTION SAVES THE DETAILS OF THE ORDERED ITEMS
def bill():
    con,f=conn()
    if con==1:
        cb=f.cursor()
        cb.execute("SELECT * FROM MENU;")
        g=cb.fetchall()
        for i in range(0,len(g)):
            itn.append(g[i][0])
            pr.append(g[i][1])
        q=[ao,bo,co,do,eo,fo,go,ho,io,jo,ko,lo,mo,no,po,qo,ro,so,to,uo,vo,wo,xo,yo,zo,ao1,bo1,co1,do1,eo1,fo1,go1]
        r=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32]
        d=0
        xy=[]
        for zk in range(0,len(q)):
            if q[zk] is None:
                vb=0
            else:
                vb=q[zk].get()
            top=1
            if vb==1:
                um=r[d].get()
                top=um*pr[d]
                xy.append([tablenumber,itn[d],um,pr[d],top])   
            d+=1
        if xy!=[]:
            for z in xy:
                orderprint.append(z)
                orderd.append(z)
            xy.clear()

            billprint(0)
        else:
            billprint(1)

#FUNCTION RESPONSIBLE FOR ORDERING ITEMS
def menu(a):
    try:
        if True==bool(table.winfo_exists()):
            table.withdraw()
        else:
            pass
    except NameError:
        pass
    global tablenumber,ords
    if a<10:
        f='0'+str(a)
        tablenumber=f
    else:
        tablenumber=a
    
    con,f=conn()
    if con==1:
        cb=f.cursor()
        cb.execute("SELECT * FROM MENU;")
        g=cb.fetchall()
        ords=Toplevel(root)
        ords.title('PLACE ORDER')
        ords.geometry("1100x650")
        ords.minsize(1100,650)
        ords.maxsize(1100,650)
        ords.configure(bg='cyan')

        global a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32
        global ao,bo,co,do,eo,fo,go,ho,io,jo,ko,lo,mo,no,po,qo,ro,so,to,uo,vo,wo,xo,yo,zo,ao1,bo1,co1,do1,eo1,fo1,go1
        q='|\n'*27

        img1= Image.open("back.png")
        rimg1= img1.resize((30,25))
        nimg1= ImageTk.PhotoImage(rimg1)
        illg1= Label(ords,image=nimg1)
        illg1.photo=nimg1
        button1= Button(ords,image=nimg1,command=lambda:tabledisp(),bg='cyan',relief='flat',activebackground='cyan').place(x=0,y=10)

        lo1=tkinter.Label(ords,text=q,fg='black',bg='cyan',font=('Arial',11)).place(x=330,y=70)
        lo3=tkinter.Label(ords,text=q,fg='black',bg='cyan',font=('Arial',11)).place(x=700,y=70)
        lo2=tkinter.Label(ords,text='PLACE YOUR ORDER',bg='brown',fg='#02FFBF',font=('Arial bold',16)).place(x=425,y=10)
        
        ao,bo,co,do,eo,fo,go,ho,io,jo,ko,lo,mo,no,po,qo,ro,so,to,uo,vo,wo,xo,yo,zo,ao1,bo1,co1,do1,eo1,fo1,go1=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32=IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()
        n=7
        
        df=80
        tf=10
        tv=[ao,bo,co,do,eo,fo,go,ho,io,jo,ko,lo,mo,no,po,qo,ro,so,to,uo,vo,wo,xo,yo,zo,ao1,bo1,co1,do1,eo1,fo1,go1]
        itq=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32]
        
        if len(g)>24:
            ords.minsize(1400,650)
            ords.maxsize(1400,650)
            
            lo8=tkinter.Label(ords,text=q,fg='black',bg='cyan',font=('Arial',11)).place(x=1070,y=70)
            
            img= Image.open("logof.png")
            rimg= img.resize((30,25))
            nimg= ImageTk.PhotoImage(rimg)
            illg= Label(ords,image=nimg)
            illg.photo=nimg
            button= Button(ords,image=nimg,command=lambda:lgp(),bg='cyan',relief='flat',activebackground='cyan').place(x=1360,y=10)
        else:
            img= Image.open("logof.png")
            rimg= img.resize((30,25))
            nimg= ImageTk.PhotoImage(rimg)
            illg= Label(ords,image=nimg)
            illg.photo=nimg
            button= Button(ords,image=nimg,command=lambda:lgp(),bg='cyan',relief='flat',activebackground='cyan').place(x=1060,y=10)

        for i in range(0,len(g)):
            co1=tkinter.Checkbutton(ords,text=g[i][0],variable=tv[i],onvalue=1,offvalue=0,padx=8,pady=8,fg='#e01f8a',bg='cyan',font=('Arial',12)).place(x=tf,y=df)
            so1=tkinter.Scale(ords,variable=itq[i],from_=1,to=20,orient=HORIZONTAL,font=('Arial',9),fg='#0F8222',bg='cyan',width=5).place(x=tf+203,y=df)
            if n==i:
                tf+=360
                df=20
                n+=8
            df+=60   
        eo1=tkinter.Button(ords,text='Click here to get the bill',font=('Arial bold',11),fg='#02FFBF',bg='brown',command=lambda:bill()).place(x=450,y=600)

#FUNCTION RESPONSIBLE FOR DISPLAYING TABLE
def tabledisp():
    try:
        if True==bool(ords.winfo_exists()):
            ords.withdraw()
        else:
            pass
    except NameError:
        pass
    try:
        if True==bool(blp2.winfo_exists()):
            blp2.withdraw()
        else:
            pass
    except NameError:
        pass

    
    global table
    table=Toplevel(root)
    table.title('TABLES')
    table.geometry("600x600")
    table.minsize(600,600)
    table.maxsize(600,600)
    table.columnconfigure(0,minsize=50)
    table.rowconfigure([0,1],minsize=30)


    
    img2= Image.open("tabledisp.jpg")
    rimg2= img2.resize((600,600))
    nimg2= ImageTk.PhotoImage(rimg2)
    illg2= Label(table,image=nimg2)
    illg2.photo=nimg2
    illg2.place(x=0,y=0)
    bgimg=tkinter.Label(table,image=nimg2).place(x=0,y=0)

    text1=tkinter.Label(table,text='TABLES',font=('Arial bold',11),bg='#02FFBF',fg='#0015ff').place(x=250,y=2)


    img= Image.open("logof.png")
    rimg= img.resize((30,25))
    nimg= ImageTk.PhotoImage(rimg)
    global illg
    illg= Label(table,image=nimg)
    illg.photo=nimg
    buttoon=Button(table,image=nimg,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='blue').place(x=564,y=2)

    img1= Image.open("back.png")
    rimg1= img1.resize((30,25))
    nimg1= ImageTk.PhotoImage(rimg1)
    illg1= Label(table,image=nimg1)
    illg1.photo=nimg1
    button1= Button(table,image=nimg1,command=lambda:lgp(),bg='#02FFBF',relief='flat',activebackground='blue',state='disabled').place(x=0,y=2)

    table1=tkinter.Button(table,text='TABLE 1',command=lambda:menu(1),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=5,column=1,padx=10,pady=10)
    table2=tkinter.Button(table,text='TABLE 2',command=lambda:menu(2),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=5,column=2,padx=10,pady=10)
    table3=tkinter.Button(table,text='TABLE 3',command=lambda:menu(3),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=5,column=3,padx=10,pady=10)
    table4=tkinter.Button(table,text='TABLE 4',command=lambda:menu(4),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=5,column=4,padx=10,pady=10)
    table5=tkinter.Button(table,text='TABLE 5',command=lambda:menu(5),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=6,column=1,padx=20,pady=20)
    table6=tkinter.Button(table,text='TABLE 6',command=lambda:menu(6),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=6,column=2,padx=20,pady=20)
    table7=tkinter.Button(table,text='TABLE 7',command=lambda:menu(7),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=6,column=3,padx=20,pady=20)
    table8=tkinter.Button(table,text='TABLE 8',command=lambda:menu(8),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=6,column=4,padx=20,pady=20)
    table9=tkinter.Button(table,text='TABLE 9',command=lambda:menu(9),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=7,column=1,padx=20,pady=20)
    table10=tkinter.Button(table,text='TABLE 10',command=lambda:menu(10),font=('Arial',11),bg='grey',fg='cyan' ,height=4,width=8).grid(row=7,column=2,padx=20,pady=20)
    table11=tkinter.Button(table,text='TABLE 11',command=lambda:menu(11),font=('Arial ',11),bg='grey',fg='cyan',height=4,width=8).grid(row=7,column=3,padx=20,pady=20)
    table12=tkinter.Button(table,text='TABLE 12',command=lambda:menu(12),font=('Arial',11),bg='grey',fg='cyan',height=4,width=8).grid(row=7,column=4,padx=20,pady=20)

    text2=tkinter.Label(table,text='*CLICK THE TABLE TO PLACE THE ORDER*',font=('Arial bold',11),bg='#02FFBF',fg='#0015ff').place(x=125,y=475)

#CALLING THE FUNCTION TO START THE PROGRAM
lgp()
mainloop()