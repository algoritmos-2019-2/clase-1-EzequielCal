print("11.- Primeros n impares")
def SerieImpares(i, n):

    if(n > 0):
        print (i*2-1)
        SerieImpares(i+1, n-1)

n = int(input("Cantidad de terminos: "))
SerieImpares(1,n)
