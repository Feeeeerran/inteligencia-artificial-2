% BASE DE CONOCIMIENTO PARA UN VIAJE INOLVIDABLE 😎





viajar(Coche, Conductor, Ruta) :-
    verificarAcompaniantes(_),
    verificarConductor(Conductor),
    verificarCoche(Coche),
    verificarRuta(Ruta)
. 

% ACOMPAÑANTES ~~~~~~~~~~~~~~~~~~~~~~~~
verificarAcompaniantes(_) :-
    \+sonMuchos(_), !
    % Podria fijarme si todos llevan cinturon o no
. 

verificarAcompaniantes(_) :- 
    sonMuchos(_),
    writeln("Son demasiados para irse de viaje"), false
. 

sonMuchos(_) :- 
    grupo(Integrantes), 
    length(Integrantes,N), N > 4,!
. 




% CONDUCTOR ~~~~~~~~~~~~~~~~~~~~~~~~~~
verificarConductor(Conductor) :- 
    conductor(Conductor,Edad), Edad > 18, 
    verificarCinturon(Conductor), tieneCarnet(Conductor), !
. 

verificarConductor(Conductor) :- 
    conductor(Conductor,Edad), Edad < 18, 
    writeln("El conductor es un menor >:("), false
. 

verificarConductor(Conductor) :- 
    \+tieneCarnet(Conductor),
    writeln("Faltan papeles para el conductor"), false
. 

verificarCinturon(Conductor) :- 
    cinturonSeguridad(Conductor,Estado), Estado == "Puesto"
. 

verificarCinturon(Conductor) :- 
    cinturonSeguridad(Conductor,Estado), not(Estado == "Puesto"),
    writeln("A ponerse el cinturon de seguridad señor conductor")
. 




% COCHE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
verificarCoche(Coche) :- 
    seguro(Coche), gasolina(Coche,Gasolina), Gasolina > 20,
    estado(Coche,Estado), Estado == "Encendido",!
. 

verificarCoche(Coche) :- 
    \+seguro(Coche),
    writeln("Habria que revisar el seguro pillin")
. 

verificarCoche(Coche) :-
    gasolina(Coche,Gasolina), Gasolina < 20,
    writeln("Coche sin gasolina"), false
. 

verificarCoche(Coche) :- 
    estado(Coche,Estado), not(Estado = "Encendido"),
    writeln("El coche esta apagado"), false
. 

% RUTA
verificarRuta(Ruta) :- 
    ruta(Ruta,Pozos), Pozos < 50
. 



% Estado de los coches
coche(ferrari).
coche(tesla).
coche(fiat600).

gasolina(ferrari,25).
gasolina(tesla,19).
gasolina(fiat600,30).

seguro(ferrari).
seguro(fiat600).

estado(ferrari,"Apagado").
estado(tesla,"Encendido").
estado(fiat600,"Encendido").


% Estado de conductores << conductor("Nombre","Edad") >>
conductor(toreto,50).
conductor(manin,25).
conductor(amigo,12).

tieneCarnet(toreto).
tieneCarnet(manin).
tieneCarnet(amigo).

% Se verifican cinturones de seguridad
cinturonSeguridad(pedrito,"Puesto").
cinturonSeguridad(manin,"Puesto").
cinturonSeguridad(amigo,"No puesto").


% Se definen acompañantes
grupo([elCabesa,muyayo,otaku]).



% Se define el estado del trayecto << ruta("Nombre","Cant. de pozos") >>
ruta(ruta_40,123).
ruta(ruta_65,23).
ruta(ruta_60,65).

