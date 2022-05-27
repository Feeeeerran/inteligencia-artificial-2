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
%       > Se mueve a menos de 10 cm/s
%       > Tiene que estar a 3 o mas metros del coche
avanzar(C) :- estado(C,Estado), Estado == "Encendido", obstaculo(_,Distancia,Velocidad), (Distancia >= 3 ; Velocidad =< 10).



% Decimos que algo es un obstaculo si cumple con alguna de las condiciones
%   > Aparece en el sensor a menos de 5 m
%   > Tiene mas de 20 cm de altura
%   > Se mueve a mas de 5 cm/s
obstaculo(Desc,Distancia,Velocidad) :- sensor(Desc,Distancia,Altura,Velocidad), (Distancia =< 10; Altura >= 20; Velocidad >= 5).


% Podemos sensar un obstaculo siempre y cuando el sensor lo capture
%   > El sensor toma (descripcion, distancia, altura, velocidad)

sensor(persona, 2, 190, 10).
sensor(perro, 15, 70, 30).
sensor(piedra,1, 10, 0).


coche(teslo).
coche(teslo2).


estado(teslo,"Apagado").
estado(teslo2,"Encendido").















