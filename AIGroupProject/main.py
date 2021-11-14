import tkinter
import datetime
from pyswip import Prolog
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# pip install pyswip

#touch necessary files
f = open("diagnosis.pl","a")
f.close()
f = open("stakeholders.pl","a")
f.close()
f = open("additional_symptoms.pl","a")
f.close()
f = open("patients.pl","a")
f.close()
# view statistical data
prolog = Prolog()
prolog.consult("diagnosis.pl")
prolog.consult("stakeholders.pl")
prolog.consult("additional_symptoms.pl")
prolog.consult("illnesses.pl")
prolog.consult("patients.pl")

def get_symptom_weight(symptom_name):
    symptoms = []
    for symptom in prolog.query("stakeholder_symptom(_, SYMPTOM, WEIGHT, PRESSURE_CHECK)"):
        if(symptom["SYMPTOM"] == symptom_name):
            return symptom["WEIGHT"]
    for symptom in prolog.query("additional_symptom(_, SYMPTOM, WEIGHT, PRESSURE_CHECK)"):
        if(symptom["SYMPTOM"] == symptom_name):
            return symptom["WEIGHT"]
    return None

def get_risk(variant,symptoms_array):
    count = 0
    weight = 0
    total_weight = 0

    for symptom in prolog.query("stakeholder_symptom(%s, SYMPTOM, WEIGHT, PRESSURE_CHECK)" %(variant)):
        total_weight = total_weight + symptom["WEIGHT"]
        if(symptoms_array.count(symptom["SYMPTOM"])):
            weight = weight + int(symptom["WEIGHT"])
        count = count + 1

    for symptom in prolog.query("additional_symptom(%s, SYMPTOM, WEIGHT, PRESSURE_CHECK)" %(variant)):
        total_weight = total_weight + symptom["WEIGHT"]
        if(symptoms_array.count(symptom["SYMPTOM"])):
            weight = weight + int(symptom["WEIGHT"])
        count = count + 1

    if(total_weight == 0):
        total_weight = 1
    risk = (weight / total_weight) * 100
    return '%.2f' % risk

def get_symptoms():
    symptoms = []
    for symptom in prolog.query("stakeholder_symptom(_, SYMPTOM, WEIGHT, PRESSURE_CHECK)"):
        if(not(symptoms.count(symptom["SYMPTOM"]))):
            symptoms.append(symptom["SYMPTOM"])
    for symptom in prolog.query("additional_symptom(_, SYMPTOM, WEIGHT, PRESSURE_CHECK)"):
        if(not(symptoms.count(symptom["SYMPTOM"]))):
            symptoms.append(symptom["SYMPTOM"])
    return symptoms

def get_patient_diagnostic(name):
    prolog.consult("diagnosis.pl")
    symptoms = get_symptoms()
    diagnostic = ""
    patient_symptoms = []
    for symptom in symptoms:
        for symp in prolog.query("is_a_patient_symptom(%s,%s)" %(name, symptom)):
            patient_symptoms.append(symptom)

    gen_risk = get_risk('normal',patient_symptoms)
    mu_risk = get_risk('mu',patient_symptoms)
    delta_risk = get_risk('delta',patient_symptoms)
    diagnostic = "GENERAL VARIANT RISK: %{gen_risk}\nMU VARIANT RISK: %{mu_risk}\nDELTA VARIANT RISK: %{delta_risk}".format(gen_risk=gen_risk,mu_risk=mu_risk,delta_risk=delta_risk)
    return diagnostic

def get_illnesses():
    illnesses = []
    for illness in prolog.query("illness(_, ILLNESS, WEIGHT, PRESSURE_CHECK)"):
        if(not(illnesses.count(illness["ILLNESS"]))):
            illnesses.append(illness["ILLNESS"])
    return illnesses

def add_patient_to_file(name, age, temperature, bloodpressure, illnesses, symptoms):
    patientsProlog = open("patients.pl","a+")
    now = datetime.datetime.now()
    bloodpressure_string = str(bloodpressure)
    temperature_string = str(temperature)
    symptoms_string = str(symptoms)
    illnesses_string = str(illnesses)
    patientsProlog.write("patient(\"%s\", %s, %i, %s, %s, %s, %s).\n" %(now, name, age, temperature_string, bloodpressure_string, illnesses_string, symptoms_string))
    patientsProlog.close()
    tkinter.messagebox.showinfo("Patient Added To File", "New Patient Has Been Added")

