from customtkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
################################################################################################################
def employee_form(myroot,update_count):
    global tree,id_entry,name_entry,contact_entry,gender_box,dep_box,emptype_box,salary_entry,password_entry,position_box,doj_entry,email_entry,search_box,search_entry,search_btn,showall_btn

    employee_frame=CTkFrame(myroot,width=980,height=600,fg_color="#161c30",bg_color="white")
    employee_frame.place(relx=270/1260,rely=78/680)


    CTkLabel(employee_frame,text="   Manage Employee Details",font=('verdana',25,'bold'),anchor='center',fg_color="#0C7E55",text_color="white").place(x=0,y=0,relwidth=1)


    #Search_Frame
    search_frame=CTkFrame(employee_frame,fg_color="#161c30",bg_color="white",width=980,height=45)
    search_frame.propagate(0)
    search_frame.place(relx=0,rely=33/680)

    
    image=Image.open("back.ico")
    back_img=ImageTk.PhotoImage(image=image)
    employee_frame.back_img = back_img   # keep reference
    CTkButton(search_frame,image=employee_frame.back_img,text='',width=20,fg_color="white",cursor='hand2',command=lambda: (employee_frame.place_forget(),update_count())).place(relx=5/980,rely=2/45)

    search_option=['Search By','Id','Name','Contacts','Email','Gender','Salary','E_Type','Dept','Password','DOJ','Position']
    default_value=StringVar(value=search_option[0])
    search_box=CTkComboBox(search_frame,values=search_option,state='readonly',variable=default_value,font=('verdana',20),height=35,width=200,fg_color="white")
    search_box.place(relx=70/980,rely=5/45)

    search_entry=CTkEntry(search_frame,fg_color="white",text_color="black",font=('verdana',20),placeholder_text="Search",height=35,width=200)
    search_entry.place(relx=300/980,rely=5/45)

    search_btn=CTkButton(search_frame,text="Search",font=('verdana',18),height=35,width=200,fg_color="#0C7E55",command=search_data,text_color="white")
    search_btn.place(relx=530/980,rely=5/45)
    showall_btn=CTkButton(search_frame,text="Show All",font=('verdana',18),height=35,width=200,fg_color="#0C7E55",command=showall,text_color="white")
    showall_btn.place(relx=760/980,rely=5/45)

    #Treeview Frame
    treeview_frame=CTkFrame(employee_frame,width=980,height=240,fg_color="#161c30")
    treeview_frame.propagate(0)
    treeview_frame.place(relx=0/980,rely=73/600)

    tree=ttk.Treeview(treeview_frame,height=10,show="headings")
    # tree.pack(side=LEFT, fill="both", expand=True)
    tree['columns']=('EMPId','Name','Gender','contact','Email','Salary','doj','E_type','position','dep','password')
    tree.heading('EMPId',text='Empid')
    tree.heading('Name',text="Name")
    tree.heading('Gender',text="Gender")
    tree.heading('contact',text="Contacts")
    tree.heading('Email',text="Email")
    tree.heading('Salary',text="Salary")
    tree.heading('doj',text="DOJ")
    tree.heading('E_type',text="Emp_type")
    tree.heading('position',text="Position")
    tree.heading('dep',text="Dep")
    tree.heading('password',text="Password")


    # tree.config(show='headings')
    tree.column('EMPId',width=70)
    tree.column('Gender',width=80)
    tree.column('Name',width=130)
    tree.column('Email',width=210)
    tree.column('Salary',width=100)
    tree.column('contact',width=120)
    # tree.column('dob',width=100)
    tree.column('doj',width=100)
    tree.column('E_type',width=100)
    tree.column('position',width=100)
    tree.column('dep',width=90)
    tree.column('password',width=120)

    style=ttk.Style()
    style.configure('Treeview.Heading',font=('verdana',12))
    style.configure('Treeview',font=('verdana',11),background="#161c30",foreground="cyan",fieldbackground="green")

    # Vertical Scrollbar 
    ver_scrollbar = ttk.Scrollbar(employee_frame, orient=VERTICAL, command=tree.yview)
    ver_scrollbar.place(relx=963/980,rely=74/600,relheight=225/600) 
    ver_scrollbar.config(command=tree.yview)
    # horizontal Scrolbar
    hor_scrollbar = ttk.Scrollbar(treeview_frame, orient=HORIZONTAL)
    hor_scrollbar.pack(side=BOTTOM, fill=X)
    hor_scrollbar.config(command=tree.xview)

    # Attach scrollbar to tree
    tree.config(xscrollcommand=hor_scrollbar.set)
    tree.config(yscrollcommand=ver_scrollbar.set) 
    tree.propagate(0)
    tree.pack(pady=0,side=LEFT,fill=BOTH,expand=1)

    # # #ENTRY FRAME
    entry_frame=CTkFrame(employee_frame,fg_color="#161c30")
    entry_frame.place(relx=0/980,rely=320/600)

    id_lbl=CTkLabel(entry_frame,text="EMPId",font=('verdana',20,'bold'),text_color="white").grid(row=0,column=0,padx=30,pady=10)
    id_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Id",state="readonly")
    id_entry.grid(row=0,column=2,padx=5)

    name_lbl=CTkLabel(entry_frame,text="Name",font=('verdana',20,'bold'),text_color="white").grid(row=0,column=3,padx=30,pady=10)
    name_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Name")
    name_entry.grid(row=0,column=5)

    contact_lbl=CTkLabel(entry_frame,text="Contact",font=('verdana',20,'bold'),text_color="white").grid(row=2,column=0,padx=20,pady=10)
    contact_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter contact")
    contact_entry.grid(row=2,column=2)

    gender_lbl=CTkLabel(entry_frame,text="Gender",font=('verdana',20,'bold'),text_color="white").grid(row=0,column=6,padx=20,pady=10)
    gender_option=['Select','Male','Female']
    selected_gender = StringVar(value=gender_option[0])
    gender_box=CTkComboBox(entry_frame,values=gender_option,fg_color="white",text_color="black",font=('verdana',20),width=175,state='readonly',variable=selected_gender)
    gender_box.grid(row=0,column=7)

    emptype_lbl=CTkLabel(entry_frame,text="E Type",font=('verdana',20,'bold'),text_color="white").grid(row=2,column=6,padx=20,pady=10)
    emptype_option=['select','Part-time','Full-time','contract']
    selected_emptype = StringVar(value=emptype_option[0])
    emptype_box=CTkComboBox(entry_frame,values=emptype_option,fg_color="white",text_color="black",font=('verdana',20),width=175,state='readonly',variable=selected_emptype)
    emptype_box.grid(row=2,column=7)

    salary_lbl=CTkLabel(entry_frame,text="Salary",font=('verdana',20,'bold'),text_color="white").grid(row=4,column=0,padx=20,pady=10)
    salary_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Salary")
    salary_entry.grid(row=4,column=2)



    doj_lbl=CTkLabel(entry_frame,text="DOJ",font=('verdana',20,'bold'),text_color="white").grid(row=2,column=3,padx=20,pady=10)
    doj_entry=DateEntry(entry_frame,width=13,height=10,font=('verdana',15),state='readonly',date_pattern='dd/mm/yy')
    doj_entry.grid(row=2,column=5)

    email_lbl=CTkLabel(entry_frame,text="Email",font=('verdana',20,'bold'),text_color="white").grid(row=4,column=3,padx=20,pady=10)
    email_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=350,placeholder_text="Enter Email")
    email_entry.place(x=473,y=155)



    dep_lbl=CTkLabel(entry_frame,text="Dep",font=('verdana',20,'bold'),text_color="white").grid(row=3,column=6,padx=20,pady=10)
    dep_option=['Select','IT','Sales','Finance','Service','Inspection']
    selected_dep = StringVar(value=dep_option[0])
    dep_box=CTkComboBox(entry_frame,values=dep_option,fg_color="white",text_color="black",font=('verdana',20),width=175,state='readonly',variable=selected_dep)
    dep_box.grid(row=3,column=7)

    position_lbl=CTkLabel(entry_frame,text="Position",font=('verdana',20,'bold'),text_color="white").grid(row=3,column=3,padx=20,pady=10)
    position_option=['Select','User','Admin']
    selected_position = StringVar(value=position_option[0])
    position_box=CTkComboBox(entry_frame,values=position_option,fg_color="white",text_color="black",font=('verdana',20),width=200,state='readonly',variable=selected_position)
    position_box.grid(row=3,column=5)

    password_lbl=CTkLabel(entry_frame,text="Password",font=('verdana',20,'bold'),text_color="white").grid(row=3,column=0,padx=5,pady=10)
    password_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Password")
    password_entry.grid(row=3,column=2)


    #Button_Frame
    btn_frame=CTkFrame(employee_frame,fg_color="#161c30",bg_color="#161c30")
    btn_frame.place(relx=90/980,rely=540/600)

    new_btn=CTkButton(btn_frame,text="New ",font=('verdana',20),corner_radius=30,fg_color="#0C7E55",command=lambda:reset(True))
    new_btn.grid(row=0,column=0,padx=10)

    add_btn=CTkButton(btn_frame,text="Add ",font=('verdana',20),corner_radius=30,fg_color="#0C7E55",command=add_employee)
    add_btn.grid(row=0,column=1,padx=10)

    update_btn=CTkButton(btn_frame,text="Update ",font=('verdana',20),corner_radius=30,fg_color="#0C7E55",command=update)
    update_btn.grid(row=0,column=2,padx=10)

    delete_btn=CTkButton(btn_frame,text="Delete ",font=('verdana',20),corner_radius=30,fg_color="#0C7E55",command=delete)
    delete_btn.grid(row=0,column=3,padx=10)

    Delete_all_btn=CTkButton(btn_frame,text="Delete All ",font=('verdana',20),corner_radius=30,fg_color="#0C7E55",command=delete_all)
    Delete_all_btn.grid(row=0,column=4,padx=10)

    #bydefalut show data when window open
    treeview_data()

    #bind window..to put data when click on row
    tree.bind('<ButtonRelease>',selection)  

