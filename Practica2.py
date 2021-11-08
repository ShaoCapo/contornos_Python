import cv2
import numpy as np

# Leemos la imagen original
img = cv2.imread('numeros.png', cv2.IMREAD_COLOR)

# Convertimos la imagen a niveles de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Encontramos los contornos empleando Canny
edges = cv2.Canny(gray, 50, 200)

# Detectamos las lineas empleando la transformada de Hough
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength = 10, maxLineGap = 250)

# Mostramos el numero de lineas encontradas
print ("num lineas encontradas: %r" %len(lines))

# Mostramos el array de 3 dimensiones devuelto por la transformada
print (lines)

# Mostramos los valores x1, yl, x2, y2 de la primera linea detectada
print (lines [0] [0] [0])
print (lines [0] [0] [1])
print (lines [0] [0] [2])
print (lines [0] [0] [3])

# Dibujamos en azul las lineas detectadas con un grosor de 3 px
cv2.line(img, (lines[0][0][0], lines[0][0][1]), (lines[0][0][2], lines[0][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[1][0][0], lines[1][0][1]), (lines[1][0][2], lines[1][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[2][0][0], lines[2][0][1]), (lines[2][0][2], lines[2][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[3][0][0], lines[3][0][1]), (lines[3][0][2], lines[3][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[4][0][0], lines[4][0][1]), (lines[4][0][2], lines[4][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[5][0][0], lines[5][0][1]), (lines[5][0][2], lines[5][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[6][0][0], lines[6][0][1]), (lines[6][0][2], lines[6][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[7][0][0], lines[7][0][1]), (lines[7][0][2], lines[7][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[8][0][0], lines[8][0][1]), (lines[8][0][2], lines[8][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[9][0][0], lines[9][0][1]), (lines[9][0][2], lines[9][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[10][0][0], lines[10][0][1]), (lines[10][0][2], lines[10][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[11][0][0], lines[11][0][1]), (lines[11][0][2], lines[11][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[12][0][0], lines[12][0][1]), (lines[12][0][2], lines[12][0][3]), (255, 0, 0), 3)
cv2.line(img, (lines[13][0][0], lines[13][0][1]), (lines[13][0][2], lines[13][0][3]), (255, 0, 0), 3)

# Dibujamos las lineas sobre la imagen original en blanco y 1 px de grosor
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 1)

# Mostramos la imagen con todas las lineas detectadas
cv2.imshow("Result Image", img)
cv2.waitKey()