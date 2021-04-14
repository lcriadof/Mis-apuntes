import xml.etree.ElementTree as ET
cadena = '''<Datos>
                <Libro isbn="978-1980892625">
                    <titulo>SEGUNDOS</titulo>
                    <fecha>Abril 2018</fecha>
                    <autor>Luis Criado Fernández</autor>
                </Libro>
            </Datos>'''
doc = ET.fromstring(cadena)
lista = doc.findall("Libro")
for l in lista:
    print ("isbn: ",l.get("isbn"))
    print ("Título: ",l.find("titulo").text)
    print ("Fecha: ",l.find("fecha").text)
    print ("Autor: ",l.find("autor").text)