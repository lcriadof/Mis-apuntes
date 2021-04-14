from xml.etree import ElementTree

f = open ("rss.xml", 'rt')
arbol = ElementTree.parse(f)
print (arbol)
for nodo in arbol.iter():
    print (nodo.tag, "---",nodo.text, "---" ,nodo.attrib)