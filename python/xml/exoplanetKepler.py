# https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue
import xml.etree.ElementTree as ET, urllib.request, gzip, io

# no funciona xq no existe un xml que empaquete todo kepler
# mo lo apunto para hacerlo
# teoricamente ese seria el código de consulta
url2 = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems_kepler.xml.gz"
oec2 = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url2).read())))
n=0
for planet in oec2.findall(".//planet"):
    if ( planet.findtext("mass") ): # el condicional se cumple si la cadena mass tiene valor, en caso contrario pondrimaos -> "not planet.findtext("mass")"
         if ( float(planet.findtext("mass"))>0.0029 and float(planet.findtext("mass"))<0.0032):
            n=n+1
            print ("planeta ",n," ",planet.findtext("name"))
            print ("     masa: ",planet.findtext("mass"), ",  radio: ",planet.findtext("radius"))
            print ("     año de descubrimiento: ", planet.findtext("discoveryyear"), " (", planet.findtext("list"),")")
