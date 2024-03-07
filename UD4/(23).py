class ExcepcionSaldo:
    def __init__(self):
        print(f"Operación no realizada\nMotivo: Saldo insuficiente\nDispone de un saldo de {self.saldo}€.")


class CuentaBancaria:
    def __init__(self, usuario, cuenta, saldo):
        self.usuario = usuario
        self.cuenta = cuenta
        self.saldo = saldo        

    def get_saldo(self):
        return self.saldo
    
    def depositar(self, cantidad):
        cantidad = float(cantidad)
        self.saldo += cantidad
        print(f"Ha depositado con exito un total de:{cantidad}€.\nDispone de un saldo de {self.get_saldo()}€.")

    def retirar(self, cantidad):
        print("Procesando retirada...")
        cantidad = float(cantidad)
        if cantidad < self.saldo:
            self.saldo -= cantidad
            print(f"Ha retirado con exito un total de: {cantidad}€.")
            print(f"Saldo: {self.get_saldo()}€.")
        else:
            ExcepcionSaldo()

    def transferir(self, cuenta_destino, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            cuenta_destino.depositar(cantidad)
            print(f"Transferecia de {cantidad} a la cuenta {cuenta_destino.cuenta} realizada.")
        else:
            ExcepcionSaldo()

    def clear(self):
        print("\n"*25)

    def iniciar(self):
        self.clear()
        print(f"\nPrograma iniciado con exito.\nCliente: {self.usuario}.\nCuenta: {self.cuenta}.\nSaldo: {self.get_saldo()}€.")
        comprobacion = True
        while comprobacion:
            print("\t1. Depositar saldo.\n\t2. Retirar saldo.\n\t3. Transferir dinero a otra cuenta o usuario.\n\t4. Salir del programa")
            eleccion = input("Indique que quiere hacer: ")
            match eleccion:
                case "1":
                    cifra = input("Ingrese la cantidad a depositar: ")
                    self.depositar(cifra)
                case "2":
                    cifra = input("Ingrese la cantidad a retirar: ")
                    self.retirar(cifra)
                case "3":
                    pass
                case "4":
                    print("Saliendo del programa...")
                    comprobacion = False



# Usuario 1
U1C1 = CuentaBancaria("Pep", "Corriente", 1000)
U1C1.iniciar()