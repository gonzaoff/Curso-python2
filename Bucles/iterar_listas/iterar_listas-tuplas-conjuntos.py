animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,16,14,72]

#iterando 2 listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"reccoriendo lista 1: {animal}")
    print(f"recorriendo lista 2: {numero}")

#recorriendo la lista animales
for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")

#recorriendo la lista numeros y multiplicandolos por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#recorriendo una lista desde el 20 a 30-1
for num in range(20,30):
    print(num)

#forma de recorrer una lista con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#forma practica y elegante. 
#estructura:
#for <indice>,<valor en lista> in enumerate(variable_lista)
#else: (se muestra siempre al terminal el for)
#   print("el bucle termino")
for i,num in enumerate(numeros):
    print(i,num)
else:
    print("el bucle termino.")

def val(valor,valores):  # sourcery skip: for-index-underscore
    #hacer: la suma de todos los elementos y su media aritmetica
    valor=int(input("cuantos valores agregara?: "))
    valores=[int for i in range(valor)]
    resultado = 0
    promedio=0
    for i in range(valor):
    
        valores[i]=int(input("Agregar valores: "))
        resultado=resultado+valores[i]
    
    promedio=resultado/valor
    print(resultado)
    print(promedio)
# val()

def nombress():  # sourcery skip: for-index-underscore
    #input: la lista de nombres y el nombre a buscar en la lista
    #output: si el nombre es true en la lista
    
    n = int(input("ingrese la cantidad: "))
    nombres= [str for i in range(n)]
    for i in range(n):
        nombres[i]=input("ingrese el nombre: ")
    
    buscado = input("Ingrese el nombre a buscar: ")
    encontrado = False
    
    for i in range(n):
        if nombres[i] == buscado:
            encontrado = True
    
    if encontrado:
        print("se encontro.")
    else:
        print("no se encontro")
    
# nombress()

def agregarTextos(): #Agregas cadenas de texto para un rango a definir
    n = int(input("ingrese la cantidad de cadenas de texto: "))
    nombres= [str for i in range(n)]
    for i in range(n):
        nombres[i]=input("ingrese el texto: ")

def evaluaciones2():
    # En un curso de 5 estudiantes se toman 3 parciales. Diseñar un algoritmo
    # para registrar las notas de los alumnos en una matriz.
    # Calcular el promedio de cada alumno y el promedio de cada parcial.
    matriz = [[0.0] * 3 for i in range(5)]

    for alumno in range(5):
        for parcial in range(3):
            nota = float(input(f"Ingrese la nota del alumno {alumno+1} en el parcial {parcial+1}: "))
            matriz[alumno][parcial] = nota

    for alumno in range(5):
        suma_notas = 0.0
        for parcial in range(3):
            suma_notas += matriz[alumno][parcial]
        promedio_alumno = suma_notas / 3
        print(f"El promedio del alumno {alumno+1} es: {promedio_alumno}")

    for parcial in range(3):
        suma_notas = 0.0
        for alumno in range(5):
            suma_notas += matriz[alumno][parcial]
        promedio_parcial = suma_notas / 5
        print(f"El promedio del parcial {parcial+1} es: {promedio_parcial}")


print("hola que hace")