# Programar las siguientes instrucciones de forma ordenada. Inicialmente, el diccionario
# es:
# a) Añadir al diccionario las claves:"perro","tigre" y "mono", con sus respectivos
# valores:"Bobby","Peepe” y "Homero"
# b) Modificar las claves:"elefante" y "delfín" con los valores:"Trompis" y "Manolo"
# respectivamente.
from pprint import pprint

animales = {"elefante": ""}

animales["elefante"] = "Trompis"
animales["perro"] = "Booby"
animales["tigre"] = "Peepe"
animales["mono"] = "Homero"
animales["delfín"] = "Manolo"

pprint(animales)
