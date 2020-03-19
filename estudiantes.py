#examen escrito = 40%
#Talleres = 20%
#Examenes = 20%
#Participacion 10%
#Parcial = 10%
hombre = 0
mujer = 0
while True:
    input(u"Finalizacion del Semestre")
    alumnos = input("Ingrese numero de alumnos: ")
    programa = input("A cual programa pertenece: ")
    sexo = input("Tipo de sexo: ")
    examen_escrito = float(input('Ingrese la nota de su examen: '))
    talleres = float(input('Ingrese la nota de sus talleres: '))
    examenes = float(input('Ingrese la nota de final de sus examenes: '))
    participacion = float(input('Ingrese la nota puesta por el docente de acuerdo a su participacion: '))
    parcial = float(input(u'Ingrese la nota de su ultimo parcial: '))

    nota = examen_escrito*0.4 + talleres*0.2 + examenes*0.2 + participacion*0.1 + parcial*0.1
    alumnos = hombre>=1 + mujer>=1
    
    print('La nota definitiva del estudiante es: ',nota)



    cerrar_programa = input("Desea continuar 'Si' , 'No' ")
    if cerrar_programa != 'si':
        break
