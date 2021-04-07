# json

JSON (JavaScript Object Notation) es un formato de datos que posee las siguientes características:<br>
1.- basado en JavaScript.<br>
2.- independiente del lenguaje de programación <br>
3.- objetos mediante parejas clave=valor<br>
&#8195; Las claves son cadenas de texto entre comillas<br>
&#8195; Los valores pueden ser:<br>
&#8195;&#8195; Tipos básicos: cadena, número, booleano, null.<br>
&#8195;&#8195; Arrays de valores: entre corchetes [ y ].<br>
&#8195;&#8195; Otros objetos JSON: entre llaves { y }.<br>
<br><br>
<u>ejemplo</u>: <br>
Nombre=“Luis”, DNI=“XXXXXXXXX”, Edad=“45”<br>
Asignaturas matriculadas:<br>
&#8195; Obligatorias: Álgebra, Matemáticas II, Geometría.<br>
&#8195; Optativas: Seminario I, Seminario II, Métodos numéricos.<br>
&#8195; Libre Elección: Informática, Música.<br>
<br>

{<br>
"Nombre":"Luis",<br>
"DNI":"XXXXXXXXX",<br>
"Edad":45, "Asignaturas matriculadas":<br>
{<br>
   "Obligatorias": ["Algebra", "Matematicas II", "Geometria"],<br>
   "Optativas":["Seminario I", "Seminario II"],<br>
   "Libre Eleccion": ["Informatica", "Musica"]<br>
}<br>
}<br>

JSON no puede almacenar cualquier tipo de valor Python, únicamente cadenas, enteros, reales, booleanos, listas, diccionarios y el tipo None.<br>
<br><br>
<u>ejemplo lectura</u>:

JsonDatos='{"nombre":"Sofia","matriculado":true,"asignaturas":34,"ID":null}'<br>
import json<br>
PythonDatos=json.loads(JsonDatos) # lectura  <br> 
print (PythonDatos)<br>

<u>ejemplo escritura</u>:


JsonDatos='{"nombre":"Sofia","matriculado":true,"asignaturas":34,"ID":null}'<br>
import json<br>
PythonDatos=json.dumps(JsonDatos) # escritura <br>
print (PythonDatos)<br>