####################################################################################################################################################################################
#Function
import EMP_MODEL
E=EMP_MODEL.Employee()

import EMP_DAO
edao=EMP_DAO.Employee_DAO()

def treeview_data():
    data=edao.showall()
    tree.delete(*tree.get_children())
    for row in data:
        tree.insert('',END,values=row)
        
def add_employee():
    
    if id_entry.get()=='' or name_entry.get()=='' or contact_entry.get()=='' or salary_entry.get()=='' or gender_box.get()=='Select' or emptype_box.get()=='Select' or position_box.get()=='Select' or email_entry.get()=='' or doj_entry.get()=='' or password_entry.get()=='' or dep_box.get()=='Select':
        messagebox.showerror('Error','All field are required!')
        
    elif edao.id_exist(id_entry.get()):
        messagebox.showerror('Error','Id already exist!')
    # elif not id_entry.get().startswith('EMP'):
    #     messagebox.showerror("Error","Invalid ID Format:Use 'EMP' followed by a number(e.g., 'EMP1') ")
    else:
        # E=MODEL.Employee()
        E.setid(id_entry.get())
        E.setname(name_entry.get())
        E.setgender(gender_box.get())
        E.setcontact(contact_entry.get())
        E.setemail(email_entry.get())
        E.setsalary(salary_entry.get())
        E.setdoj(doj_entry.get())
        E.setetype(emptype_box.get())
        E.setpos(position_box.get())
        E.setdept(dep_box.get())
        E.setpass(password_entry.get())
   
        
        # edao=Employee_dao.Employee_DAO()
        data=edao.insertemployee(E)
        # reset()
        treeview_data()
        if data==True:
            messagebox.showinfo("Inserted",'Record Insert Successfully')
        else:
            messagebox.showerror("Error",'Something went wrong!')

