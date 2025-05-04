###VARIABLES###

### Una variable es un contenedor que guarda un valor en memoria para poder usarlo más tarde.###

nombre = "Javier"
edad = 41

#Tipos de variables en Python:
### En Python, las variables pueden ser de diferentes tipos. ###    
### Por ejemplo, "Javier" es un texto (String) y 41 es un número (Integer). ###
### En este caso, "nombre" es una variable de tipo String y "edad" es una variable de tipo Integer. ###
### En Python, los tipos de datos son importantes porque determinan cómo se pueden manipular y operar los valores. ###

# Tipos de datos en Python:
# 1. String (Texto): Se representa entre comillas simples o dobles.
# 2. Integer (Número entero): Se representa sin comillas.
# 3. Float (Número decimal): Se representa con un punto decimal.
# 4. Boolean (Verdadero o falso): Se representa con True o False.
# 5. List (Lista): Se representa entre corchetes [] y puede contener diferentes tipos de datos.
# 6. Tuple (Tupla): Se representa entre paréntesis () y es inmutable.
# 7. Dictionary (Diccionario): Se representa entre llaves {} y contiene pares clave-valor.

Numero = 2 #Integer
Decimal = 2.5 #Float
Texto = "Hola" #String
Booleano = True #Boolean
Lista = [1, 2, 3] #List
Tupla = (1, 2, 3) #Tuple
Diccionario = {"clave1": "valor1", "clave2": "valor2"} #Dictionary

# Ejemplo de uso de variables:
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")
print("El número es: " + str(Numero) + ", el decimal es: " + str(Decimal) + ", el texto es: " + Texto + ", el booleano es: " + str(Booleano) + ", la lista es: " + str(Lista) + ", la tupla es: " + str(Tupla) + ", el diccionario es: " + str(Diccionario))


# Ejemplo de uso de variables con formato:
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
print(f"El número es: {Numero}, el decimal es: {Decimal}, el texto es: {Texto}, el booleano es: {Booleano}, la lista es: {Lista}, la tupla es: {Tupla}, el diccionario es: {Diccionario}")


# Ejemplo de uso de variables con formato y concatenación:
print("Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años.")
print("El número es: " + str(Numero) + ", el decimal es: " + str(Decimal) + ", el texto es: " + Texto + ", el booleano es: " + str(Booleano) + ", la lista es: " + str(Lista) + ", la tupla es: " + str(Tupla) + ", el diccionario es: " + str(Diccionario))

#2. Tipos de datos básicos en Python

#Tipo	Ejemplo	Descripción
#int	5, -12, 100	Enteros
#float	3.14, -1.5	Decimales
#str	"Hola"	Texto (cadena de caracteres)
#bool	True, False	Booleano (verdadero o falso)
#list	[1, 2, 3], ["a", "b"]	Lista de elementosd
#dict	{"nombre": "Ana", "edad": 30}	Diccionario con claves y valores
