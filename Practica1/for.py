print("Ejercicio bucle for")
a=0
print("¿Que numero desea utilizar?")
N=int(input())
for n in range(N):
    print(n+1)
    a=a+n+1
print("La suma de 1 hasta "+str(N)+" es: "+ str(a))
