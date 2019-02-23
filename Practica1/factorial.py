print("13.- Factorial de un numero")
def Factorial():
    Numero= int(input("Ingrese un numero"))
    Factorial = 1
    for i in range(Numero):
        Factorial *= Numero
        Numero -= 1
    print("El factorial de ese numero es ",Factorial)
Factorial()
