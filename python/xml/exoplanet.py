# https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue
import xml.etree.ElementTree as ET, urllib.request, gzip, io



url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))


# mass= La referencia es Jupiter, es decir, 1.0 es identico a la masa de jupiter
#     La masa de Jupiter es 318 veces la de la Tierra, luego a esta escala necesitamos
#     planetas que esten cercanos al valorr 0.0031457007
# Listado de planetas confirmados de tamaño similar a La Tierra (entre la lista aparece La Tierra)
n=0
for planet in oec.findall(".//planet"):
    if ( planet.findtext("mass") ): # el condicional se cumple si la cadena mass tiene valor, en caso contrario pondrimaos -> "not planet.findtext("mass")"
         if ( float(planet.findtext("mass"))>0.0029 and float(planet.findtext("mass"))<0.0032):
            n=n+1
            print ("planeta ",n," ",planet.findtext("name"))
            print ("     masa: ",planet.findtext("mass"), ",  radio: ",planet.findtext("radius"))
            print ("     año de descubrimiento: ", planet.findtext("discoveryyear"), " (", planet.findtext("list"),")")

