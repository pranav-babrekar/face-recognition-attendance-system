from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import mysql.connector


class StudentDetails:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.configure(bg='teal')
        self.root.title("Student Attendance System")
        self.root.state("zoomed")

        # ================ variables==============
        self.var_branch = StringVar()
        self.var_year = StringVar()
        self.var_enrollment = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_mob = StringVar()
        self.var_search_branch_combo = StringVar()
        self.var_search_year_combo = StringVar()
        self.var_search_division_combo = StringVar()
        self.b1 = StringVar()

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
        main_frame.place(x=5, y=50, width=1265, height=530)

        # title
        title_lbl = Label(self.root, text="STUDENT DETAILS", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=50, width=1280, height=50)

        back_btn = Button(f_banner, command=self.backFunction, text="Back", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        back_btn.grid(row=0, column=0, padx=6, pady=6)

        # left label frame
        Left_frame = LabelFrame(main_frame, bg="white", bd=3, relief=GROOVE, font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=650, y=10, width=600, height=505)

        # current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=GROOVE, text="Current Course Details", font=(
            "times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=5, width=580, height=90)

        # branch
        branch_label = Label(current_course_frame, bg="white", text="Branch", font=(
            "times new roman", 12, "bold"))
        branch_label.grid(row=0, column=0, padx=10, sticky=W)

        branch_combo = ttk.Combobox(current_course_frame, textvariable=self.var_branch, state="readonly", font=(
            "times new roman", 12, "bold"))
        branch_combo["values"] = ("Select",
                                  "Computer Engg.", "Civil Engg.", "Mechanical Engg.")
        branch_combo.current(0)
        branch_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # year
        year_label = Label(current_course_frame, bg="white", text="Year", font=(
            "times new roman", 12, "bold"))
        year_label.grid(row=0, column=2, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, state="readonly", font=(
            "times new roman", 12, "bold"))
        year_combo["values"] = ("Select",
                                "First Year", "Second Year", "Third Year")
        year_combo.current(0)
        year_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # class student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=GROOVE, text="Student Information", font=(
            "times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=100, width=580, height=380)

        # Enrollment No
        Enrollment_no_label = Label(class_student_frame, bg="white", text="Enrollment No :", font=(
            "times new roman", 12, "bold"))
        Enrollment_no_label.grid(row=0, column=0, padx=10, sticky=W)
        Enrollment_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_enrollment, width=15, font=(
            "times new roman", 12, "bold"))
        Enrollment_no_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student_frame, bg="white", text="Roll No :", font=(
            "times new roman", 12, "bold"))
        roll_no_label.grid(row=1, column=0, padx=10, sticky=W)
        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=15, font=(
            "times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # student name
        Student_name_label = Label(class_student_frame, bg="white", text="StudentName :", font=(
            "times new roman", 12, "bold"))
        Student_name_label.grid(row=2, column=0, padx=10, sticky=W)
        Student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_name, width=15, font=(
            "times new roman", 12, "bold"))
        Student_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, bg="white", text="Gender :", font=(
            "times new roman", 12, "bold"))
        gender_label.grid(row=6, column=0, padx=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, width=13, textvariable=self.var_gender, state="readonly", font=(
            "times new roman", 12, "bold"))
        gender_combo["values"] = ("Select",
                                  "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        # Division
        class_div_label = Label(class_student_frame, bg="white", text="Division :", font=(
            "times new roman", 12, "bold"))
        class_div_label.grid(row=7, column=0, padx=10, sticky=W)

        div_combo = ttk.Combobox(class_student_frame, width=13, textvariable=self.var_div, state="readonly", font=(
            "times new roman", 12, "bold"))
        div_combo["values"] = ("Select",
                               "A", "B")
        div_combo.current(0)
        div_combo.grid(row=7, column=1, padx=10, pady=10, sticky=W)

        # mobile no
        mobile_label = Label(class_student_frame, bg="white", text="Mobile No :", font=(
            "times new roman", 12, "bold"))
        mobile_label.grid(row=8, column=0, padx=10, sticky=W)
        mobile_entry = ttk.Entry(class_student_frame, textvariable=self.var_mob, width=15, font=(
            "times new roman", 12, "bold"))
        mobile_entry.grid(row=8, column=1, padx=10, pady=5, sticky=W)

        profile_photo = LabelFrame(
            class_student_frame, bd=4, highlightcolor="blue",  bg="white")
        profile_photo.place(x=348, y=2, width=178, height=170)
        tab1 = Image.open(
            fr"images\log1.png")
        tab1 = tab1.resize((180, 160))
        self.tab_img1 = ImageTk.PhotoImage(tab1)
        b1 = Label(profile_photo, textvariable=self.b1,  image=self.tab_img1)
        b1.place(x=0, y=0, width=170, height=160)

        # buttons frame
        btn_frame = Frame(class_student_frame,
                          relief=GROOVE, bg="white")
        btn_frame.place(x=10, y=260, width=545, height=90)

        save_btn = Button(btn_frame, command=self.add_data, text="Save", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=6, pady=6)

        update_btn = Button(btn_frame, command=self.update_data, text="Update", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=6, pady=6)

        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        reset_btn.grid(row=0, column=2)

        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Take Photo", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0)

        delete_btn = Button(btn_frame, command=self.delete_data, text="Delete", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        delete_btn.grid(row=1, column=1)

        # right label frame
        Right_frame = LabelFrame(main_frame, bg="white", bd=3, relief=GROOVE, font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=10, y=10, width=630, height=505)

        Search_frame = LabelFrame(Right_frame, bg="white", bd=3, relief=GROOVE, text="Search By :", font=(
            "times new roman", 12, "bold"))
        Search_frame.place(x=5, y=5, width=610, height=70)

        search_branch_combo = ttk.Combobox(Search_frame, textvariable=self.var_search_branch_combo,  state="readonly", font=(
            "times new roman", 12, "bold"), width=10)
        search_branch_combo["values"] = ("Branch",
                                         "Computer Engg.", "Civil Engg.", "Mechanical Engg.", "All")
        search_branch_combo.current(0)
        search_branch_combo.grid(row=0, column=0, padx=5, pady=8, sticky=W)

        search_year_combo = ttk.Combobox(Search_frame, textvariable=self.var_search_year_combo, state="readonly", font=(
            "times new roman", 12, "bold"), width=10)
        search_year_combo["values"] = ("Year",
                                       "First Year", "Second Year", "Third Year", "All")
        search_year_combo.current(0)
        search_year_combo.grid(row=0, column=1, padx=5, pady=8, sticky=W)

        search_division_combo = ttk.Combobox(Search_frame, textvariable=self.var_search_division_combo, state="readonly", font=(
            "times new roman", 12, "bold"), width=10)
        search_division_combo["values"] = ("Division",
                                           "A", "B", "All")
        search_division_combo.current(0)
        search_division_combo.grid(row=0, column=2, padx=5, pady=8, sticky=W)

        search_btn = Button(Search_frame, command=self.search_data, text="Search", font=(
            "time new roman", 12, "bold"), width=10, bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5)

        showAll_btn = Button(Search_frame, command=self.fetch_data, text="Show All", font=(
            "time new roman", 13, "bold"), width=10, bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4)

        # =================table frame================
        table_frame = Frame(Right_frame, bg="white", bd=3, relief=GROOVE)
        table_frame.place(x=5, y=80, width=610, height=410)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=(
            "enroll", "name", "branch", "year",  "div", "roll", "gen", "mob", "photosample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("enroll", text="Enrollment No")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("branch", text="Branch")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gen", text="Gender")
        self.student_table.heading("mob", text="Mobile No")
        self.student_table.heading("photosample", text="Photo Status")

        self.student_table["show"] = "headings"
        self.student_table.column("enroll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("branch", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gen", width=100)
        self.student_table.column("mob", width=100)
        self.student_table.column("photosample", width=100)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()
        self.updatePhotoStatus()
    # ==================== search data ==================================

    def search_data(self):
        if self.var_search_branch_combo.get() == "Branch" or self.var_search_year_combo.get() == "Year" or self.var_search_division_combo.get() == "Division":
            messagebox.showerror(
                "Error", "Please Select Branch, Year, Division", parent=self.root)
        else:
            try:
                branch = self.var_search_branch_combo.get()
                year = self.var_search_year_combo.get()
                division = self.var_search_division_combo.get()
                conn = mysql.connector.connect(
                    host="localhost", user="root", database="stud_details")
                my_cursor = conn.cursor()
                if branch == "All":
                    branch = 0
                if year == "All":
                    year = 0
                if division == "All":
                    division = 0
                my_cursor.execute("select * from stud_info where branch=%s and year=%s and division=%s", (
                    branch,
                    year,
                    division
                ))
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo(
                        "Search", "Student Record Not Found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

        # =============== add data function =============

    # ================ add student data =================================
    def add_data(self):
        if self.var_branch.get() == "Select Department" or self.var_year.get() == "" or self.var_enrollment.get() == "" or self.var_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_mob.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", database="stud_details")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into stud_info values(%s,%s,%s,%s,%s,%s,%s,%s,'No')", (
                        self.var_enrollment.get(),
                        self.var_name.get(),
                        self.var_branch.get(),
                        self.var_year.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_mob.get()


                    ))
                my_cursor.execute(
                    "insert into attendance values(%s,%s,%s,%s,%s,%s,'-','-','-','-','-','-','Absent')", (
                        self.var_enrollment.get(),
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_branch.get(),
                        self.var_year.get(),
                        self.var_div.get()
                    ))
                conn.commit()
                self.reset_data()
                conn.close()
                try:
                    branch = self.var_search_branch_combo.get()
                    year = self.var_search_year_combo.get()
                    division = self.var_search_division_combo.get()
                    conn = mysql.connector.connect(
                        host="localhost", user="root", database="stud_details")
                    my_cursor = conn.cursor()
                    if branch == "All" or branch == "Branch":
                        branch = 0
                    if year == "All" or year == "Year":
                        year = 0
                    if division == "All" or division == "Division":
                        division = 0
                    my_cursor.execute("select * from stud_info where branch=%s and year=%s and division=%s", (
                        branch,
                        year,
                        division
                    ))
                    data = my_cursor.fetchall()
                    if len(data) != 0:
                        self.student_table.delete(
                            *self.student_table.get_children())
                        for i in data:
                            self.student_table.insert(
                                "", END, values=i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Due To :{str(es)}", parent=self.root)

                messagebox.showinfo(
                    "Success", "Student Details Added Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ================= fetch data function =============================
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", database="stud_details")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from stud_info")
        data = my_cursor.fetchall()

        if (data != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        self.var_search_branch_combo.set("Branch")
        self.var_search_year_combo.set("Year")
        self.var_search_division_combo.set("Division")

    def updatePhotoStatus(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", user="root", database="stud_details")
            my_cursor = conn.cursor()

            data_dir = ("data")
            path = [os.path.join(data_dir, file)
                    for file in os.listdir(data_dir)]
            id2 = []

            for image in path:
                id = int(os.path.split(image)[1].split('.')[1])
                id2.append(id)
            for k in id2:
                my_cursor.execute(
                    "update stud_info set photo_sample='Yes' where enrollment_no=%s", (
                        k,
                    ))
                conn.commit()
            conn.close()
            self.fetch_data()
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due To :{str(es)}", parent=self.root)

    # =========== get particular data ===================================

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        # self.var_radio1.set("No")
        self.var_enrollment.set(data[0]),
        self.var_name.set(data[1]),
        self.var_branch.set(data[2]),
        self.var_year.set(data[3]),
        self.var_div.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_mob.set(data[7])

        data_dir = ("data")
        path = [os.path.join(data_dir, file)
                for file in os.listdir(data_dir)]
        id2 = []

        flag = "No"
        for image in path:
            id = int(os.path.split(image)[1].split('.')[1])
            id2.append(id)
        en = int(self.var_enrollment.get())

        for k in id2:
            if en == k:
                flag = "Yes"

        if flag == "Yes":
            # self.var_radio1.set("Yes")
            # profile photo
            tab1 = Image.open(
                fr"data\student.{en}.5.jpg")
            tab1 = tab1.resize((180, 160))
            self.tab_img1 = ImageTk.PhotoImage(tab1)
            b1 = Label(self.root, textvariable=self.b1,  image=self.tab_img1)
            b1.place(x=1020, y=294, width=170, height=160)
        else:
            tab1 = Image.open(
                fr"images\log1.png")
            tab1 = tab1.resize((180, 160))
            self.tab_img1 = ImageTk.PhotoImage(tab1)
            b1 = Label(self.root, textvariable=self.b1,  image=self.tab_img1)
            b1.place(x=1020, y=294, width=170, height=160)

    # ============= update data functions ===============================

    def update_data(self):
        if self.var_branch.get() == "Select Department" or self.var_year.get() == "" or self.var_enrollment.get() == "" or self.var_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_mob.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do You Want to Update This Student Details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", database="stud_details")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update stud_info set name=%s,branch=%s,year=%s,division=%s,roll_no=%s,gender=%s,mobile=%s where enrollment_no=%s", (
                            self.var_name.get(),
                            self.var_branch.get(),
                            self.var_year.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_mob.get(),
                            self.var_enrollment.get()
                        ))

                    my_cursor.execute(
                        "update attendance set std_roll=%s,std_name=%s,std_branch=%s,std_year=%s,std_div=%s where std_enroll=%s", (
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_branch.get(),
                            self.var_year.get(),
                            self.var_div.get(),
                            self.var_enrollment.get()
                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student Details Successfuly Modified", parent=self.root)
                conn.commit()
                conn.close()
                try:
                    branch = self.var_search_branch_combo.get()
                    year = self.var_search_year_combo.get()
                    division = self.var_search_division_combo.get()
                    conn = mysql.connector.connect(
                        host="localhost", user="root", database="stud_details")
                    my_cursor = conn.cursor()
                    if branch == "All" or branch == "Branch":
                        branch = 0
                    if year == "All" or year == "Year":
                        year = 0
                    if division == "All" or division == "Division":
                        division = 0
                    my_cursor.execute("select * from stud_info where branch=%s and year=%s and division=%s", (
                        branch,
                        year,
                        division
                    ))
                    data = my_cursor.fetchall()
                    if len(data) != 0:
                        self.student_table.delete(
                            *self.student_table.get_children())
                        for i in data:
                            self.student_table.insert(
                                "", END, values=i)
                        conn.commit()
                    conn.close()
                    self.updatePhotoStatus()
                except Exception as es:
                    messagebox.showerror(
                        "Error", f"Due To :{str(es)}", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # =========== delete function =======================================
    def delete_data(self):
        if self.var_enrollment.get() == "":
            messagebox.showerror(
                "Error", "Enrollment No must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student information", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", database="stud_details")
                    my_cursor = conn.cursor()
                    sql = "delete from stud_info where enrollment_no=%s"
                    val = (self.var_enrollment.get(),)
                    my_cursor.execute(sql, val)
                    delsql = "delete from attendance where std_enroll=%s"
                    my_cursor.execute(delsql, val)
                    id = self.var_enrollment.get()
                    img_id = 1
                    while True:
                        if os.path.exists("data/student." + str(id)+"."+str(img_id)+".jpg"):
                            os.remove("data/student." + str(id) +
                                      "."+str(img_id)+".jpg")
                        img_id += 1
                        if int(img_id) == 101:
                            break
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                messagebox.showinfo(
                    "Delete", "Sucessfully Deleted student Details", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ========== reset function =========================================
    def reset_data(self):
        self.var_enrollment.set(""),
        self.var_name.set(""),
        self.var_branch.set("Select"),
        self.var_year.set("Select"),
        self.var_div.set("Select"),
        self.var_roll.set(""),
        self.var_gender.set("Select"),
        self.var_mob.set(""),

        profile_photo = LabelFrame(
            self.root, bd=4, highlightcolor="blue",  bg="white")
        profile_photo.place(x=1016, y=290, width=178, height=170)
        tab1 = Image.open(
            fr"images\log1.png")
        tab1 = tab1.resize((180, 160))
        self.tab_img1 = ImageTk.PhotoImage(tab1)
        b1 = Label(profile_photo, image=self.tab_img1,
                   cursor="hand2")
        b1.place(x=0, y=0, width=170, height=160)

    # ============ generate dataset or take photo =======================
    def generate_dataset(self):
        if self.var_branch.get() == "Select Branch" or self.var_year.get() == "" or self.var_enrollment.get() == "" or self.var_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_mob.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                id = self.var_enrollment.get()

                # ========== load predefined data on frontal face from opencv ===========
                face_classifier = cv2.CascadeClassifier(
                    "lib/haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # scaling factor 1.3, minimum neighbor=5
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, face_frame = cap.read()
                    if face_cropped(face_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(face_frame), (470, 470))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        face = cv2.normalize(
                            face, None, 0, 255, cv2.NORM_MINMAX)
                        file_name_path = "data/student." + \
                            str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 2)
                        cv2.imshow("Capture Images", face)
                        cv2.setWindowProperty(
                            "Capture Images", cv2.WND_PROP_TOPMOST, 1)
                        cv2.waitKey(250)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Generating Dataset Completed...", parent=self.root)
                self.updatePhotoStatus()
                self.reset_data()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # =================== back button ====================================
    def backFunction(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = StudentDetails(root)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()
