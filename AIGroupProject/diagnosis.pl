

get_symptom(Name,Temp,Dizziness,Fainting,Vision):-
           (Temperature is Temp * 9/5 + 32),
		   
            nl,write("****************DIAGNOSIS*****************"),nl,
			
            write(Temperature),nl,write(Name),nl,
			(Temperature > 100 -> Tempval is 1; Tempval is 0),
           (Dizziness is 1 ->  Dizzyvalue is 1;Dizzyvalue is 0),
           (Fainting is 1 -> Faintvalue is 1;Faintvalue is 0),
           (Vision is 1 -> Visionvalue is 1;Visionvalue is 0),

			Riskvalue is Tempval+Dizzyvalue+Faintvalue+Visionvalue,
			(Riskvalue > 2 -> nl,write("Patient: "),write(Name),write(" is at risk"),nl;
			nl,write("Patient "),write(Name),write(" is not at risk"),nl).