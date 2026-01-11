from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class Login_system:
    def __init__(self):
        self.count = 0
        self.text = ""

        # ---------------------------------------------------------------------------------------------------------------------------------------
        # Root
        self.myroot = CTk()
        self.myroot.geometry('1000x590')
        self.myroot.resizable(0, 0)
        self.myroot.config(bg="white")
        self.myroot.title("IMS BY ¥∆$# ₲@₹₲")

        self.t = "Inventory Managment System"
        self.slider_label = CTkLabel(self.myroot, text=self.t, font=('times new roman', 40),
                                     fg_color="#010c48", anchor="center", text_color="white")
        self.slider_label.place(relx=0, rely=0, relwidth=1)
        self.slider()

        # .........................................................................
        # loginimage
        file1 = Image.open("IMAGES/Log_img0.jpg").resize((700, 400))
        file2 = Image.open("IMAGES/Log_img2.jpg").resize((690, 400))
        file3 = Image.open("IMAGES/Log_img3.jpg").resize((700, 400))

        self.images = [
            ImageTk.PhotoImage(file1),
            ImageTk.PhotoImage(file2),
            ImageTk.PhotoImage(file3)
        ]
        self.img_index = 0

        # Label_Image
        self.login_image = CTkLabel(self.myroot, image=self.images[2],
                                    text='', fg_color='transparent', bg_color='transparent')
        self.login_image.place(relx=10/1000, rely=90/500)
        self.image_change()

        # Login_Frame .............................................................................................
        login_frame = CTkFrame(self.myroot, width=350, height=520,
                               corner_radius=10, bg_color='white', fg_color='white')
        login_frame.propagate(0)
        login_frame.place(relx=630/1000, rely=50/500)

        CTkLabel(login_frame, text='Login system', text_color="#005271",
                 font=('gabriola', 40, 'bold')).place(relx=90/350, rely=10/430)

        # loginimage
        log_frame_img = Image.open("IMAGES/login.png").resize((100, 100))
        self.login_frame_img = ImageTk.PhotoImage(image=log_frame_img)

        CTkLabel(login_frame, image=self.login_frame_img, text='').place(
            relx=130/350, rely=90/430)

        # Employee_Id
        CTkLabel(login_frame, text='Employee Id', text_color="black",
                 font=('verdana', 15)).place(relx=50/350, rely=180/430)
        self.employee_Id = StringVar()
        self.password = StringVar()
        employee_Id = CTkEntry(login_frame, textvariable=self.employee_Id, placeholder_text="Enter Employee Id",
                            width=220, fg_color="white", text_color="black", font=('verdana', 19),
                            corner_radius=9, bg_color="white")
        employee_Id.place(relx=50/350, rely=210/430)

        # PASSWORD
        CTkLabel(login_frame, text='Password', text_color="black",
                 font=('verdana', 15)).place(relx=50/350, rely=250/430)

        password = CTkEntry(login_frame, textvariable=self.password, placeholder_text="Enter Password",
                            width=220, fg_color="white", text_color="black", font=('verdana', 19),
                            corner_radius=9, bg_color="white", show='*')
        password.place(relx=50/350, rely=280/430)

        password.bind('<Return>',self.display)

        # HIDE IMAGE
        hide_image = Image.open("IMAGES/hide.png").resize((40, 40))
        self.hide_photo = ImageTk.PhotoImage(hide_image)

        hide_label = CTkLabel(login_frame, text="", image=self.hide_photo, bg_color="white")
        hide_label.place(relx=280/350, rely=275/430)

        # Function
        def show_password(event):
            password.configure(show="")

        def hide_password(event):
            password.configure(show="*")

        hide_label.bind("<ButtonPress-1>", show_password)
        hide_label.bind("<ButtonRelease-1>", hide_password)

        # LOGIN BUTTON
        CTkButton(login_frame, text="Login", width=160, font=('Verdana', 20), cursor="hand2",
                  corner_radius=50, bg_color="white", fg_color='#005271',command=self.display).place(relx=80/350, rely=330/430)

        # OR LABEL
        CTkFrame(login_frame, bg_color='#005271', width=230,
                 height=2).place(relx=50/350, rely=380/430)
        CTkLabel(login_frame, text="OR", bg_color='white',
                 fg_color='white', text_color='#005271').place(relx=155/350, rely=368/430)

        # FORGET Button
        forget_btn = CTkButton(login_frame, text="Forget Password?", width=160, font=('Verdana', 12),
                               cursor="hand2", corner_radius=50, bg_color="white",
                               fg_color='white', text_color='#005271', hover_color='#fafafa')
        forget_btn.place(relx=87/350, rely=388/430)

        def on_enter(event):
            forget_btn.configure(text_color="#00394d",
                                 font=("Verdana", 12, "bold"))

        def on_leave(event):
            forget_btn.configure(text_color="#005271",
                                 font=("Verdana", 12))

        forget_btn.bind("<Enter>", on_enter)
        forget_btn.bind("<Leave>", on_leave)

        # Don't ...Label
        CTkLabel(login_frame, text="Don't have an account ?", width=160,
                 font=('Verdana', 12), text_color='black').place(relx=53/350, rely=408/430)

        # SIGN Button
        sign_btn = CTkButton(login_frame, text="Sign Up", width=80, font=('Verdana', 12),
                             cursor="hand2", corner_radius=50, bg_color="white",
                             fg_color='white', text_color='#005271', hover_color='#fafafa')
        sign_btn.place(relx=208/350, rely=408/430)

        def on_enter(event):
            sign_btn.configure(text_color="#00394d",
                               font=("Verdana", 12, "bold"))

        def on_leave(event):
            sign_btn.configure(text_color="#005271",
                               font=("Verdana", 12))

        sign_btn.bind("<Enter>", on_enter)
        sign_btn.bind("<Leave>", on_leave)

        self.myroot.mainloop()

    # -----------------------------------------------------------------------
    def slider(self):
        if self.count == len(self.t):
            pass
        #TO RUN CONTINOUSLY
        # self.count = 0
        # self.text = ""

        self.text += self.t[self.count]
        self.slider_label.configure(text=self.text)
        self.count += 1
        self.slider_label.after(200, self.slider)

    def image_change(self):
        self.login_image.configure(image=self.images[self.img_index])
        self.img_index = (self.img_index + 1) % len(self.images)
        self.login_image.after(1800, self.image_change)

    def display(self,event=None):
        import sys, os
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))

        import EMP_CONNECTION
        try:
            if self.employee_Id.get()=='' or self.password.get()=='':
                messagebox.showerror("Error_Window","All Fields Are Required!")
            else:
                # Get the cursor and connection from CONNECTION module
                self.cur, self.con = EMP_CONNECTION.connection.getconnection()
                self.cur.execute("select position,Name from EMPLOYEE_DATA where id=%s AND password=%s",(self.employee_Id.get(),self.password.get()))
                data=self.cur.fetchone()
                print(data)
                if data==None:
                    messagebox.showwarning("Warning","Invalid Employee ID or Password/ No Data Found!")
                elif data[0]=='Admin':
                    self.myroot.destroy()
                    # os.system("python IMS.py")
                    # from IMS import Ims_run
                    # # inside your login success function
                    # employee_name = data[1]    # assuming 2nd column of DB is employee_name
                    # Ims_run(employee_name)
                    import IMS
                    IMS.admin_name=data[1]
                    IMS.run_dashboard()


                elif data[0]=='User':
                    self.myroot.destroy()
                    # os.system("python SHOPPING.py")
                    import SHOPPING
                    SHOPPING.username =data[1]
                    SHOPPING.run_dashboard()


        except Exception as e:
            print(f"Error Occured {e}")

if __name__ == "__main__":
    Login_system()
