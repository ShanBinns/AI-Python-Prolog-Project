import tkinter
import datetime
from pyswip import Prolog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# pip install pyswip


# view statistical data


prolog = Prolog()
prolog.consult("diagnosis.pl")

def add_symptom_to_file(variant,symptom,weight,bloodpressure_check):
    symptom_prolog_file = open("additional_symptoms.pl","a+")
    now = datetime.datetime.now()
    symptom_prolog_file.write("symptom(\"%s\", %s, %s, %i, %i).\n" %(now, variant, symptom, weight, bloodpressure_check.get()))
    symptom_prolog_file.close()
    tkinter.messagebox.showinfo("Symptom Added To File", "New Symptom Fact has been added")

class add_covid_fact:
    def __init__(self, root):
        self.root = root
        self.lbl_head = Label(root, text="Add Knowledge about the Covid-19 virus", bd=5, relief=GROOVE,
                              font=("times new Roman", 20, "bold"),
                              bg="gold", fg="blue")
        self.lbl_head.pack(side=TOP, fill=X)

        self.covid_symptomNameLabel = Label(root, text="Enter Covid-19 Symptom (eg. runny_nose):", fg="blue", font=("times new Roman", 12, "bold"))
        self.covid_symptomNameLabel.place(x=10, y=100)
        self.covid_symptomNameEntry = Entry(root, bd=3, width=20)
        self.covid_symptomNameEntry.place(x=320, y=100)

        self.covid_symptomWeightLabel = Label(root, text="Enter Fact Weight (eg. 10):", fg="blue", font=("times new Roman", 12, "bold"))
        self.covid_symptomWeightLabel.place(x=10, y=140)
        self.covid_symptomWeightEntry = Entry(root, bd=3, width=20)
        self.covid_symptomWeightEntry.place(x=320, y=140)
        self.requires_bloodpressure_check = BooleanVar()
        self.covid_factBtn = Button(
            root, 
            text="Submit Fact", 
            borderwidth=3, 
            relief="sunken", 
            command=(lambda: add_symptom_to_file("normal",self.covid_symptomNameEntry.get().replace(" ","_").lower(),int(self.covid_symptomWeightEntry.get()),self.requires_bloodpressure_check)),
            width=15, 
            height=2, 
            bg="gold",
            fg="medium blue",
            font=("times new Roman", 10, "bold")
        )
        self.covid_factBtn.place(x=250, y=200)
        checkButton = Checkbutton(
            root, 
            text="Requires Bloodpressure Check", 
            variable=self.requires_bloodpressure_check, 
            onvalue=1, 
            offvalue=0
        ).place(x=320,y=160)

class add_mu_fact:
    def __init__(self, root):
        self.root = root
        self.lbl_head = Label(root, text="Add Knowledge about the Mu Covid-19 variant", bd=5, relief=GROOVE,
                              font=("times new Roman", 20, "bold"),
                              bg="gold", fg="blue")
        self.lbl_head.pack(side=TOP, fill=X)

        self.covid_symptomNameLabel = Label(root, text="Enter Covid-19 Symptom (eg. runny_nose):", fg="blue", font=("times new Roman", 12, "bold"))
        self.covid_symptomNameLabel.place(x=10, y=100)
        self.covid_symptomNameEntry = Entry(root, bd=3, width=20)
        self.covid_symptomNameEntry.place(x=320, y=100)

        self.covid_symptomWeightLabel = Label(root, text="Enter Fact Weight (eg. 10):", fg="blue", font=("times new Roman", 12, "bold"))
        self.covid_symptomWeightLabel.place(x=10, y=140)
        self.covid_symptomWeightEntry = Entry(root, bd=3, width=20)
        self.covid_symptomWeightEntry.place(x=320, y=140)
        self.covid_factBtn = Button(
            root, 
            text="Submit Fact", 
            borderwidth=3, 
            relief="sunken", 
            command=(lambda: add_symptom_to_file("mu",self.covid_symptomNameEntry.get().replace(" ","_").lower(),int(self.covid_symptomWeightEntry.get()),self.requires_bloodpressure_check)),
            width=15, 
            height=2, 
            bg="gold",
            fg="medium blue",
            font=("times new Roman", 10, "bold")
        )
        self.covid_factBtn.place(x=250, y=200)
        self.requires_bloodpressure_check = BooleanVar()
        Checkbutton(
            root, 
            text="Requires Bloodpressure Check", 
            variable=self.requires_bloodpressure_check, 
            onvalue=1, 
            offvalue=0
        ).place(x=320,y=160)


