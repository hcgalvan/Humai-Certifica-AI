# Biomecánica & Redes Neuronales Convulcionales: Análisis en tiempo real con Modelos genéricos y datos públicos.

# Resumen

# Introducción

La biomecánica, evalúa si una postura corporal genera sobrecarga en la estructura del aparato locomotor humano. Las posturas correctas del cuerpo en movimiento como en reposo, están definidas en la higiene postural. La falta de higiene postural, llevan a problemas de salud y falta de bienestar general.

Las redes neuronales convulcionales, rama específica del aprendizaje profundo, emula el sistema visual humano. Esta arquitectura utiliza la visión artificial para identificar patrones, agrupando distintos modelos de aplicación. El grupo que investiga la estimación de la pose humana, ha logrado avances en rendimientos de eficiencia y bajo consumo para análisis en tiempo real.


---> aquí va la revision de articulos

Sin embargo, diferentes artículos se enfocaron a generar alternativas en arquitecturas de reconocimiento de posturas y artículos específicos avanzaron en su aplicación real con set de datos privados y arquitecturas no disponibles. Por lo tanto, en este artículo, propusimos diseñar un evaluador de posturas con la arquitectura pre-entrenada YOLO v7 o MediaPipe Pose y dataset públicos sinteticos y reales, que verifique la correcta postura corporal en bipedestación con movimiento o reposo para la población Argentina.
Esta contribución brinda valoración de arquitecturas genéricas de posturas con set de datos públicos, dentro del ámbito de higiene postural en biomecánica.
Específicamente, entrena una arquitectura pre-entrenada con posturas correctas de dataset públicos, conecta con camara web convencional y genera devolución en tiempo real del esqueleto con indicadores de poses correctas e incorrectas.



# Materiales y Métodos

MediaPipe Pose es una solución de ML para el seguimiento de la postura del cuerpo de alta fidelidad, que infiere 33 puntos de referencia 3D y una máscara de segmentación de fondo en todo el cuerpo a partir de fotogramas de video RGB utilizando BlazePose.


cvtColor(): Convierte una imagen de un espacio de color a otro. Color space conversion codes: CV_BGR2GRAY, CV_RGB2GRAY, CV_BGR2YCrCb, CV_YCrCb2BGR, CV_RGB2HSV, CV_HLS2RGB, CV_HLS2Lab.

Al leer un archivo de imagen en color, OpenCV imread()lee como una matriz NumPy `ndarray` de `row (height) x column (width) x color (3)`. El orden de color es BGR (azul, verde, rojo).


Parámetros

* ret: Tiene un valor booleano. Es verdadero si el marco se lee con éxito, de lo contrario, es falso.
* fotograma: este es el fotograma real que se lee. Este marco se puede almacenar en una variable y se puede usar de manera similar a cómo cargamos imágenes individuales
* isOpened(): Verifica si está inicializado la cámara
* fourcc: se utiliza para comprimir los fotogramas, tiene 4 caracteres para definir el códec. Por ejemplo, VideoWriter.fourcc('P','I','M','1') es un códec MPEG-1.
* fps: Es para definir velocidad de fotogramas de la transmisión de video creada.
* get(CAP_PROP_FPS) o get(CV_CAP_PROP_FPS): obtiene los fotogramas por segundo de la cámara.
* get(cv2.CAP_PROP_FRAME_HEIGHT), get(cv2.CAP_PROP_FRAME_WIDTH): obtiene valores de la altura y ancho del marco de cámara.
* waitKey(): Espera un evento, en base a un tiempo en milisegundos, solo si hay una ventana activa.
* release(): Libera el recurso, la cámara que está utilizando.


# Resultados

# Discusión

# Literatura Citada