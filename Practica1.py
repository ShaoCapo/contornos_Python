import numpy as np
import cv2
import random as rng

# leemos y mostramos la imagen original en color
im = cv2.imread('formas.png', cv2.IMREAD_COLOR)
cv2.imshow('0 color', im)
cv2.waitKey()

# leemos y mostramos la imagen original en niveles de gris
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('O gris', imgray)
cv2.waitKey()

# leemos y mostramos la imagen de contornos detectados utilizando Canny
canny = cv2.Canny(imgray, 127, 254)
cv2. imshow('CANNY', canny)
cv2.waitKey()

# obtenemos los datos de los contornos y su jerarquia
contornos, jerarquia = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# y los mostramos sobre una imagen vacia
imdraw = np.zeros((canny.shape[0], canny.shape[1]))
for i in range(len(contornos)):
    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
    cv2.drawContours(imdraw, contornos, i, color, 2)
cv2.imshow('contornos', imdraw)
cv2.waitKey()

# num contornos detectados
numContornos = len(contornos)
print("num contornos detectados es %r" %numContornos)

# Jerarquia [Next, Previous, First_Child, Parent]
print(jerarquia)

# obtenemos y mostramos los momentos de cada uno de los contornos
# y su centro para reconocer su posición en la imagen
for contorno in contornos:
    M = cv2.moments(contorno)
    print(M)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print('El centro de gravedad del contorno es (', cx, ',', cy, ')')