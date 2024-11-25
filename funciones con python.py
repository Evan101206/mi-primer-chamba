#crear una funcion

#funcion llamada saludar, va a recibir el nombre
def saludar(nombre):
    print("hola ", nombre)

nom=input("ingresa tu nombre ")
saludar(nom)

#funcion llamada sumita, va a recibir 5 numeros
#va a regresar el valor de la suma
def  sumita(n1,n2,n3,n4,n5):
    res_suma=n1+n2+n3+n4+n5
    return res_suma

num1=int(input("ingresa el primer digito"))
num2=int(input("ingresa el segundo digito"))
num3=int(input("ingresa el tercer digito"))
num4=int(input("ingresa el cuarto digito"))
num5=int(input("ingresa el quinto digito"))

#mandar llamar a la fubcion/usarla
print(sumita(num1,num2,num3,num4,num5))

#crear una funcion llamada area_triangulo
#que reciba base y altura
#regrese al resubtario del area
def area_triangulo(b,h):
    area=(b*h)/2
    return area
#usar la funcion
print(area_triangulo(4,5))
#ejercicios
#1- crear una funcion llamada multiplicar 



#usar la funcion
def multiplicar(num4,num5,num6):
    resultado=(num4*num5*num6)
    return resultado
#2- 



#usar funcion
def largo_cadena(texto):
    cantidad=len(texto)
    return cantidad
#3- crear una funcion llamada promedio



def promedio(cal1,cal2):
    res=(cal1+cal2)/2
    return res
#pedir calif, primer y segundo parcial
cal1=float(input("ingresa cali1"))
cal2=float(input("ingresa cal2"))
print("el promedio es: ", promedio(cal1,cal2))

#crear una funcion que resiva el nombre 
#de la persona, su edad y el mes de nacimiento
#devuelta:
#las dos promeras letras del nombre-edad-primer
#letra del mes
#ejemplo: MA17O
def disk_curp(nombre, edad, mes):
    letras=nombre[0:2]
    print(letras)

disk_curp("ale", 17, "diciembre")