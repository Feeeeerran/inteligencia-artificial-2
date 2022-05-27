/*
    Desarrolle una base de conocimientos (KB, Knowledge Base) en PROLOG para alguna de las
    alternativas que se presentan más abajo. Además de la base de conocimientos, plantee
    preguntas que el sistema puede contestar, incluyendo preguntas cerradas (verdadero/falso) y
    preguntas abiertas (ej: qué debe hacerse?). Además de las reglas axiomáticas, incuya algunos
    ground facts (hechos) necesarios para codificar una instancia del problema

*/


% La base del conocimiento sera sobre un coche autonomo

% EL TESLO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

% Para que funcione el coche, tiene que estar encencido,
%   > Si esta encendido no puede encenderse ni tampoco puede estar apagado
encenderse(Coche) :- estado(Coche,Estado), Estado == "Apagado".
apagarse(Coche) :- estado(Coche,Estado), Estado == "Encendido".

% Para poder avanzar
%   > El coche tiene que estar encendido
%   > Si hay un obstaculo
%       > No puede moverse a mas de 10 cm/s
%       > Tiene que estar a 2 o mas metros del coche
avanzar(C) :- estado(C,Estado), Estado == "Encendido".
avanzar(c) :- obstaculo(_,Distancia,Velocidad), Distancia =< 10 , Velocidad =< 2.



% Decimos que algo es un obstaculo si 
%   > Aparece en el sensor a menos de 5 m
%   > Tiene mas de 20 cm de altura
%   > Se mueve a mas de 5cm/s
obstaculo(Desc,Distancia,Velocidad) :- sensor(Desc,Distancia,Altura,Velocidad), Altura >= 20, Distancia =< 5, Velocidad >= 5.
obstaculo(Desc,Distancia,Velocidad) :- sensor(Desc,Distancia,_,Velocidad).


% Podemos sensar un obstaculo siempre y cuando el sensor lo capture
%   > El sensor toma (descripcion, distancia, altura, velocidad)

% sensor(persona, 10, 190, 10).
sensor(perro, 25, 70, 30).
sensor(piedra,1, 10, 0).


coche(teslo).
coche(teslo2).


estado(teslo,"Apagado").
estado(teslo2,"Encendido").















