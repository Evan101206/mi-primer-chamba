print("bienvenido a mi programa de estudio")
opcion=1
while opcion!=0:
    print("ingresa 1. area triangulo")
    print("ingresa 2. area rectangulo")
    print("ingresa 3. area circulo")
    print("ingresa 4. convertir la temperatura °F a °C")
    print("ingrea 5. convertir temperatura °C a °F")
    op=int(input("¿que actividad quieres ingresar?"))
    if (op==1):
        base=int(input("ingresa la base "))
        res=base*altura/2
        print("el area del triangulo es ", res)
    elif (op==2):
        altura=int(input("ingresa la altura "))
        res=base*altura
        print("el area del rectangulo es ", res)
    elif (op==3):
        radio=int(input("ingresa el radio "))
        res=3.14159265*radio/2
        print("el area del circulo es ", res)
    elif (op==4):
        temperatura=int(input("ingrea la temperatura"))
        res=temperatura*9/5+32
        print("la temperatura es ", res)
    elif (op==5):
        temperatura=int(input("ingrea la temperatura"))
        res=temperatura-32*5/9
        print("la temperatura es ", res)
    else:
        print("no valido")
    opcion=int(input("desea continuar, sino presiona 0. para salir"))