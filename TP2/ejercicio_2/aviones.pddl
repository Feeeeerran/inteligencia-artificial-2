(define (domain aviones)
(:requirements :strips)
(:predicates
	(en ?a ?b) 
	(avion ?a)
	(carga ?c)
	(aeropuerto ?a)
	(combustible-bajo ?a)
	(combustible-alto ?a)

) 
(:action cargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?ap) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?a) 
		(not (en ?c ?ap))
	)
)
(:action descargar
 :parameters ( ?c ?a ?ap)
 :precondition
	(and (en ?c ?a) (en ?a ?ap) (carga ?c) (avion ?a) (aeropuerto ?ap))
 :effect
	(and 
		(en ?c ?ap) 
		(not (en ?c ?a))
	)
)
(:action volar
 :parameters ( ?a ?origen ?destino)
 :precondition
	(and (en ?a ?origen) (avion ?a) (aeropuerto ?origen) (aeropuerto ?destino))
 :effect
	(and 
		(en ?a ?destino) 
		(not (en ?a ?origen))
	)
)			
(:action refuel
 :parameters (?a)
 :precondition
	(and (combustible-bajo ?a) (avion ?a))
 :effect
	(and 
		(combustible-alto ?a) 
		(not (combustible-bajo ?a))
	)
)			
)
