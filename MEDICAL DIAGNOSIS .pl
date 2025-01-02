symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, nausea).

disease(fever, flu).
disease(cough, flu).
disease(headache, stress).
disease(nausea, food_poisoning).

diagnosis(Person, Disease) :-
    symptom(Person, Symptom),
    disease(Symptom, Disease).