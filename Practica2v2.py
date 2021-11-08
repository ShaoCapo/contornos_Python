import cv2
import numpy as np

# Leemos y mostramos la imagen original
img = cv2.imread('numeros.png', cv2.IMREAD_COLOR)
cv2.imshow("Original", img)
cv2.waitKey()

# Convertimos la imagen a niveles de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Obtenemos y mostramos la imagen de contornos con Canny
edges = cv2.Canny(gray, 50, 200)
cv2.imshow("Canny", edges)
cv2.waitKey()

# Detectamos las lineas empleando la transformada de Hough
lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

# Mostramos el numero de lineas encontradas
print ("num lineas encontradas: %r" %len(lines))

# Mostramos el array de 3 dimensiones devuelto por la transformada
print (lines)

# Mostramos los valores rho, theta de las primeras lineas detectadas
print (lines [0] [0] [0])
print (lines [0] [0] [1])
print (lines [1] [0] [0])
print (lines [1] [0] [1])

# Dibujamos en verde todas las lineas detectadas con un grosor de 1 px
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        print (rho)
        theta = lines[i][0][1]
        print (theta)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int (x0 + 1000 * (-b)), int (y0 + 1000 * (a)))
        pt2 = (int (x0 - 1000 * (-b)), int (y0 - 1000 * (a)))
        cv2.line(img, pt1, pt2, (0, 255, 0), 1, cv2.LINE_AA)
        
# Mostramos la imagen con todas las lineas detectadas
cv2.imshow("Resultado", img)
cv2.waitKey()