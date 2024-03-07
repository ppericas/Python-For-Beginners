nums = ["pep", "contrasenya"]
usuario = input("Ingrese su usuario:")
if nums[0] == usuario:
    contraseña = input("Ingrese su contraseña:")
    if nums[1] == contraseña:
        print("Login correcto.")
    else:
        print("Login incorrecto.")
else:
    print("Login incorrecto.")