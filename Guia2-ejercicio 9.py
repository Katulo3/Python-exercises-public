asteriscos = "****"
edad = int(input("Bienvenido al foro de adolescentes, ingrese su edad:"))

nombre = str(input("Ingrese su nombre:"))

condicion_1 = len(nombre) >= 3
condicion_2 = len(nombre) <= 10
condicion_3 = nombre != asteriscos
condicion_4 = edad > 10
condicion_5 = edad < 18

validacion = condicion_1 and condicion_2 and condicion_3 and condicion_4 and condicion_5

if validacion:
    print(validacion)
else:
    print("Error, por favor verifique sus datos.")
