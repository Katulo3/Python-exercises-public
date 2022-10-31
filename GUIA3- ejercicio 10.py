# Usuario tiene que tener entre 5 y 10
# caracteres y no puede empezar con un número.
# contraseña tiene que tener mínimo 6 caracteres.
username = str(input("Ingrese nombre de usuario, 10 carácteres máximo:"))
print("Su contraseña debe tener más de 6 caracteres.")
contraseña = str(
    input(
        """Ingrese su contraseña, sólo letras,no símbolos, 
ni números:"""
    )
)
contraseña_repetida = input("Escriba de nuevo la contraseña: ")

validar_formulario = True

validacion_1 = username[0].isdigit()
validacion_2 = len(username) > 5
validacion_3 = len(username) < 10
validacion_4 = len(contraseña) > 6
validacion_5 = contraseña_repetida == contraseña

if not validacion_1:
    print("El nombre no debe empezar con números.")
    validar_formulario = False

if not validacion_2:
    print("El nombre debe tener más de 6 caractéres.")
    validar_formulario = False

if not validacion_3:
    print("El nombre debe tener menos de 10 caractéres")
    validar_formulario = False

if not validacion_4:
    print("La contraseña debe tener más de 8 caractéres")
    validar_formulario = False

if not validacion_5:
    print("La contraseña escrita no es igual a la original.")
    validar_formulario = False


if validar_formulario:
    print("Enviando Formulario")
else:
    print("Formulario inválido, verifique que los datos sean correcetos.")
