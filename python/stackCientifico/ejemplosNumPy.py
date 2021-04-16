# El elemento esencial de NumPy son unos objetos denominados ndarray,
# arrays multidimensionales donde todos sus elementos son del mismo tipo y están indexados
# por una tupla de números positivos.

# Su principal ventaja es la eficiencia para manipular vectores y matrices.
# En este sentido, proporciona funciones que operan sobre ndarrays.

import numpy as np
import numpy.random as r

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
print("7.- intercambiar filas de un array")
opcion = int(input('opción ¿?: '))



# creacion
if opcion==1:
    print("---------------  ejemplos de tipos de matrices")
    a = np.array( [2,3,4] )
    print("tipo: ",type(a))
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

    # array a partir de una tupla
    print()
    mi_tupla = (1, 58, 63, 45)
    print(type(mi_tupla))
    arr_tuple = np.array(mi_tupla)
    print(arr_tuple)
    print(type(arr_tuple))

   # array a partir de diccionario
    print()
    my_dict = {'one': 'uno',
           'two': 'dos',
           'three': 'tres'}
    print(my_dict.items())
    print(type(my_dict))
    dict_list = list(my_dict.items()) # pasamos el diccionario a tupla
    print(dict_list)
    print(type(dict_list))
    arr_dict = np.array(dict_list) # finalmente lo pasamos a array
    print(arr_dict)
    print(type(arr_dict))

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
    a = np.array([[100, 5, 6, 52],
                  [80, 65, 4, 61]])
    print(a)
    print("suma: ",np.sum(a))  # Suma todos los elementos
    print("valor mínimo: ",np.min(a), "posición: ", np.argmin(a))  # Valor mínimo y su posición
    print("valor máximo: ",np.max(a), "posición: ", np.argmax(a))  # Valor máximo y su posición
    print("valor medio: ",np.mean(a))  # Media del array, considerando todos su valores
    print("media por columnas: ",np.mean(a, axis=0))  # Media por columnas
    print("varianza por columnas: ",np.var(a, axis=0))  # Varianza por columnas
    print("Desviación estandar por columnas: ",np.std(a, axis=0))  # Desviación estandar (por columnas)
    print("Mediana por filas: ",np.median(a, axis=1))  # Mediana por filas
    print()
    a = np.array([[2, 3, 4, 5], [4, 5, 6, 6]])
    print(a)
    print("correlación de la transpuesta: ",np.corrcoef(a))  # correlación de la transpuesta
    print("covarianza de la primera columna: ",np.cov(a[:, 0]))  # covarianza de la primera columna
    print()
    s = r.rand(10)  # Genera los números aleatorios de una normal (0,1)
    print(s)
    t = r.normal(size=(5, 1))  # Genera un array con números pertenecientes a una normal
    print(t)
    k = r.normal()  # Genera un número perteneciente a una normal
    print(k)

# itercambiar filas de un array
if opcion == 7:
    print()
    A = np.arange(20).reshape(5, 4)
    print(A)
    print(A[[0,1]])
    print(A[[1,0]])
    # intercambiamos
    A[[0, 1]] = A[[1, 0]]
    print()
    print(A)
    print(A[[0, 1]])
    print(A[[1, 0]])

