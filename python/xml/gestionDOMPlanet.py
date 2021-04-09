from xml.dom.minidom  import parse
import xml.dom.minidom

ArbolDom = xml.dom.minidom.parse("Alpha Centauri.xml")
channel = ArbolDom.getElementsByTagName("star")[0]
item = channel.getElementsByTagName("planet")
for i in item:
    nombrePlaneta = i.getElementsByTagName("name")
    print("---> planeta ")
    for nombre in nombrePlaneta:
        print("nombre:", nombre.firstChild.data)
    print()