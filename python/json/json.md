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
<br>
<u>ejemplo</u>: <br>
Nombre=“Luis”, DNI=“XXXXXXXXX”, Edad=“45”<br>
Asignaturas matriculadas:<br>
&#8195; Obligatorias: Álgebra, Matemáticas II, Geometría.<br>
&#8195; Optativas: Seminario I, Seminario II, Métodos numéricos.<br>
&#8195; Libre Elección: Informática, Música.<br>
<br>

{

"Nombre":"Luis",

"DNI":"XXXXXXXXX",

"Edad":45, "Asignaturas matriculadas":

{

   "Obligatorias": ["Algebra", "Matematicas II", "Geometria"],

   "Optativas":["Seminario I", "Seminario II"],

   "Libre Eleccion": ["Informatica", "Musica"]

}

}