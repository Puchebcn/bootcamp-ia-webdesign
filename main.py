# Importamos las funciones desde funciones.py
from funciones import mostrar_propiedades, calcular_area_rectangulo, calcular_dias_vividos, realizar_operaciones

# Llamamos a las funciones desde aquí
if __name__ == "__main__":
    # Ejercicio 1
    mostrar_propiedades("Javier Puche Rodriguez", 41, "Barcelona", 91.8)

    # Ejercicio 2
    base = 35
    altura = 20
    calcular_area_rectangulo(base, altura)

    # Ejercicio 3
    edad = int(input("¿Cuántos años tienes? "))
    calcular_dias_vividos(edad)

    # Ejercicio 4
    numero1 = int(input("Introduce un número: "))
    numero2 = int(input("Introduce otro número: "))
    realizar_operaciones(numero1, numero2)