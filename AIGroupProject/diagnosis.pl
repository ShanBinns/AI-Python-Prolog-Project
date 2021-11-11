/*   get_symptom(timothy,40.0,70,1,1,0,0,0,1,135,80).
f = open("demofile3.txt", "w")

  f.write("Woops! I have deleted the content!")

f.close()



  #open and read the file after the appending:

f = open("demofile3.txt", "r")

  print(f.read())
*/

get_symptom(Name,Temp,Age,Dizziness,Fainting,Vision,Coughing,Short_Breath,History,Systolic,Diastolic):-


            nl,write("**************DIAGNOSIS***************"),nl,

		   (Temperature is Temp * 9/5 + 32),
           (Temperature > 100 -> Tempval is 1; Tempval is 0),
           (Age > 65 -> Ageval is 1; Ageval is 0),

		   write(Temp),nl,write(Name),nl,write(Age),nl,

			%commonsymptoms
           (Dizziness is 1 ->  Dizzyvalue is 1;Dizzyvalue is 0),
           (Fainting is 1 -> Faintvalue is 1;Faintvalue is 0),
           (Vision is 1 -> Visionvalue is 1;Visionvalue is 0),
		   (Coughing is 1 ->  Coughingvalue is 1;Coughingvalue is 0),

		   %SeriousSymptoms
           (Short_Breath is 1 -> Breathingvalue is 1;Breathingvalue is 0),

		   %UnderlyingIllness
		   (History is 1 -> HighRiskvalue is 3;HighRiskvalue is 0),

		   %Bloodpressure
            blood_pressure(Systolic,Diastolic,BPrisk,BPcom),
		   assess_risk(Name,Tempval,Ageval,Dizzyvalue,Faintvalue,Visionvalue,Coughingvalue,Breathingvalue,HighRiskvalue),
		   recommendations(Name,Temperature,Age,BPrisk,BPcom).


%Fix_this_function
blood_pressure(Systolic,Diastolic,BPrisk,BPcom):-nl,BPrisk is 0,BPcom is 0,
           (Systolic >= 120),(Systolic < 130),(Diastolic < 80) -> BPrisk is 1, BPcom = "elevated BP", 
           ((Systolic >= 130),(Systolic < 140)); ((Diastolic >= 80),(Diastolic < 90) ) -> BPrisk is 2,BPcom = "stage 1 hypertension".
       /*    ((Systolic>=140); (Diastolic>=90) )-> BPrisk is 3,BPcom = "stage 2 hypertension", write(BPrisk),write(BPcom).*/




assess_risk(Name,Tempval,Ageval,Dizzyvalue,Faintvalue,Visionvalue,Coughingvalue,Breathingvalue,HighRiskvalue):-
			Riskvalue is Tempval + Dizzyvalue + Faintvalue + Visionvalue + HighRiskvalue + Ageval + Coughingvalue +Breathingvalue,

			(Riskvalue > 2 -> nl,write("Final Diagnosis: "),write(Name),write(" is at risk"),nl;
			nl,write("Final Diagnosis "),write(Name),write(" is not at risk"),nl).



recommendations(Name,Temperature,Age,BPrisk,BPcom):- nl,write("****COMMENTS AND RECOMMENDATION*****"),nl,
						  write("**Based on analysis, the following factors puts patient "),write(Name),write(" at risk**"),nl,nl,
                         (Temperature > 100) -> write("A fever, with a high temperature value of "),write(Temperature),nl,
                         (Age > 65) -> write("Age risk: "),write(Age),nl,
						 (BPrisk > 0) -> write("Experiencing : "),write(BPcom).

