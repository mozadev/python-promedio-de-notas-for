contador=0
st=0
s_promedios=0

while(contador<3):
    s = 0
    cantidad=int(input(f"ingrese la cantidad de notas del alumno {contador+1}: "))
    i=0
    for i in range (cantidad):
        n=int(input(f"ingrese la nota numero {i+1}: "))
        s=s+n
    p=s/cantidad
    print(f"el promedio de las notas de este alumno es de : {p:.2f}")
    s_promedios = s_promedios+p

    contador=contador+1

ptotal=s_promedios/3
print(f"el promedio de todos los alumnos es: {ptotal}")
