from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class ManageUsers:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.configure(bg='teal')
        self.root.title("Student Attendance System")
        self.root.state("zoomed")

        # ================ variables==============
        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_usertype = StringVar()

        # banner
        img = Image.open(
            r"images\bg1.jpg")
        img = img.resize((1280, 180))
        self.photoimg = ImageTk.PhotoImage(img)
        f_banner = Label(self.root, image=self.photoimg)
        f_banner.place(x=0, y=0, width=1280, height=50)

        # background
        bg = Image.open(
            r"images\bg.png")
        bg = bg.resize((1280, 630))
        self.photoimg2 = ImageTk.PhotoImage(bg)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=100, width=1280, height=640)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=50, width=1265, height=480)

        # title
        title_lbl = Label(self.root, text="Manage Users", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=50, width=1280, height=50)

        back_btn = Button(f_banner, command=self.backFunction, text="Back", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        back_btn.grid(row=0, column=0, padx=6, pady=6)

        # left label frame
        Left_frame = LabelFrame(main_frame, bg="white", bd=3, relief=GROOVE, font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=650, y=10, width=600, height=440)

        # class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=GROOVE, text="Manage Users", font=(
            "times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=0, width=580, height=420)

        # Enrollment No
        username = Label(class_student_frame, bg="white", text="Username :", font=(
            "times new roman", 12, "bold"))
        username.grid(row=0, column=0, padx=10, sticky=W)
        username_entry = ttk.Entry(class_student_frame, textvariable=self.var_username, width=15, font=(
            "times new roman", 12, "bold"))
        username_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        password = Label(class_student_frame, bg="white", text="Password :", font=(
            "times new roman", 12, "bold"))
        password.grid(row=1, column=0, padx=10, sticky=W)
        password_entry = ttk.Entry(class_student_frame, textvariable=self.var_password, width=15, font=(
            "times new roman", 12, "bold"))
        password_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # buttons frame
        btn_frame = Frame(class_student_frame,
                          relief=GROOVE, bg="white")
        btn_frame.place(x=10, y=300, width=545, height=90)

        save_btn = Button(btn_frame,  text="Add User", command=self.add_data, font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=6, pady=6)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        reset_btn.grid(row=0, column=2)

        delete_btn = Button(btn_frame,  text="Delete User", command=self.delete_data, font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        delete_btn.grid(row=0, column=1, padx=6, pady=6)

        # right label frame
        Right_frame = LabelFrame(main_frame, bg="white", bd=3, relief=GROOVE, font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=10, y=10, width=630, height=440)

        # =================table frame================
        table_frame = Frame(Right_frame, bg="white", bd=3, relief=GROOVE)
        table_frame.place(x=5, y=10, width=610, height=410)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=(
            "username", "password", "usertype"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("username", text="Username")
        self.student_table.heading("password", text="Password")
        self.student_table.heading("usertype", text="User Type")

        self.student_table["show"] = "headings"

        self.student_table.column("username", width=100)
        self.student_table.column("password", width=100)
        self.student_table.column("usertype", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # ================ add user data =================================

    def add_data(self):
        if self.var_username.get() == "" or self.var_password.get() == "" or self.var_usertype.get() == "Select":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", database="stud_details")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into users values(%s,%s,%s,%s)", (
                        "",
                        self.var_username.get(),
                        self.var_password.get(),
                        "Faculty"
                    ))

                conn.commit()
                self.reset_data()
                conn.close()
                self.fetch_data()

                messagebox.showinfo(
                    "Success", "User Added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # # ================= fetch data function =============================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", database="stud_details")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "select username,password,user_type from users Where user_type='Faculty'")
        data = my_cursor.fetchall()

        if (data != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # # =========== get particular data ===================================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_username.set(data[0]),
        self.var_password.set(data[1]),
        self.var_usertype.set(data[2]),

    # =========== delete function =======================================
    def delete_data(self):
        if self.var_username.get() == "" or self.var_password.get() == "" or self.var_usertype.get() == "Select":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete User", "Do you want to delete", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", database="stud_details")
                    my_cursor = conn.cursor()
                    sql = "delete from users where username=%s AND password=%s AND user_type=%s"
                    val = (self.var_username.get(),
                           self.var_password.get(), "Faculty",)
                    my_cursor.execute(sql, val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                messagebox.showinfo(
                    "Delete", "User Deleted Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ========== reset function =========================================

    def reset_data(self):
        self.var_username.set(""),
        self.var_password.set(""),

    # =================== back button ====================================

    def backFunction(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = ManageUsers(root)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()
