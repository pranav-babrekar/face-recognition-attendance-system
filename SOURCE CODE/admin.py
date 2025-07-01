from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from student_details import StudentDetails
from manage_users import ManageUsers
import os
import cv2
import numpy as np


class Admin_dashboard:
    def __init__(self, root, temp_user=""):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.configure(bg='teal')
        self.root.title("Student Attendance System")
        self.root.state("zoomed")

        # banner
        img = Image.open(r"images\bg1.jpg")
        img = img.resize((1280, 180))
        self.photoimg = ImageTk.PhotoImage(img)
        f_banner = Label(self.root, bg="#ffd6cc")
        f_banner.place(x=0, y=0, width=1280, height=50)

        back_btn = Button(self.root, command=self.on_closed, text="LOGOUT", font=(
            "time new roman", 16, "bold"), width=13, bg="blue", fg="white")
        back_btn.grid(row=0, column=0, padx=6, pady=6)

        # title
        title_lbl = Label(self.root, text="STUDENT ATTENDANCE SYSTEM", font=(
            "time new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=50, width=1280, height=50)

        # background
        bg_img = Label(self.root, bg="#ffd6cc")
        bg_img.place(x=0, y=100, width=1280, height=640)

        title_lbl4 = Label(self.root, text="welcome, "+temp_user, font=(
            "time new roman", 24), bg="#ffd6cc", fg="#000080")
        title_lbl4.place(x=-150, y=100, width=600, height=50)

        # student details
        tab1 = Image.open(
            r"images\std1.jpg")
        tab1 = tab1.resize((220, 220))
        self.tab_img1 = ImageTk.PhotoImage(tab1)

        b1 = Button(bg_img, image=self.tab_img1,
                    command=self.Student_Details, cursor="hand2")
        b1.place(x=230, y=150, width=250, height=240)
        b1_1 = Button(bg_img, text="Student Details", command=self.Student_Details, font=(
            "times new roman", 20), bg="#008000", fg="white")
        b1_1.place(x=230, y=380, width=250, height=40)

        # Train Data
        tab4 = Image.open(
            r"images\tra1.jpg")
        tab4 = tab4.resize((220, 220))
        self.tab_img4 = ImageTk.PhotoImage(tab4)
        b4 = Button(bg_img, command=self.train_data,
                    image=self.tab_img4, cursor="hand2")
        b4.place(x=530, y=150, width=250, height=240)
        b4_1 = Button(bg_img, command=self.train_data, text="Train Data", font=(
            "times new roman", 20), bg="#008000", fg="white")
        b4_1.place(x=530, y=380, width=250, height=40)

        # create users
        tab12 = Image.open(
            r"images\log.jpg")
        tab12 = tab12.resize((220, 220))
        self.tab_img12 = ImageTk.PhotoImage(tab12)
        b1 = Button(bg_img, image=self.tab_img12, command=self.Manage_users,
                    cursor="hand2")
        b1.place(x=830, y=150, width=250, height=240)
        b1_1 = Button(bg_img, text="Manage Users",command=self.Manage_users, font=(
            "times new roman", 20), bg="#008000", fg="white")
        b1_1.place(x=830, y=380, width=250, height=40)

    def open_img(self):
        os.startfile("data")

    # button events

    def Student_Details(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentDetails(self.new_window)
        self.new_window.attributes('-topmost', True)
        self.new_window.wm_attributes('-fullscreen', 'True')

    def Manage_users(self):
        self.new_window = Toplevel(self.root)
        self.app = ManageUsers(self.new_window)
        self.new_window.wm_attributes('-fullscreen', 'True')

    def on_closed(self):
        if messagebox.askokcancel("Quit", "Do you Want to Quit?", parent=self.root):
            self.root.destroy()

    # ========== Train Data =========
    def train_data(self):
        Train = messagebox.askyesno(
            "Train Data", "Do You Want to Train This Data", parent=self.root)
        if Train > 0:
            data_dir = ("data")
            path = [os.path.join(data_dir, file)
                    for file in os.listdir(data_dir)]

            if path == []:
                messagebox.showerror(
                    "error", "please take photos", parent=self.root)
            else:
                faces = []
                ids = []

                for image in path:
                    img = Image.open(image).convert('L')  # Gray scale image
                    imageNP = np.array(img, 'uint8')
                    id = int(os.path.split(image)[1].split('.')[1])

                    faces.append(imageNP)
                    ids.append(id)

                    cv2.imshow("Training", imageNP)
                    cv2.waitKey(1) == 13

                ids = np.array(ids)

                # ============ train the classifier and save it =====
                clf = cv2.face.LBPHFaceRecognizer_create()
                clf.train(faces, ids)
                clf.write("lib/classifier.xml")

                cv2.destroyAllWindows()
                messagebox.showinfo(
                    "Result", "Training Dataset Completed...", parent=self.root)
        else:
            if not Train:
                return


if __name__ == "__main__":
    root = Tk()
    obj = Admin_dashboard(root)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()
