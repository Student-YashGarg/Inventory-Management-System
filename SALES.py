from customtkinter import *
from tkinter import messagebox,Scrollbar,Listbox,Text
from PIL import Image,ImageTk
import os

###############################################################################################################################
def sales_form(myroot,update_count):
    global invoice_entry,list_box,bill_text

    bill_frame=CTkFrame(myroot,width=980,height=600,fg_color="white",bg_color="white") #FDEBD0
    bill_frame.place(relx=270/1260,rely=78/680)


    CTkLabel(bill_frame,text="View Customer Bills",font=('verdana',25,'bold'),anchor='center',fg_color="#D68910",text_color="white").place(relx=0,rely=0,relwidth=1)

    image=Image.open("back.ico")
    back_img=ImageTk.PhotoImage(image=image)
    bill_frame.back_img=back_img
    CTkButton(bill_frame,image=bill_frame.back_img,text='',width=20,fg_color="#D68910",cursor='hand2',command=lambda: (bill_frame.place_forget(),update_count())).place(relx=10/980,rely=45/600)

    invoice_lbl=CTkLabel(bill_frame,text="Invoice No.",font=('verdana',18,'bold'),text_color="black").place(x=40,y=110)

    invoice_entry=CTkEntry(bill_frame,fg_color="white",text_color="black",font=('verdana',18),placeholder_text="Enter Invoice No.",height=20,width=170)
    invoice_entry.place(x=170,y=110)
    invoice_entry.insert(0,'INV')

    search_btn=CTkButton(bill_frame,text="Search",font=('verdana',18),corner_radius=30,width=90,fg_color="#D68910",text_color="white",command=search_bill)
    search_btn.place(x=360,y=110)

    clear_btn=CTkButton(bill_frame,text="Clear",font=('verdana',18),corner_radius=30,width=90,fg_color="#D68910",text_color="white",command=clear)
    clear_btn.place(x=460,y=110)

    delete_btn = CTkButton(bill_frame, text="Delete", font=('verdana', 18), corner_radius=30,width=90, fg_color="#D68910",text_color="white",command=delete_bill)
    delete_btn.place(x=560, y=110)


    #----------------------------------------------------------------------------------------------------
    #LEFT FRAME
    left_frame=CTkFrame(bill_frame,width=200,height=330)
    left_frame.propagate(0)
    left_frame.place(x=40,y=150)

    CTkLabel(left_frame,text="Invoices",font=('verdana',14,'bold'),anchor='center',fg_color="#D68910").pack(side=TOP,fill=X)

    ver_scrollbar = Scrollbar(left_frame, orient=VERTICAL)
    list_box = Listbox(left_frame, font=('verdana', 15), bg="#161c30", yscrollcommand=ver_scrollbar.set,fg="cyan")
    ver_scrollbar.pack(side=RIGHT, fill=Y)
    ver_scrollbar.config(command=list_box.yview)
    list_box.pack(fill=BOTH, expand=True)

    insert_listbox()

    #-------------------------------------------------------------------------------  
    #RIGHT FRAME
    right_frame=CTkFrame(bill_frame,width=410,height=330)
    right_frame.propagate(0)
    right_frame.place(x=240,y=150)

    CTkLabel(right_frame,text="Customer Bill Area",font=('verdana',14,'bold'),anchor='center',fg_color="#D68910").pack(side=TOP,fill=X)

    ver_scrollbar = Scrollbar(right_frame, orient=VERTICAL)
    bill_text=Text(right_frame,font=('verdana',10),yscrollcommand=ver_scrollbar.set,wrap="word",bg="#161c30",fg="white")  # optional: better formatting)
    ver_scrollbar.pack(side=RIGHT, fill=Y)
    ver_scrollbar.config(command=bill_text.yview)
    bill_text.pack(fill=BOTH,expand=True)

    #image
    image=Image.open("Sales_bill.jpg")
    image=image.resize((340,350),Image.LANCZOS)
    sales_bill_image=ImageTk.PhotoImage(image=image)
    CTkLabel(bill_frame,image=sales_bill_image,fg_color="white",text='').place(relx=650/980,rely=150/600)

    #------------------------------------------------------------------------------------------------

    list_box.bind("<<ListboxSelect>>", selection)

###################################################################################################
#FUNCTIONS..............
def insert_listbox():
    list_box.delete(0,END)
    for i in os.listdir('Bills'):
        bill=i.split('.')[0]
        list_box.insert(END,bill)
        
def selection(event):  # Bind this to Listbox click
    selected = list_box.get(list_box.curselection())  # e.g., "bill1"
    filename = f'Bills/{selected}.txt'
    
    invoice_entry.delete(0,END)
    invoice_entry.insert(0,selected)

    try:
        with open(filename, 'r') as f:
            bill_text.delete(1.0, END)
            bill_text.insert(END, f.read())
    except FileNotFoundError:
        messagebox.showerror("Error", f"Bill file '{filename}' not found.")
        
def search_bill():
    bill_found = False  # To track if the bill is found
    
    if invoice_entry.get()=='':
        messagebox.showerror("Error","Please Select Invoice No.!")
        return
            
    for i in os.listdir('Bills'):  
        if i.split('.')[0] == invoice_entry.get() :
            bill_found = True
            with open(f'Bills/{i}', 'r') as f:
                bill_text.delete(1.0, END)  # Clear existing content (1.0= line is 1 ,character is 0 )
                bill_text.insert(END, f.read())  # Insert the file's content
            break  # Exit the loop as we've found the bill

    if not bill_found:
        messagebox.showerror('Error', 'Invalid Bill Number!')

def clear():
    list_box.select_clear(0,END)  #remove list_box selection
    invoice_entry.delete(0,END)
    invoice_entry.insert(0,'INV')
    
    bill_text.delete(1.0, END)  # Clear existing content

def delete_bill():
    if not list_box.curselection():
        messagebox.showwarning("Warning", "Please select a bill to delete!")
        return
    
    selected = list_box.get(list_box.curselection())  # e.g., "bill1"
    filename = f'Bills/{selected}.txt'
    
    invoice_entry.delete(0,END)
    invoice_entry.insert(0,selected)

    try:
        with open(filename, 'r') as f:
            bill_text.delete(1.0, END)
            bill_text.insert(END, f.read())
    except FileNotFoundError:
        messagebox.showerror("Error", f"Bill file '{filename}' not found.")
        
    #conform
    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{selected}'?")
    if confirm:
        try:
            os.remove(filename) #delete file 
            messagebox.showinfo("Deleted", f"'{selected}' has been deleted successfully.")
            insert_listbox()  # refresh list after deletion
            clear()  # clear UI
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete file: {e}")