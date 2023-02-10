# Biomecánica: Análisis en tiempo real con ML .

# Resumen

# Introducción

La biomecánica, evalúa si una postura corporal genera sobrecarga en la estructura del aparato locomotor humano. Las posturas correctas del cuerpo en movimiento como en reposo, están definidas en la higiene postural. La falta de higiene postural, llevan a problemas de salud y falta de bienestar general.

Las redes neuronales convulcionales, rama específica del aprendizaje profundo, emula el sistema visual humano. Esta arquitectura utiliza la visión artificial para identificar patrones, agrupando distintos modelos de aplicación. El grupo que investiga la estimación de la pose humana, ha logrado avances en rendimientos de eficiencia y bajo consumo para análisis en tiempo real.


---> aquí va la revision de articulos

Sin embargo, diferentes artículos se enfocaron a generar alternativas en arquitecturas de reconocimiento de posturas y artículos específicos avanzaron en su aplicación real con set de datos privados y arquitecturas no disponibles. Por lo tanto, en este artículo, propusimos diseñar un evaluador de posturas con la arquitectura pre-entrenada YOLO v7 o MediaPipe Pose y dataset públicos sinteticos y reales, que verifique la correcta postura corporal en bipedestación con movimiento o reposo para la población Argentina.
Esta contribución brinda valoración de arquitecturas genéricas de posturas con set de datos públicos, dentro del ámbito de higiene postural en biomecánica.
Específicamente, entrena una arquitectura pre-entrenada con posturas correctas de dataset públicos, conecta con camara web convencional y genera devolución en tiempo real del esqueleto con indicadores de poses correctas e incorrectas.



# Materiales y Métodos
Una de las tareas más difíciles en la visión por computadora es determinar el alto grado de configuración a realizar. Ya sea determinar la soltura del cuerpo humano con todas sus extremidades y la complejidad de resolver límites. Ya sea encontrar fronteras de partes similares o variaciones debido a la ropa, como el tipo de cuerpo, la iluminación, y muchos otros factores. Este problema se define como las técnicas de visión por computadora que predicen la ubicación de varios puntos clave humanos (articulaciones y puntos de referencia) como hombros, codos, muñecas, caderas, rodillas, tobillos y cuello.

MediaPipe Pose es una solución de Machine Learning para el seguimiento de la postura del cuerpo de alta fidelidad, que infiere 33 puntos de referencia 3D y una máscara de segmentación de fondo en todo el cuerpo a partir de fotogramas de video RGB utilizando BlazePose.

# Mediapipe Pose y Opencv: La red troncal de entrada (backbone).

MediaPipe Pose es una solución utiliza una canalización Machine Learning «detector-tracker» de dos pasos. En el primer paso, el detector facilita el fotograma de entrada a la capa convolucional que produce un mapa de características convolucionales. Luego, una red neuronal utiliza este mapa para predecir la región. A partir de la región predicha se remodela, utilizando una capa de agrupación de región de interés (RoI). En el segundo paso, el «tracker» predice los 33 puntos claves contenidos en esta ROI. Para tener un rendimiento rápido, condensado en unos milisegundos por fotograma, y lograr en tiempo real la canalización de ML compuesto por la detección y seguimiento de la pose, se observa que la señal más fuerte a la red neuronal encima del torso es la cara de la persona (debido al alto contraste y pequeñas variaciones). En el caso de un vıdeo, el detector se ejecuta solo en el primer fotograma. Para los fotogramas siguientes, se deriva la ROI que contiene los puntos clave obtenidos anteriormente, como se describe en la figura siguiente
En la salida del modelo denominado `pose_landmarks` Cada fotograma, es conformado por una lista de 33 puntos de referencia de la pose. Cada punto de referencia consta de lo siguiente:

