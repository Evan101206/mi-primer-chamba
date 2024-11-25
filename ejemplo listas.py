print("hello")

deportes=["futbol", "basquetbol", "voleibol", "natacion"]
print(deportes[2])

#la posicion de natacion
pos=deportes.index("natacion")
print("la posicion de natacion es:",pos)
pos=deportes.index("futbol")
print("la posicion de futbol es:",pos)

#agregar otro deporte al final
deportes.append("hanball")
print(deportes)
deportes.insert(1,"hanball")
print(deportes)

cantidad_saludos=int(input("cuantos saludos quieres?"))
for i in range(cantidad_saludos):
    print("holaaa")

num_deportes=int(input("cuantos deportes vas a agregar? "))
for i in (range(num_deportes)):
    dep=input("ingresa deporte ")
    deportes.append(dep)
print(deportes)