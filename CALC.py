from customtkinter import *
from tkinter import messagebox,Menu

def calculator(frame):

    calc_frame=CTkFrame(frame,height=351,width=244,fg_color="#161c30",corner_radius=0,border_width=1,border_color="black")
    calc_frame.propagate(0)
    calc_frame.place(x=0,y=0)

    CTkLabel(calc_frame,text="Calculator",font=('verdana',14,'bold'),anchor='center',fg_color="#2471a3",text_color="white").pack(side=TOP,fill=X)

    #Entry box
    textfield=CTkEntry(calc_frame,justify='center',text_color='cyan',border_color="cyan",fg_color="#161c30",font=("verdana",25),placeholder_text='0')
    textfield.pack(fill=X,side=TOP)

    #Button frame
    btnframe=CTkFrame(calc_frame,width=244,height=531,fg_color="#161c30")
    btnframe.propagate(0)
    btnframe.pack(side=TOP,anchor=W)

    #command
    def click(event=None):
        b=event.widget.master
        btntext=b.cget("text")
        if btntext=='Ans':
            try:
                result=eval(textfield.get())
                textfield.delete(0,END)
                textfield.insert(END,result)
            except ZeroDivisionError:
                messagebox.showwarning("Warning","Can't Divide by zero !")
            except SyntaxError:
                messagebox.showerror("Syntax error","Invalid Syntax !")
            except NameError:
                messagebox.showerror("Name Error","Invalid Keyword!")
            return
        
        elif btntext=="X":
            textfield.insert(END,"*")
            return   
        elif btntext=="C":
            textfield.delete(0,END)
            return
        elif btntext=="<--":
            data=textfield.get()
            newdata=data[0:len(data)-1]
            textfield.delete(0,END)
            textfield.insert(0,newdata)
            return
        else:
            textfield.insert(END,btntext)
            
    def percentage(event=None):
        b=event.widget.master
        btntext=b.cget("text")
        text_value=textfield.get()
        answer=""
        if btntext == "%":
            try:
                if '+' in text_value:
                    A, B = text_value.split("+")
                    answer = str(float(A) + (float(A) * float(B) / 100))

                elif '-' in text_value:
                    A, B = text_value.split("-")
                    answer = str(float(A) - (float(A) * float(B) / 100))

                elif '*' in text_value:
                    A, B = text_value.split("*")
                    answer = str((float(A) * float(B)) / 100)

                elif '/' in text_value:
                    A, B = text_value.split("/")
                    answer = str(float(A) / (float(B) / 100))

                else:
                    # Just a plain percent like "5%" or "100%" etc.
                    answer = str(float(text_value) / 100)
            except ValueError:
                messagebox.showerror("Error","Invalid input!")
                return
                
            textfield.delete(0,END)
            textfield.insert(END,answer)

    def enterclick(event=None):
        try:
            result=eval(textfield.get())
            textfield.delete(0,END)
            textfield.insert(END,result)
        except ZeroDivisionError:
                messagebox.showwarning("Warning","Can't Divide by zero !")
        except SyntaxError:
                messagebox.showerror("Syntax error","Invalid Syntax !")
        except NameError:
                messagebox.showerror("Name Error","Invalid Keyword!")
        return
            
    textfield.bind("<Return>",enterclick)  

    btn1=CTkButton(btnframe,width=60,height=50,text='1',font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    btn2=CTkButton(btnframe,width=60,height=50,text='2',font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    btn3=CTkButton(btnframe,width=60,height=50,text='3',font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    btn4=CTkButton(btnframe,width=60,height=50,text='4',font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    btn5=CTkButton(btnframe,width=60,height=50,text='5',font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    btn6=CTkButton(btnframe,width=60,height=50,text='6',font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    btn7=CTkButton(btnframe,width=60,height=50,text='7',font=('verdana',25),bg_color="#161c30",fg_color="#005271") 
    btn8=CTkButton(btnframe,width=60,height=50,text='8',font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    btn9=CTkButton(btnframe,width=60,height=50,text='9',font=('verdana',25),bg_color="#161c30",fg_color="#005271")  

    btn7.grid(row=0,column=0,padx=1,pady=1) 
    btn8.grid(row=0,column=1)  
    btn9.grid(row=0,column=2,padx=1,pady=1)  
    btn4.grid(row=1,column=0)  
    btn5.grid(row=1,column=1)    
    btn6.grid(row=1,column=2)  
    btn1.grid(row=2,column=0,padx=1,pady=1)  
    btn2.grid(row=2,column=1)  
    btn3.grid(row=2,column=2)    
    # #other buttons
    obrac=CTkButton(btnframe,text="(",width=60,height=50,font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    zero=CTkButton(btnframe,text="0",width=60,height=50,font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    cbrac=CTkButton(btnframe,text=")",width=60,height=50,font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    dot=CTkButton(btnframe,text=".",width=60,height=50,font=('verdana',25),bg_color="#161c30",fg_color="#005271")
    back=CTkButton(btnframe,text="<--",width=60,height=50,font=('verdana',25),bg_color="#161c30",fg_color="cyan3")
    clear=CTkButton(btnframe,text="C",width=60,height=50,font=('verdana',25),bg_color="#161c30",fg_color="coral2")
    plus=CTkButton(btnframe,text="+",width=63,height=50,font=('verdana',25,'bold'),bg_color="#161c30",fg_color="palegoldenrod",text_color="black",hover_color="#0088a9")
    minus=CTkButton(btnframe,text="-",width=63,height=50,font=('verdana',25,'bold'),bg_color="#161c30",fg_color="orange",text_color="black",hover_color="#0088a9")
    prod=CTkButton(btnframe,text="X",width=63,height=50,font=('verdana',25,'bold'),bg_color="#161c30",fg_color="palegoldenrod",text_color="black",hover_color="#0088a9")
    div=CTkButton(btnframe,text="/",width=63,height=50,font=('verdana',25,'bold'),bg_color="#161c30",fg_color="orange",text_color="black",hover_color="#0088a9")
    per=CTkButton(btnframe,text="%",width=63,height=50,font=('verdana',25,'bold'),bg_color="#161c30",fg_color="palegoldenrod",text_color="black",hover_color="#0088a9")

    ans=CTkButton(calc_frame,text="Ans",width=244,height=10,font=('verdana',25),bg_color="#161c30",fg_color="green")

    # #grid
    obrac.grid(row=3,column=0)
    zero.grid(row=3,column=1)
    cbrac.grid(row=3,column=2)
    dot.grid(row=4,column=0,padx=1,pady=1)
    back.grid(row=4,column=1)
    clear.grid(row=4,column=2)
    plus.grid(row=0,column=3)
    minus.grid(row=1,column=3)
    prod.grid(row=2,column=3)
    div.grid(row=3,column=3)
    per.grid(row=4,column=3)

    ans.pack(side=TOP,fill=X,expand=1)

    #bind
    obrac.bind("<Button-1>",click)
    zero.bind("<Button-1>",click)
    cbrac.bind("<Button-1>",click)
    dot.bind("<Button-1>",click)
    back.bind("<Button-1>",click)
    clear.bind("<Button-1>",click)
    plus.bind("<Button-1>",click)
    minus.bind("<Button-1>",click)
    prod.bind("<Button-1>",click)
    div.bind("<Button-1>",click)
    ans.bind("<Button-1>",click)

    btn7.bind("<Button-1>",click) 
    btn8.bind("<Button-1>",click) 
    btn9.bind("<Button-1>",click) 
    btn4.bind("<Button-1>",click) 
    btn5.bind("<Button-1>",click)    
    btn6.bind("<Button-1>",click)
    btn1.bind("<Button-1>",click)  
    btn2.bind("<Button-1>",click)
    btn3.bind("<Button-1>",click)

    per.bind("<Button-1>",percentage)

