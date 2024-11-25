equipo=["mary", "juanito", "hal"]
integrantes=int(input("cuantos integrantes mas va a agregar? "))
for i in (range(integrantes)):
    integrantes=input("ingresa nombres ")
    equipo.append(integrantes)
print(equipo)