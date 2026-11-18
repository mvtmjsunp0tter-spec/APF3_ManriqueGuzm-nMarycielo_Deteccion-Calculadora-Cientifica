
# APF3_ManriqueGuzmánMarycielo_Deteccion-Calculadora-Cientifica

## Sistema de detección de una calculadora científica mediante Python y OpenCV

### 1. Descripción del proyecto

El presente proyecto consiste en desarrollar un sistema de detección de una calculadora científica mediante técnicas de visión artificial, utilizando Python y la biblioteca OpenCV.

Para el reconocimiento del objeto se empleó el método Haar Cascade, cuyo modelo fue entrenado mediante la herramienta Cascade Trainer GUI. Posteriormente, se implementó el clasificador en un programa de Python para realizar detecciones en tiempo real mediante una cámara conectada a través de DroidCam.

### 2. Objetivo

Desarrollar un sistema capaz de identificar y detectar una calculadora científica en imágenes capturadas por una cámara, utilizando un clasificador entrenado mediante Haar Cascade.

### 3. Herramientas utilizadas

- Python.
- OpenCV.
- Haar Cascade.
- Cascade Trainer GUI.
- DroidCam.

### 4. Dataset utilizado

Para el entrenamiento del clasificador se elaboró un conjunto de imágenes dividido en dos categorías:

- **Imágenes positivas (p):** 100 imágenes que contienen la calculadora científica.
- **Imágenes negativas (n):** más de 200 imágenes en las que no aparece la calculadora.

Las imágenes fueron recopiladas considerando diferentes fondos, posiciones y condiciones de captura.

### 5. Entrenamiento del modelo

El entrenamiento se realizó mediante Cascade Trainer GUI, utilizando las imágenes positivas y negativas del dataset.

Como resultado se obtuvo el archivo `cascade.xml`, que contiene el clasificador entrenado para reconocer la calculadora científica.

### 6. Implementación

El modelo entrenado se integró en un programa desarrollado en Python con OpenCV. El sistema captura imágenes en tiempo real, analiza los fotogramas y, cuando reconoce la calculadora, dibuja un rectángulo alrededor del objeto detectado.

### 7. Resultados

Durante las pruebas realizadas, el sistema logró detectar correctamente la calculadora científica mediante la cámara, demostrando el funcionamiento del modelo entrenado.

### 8. Estructura del proyecto

- `p/`: imágenes positivas.
- `n/`: imágenes negativas.
- `classifier/`: modelo entrenado `cascade.xml`.
- `APF3_Marycielo.py`: código fuente del detector.
- `Informe.pdf`: informe técnico del proyecto.

### 9. Ejecución del programa

Para ejecutar el detector se requiere:

1. Tener instalado Python.
2. Instalar OpenCV:

   `pip install opencv-python`

3. Verificar que el archivo `cascade.xml` esté ubicado en la ruta indicada en el código.
4. Ejecutar el archivo Python del detector.

### 10. Autora

**Marycielo Manrique Guzmán**

Proyecto académico de detección de objetos mediante visión artificial.
