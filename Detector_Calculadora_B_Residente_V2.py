
import cv2
import os

# Conectar con DroidCam
cap = cv2.VideoCapture(
    "http://192.168.1.35:4747/video"
)

# Cargar clasificador de la calculadora
base = os.path.dirname(os.path.abspath(__file__))

ruta = os.path.join(
    base,
    "classifier",
    "cascade.xml"
)

CalculadoraClassif = cv2.CascadeClassifier(ruta)

# Comprobar clasificador
if CalculadoraClassif.empty():
    print("ERROR: No se pudo cargar cascade.xml")
    cap.release()
    exit()

print("Clasificador de calculadora cargado correctamente")

# Comprobar camara
if not cap.isOpened():
    print("ERROR: No se pudo conectar con DroidCam")
    exit()

print("Camara conectada correctamente")

while True:

    ret, frame = cap.read()

    if not ret:
        print("No se pudo recibir imagen")
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    toy = CalculadoraClassif.detectMultiScale(
        gray,
        scaleFactor=5,
        minNeighbors=91,
        minSize=(70,78)
    )

    for (x,y,w,h) in toy:

        # Calcular margenes alrededor de la calculadora
        margen_x = int(w * 0.70)
        margen_y = int(h * 0.40)

        # Ampliar el rectangulo
        x1 = max(x - margen_x, 0)
        y1 = max(y - margen_y, 0)

        x2 = min(x + w + margen_x, frame.shape[1])
        y2 = min(y + h + margen_y, frame.shape[0])

        # Dibujar rectangulo verde
        cv2.rectangle(
            frame,
            (x1,y1),
            (x2,y2),
            (0,255,0),
            2
        )

        # Mostrar nombre del objeto
        cv2.putText(
            frame,
            'Calculadora_Cientifica',
            (x1,max(y1-10,20)),
            cv2.FONT_HERSHEY_SIMPLEX,
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

