# obtener informacion de una IP
# uso del API GeoIP7 (servicio de geolocalización que se utiliza para deducir la ubicación geográfica de una IP.
#   Se trata de una base de datos de geolocalización gratuita que se actualiza periódicamente.

import urllib.request
import json

servicioUrl='http://ip-api.com/json/'
while True:
    ip = input('teclee IP: ')
    if ip == "FIN":
        break
    else:
        url=servicioUrl+ip
        print("Conectando con ", url)
        request = urllib.request.Request(url)
        request.add_header('User-Agent', "cheese")
        datos = urllib.request.urlopen(request).read()
        try:
            js=json.loads(datos)
        except: js - None
        if ("status" in js and js['status']=="fail"):
            print(" --- error ---> ",js['message'])
        else:
            print("ciudad: ",js['city'])