def add_symptom_to_file(variant,symptom,weight,bloodpressure_check):
    symptom_prolog_file = open("additional_symptoms.pl","a+")
    symptom_prolog_file.write("additional_symptom(%s, %s, %i, %i).\n" %(variant, symptom, weight, bloodpressure_check.get()))
    symptom_prolog_file.close()
    tkinter.messagebox.showinfo("Symptom Added To Database", "New Symptom Fact has been added")

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

        illnesses = get_illnesses()
        self.illnessCheckBoxValues = []
        for illness in illnesses:
            self.illnessCheckBoxValues.append(IntVar())

        self.lbl = Label(detail_frame, text="Select all underlying illnesses that applies patient.", fg="blue", font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=200)
        position_x = 10
        position_y = 240
        for illness in enumerate(illnesses):
            Checkbutton(detail_frame, text=illness[1], variable=self.illnessCheckBoxValues[illness[0]], onvalue=1, offvalue=0).place(x=position_x,y=position_y)
            position_y = position_y + 20

        # List to save checkbox responses
        self.List = []
        self.varList = []
        for illness in enumerate(illnesses):
            self.varList.append(illness)

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
        symptoms = get_symptoms()
        self.symptomCheckBoxValues = []
        for symptom in symptoms:
            self.symptomCheckBoxValues.append(IntVar())

        position_x = 10
        position_y = 90
        for symptom in enumerate(symptoms):
            self.lbl = Label(history_frame, text=symptom[1]+":", font=("times new Roman", 12))
            self.lbl.place(x=10, y=position_y)
            Radiobutton(history_frame, text="yes", variable=self.symptomCheckBoxValues[symptom[0]], value=1).place(x=200, y=position_y)
            Radiobutton(history_frame, text="no", variable=self.symptomCheckBoxValues[symptom[0]], value=0).place(x=270, y=position_y)
            position_y = position_y + 30

        # Blood Pressure
        self.lbl = Label(history_frame, text="Please enter blood pressure reading", fg="blue",
                         font=("times new Roman", 12, "bold"))
        self.lbl.place(x=10, y=340)

        self.lbl2 = Label(history_frame, text="Systolic:", font=("times new Roman", 12))
        self.lbl2.place(x=10, y=370)
        self.systolic = Entry(history_frame, bd=3, width=10)
        self.systolic.place(x=200, y=370)

        self.lbl2 = Label(history_frame, text="Diastolic:", font=("times new Roman", 12))
        self.lbl2.place(x=10, y=400)
        self.diastolic = Entry(history_frame, bd=3, width=10)
        self.diastolic.place(x=200, y=400)

        # Submit button
        self.submitBtn = Button(root, text="Diagnose Patient", borderwidth=3, relief="sunken", command=self.submit,
                                width=20, height=2, bg="gold", fg="medium blue", font=("times new Roman", 12, "bold"))
        self.submitBtn.place(x=1090, y=600)

    # Function that queries prolog file
    def submit(self):
        name = self.name.get()
        age = int(self.age.get())
        temperature = float(self.temp.get())
        
        systolic_var = int(self.systolic.get())
        diastolic_var = int(self.diastolic.get())
        bloodpressure = [diastolic_var, systolic_var]

        illnesses = get_illnesses()
        chosen_illnesses = []
        for illness in enumerate(illnesses):
            if(self.illnessCheckBoxValues[illness[0]].get()):
                chosen_illnesses.append(illness[1])
        
        symptoms = get_symptoms()
        chosen_symptoms = []
        for symptom in enumerate(symptoms):
            if(self.symptomCheckBoxValues[symptom[0]].get()):
                chosen_symptoms.append(symptom[1])
        
        add_patient_to_file(name, age, temperature, bloodpressure, chosen_illnesses, chosen_symptoms)
        prolog.consult("patients.pl")
        tkinter.messagebox.showinfo("%s's Diagnosis"%(name), str(get_patient_diagnostic(name)))
        print(str(get_patient_diagnostic(name)))

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
