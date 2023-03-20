from tkinter import *
from tkinter import messagebox as letter
ip = "127.0.0.1"
websl=[]
def remove():
    ab=fill.get()
    if ab=="" :
        letter.showerror(" Empty Entry box","Entrybox is Already Blank !! ")
    else:
        fill.delete(0, END)
def exit1():
    r2=letter.askquestion("Exit","Do You Really Want To Exit? ")
    if r2 == 'yes' :
        win.destroy()     
    else:
        pass
    
    
def blocker():
    txttext = fill.get()
    if ("www" not in txttext):
        letter.showerror("invalid website","Please enter a valid address!!\n eg:www.example.com")
    else:
        my_websites=txttext.lower()
        if (txttext == ""):
            letter.showerror("Empty Entry Box","Please Write Something in Entry Box !!")
        else:
            fill.delete(0, END)
            
            ip = "127.0.0.1"
            with open(r"C:\Windows\System32\drivers\etc\hosts", "r+") as host:
                content = host.read()
                host.close()
                if my_websites in content:
                    letter.showerror("Already Blocked","The chosen website is already Blocked !!")
                    host.close()
                    pass
                else:
                    ls=[]
                    data=open("C:\Windows\System32\drivers\etc\hosts", "r+")
                    for i in data:
                        j=i.replace("\n","")
                        ls.append(j)
                    data.close()
                    we=(ip+"\t"+my_websites)
                    ls.append(we)
                    data=open("C:\Windows\System32\drivers\etc\hosts", "r+")
                    for l in ls:
                        i=(l + "\n")
                        data.write(i)
                    data.close()
                    weeb()
def unblocker():
    txttext = fill.get()
    if ("www" not in txttext):
        letter.showerror("invalid website","Please enter a valid address!!\n eg:www.example.com")
    else:
        my_websites=txttext.lower()
        if (txttext == ""):
            letter.showerror("Empty Entry Box","Please Write the Website in Entry Box !!")
        else:
            fill.delete(0, END)
            
            ip = "127.0.0.1"
            with open(r"C:\Windows\System32\drivers\etc\hosts", "r+") as host:
                content = host.read()
                host.close()
                if my_websites in content:
                    ls=[]
                    data=open("C:\Windows\System32\drivers\etc\hosts", "r+")
                    for i in data:
                        j=i.replace("\n","")
                        ls.append(j)
                    data.close()
                    we=(ip+"\t"+my_websites)
                    ls.remove(we)
                    data=open("C:\Windows\System32\drivers\etc\hosts", "w")
                    for l in ls:
                        i=(l + "\n")
                        data.write(i)
                    data.close()
                    weeb()

                else:
                    letter.showerror("Not Blocked","The chosen website wasn't  Blocked !!")
                    print(my_websites + " was not been blocked")
                    host.close()
def weeb():
    
    gh=[]
    cd=""
    data=open("C:\Windows\System32\drivers\etc\hosts", "r+")
    for i in data:
        j=i.replace(ip+"\t","")
        gh.append(j)
    data.close()
    for i in range(len(gh)):
        cd=cd+gh[i]
    web.config(text = cd)

def uball():
    data=open("C:\Windows\System32\drivers\etc\hosts", "w")
    data.close()
    web.config(text = "")
def about():
    def forwin2():
        po2.destroy()
    po2=Tk()
    po2.title("About Website Blocker")
    abel2=Label(po2,text="""               WELCOME To Website Blocker
    ***** HOW TO USE  *****
1)Use entry field to insert website address you would like to block.
2)Use button given below "Block" to Block the address.
3)Unblock all websites using "unblock all" option from menubar.
4)Many more feature available in menubar.
5)Clear entry with "clear" button.
""")
    abel2.pack()
    bu1=Button(po2,text="  OK  ",font=('Helvetica 14 bold italic'),command=forwin2)
    bu1.pack()


hash_rm=open("C:\Windows\System32\drivers\etc\hosts", "r+")
content = hash_rm.read()
hash_rm.close()
if ("#" in content):
    hash_rm=open("C:\Windows\System32\drivers\etc\hosts", "w")
    hash_rm.close()
else:
    pass

    

win = Tk()
win.title("WebBlocker ")

win.iconbitmap("logo.ico")

mla=Label(win,text="WebBlocker ⛔️",font=("Algerian",15),fg="purple")
mla.pack()
mla4=Label(win,text="<= Enter Website Below =>")
mla4.pack()

fill = Entry(win,width=45,font=' 13',bg="powder blue")
fill.focus_set()
fill.pack(side=TOP)
web22=Label(win,text="Example: www.example.com",fg="green")
web22.pack()
butt = Button(win, text=" Clear Entry ⬅ ",bg="white",fg="red",font=('Time 10 bold'),command=remove)
butt.pack()


alb=Label(win,text="Blocked Websites : ",font=("times 10 bold",13),fg="brown")
alb.pack()
web=Label(win,text="",font=("Algerian",13),fg="black")
web.pack()
weeb()


button1=Button(win, text="Unblock ",font=("Algerian",14),fg="green",command=unblocker)
button1.pack(padx=7,pady=5,side=LEFT)

button2=Button(win, text="Block",font=("Algerian",14),fg="red",command=blocker)
button2.pack(padx=7,pady=5,side=RIGHT)
 

button3=Button(win, text="EXIT",font=("Algerian",14),command=exit1)
button3.pack(padx=7,pady=5,side=BOTTOM)

menubar=Menu(win)

em=Menu(menubar,tearoff=0)
em.add_command(label="Unblock All",command=uball)
em.add_separator()
em.add_command(label="Exit",command=exit1)
menubar.add_cascade(label="Edit",menu=em)


rm=Menu(menubar,tearoff=0)
rm.add_command(label="Clear Entry",command=remove)
rm.add_separator()
rm.add_command(label="Block",command=blocker)
rm.add_command(label="Unblock ",command=unblocker)
menubar.add_cascade(label="Run",menu=rm)

hm=Menu(menubar,tearoff=0)
hm.add_command(label="About ❔",command=about)
menubar.add_cascade(label="Help ❔",menu=hm)


win.config(menu=menubar)

win.mainloop


