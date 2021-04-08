import xml.sax



class ManejadorRSS (xml.sax.handler.ContentHandler):
    def __init__(self):
        self.Datos = ""
        self.title = ""
        self.link = ""
        self.description = ""

    def startElement(self,etiqueta,atributos):
        self.Datos=etiqueta

    def endElement(self,etiqueta):
        if self.Datos=="title":
            print("titulo: ",self.title)
        elif self.Datos=="link":
            print("enlace: ",self.link)
        elif self.Datos=="description":
            print("descripción: ",self.description)
        self.Datos=""
    def characters(self, contenido):
        if self.Datos == "title":
            self.title=contenido
        elif self.Datos == "link":
            self.link=contenido
        elif self.Datos == "description":
            self.description=contenido

if (__name__=="__main__"):
    parser=xml.sax.make_parser() # crear un XMLReader
    parser.setFeature(xml.sax.handler.feature_namespaces,0)  # deshabilitar namespaces
    Handler=ManejadorRSS() # sobreescribimos ContentHandler
    parser.setContentHandler(Handler)
    parser.parse("rss.xml")


