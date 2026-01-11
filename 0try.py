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

class Ims_run:

#FUNCTION
###############################################################################################################################################################


    def slider(self):
        if self.count == len(self.t):
            pass
            #TO RUN CONTINOUSLY
            # self.count = 0
            # self.text = ""   # reset when finished
             
        self.text=self.text+self.t[self.count]
        self.slider_label.configure(text=self.text)
        self.count+=1
        #loop
        self.slider_label.after(200,self.slider)

    def clock(self,admin_name):
        currenthour=datetime.now().hour
        if 5<=currenthour<12:
            greeting="Good Morning"
        elif 12<=currenthour<18:
            greeting="Good Afternoon"
        else:
            greeting="Good Evening"
            
        admin=admin_name
        current_date=time.strftime("%d/%m/%Y")
        current_time=time.strftime("%I:%M:%S %p")
        
        self.date_time_label.configure(text=f"{greeting} {admin}!\t\t\tDate:- {current_date}\t\t\tTime:- {current_time}")
        #loop
        self.date_time_label.after(1000,lambda: self.clock(self.admin))

    def total_sales(self):
        import os
        sales=0
        for i in os.listdir('Bills'):
            sales+=1
        return sales

    def exit(self):
        conform=messagebox.askyesno("Conform Exit","Are you sure want to Exit?")
        if conform:
            self.myroot.destroy()

    def update_count(self):
        print("update count")
        self.emp_count.configure(text=str(edao.get_employee_count()))
        self.sup_count.configure(text=str(sdao.get_supplier_count()))
        self.catg_count.configure(text=str(cdao.get_category_count()))
        self.prod_count.configure(text=str(pdao.get_product_count()))
        
        self.sales_count.configure(text=str(self.total_sales()))

    def logout(self):
        self.myroot.destroy()
        os.system("python LOGIN_MAIN_FORM.py")
    
