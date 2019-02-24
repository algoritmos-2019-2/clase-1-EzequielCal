print("Respuestas del cuestionario:")
print("  1.- Los dos tipos de valores booleanos son verdadero y falso, los cuales se escriben True y False respectivamente.  ")
print(" 2.- Los 3 operadores booleanos son AND, OR y NOT. ")
print(" 4.- Los 6 operadores son: estrictamente mayor (<) , estrictamente menor (>) , igual que (==) , mayor o igual que (<=) , menor o igual que (>=) y diferente de (  . ")
print(" 5.-El operador igual(==) sirve para comparar 2 valores, mientras que el operador de asignación (=) sirve para declarar variables y/o condiciones de un programa. ")
print(" 6.- Una condición es un elemento que nos sirve para declarar estados donde un programa se ejecuta de una forma u de otra; puede ser usada en un programa de acceso pidiendo una contraseña. ")
print(" 7.- Para salir del bucle hay presionar Ctrl+c. ")
print(" 8.- Cuando un programa se rompe,este se detiene o vuelve a su estado inicial; mientras que cuando un programa continua, este termina de correr la secuencia para la cual fue diseñado. ")
print(" 9.- Para términos de funcionamiento, no hay diferenica alguna. Pero en terminos de significado de programa si; especificamente, en el rango (10) se declara una secuencia que implicitamente inicia en cero y despliega cada número desde cero hasta n-1, o sea 9; para el rango (0,10) establecemos como valor de inicio a cero, esto de forma voluntaria y que lo hace diferente al rango (10) , corriendo igualmente hasta 9; finalmente el rango (0,10, 1) se diferencia de los otros dos ya que establecemos voluntariamente que la secuencia irà creciendo a razón de 1, lo cual se hace automaticamente en los otros 2 rangos")

print("3.- Tablas de verdad de booleanos")
A=[True, False]
B=[True, False]
print("")
print("NOT")
print("A notA")
for n in A:
    print(str(n)+" "+str(not(n)))

print("")
print("")

print("AND")
print("A   B    A and B")
for n in A:
    for m in B:
        print(str(n)+" "+(str(m))+" "+str(m and n))
print("")
print("")

print("OR")
print("A    B    A or B")
for n in A:
    for m in B:
        print(str(n)+" "+(str(m))+" "+str(n or m))
print("")
