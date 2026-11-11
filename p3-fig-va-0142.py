import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import cv2
# yahir sifuentes NC = 0142 
print("yahir sifuentes NC 0142")
print("UIII Act3 colocar puntos a una imagen en blanco y negro con va ")
mi_imagen = cv2.imread("pele.png", 0)
plt.imshow(mi_imagen, cmap="gray")
plt.title("pele y yahir sifuentes 0142")
plt.show()
print("+-+-+-+- puntos en la imagen +-+-+-+-")
plt.imshow(mi_imagen, cmap="gray")
x = [100,100,300,340]
y = [100,400,500,300]
plt.scatter(x,y, s=20,c="red")
plt.show()
print("+-+-+-+- cuadro azul en la imagen +-+-+-+-")
img_pele = cv2.imread("pele.png", 0)
plt.imshow(img_pele, cmap="gray")
## nuevas cordenadas del cuadro
x = [105, 186, 186, 105, 105]
y = [150, 150, 231, 231, 150]
plt.plot(x,y,c="blue")
plt.show()
print("+-+-+-+- circulo verde en la imagen +-+-+-+-")
I = cv2.imread("pele.png", 0)
plt.imshow(I, cmap="gray")
N = 30 # lados del poligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340,350)
r = 150 # radio
for i in range(N+1):
    t = 2*np.pi/N*i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)
plt.plot(x,y,c="green")
plt.show()




