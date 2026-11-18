
import cv2
import numpy as np
import imutils
import os

Datos = "p"              # Carpeta para fotografias positivas

if not os.path.exists(Datos):
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos)

# Conectar con DroidCam
cap = cv2.VideoCapture("http://192.168.1.35:4747/video")

x1, y1 = 120, 40
x2, y2 = 550, 450

# CONTINUAR NUMERACION DESDE LA ULTIMA IMAGEN
imagenes = [
    archivo for archivo in os.listdir(Datos)
    if archivo.startswith("objeto_") and archivo.endswith(".jpg")
]

if len(imagenes) > 0:
    numeros = [
        int(archivo.replace("objeto_", "").replace(".jpg", ""))
        for archivo in imagenes
    ]
    count = max(numeros) + 1
else:
    count = 0

print("La siguiente imagen sera:", count)

# INICIAR CAPTURA
while True:

    ret, frame = cap.read()

    if ret == False:
        print("No se pudo recibir imagen de la camara")
        break

    imAux = frame.copy()

    cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 2)

    objeto = imAux[y1:y2, x1:x2]
    objeto = imutils.resize(objeto, width=38)

    k = cv2.waitKey(1) & 0xFF

    if k == ord('s'):

        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count), objeto)

        print('Imagen guardada: objeto_{}.jpg'.format(count))

        count = count + 1

    if k == 27:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('objeto', objeto)

# CERRAR CAMARA
cap.release()
cv2.destroyAllWindows()

print("Total de imagenes guardadas en esta sesion:", count)

