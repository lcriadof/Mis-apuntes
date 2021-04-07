# acceder a una URL
import urllib.request

url = input('teclee URL: ')
print ("Conectando con ",url)

request=urllib.request.Request(url)
request.add_header('User-Agent',"cheese")
datos=urllib.request.urlopen(request).read()
print (datos)