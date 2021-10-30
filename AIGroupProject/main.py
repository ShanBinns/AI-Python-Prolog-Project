from pyswip import Prolog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# pip install pyswip



prolog = Prolog()
prolog.consult("diagnosis.pl")


class DiagnosisWindow:
    def __init__(self, root):
        self.root = root
        self.lbl_head = Label(root, text="Medical Diagnosis Evaluation Form", bd=5, relief=GROOVE,
                              font=("times new Roman", 20, "bold"),
                              bg="lavender", fg="blue")
        self.lbl_head.pack(side=TOP, fill=X)

        self.lbl1 = Label(root, text="Please fill in all field below with the patient's information", fg="blue",
                          font=("times new Roman", 14, "bold"))
        self.lbl1.place(x=150, y=50)









# Main window
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("MOH Covid-19 Diagnosis System")
        self.root.geometry("1300x670+10+10")

        title = Label(self.root, text="MOH Covid-19 Diagnosis System", bd=5, relief=GROOVE,
                      font=("times new Roman", 40, "bold"), bg="gold", fg="blue")
        title.pack(side=TOP, fill=X)

        #Add Fact Buttons
        self.covidFactBtn = Button(self.root,text="Add Covid-19 Fact",width=20,height=2,command=print(),
                                   bg="blue", fg="gold",font=("times new Roman", 12, "bold"))
        self.covidFactBtn.place(x=300, y=80)

        self.muFactBtn = Button(self.root, text="Add Mu Variant Fact", width=20, height=2, command=print(),
                                bg="blue", fg="gold",font=("times new Roman", 12, "bold"))
        self.muFactBtn.place(x=600, y=80)

        self.deltaFactBtn = Button(self.root, text="Add Delta Variant Fact", width=20, height=2, command=print(),
                                   bg="blue", fg="gold",font=("times new Roman", 12, "bold"))
        self.deltaFactBtn.place(x=900, y=80)

        self.lbl1 = Label(self.root, text="Please fill in all field below with the patient's information", fg="blue",
                          font=("times new Roman", 14, "bold"))
        self.lbl1.place(x=400, y=160)

        # Section One Frame
        detail_frame = Frame(root, bd=4, relief=RIDGE)
        detail_frame.place(x=20, y=200, width=500, height=450)

        # RadioButton Variables
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()

        self.lbl_search = Label(detail_frame, text="Section 1: Demographics and Symptoms", fg="blue",
                                font=("times new Roman", 15, "bold"))
        self.lbl_search.place(x=10, y=10)

        self.lbl1 = Label(detail_frame, text="Name:", fg="blue", font=("times new Roman", 12, "bold"))
        self.lbl1.place(x=10, y=50)
        self.name = Entry(detail_frame, bd=3, width=30)
        self.name.place(x=300, y=50)

        self.lbl2 = Label(detail_frame, text="Age:", fg="blue",
                          font=("times new Roman", 12, "bold"))
        self.lbl2.place(x=10, y=92)
        self.temp = Entry(detail_frame, bd=3, width=10)
        self.temp.place(x=300, y=90)

        self.lbl3 = Label(detail_frame, text="Weight (in pounds):", fg="blue",
                          font=("times new Roman", 12, "bold"))
        self.lbl3.place(x=10, y=130)
        self.temp = Entry(detail_frame, bd=3, width=10)
        self.temp.place(x=300, y=130)

        self.lbl3 = Label(detail_frame, text=" Temperature (in degrees):", fg="blue",
                          font=("times new Roman", 12, "bold"))
        self.lbl3.place(x=10, y=170)
        self.temp = Entry(detail_frame, bd=3, width=10)
        self.temp.place(x=300, y=170)

        self.lbl = Label(detail_frame, text="The patient is experiencing Dizziness:", fg="blue",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=210)
        Radiobutton(detail_frame, text="yes", variable=self.var1, value=1).place(x=300, y=210)
        Radiobutton(detail_frame, text="no", variable=self.var1, value=0).place(x=370,y=210)

        self.lbl = Label(detail_frame, text="The patient is experiencing Fainting:", fg="blue",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=240)
        Radiobutton(detail_frame, text="yes", variable=self.var2, value=1).place(x=300, y=240)
        Radiobutton(detail_frame, text="no", variable=self.var2, value=0).place(x=370, y=240)

        self.lbl = Label(detail_frame, text="The patient is experiencing Blurred Vision:", fg="blue",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=280)
        Radiobutton(detail_frame, text="yes", variable=self.var3, value=1).place(x=300, y=280)
        Radiobutton(detail_frame, text="no", variable=self.var3, value=0).place(x=370, y=280)

        #Patient history frame
        history_frame = Frame(root, bd=4, relief=RIDGE)
        history_frame.place(x=570, y=200, width=500, height=450)

        # Checkbox Variables
        self.var_check1 = IntVar()
        self.var_check2 = IntVar()
        self.var_check3 = IntVar()
        self.var_check4 = IntVar()
        self.var_check5 = IntVar()
        self.var_check6 = IntVar()
        self.var_check7 = IntVar()

        self.lbl_search = Label(history_frame, text="Section 2: Patient Medical History", fg="blue",
                                font=("times new Roman", 15, "bold"))
        self.lbl_search.place(x=10, y=10)

        self.lbl = Label(history_frame, text="Select all that applies.", fg="blue", font=("times new Roman", 12))
        self.lbl.place(x=10, y=50)

        Checkbutton(history_frame, text="Heart Disease", variable=self.var_check1,onvalue=1,offvalue=0).place(x=10,y=80)
        Checkbutton(history_frame, text="Lung Conditions (including severe asthma,pneumonia,Cystic fibrosis)",
                    variable=self.var_check2, onvalue=1, offvalue=0).place(x=10, y=110)
        Checkbutton(history_frame, text="Weakened Immune System (including Organ transplants, HIV/AIDs,",
                    variable=self.var_check3, onvalue=1, offvalue=0).place(x=10, y=140)
        Checkbutton(history_frame, text="Diabetes", variable=self.var_check4, onvalue=1, offvalue=0).place(x=10, y=170)
        Checkbutton(history_frame, text="Hypertension",variable=self.var_check5,onvalue=1,offvalue=0).place(x=10,y=200)
        Checkbutton(history_frame, text="Chronic kidney or liver disease", variable=self.var_check6, onvalue=1,
                    offvalue=0).place(x=10, y=230)
        Checkbutton(history_frame, text="Down Syndrome",variable=self.var_check7,onvalue=1,offvalue=0).place(x=10,y=260)

        # Submit button
        self.submitBtn = Button(root, text="submit",command=self.submit,width=30,height=2, bg="blue", fg="gold",font=("times new Roman", 12, "bold"))
        self.submitBtn.place(x=1100, y=600)

    # Function that queries prolog file
    def submit(self):
        name_var = self.name.get()
      #  temp_var = float(self.temp.get())
        dizzy_choice = int(self.var1.get())
        faint_choice = int(self.var2.get())
        vision_choice = int(self.var3.get())
        history_var = IntVar()


        def isChecked():
            for c in (self.var_check1.get(),self.var_check2.get(),self.var_check3.get(),self.var_check4.get(),
                      self.var_check4.get(),self.var_check6.get(),self.var_check7.get()):
               if c==1:
                   break
                   history_var = 1
                   print(history_var)
                   break
               else:
                   break
                   history_var = 0
                   print(history_var)





        isChecked()
        print(history_var)



        #result = list(prolog.query("get_symptom(%s, %f, %d,%d,%d)." % (name_var, temp_var, dizzy_choice, faint_choice,
             #                                                          vision_choice)))

        # return prolog.query("get_symptom(%d,%d,%d)." % (dizzy_choice,faint_choice,vision_choice))
        # write the result to file in prolog, then read from file to messagebox
        # tkinter.messagebox.showinfo("Your results", result)

    def diagnosis_window(self):
        diagnosis = Tk()
        diag = DiagnosisWindow(diagnosis)
        diagnosis.title("Diagnosis Patient")
        diagnosis.geometry("1200x1000+10+10")
        diagnosis.mainloop()


root = Tk()
ob = MainWindow(root)
root.mainloop()
