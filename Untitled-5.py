print("hola bienvenido a mi calculadora")
#
#calculadora
opcion=1
#en un ciclo while realiza operaciones hata que el usuario escriba 0
while opcion!=0:
    num1=int(input("ingresa el primer numero "))
    num2=int(input("ingresa el segundo numero "))
    print("ingresa 1. sumar")
    print("ingresa 2. restar")
    print("ingresa 3. multiplicar")
    print("ingresa 4. division")
    op=int(input("¿que operacion quieres hacer con esos numeros? "))
    if (op==1):
        res=num1+num2
        print("la suma de los dos numeron son: ", res)
    elif(op==2):
        res=num1-num2
        print("la resta de los dos numeron son: ", res)
    elif(op==3):
        res=num1*num2
        print("la multiplicacion de los dos numeros son: ", res)
    elif(op==4):
        res=num1/num2
        print("la division de los dos numeros es: ", res)
    else:
        print("no valido")
    opcion=int(input("desea continuar, sino presiona 0. para salir"))