from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import DateEntry
import webbrowser
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle
import mysql.connector
import os


class Manage_Attendance:

    TeacherName = ""
    # ================== manage attendance GUI ========================

    def __init__(self, root, global_user="khushal"):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.configure(bg='teal')
        self.root.title("Student Attendance System")
        self.root.state("zoomed")

        # ============ variables ==========
        self.var_enrollment_id = StringVar()
        self.var_name = StringVar()
        self.var_roll_no = StringVar()
        self.var_branch = StringVar()
        self.var_year = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_status = StringVar()
        self.var_div = StringVar()
        self.search_branch = StringVar()
        self.search_year = StringVar()
        self.search_division = StringVar()
        self.var_search_branch_combo = StringVar()
        self.var_search_year_combo = StringVar()
        self.var_search_division_combo = StringVar()

        self.branch_cmb = StringVar()
        self.year_cmb = StringVar()
        self.sem_cmb = StringVar()
        self.session_cmb = StringVar()
        self.div_cmb = StringVar()
        self.sub_cmb = StringVar()
        self.var_dob = StringVar()

        global TeacherName
        TeacherName = global_user

        # banner
        img = Image.open(
            r"images\bg1.jpg")
        img = img.resize((1280, 180))
        self.photoimg = ImageTk.PhotoImage(img)
        f_banner = Label(self.root, image=self.photoimg)
        f_banner.place(x=0, y=0, width=1280, height=50)

        back_btn = Button(f_banner, command=self.backFunction, text="Back", font=(
            "time new roman", 13, "bold"), width=16, bg="blue", fg="white")
        back_btn.grid(row=0, column=0, padx=6, pady=6)

        # title
        title_lbl = Label(self.root, text="View Attendance", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=50, width=1280, height=50)

        # background
        bg = Image.open(
            r"images\bg3.jpg")
        bg = bg.resize((1280, 630))
        self.photoimg2 = ImageTk.PhotoImage(bg)
        bg_img = Label(self.root, image=self.photoimg2)
        bg_img.place(x=0, y=100, width=1280, height=640)
        title_lbl4 = Label(title_lbl, justify=LEFT,  text="welcome, prof. "+global_user, font=(
            "time new roman", 18), bg="white", fg="red")
        title_lbl4.place(x=20, y=10, width=400,
                         height=30)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=5, y=20, width=1265, height=560)

        Right_frame = LabelFrame(main_frame, bg="white", bd=3, relief=GROOVE, font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=20, y=10, width=1220, height=540)

        export_pdf_btn = Button(Right_frame, command=self.exportPDF,  text="Export PDF", font=(
            "time new roman", 13, "bold"), width=15, bg="blue", fg="white")
        export_pdf_btn.place(x=850, y=495)

        open_pdf_btn = Button(Right_frame, command=self.open_pdf, text="View PDF", font=(
            "time new roman", 13, "bold"), width=15, bg="blue", fg="white")
        open_pdf_btn.place(x=1020, y=495)

        Search_frame = LabelFrame(Right_frame, bg="white", bd=3, relief=GROOVE,
                                  text="View Attendance Report", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=50, width=610, height=440)
        right_search_frame = LabelFrame(
            Right_frame, bg="white", text="Search By :", font=(
                "times new roman", 12, "bold"), bd=3, relief=GROOVE)
        right_search_frame.place(x=5, y=2, width=1200, height=70)

        branch_cmb = ttk.Combobox(right_search_frame, textvariable=self.branch_cmb,  state="readonly", font=(
            "times new roman", 12, "bold"), width=12, height=50)
        branch_cmb["values"] = ("Branch",
                                "Computer Engg.", "Civil Engg.", "Mechanical Engg.")
        branch_cmb.current(0)
        branch_cmb.grid(row=0, column=0, padx=5, pady=8, sticky=W)

        year_cmb = ttk.Combobox(right_search_frame, textvariable=self.year_cmb, state="readonly", font=(
            "times new roman", 12, "bold"),  width=12, height=50)
        year_cmb["values"] = ("Year",
                              "First Year", "Second Year", "Third Year")
        year_cmb.current(0)
        year_cmb.grid(row=0, column=1, padx=5, pady=8, sticky=W)

        sem_cmb = ttk.Combobox(right_search_frame, textvariable=self.sem_cmb, state="readonly", font=(
            "times new roman", 12, "bold"),  width=12, height=50)
        sem_cmb["values"] = ("Semester",)
        sem_cmb.current(0)
        sem_cmb.grid(row=0, column=2, padx=5, pady=8, sticky=W)

        sub_cmb = ttk.Combobox(right_search_frame, textvariable=self.sub_cmb, state="readonly", font=(
            "times new roman", 12, "bold"),  width=12, height=50)
        sub_cmb["values"] = ("Subject")
        sub_cmb.current(0)
        sub_cmb.grid(row=0, column=3, padx=5, pady=8, sticky=W)

        search_division_combo = ttk.Combobox(right_search_frame, textvariable=self.session_cmb, state="readonly", font=(
            "times new roman", 12, "bold"),  width=12, height=50)
        search_division_combo["values"] = ("Session Type",
                                           "Theory", "Practical")
        search_division_combo.current(0)
        search_division_combo.grid(
            row=0, column=4, padx=5, pady=8, sticky=W)

        search_division_combo = ttk.Combobox(right_search_frame, textvariable=self.div_cmb, state="readonly", font=(
            "times new roman", 12, "bold"),  width=12, height=50)
        search_division_combo["values"] = ("Division",
                                           "A", "B", "All")
        search_division_combo.current(0)
        search_division_combo.grid(
            row=0, column=6, padx=5, pady=8, sticky=W)

        dob_cal = DateEntry(right_search_frame, width=14, background="#0066c1", date_pattern='dd/mm/yyyy', textvariable=self.var_dob, font=(
            "arial", 13, "bold"), foreground="white", bd=2)
        dob_cal.grid(row=0, column=7, padx=8, sticky=W)

        def update_values12(event):
            year_cmb = self.year_cmb.get()

            temp_sem = []
            if year_cmb == "First Year":
                temp_sem = [
                    "1st Sem", "2nd Sem"]
            elif year_cmb == "Second Year":
                temp_sem = ["3rd Sem", "4th Sem"]

            elif year_cmb == "Third Year":
                temp_sem = ["5th Sem", "6th Sem"]
            else:
                temp_sem = ["Select"]
            sem_cmb["values"] = temp_sem

        year_cmb.bind("<<ComboboxSelected>>", update_values12)

        def update_values(event):
            branch_cmb = self.branch_cmb.get()
            year_cmb = self.year_cmb.get()
            sem_cmb = self.sem_cmb.get()
            temp_subjects = []

            if branch_cmb == "Computer Engg.":
                if year_cmb == "First Year":
                    if sem_cmb == "1st Sem":
                        temp_subjects = [
                            "ENG(22101)", "BSC(22102)", "BMS(22103)", "ICT(22001)", "EGE(22003)", "WPC(22005)"]
                    elif sem_cmb == "2nd Sem":
                        temp_subjects = [
                            "EEC(22215)", "AMI(22224)", "BEC(22225)", "PCI(22226)", "BCC(22009)", "CPH(22013)", "WPD(22014)"]
                    else:
                        temp_subjects = ["Select"]
                elif year_cmb == "Second Year":
                    if sem_cmb == "3rd Sem":
                        temp_subjects = [
                            "OOP(22316)", "DSU(22317)", "CGR(22318)", "DMS(22319)", "DTE(22320)"]
                    elif sem_cmb == "4th Sem":
                        temp_subjects = [
                            "JPR(22412)", "SEN(22413)", "DCC(22414)", "MIC(22415)", "GAD(22034)"]
                    else:
                        temp_subjects = ["Select"]
                elif year_cmb == "Third Year":
                    if sem_cmb == "5th Sem":
                        temp_subjects = ["EST(22447)", "OSY(22516)", "AJP(22517)", "STE(22518)",
                                         "CSS(22519)", "ACN(22520)", "ADM(22521)", "ITR(22057)", "CPP(22058)"]
                    elif sem_cmb == "6th Sem":
                        temp_subjects = ["MGT(22509)", "PWP(22616)", "MAD(22617)", "ETI(22618)",
                                         "WBP(22619)", "NIS(22620)", "DWM(22621)", "EDE(22032)", "CPE(22060)"]
                    else:
                        temp_subjects = ["Select"]
                else:
                    temp_subjects = ["Select"]

            elif branch_cmb == "Civil Engg.":
                if year_cmb == "First Year":
                    if sem_cmb == "1st Sem":
                        temp_subjects = [
                            "ENG(22101)", "BSC(22102)", "BMS(22103)", "ICT(22001)", "EGM(22002)", "WPM(22004)"]
                    elif sem_cmb == "2nd Sem":
                        temp_subjects = ["AMS(22201)", "ASM(22202)", "AME(22203)",
                                         "CMA(22204)", "BSU(22205)", "CEW(22008)", "BCC(22009)"]

                elif year_cmb == "Second Year":
                    if sem_cmb == "3rd Sem":
                        temp_subjects = [
                            "ASU(22301)", "HEN(22302)", "MOS(22303)", "BCO(22304)", "CTE(22305)", "CAD(22022)"]
                    elif sem_cmb == "4th Sem":
                        temp_subjects = [
                            "HRY(22401)", "TOS(22402)", "RBE(22403)", "GTE(22404)", "BPD(22405)", "EST(22447)"]

                elif year_cmb == "Third Year":
                    if sem_cmb == "5th Sem":
                        temp_subjects = ["WRE(22501)", "DSR(22502)", "EAC(22503)", "PHE(22504)", "RDE(22505)",
                                         "ECG(22506)", "TEN(22507)", "PPC(22508)", "ITR(22057)", "CPP(22058)"]
                    elif sem_cmb == "6th Sem":
                        temp_subjects = ["MAN(22509)", "CAA(22601)", "MRS(22602)", "ETC(22603)", "BSE(22604)",
                                         "SWM(22605)", "ERB(22606)", "ADE(22607)", "EDP(22032)", "CPE(22060)", "CMA(22061)"]

            elif branch_cmb == "Mechanical Engg.":
                if year_cmb == "First Year":
                    if sem_cmb == "1st Sem":
                        temp_subjects = [
                            "ENG(22101)", "BSC(22102)", "BMS(22103)", "ICT(22001)", "EGM(22002)", "WPM(22004)"]
                    elif sem_cmb == "2nd Sem":
                        temp_subjects = ["ASM(22202)", "AME(22203)", "AMP(22206)",
                                         "EDR(22207)", "BCC(22209)", "MEW(22010)", "BCC(22009)"]
                elif year_cmb == "Second Year":
                    if sem_cmb == "3rd Sem":
                        temp_subjects = [
                            "SOM(22306)", "BEE(22310)", "TEN(22337)", "MWM(22341)", "EME(22342)", "MEM(22343)"]
                    elif sem_cmb == "4th Sem":
                        temp_subjects = ["TOM(22438)", "MEM(22443)", "FMM(22445)",
                                         "MPR(22446)", "EST(22447)", "CAD(22042)", "FOM(22048)"]
                elif year_cmb == "Third Year":
                    if sem_cmb == "5th Sem":
                        temp_subjects = ["MAN(22509)", "PER(22562)", "AMP(22563)", "EMD(22564)",
                                         "TEN(22565)", "PPE(22566)", "SMA(22053)", "ITR(22057)", "CPP(22058)"]
                    elif sem_cmb == "6th Sem":
                        temp_subjects = ["ETM(22652)", "IHP(22655)", "AEN(22656)", "IEQ(22657)",
                                         "CIM(22658)", "RAC(22660)", "RET(22661)", "EDE(22032)", "CPE(22060)"]

            sub_cmb["values"] = temp_subjects

        sem_cmb.bind("<<ComboboxSelected>>", update_values)

        search_btn = Button(right_search_frame, command=self.search_data, text="Search", font=(
            "time new roman", 13, "bold"), width=10, bg="blue", fg="white")
        search_btn.grid(row=0, column=8, padx=5, pady=8, sticky=W)
        search_all_btn = Button(right_search_frame, command=self.fetch_data, text="Show All", font=(
            "time new roman", 13, "bold"), width=10, bg="blue", fg="white")
        search_all_btn.grid(row=0, column=9, padx=5, pady=8, sticky=W)

        # =================table frame================
        table_frame = Frame(Right_frame, bg="white", bd=3, relief=GROOVE)
        table_frame.place(x=5, y=70, width=1200, height=420)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "enrollment_no", "roll_no", "name", "branch", "year", "division", "semester", "subject", "sessiontype", "date", "time", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        self.AttendanceReportTable.heading(
            "enrollment_no", text="Enrollment No")
        self.AttendanceReportTable.heading("roll_no", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Student Name")
        self.AttendanceReportTable.heading("branch", text="Branch")
        self.AttendanceReportTable.heading("year", text="Year")
        self.AttendanceReportTable.heading("division", text="Division")
        self.AttendanceReportTable.heading("semester", text="Semester")
        self.AttendanceReportTable.heading("subject", text="Subject")
        self.AttendanceReportTable.heading("sessiontype", text="Session Type")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("status", text="Attendance Status")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("enrollment_no", width=100)
        self.AttendanceReportTable.column("roll_no", width=60)
        self.AttendanceReportTable.column("name", width=140)
        self.AttendanceReportTable.column("branch", width=100)
        self.AttendanceReportTable.column("year", width=100)
        self.AttendanceReportTable.column("division", width=80)
        self.AttendanceReportTable.column("semester", width=100)
        self.AttendanceReportTable.column("subject", width=100)
        self.AttendanceReportTable.column("sessiontype", width=100)
        self.AttendanceReportTable.column("date", width=80)
        self.AttendanceReportTable.column("time", width=80)
        self.AttendanceReportTable.column("status", width=150)
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>")

    # =========================== fetch data =============================
    def fetch_data(self):
        global TeacherName
        conn = mysql.connector.connect(
            host="localhost", user="root", database="stud_details")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "select std_enroll,std_roll,std_name,std_branch,std_year,std_div,std_semester,std_subject,std_session_type,std_date,std_time,std_status from history where std_sub_teacher=%s", (TeacherName,))
        data = my_cursor.fetchall()

        if (data != 0):
            self.AttendanceReportTable.delete(
                *self.AttendanceReportTable.get_children())
            for i in data:
                self.AttendanceReportTable.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showinfo(
                "Search", "Student Record Not Found", parent=self.root)
        conn.close()
        self.var_search_branch_combo.set("Branch")
        self.var_search_year_combo.set("Year")
        self.var_search_division_combo.set("Division")

    # ====================== search data ===========================
    def search_data(self):
        if self.branch_cmb.get() == "Branch":
            messagebox.showerror(
                "Error", "Please Select Branch", parent=self.root)
        else:
            try:
                stud_branch = self.branch_cmb.get()
                stud_year = self.year_cmb.get()
                stud_sem = self.sem_cmb.get()
                stud_subject = self.sub_cmb.get()
                stud_session = self.session_cmb.get()
                stud_division = self.div_cmb.get()
                stud_date = self.var_dob.get()
                if stud_division == "All":
                    stud_division = 0

                conn = mysql.connector.connect(
                    host="localhost", user="root", database="stud_details")
                my_cursor = conn.cursor()
                my_cursor.execute("select std_enroll,std_roll,std_name,std_branch,std_year,std_div,std_semester,std_subject,std_session_type,std_date,std_time,std_status from history where std_branch=%s and std_year=%s and std_semester=%s and std_subject=%s and std_session_type=%s and std_div=%s and std_date=%s and std_sub_teacher=%s", (
                    stud_branch,
                    stud_year,
                    stud_sem,
                    stud_subject,
                    stud_session,
                    stud_division,
                    stud_date,
                    TeacherName
                ))
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.AttendanceReportTable.delete(
                        *self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showinfo(
                        "Search", "Student Record Not Found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)

    # ========================= open pdf ===================

    def open_pdf(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("All Files", "*")], parent=self.root
        )
        if filepath:
            self.root.attributes("-topmost", True)
            self.root.after_idle(self.root.attributes, '-topmost', False)
            webbrowser.open_new(filepath)

    # # ========================= export pdf file =======================

    def exportPDF(self):
        if self.branch_cmb.get() == "Branch":
            messagebox.showerror(
                "Error", "Please select Branch", parent=self.root)
        elif self.year_cmb.get() == "Year":
            messagebox.showerror(
                "Error", "Please select Year", parent=self.root)
        elif self.sem_cmb.get() == "Semester":
            messagebox.showerror(
                "Error", "Please select Semester", parent=self.root)
        elif self.sub_cmb.get() == "Subject":
            messagebox.showerror(
                "Error", "Please select Subject", parent=self.root)
        elif self.session_cmb.get() == "Session Type":
            messagebox.showerror(
                "Error", "Please select Session Type", parent=self.root)
        elif self.div_cmb.get() == "Division":
            messagebox.showerror(
                "Error", "Please select Division", parent=self.root)
        else:
            try:
                stud_branch = self.branch_cmb.get()
                stud_year = self.year_cmb.get()
                stud_sem = self.sem_cmb.get()
                stud_subject = self.sub_cmb.get()
                stud_session = self.session_cmb.get()
                stud_division = self.div_cmb.get()
                stud_date = self.var_dob.get()
                stud_enroll = ""
                stud_rol = ""
                stud_name = ""
                stud_time = ""
                stud_status = ""
                global TeacherName

                if stud_division == "All":
                    stud_division = 0

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    database="stud_details"
                )
                mycursor = mydb.cursor()
                mycursor.execute("SELECT std_enroll,std_roll,std_name,std_time,std_status FROM history WHERE std_branch= %s AND std_year= %s AND std_div= %s AND std_semester=%s AND std_subject=%s  AND std_session_type=%s AND std_date=%s AND std_sub_teacher=%s", (
                    stud_branch,
                    stud_year,
                    stud_division,
                    stud_sem,
                    stud_subject,
                    stud_session,
                    stud_date,
                    TeacherName
                ))
                myresult = mycursor.fetchall()

                heading = ["Enrollment No", "Roll No",
                           "Student Name", "Time", "Status"]

                myresult.insert(0, heading)
                inch = 10
                fln = filedialog.asksaveasfilename(initialdir=os.getcwd()+"/Attendance_Reports", title="Save PDF",
                                                   defaultextension='.pdf', filetypes=(("PDF File", "*.pdf"), ("ALL File", "*.*")), parent=self.root)
                if fln == "":
                    self.branch_cmb.get() == "Branch"
                    self.year_cmb.get() == "Year"
                    self.sem_cmb.get() == "Semester"
                    self.sub_cmb.get() == "Subject"
                    self.session_cmb.get() == "Session Type"
                    self.div_cmb.get() == "Division"
                else:
                    pdf_file = SimpleDocTemplate(fln, pagesize=portrait(
                        A4), topMargin=inch, bottomMargin=inch, leftMargin=10, rightMargin=10)

                    flowables = []
                    my_Style = ParagraphStyle('My Para style',
                                              fontName='Times-Roman',
                                              fontSize=28,
                                              leading=40,
                                              alignment=1
                                              )
                    my_Style1 = ParagraphStyle('My Para style',
                                               fontName='Times-Roman',
                                               fontSize=16,
                                               leading=30,
                                               alignment=1
                                               )
                    my_Style3 = ParagraphStyle('My Para style',
                                               fontName='Times-Roman',
                                               fontSize=14,
                                               leading=10,
                                               alignment=2
                                               )
                    if stud_division == 0:
                        stud_division = "All"
                    text = "Attendance Report"
                    date = "Date :- " + stud_date
                    text2 = "Branch :- "+stud_branch+" | Year :- " + \
                        stud_year+" | Semester :-  "+stud_sem
                    text3 = "Subject :- " + \
                        stud_subject+" | Session Type :-  "+stud_session + " | Division :- "+stud_division
                    p = Paragraph(text, my_Style)
                    p1 = Paragraph(text2, my_Style1)
                    p2 = Paragraph(text3, my_Style1)
                    p3 = Paragraph(date, my_Style3)
                    
                    
                   
                    flowables.append(p3)
                    flowables.append(p)
                    flowables.append(p1)
                    flowables.append(p2)

                    table = Table(myresult, rowHeights=30,
                                  normalizedData=0, repeatRows=1)
                    table.setStyle(TableStyle([
                        ("BACKGROUND", (0, 0), (-1, 0), "#4D0026"),
                        ("BOX", (0, 0), (-1, -1), 1, colors.black),
                        ("GRID", (0, 0), (-1, -1), 1, colors.black),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTSIZE", (0, 0), (-1, 0), 14),
                        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                        ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
                        ("ALIGN", (0, 1), (-1, -1), "CENTER"),
                        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                        ("FONTSIZE", (0, 1), (-1, -1), 12),
                        ("BOTTOMPADDING", (0, 1), (-1, -1), 10),
                    ]))
                    
                    
                    for i in range(1, len(myresult)):
                        if "Present" in myresult[i][4]:
                            table.setStyle(TableStyle([
                                ('BACKGROUND', (0, i), (-1, i), "#8cf2a7"),
                                ('TEXTCOLOR', (0, i), (-1, i), colors.black),
                            ]))
                        else:
                            table.setStyle(TableStyle([
                                ('BACKGROUND', (0, i), (-1, i), "#d4d4d4"),
                                ('TEXTCOLOR', (0, i), (-1, i), colors.black),
                            ]))

                   
                   
                    flowables.append(table)
                    pdf_file.build(flowables)
                    messagebox.showinfo("Data Export", "Your data exported to " +
                                        os.path.basename(fln)+" sucessfully", parent=self.root)

            except Exception as es:
                messagebox.showerror(


                    "Error", f"Due to :{str(es)}", parent=self.root)

    # back button

    def backFunction(self):
        self.root.destroy()


# =========== tkinter object creation =====================
if __name__ == "__main__":
    root = Tk()
    obj = Manage_Attendance(root)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()
