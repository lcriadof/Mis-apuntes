
#Importamos la librería pandas para obtener data frames
import pandas as pd

#Abrir un fichero csv
ejemplo = pd.read_csv("SacramentocrimeJanuary2006.csv", delimiter=",", encoding="iso-8859_2")
#Mostramos los 5 primeros registros
print(ejemplo.head(5))

# si queremos visualizar la totalidad del fichero
print (ejemplo)


# Mostramos las columnas y la dimensión del data frame
print ("Columnas del data frame")
print (ejemplo.columns) # obtenemos los titulos de columnas
print ("\n")
print ("Dimensiones del data frame")
print (ejemplo.shape)  # devuelve algo del estilo: Dimensiones del data frame (211752, 14)

# podemos acceder a los tipos de variables
print ("Tipo de dato por variable: \n")
print (ejemplo.dtypes)