from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from admin import Admin_dashboard
from main import Dashboard
import mysql.connector


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1280x790+0+0")
        self.root.state("zoomed")
        self.root.wm_iconbitmap("images\\App_logo.ico")
        self.root.configure(background='#0066c1')

        # variables
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()

        back_btn = Button(self.root, command=self.backFunction, text="EXIT", font=(
            "time new roman", 18), width=16, bg="#D0492C", fg="white")
        back_btn.grid(row=0, column=0, padx=40, pady=30)

        design_frame3 = Listbox(self.root, bg='#1e85d0', width=100,
                                height=33, highlightthickness=0, borderwidth=0)
        design_frame3.place(x=40, y=106)

        design_frame4 = Listbox(self.root, bg='#f8f8f8', width=100,
                                height=33, highlightthickness=0, borderwidth=0)
        design_frame4.place(x=630, y=106)

        welcome_label = Label(design_frame4, text='Welcome to Student Attedance System', font=(
            'Arial', 20, 'bold'), bg='#f8f8f8')
        welcome_label.place(x=40, y=15)

        welcome_label = Label(design_frame4, text='Admin/Faculty Login', font=(
            'Arial', 20, 'bold'), bg='#f8f8f8')

        welcome_label.place(x=130, y=90)
        # ====== user ====================
        self.txtuser = Entry(design_frame4,  font=(
            "yu gothic ui semibold", 12), highlightthickness=2)
        self.txtuser.place(x=134, y=170, width=280, height=34)
        self.txtuser.config(highlightbackground="black",
                            highlightcolor="black")
        textuserlabel = Label(design_frame4, text='• Username',
                              bg='#f8f8f8', font=("times new roman", 16 ))
        textuserlabel.place(x=130, y=140)

        # ==== Password ==================
        self.txtpwd = Entry(design_frame4,  font=(
            "yu gothic ui semibold", 12), show='•', highlightthickness=2)
        self.txtpwd.place(x=134, y=250, width=280, height=34)
        self.txtpwd.config(
            highlightbackground="black", highlightcolor="black")
        password_label = Label(design_frame4, text='• Password',
                               bg='#f8f8f8', font=("times new roman", 16))
        password_label.place(x=130, y=220)

        loginbtn = Button(design_frame4, command=self.login, text="Login", font=("times new roman", 20),
                          highlightthickness=2, fg="white", bg="#0066c1", activeforeground="white", activebackground="#007ACC")
        loginbtn.config(
            highlightbackground="black", highlightcolor="black")
        loginbtn.place(x=130, y=320, width=280, height=40)

        # ===== Left Side Picture ============
        side_image = Image.open(r'images\loginlabel.jpg')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
        side_image_label.image = photo
        side_image_label.place(x=0, y=-50)

    def login(self):
        if (self.txtuser.get() == "" or self.txtpwd.get() == ""):
            messagebox.showerror(
                "Error", "All Field Required!", parent=self.root)
        else:

            temp_user = self.txtuser.get()
            temp_pass = self.txtpwd.get()
            self.reset_data()
            conn = mysql.connector.connect(
                host="localhost", user="root", database="stud_details")
            type = "Admin"
            my_cursor = conn.cursor()
            my_cursor.execute("select * from users where username = %s and password=%s and user_type = %s", (
                temp_user,
                temp_pass,
                type
            ))

            row = my_cursor.fetchone()
            if row == None:
                type = "Faculty"
                my_cursor = conn.cursor()
                my_cursor.execute("select * from users where username = %s and password=%s and user_type = %s", (
                    temp_user,
                    temp_pass,
                    type
                ))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid user and Password!")
                else:

                    self.new_window = Toplevel(self.root)
                    self.app = Dashboard(self.new_window, temp_user)
                    self.new_window.wm_attributes('-fullscreen', 'True')
                    messagebox.showinfo(
                        "Success", "Welcome " + temp_user+"", parent=self.new_window)
            else:
                self.new_window = Toplevel(self.root)
                self.app = Admin_dashboard(self.new_window, temp_user)

                self.new_window.wm_attributes('-fullscreen', 'True')
                messagebox.showinfo(
                    "Success", "Welcome " + temp_user+"", parent=self.new_window)
            conn.commit()
            conn.close()

    def reset_data(self):
        self.txtuser.delete(0, "end"),
        self.txtpwd.delete(0, "end")

    def backFunction(self):
        if messagebox.askokcancel("Quit", "Do you Want to Quit?", parent=self.root):
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()