def reset(value=False):
    if value:
        tree.selection_remove(tree.focus())
        id_entry.configure(state='normal')     # Unlock first
        id_entry.delete(0, END)                     # ✅ First clear
        id_entry.insert(0, edao.get_next_id())      # ✅ Then insert new ID
        id_entry.configure(state='readonly')   # Lock again
    else:
        id_entry.configure(state='normal')     # Unlock first
        id_entry.delete(0, END)  # Still clear if not new
        id_entry.configure(state='readonly')     # Lock again
    name_entry.delete(0,END)
    gender_box.set('Select')
    contact_entry.delete(0,END)
    email_entry.delete(0,END)
    salary_entry.delete(0,END)
    # doj_entry.set_date(any)
    emptype_box.set('Select')
    position_box.set('Select')
    dep_box.set('Select')
    password_entry.delete(0,END)
    
    # myroot.focus()
    name_entry.focus()
    # salary_entry.focus()
    # contact_entry.focus()
    # password_entry.focus()
    # email_entry.focus()
    # id_entry.focus()

def selection(event):
    selected_item=tree.selection()
    row=tree.item(selected_item)['values']
    # print(row)
    reset()
    # role_box
    id_entry.configure(state='normal')     # Unlock first
    id_entry.delete(0, END)  # Still clear if not new
    id_entry.insert(0,row[0])
    id_entry.configure(state='readonly')     # Lock again
    
    name_entry.insert(0,row[1])
    gender_box.set(row[2])
    contact_entry.insert(0,row[3])
    email_entry.insert(0,row[4])
    salary_entry.insert(0,row[5])
    doj_entry.set_date(row[6])
    emptype_box.set(row[7])
    position_box.set(row[8])
    dep_box.set(row[9])
    password_entry.insert(0,row[10])
     
