
import cv2
import os

# Conectar con DroidCam
cap = cv2.VideoCapture("http://192.168.1.35:4747/video")

# Buscar el archivo cascade.xml dentro de classifier
base = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(base, "classifier", "cascade.xml")

# Cargar clasificador de la calculadora
CalculadoraClassif = cv2.CascadeClassifier(ruta)

# Comprobar si el clasificador se cargo correctamente
if CalculadoraClassif.empty():
    print("ERROR: No se pudo cargar cascade.xml")
    print("Revisa la ubicacion:", ruta)
    cap.release()
    exit()

print("Clasificador cargado correctamente")

# Comprobar conexion de la camara
if not cap.isOpened():
    print("ERROR: No se pudo conectar con DroidCam")
    exit()

print("Camara conectada correctamente")

while True:

    ret, frame = cap.read()

    if not ret:
        print("No se pudo recibir imagen de la camara")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = CalculadoraClassif.detectMultiScale(
        gray,
        scaleFactor=5,
        minNeighbors=91,
        minSize=(70,78)
    )

    for (x,y,w,h) in toy:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        cv2.putText(
            frame,
            'Calculadora_Cientifica',
            (x,y-10),
            2,
            0.7,
            (0,255,0),
            2,
            cv2.LINE_AA
        )

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

