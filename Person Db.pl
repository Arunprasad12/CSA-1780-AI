person(john, date(1990, 5, 15)).
person(emma, date(1985, 12, 8)).
person(michael, date(1995, 3, 22)).
dob_for_person(Name, DOB) :-
    person(Name, DOB).
is_person_in_db(Name) :-
    person(Name, _).