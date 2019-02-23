print("12.- Terminos de Fibonacci")
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)
#Se establece como 1000 el valor maximo de los numeros de la sucesion mostrados
