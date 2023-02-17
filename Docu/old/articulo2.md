# Biomecánica & Redes Neuronales Convulcionales: Evaluación del análisis en tiempo real de Modelos genéricos y datos públicos.

# Resumen

# Introducción

La biomecánica, evalúa si una postura corporal genera sobrecarga en la estructura del aparato locomotor humano. Las posturas correctas del cuerpo en movimiento como en reposo, están definidas en la higiene postural. La falta de higiene postural, llevan a problemas de salud y falta de bienestar general.

Las redes neuronales convulcionales, rama específica del aprendizaje profundo, emula el sistema visual humano. Esta arquitectura utiliza la visión artificial para identificar patrones, agrupando distintos modelos de aplicación. El grupo que investiga la estimación de la pose humana, ha logrado avances en rendimientos de eficiencia y bajo consumo para análisis en tiempo real.


---> aquí va la revision de articulos

Sin embargo, diferentes artículos se enfocaron a generar alternativas en arquitecturas de reconocimiento de posturas y artículos específicos avanzaron en su aplicación real con set de datos privados y arquitecturas no disponibles. Por lo tanto, en este artículo, propusimos evaluar arquitecturas pre-entrenadas de estimación de posturas YOLO v7 con dataset públicos sinteticos y reales, que verifique la correcta postura corporal en bipedestación con movimiento o reposo para la población Argentina.
Esta contribución brinda valoración de arquitecturas genéricas de posturas con set de datos públicos, dentro del ámbito de higiene postural en biomecánica.
Específicamente, entrena una arquitectura pre-entrenada con posturas correctas de dataset públicos, conecta con camara web convencional y genera devolución en tiempo real del esqueleto con indicadores de poses correctas e incorrectas.



# Materiales y Métodos

# Resultados

# Discusión

# Literatura Citada

MediaPipe Pose es una solución de Machine Learning para el seguimiento de la postura del cuerpo de alta fidelidad, que infiere 33 puntos de referencia 3D y una máscara de segmentación de fondo en todo el cuerpo a partir de fotogramas de video RGB utilizando BlazePose.

---
BlazeFace: 
MediaPipe Face Detection es una solución ultrarrápida de detección de rostros que viene con 6 puntos de referencia y compatibilidad con múltiples rostros. Se basa en BlazeFace-detección de rostros neuronales en submilisegundos en GPU móviles-(1), un detector de rostros liviano y de buen rendimiento diseñado para la inferencia de GPU móvil
(1)https://arxiv-org.translate.goog/abs/1907.05047?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es

---
OpenCV es una solución escrita en C/C++, desarrollada por Intel, que esta dirigida fundamentalmente a la visión por computador en tiempo real. Entre sus bloques de funciones: a. estructuras y operaciones de matrices, grafos, árboles entre otros; b. procesamiento y análisis de imágenes; c. análisis de movimientos y seguimiento de objetos; d. adquisición de videos e interfaces gráficas de videos. Las operaciones básicas comienza con la captura de entrada de un video, sea un archivo o una cámara; define el número de filas o altura en pixeles, columnas o ancho en pixeles y canales; tipo de imagen, número de pixeles. A este arreglo o matriz llamado frame o fotograma realiza alguna operación. Estas tareas pasan por detección de objetos, demarcar partes importantes, agregar texto o cualquier otro tipo de gráfica.
Parámetros utilizados
`cvtColor()`: Convierte una imagen de un espacio de color a otro. Color space conversion codes: CV_BGR2GRAY, CV_RGB2GRAY, CV_BGR2YCrCb, CV_YCrCb2BGR, CV_RGB2HSV, CV_HLS2RGB, CV_HLS2Lab.
`COLOR_BGR2RGB`Cuando el archivo de imagen se lee con la función `imread()`, el orden de los colores es BGR (azul, verde, rojo) y lo convierte a rojo, verde, azul. BGR y RGB no son espacios de color, convenciones para el orden de los diferentes canales de color, se apilan para formar un píxel.(2)
Al leer un archivo de imagen en color, OpenCV `imread()`lee como una matriz NumPy `ndarray` de `row (height) x column (width) x color (3)`.
(2) https://stackoverflow.com/questions/50963283/imshow-doesnt-need-convert-from-bgr-to-rgb


Mientras que BGR se usa consistentemente en OpenCV, la mayoría de las otras bibliotecas de procesamiento de imágenes usan el orden RGB por ello su necesaria conversion.

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