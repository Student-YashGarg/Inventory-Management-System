'''IMS DASHBOARD'''

from customtkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from datetime import *
import time
import os


from EMPLOYEE import employee_form
from SUPPLIER import supplier_form
from CATEGORY import category_form
from PRODUCT import product_form
from SALES import sales_form
from TAX import tax_form

import EMP_DAO
import SUP_DAO
import CAT_DAO
import PROD_DAO
edao=EMP_DAO.Employee_DAO()
sdao=SUP_DAO.Supplier_DAO()
cdao=CAT_DAO.Category_DAO()
pdao=PROD_DAO.Product_DAO()

admin_name="Yash"
count=0
text=""
def run_dashboard():

    #FUNCTION
    ###############################################################################################################################################################
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
        global admin_name

        currenthour=datetime.now().hour
        if 5<=currenthour<12:
            greeting="Good Morning"
        elif 12<=currenthour<18:
            greeting="Good Afternoon"
        else:
            greeting="Good Evening"
            
        current_date=time.strftime("%d/%m/%Y")
        current_time=time.strftime("%I:%M:%S %p")
        
        date_time_label.configure(text=f"{greeting} {admin_name}!\t\t\tDate:- {current_date}\t\t\tTime:- {current_time}")
        #loop
        date_time_label.after(1000,clock)

    def total_sales():
        import os
        sales=0
        for i in os.listdir('Bills'):
            sales+=1
        return sales

    def exit():
        conform=messagebox.askyesno("Conform Exit","Are you sure want to Exit?")
        if conform:
            myroot.destroy()

    def update_count():
        print("update count")
        emp_count.configure(text=str(edao.get_employee_count()))
        sup_count.configure(text=str(sdao.get_supplier_count()))
        catg_count.configure(text=str(cdao.get_category_count()))
        prod_count.configure(text=str(pdao.get_product_count()))
        sales_count.configure(text=str(total_sales()))
    
    def logout():
        myroot.destroy()
        os.system("python LOGIN_MAIN_FORM.py")
    ###################################################################################################################################################################################
        
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #ROOT
    myroot=CTk()
    myroot.geometry('1260x680')
    myroot.resizable(0,0)
    myroot.config(bg="white")
    myroot.title("IMS BY ¥∆$# ₲@₹₲")
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #HEADING SECTION
    image=Image.open("IMS_heading_img.png")
    iconimg=ImageTk.PhotoImage(image=image)

    t="Inventory Managment System"
    slider_label=CTkLabel(myroot,text=t,font=('times new roman',45),fg_color="#010c48",anchor="center",text_color="white")
    slider_label.place(x=0,y=0,relwidth=1)
    slider()

    CTkLabel(myroot,image=iconimg,fg_color="#010c48",anchor='w',padx=40,text="").place(relx=40/1260,rely=0)
    CTkButton(myroot,text="Logout",font=('times new roman',20,'bold'),cursor="hand2",bg_color="#010c48",text_color="white",command=logout).place(relx=1095/1260,rely=10/680)
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #DATE TIME
    date_time_label=CTkLabel(myroot,fg_color="#005271",font=('Times new roman',20),anchor="center",text_color="white")
    date_time_label.place(x=0,rely=50/680,relwidth=1)
    clock()

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #LEFT FRAME SECTION
    left_frame=CTkFrame(myroot,height=550,width=200,fg_color="white",bg_color="white")
    left_frame.place(relx=35/1260,rely=120/680)

    image=Image.open("freepik__upload__22257.jpeg")
    image=image.resize((250,200),Image.LANCZOS)
    invent_img=ImageTk.PhotoImage(image=image)

    CTkLabel(left_frame,image=invent_img,text='').place(x=0,y=0)
    CTkLabel(left_frame,text="Menu",font=('Verdana',22),fg_color="blue",text_color="white").place(x=0,y=160,relwidth=1)

    image=Image.open("Employee.ico")
    Emp_img=ImageTk.PhotoImage(image=image)
    CTkButton(left_frame,image=Emp_img,text="Employees",font=('Verdana',25),anchor='w',command=lambda:employee_form(myroot,update_count),text_color="white").place(x=0,y=200,relwidth=1)

    image=Image.open("supplier1.ico")
    sup_img=ImageTk.PhotoImage(image=image)
    CTkButton(left_frame,image=sup_img,text="  Supplier",font=('Verdana',25),anchor='w',command=lambda:supplier_form(myroot,update_count),text_color="white").place(x=0,y=250,relwidth=1)

    image=Image.open("category1.ico")
    catg_img=ImageTk.PhotoImage(image=image)
    CTkButton(left_frame,image=catg_img,text="Category",font=('Verdana',25),command=lambda:category_form(myroot,update_count),text_color="white").place(x=0,y=300,relwidth=1)

    image=Image.open("product1.ico")
    prod_img=ImageTk.PhotoImage(image=image)
    CTkButton(left_frame,image=prod_img,text="Product",font=('Verdana',25),command=lambda:product_form(myroot,update_count),text_color="white").place(x=0,y=350,relwidth=1)

    image=Image.open("Sales.ico")
    sales_img=ImageTk.PhotoImage(image=image)
    CTkButton(left_frame,image=sales_img,text="Sales",font=('Verdana',25),command=lambda:sales_form(myroot,update_count),text_color="white").place(x=0,y=400,relwidth=1)

    image=Image.open("tax.ico")
    tax_img=ImageTk.PhotoImage(image=image)
    CTkButton(left_frame,image=tax_img,text="Tax",font=('Verdana',25),command=lambda:tax_form(myroot),text_color="white").place(x=0,y=450,relwidth=1)


    image=Image.open("exit.ico")
    exit_img=ImageTk.PhotoImage(image=image)
    CTkButton(left_frame,image=exit_img,text="Exit",font=('Verdana',25),command=exit,text_color="white").place(x=0,y=500,relwidth=1)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #TOTAL EMPLOYEES
    image=Image.open("Temployees.png")
    image=image.resize((250,180),Image.LANCZOS)
    temp_img=ImageTk.PhotoImage(image=image)
    CTkLabel(myroot,image=temp_img,fg_color="white",text='').place(relx=420/1260,rely=80/680)
    CTkLabel(myroot,text="Total Employees",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=410/1260,rely=200/680)

    emp_count=CTkLabel(myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="blue",anchor="center",height=70,width=200)
    emp_count.place(relx=440/1260,rely=240/680)

    #TOTAL SUPPLIERS
    image=Image.open("Tsupplier.png")
    image=image.resize((250,120),Image.LANCZOS)
    tsup_img=ImageTk.PhotoImage(image=image)
    CTkLabel(myroot,image=tsup_img,fg_color="white",text='').place(relx=820/1250,rely=90/680)
    CTkLabel(myroot,text="Total Suppliers",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=830/1260,rely=200/680)

    sup_count=CTkLabel(myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="green",anchor="center",height=70,width=200,bg_color="white")
    sup_count.place(relx=850/1260,rely=240/680)

    #TOTAL CATEGORY
    image=Image.open("Tcategory.png")
    image=image.resize((200,150),Image.LANCZOS)
    tcat_img=ImageTk.PhotoImage(image=image)
    CTkLabel(myroot,image=tcat_img,fg_color="white",text='').place(relx=440/1260,rely=300/680)
    CTkLabel(myroot,text="Total Category",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(x=425,y=440)

    catg_count=CTkLabel(myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="violet",anchor="center",height=70,width=200,bg_color="white")
    catg_count.place(relx=440/1260,rely=480/680)

    #TOTAL PRODUCTS
    image=Image.open("Tproduct.png")
    image=image.resize((250,120),Image.LANCZOS)
    tprod_img=ImageTk.PhotoImage(image=image)
    CTkLabel(myroot,image=tprod_img,fg_color="white",text='').place(relx=850/1260,rely=320/680)
    CTkLabel(myroot,text="Total Products",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=840/1260,rely=440/680)

    prod_count=CTkLabel(myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="orange",anchor="center",height=70,width=200,bg_color="white")
    prod_count.place(relx=860/1260,rely=480/680)

    #TOTAL SALES
    image=Image.open("Tsales.png")
    image=image.resize((250,120),Image.LANCZOS)
    tsales_img=ImageTk.PhotoImage(image=image)
    CTkLabel(myroot,image=tsales_img,fg_color="white",text='').place(relx=630/1260,rely=490/680)
    CTkLabel(myroot,text="Total Sales",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=660/1260,rely=580/680)

    sales_count=CTkLabel(myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="#d32d41",anchor="center",height=70,width=200,bg_color="white")
    sales_count.place(relx=660/1260,rely=610/680)

    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    update_count()

    myroot.mainloop()


if __name__ == "__main__":
    run_dashboard()