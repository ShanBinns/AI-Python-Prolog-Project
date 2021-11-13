/*get_symptom(timothy,40.0,70,1,1,0,0,0,1,135,80).     get_symptom(sara,25.0,70,0,0,0,0,0,0,135,80). */
list_member(X,[X|_]).
list_member(X,[_|TAIL]) :- list_member(X,TAIL).

symptoms_of_patient(PATIENT,SYMPTOMS) :-
	patient(_, PATIENT, _, _, _, _, SYMPTOMS).

is_a_patient_symptom(PATIENT,SYMPTOM) :-
	symptoms_of_patient(PATIENT,SYMPTOMS),
	list_member(SYMPTOM, SYMPTOMS).


get_symptom(Name,Temp,Age,Dizziness,Fainting,Vision,Coughing,Short_Breath,History,Systolic,Diastolic):-

            nl,nl,write("**************DIAGNOSIS***************"),nl,

		   (Temperature is Temp * 9/5 + 32),
           (Temperature > 100 -> Tempval is 1; Tempval is 0),
           (Age > 65 -> Ageval is 1; Ageval is 0),

			%commonsymptoms
           (Dizziness is 1 ->  Dizzyvalue is 1, Isdizzy = "yes";Dizzyvalue is 0, Isdizzy = "no"),
           (Fainting is 1 -> Faintvalue is 1, IsFaint = "yes";Faintvalue is 0, IsFaint = "no"),
           (Vision is 1 -> Visionvalue is 1, IsBlurry = "yes";Visionvalue is 0, IsBlurry = "no"),
		   (Coughing is 1 ->  Coughingvalue is 1, IsCough = "yes";Coughingvalue is 0, IsCough = "no"),

		   %SeriousSymptoms
           (Short_Breath is 1 -> Breathingvalue is 1, IsShortBreath = "yes";Breathingvalue is 0, IsShortBreath = "no"),

		   %UnderlyingIllness
		   (History is 1 -> HighRiskvalue is 3, IsUnderlyingIllness = "yes";HighRiskvalue is 0, IsUnderlyingIllness = "no"),

		   %analysisfunctions
			blood_pressure(Systolic,Diastolic,BPrisk,BPcom),
			assess_risk(Name,Tempval,Ageval,Dizzyvalue,Faintvalue,Visionvalue,Coughingvalue,Breathingvalue,HighRiskvalue,BPrisk,Symptomval,Riskvalue),
			
			%readandwritetofile
			file_write(Name,Age,Temperature,Isdizzy,IsFaint,IsBlurry,IsCough,IsShortBreath,IsUnderlyingIllness,BPcom,Symptomval,Riskvalue),
			file_read,
			
			
		    recommendations(Name,Temperature,Age,BPrisk,BPcom).





blood_pressure(Systolic,Diastolic,BPrisk,BPcom):-nl,BPrisk is 0,BPcom = "no comment",
			((Systolic < 90) -> BPrisk is 2,BPcom = "Low Blood Pressure");
			((Diastolic < 60) -> BPrisk is 2,BPcom = "Low Blood Pressure");
            ((Systolic >= 130) -> BPrisk is 2,BPcom = "Hypertension");
		    ((Diastolic >= 80) -> BPrisk is 2,BPcom = "Hypertension").



assess_risk(Name,Tempval,Ageval,Dizzyvalue,Faintvalue,Visionvalue,Coughingvalue,Breathingvalue,HighRiskvalue,BPrisk,Symptomval,Riskvalue):-
			Riskvalue is Tempval + Dizzyvalue + Faintvalue + Visionvalue + HighRiskvalue + Ageval + Coughingvalue +Breathingvalue+BPrisk,

			/*Low Risk < 3
			Medium Risk 3 - 6
			High Risk >= 6*/

			(Riskvalue < 3 -> write("Final Diagnosis: "),write(Name),write("  has a low at risk for Corona virus"),Symptomval="mild",nl;
			(Riskvalue >= 3,Riskvalue < 6) -> write("Final Diagnosis: "),write(Name),write("  has a medium at risk for Corona virus"),Symptomval="mild",nl;
			Riskvalue >= 6 -> write("Final Diagnosis: "),write(Name),write(" is at high risk for Corona virus"),Symptomval="severe",nl).



recommendations(Name,Temperature,Age,BPrisk,BPcom):- nl,write("****COMMENTS AND RECOMMENDATION*****"),nl,
						  write("*Based on analysis, the following factors puts patient "),write(Name),write(" at risk*"),nl,nl,
						 (BPrisk > 0) -> nl,write("*Experiencing : "),write(BPcom),

                         (Temperature > 100) -> nl,nl,write("*A fever, with a high temperature value of "),write(Temperature),nl,
						 write(". N.B. Patient is symptomatic and must stay home until symptoms subsides. Patient must be adviced to stay intouch with their doctor, monitor symptoms and isolate."),
                         (Age > 65) -> nl,nl,write("*Age risk: "),write(Age),nl,
						 write("N.B. Older adults are more likely to be hospitalized or die. Patient must be advised to get fully vaccinated, and practice social distancing."),
						 (Temperature < 100,Age < 65,BPrisk == 0) -> write("Patient is Healthy").

file_read:-
    open('files.txt',read,Str),
    get_char(Str, Output),
    process_stream(Output,Str),
    close(Str).

process_stream(end_of_file,_):-!.
process_stream(Char,Str):-write(Char),get_char(Str,Char2),process_stream(Char2,Str).


file_write(Name,Age,Temperature,Isdizzy,IsFaint,IsBlurry,IsCough,IsShortBreath,IsUnderlyingIllness,BPcom,Symptomval,Riskvalue):-
				open('files.txt',append,Str),
				nl(Str),    
				write(Str,' Name:'),write(Str,Name),
				write(Str,' Age:'),write(Str,Age),
				write(Str,' Temperature:'),write(Str,Temperature),
				write(Str,' Dizziness:'),write(Str,Isdizzy),
				write(Str,' Faintness:'),write(Str,IsFaint),
				write(Str,' BlurredVision:'),write(Str,IsBlurry),
				write(Str,' Coughing:'),write(Str,IsCough),
				write(Str,' ShortnessOfBreath:'),write(Str,IsShortBreath),
				write(Str,' UnderlyingIllness:'),write(Str,IsUnderlyingIllness),
				write(Str,' BloodPressure:'),write(Str,BPcom),
				write(Str,' Severity:'),write(Str,Symptomval),
				write(Str,' Riskvalue:'),write(Str,Riskvalue),
				close(Str).





/*write("Please advice Patient to regular blood pressure and practice social distancing."),

(History > 0) -> nl,nl,write("*Underlying Illness Risk: "),nl,write("N.B.Persons with underlying illnesses are at greater risk of severe illness from Covid-19. Patient must be adviced to isolate and contact their medical practioner."),write("Please advice Patient to regular blood pressure and practice social distancing."),*/
