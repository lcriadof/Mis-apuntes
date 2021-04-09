from xml.dom.minidom  import parse
import xml.dom.minidom

ArbolDom = xml.dom.minidom.parse("rss.xml")
item = ArbolDom.getElementsByTagName("item")
for i in item:
    titulo = i.getElementsByTagName("title")[0].firstChild.data
    enlace = i.getElementsByTagName("link")[0].firstChild.data
    description = i.getElementsByTagName("description")[0].firstChild.data
    print("titulo:", titulo)
    print("enlace:", enlace)
    print("description:", description)
    print("-----")