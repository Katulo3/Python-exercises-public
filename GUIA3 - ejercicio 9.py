num1: int = int(input("Ingrese un número entero:"))
num2: int = int(input("Ingrese el segundo número entero:"))

print(
    """Seleccione el número de operación a realizar.
1-Mostrar una suma de los dos números
2-Mostrar una resta de los dos números (el primero menos el segundo)
3-Mostrar una multiplicación de los dos números.
 """
)
eleccion = int(input())

while eleccion >= 4:
    print("Error")
    break
else:
    if eleccion == 1:
        print(f"Su resultado es {num1 + num2}")
    if eleccion == 2:
        print(f"Su resultado es {num1 - num2}")
    elif eleccion == 3:
        print(f"Su resultado es {num1 * num2}")
