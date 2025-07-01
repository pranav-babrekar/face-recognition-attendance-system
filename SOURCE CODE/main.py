from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from take_attendance import Take_Attendance
from manage_attendance import Manage_Attendance



class Dashboard:
    global_user = ""

    def __init__(self, root, tmp_user=""):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.configure(bg='teal')
        self.root.title("Student Attendance System")

        self.root.state("zoomed")
        global global_user
        global_user = tmp_user

        # banner
        img = Image.open(r"images\bg1.jpg")
        img = img.resize((1280, 180))
        self.photoimg = ImageTk.PhotoImage(img)
        f_banner = Label(self.root, bg="#ffd6cc")
        f_banner.place(x=0, y=0, width=1280, height=50)
        back_btn = Button(f_banner, command=self.on_closed, text="LOGOUT", font=(
            "time new roman", 16, "bold"), width=13, bg="blue", fg="white")
        back_btn.grid(row=0, column=0, padx=6, pady=0)

        # title
        title_lbl = Label(self.root, text="STUDENT ATTENDANCE SYSTEM", font=(
            "time new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=50, width=1280, height=50)

        # background
        bg_img = Label(self.root, bg="#ffd6cc")
        bg_img.place(x=0, y=100, width=1280, height=640)
        title_lbl4 = Label(self.root, text="welcome, prof. "+global_user, font=(
            "time new roman", 28), bg="#ffd6cc", fg="#000080")
        title_lbl4.place(x=270, y=100, width=600, height=50)

        # Take Attendance
        tab2 = Image.open(
            r"images\det1.jpg")
        tab2 = tab2.resize((220, 220))
        self.tab_img2 = ImageTk.PhotoImage(tab2)
        b2 = Button(bg_img, command=self.TakeAttendance,
                    image=self.tab_img2, cursor="hand2")
        b2.place(x=320, y=150, width=250, height=240)
        b2_1 = Button(bg_img, command=self.TakeAttendance, text="Take Attendance", font=(
            "times new roman", 20), bg="#008000", fg="white")
        b2_1.place(x=320, y=380, width=250, height=40)

        # manage attedenace
        tab3 = Image.open(
            r"images\att.jpg")
        tab3 = tab3.resize((220, 220))
        self.tab_img3 = ImageTk.PhotoImage(tab3)
        b3 = Button(bg_img, command=self.ManageAttendance,
                    image=self.tab_img3, cursor="hand2")
        b3.place(x=640, y=150, width=250, height=240)
        b3_1 = Button(bg_img, command=self.ManageAttendance, text="View Attendance", font=(
            "times new roman", 20), bg="#008000", fg="white")
        b3_1.place(x=640, y=380, width=250, height=40)

       # button events
    def TakeAttendance(self):
        self.new_window = Toplevel(self.root)
        global global_user
        self.app = Take_Attendance(self.new_window, global_user)

        self.new_window.wm_attributes('-fullscreen', 'True')

    def ManageAttendance(self):
        self.new_window = Toplevel(self.root)

        global global_user
        self.app = Manage_Attendance(self.new_window, global_user)
        self.new_window.attributes('-topmost', True)
        self.new_window.wm_attributes('-fullscreen', 'True')

    def on_closed(self):
        if messagebox.askokcancel("Quit", "Do you Want to Quit?", parent=self.root):
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Dashboard(root)
    root.wm_attributes('-fullscreen', 'True')
    root.mainloop()
