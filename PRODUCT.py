from customtkinter import *
from tkinter import  Spinbox, messagebox,ttk,Scrollbar
from PIL import Image,ImageTk

####################################################################################################################################################################################
def product_form(myroot,update_count):
    global tree,catg_lbl,catg_box,supplier_lbl,supplier_box,name_entry,price_entry,price_lbl,discount_lbl,discount_count,quantity_entry,quantity_lbl,status_lbl,status_box,catg_option,supplier_option,search_box,search_entry,search_btn,showall_btn

    product_frame=CTkFrame(myroot,width=980,height=600,fg_color="#161c30",bg_color="white")
    product_frame.place(x=270,y=78)

    CTkLabel(product_frame,text="   Manage Product Details",font=('verdana',23,'bold'),anchor='center',fg_color="#B83333",text_color="white").place(relx=0,rely=0,relwidth=1)

    #Search_Frame
    search_frame=CTkFrame(product_frame,fg_color="#161c30",bg_color="white",width=980,height=45)
    search_frame.propagate(0)
    search_frame.place(relx=0,rely=33/600)

    image=Image.open("back.ico")
    back_img=ImageTk.PhotoImage(image=image)
    product_frame.back_img=back_img
    CTkButton(search_frame,image=product_frame.back_img,text='',width=20,fg_color="white",cursor='hand2',command=lambda: (product_frame.place_forget(),update_count())).place(relx=5/980,rely=2/45)

    search_option=['Search By','Category','Supplier','Name','Price','Discount','Quantity','Status']
    default_value=StringVar(value=search_option[0])
    search_box=CTkComboBox(search_frame,values=search_option,state='readonly',variable=default_value,font=('verdana',20),height=35,width=200,fg_color="white")
    search_box.place(relx=70/980,rely=5/45)

    search_entry=CTkEntry(search_frame,fg_color="white",text_color="black",font=('verdana',20),placeholder_text="Search",height=35,width=200)
    search_entry.place(relx=300/980,rely=5/45)

    search_btn=CTkButton(search_frame,text="Search",font=('verdana',18),height=35,width=200,fg_color='#B83333',text_color="white",command=search_data)
    search_btn.place(relx=530/980,rely=5/45)
    showall_btn=CTkButton(search_frame,text="Show All",font=('verdana',18),height=35,width=200,fg_color='#B83333',text_color="white",command=showall)
    showall_btn.place(relx=760/980,rely=5/45)

    #LEFT FRAME
    left_frame=CTkFrame(product_frame,fg_color="#161c30")
    left_frame.propagate(0)
    left_frame.place(relx=0,rely=80/600)
    #labels
    catg_lbl=CTkLabel(left_frame,text="Category",font=('verdana',20,'bold'),text_color="white")
    supplier_lbl=CTkLabel(left_frame,text="Supplier",font=('verdana',20,'bold'),text_color="white")
    name_lbl=CTkLabel(left_frame,text="Name",font=('verdana',20,'bold'),text_color="white")
    price_lbl=CTkLabel(left_frame,text="Price",font=('verdana',20,'bold'),text_color="white")
    discount_lbl=CTkLabel(left_frame,text="Discount(%)",font=('verdana',20,'bold'),text_color="white")
    quantity_lbl=CTkLabel(left_frame,text="Quantity",font=('verdana',20,'bold'),text_color="white")
    status_lbl=CTkLabel(left_frame,text="Status",font=('verdana',20,'bold'),text_color="white")
    #grid
    catg_lbl.grid(row=0,column=0,padx=10,pady=15)
    supplier_lbl.grid(row=2,column=0,padx=20,pady=15)
    name_lbl.grid(row=3,column=0,padx=20,pady=15)
    price_lbl.grid(row=4,column=0,padx=20,pady=15)
    discount_lbl.grid(row=5,column=0,padx=20,pady=15)
    quantity_lbl.grid(row=6,column=0,padx=20,pady=15)
    status_lbl.grid(row=7,column=0,padx=20,pady=15)

    #Entry
    name_entry=CTkEntry(left_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter Name")
    price_entry=CTkEntry(left_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter price")
    quantity_entry=CTkEntry(left_frame,fg_color="white",text_color="black",font=('verdana',20),width=200,placeholder_text="Enter quantity")

    #combo boxes
    catg_option=[]
    selected_catg=StringVar(value='Empty')
    catg_box=CTkComboBox(left_frame,values=catg_option,fg_color="white",text_color="black",font=('verdana',20),width=200,state='readonly',variable=selected_catg)

    supplier_option=[]
    selected_supplier=StringVar(value='Empty')
    supplier_box=CTkComboBox(left_frame,values=supplier_option,fg_color="white",text_color="black",font=('verdana',20),width=200,state='readonly',variable=selected_supplier)


    status_option=['select','Active','Inactive']
    selected_status = StringVar(value=status_option[0])
    status_box=CTkComboBox(left_frame,values=status_option,fg_color="white",text_color="black",font=('verdana',20),width=200,state='readonly',variable=selected_status)

    #spinbox
    discount_count = Spinbox(left_frame, from_=0, to=100, font=('verdana', 18),width=11)
    

    #grid
    catg_box.grid(row=0,column=2,padx=10)
    supplier_box.grid(row=2,column=2)
    name_entry.grid(row=3,column=2)
    price_entry.grid(row=4,column=2)
    discount_count.grid(row=5,column=2)
    quantity_entry.grid(row=6,column=2)
    status_box.grid(row=7,column=2)

    #BUTTON FRAME
    btn_frame = CTkFrame(product_frame, fg_color="#161c30")
    btn_frame.place(relx=50/980,rely=500/600)

    CTkButton(btn_frame, text="Add", font=('times new roman', 20, 'bold'), corner_radius=30,fg_color="#b83333",command=add_product).grid(row=0, column=0, padx=10,pady=10)
    CTkButton(btn_frame, text="Update", font=('times new roman', 20, 'bold'), corner_radius=30,fg_color="#b83333",command=update).grid(row=0, column=1, padx=10)
    CTkButton(btn_frame, text="Delete", font=('times new roman', 20, 'bold'), corner_radius=30,fg_color="#b83333",command=delete).grid(row=1, column=0, padx=10,pady=10)
    CTkButton(btn_frame, text="Clear", font=('times new roman', 20, 'bold'), corner_radius=30,fg_color="#b83333",command=reset).grid(row=1, column=1, padx=10)

    #Treeview Frame
    treeview_frame=CTkFrame(product_frame,width=550,height=521,fg_color="red")
    treeview_frame.propagate(0)
    treeview_frame.place(relx=413/980,rely=78/600)

    tree=ttk.Treeview(treeview_frame,height=30,show="headings",selectmode="browse")
    tree.propagate(0)
    # tree.pack(side=LEFT, fill="both", expand=True)
    tree['columns']=('id','category','supplier','name','price','discount','discounted_price','quantity','status')
    tree.heading('id',text='Id')
    tree.heading('category',text="Category")
    tree.heading('supplier',text="Supplier")
    tree.heading('name',text="Name")
    tree.heading('price',text="Price")
    tree.heading('discount',text="Discount")
    tree.heading('discounted_price',text="Discounted Price")
    tree.heading('quantity',text="Quantity")
    tree.heading('status',text="Status")

    # tree.config(show='headings')
    tree.column('id',width=70)
    tree.column('category',width=100)
    tree.column('supplier',width=130)
    tree.column('name',width=200)
    tree.column('price',width=100)
    tree.column('discount',width=120)
    tree.column('discounted_price',width=100)
    tree.column('quantity',width=100)
    tree.column('status',width=100)

    style=ttk.Style()
    style.configure('Treeview.Heading',font=('verdana',12))
    style.configure('Treeview',font=('verdana',12),background="#161c30",foreground="cyan",fieldbackground="green")

    # Create Scrollbars
    ver_scrollbar = Scrollbar(product_frame, orient=VERTICAL)
    hor_scrollbar = Scrollbar(treeview_frame, orient=HORIZONTAL)



    ver_scrollbar.place(relx=963/980,rely=78/600,height=521)
    # hor_scrollbar.place(x=515,y=730,width=692)
    hor_scrollbar.pack(side=BOTTOM, fill=X)
    # ver_scrollbar.pack(side=RIGHT, fill=Y)
    # Attach tree to Scrollbars
    ver_scrollbar.config(command=tree.yview)
    hor_scrollbar.config(command=tree.xview)
    # # Attach scrollbar to tree
    tree.config(yscrollcommand=ver_scrollbar.set)
    tree.config(xscrollcommand=hor_scrollbar.set)
        
    tree.pack(pady=0,side=LEFT,fill=BOTH,expand=1)

    #bind window..to put data when click on row
    tree.bind('<ButtonRelease>',selection)  
    treeview_data()

    fetch_sup_catg()
 
####################################################################################################################################################################################
#FUNCTIONS..............
import PROD_MODEL
P=PROD_MODEL.product()

import PROD_DAO
pdao=PROD_DAO.Product_DAO()

def treeview_data():
    try:
        data = pdao.showall()
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert('', END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data: {e}")


def fetch_sup_catg():
    category,supplier=pdao.fetch_sup_catg()
    
    # Clear old options first
    catg_option.clear()
    supplier_option.clear()
    
    if len(category)>0:
        selected_catg=StringVar(value='Select')
    else:
        selected_catg=StringVar(value='Empty')
    if len(supplier)>0:
        selected_supplier=StringVar(value='Select')
    else:
        selected_catg=StringVar(value='Empty')
  
    for catg in category:
        catg_option.append(catg[0])
    for sup in supplier:
        supplier_option.append(sup[0])
        
    # ✅ Update ComboBox values
    catg_box.configure(values=catg_option,variable=selected_catg)
    supplier_box.configure(values=supplier_option,variable=selected_supplier)
    

def add_product():

        
    if catg_box.get()=='Empty':
        messagebox.showerror("Error","Please Add Categories!")
        return
    if supplier_box.get()=='Empty':
        messagebox.showerror("Error","Please Add Suppliers!")
        return
    
    if catg_box.get()=='Select' or supplier_box.get()=='Select' or name_entry.get()=='' or price_entry.get()=="" or quantity_entry.get()=="" or status_box.get()=="Select":
        messagebox.showerror("Error","All fields are required!")
        return
    
    try:
        price = float(price_entry.get())
        discount = float(discount_count.get())
        quantity = int(quantity_entry.get())
        discounted_price = round(price - (price * discount / 100), 2)
    except ValueError:
        messagebox.showerror("Error", "Invalid number in Price, Discount or Quantity!")
        return
    
    P.setdiscounted_price(discounted_price)
    P.setcategory(catg_box.get())
    P.setsupplier(supplier_box.get())
    P.setname(name_entry.get())
    P.setprice(price_entry.get())
    P.setdiscount(discount_count.get())
    P.setquantity(quantity_entry.get())
    P.setstatus(status_box.get())
    
    check=pdao.already_exist(P)
    if check:
        messagebox.showerror("Error","Product already Exist!")
        return
    else:
        data=pdao.insertproduct(P)
        
        treeview_data()
        if data==True:
            messagebox.showinfo("Inserted","Record Insered Successfully")
        else:
            messagebox.showerror("Error","Something Went Wrong!")

def reset():
    if tree.focus():
        tree.selection_remove(tree.focus())
        
    # Re-fetch Category & Supplier data
    fetch_sup_catg()
    # Clear entries
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    discount_count.delete(0, END)
    discount_count.insert(0, "0")  # Reset discount to 0
    status_box.set("Select")
    
    name_entry.focus()

def showall():
    reset()
    treeview_data()
    search_box.set('Search By')
    search_entry.delete(0,END)
    search_entry.focus()

def search_data():
    if search_box.get()=='Search By':
        messagebox.showerror("Error","Please Select an Option!")
        return
    elif search_entry.get()=="":
        messagebox.showerror('Error',"Enter Value to Search!")
        return
    else:
        data=pdao.search(search_box.get(),search_entry.get())
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert('',END,values=row)
            
def selection(event):
    selected_item=tree.selection()
    print(selected_item)
    row=tree.item(selected_item)['values']
    # print(row)
    reset()
    # role_box
    catg_box.set(row[1])
    supplier_box.set(row[2])
    name_entry.insert(0,row[3])
    price_entry.insert(0,row[4])
    
    discount_count.delete(0,END)
    discount_count.insert(0,row[5])
    
    quantity_entry.insert(0,row[7])
    status_box.set(row[8])
   
        
def update():
  
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Select Data to Update!')
        return
    
    row=tree.item(selected_item)['values']
    product_id=row[0]

    try:
        price = float(price_entry.get())
        discount = float(discount_count.get())
        quantity = int(quantity_entry.get())
        discounted_price = round(price - (price * discount / 100), 2)
    except ValueError:
        messagebox.showerror("Error", "Invalid number in Price, Discount or Quantity!")
        return

    # Set all values in model
    P.setid(product_id)  # ✅ Set ID for update
    P.setdiscounted_price(discounted_price)
    P.setcategory(catg_box.get())
    P.setsupplier(supplier_box.get())
    P.setname(name_entry.get())
    P.setprice(price_entry.get())
    P.setdiscount(discount_count.get())
    P.setquantity(quantity_entry.get())
    P.setstatus(status_box.get())

    ch = pdao.update_data(P)
    if ch == 0:
        messagebox.showinfo('Information', 'No Changes Detected!')
    else:
        treeview_data()
        reset()
        messagebox.showinfo('Update', "Data Updated Successfully!")

            
def delete():
    selected_item = tree.focus()
    print(selected_item)
    if not selected_item:
        messagebox.showerror('Error', 'Select Data to Delete')
        return
    
    row=tree.item(selected_item)['values']
    product_id=row[0]

    ch = messagebox.askyesno('Confirm', 'Are you sure you want to delete this product?')
    if ch:
        pdao.delete_by_id(product_id)
        treeview_data()
        reset()
        messagebox.showinfo('Deleted', "Product deleted successfully!")