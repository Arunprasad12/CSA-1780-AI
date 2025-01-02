symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, nausea).

disease(flu, fever).
disease(flu, cough).
disease(stress, headache).
disease(food_poisoning, nausea).

% Backward chaining procedure to diagnose disease
diagnose(Person, Disease) :-
    symptom(Person, Symptom),
    disease(Disease, Symptom).

% Example queries
% Query to find what disease John may have
% ?- diagnose(john, Disease).
%
% Query to find what disease Jane may have
% ?- diagnose(jane, Disease).

