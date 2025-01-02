sum(1, N) :-
   N = 1.
sum(N, Total) :-
   N1 is N - 1,
   sum(N1, RemainingTotal),
   Total is N + RemainingTotal.