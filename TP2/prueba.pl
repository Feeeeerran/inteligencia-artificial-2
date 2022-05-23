

alarma(X) :- explota(X).
explota(X) :- presion(X,Valor), Valor > 100.


presion(t1, X) :- X is 200.
tuberia(pipe1).


