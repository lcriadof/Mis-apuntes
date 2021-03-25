nociones básicas de Bash Scripting
------------------------------------


-- Cambio de directorio:<br>
cd [nombre directorio]
<br><br>
-- Directorio actual:<br>
pwd
<br><br>
-- Listado de un directorio:<br>
ls
<br><br>
este comando admite varias opciones<br>
ls -R lista recursivamente los subdirectorios encontrados.<br>
ls -a muestra todos los archivos, incluyendo algunos que están ocultos para el usuario —aquellos que comienzan por un punto—. El archivo punto . indica el directorio actual y el doble punto .. el directorio padre, que contiene al actual.<br>
ls -c muestra ordenando por día y hora de creación.<br>
ls -t muestra ordenando por día y hora de modificación.<br>
ls -r muestra el directorio y lo ordena en orden inverso.<br>
ls subdir muestra el contenido del subdirectorio subdir.<br>
ls -l filename muestra toda la información (fecha, permisos) sobre el archivo.<br>
ls -color muestra el contenido del directorio coloreado: verde para los ejecutables, azul para las carpetas, fucsia para las imágenes, rojo para los comprimidos, etc.<br>
ls -l muestra toda la información de cada archivo, incluyendo protecciones, tamaño y fecha de creación o del último cambio introducido, etc.<br>
ls -cr el directorio ordenando inversamente por fechas<br>
<br><br>
-- creacion fichero<br>
touch [nombre fichero]
<br><br>
-- creacion subdirectorio<br>
mkdir [nombre subdir]
<br><br>
-- borrar subdirectorio<br>
 rmdir [nombre subdir]
 <br><br>
-- copia un fichero en otro<br>
cp [path y nombre fichero origen] [path y nombre fichero destino]
<br><br>
  También se puede usar como cp file1 file2 namedir que hace copias de file1 y file2 en el directorio
<br><br>
