#✅ Ejercicio 1 – Crea variables y muéstralas por pantalla:

def Propiedades():
    # Definición de variables
    nombre = "Javier Puche Rodriguez"
    edad = 41
    ciudad = "Barcelona"
    peso = 91.8
    SoyGuapo = True
    Lista = [1, 2, 3, 4]
    Tupla = (1, 2, 3, 4)
    Diccionario = {"nombre": "Javier", "edad": 41, "ciudad": "Barcelona"}
    
    # Mostrar variables por pantalla
    print(f"Hola mi nombre es {nombre} y tengo {edad} años vivo en {ciudad} y peso {peso}kg")

#Llamada a la función
Propiedades()

#✅ Ejercicio 2 – Calcula el área de un rectángulo

def AreaRectangulo():
    # Definición de variables
    base = 35
    altura = 20

    area = base * altura

    print(f"El area del rectangulo es : {area} m2")

AreaRectangulo()

# Ejercicio 3 – Pregunta al usuario su edad y calcula cuántos días ha vivido

def DiasVividos():
    # Definición de variables
    edad = int(input("¿Cuántos años tienes? "))
    diasvividos = 365
    total = edad * diasvividos

    print(f"Has vivido un total de {total} dias")

DiasVividos()

#Crea una variable con tu nombre y otra con tu edad. Luego imprime:

def datos():
    #Definicion de variables
    nombre = "Javier"
    edad = 41

    print(f"Hola mi nimbre es {nombre} y tengo {edad} años")

datos()

#Pide al usuario dos números por teclado y muestra su suma, resta y multiplicación.

def operaciones():
    #Definicion de variables
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2

    print(f"La suma es = {suma}, la resta es = {resta}, la multiplicacion es = {multiplicacion}")

operaciones()