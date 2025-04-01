

import math
import sys


print("Quieres conocer tu indice de masa muscular estimado? Ingresa los siguientes valores")
peso_paciente=float(input("Ingresa tu peso total en kilogramos: "))
estatura_paciente=float(input("Ingresa tu estatura en metros: "))
actividad_diaria=input("Ingresa tu actividad diaria (sedentario, moderado, deportista): ")
porcentaje_muscular=float

if actividad_diaria == "sedentario":
    porcentaje_muscular=0.3
elif actividad_diaria=="moderado":
    porcentaje_muscular=0.4
elif actividad_diaria=="deportista":
    porcentaje_muscular=0.5
else:
    print("Actividad no valida, adiós")
    sys.exit()
    
indice_masa_corporal= float(peso_paciente/math.pow(estatura_paciente,2))

indice_masa_muscular= float((indice_masa_corporal*porcentaje_muscular)/100)

print(f"El indice de masa corporal es '{indice_masa_corporal}' y tu indice de masa muscular es '{indice_masa_muscular}'")
