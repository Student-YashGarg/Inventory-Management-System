from customtkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
################################################################################################################
def category_form(myroot,update_count):
    global search_box,search_btn,showall_btn,search_entry,quantity_entry,id_entry,name_entry,description_entry,tree 

    category_frame=CTkFrame(myroot,width=980,height=600,fg_color="white",bg_color="white")
    category_frame.place(relx=270/1260,rely=78/680)

    image=Image.open("category_form_img.jpg")
    image=image.resize((320,400),Image.LANCZOS)
    temp_img=ImageTk.PhotoImage(image=image)
    CTkLabel(category_frame,image=temp_img,fg_color="white",text='').place(relx=652/980,rely=100/600)

    CTkLabel(category_frame,text="   Manage Category Details",font=('verdana',23,'bold'),anchor='center',fg_color="#7242eb",text_color="white").place(x=0,y=0,relwidth=1)

    search_frame=CTkFrame(category_frame,fg_color="#161c30",bg_color="white",width=980,height=45)
    search_frame.propagate(0)
    search_frame.place(relx=0,rely=33/600)

    image=Image.open("back.ico")
    back_img=ImageTk.PhotoImage(image=image)
    category_frame.back_img=back_img
    CTkButton(search_frame,image=category_frame.back_img,text='',width=20,fg_color="white",cursor='hand2',command=lambda: (category_frame.place_forget(),update_count())).place(relx=5/980,rely=2/45)

    search_option=['Search By','Id','Name','items','description']
    default_value=StringVar(value=search_option[0])
    search_box=CTkComboBox(search_frame,values=search_option,state='readonly',variable=default_value,font=('verdana',20),height=35,width=200,fg_color="white")
    search_box.place(relx=70/980,rely=5/45)

    search_entry=CTkEntry(search_frame,fg_color="white",text_color="black",font=('verdana',20),placeholder_text="Search",height=35,width=200)
    search_entry.place(relx=300/980,rely=5/45)

    search_btn=CTkButton(search_frame,text="Search",font=('verdana',18),height=35,width=200,command=search_data,fg_color="#7242eb",text_color="white")
    search_btn.place(relx=530/980,rely=5/45)
    showall_btn=CTkButton(search_frame,text="Show All",font=('verdana',18),height=35,width=200,command=showall,fg_color="#7242eb",text_color="white")
    showall_btn.place(relx=760/980,rely=5/45)

    treeview_frame=CTkFrame(category_frame,width=650,height=240)
    treeview_frame.propagate(0)
    treeview_frame.place(relx=0,rely=78/600)

    tree=ttk.Treeview(treeview_frame,height=11,show="headings")
    # tree.pack(side=LEFT, fill="both", expand=True)
    tree['columns']=('id','Name','items','description')
    tree.heading('id',text='Id')
    tree.heading('Name',text="Name")
    tree.heading('items',text="Quantity")
    tree.heading('description',text="Description")

    tree.column('id',width=100)
    tree.column('Name',width=200)
    tree.column('items',width=180)
    tree.column('description',width=300)

    style=ttk.Style()
    style.configure('Treeview.Heading',font=('verdana',15))
    style.configure('Treeview',font=('verdana',12),background="#161c30",foreground="cyan",fieldbackground="green")

    # Vertical Scrollbar 
    ver_scrollbar = ttk.Scrollbar(category_frame, orient=VERTICAL, command=tree.yview)
    ver_scrollbar.place(relx=640/980,rely=78/600,height=240) 
    tree.config(yscrollcommand=ver_scrollbar.set) 

    # horizontal Scrolbar
    hor_scrollbar = ttk.Scrollbar(treeview_frame, orient=HORIZONTAL)
    hor_scrollbar.pack(side=BOTTOM, fill=X)
    hor_scrollbar.config(command=tree.xview)

    tree.pack(pady=0,side=LEFT,fill=BOTH,expand=1)
    # tree.pack(pady=10)


    entry_frame=CTkFrame(category_frame,fg_color="#161c30",width=400,height=300)
    entry_frame.place(relx=0,rely=330/600)
    entry_frame.propagate(0)

    id_lbl=CTkLabel(entry_frame,text="Category Id",font=('verdana',20,'bold'),text_color="white").grid(row=0,column=0,padx=30,pady=10)
    id_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Id",state="readonly")
    id_entry.grid(row=0,column=2,padx=5)

    name_lbl=CTkLabel(entry_frame,text="Category Name",font=('verdana',20,'bold'),text_color="white").grid(row=1,column=0,padx=30,pady=10)
    name_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Name")
    name_entry.grid(row=1,column=2,padx=5)

    quantity_lbl=CTkLabel(entry_frame,text="Quantity",font=('verdana',20,'bold'),text_color="white").grid(row=2,column=0,padx=30,pady=10)
    quantity_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter quantity")
    quantity_entry.grid(row=2,column=2,padx=5)

    descrpition_lbl=CTkLabel(entry_frame,text="Description",font=('verdana',20,'bold'),text_color="white").grid(row=3,column=0,padx=30,pady=10)
    description_entry=CTkEntry(entry_frame,fg_color="white",text_color="black",font=('verdana',20),width=420,placeholder_text=("Enter Description"))
    # email_entry.place(x=32,y=180)
    description_entry.grid(row=3,column=2,padx=5)

    #Button_Frame
    btn_frame=CTkFrame(category_frame,fg_color="white",bg_color="white")
    btn_frame.place(relx=0,rely=540/600)

    new_btn=CTkButton(btn_frame,text="New ",font=('verdana',20),corner_radius=30,command=lambda:reset(True),fg_color="#7242eb")
    new_btn.grid(row=0,column=0,padx=10)

    add_btn=CTkButton(btn_frame,text="Add ",font=('verdana',20),corner_radius=30,command=add_category,fg_color="#7242eb")
    add_btn.grid(row=0,column=1,padx=10)

    update_btn=CTkButton(btn_frame,text="Update ",font=('verdana',20),corner_radius=30,command=update,fg_color="#7242eb")
    update_btn.grid(row=0,column=2,padx=10)

    delete_btn=CTkButton(btn_frame,text="Delete ",font=('verdana',20),corner_radius=30,command=delete,fg_color="#7242eb")
    delete_btn.grid(row=0,column=3,padx=10)

    Delete_all_btn=CTkButton(btn_frame,text="Delete All ",font=('verdana',20),corner_radius=30,command=delete_all,fg_color="#7242eb")
    Delete_all_btn.grid(row=0,column=4,padx=10)
    
    #bydefalut show data when window open
    treeview_data()

    #bind window..to put data when click on row
    tree.bind('<ButtonRelease>',selection)  
    

