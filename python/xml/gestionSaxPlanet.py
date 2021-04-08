# exoplanetas
import xml.sax



class ManejadorPlanet (xml.sax.handler.ContentHandler):


    def __init__(self):
        self.Datos = ""
        self.nombrePlaneta = ""
        self.bandera=0
        self.numNamesPlanet=0
        self.masa=0

    def startElement(self,etiqueta,atributos):
        self.Datos=etiqueta
        if self.Datos=="planet":
            self.numNamesPlanet = 0
            self.bandera = 1
            print("\n-- planeta encontrado: ")
        if self.Datos=="name":
            if self.bandera == 1:
                self.bandera = 2


    def endElement(self,etiqueta):
        if self.Datos == "planet":
            self.bandera = 0
        if self.Datos=="name":
            if self.bandera == 2:
                self.bandera = 1



    def characters(self, contenido):
        if (self.Datos == "name" and self.bandera==2):
            self.nombrePlaneta=contenido
            self.numNamesPlanet=self.numNamesPlanet+1
            print("-------> nombre ",self.numNamesPlanet," ",self.nombrePlaneta)
        if (self.Datos=="mass" and self.bandera==1):
            self.masa=contenido
            print("-------> masa ", self.masa)




if (__name__=="__main__"):
    parser=xml.sax.make_parser() # crear un XMLReader
    parser.setFeature(xml.sax.handler.feature_namespaces,0)  # deshabilitar namespaces
    Handler=ManejadorPlanet() # sobreescribimos ContentHandler
    parser.setContentHandler(Handler)
    parser.parse("Alpha Centauri.xml")


