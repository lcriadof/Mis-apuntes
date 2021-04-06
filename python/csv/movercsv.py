# Problema:
#   Encontrar todos los archivos CSV del directorio actual.
#   Leer el contenido de cada archivo.
#   Escribir nuevamente el contenido saltándose la primera línea sobre un nuevo archivo CSV.
import os,csv



# solución 1:  manteniendo ambos ficheros entrada-salida abiertas en el proceso de copia

#Se crea un directorio para almacenar los archivos sin cabecera
os.makedirs('SinCabeceras', exist_ok=True)
# Bucle para recuperar los archivos del directorio actual
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # Saltar los archivos que no son csv
    else:
        print('\n Eliminando cabeceras de ' + csvFilename
              + '\n    y utilizo de elemento delimitador el tabulador...')
        archivoEntrada = open (csvFilename)                       # csv de entrada
        archivoSalida = open ('SinCabeceras/'+csvFilename, 'w')   # csv de salida
        entradaLector = csv.reader(archivoEntrada)
        salidaEscritor = csv.writer(archivoSalida,delimiter='\t',lineterminator='\n')
        for linea in entradaLector:
            if entradaLector.line_num>1:
                # print ('Línea #',str(entradaLector.line_num)+" "+str(linea))
                salidaEscritor.writerow(linea)
        print ('    líneas volcadas: ',str(entradaLector.line_num-1))
        archivoEntrada.close()
        archivoSalida.close()

