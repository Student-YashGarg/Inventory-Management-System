'''SHOPPING DASHBOARD'''

from customtkinter import *
from PIL import Image,ImageTk
from datetime import *
import time

from tkinter import ttk,Scrollbar,messagebox,Text,simpledialog

import PROD_CONNECTION
cur,con = PROD_CONNECTION.connection.getconnection()

#FUNCTION
###############################################################################################################################################################
username="Yash"
count=0
text=""
# ------------------------------
    # Add these global variables here at start
bill = 0
net = 0
total_discount = 0
total_tax = 0
total_bill = 0
invoice = 0
generatebill = False
new_discount = 0
tax_count = 0
    # ------------------------------
def run_dashboard():
    global tax_count
    
    def slider():
        global text,count
        
        # #to run continously 
        # if count==len(t):
        #     count=0
        #     text=""
        
        text=text+t[count]
        slider_label.configure(text=text)
        count+=1
        #loop
        slider_label.after(200,slider)


    def clock():
        global username
        
        currenthour=datetime.now().hour
        if 5<=currenthour<12:
            greeting="Good Morning"
        elif 12<=currenthour<18:
            greeting="Good Afternoon"
        else:
            greeting="Good Evening"

        # admin=username
        current_date=time.strftime("%d/%m/%Y")
        current_time=time.strftime("%I:%M:%S %p")
        
        date_time_label.configure(text=f"{greeting} {username}!\t\t\tDate:- {current_date}\t\t\tTime:- {current_time}")
        #loop
        date_time_label.after(1000,clock)

    def treeview_data():
        cur.execute("SELECT id,name,price,quantity,status FROM PRODUCT_DATA WHERE status='active' ORDER BY id") 
        data=cur.fetchall()
        tree.delete(*tree.get_children())
        for row in data:
            tree.insert('', END, values=row)
    tax_count=0   
    def tax():
        global tax_count
        import MySQLdb
        try:
            con = MySQLdb.connect(host="localhost", user="root", password="YASH@3315",database='INVENTORY_MANAGEMENT')
            cur = con.cursor()
            cur.execute("USE INVENTORY_MANAGEMENT")
            cur.execute("select tax from tax_table where id=1")
            result=cur.fetchone()
            
            tax_count=int(result[0])
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")
            print(e)
            return
            
    new_discount=0
    def set_discount():
        global new_discount
        if cart_tree.get_children():
            messagebox.showerror("Error","Please Clear Cart first!")
            return
        new_discount=simpledialog.askinteger('Discount',"Enter Net.Discount: ")
        
        discount_count.configure(state='normal')
        discount_count.delete(0,END)
        discount_count.insert(0,new_discount)
        discount_count.configure(state='readonly')
        
        messagebox.showinfo("Updated",f"Net Discount is Set to {new_discount} % Successfully.")
        
    bill=0
    net=0
    total_discount=0
    total_tax=0
    total_bill=0

    def bill_caclculate():
        global bill,net,total_discount,new_discount,total_tax,total_bill
        bill=0
        for row in cart_data_list:
            bill=bill+float(row[4])
            
        total_discount=((bill*new_discount)/100)
        
        tax()
        net=bill-total_discount
        total_tax=((net*tax_count)/100)
        total_bill=net+total_tax
        
        bill=round(bill,2)
        total_discount=round(total_discount,2)
        net=round(net,2)
        total_tax=round(total_tax,2)
        total_bill=round(total_bill)
        
        bill_count.configure(text=f'{bill}') 
        net_count.configure(text=f'{net}')
        cart_title.configure(text=f'CART | Total Products: {str(len(cart_data_list))}')

    cart_data_list = []

    def cart_treeview_data():
        global generatebill
        if generatebill:
            messagebox.showerror("Error","Please clear all the field before adding a new one.")
            return 
        if productname_entry.get() == "" or price_entry.get() == "":
            messagebox.showerror("Error", "Please select product!")
            return
        elif quantity_entry.get() == '':
            messagebox.showerror("Error", "Please Enter Quantity!")
            return
        elif discount_count.get()=="":
            messagebox.showerror('Error',"Please Set Net Discount! ")
            set_discount()
                
        try:
            # Calculate price
            price = float(price_entry.get())
            quantity = int(quantity_entry.get())
            cart_price = price * quantity

            # Safely get product_id
            selected_item = cart_tree.focus()
            if selected_item:
                row = cart_tree.item(selected_item)['values']
                if row: product_id = row[0]
                
                if quantity>row[5]:
                    messagebox.showerror("Error","Quantity is more than Stock!")
                    return
                if quantity<0:
                    messagebox.showerror("Error","Invalid Quantity!")
                    return
            else:
                selected_item = tree.focus()
                if selected_item:
                    row = tree.item(selected_item)['values']
                    if row: product_id = row[0]
                    
                    if quantity>row[3]:
                        messagebox.showerror("Error","Quantity is more than Stock!")
                        return
                    if quantity<=0:
                        messagebox.showerror("Error","Invalid Quantity!")
                        return
                else:
                    messagebox.showerror("Error", "Please select a product!")
                    return

        except Exception as obj:
            print(obj)
            messagebox.showerror("Error", "Invalid Quantity!")
            return
        #stock
        stock=str(row[3])
        # New row to be added
        row = [product_id, productname_entry.get(),price, quantity_entry.get(),cart_price,stock]

        # Check if already present
        present = False
        for i in range(len(cart_data_list)):
            if product_id == cart_data_list[i][0]:
                present = True
                break

        # If present, ask to update
        if present:
            messagebox.showinfo("Info", f"{productname_entry.get()} already added")
            choice = messagebox.askyesno("Confirm", "Do you want to Update?")
            if choice:
                if quantity_entry.get() == '0':
                    cart_data_list.pop(i)
                    
                else:
                    cart_data_list[i] = row  # update existing entry
        else:
            cart_data_list.append(row)  # only add if not already present

        show_cart_treeview_data()
        bill_caclculate()

    def show_cart_treeview_data():
        cart_tree.delete(*cart_tree.get_children())
        for row in cart_data_list:
            cart_tree.insert('',END,value=row)

        
    def selection(event):
        selected_item=tree.selection()
        row=tree.item(selected_item)['values']
        
        # reset() 
        productname_entry.configure(state='normal')   
        price_entry.configure(state='normal')
        
        productname_entry.delete(0,END)
        price_entry.delete(0,END)
        
        productname_entry.insert(0,row[1])
        price_entry.insert(0,row[2])
        
        productname_entry.configure(state='readonly')
        price_entry.configure(state='readonly')
        
        stock_count.configure(text=f"{str(row[3])}")
        
        quantity_entry.delete(0,END)
        quantity_entry.insert(0,1)
        
    def cart_selection(event):
        selected_item=cart_tree.selection()
        row=cart_tree.item(selected_item)['values']
        # print(row)
        # reset()    
        productname_entry.configure(state='normal')   
        price_entry.configure(state='normal')
        
        productname_entry.delete(0,END)
        price_entry.delete(0,END)
        
        productname_entry.insert(0,row[1])
        price_entry.insert(0,row[2])
        
        productname_entry.configure(state='readonly')
        price_entry.configure(state='readonly')
        
        quantity_entry.delete(0,END)
        quantity_entry.insert(0,row[3])
        stock_count.configure(text=f"{str(row[5])}")
        
        # cart_treeview_data()

    def showall():
        product_entry.delete(0,END)
        treeview_data()

    def search():
        if product_entry.get()=="":
            messagebox.showerror("Error","Please Insert Product Name!")
            return
        cur.execute("SELECT id, name, price, quantity, status FROM PRODUCT_DATA WHERE name LIKE %s", (f"%{product_entry.get()}%",))
        data=cur.fetchall()
        
        tree.delete(*tree.get_children())
        if data:
            for row in data:
                tree.insert('',END,values=row)
        else:
            messagebox.showerror("Error",f"{product_entry.get()} is Not found!")
            return
        

    def reset():
        if tree.focus():
            tree.selection_remove(tree.focus())
        if cart_tree.focus():
            cart_tree.selection_remove(cart_tree.focus())
        
        productname_entry.configure(state='normal')   
        price_entry.configure(state='normal')
        productname_entry.delete(0,END)
        price_entry.delete(0,END)
        productname_entry.configure(state='readonly')
        price_entry.configure(state='readonly')
        
        stock_count.configure(text='')
        quantity_entry.delete(0,END)
        


    def clear_all():
        global bill,net,total_bill,total_discount,total_tax,invoice,generatebill
        
        customer_name_entry.delete(0,END)
        contact_entry.delete(0,END)
        
        for item in cart_tree.get_children():
            cart_tree.delete(item)
        cart_data_list.clear()
        cart_title.configure(text=f'CART | Total Products: 0')
        
        bill_count.configure(text='0')
        net_count.configure(text='0')
        
        bill_text.delete(1.0,END)
        
        bill = net = total_discount = total_tax = total_bill = invoice = 0

        generatebill=False
        reset()
        

    generatebill=False
    def generate_bill():
        global generatebill

        if customer_name_entry.get()=='' or contact_entry.get()=='':
            messagebox.showerror("Error","Customer Details are Required!")
            return
        elif len(cart_data_list)==0:
            messagebox.showerror("Error","Please Add Products in cart!")
        
        elif generatebill:
            messagebox.showerror("Error","Please clear the current bill before generating a new one.")
            return  
        else:
            bill_text.delete(1.0,END)
            bill_top()
            bill_middle()
            bill_down()
            save_bill()
                
        
    invoice=0
    def bill_top():
        global invoice
        import random
        invoice ='INV'+time.strftime("%d%m%H%M") + str(random.randint(100, 999)) #get uinque invoice always..

        bill_text.delete(1.0,END)
        bill_text.insert(END,"\t        ****IMS BY ¥∆$# ₲@₹₲****\n")
        bill_text.insert(END,"\t    Con.  7078771255 , Mur.(201206)")
        bill_text.insert(END,f"\n{str('-'*67)}")
        bill_text.insert(END,f"\nBill No. : {str(invoice)}\t\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}")
        bill_text.insert(END,f"\nCustomer Name: {str(customer_name_entry.get())}")
        bill_text.insert(END,f"\nPhone No. : {str(contact_entry.get())}")
        bill_text.insert(END,f"\n\n{str('='*37)}")
        bill_text.insert(END,f"\n\tProduct Name\t\tQTY\tPrice(Rs.))")
        bill_text.insert(END,f"\n{str('='*37)}")

    def bill_middle():
        import MySQLdb
        try:
            con = MySQLdb.connect(
                host="localhost", user="root", password="YASH@3315", database='INVENTORY_MANAGEMENT'
            )
            cur = con.cursor()

            for row in cart_data_list:
                name = row[1]
                qty = str(row[3])
                price = str(row[4])

                # Insert into bill text area
                bill_text.insert(END, f"\n\t{name}\t\t{qty}\t{price}")

                # Update stock and status
                pid = row[0]
                current_stock = int(row[5])
                quantity_purchased = int(row[3])
                updated_stock = current_stock - quantity_purchased
        

                status = 'Inactive' if quantity_purchased==current_stock else 'Active'

                cur.execute(
                    "UPDATE PRODUCT_DATA SET quantity=%s, status=%s WHERE id=%s",
                    (updated_stock, status, pid)
                )

            con.commit()
            con.close()
            treeview_data()

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")
            print(e)
            return

    def bill_down():
        global generatebill,bill,total_discount,new_discount,total_bill,net,tax_count,total_tax

        bill_text.insert(END,f"\n{str('-'*67)}")
        bill_text.insert(END,f"\n\nBill Amount:\t\t\t{bill} Rs.")
        bill_text.insert(END,f"\nDiscount:\t\t{new_discount}%\t{total_discount}  Rs.")
        bill_text.insert(END,f"\nNet Amount:\t\t\t{net} Rs.")
        bill_text.insert(END,f"\n\nNet GST:\t\t{tax_count}%\t{total_tax} Rs\n")
        bill_text.insert(END,f"\n{str('='*37)}")
        bill_text.insert(END,f"\nTOTAL PAY:\t\t\t\t{total_bill}  Rs.")
        bill_text.insert(END,f"\n{str('='*37)}")
        
        bill = net = total_discount = total_tax = total_bill = 0
        generatebill=True
  

    def save_bill():
        global invoice
        ch=messagebox.askyesno("Conform","Do you want to Save Bill?")
        if ch:
            filename=f'Bills/{invoice}.txt'
            bill_data=bill_text.get(1.0,END)
            try:
                with open(filename,'w',encoding="utf-8") as f:
                    f.write(bill_data)
            except Exception as e:
                messagebox.showerror('Error','Something Went Wrong!')
                print(e)
                return
            messagebox.showinfo("Saved",f'Bill {invoice} has been Saved Successfully!')

    def print_bill():
        import tempfile
        
        if bill_text.get(1.0, END).strip() == '':
            messagebox.showerror('Error', 'Bill is not generated yet!')
            return

        try:
            # Create a temporary file to hold the bill content
            temp_file = tempfile.mktemp('.txt')
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(bill_text.get(1.0, END))

            # Send the file to the printer
            os.startfile(temp_file, 'print')
        except Exception as e:
            messagebox.showerror("Print Error", f"Could not print bill.\n{e}")

    def logout():
        myroot.destroy()
        os.system("python LOGIN_MAIN_FORM.py")

            
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #ROOT
    myroot=CTk()
    myroot.geometry('1260x680')
    myroot.resizable(0,0)
    myroot.config(bg="#ebf5fb")
    myroot.title("IMS BY ¥∆$# ₲@₹₲")
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #HEADING SECTION
    image=Image.open("IMS_heading_img.png")
    iconimg=ImageTk.PhotoImage(image=image)

    t="Inventory Managment System"
    slider_label=CTkLabel(myroot,text=t,font=('times new roman',45),fg_color="#010c48",anchor="center",text_color="white")
    slider_label.place(relx=0,rely=0,relwidth=1)
    slider()

    CTkLabel(myroot,image=iconimg,fg_color="#010c48",anchor='w',padx=40,text="").place(relx=40/1260,rely=0)
    CTkButton(myroot,text="Logout",font=('times new roman',20,'bold'),cursor="hand2",bg_color="#010c48",text_color="white",command=logout).place(x=1095,y=10)
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #DATE TIME
    date_time_label=CTkLabel(myroot,fg_color="#005271",font=('Times new roman',20),anchor="center",text_color="white")
    date_time_label.place(x=0,y=50,relwidth=1)
    clock()

    discount_btn_btn=CTkButton(myroot,text="Add/Update Discount",font=('verdana',18),corner_radius=30,width=90,command=set_discount,bg_color="#ebf5fb",text_color="white")
    discount_btn_btn.place(x=1010,y=80)
    tax()
    CTkLabel(myroot,text=f"NOTE: Enter 0 Quantity to remove product from the cart. | TAX = {tax_count}%",text_color="red",fg_color='#ebf5fb').place(relx=420/1260,rely=80/680)

    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #PRODUCT FRAME
    product_frame=CTkFrame(myroot,width=360,height=550)
    product_frame.propagate(0)
    product_frame.place(relx=18/1260,rely=110/680)

    CTkLabel(product_frame,text="All Products",font=('verdana',14,'bold'),anchor='center',fg_color="#b83333",text_color="white").pack(side=TOP,fill=X)

    search_frame=CTkFrame(product_frame,height=90,fg_color="white",corner_radius=0,border_width=1,border_color="black")
    search_frame.pack(side=TOP,fill=X)

    CTkLabel(search_frame,text="Product Name",font=('verdana',18,'bold'),text_color="black").place(x=15,y=10)

    product_entry=CTkEntry(search_frame,fg_color="white",text_color="black",font=('verdana',18),height=20,width=170)
    product_entry.place(x=170,y=12)

    search_btn=CTkButton(search_frame,text="Search",font=('verdana',18),corner_radius=30,width=90,command=search,fg_color='#b83333',text_color="white")
    search_btn.place(x=80,y=50)

    showall_btn=CTkButton(search_frame,text="Showall",font=('verdana',18),corner_radius=30,width=90,command=showall,fg_color="#b83333",text_color="white")
    showall_btn.place(x=190,y=50)

    #Treeview Frame
    treeview_frame=CTkFrame(product_frame,width=550,height=535,border_width=1,border_color="black")
    treeview_frame.propagate(0)
    # treeview_frame.place(x=410,y=78)
    treeview_frame.pack(side=TOP ,fill=BOTH)

    tree=ttk.Treeview(treeview_frame,height=31,show="headings",selectmode="browse")
    # tree.pack(side=LEFT, fill="both", expand=True)
    tree['columns']=('id','name','price','quantity','status')
    tree.heading('id',text='Id')
    tree.heading('name',text="Name")
    tree.heading('price',text="Price")
    tree.heading('quantity',text="Quantity")
    tree.heading('status',text="Status")

    # tree.config(show='headings')
    tree.column('id',width=70)
    tree.column('name',width=200)
    tree.column('price',width=100)
    tree.column('quantity',width=100)
    tree.column('status',width=100)

    style=ttk.Style()
    style.configure('Treeview.Heading',font=('verdana',12))
    style.configure('Treeview',font=('verdana',11),background="#161c30",foreground="cyan",fieldbackground="green")

    # Create Scrollbars
    ver_scrollbar = Scrollbar(product_frame, orient=VERTICAL)
    hor_scrollbar = Scrollbar(treeview_frame, orient=HORIZONTAL)
    #place scroolbars
    ver_scrollbar.place(relx=345/360,rely=118/550,height=418)
    hor_scrollbar.pack(side=BOTTOM, fill=X)

    # Attach tree to Scrollbars
    ver_scrollbar.config(command=tree.yview)
    hor_scrollbar.config(command=tree.xview)

    # # Attach scrollbar to tree
    tree.config(yscrollcommand=ver_scrollbar.set)
    tree.config(xscrollcommand=hor_scrollbar.set)

    tree.pack(pady=0,side=LEFT,fill=BOTH,expand=1)

    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #CUSTOMER FRAME
    customer_frame=CTkFrame(myroot,width=488,height=550)
    customer_frame.propagate(0)
    customer_frame.place(x=385,y=110)

    CTkLabel(customer_frame,text="Customer Billing Area",font=('verdana',14,'bold'),anchor='center',fg_color="#2471a3",text_color="white").pack(side=TOP,fill=X)
    #-------------------------------------------------------------------------------------------------------------------------------------------------------
    first_frame=CTkFrame(customer_frame,height=50,fg_color="white",corner_radius=0,border_width=1,border_color="black")
    first_frame.pack(side=TOP,fill=X)

    CTkLabel(first_frame,text="Name",font=('verdana',14,'bold'),text_color="black").place(x=15,y=10)

    customer_name_entry=CTkEntry(first_frame,fg_color="white",text_color="black",font=('verdana',18),height=20,width=150)
    customer_name_entry.place(x=70,y=12)

    CTkLabel(first_frame,text="Contact No.",font=('verdana',14,'bold'),text_color="black").place(x=226,y=10)

    contact_entry=CTkEntry(first_frame,fg_color="white",text_color="black",font=('verdana',18),height=20,width=150)
    contact_entry.place(x=325,y=10)
    #-------------------------------------------------------------------------------------------------------------------------------------------------------
    second_frame=CTkFrame(customer_frame,height=350,fg_color="white",corner_radius=0,border_width=1,border_color="black")
    second_frame.pack(side=TOP,fill=X)

    calc_frame=CTkFrame(second_frame,height=351,width=244,fg_color="white",corner_radius=0,border_width=1,border_color="black")
    calc_frame.propagate(0)
    calc_frame.place(x=0,y=0)

    CTkLabel(calc_frame,text="Calculator",font=('verdana',14,'bold'),anchor='center',fg_color="#2471a3",text_color="red").pack(side=TOP,fill=X)
    from CALC import calculator
    calculator(calc_frame)

    cart_treeview_frame=CTkFrame(second_frame,height=350,width=243,fg_color="green",corner_radius=0,border_width=1,border_color="black")
    cart_treeview_frame.pack_propagate(0)
    cart_treeview_frame.place(x=244)

    cart_title=CTkLabel(cart_treeview_frame,text="CART | Total Products: 0",font=('verdana',14,'bold'),anchor='center',fg_color="#2471a3",text_color="white")
    cart_title.pack(side=TOP,fill=X)

    cart_tree=ttk.Treeview(cart_treeview_frame,height=15,show="headings",selectmode="browse")
    # tree.pack(side=LEFT, fill="both", expand=True)
    cart_tree['columns']=('id','name','price','quantity')
    cart_tree.heading('id',text='Id')
    cart_tree.heading('name',text="Name")
    cart_tree.heading('price',text="Price")
    cart_tree.heading('quantity',text="Quantity")
    # cart_tree.heading('status',text="Status")

    # tree.config(show='headings')
    cart_tree.column('id',width=70)
    cart_tree.column('name',width=200)
    cart_tree.column('price',width=100)
    cart_tree.column('quantity',width=100)
    # cart_tree.column('status',width=100)

    style=ttk.Style()
    style.configure('Treeview.Heading',font=('verdana',12))
    style.configure('Treeview',font=('verdana',11),background="#161c30",foreground="cyan",fieldbackground="green")

    # Create Scrollbars
    ver_scrollbar = Scrollbar(second_frame, orient=VERTICAL)
    hor_scrollbar = Scrollbar(cart_treeview_frame, orient=HORIZONTAL)
    #place scroolbars
    ver_scrollbar.place(x=470,rely=29/350,height=305)
    hor_scrollbar.pack(side=BOTTOM, fill=X)

    # Attach tree to Scrollbars
    ver_scrollbar.config(command=cart_tree.yview)
    hor_scrollbar.config(command=cart_tree.xview)

    # # Attach scrollbar to tree
    cart_tree.config(yscrollcommand=ver_scrollbar.set)
    cart_tree.config(xscrollcommand=hor_scrollbar.set)

    cart_tree.pack(pady=0,side=TOP,fill=BOTH,expand=1)

    #--------------------------------------------------------------------------------------------------------------------------
    third_frame=CTkFrame(customer_frame,height=130,fg_color="white",corner_radius=0,border_width=1,border_color="black")
    third_frame.pack(side=TOP,fill=X)

    CTkLabel(third_frame,text="Product Name",font=('verdana',14,'bold'),text_color="black").place(x=25,y=10)
    CTkLabel(third_frame,text="Price",font=('verdana',14,'bold'),text_color="black").place(x=210,y=10)
    CTkLabel(third_frame,text="Quantity",font=('verdana',14,'bold'),text_color="black").place(x=360,y=10)

    #Entry
    productname_entry=CTkEntry(third_frame,fg_color="white",text_color="black",font=('verdana',18),height=20,width=150,state='readonly')
    productname_entry.place(x=25,y=40)
    price_entry=CTkEntry(third_frame,fg_color="white",text_color="black",font=('verdana',18),height=20,width=120,state='readonly')
    price_entry.place(x=210,y=40)
    quantity_entry=CTkEntry(third_frame,fg_color="white",text_color="black",font=('verdana',18),height=20,width=100)
    quantity_entry.place(x=360,y=40)

    CTkLabel(third_frame,text="In Stock:",font=('verdana',14,'bold'),text_color="black").place(x=20,y=80)
    stock_count=CTkLabel(third_frame,text="",font=('verdana',15,'bold'),text_color="#D68910")
    stock_count.place(x=100,y=80)

    clear_btn=CTkButton(third_frame,text="Clear",font=('verdana',18),corner_radius=30,width=90,command=reset,text_color="white")
    clear_btn.place(x=190,y=80)
    add_update_btn=CTkButton(third_frame,text="Add/Update Cart",font=('verdana',18),corner_radius=30,width=90,command=cart_treeview_data,text_color="white")
    add_update_btn.place(x=290,y=80)
    #----------------------------------------------------------------------------------------------------------------------------------------------------
    #BILL FRAME
    bill_frame=CTkFrame(myroot,width=360,height=550)
    bill_frame.propagate(0)
    bill_frame.place(relx=880/1260,rely=110/680)

    CTkLabel(bill_frame,text="Customer Billing Area",font=('verdana',14,'bold'),anchor='center',fg_color="#D68910",text_color="white").pack(side=TOP,fill=X)

    textbox_frame=CTkFrame(bill_frame,height=410,fg_color="white",corner_radius=0,border_width=1,border_color="black")
    textbox_frame.propagate(0)
    textbox_frame.pack(side=TOP,fill=X)

    ver_scrollbar = Scrollbar(textbox_frame, orient=VERTICAL)
    bill_text=Text(textbox_frame,font=('verdana',8),yscrollcommand=ver_scrollbar.set,wrap="word",bg="#161c30",fg="white",height=10)  
    ver_scrollbar.pack(side=RIGHT, fill=Y)
    # ver_scrollbar.place(x=80,rely=29/100,height=100)
    ver_scrollbar.config(command=bill_text.yview)
    bill_text.pack(fill=BOTH,expand=True)

    button_frame=CTkFrame(bill_frame,height=140,fg_color="white",corner_radius=0,border_width=1,border_color="black")
    button_frame.propagate(0)
    button_frame.pack(side=TOP,fill=X)



    CTkLabel(button_frame,text="Bill Amount(Rs.)",font=('verdana',13,'bold'),text_color="black").place(x=15,y=8)
    CTkLabel(button_frame,text="Discount(%)",font=('verdana',13,'bold'),text_color="black").place(x=150,y=8)
    CTkLabel(button_frame,text="Net Amt.(Rs.)",font=('verdana',13,'bold'),text_color="black").place(x=255,y=8)

    bill_count=CTkLabel(button_frame,text="0",font=('verdana',15,'bold'),text_color="#2874a6")
    bill_count.place(x=30,rely=40/140)
    # discount_count=CTkLabel(button_frame,text="Empty",font=('verdana',15,'bold'),text_color="#0C7E55")
    # discount_count.place(x=170,y=30)
    discount_count=CTkEntry(button_frame,fg_color="white",text_color="green",font=('verdana',14,'bold'),height=20,width=50,state='readonly')
    discount_count.place(x=160,rely=40/140)
    net_count=CTkLabel(button_frame,text="0",font=('verdana',15,'bold'),text_color="#DC3131")
    net_count.place(x=260,rely=40/140)

    clearall_btn=CTkButton(button_frame,text="Clear All",font=('verdana',18),corner_radius=30,width=90,fg_color="#D68910",text_color="white",command=clear_all)
    clearall_btn.place(x=5,rely=90/140)
    print_btn=CTkButton(button_frame,text="Print",font=('verdana',18),corner_radius=30,width=90,fg_color="#D68910",text_color="white",command=print_bill)
    print_btn.place(x=114,rely=90/140)
    generate_btn=CTkButton(button_frame,text="Gen./Save Bill",font=('verdana',13,'bold'),corner_radius=30,width=100,fg_color="coral2",text_color="white",command=generate_bill)
    generate_btn.place(x=210,rely=90/140)

    #----------------------------------------------------------------------------------------------------------------------------------------------------
    tree.bind('<ButtonRelease>',selection)
    cart_tree.bind('<ButtonRelease>',cart_selection) 
    treeview_data()

    # show_cart_treeview_data()
    myroot.mainloop()

if __name__ == "__main__":
    run_dashboard()