`x` e `y`: Coordenadas del punto de referencia normalizadas [0.0, 1.0] por el ancho y la altura de la imagen, respectivamente.
`z`: Representa la profundidad del punto de referencia con la profundidad en el punto medio de las caderas como origen, y cuanto menor sea el valor, más cerca estará el punto de referencia de la cámara. La magnitud de z utilza aproximadamente la misma escala que x.
`visibility`: Un valor [0.0, 1.0] indica la probabilidad que el punto de referencia sea visible (presente y no presente) en la imagen.

---
BlazeFace: 
MediaPipe Face Detection es una solución ultrarrápida de detección de rostros que viene con 6 puntos de referencia y compatibilidad con múltiples rostros. Se basa en BlazeFace-detección de rostros neuronales en submilisegundos en GPU móviles-(1), un detector de rostros liviano y de buen rendimiento diseñado para la inferencia de GPU móvil
(1)https://arxiv-org.translate.goog/abs/1907.05047?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es

---

`cvtColor()`: Convierte una imagen de un espacio de color a otro. Color space conversion codes: CV_BGR2GRAY, CV_RGB2GRAY, CV_BGR2YCrCb, CV_YCrCb2BGR, CV_RGB2HSV, CV_HLS2RGB, CV_HLS2Lab.

`COLOR_BGR2RGB`Cuando el archivo de imagen se lee con la función `imread()`, el orden de los colores es BGR (azul, verde, rojo) y lo convierte a rojo, verde, azul.
BGR y RGB no son espacios de color, convenciones para el orden de los diferentes canales de color, se apilan para formar un píxel.(2)
Al leer un archivo de imagen en color, OpenCV `imread()`lee como una matriz NumPy `ndarray` de `row (height) x column (width) x color (3)`.
(2) https://stackoverflow.com/questions/50963283/imshow-doesnt-need-convert-from-bgr-to-rgb


Mientras que BGR se usa consistentemente en OpenCV, la mayoría de las otras bibliotecas de procesamiento de imágenes usan el orden RGB por ello su necesaria conversion.

Parámetros
`Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5`, entonces
`min_detection_confidence`: Define Valor mínimo de confianza ( [0.0, 1.0]) del modelo de detección de personas para que la detección se considere exitosa. Predeterminado a 0.5
`min_tracking_confidence`: Define valor mínimo de confianza dondel el mínimo es ( [0.0, 1.0]), para que el modelo de seguimiento de puntos de referencia se consideren rastreados correctamente, sino se invocará la detección en la siguiente imagen. Predeterminado a 0.5
`ret, frame = cap.read()`: 
* `ret`: Tiene un valor booleano. Es verdadero si el marco se lee con éxito, de lo contrario, es falso.
* `frame`: este es el fotograma real que se lee. Este marco se puede almacenar en una variable y se puede usar de manera similar a cómo cargamos imágenes individuales.

`cv2.isOpened()`
* `isOpened()`: Verifica si está inicializado la cámara

`cap = cv2.VideoCapture(0)`
`alto = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)`
`ancho = cap.get(cv2.CAP_PROP_FRAME_WIDTH)`
`fps = cap.get(cv2.CAP_PROP_FPS)`
`cv2.VideoWriter(VIDEO_PATH, cv2.VideoWriter_fourcc('P','I','M','1'), fps, (int(ancho), int(alto)))`
* `fourcc`: se utiliza para comprimir los fotogramas, tiene 4 caracteres para definir el códec. Por ejemplo, VideoWriter.fourcc('P','I','M','1') es un códec MPEG-1.
* `fps`: Es para definir velocidad de fotogramas de la transmisión de video creada.
* `get(CAP_PROP_FPS)` o `get(CV_CAP_PROP_FPS)`: obtiene los fotogramas por segundo de la cámara.
* `get(cv2.CAP_PROP_FRAME_HEIGHT)`, `get(cv2.CAP_PROP_FRAME_WIDTH)`: obtiene valores de la altura y ancho del marco de la cámara.

`cv2.waitKey(10)`
* `waitKey()`: Espera un evento, en base a un tiempo en milisegundos, solo si hay una ventana activa.

`cap.release()`
* `release()`: Libera el recurso, la cámara que está utilizando.


# Resultados

# Discusión

# Literatura Citada