from customtkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
################################################################################################################
def supplier_form(myroot,update_count):
    global search_box,search_btn,showall_btn,search_entry,contact_entry,invoice_entry,supplier_entry,description_entry,tree 

    employee_frame=CTkFrame(myroot,width=980,height=600,fg_color="white",bg_color="white")
    employee_frame.place(relx=270/1260,rely=78/680)

    image=Image.open("supplier_form_img.jpg")
    image=image.resize((340,400),Image.LANCZOS)
    temp_img=ImageTk.PhotoImage(image=image)
    CTkLabel(employee_frame,image=temp_img,fg_color="white",text='').place(relx=650/980,rely=100/600)

    CTkLabel(employee_frame,text="   Manage Supplier Details",font=('verdana',23,'bold'),anchor='center',fg_color="#d94c6d",text_color="white").place(relx=0,rely=0,relwidth=1)

    search_frame=CTkFrame(employee_frame,fg_color="#161c30",bg_color="white",width=980,height=45)
    search_frame.propagate(0)
    search_frame.place(relx=0,rely=33/600)

    image=Image.open("back.ico")
    back_img=ImageTk.PhotoImage(image=image)
    employee_frame.back_img = back_img   # keep reference
    CTkButton(search_frame,image=employee_frame.back_img,text='',width=20,fg_color="white",cursor='hand2',command=lambda: (employee_frame.place_forget(),update_count())).place(relx=5/980,rely=2/45)

    search_option=['Search By','Id','Name','Contacts','description']
    default_value=StringVar(value=search_option[0])
    search_box=CTkComboBox(search_frame,values=search_option,state='readonly',variable=default_value,font=('verdana',20),height=35,width=200)
    search_box.place(relx=70/980,rely=5/45)

    search_entry=CTkEntry(search_frame,fg_color="white",text_color="black",font=('verdana',20),placeholder_text="Search",height=35,width=200)
    search_entry.place(relx=300/980,rely=5/45)

    search_btn=CTkButton(search_frame,text="Search",font=('verdana',18),height=35,width=200,fg_color="#d94c6d",text_color="white",command=search_data)
    search_btn.place(relx=530/980,rely=5/45)
    showall_btn=CTkButton(search_frame,text="Show All",font=('verdana',18),height=35,width=200,fg_color="#d94c6d",text_color="white",command=showall)
    showall_btn.place(relx=760/980,rely=5/45)

    treeview_frame=CTkFrame(employee_frame,width=650,height=240,fg_color="red")
    treeview_frame.propagate(0)
    treeview_frame.place(relx=0,rely=78/600)

    tree=ttk.Treeview(treeview_frame,height=11,show="headings")
    # tree.pack(side=LEFT, fill="both", expand=True)
    tree['columns']=('invoice','Name','contact','description')
    tree.heading('invoice',text='Invoice')
    tree.heading('Name',text="Name")
    tree.heading('contact',text="Contacts")
    tree.heading('description',text="Description")

    tree.column('invoice',width=100)
    tree.column('Name',width=200)
    tree.column('contact',width=180)
    tree.column('description',width=300)

    style=ttk.Style()
    style.configure('Treeview.Heading',font=('verdana',15))
    style.configure('Treeview',font=('verdana',12),background="#161c30",foreground="cyan",fieldbackground="green")

    # Vertical Scrollbar 
    ver_scrollbar = ttk.Scrollbar(employee_frame, orient=VERTICAL, command=tree.yview)
    ver_scrollbar.place(relx=640/980,rely=78/600,height=240) 
    tree.config(yscrollcommand=ver_scrollbar.set) 

    # horizontal Scrolbar
    hor_scrollbar = ttk.Scrollbar(treeview_frame, orient=HORIZONTAL)
    hor_scrollbar.pack(side=BOTTOM, fill=X)
    hor_scrollbar.config(command=tree.xview)


    # tree.pack(side=LEFT, fill=BOTH, expand=True)
    tree.pack(pady=0,side=LEFT,fill=BOTH,expand=1)

    entry_frame=CTkFrame(employee_frame,fg_color="#161c30",width=430,height=300)
    entry_frame.place(relx=0,rely=330/600)
    entry_frame.propagate(0)

    invoice_lbl=CTkLabel(entry_frame,text="Invoice No.",font=('verdana',20,'bold'),text_color="white").grid(row=0,column=0,padx=30,pady=10)
    invoice_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Invoice",state="readonly")
    invoice_entry.grid(row=0,column=2,padx=5)

    supplier_lbl=CTkLabel(entry_frame,text="Supplier Name",font=('verdana',20,'bold'),text_color="white").grid(row=1,column=0,padx=30,pady=10)
    supplier_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Name")
    supplier_entry.grid(row=1,column=2,padx=5)

    contact_lbl=CTkLabel(entry_frame,text="Contact No.",font=('verdana',20,'bold'),text_color="white").grid(row=2,column=0,padx=30,pady=10)
    contact_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Contact")
    contact_entry.grid(row=2,column=2,padx=5)

    descrpition_lbl=CTkLabel(entry_frame,text="Description",font=('verdana',20,'bold'),text_color="white").grid(row=3,column=0,padx=30,pady=10)
    description_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=420,placeholder_text=("Enter Description"))
    # email_entry.place(x=32,y=180)
    description_entry.grid(row=3,column=2,padx=5)

    #Button_Frame
    btn_frame=CTkFrame(employee_frame,fg_color="white",bg_color="white")
    btn_frame.place(x=0,y=540)

    new_btn=CTkButton(btn_frame,text="New ",font=('verdana',20),corner_radius=30,fg_color="#d94c6d",command=lambda:reset(True))
    new_btn.grid(row=0,column=0,padx=10)

    add_btn=CTkButton(btn_frame,text="Add ",font=('verdana',20),corner_radius=30,fg_color="#d94c6d",command=add_supplier)
    add_btn.grid(row=0,column=1,padx=10)

    update_btn=CTkButton(btn_frame,text="Update ",font=('verdana',20),corner_radius=30,fg_color="#d94c6d",command=update)
    update_btn.grid(row=0,column=2,padx=10)

    delete_btn=CTkButton(btn_frame,text="Delete ",font=('verdana',20),corner_radius=30,fg_color="#d94c6d",command=delete)
    delete_btn.grid(row=0,column=3,padx=10)

    Delete_all_btn=CTkButton(btn_frame,text="Delete All ",font=('verdana',20),corner_radius=30,fg_color="#d94c6d",command=delete_all)
    Delete_all_btn.grid(row=0,column=4,padx=10)
        
    #bydefalut show data when window open
    treeview_data()

    #bind window..to put data when click on row
    tree.bind('<ButtonRelease>',selection)  