####################################################################################################################################################################################

#Function
import CAT_MODEL
C=CAT_MODEL.Category()

import CAT_DAO
cdao=CAT_DAO.Category_DAO()

def treeview_data():
    data=cdao.showall()
    tree.delete(*tree.get_children())
    for row in data:
        tree.insert('',END,values=row)
        
def add_category():
    
    if id_entry.get()=='' or name_entry.get()=='' or quantity_entry.get()=='' or description_entry.get()=='':
        messagebox.showerror('Error','All field are required!')
        
    elif cdao.id_exist(id_entry.get()):
        messagebox.showerror('Error','Id already exist!')
    # elif not id_entry.get().startswith('CAT'):
    #     messagebox.showerror("Error","Invalid ID Format:Use 'CAT' followed by a number(e.g., 'CAT1') ")
    else:
        # E=MODEL.category()
        C.setid(id_entry.get())
        C.setname(name_entry.get())
        C.setquantity(quantity_entry.get())
        C.setdesc(description_entry.get())
   
        
        # edao=category_dao.category_DAO()
        data=cdao.insertcategory(C)
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
        id_entry.insert(0, cdao.get_next_id())      # ✅ Then insert new ID
        id_entry.configure(state='readonly')   # Lock again
        
    else:
        id_entry.configure(state='normal')     # Unlock first
        id_entry.delete(0, END)  # Still clear if not new
        id_entry.configure(state='readonly')     # Lock again
    name_entry.delete(0, END)
    quantity_entry.delete(0, END)
    description_entry.delete(0, END)
    name_entry.focus()

    
    # myroot.focus()
    name_entry.focus()
    # quantity_entry.focus()
    # description_entry.focus()
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
    quantity_entry.insert(0,row[2])
    description_entry.insert(0,row[3])

     
def update():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select Data to Update')
    else:
        C.setid(id_entry.get())
        C.setname(name_entry.get())
        C.setquantity(quantity_entry.get())
        C.setdesc(description_entry.get())
   

        
        # edao=category_dao.category_DAO()
        ch=cdao.update_data(C)
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
            cdao.delete_by_id(id_entry.get())
            treeview_data()
            reset()
            messagebox.showinfo('Delete',"Data Deleted Successfully!")

def delete_all():
    ch=messagebox.askyesno('Conform','Are you sure want to Delete All!?')
    if ch:
        cdao.delete_all() 
        treeview_data()
        reset()  
        messagebox.showinfo('Delete All',"All Data Deleted Successfully!") 
        
def search_data():
    if search_box.get()=='Search By':
        messagebox.showerror("Error","Please Select an Option!")
    elif search_entry.get()=="":
        messagebox.showerror('Error',"Enter Value to Search!")
    else:
        data=cdao.search(search_box.get(),search_entry.get())
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