import matplotlib.pyplot as plt
import numpy as np

# El principal comando de Matplotlib es plot(), el cual permite representar gráficamente una lista de pares
# de valores (x, y) sobre un eje de coordenadas uniendo cada punto de acuerdo al orden en que aparecen.

print(" 1.- definiendo eje x e y")
print(" 2.- definiendo solo eje y")
print(" 3.- definiendo ejes y datos con rangos")
print(" 4.- varios plot fusionados en un mismo grafico")
print(" 5.- un plot con varios graficos")
print(" 6.- utilizando las dos librerias: matplotlib y numpy")
print(" 7.- representar función cuadrática")
print(" 8.- representar función lineal, cuadrática y cúbica")
print(" 9.- representar función lineal, cuadrática y cúbica (marcando puntos)")
print("10.- marcar un punto en una gráfica")
print("11.- histogramas")
print("12.- diagramas de barras")
print("13.- diagramas de circulares")
print("14.- Diagramas de dispersión")

opcion = int(input('opción ¿?: '))

# definiendo eje x e y
if opcion==1:
    plt.plot([0,1,3,5],[-7,1,4,5])
    plt.show()

# definiendo solo eje y
if opcion==2:
    plt.plot([-7,1,4,5])
    plt.show()

# definiendo ejes y datos con rangos
if opcion==3:
    x = range(8)
    plt.plot(x, [xi**2 for xi in x])
    plt.show()

# varios plot en un mismo grafico
if opcion==4:
    x = range(8)
    plt.plot(x, [xi**2 for xi in x])
    plt.plot(x, [xi**3 for xi in x])
    plt.plot(x, [xi**4 for xi in x])
    plt.show()

# un plot con varios graficos
if opcion==5:
    x = range(8)
    plt.plot(x, [xi**2 for xi in x], x, [xi**3 for xi in x], x, [xi**4 for xi in x])
    plt.show()

# utilizando las dos librerias: matplotlib y numpy
if opcion==6:
    x = np.arange(8)
    plt.plot(x, [xi ** 2 for xi in x])
    plt.xticks(range(8), ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    plt.yticks(range(0, 16, 2))
    plt.show()

# representar función cuadrática
if opcion==7:
    x = range(8)
    plt.plot(x, [xi ** 2 for xi in x])
    plt.grid(True)
    plt.title("Representación de la función cuadrática ")
    plt.xlabel("Eje de valores X")
    plt.ylabel("Eje de valores Y")
    plt.show()

# representar función lineal, cuadrática y cúbica
if opcion==8:
    x = range(8)
    plt.plot(x, [xi for xi in x], label="Lineal")
    plt.plot(x, [xi ** 2 for xi in x], label="Cuadrática")
    plt.plot(x, [xi ** 3 for xi in x], label="Cúbica")
    plt.grid(True)
    plt.title("Representación de la función cuadrática ")
    plt.xlabel("Eje de valores X")
    plt.ylabel("Eje de valores Y")
    plt.legend()
    plt.show()

# representar función lineal, cuadrática y cúbica (marcando puntos)
if opcion==9:
    x = range(8)
    plt.plot(x, [xi for xi in x], 'b-d', label="Lineal")
    plt.plot(x, [xi ** 2 for xi in x], 'y--p', label="Cuadrática")
    plt.plot(x, [xi ** 3 for xi in x], 'r:s', label="Cúbica")
    plt.legend()
    plt.xlabel("Eje de valores X")
    plt.ylabel("Eje de valores Y")
    plt.show()

# marcar un punto en una gráfica
if opcion==10:
    x = range(8)
    plt.plot(x, [xi for xi in x])
    plt.grid(True)
    plt.annotate("Punto (3,3)", xy=(3, 3), xytext=(4, 3),
                 arrowprops=dict(facecolor="green", shrink=0.05, headlength=2))
    plt.show()

# histogramas
if opcion==11:
    y = np.random.randn(1000)
    plt.hist(y, 15)
    plt.show()

# 12.- diagramas de barras
if opcion == 12:
    left=range(5)
    p1 = plt.bar(left, height=[20,35,30,35,27], width=0.4, color='green', yerr=[2,3,4,1,2])
    p2 = plt.bar(left, height=[25,32,34,20,25], width=0.4, color='red',   bottom=[20,35,30,35,27], yerr=[3,5,2,3,3])
    plt.legend(["Secuencia 1","Secuencia 2"])
    plt.xticks(range(5),["A","B","C","D","E"])
    plt.show()

# 13.- diagramas de circulares
if opcion == 13:
    # x = [4,7,5,3,9,15] # en caso de no sumar 100% se se calcula el porcentaje
    x = [10, 15, 18, 22, 20, 15] # si suma 100% se respeta la distribucion
    labels = ['Madrid', 'Barcelona', 'Valencia', 'Zaragoza', 'Sevilla', 'Granada']
    colors = ['yellow', 'blue', 'red', 'green', 'brown', 'orange']
    explode = [0.2, 0.2, 0, 0, 0.1, 0.1]
    plt.pie(x, labels=labels, labeldistance=1.3, explode=explode, autopct='%1.1f%%',
            colors=colors, pctdistance=0.5, shadow=True);
    plt.show()

# 14.- Diagramas de dispersión
if opcion == 14:
    x = np.random.randn(1000)
    y = np.random.randn(1000)
    colores = np.random.randn(1000)
    tam = 50 * np.random.randn(1000)
    plt.scatter(x, y, s=tam, c=colores, marker='+')
    plt.show()