class add_delta_fact:
    def __init__(self, root):
        self.root = root
        self.lbl_head = Label(root, text="Add Knowledge about the Delta Covid-19 variant", bd=5, relief=GROOVE,
                              font=("times new Roman", 20, "bold"),
                              bg="gold", fg="blue")
        self.lbl_head.pack(side=TOP, fill=X)

        self.covid_symptomNameLabel = Label(root, text="Enter Covid-19 Symptom (eg. runny_nose):", fg="blue", font=("times new Roman", 12, "bold"))
        self.covid_symptomNameLabel.place(x=10, y=100)
        self.covid_symptomNameEntry = Entry(root, bd=3, width=20)
        self.covid_symptomNameEntry.place(x=320, y=100)

        self.covid_symptomWeightLabel = Label(root, text="Enter Fact Weight (eg. 10):", fg="blue", font=("times new Roman", 12, "bold"))
        self.covid_symptomWeightLabel.place(x=10, y=140)
        self.covid_symptomWeightEntry = Entry(root, bd=3, width=20)
        self.covid_symptomWeightEntry.place(x=320, y=140)
        self.covid_factBtn = Button(
            root, 
            text="Submit Fact", 
            borderwidth=3, 
            relief="sunken", 
            command=(lambda: add_symptom_to_file("delta",self.covid_symptomNameEntry.get().replace(" ","_").lower(),int(self.covid_symptomWeightEntry.get()),self.requires_bloodpressure_check)),
            width=15, 
            height=2, 
            bg="gold",
            fg="medium blue",
            font=("times new Roman", 10, "bold")
        )
        self.covid_factBtn.place(x=250, y=200)
        self.requires_bloodpressure_check = BooleanVar()
        Checkbutton(
            root, 
            text="Requires Bloodpressure Check", 
            variable=self.requires_bloodpressure_check, 
            onvalue=1, 
            offvalue=0
        ).place(x=320,y=160)


class statistics:
    def __init__(self, root):
        self.root = root
        self.lbl_head = Label(root, text="MOH Covid-19 Statistical Data", bd=5, relief=GROOVE,
                              font=("times new Roman", 20, "bold"),bg="gold", fg="blue")
        self.lbl_head.pack(side=TOP, fill=X)

        self.statsLabel = Label(root, text="Below are the data from all patients:", fg="blue",
                                  font=("times new Roman", 14, "bold"))
        self.statsLabel.place(x=10, y=100)

        self.stats_data = Text(root,width=70,height=10, font=("", 10))
        self.stats_data.place(x=20, y=150)

        #Reads the stats from the text file, displaying data
        file = open("files.txt", "r")
        data = file.read()
        self.mild_occurence = data.count("mild")
        print("The number of patients with mild symptoms is", self.mild_occurence)

        self.stats_data.insert(END, "The number of patients with mild symptoms is", self.mild_occurence)


