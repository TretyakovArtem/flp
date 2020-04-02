tr_sq(X,Y,S):- S is (1/2 * X *Y).
trapez_sq(X,Y,H,S):- S is (1/2 * H * (X+Y)).
compare(S1,S2):- S1 < S2 -> print("S треугольника меньше"); print("S трапеции меньше").
result(S1, S2):- tr_sq(7,5,S1), trapez_sq(3,6,4,S2), compare(S1,S2).

