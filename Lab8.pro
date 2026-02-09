area_rectangle(Length, Breadth, Area) :- Area is Length * Breadth.

celsius_to_fahrenheit(C, F) :- F is C * 9 / 5 + 32.

factorial(0, 1).
factorial(N, Result) :- N > 0, N_minus_1 is N - 1, factorial(N_minus_1, SubResult), Result is N * SubResult.

