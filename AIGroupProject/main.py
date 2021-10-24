import tkinter
from pyswip import Prolog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# pip install pyswip
# https://trinket.io/docs/colors
# TO DO update checkbox variables, add blood pressure input, adjust subit button, update prolog file


prolog = Prolog()
prolog.consult("diagnosis.pl")


# Main window
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("MOH Covid-19 Diagnosis System")
        self.root.geometry("900x500+10+10")

        title = Label(self.root, text="MOH Covid-19 Diagnosis System", bd=5, relief=GROOVE,
                      font=("times new Roman", 40, "bold"), bg="violet", fg="medium blue")
        title.pack(side=TOP, fill=X)

        self.covidFactBtn = Button(self.root, text="Add Covid-19 Fact", width=25, height=2, command=print(),
                                   bg="lavender", fg="purple")
        self.covidFactBtn.place(x=300, y=100)

        self.muFactBtn = Button(self.root, text="Add Mu Variant Fact", width=25, height=2, command=print(),
                                bg="lavender", fg="purple")
        self.muFactBtn.place(x=300, y=150)

        self.deltaFactBtn = Button(self.root, text="Add Delta Variant Fact", width=25, height=2, command=print(),
                                   bg="lavender", fg="purple")
        self.deltaFactBtn.place(x=300, y=200)

        self.diagBtn = Button(self.root, text="Diagnose Patient", width=25, height=2, command=self.diagnosis_window,
                              bg="violet", fg="purple")
        self.diagBtn.place(x=300, y=250)

    def diagnosis_window(self):
        diagnosis = Tk()
        diag = DiagnosisWindow(diagnosis)
        diagnosis.title("Diagnosis Patient")
        diagnosis.geometry("1100x700+10+10")
        diagnosis.mainloop()


class DiagnosisWindow(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.lbl_head = Label(root, text="Medical Diagnosis Evaluation Form", bd=5, relief=GROOVE,
                              font=("times new Roman", 40, "bold"),
                              bg="violet", fg="blue")
        self.lbl_head.pack(side=TOP, fill=X)

        self.lbl1 = Label(root, text="Please fill in all field below with the patient's information", fg="purple",
                          font=("times new Roman", 14, "bold"))
        self.lbl1.place(x=350, y=90)

        #Section One Frame
        detail_frame = Frame(root, bd=4, relief=RIDGE)
        detail_frame.place(x=20, y=150, width=500, height=480)

        self.lbl_search = Label(detail_frame, text="Section 1: Demographics and Symptoms", fg="purple",
                                font=("times new Roman", 15, "bold"))
        self.lbl_search.place(x=10, y=10)

        #Variables
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

        self.lbl1 = Label(detail_frame, text="Name:", fg="purple", font=("times new Roman", 12, "bold"))
        self.lbl1.place(x=10, y=50)
        self.name = Entry(detail_frame, bd=3, width=30)
        self.name.place(x=250, y=50)

        self.lbl2 = Label(detail_frame, text="Age:", fg="purple",
                          font=("times new Roman", 12, "bold"))
        self.lbl2.place(x=10, y=100)
        self.temp = Entry(detail_frame, bd=3, width=10)
        self.temp.place(x=250, y=100)

        self.lbl3 = Label(detail_frame, text="Weight (in pounds):", fg="purple",
                          font=("times new Roman", 12, "bold"))
        self.lbl3.place(x=10, y=150)
        self.temp = Entry(detail_frame, bd=3, width=10)
        self.temp.place(x=250, y=150)

        self.lbl3 = Label(detail_frame, text=" Temperature (in degrees):", fg="purple",
                          font=("times new Roman", 12, "bold"))
        self.lbl3.place(x=10, y=200)
        self.temp = Entry(detail_frame, bd=3, width=10)
        self.temp.place(x=250, y=200)

        self.lbl = Label(detail_frame, text="The patient is experiencing Dizziness:", fg="purple",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=250)
        Radiobutton(detail_frame, text="yes", variable=self.var1, value=1).place(x=300, y=250)
        Radiobutton(detail_frame, text="no", variable=self.var1, value=0).place(x=370, y=250)

        self.lbl = Label(detail_frame, text="The patient is experiencing Fainting:", fg="purple",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=280)
        Radiobutton(detail_frame, text="yes", variable=self.var2, value=1).place(x=300, y=280)
        Radiobutton(detail_frame, text="no", variable=self.var2, value=0).place(x=370, y=280)

        self.lbl = Label(detail_frame, text="The patient is experiencing Blurred Vision:", fg="purple",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=310)
        Radiobutton(detail_frame, text="yes", variable=self.var3, value=1).place(x=300, y=310)
        Radiobutton(detail_frame, text="no", variable=self.var3, value=0).place(x=370, y=310)

        #History Frame
        history_frame = Frame(root, bd=4, relief=RIDGE)
        history_frame.place(x=570, y=150, width=500, height=480)

        self.lbl_search = Label(history_frame, text="Section 2: Patient Medical History", fg="purple", font=("times new Roman", 15, "bold"))
        self.lbl_search.place(x=10, y=10)

        # Select all that applies...

        Checkbutton(history_frame, text="Heart Disease", variable=self.var1, onvalue=1, offvalue=0).place(x=10, y=50)
        Checkbutton(history_frame, text="Lung Conditions (including severe asthma,pneumonia,Cystic fibrosis)",
                    variable=self.var1, onvalue=1, offvalue=0).place(x=10, y=80)
        Checkbutton(history_frame, text="Weakened Immune System (including Organ transplants, HIV/AIDs,",
                    variable=self.var1, onvalue=1, offvalue=0).place(x=10, y=110)
        Checkbutton(history_frame, text="Diabetes", variable=self.var1, onvalue=1, offvalue=0).place(x=10, y=140)
        Checkbutton(history_frame, text="Hypertension", variable=self.var1, onvalue=1, offvalue=0).place(x=10, y=170)
        Checkbutton(history_frame, text="Chronic kidney or liver disease", variable=self.var1, onvalue=1, offvalue=0).place(x=10, y=200)
        Checkbutton(history_frame, text="Down Syndrom", variable=self.var1, onvalue=1,
                    offvalue=0).place(x=10, y=230)


        # Submit button
        self.submitBtn = Button(root, text="Submit", width=20, command=self.submit, bg="violet", fg="purple")
        self.submitBtn.place(x=400, y=650)

    # Function that queries prolog file
    def submit(self):
        name_var = self.name.get()
        temp_var = float(self.temp.get())
        print(name_var)
        dizzy_choice = int(self.var1.get())
        faint_choice = int(self.var2.get())
        vision_choice = int(self.var3.get())

        result = list(prolog.query("get_symptom(%s, %f, %d,%d,%d)." % (name_var, temp_var, dizzy_choice, faint_choice,
                                                                       vision_choice)))

        # return prolog.query("get_symptom(%d,%d,%d)." % (dizzy_choice,faint_choice,vision_choice))
        # write the result to file in prolog, then read from file to messagebox
        # tkinter.messagebox.showinfo("Your results", result)


root = Tk()
ob = MainWindow(root)
root.mainloop()
