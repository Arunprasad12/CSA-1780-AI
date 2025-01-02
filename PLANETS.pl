planet(mercury, rocky, 0.39, 88,1994).
planet(venus, rocky, 0.72, 225,1982).
planet(earth, rocky, 1, 365,1970).
planet(mars, rocky, 1.52, 687,1985).
planet(jupiter, gas_giant, 5.2,2004).
planet(saturn, gas_giant, 9.58,1998).
planet(uranus, ice_giant, 19.22,2009).
planet(neptune, ice_giant, 30.05,2016).

planet_info(Name, Type, Distance, OrbitDays,year) :-
    planet(Name, Type, Distance, OrbitDays,year).
rocky_planet(Name) :-
    planet(Name, rocky,_ , _,_).
gas_giant_planet(Name) :-
    planet(Name, gas_giant, _, _,_).
ice_giant_planet(Name) :-
    planet(Name, ice_giant, _, _,_).