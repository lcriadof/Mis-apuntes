# El elemento esencial de NumPy son unos objetos denominados ndarray,
# arrays multidimensionales donde todos sus elementos son del mismo tipo y están indexados
# por una tupla de números positivos.

# Su principal ventaja es la eficiencia para manipular vectores y matrices.
# En este sentido, proporciona funciones que operan sobre ndarrays.

import numpy as np

def caracteristicas(matriz):
    print()
    print(matriz)
    print("CARACTERISTICAS DEL ARRAY ")
    print("número de dimension: ", matriz.ndim)
    print("tipo de elemento: ", matriz.dtype)
    print("tamaño de cada dimension: ", matriz.shape)
    print("número total de elementos", matriz.size)
    print()
# fin de funcion caracteristicas

print("1.- ejemplos de tipos de matrices")
print("2.- operaciones")
print("3.- Acceso en arrays unidimensionales")
print("4.- iterar sobre los elementos de un array")
print("5.- redimensionar array")
print("6.- estadisticas")
opcion = int(input('opción ¿?: '))



# creacion
if opcion==1:
    print("---------------  ejemplos de tipos de matrices")
    a = np.array( [2,3,4] )
    caracteristicas(a)

    b = np.array( [[2,3,4], [5,6,7]] )
    caracteristicas(b)

    c = np.array( [[2,3], [5,6]], dtype=complex )
    caracteristicas(c)


    a = np.zeros(4)
    print("matriz cero ",a)
    b = np.ones ([1 ,2])
    print("matriz identidad ",b)
    c = np.empty((4,4)) # empty: crea un array con valores sin inicializar cuyo contenido es aleatorio.
    print("matriz aleatoria ",c)


# operaciones con matrices
if opcion==2:
    print()
    print("---------------  operaciones")
    a = np.array([34,12,3,4])
    b = np.array([2,3,5,6])
    c=a-b
    d=a*10
    print(c)
    print(d)

    b = np.array( [[2,3,4], [5,6,7]] )
    print(b)
    print("suma axis=0: ",b.sum(axis=0))
    print("suma axis=1: ",b.sum(axis=1))

    c = np.array( [[2,3,4], [1,3,8], [5,6,7]] )
    print(c)
    print("suma axis=0: ",c.sum(axis=0))
    print("suma axis=1: ",c.sum(axis=1))

    a = np.array([2,3,5,6])
    print(a)
    a+=3
    print(a)
    a *= a
    print(a)

    # copiar un array por referencia
    copia1=c.view()
    print(copia1)
    c[0][1]=88
    print(copia1)
    print()

    # copiar un array
    copia2 = c.copy()
    print(copia2)
    c[0][1] = 77
    print(copia2)
    copia2[0][1] = 77
    print(copia2)





# Acceso en arrays unidimensionales
if opcion==3:
    print()
    print("---------------  Acceso en arrays unidimensionales")
    arr = np.arange(2,20)
    print(arr)
    print(arr[0]) # a un elemento en particular
# Cuando se elige un subrango se indica por cada dimensión a:b:c, donde
#   a: indica dónde se comienza,
#   b: dónde se termina
#   c: el salto entre elementos.
    print(arr[1:13:3])
# si b no se indica se entiende que es hasta el final
    print(arr[1::3])



# iterar sobre los elementos de un array:
if opcion == 4:
    print()
    print("---------------  iterar sobre los elementos de un array")

    a = np.arange(10)
    print(a)
    print()
    for i in a:
        print (i)


# redimensionar array:
if opcion == 5:
    z = np.arange(12)
    print(z)
    print()
    z=z.reshape(4, 3)
    print(z)
    print()
    z=z.ravel()
    print(z)
    print()
    z.shape = (4, 3)
    print(z)

# estadisticas
if opcion == 6:
    print("por aqui")