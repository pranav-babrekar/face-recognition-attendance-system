from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import mysql.connector
from time import strftime
from datetime import datetime
import pygame


class Take_Attendance:
    TeacherName = ""

    def __init__(self, root, global_user=""):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.configure(bg='#ffd6cc')
        self.root.title("Student Attendance System")
        self.root.state("zoomed")
        self.var_subject = StringVar()
        self.var_teacher = StringVar()
        self.branch_cmb = StringVar()
        self.year_cmb = StringVar()
        self.sem_cmb = StringVar()
        self.session_cmb = StringVar()
        self.div_cmb = StringVar()
        self.sub_cmb = StringVar()

        global TeacherName
        TeacherName = global_user

        bg1 = Image.open(r"images\bg3.jpg")
        bg1 = bg1.resize((1366, 768))

        temp_subjects = []

        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, bg="#ffd6cc")
        bg_img.place(x=0, y=60, width=1280, height=700)
        back_btn = Button(self.root,  command=self.backFunction, text="Back", font=(
            "time new roman", 16, "bold"), width=13, bg="blue", fg="white")
        back_btn.grid(row=0, column=0, padx=6, pady=6)

        # title
        title_lbl = Label(self.root, text="Take Attendance", font=(
            "time new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=50, width=1280, height=50)
        title_lbl4 = Label(self.root, justify=LEFT,  text="welcome, prof. "+global_user, font=(
            "time new roman", 28), bg="#ffd6cc", fg="#000080")
        title_lbl4.place(x=-600, y=100, width=2500,
                         height=50)

        btn_frame = Frame(self.root,
                          relief=GROOVE, bg="white")
        btn_frame.place(x=50, y=180, width=480, height=330)

        class_student_frame = LabelFrame(btn_frame, bd=2, bg="white", relief=GROOVE, text="Select Class Details", font=(
            "times new roman", 14, "bold"))
        class_student_frame.place(x=15, y=10, width=450, height=300)

        branch_label = Label(class_student_frame, bg="white", text="Branch", font=(
            "times new roman", 14, "bold"))
        branch_label.grid(row=0, column=0, padx=10, sticky=W)
        branch_cmb = ttk.Combobox(class_student_frame, textvariable=self.branch_cmb,  state="readonly", font=(
            "times new roman", 14, "bold"), width=25, height=50)
        branch_cmb["values"] = ("Select",
                                "Computer Engg.", "Civil Engg.", "Mechanical Engg.")
        branch_cmb.current(0)
        branch_cmb.grid(row=0, column=1, padx=5, pady=8, sticky=W)

        year_label = Label(class_student_frame,  bg="white", text="Year", font=(
            "times new roman", 14, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)
        year_cmb = ttk.Combobox(class_student_frame, textvariable=self.year_cmb, state="readonly", font=(
            "times new roman", 14, "bold"),  width=25, height=50)
        year_cmb["values"] = ("Select",
                              "First Year", "Second Year", "Third Year")
        year_cmb.current(0)
        year_cmb.grid(row=1, column=1, padx=5, pady=8, sticky=W)

        year_label = Label(class_student_frame,  bg="white", text="Semester", font=(
            "times new roman", 14, "bold"))
        year_label.grid(row=2, column=0, padx=10, sticky=W)
        sem_cmb = ttk.Combobox(class_student_frame, textvariable=self.sem_cmb, state="readonly", font=(
            "times new roman", 14, "bold"),  width=25, height=50)
        sem_cmb["values"] = ("Select",)
        sem_cmb.current(0)
        sem_cmb.grid(row=2, column=1, padx=5, pady=8, sticky=W)

        class_div_label = Label(class_student_frame, bg="white", text="Subject :", font=(
            "times new roman", 14, "bold"))
        class_div_label.grid(row=3, column=0, padx=10, sticky=W)
        sub_cmb = ttk.Combobox(class_student_frame, textvariable=self.sub_cmb, state="readonly", font=(
            "times new roman", 14, "bold"),  width=25, height=50)
        sub_cmb["values"] = ("Select")
        sub_cmb.current(0)
        sub_cmb.grid(row=3, column=1, padx=5, pady=8, sticky=W)

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

        class_div_label = Label(class_student_frame, bg="white", text="TH or PR :", font=(
            "times new roman", 14, "bold"))
        class_div_label.grid(row=4, column=0, padx=10, sticky=W)
        search_division_combo = ttk.Combobox(class_student_frame, textvariable=self.session_cmb, state="readonly", font=(
            "times new roman", 14, "bold"),  width=25, height=50)
        search_division_combo["values"] = ("Select",
                                           "Theory", "Practical")
        search_division_combo.current(0)
        search_division_combo.grid(
            row=4, column=1, padx=5, pady=8, sticky=W)

        class_div_label = Label(class_student_frame, bg="white", text="Division :", font=(
            "times new roman", 14, "bold"))
        class_div_label.grid(row=5, column=0, padx=10, sticky=W)
        search_division_combo = ttk.Combobox(class_student_frame, textvariable=self.div_cmb, state="readonly", font=(
            "times new roman", 14, "bold"),  width=25, height=50)
        search_division_combo["values"] = ("Select",
                                           "A", "B", "All")
        search_division_combo.current(0)
        search_division_combo.grid(
            row=5, column=1, padx=5, pady=8, sticky=W)

        # recognition button
        tab1 = Image.open(
            r"images\det1.jpg")
        tab1 = tab1.resize((220, 220))
        self.tab_img1 = ImageTk.PhotoImage(tab1)
        b1 = Button(bg_img, image=self.tab_img1,
                    command=self.face_recognition, cursor="hand2")
        b1.place(x=650, y=150, width=250, height=240)
        b1_1 = Button(bg_img, text="Take Attendance", command=self.face_recognition, font=(
            "times new roman", 20, "bold"), bg="#008000", fg="white")
        b1_1.place(x=650, y=370, width=250, height=40)

    def mark_attendance(self, enroll):
        global TeacherName

        stud_branch = self.branch_cmb.get()
        stud_year = self.year_cmb.get()
        stud_sem = self.sem_cmb.get()
        stud_subject = self.sub_cmb.get()
        stud_session = self.session_cmb.get()
        stud_division = self.div_cmb.get()
        if stud_division == "All":
            stud_division = 0
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        t1 = now.strftime("%H:%M:%S")
        st = "Present"

        conn12 = mysql.connector.connect(
            host="localhost", user="root", database="stud_details")
        my_cursor123 = conn12.cursor()
        my_cursor123.execute(
            "SELECT std_status=%s from attendance WHERE std_enroll=%s AND std_branch=%s AND std_year=%s AND std_div=%s", (
                st,
                enroll,
                stud_branch,
                stud_year,
                stud_division,
            ))

        data = my_cursor123.fetchone()
        conn12.commit()
        conn12.close()
        conn1267 = mysql.connector.connect(
            host="localhost", user="root", database="stud_details")
        my_cursor12356 = conn1267.cursor()

        if data is None:
            pass
        else:
            if data[0] == 0:
                my_cursor12356.execute(
                    "UPDATE attendance set std_semester=%s,std_subject=%s,std_sub_teacher=%s,std_session_type=%s, std_date=%s,std_time=%s,std_status=%s WHERE std_enroll=%s AND std_branch=%s AND std_year=%s AND std_div=%s", (
                        stud_sem,
                        stud_subject,
                        TeacherName,
                        stud_session,
                        d1,
                        t1,
                        st,
                        enroll,
                        stud_branch,
                        stud_year,
                        stud_division
                    ))
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load("lib/present.mp3")
                pygame.mixer.music.play()

        conn1267.commit()
        conn1267.close()

    # =========== face recognition ============
    def face_recognition(self):

        conn = mysql.connector.connect(
            host="localhost", user="root", database="stud_details")
        my_cursor = conn.cursor()

        my_cursor.execute(
            "UPDATE attendance set std_semester='-',std_subject='-',std_sub_teacher='-',std_session_type='-', std_date='-',std_time='-',std_status='Absent'")
        conn.commit()
        conn.close()

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predic = clf.predict(gray_image[y:y+h, x:x+w])
                # print("predict= ",predic)
                confidence = int((100*(1-predic/300)))
                # print("confidence", confidence)
                conn = mysql.connector.connect(
                    host="localhost", user="root", database="stud_details")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "SELECT enrollment_no from stud_info WHERE enrollment_no="+str(id))
                enroll = my_cursor.fetchone()
                enroll = "+".join(enroll)
                

                my_cursor.execute(
                    "SELECT branch from stud_info WHERE enrollment_no="+str(id))
                branch = my_cursor.fetchone()
                branch = "+".join(branch)

                my_cursor.execute(
                    "SELECT roll_no from stud_info WHERE enrollment_no="+str(id))
                roll = my_cursor.fetchone()
                roll = "+".join(roll)

                my_cursor.execute(
                    "SELECT name from stud_info WHERE enrollment_no="+str(id))
                name = my_cursor.fetchone()
                name = "+".join(name)

                my_cursor.execute(
                    "SELECT year from stud_info WHERE enrollment_no="+str(id))
                year = my_cursor.fetchone()
                year = "+".join(year)

                # my_cursor.execute(
                #     "SELECT std_status from attendance WHERE std_enroll="+str(id))
                # mark = my_cursor.fetchone()
                # mark = " ".join(mark)

                per = "{0}%".format(round(confidence))

                if confidence > 77:
                    cv2.putText(
                        img, f"Roll: {roll}", (x, y-100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Name: {name}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Branch: {branch}", (x, y-50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Year: {year}", (x, y-25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(
                        img, f"Match: {per}", (x, y+180), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    # if mark == 'Present':
                    #     cv2.putText(
                    #         img, f"Already Marked", (x, y+150), cv2.FONT_HERSHEY_COMPLEX, 0.8, (200, 0, 255), 2)
                    self.mark_attendance(enroll)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown Face", (x, y-15),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 115, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "lib/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("lib/classifier.xml")

        video_cap = cv2.VideoCapture(0)
        wait_time = 5000

        global TeacherName
        stud_branch = self.branch_cmb.get()
        stud_year = self.year_cmb.get()
        stud_sem = self.sem_cmb.get()
        stud_subject = self.sub_cmb.get()
        stud_session = self.session_cmb.get()
        stud_division = self.div_cmb.get()
        if stud_division == "All":
            stud_division = 0

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q') or wait_time == 0:

                now = datetime.now()
                d3 = now.strftime("%d/%m/%Y")
                t2 = now.strftime("%H:%M:%S")

                conn = mysql.connector.connect(
                    host="localhost", user="root", database="stud_details")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE attendance set std_semester=%s,std_subject=%s,std_sub_teacher=%s,std_session_type=%s,std_date=%s,std_time=%s WHERE std_status='Absent' AND std_branch=%s AND std_year=%s AND std_div=%s", (
                        stud_sem,
                        stud_subject,
                        TeacherName,
                        stud_session,
                        d3,
                        t2,
                        stud_branch,
                        stud_year,
                        stud_division

                    ))
                conn.commit()
                conn.close()
                break
            wait_time -= 1
        # store all data from table to history table
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="stud_details"
        )
        cursor = mydb.cursor()
        cursor.execute(
            "SELECT * FROM attendance WHERE std_branch= %s AND std_year= %s AND std_div= %s AND std_semester=%s AND std_subject=%s AND std_sub_teacher=%s AND std_session_type=%s AND std_date=%s", (
                stud_branch,
                stud_year,
                stud_division,
                stud_sem,
                stud_subject,
                TeacherName,
                stud_session,
                d3
            ))

        rows = cursor.fetchall()
        mydb.commit()
        for row in rows:
            t_std_enroll = row[0]
            t_std_roll = row[1]
            t_std_name = row[2]
            t_std_branch = row[3]
            t_std_year = row[4]
            t_std_div = row[5]
            t_std_semester = row[6]
            t_std_subject = row[7]
            t_std_sub_teacher = row[8]
            t_std_session_type = row[9]
            t_std_date = row[10]
            t_std_time = row[11]
            t_std_status = row[12]

            cursor.execute("SELECT * FROM history WHERE std_enroll=%s AND std_roll=%s AND std_name=%s AND std_branch= %s AND std_year= %s AND std_div= %s AND std_semester=%s AND std_subject=%s AND std_sub_teacher=%s AND std_session_type=%s AND std_date=%s AND std_status=%s", (
                t_std_enroll,
                t_std_roll,
                t_std_name,
                t_std_branch,
                t_std_year,
                t_std_div,
                t_std_semester,
                t_std_subject,
                t_std_sub_teacher,
                t_std_session_type,
                t_std_date,
                t_std_status
            ))

            result = cursor.fetchone()

            mydb.commit()
            if result:
                cursor.execute(
                    "UPDATE history SET std_time=%s,std_status=%s WHERE std_enroll=%s AND std_roll=%s AND std_name=%s AND std_branch= %s AND std_year= %s AND std_div= %s AND std_semester=%s AND std_subject=%s AND std_sub_teacher=%s AND std_session_type=%s AND std_date=%s AND std_status='Absent'", (
                        t_std_time,
                        t_std_status,
                        t_std_enroll,
                        t_std_roll,
                        t_std_name,
                        t_std_branch,
                        t_std_year,
                        t_std_div,
                        t_std_semester,
                        t_std_subject,
                        t_std_sub_teacher,
                        t_std_session_type,
                        t_std_date
                    ))
                mydb.commit()
            else:
                cursor.execute(
                    "INSERT INTO history VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)", (
                        t_std_enroll,
                        t_std_roll,
                        t_std_name,
                        t_std_branch,
                        t_std_year,
                        t_std_div,
                        t_std_semester,
                        t_std_subject,
                        t_std_sub_teacher,
                        t_std_session_type,
                        t_std_date,
                        t_std_time,
                        t_std_status

                    ))
                mydb.commit()
        mydb.commit()
        mydb.close()

        video_cap.release()
        cv2.destroyAllWindows()

        messagebox.showinfo(
            "Status", "Attendance Saved Successfully", parent=self.root)
        stud_branch = self.branch_cmb.set("Select")
        stud_year = self.year_cmb.set("Select")
        stud_sem = self.sem_cmb.set("Select")
        stud_subject = self.sub_cmb.set("Select")
        stud_session = self.session_cmb.set("Select")
        stud_division = self.div_cmb.set("Select")

    def backFunction(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Take_Attendance(root)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()
