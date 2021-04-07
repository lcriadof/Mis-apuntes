# xml

XML (Extensible Markup Language) es un metalenguaje que permite definir tags de marcado<br>
&#8195;&#8195; tag:  etiquetas que se encierran entre corchetes angulares, <>, y se usan en pares

<u>Consta de dos declaraciones:</u><br>
1.- versión de XML utilizada y el tipo de codificación de caracteres.<br>
2.- tipo de documento que asocia el documento a una DTD o XSD respecto a la cual el documento es conforme.<br>
<br>
Las etiquetas de los elementos pueden incluir 1 o más atributos que representan propiedades de los elementos de la forma Nombre atributo=“Valor atributo”

<u>SAX (Simple API for XML)</u><br>
permite leer el contenido como una secuencia de datos e interpretar las etiquetas según se van encontrando.

Para procesar usando SAX, es necesario crearse un manejador propio ContentHandler como subclase de xml.sax.ContentHandler. El manejador gestionará las etiquetas y atributos que se deseen del documento XML que va a ser procesado.

a.- Los métodos startDocument y endDocument son llamadas al comienzo y al final del archivo XML.<br>
b.- Los  métodos startElement (etiqu eta, atributos) y endElement (etiqueta) son llamados al comienzo y al final de cada elemento. En caso de utilizar espacios de nombres se utilizarían los métodos startElementNS y endElementNS.<br>
c.- El método character (texto) es llamado cuando es una cadena de texto.<br>
d.- xml.sax.make_parser ([Lista de parsers]): crea un nuevo objeto parser. Tiene como argumento optativo una lista de parsers.<br>
e.- xml.sax.parse (archivo XML, Manejador, [ManejadorErrores]): crea un parser SAX y lo usa para procesar el documento XML. Tiene como argumento el documento XML que va a ser procesado, el manejador de eventos y optativamente un manejador de errores.<br>
f.- xml.sax.parseString (NombreCadenaXML, Manejador, [ManejadorErrores]): crea un parser SAX y lo usa para procesar la cadena XML dada. Tiene como argumento la cadena XML que va a ser procesada, el manejador de eventos y optativamente un manejador de errores.<br>

AL final cuando se trabaja con SAX desde python hay que tener en cuenta lo siguiente:<br>
* importar el paquete SAX: import xml.sax.<br>
* implementar nuestro manejador concreto para el XML que trataremos, esto se hace construyendo una clase heredara de  xml.sax.ContentHandler (principal interfaz de llamada en SAX).<br>
* nuestra clase manejadora debe implementar al menos los métodos:
--init--, startElement, endElement y characters<br>
* desde el programa principal se realiza el procesamiento

[ejemplo de uso de SAX](gestionSax.py)
  