# Main window
class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("MOH Covid-19 Diagnosis System")
        self.root.geometry("1300x670+10+10")

        title = Label(self.root, text="MOH Covid-19 Diagnosis System", bd=5, relief=GROOVE,
                      font=("times new Roman", 40, "bold"), bg="gold", fg="blue")
        title.pack(side=TOP, fill=X)

        # Add Fact Buttons
        self.covidFactBtn = Button(self.root, text="Add Covid-19 Fact", width=20, height=2, command=self.add_covid_fact,
                                   bg="medium blue", fg="gold", font=("times new Roman", 13, "bold"))
        self.covidFactBtn.place(x=10, y=80)

        self.muFactBtn = Button(self.root, text="Add Mu Variant Fact", width=20, height=2, command=self.add_mu_fact,
                                bg="medium blue", fg="gold", font=("times new Roman", 13, "bold"))
        self.muFactBtn.place(x=300, y=80)

        self.deltaFactBtn = Button(self.root, text="Add Delta Variant Fact", width=20, height=2,
                                   command=self.add_delta_fact,
                                   bg="medium blue", fg="gold", font=("times new Roman", 13, "bold"))
        self.deltaFactBtn.place(x=600, y=80)

        self.statisticsBtn = Button(self.root, text="View Statistics", width=20, height=2,
                                   command=self.statistics,
                                   bg="medium blue", fg="gold", font=("times new Roman", 13, "bold"))
        self.statisticsBtn.place(x=900, y=80)


        self.lbl1 = Label(self.root, text="Use the quick link buttons to add facts or fill out the form below to "
                                          "diagnosis patient", fg="blue", font=("times new Roman", 14, "bold"))
        self.lbl1.place(x=200, y=160)

        # Section One Frame
        detail_frame = Frame(root, bd=4, relief=RIDGE)
        detail_frame.place(x=20, y=200, width=500, height=450)

        self.lbl_search = Label(detail_frame, text="Section 1: Patient Demographics and Health History", fg="blue",
                                font=("times new Roman", 15, "bold"))
        self.lbl_search.place(x=10, y=10)

        self.lbl1 = Label(detail_frame, text="Name:", font=("times new Roman", 12))
        self.lbl1.place(x=10, y=50)
        self.name = Entry(detail_frame, bd=3, width=25)
        self.name.place(x=200, y=50)

        self.lbl2 = Label(detail_frame, text="Age:", font=("times new Roman", 12))
        self.lbl2.place(x=10, y=92)
        self.age = Entry(detail_frame, bd=3, width=10)
        self.age.place(x=200, y=90)

        self.lbl3 = Label(detail_frame, text=" Temperature (in degrees):", font=("times new Roman", 12))
        self.lbl3.place(x=10, y=130)
        self.temp = Entry(detail_frame, bd=3, width=10)
        self.temp.place(x=200, y=130)

        # Checkbox Variables
        self.var_check1 = IntVar()
        self.var_check2 = IntVar()
        self.var_check3 = IntVar()
        self.var_check4 = IntVar()
        self.var_check5 = IntVar()
        self.var_check6 = IntVar()
        self.var_check7 = IntVar()
        self.var_check8 = IntVar()

        self.lbl = Label(detail_frame, text="Select all underlying illnesses that applies patient.", fg="blue",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=200)

        Checkbutton(detail_frame, text="Heart Disease", variable=self.var_check1, onvalue=1, offvalue=0).place(x=10,
                                                                                                               y=240)
        Checkbutton(detail_frame, text="Lung Conditions (including severe asthma,pneumonia,Cystic fibrosis)",
                    variable=self.var_check2, onvalue=1, offvalue=0).place(x=10, y=260)
        Checkbutton(detail_frame, text="Weakened Immune System (including Organ transplants, HIV/AIDs,",
                    variable=self.var_check3, onvalue=1, offvalue=0).place(x=10, y=280)
        Checkbutton(detail_frame, text="Diabetes", variable=self.var_check4, onvalue=1, offvalue=0).place(x=10, y=300)
        Checkbutton(detail_frame, text="Hypertension", variable=self.var_check5, onvalue=1, offvalue=0).place(x=10,
                                                                                                              y=320)
        Checkbutton(detail_frame, text="Chronic kidney or liver disease", variable=self.var_check6, onvalue=1,
                    offvalue=0).place(x=10, y=340)
        Checkbutton(detail_frame, text="Down Syndrome", variable=self.var_check7, onvalue=1, offvalue=0).place(x=10,
                                                                                                               y=360)
        Checkbutton(detail_frame, text="Obesity", variable=self.var_check8, onvalue=1, offvalue=0).place(x=10, y=380)

        # List to save checkbox responses
        self.List = []
        self.varList = []
        self.varList.append(self.var_check1)
        self.varList.append(self.var_check2)
        self.varList.append(self.var_check3)
        self.varList.append(self.var_check4)
        self.varList.append(self.var_check5)
        self.varList.append(self.var_check6)
        self.varList.append(self.var_check7)
        self.varList.append(self.var_check8)

        # Patient history frame
        history_frame = Frame(root, bd=4, relief=RIDGE)
        history_frame.place(x=570, y=200, width=500, height=450)

        self.lbl_search = Label(history_frame, text="Section 2: Patient Medical History", fg="blue",
                                font=("times new Roman", 15, "bold"))
        self.lbl_search.place(x=10, y=10)

        self.lbl = Label(history_frame, text="Is the patient experiencing any of the following symptoms?", fg="blue",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=50)

        # RadioButton Variables
        self.vardiz = IntVar()
        self.varfai = IntVar()
        self.varvis = IntVar()
        self.var_cough = IntVar()
        self.varsho = IntVar()

        self.lbl = Label(history_frame, text="Dizziness:", font=("times new Roman", 12))
        self.lbl.place(x=10, y=90)
        Radiobutton(history_frame, text="yes", variable=self.vardiz, value=1).place(x=200, y=90)
        Radiobutton(history_frame, text="no", variable=self.vardiz, value=0).place(x=270, y=90)

        self.lbl = Label(history_frame, text="Fainting:", font=("times new Roman", 12))
        self.lbl.place(x=10, y=120)
        Radiobutton(history_frame, text="yes", variable=self.varfai, value=1).place(x=200, y=120)
        Radiobutton(history_frame, text="no", variable=self.varfai, value=0).place(x=270, y=120)

        self.lbl = Label(history_frame, text="Blurred Vision:", font=("times new Roman", 12))
        self.lbl.place(x=10, y=150)
        Radiobutton(history_frame, text="yes", variable=self.varvis, value=1).place(x=200, y=150)
        Radiobutton(history_frame, text="no", variable=self.varvis, value=0).place(x=270, y=150)

        self.lbl = Label(history_frame, text="Cough:", font=("times new Roman", 12))
        self.lbl.place(x=10, y=180)
        Radiobutton(history_frame, text="yes", variable=self.var_cough, value=1).place(x=200, y=180)
        Radiobutton(history_frame, text="no", variable=self.var_cough, value=0).place(x=270, y=180)

        self.lbl = Label(history_frame, text="Shortness of Breath:", font=("times new Roman", 12))
        self.lbl.place(x=10, y=210)
        Radiobutton(history_frame, text="yes", variable=self.varsho, value=1).place(x=200, y=210)
        Radiobutton(history_frame, text="no", variable=self.varsho, value=0).place(x=270, y=210)

        # Blood Pressure
        self.lbl = Label(history_frame, text="Please enter blood pressure reading", fg="blue",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=250)

        self.lbl2 = Label(history_frame, text="Systolic:", font=("times new Roman", 12))
        self.lbl2.place(x=10, y=280)
        self.systolic = Entry(history_frame, bd=3, width=10)
        self.systolic.place(x=200, y=280)

        self.lbl2 = Label(history_frame, text="Diastolic:", font=("times new Roman", 12))
        self.lbl2.place(x=10, y=310)
        self.diastolic = Entry(history_frame, bd=3, width=10)
        self.diastolic.place(x=200, y=310)

        # Submit button
        self.submitBtn = Button(root, text="Diagnose Patient", borderwidth=3, relief="sunken", command=self.submit,
                                width=20, height=2, bg="gold", fg="medium blue", font=("times new Roman", 12, "bold"))
        self.submitBtn.place(x=1090, y=600)

    # Function that queries prolog file
    def submit(self):
        name_var = self.name.get()
        temp_var = float(self.temp.get())
        age_var = int(self.age.get())

        history_var = IntVar()

        dizzy_choice = int(self.vardiz.get())
        faint_choice = int(self.varfai.get())
        vision_choice = int(self.varvis.get())
        cough_choice = int(self.var_cough.get())
        shortbreath_choice = int(self.varsho.get())

        systolic_var = int(self.systolic.get())
        diastolic_var = int(self.diastolic.get())

        # Checkbox
        def isChecked():
            global List

            List = []
            for item in self.varList:
                if item.get() != "":
                    List.append(item.get())

        isChecked()
        # print(List)
        if 1 in List:
            history_var = 1
        else:
            history_var = 0

        result = list(prolog.query("get_symptom(%s,%f,%d,%d,%d,%d,%d,%d,%d,%d,%d)."
                                   % (
                                       name_var, temp_var, age_var, dizzy_choice, faint_choice, vision_choice,
                                       cough_choice, shortbreath_choice, history_var, systolic_var, diastolic_var)))
        tkinter.messagebox.showinfo("Completed", "Patient information Submitted")



    # functions for add fact buttons
    def add_covid_fact(self):
        covid_fact = Tk()
        cfact = add_covid_fact(covid_fact)
        covid_fact.title("Add Covid Fact")
        covid_fact.geometry("600x400+10+10")
        covid_fact.mainloop()

    def add_mu_fact(self):
        mu_fact = Tk()
        mfact = add_mu_fact(mu_fact)
        mu_fact.title("Add Mu Variant Fact")
        mu_fact.geometry("600x400+10+10")
        mu_fact.mainloop()

    def add_delta_fact(self):
        delta_fact = Tk()
        dfact = add_delta_fact(delta_fact)
        delta_fact.title("Add Delta Variant Fact")
        delta_fact.geometry("600x400+10+10")
        delta_fact.mainloop()

    def statistics(self):
        stats = Tk()
        s = statistics(stats)
        stats.title("View Statistics")
        stats.geometry("600x400+10+10")
        stats.mainloop()

root = Tk()
ob = MainWindow(root)
root.mainloop()
