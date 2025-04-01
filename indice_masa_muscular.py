
print("Quieres conocer tu indice de masa muscular ? Ingresa los siguientes valores")
peso_paciente=float(input("Ingresa tu peso total en kilogramos: "))
estatura_paciente=float(input("Ingresa tu estatura en metros: "))
actividad_diaria=input("Ingresa tu actividad diaria (sedentario, moderado, deportista): ")


if actividad_diaria == "sedentario":
    porcentaje_muscular=0.3
elif actividad_diaria=="moderado":
    porcentaje_muscular=0.4
elif actividad_diaria=="deportista":

else:
    print("Sea serio nonorrea")







indice_masa_corporal= peso_paciente/estatura_paciente.math.pow(2)

indice_masa_muscular= indice_masa_corporal* porcentaje_muscular/100