###################################################################################################################################################################################

    def __init__(self,admin='Yash'):
        self.admin=admin
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #ROOT
        self.myroot=CTk()
        self.myroot.geometry('1260x680')
        self.myroot.resizable(0,0)
        self.myroot.config(bg="white")
        self.myroot.title("IMS BY ¥∆$# ₲@₹₲")
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #HEADING SECTION
        image=Image.open("IMS_heading_img.png")
        iconimg=ImageTk.PhotoImage(image=image)

        self.count = 0
        self.text = ""
        self.t="Inventory Managment System"
        
        self.slider_label=CTkLabel(self.myroot,text=self.t,font=('times new roman',45),fg_color="#010c48",anchor="center",text_color="white")
        self.slider_label.place(x=0,y=0,relwidth=1)
        self.slider()

        CTkLabel(self.myroot,image=iconimg,fg_color="#010c48",anchor='w',padx=40,text="").place(relx=40/1260,rely=0)
        CTkButton(self.myroot,text="Logout",font=('times new roman',20,'bold'),cursor="hand2",bg_color="#010c48",text_color="white",command=self.logout).place(relx=1095/1260,rely=10/680)
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #DATE TIME
        self.date_time_label=CTkLabel(self.myroot,fg_color="#005271",font=('Times new roman',20),anchor="center",text_color="white")
        self.date_time_label.place(x=0,rely=50/680,relwidth=1)
        self.clock(self.admin)

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #LEFT FRAME SECTION
        left_frame=CTkFrame(self.myroot,height=550,width=200,fg_color="white",bg_color="white")
        left_frame.place(relx=35/1260,rely=120/680)

        image=Image.open("freepik__upload__22257.jpeg")
        image=image.resize((250,200),Image.LANCZOS)
        invent_img=ImageTk.PhotoImage(image=image)

        CTkLabel(left_frame,image=invent_img,text='').place(x=0,y=0)
        CTkLabel(left_frame,text="Menu",font=('Verdana',22),fg_color="blue",text_color="white").place(x=0,y=160,relwidth=1)

        image=Image.open("Employee.ico")
        Emp_img=ImageTk.PhotoImage(image=image)
        CTkButton(left_frame,image=Emp_img,text="Employees",font=('Verdana',25),anchor='w',command=lambda:employee_form(self.myroot,self.update_count),text_color="white").place(x=0,y=200,relwidth=1)

        image=Image.open("supplier1.ico")
        sup_img=ImageTk.PhotoImage(image=image)
        CTkButton(left_frame,image=sup_img,text="  Supplier",font=('Verdana',25),anchor='w',command=lambda:supplier_form(self.myroot,self.update_count),text_color="white").place(x=0,y=250,relwidth=1)

        image=Image.open("category1.ico")
        catg_img=ImageTk.PhotoImage(image=image)
        CTkButton(left_frame,image=catg_img,text="Category",font=('Verdana',25),command=lambda:category_form(self.myroot,self.update_count),text_color="white").place(x=0,y=300,relwidth=1)

        image=Image.open("product1.ico")
        prod_img=ImageTk.PhotoImage(image=image)
        CTkButton(left_frame,image=prod_img,text="Product",font=('Verdana',25),command=lambda:product_form(self.myroot,self.update_count),text_color="white").place(x=0,y=350,relwidth=1)

        image=Image.open("Sales.ico")
        sales_img=ImageTk.PhotoImage(image=image)
        CTkButton(left_frame,image=sales_img,text="Sales",font=('Verdana',25),command=lambda:sales_form(self.myroot,self.update_count),text_color="white").place(x=0,y=400,relwidth=1)

        image=Image.open("tax.ico")
        tax_img=ImageTk.PhotoImage(image=image)
        CTkButton(left_frame,image=tax_img,text="Tax",font=('Verdana',25),command=lambda:tax_form(self.myroot),text_color="white").place(x=0,y=450,relwidth=1)


        image=Image.open("exit.ico")
        exit_img=ImageTk.PhotoImage(image=image)
        CTkButton(left_frame,image=exit_img,text="Exit",font=('Verdana',25),command=exit,text_color="white").place(x=0,y=500,relwidth=1)

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

        #TOTAL EMPLOYEES
        image=Image.open("Temployees.png")
        image=image.resize((250,180),Image.LANCZOS)
        temp_img=ImageTk.PhotoImage(image=image)
        CTkLabel(self.myroot,image=temp_img,fg_color="white",text='').place(relx=420/1260,rely=80/680)
        CTkLabel(self.myroot,text="Total Employees",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=410/1260,rely=200/680)

        self.emp_count=CTkLabel(self.myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="blue",anchor="center",height=70,width=200)
        self.emp_count.place(relx=440/1260,rely=240/680)

        #TOTAL SUPPLIERS
        image=Image.open("Tsupplier.png")
        image=image.resize((250,120),Image.LANCZOS)
        tsup_img=ImageTk.PhotoImage(image=image)
        CTkLabel(self.myroot,image=tsup_img,fg_color="white",text='').place(relx=820/1250,rely=90/680)
        CTkLabel(self.myroot,text="Total Suppliers",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=830/1260,rely=200/680)

        self.sup_count=CTkLabel(self.myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="green",anchor="center",height=70,width=200,bg_color="white")
        self.sup_count.place(relx=850/1260,rely=240/680)

        #TOTAL CATEGORY
        image=Image.open("Tcategory.png")
        image=image.resize((200,150),Image.LANCZOS)
        tcat_img=ImageTk.PhotoImage(image=image)
        CTkLabel(self.myroot,image=tcat_img,fg_color="white",text='').place(relx=440/1260,rely=300/680)
        CTkLabel(self.myroot,text="Total Category",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(x=425,y=440)

        self.catg_count=CTkLabel(self.myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="violet",anchor="center",height=70,width=200,bg_color="white")
        self.catg_count.place(relx=440/1260,rely=480/680)

        #TOTAL PRODUCTS
        image=Image.open("Tproduct.png")
        image=image.resize((250,120),Image.LANCZOS)
        tprod_img=ImageTk.PhotoImage(image=image)
        CTkLabel(self.myroot,image=tprod_img,fg_color="white",text='').place(relx=850/1260,rely=320/680)
        CTkLabel(self.myroot,text="Total Products",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=840/1260,rely=440/680)

        self.prod_count=CTkLabel(self.myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="orange",anchor="center",height=70,width=200,bg_color="white")
        self.prod_count.place(relx=860/1260,rely=480/680)

        #TOTAL SALES
        image=Image.open("Tsales.png")
        image=image.resize((250,120),Image.LANCZOS)
        tsales_img=ImageTk.PhotoImage(image=image)
        CTkLabel(self.myroot,image=tsales_img,fg_color="white",text='').place(relx=630/1260,rely=490/680)
        CTkLabel(self.myroot,text="Total Sales",font=('Verdana',30,'bold'),fg_color="white",text_color="#1c4e80").place(relx=660/1260,rely=580/680)

        self.sales_count=CTkLabel(self.myroot,text="0",font=('verdana',50,'bold'),fg_color="white",text_color="#d32d41",anchor="center",height=70,width=200,bg_color="white")
        self.sales_count.place(relx=660/1260,rely=610/680)

        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.update_count()


        self.myroot.mainloop()

    # if __name__ == "__main__":
    #     Ims_run(admin)
if __name__ == "__main__":
    app = Ims_run(admin="Yash")


