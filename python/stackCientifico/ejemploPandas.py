# Pandas es una librería construida sobre NumPy que ofrece estructuras de datos de alto nivel que facilitan el análisis de datos desde Python.

# estructuras estudiadas
#    a.- Series
#    b.- DataFrame
import numpy as np
import pandas as pd
from pandas import *


print("Series")
print("1.- ndarray")
print("2.- diccionario")
print("3.- valor escalar")
print("Dataframes")
# Un dataframe es una estructura que contiene una colección ordenada de columnas, cada una de las cuales puede
# tener valores de diferentes tipos. Está formado por datos, opcionalmente un índice (etiquetas de las filas) y un
# conjunto de columnas (etiquetas de las columnas). En caso de no existir un índice, se genera a partir de los datos.
print("4.- Diccionario de ndarrays")
print("5.- Lista de diccionarios")
print("6.- Diccionario de tuplas")
print("7.- Diccionario de series")
print("8.- Array estructurado")
opcion = int(input('opción ¿?: '))

# 1.- ndarray
if opcion==1:
    s=Series([1,2,3,4,5], index=['a','b','c','d','e'])
    print(s)
    s = Series([1, 2, 3, 4, 5])
    print(s)

# 2.- diccionario
if opcion==2:
    d = {'a': 0., 'b': 1., 'c': 2.}
    s = Series(d, index=['b', 'c', 'd', 'a'])
    print(s)
    d = {'a': 0., 'b': 1., 'c': 2.}
    s = Series(d)
    print(s)

# 3.- valor escalar
if opcion==3:
    s = Series(5., index=['a', 'b', 'c', 'd', 'e'])
    print(s)

# 4.- Diccionario de ndarrays
if opcion==4:
    d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.]}
    print( DataFrame(d) )

# 5.- Lista de diccionarios
if opcion==5:
    data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
    print( DataFrame(data2) )

# 6.- Diccionario de tuplas
if opcion==6:
    print (DataFrame({
        ('a', 'b'): {('A', 'B'): 1, ('A', 'B'): 2},
        ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
        ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
        ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
        ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}
    }))

# 7.- Diccionario de series
if opcion==7:
    d = {'one': Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])
         }
    df = DataFrame(d)
    print(df)

# 8.- Array estructurado
if opcion==8:
    data = np.zeros((2,), dtype=[
        ('A', 'i4'), ('B', 'f4'), ('C', 'a10'),
    ])
    data[:] = [(1, 2., 'Hello'), (2, 3., "World")]
    print ( DataFrame(data) )