####################################################################################################################################################################################

#Function
import SUP_MODEL
S=SUP_MODEL.Supplier()

import SUP_DAO
sdao=SUP_DAO.Supplier_DAO()

def treeview_data():
    data=sdao.showall()
    tree.delete(*tree.get_children())
    for row in data:
        tree.insert('',END,values=row)
        
def add_supplier():
    
    if invoice_entry.get()=='' or supplier_entry.get()=='' or contact_entry.get()=='' or description_entry.get()=='':
        messagebox.showerror('Error','All field are required!')
        
    elif sdao.id_exist(invoice_entry.get()):
        messagebox.showerror('Error','Id already exist!')
    # elif not invoice_entry.get().startswith('SUP'):
    #     messagebox.showerror("Error","Invalid ID Format:Use 'SUP' followed by a number(e.g., 'SUP1') ")
    else:
        # E=MODEL.Employee()
        S.setid(invoice_entry.get())
        S.setname(supplier_entry.get())
        S.setcontact(contact_entry.get())
        S.setdesc(description_entry.get())
   
        
        # edao=Employee_dao.Employee_DAO()
        data=sdao.insertsupplier(S)
        # reset()
        treeview_data()
        if data==True:
            messagebox.showinfo("Inserted",'Record Insert Successfully')
        else:
            messagebox.showerror("Error",'Something went wrong!')

def reset(value=False):
    if value:
        tree.selection_remove(tree.focus())
        invoice_entry.configure(state='normal')     # Unlock first
        invoice_entry.delete(0, END)                     # ✅ First clear
        invoice_entry.insert(0, sdao.get_next_id())      # ✅ Then insert newinvoice
        invoice_entry.configure(state='readonly')   # Lock again
    else:

        invoice_entry.configure(state='normal')     # Unlock first
        invoice_entry.delete(0, END)  # Still clear if not new
        invoice_entry.configure(state='readonly')     # Lock again
    supplier_entry.delete(0,END)
    contact_entry.delete(0,END)
    description_entry.delete(0,END)
    
    # myroot.focus()
    supplier_entry.focus()
    contact_entry.focus()
    description_entry.focus()
    invoice_entry.focus()

def selection(event):
    selected_item=tree.selection()
    row=tree.item(selected_item)['values']
    # print(row)
    reset()
    # role_box
    invoice_entry.configure(state='normal')     # Unlock first
    invoice_entry.delete(0, END)  # Still clear if not new
    invoice_entry.insert(0,row[0])
    invoice_entry.configure(state='readonly')     # Lock again
    
    supplier_entry.insert(0,row[1])
    contact_entry.insert(0,row[2])
    description_entry.insert(0,row[3])

     
def update():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to Update')
    else:
        S.setid(invoice_entry.get())
        S.setname(supplier_entry.get())
        S.setcontact(contact_entry.get())
        S.setdesc(description_entry.get())
   

        
        # edao=Employee_dao.Employee_DAO()
        ch=sdao.update_data(S)
        if ch==0:
            messagebox.showinfo('Information','No Changes Detected!')
        else:  
            treeview_data()
            reset()
            messagebox.showinfo('Update',"Data Updated Successfully!")

def delete():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to Delete')
    else:
        ch=messagebox.askyesno('Conform','Are you sure want to Delete!?')
        if ch:
            sdao.delete_by_id(invoice_entry.get())
            treeview_data()
            reset()
            messagebox.showinfo('Delete',"Data Deleted Successfully!")

def delete_all():
    ch=messagebox.askyesno('Conform','Are you sure want to Delete All!?')
    if ch:
        sdao.delete_all() 
        treeview_data()
        reset()  
        messagebox.showinfo('Delete All',"All Data Deleted Successfully!") 
        
def search_data():
    if search_box.get()=='Search By':
        messagebox.showerror("Error","Please Select an Option!")
    elif search_entry.get()=="":
        messagebox.showerror('Error',"Enter Value to Search!")
    else:
        data=sdao.search(search_box.get(),search_entry.get())
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