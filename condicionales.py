#Declaramos la variable
calificacion= input("Introduce tu calificacion de la AZ-900: ")

calificacion = int(calificacion)

#Preguntamos si la calificacion es menor a 700
if calificacion < 700:
    print("Reprobado, por no estudiar")# Si es menor a 700, muestra esto
elif calificacion > 1000:
    print("Mientes. no puedes sacar mas de 1000")
else : # Si no se comple el if anterior pasa a esta linea
    print("Felicidades, pasa por tu certificado") #Se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad
edad= input("introduce tu edad")
edad= int(edad)

if edad >=18 and edad<=100 :
    print("Bienvenido al mamitas")
elif edad>100 :
    print("Si vienes acompañado de tus abuelos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

    