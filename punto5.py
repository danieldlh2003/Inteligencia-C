# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:50:46 2022

@author: ddelahoz28
"""

#punto 5
persona1 = int(input("ingresa los estudiantes de redes "))
persona2 = int(input("ingrese los estudiantes de contabilidad  "))
persona3 = int(input("ingrese los estudiantes de diseño "))
total = persona1+persona2+persona3
porcentaje1 = persona1 * 100 / total
porcentaje2 = persona2 *100/total 
porcentaje3 =persona3 *100/ total
print(f"el porcentaje de los estudiantes de redes es de:{porcentaje1}%")
print(f"el porcentaje de los estudiantes de contabilidad es de:{porcentaje2}%")
print(f"el porcentaje de los estudiantes de diseño es de:{porcentaje3}%")