from customtkinter import *
from tkinter import Toplevel, Spinbox, messagebox

def tax_form(myroot):
    
    def save_tax():
        value = tax_count.get()

        import MySQLdb
        try:
            con = MySQLdb.connect(host="localhost", user="root", password="YASH@3315", autocommit=True)
            cur = con.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS INVENTORY_MANAGEMENT")
            cur.execute("USE INVENTORY_MANAGEMENT")
            cur.execute("CREATE TABLE IF NOT EXISTS tax_table(id INT PRIMARY KEY, tax DECIMAL(5,2))")
            
            cur.execute("SELECT id FROM tax_table WHERE id = 1")
            if cur.fetchone():
                cur.execute("UPDATE tax_table SET tax = %s WHERE id = 1", (value,))
            else:
                cur.execute("INSERT INTO tax_table (id, tax) VALUES (1, %s)", (value,))
            
            con.commit()
            messagebox.showinfo("Success", f"TAX is set to {value}%\nand saved successfully!", parent=tax_root)
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}", parent=tax_root)

    tax_root = Toplevel(myroot)
    tax_root.geometry("300x200")
    tax_root.title("Tax Window")
    tax_root.config(bg="#101c43")
    tax_root.resizable(0,0)
    tax_root.grab_set()

    CTkLabel(tax_root, text="Enter Tax %", font=('verdana', 20)).pack(padx=10, pady=10)

    tax_count = Spinbox(tax_root, from_=0, to=100, font=('verdana', 20))
    tax_count.pack(padx=10, pady=10)

    CTkButton(tax_root, text="Save", font=('times new roman', 20, 'bold'),text_color="white", command=save_tax).pack(pady=10)
    print(tax_count)