def update():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to Update!')
    else:
        E.setid(id_entry.get())
        E.setname(name_entry.get())
        E.setgender(gender_box.get())
        E.setcontact(contact_entry.get())
        E.setemail(email_entry.get())
        E.setsalary(salary_entry.get())
        E.setdoj(doj_entry.get())
        E.setetype(emptype_box.get())
        E.setpos(position_box.get())
        E.setdept(dep_box.get())
        E.setpass(password_entry.get())

        
        # edao=Employee_dao.Employee_DAO()
        ch=edao.update_data(E)
        if ch==0:
            messagebox.showinfo('Information','No Changes Detected!')
        else:  
            treeview_data()
            reset()
            messagebox.showinfo('Update',"Data Updated Successfully!")

def delete():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to Delete!')
    else:
        ch=messagebox.askyesno('Conform','Are you sure want to Delete!?')
        if ch:
            edao.delete_by_id(id_entry.get())
            treeview_data()
            reset()
            messagebox.showinfo('Delete',"Data Deleted Successfully!")

def delete_all():
    ch=messagebox.askyesno('Conform','Are you sure want to Delete All!?')
    if ch:
        edao.delete_all() 
        treeview_data()
        reset()  
        messagebox.showinfo('Delete All',"All Data Deleted Successfully!") 
        
def search_data():
    if search_box.get()=='Search By':
        messagebox.showerror("Error","Please Select an Option!")
    elif search_entry.get()=="":
        messagebox.showerror('Error',"Enter Value to Search!")
    else:
        data=edao.search(search_box.get(),search_entry.get())
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert('',END,values=row)
            
def showall():
    reset()
    treeview_data()
    search_box.set('Search By')
    search_entry.delete(0,END)
    search_entry.focus()
                  

################################################################################################################

