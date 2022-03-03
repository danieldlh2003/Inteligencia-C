# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:23:36 2022

@author: ddelahoz28
"""

#punto 4
notaTaller1 = int(input("ingrese la nota 1"))
notaTaller2 = int(input("ingrese la nota 2"))
notaTaller3 = int(input("ingrese la nota 3"))
notaexamen = int(input("ingrese la nota del examen"))
notaproyecto = int(input("ingrese la nota del proyecto"))
calificacionTaller=  (notaTaller1 + notaTaller2+ notaTaller3)/3
notaTalleres = calificacionTaller *0.5
calificacionexamen= notaexamen*0.3
calificacionproyecto = notaproyecto *0.2
notaFinal = notaTalleres + calificacionexamen + calificacionproyecto
print(f"la nota final es: {notaFinal}")