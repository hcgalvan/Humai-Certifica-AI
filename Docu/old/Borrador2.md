# Biomecánica: Análisis en tiempo real

 El propósito es resolver algunos de los siguientes problemas:

* *Malas posturas (Reconocerlos, educar y reentrenar)*
* Patologías y lesiones (Educar en ejercicios terapéuticos)
* Pérdida muscular ( Recuperar la musculatura)
* Dolor y deterioro muscular (Mejorar el dolor, limitar el deterioro y recuperar la actividad al máximo)

Por el tiempo que contamos, veo mayor viabilidad el primer punto.

---
La postura humana es un aspecto importante de la salud y el bienestar general, que afecta la salud física como la mental. La mala postura puede provocar una variedad de problemas, que incluyen dolor de espalda, dolores de cabeza e incluso depresión. Sin embargo, muchas personas desconocen su postura y es posible que no sepan cómo corregirla.

Para abordar este problema, los investigadores están desarrollando tecnología que puede clasificar varias posturas humanas en tiempo real y ubicar diferentes partes del cuerpo.Esta tecnología podrá identificar y corregir las posturas del usuario, ayudándole a mejorar su salud y bienestar general.

Un ejemplo de esta tecnología es el uso de sensores de captura de movimiento, que pueden rastrear el movimiento de diferentes partes del cuerpo. Estos sensores se pueden utilizar para analizar la postura del usuario y proporcionar información sobre cómo mejorarla. Otro ejemplo es el uso de algoritmos de aprendizaje automático, que pueden analizar datos de sensores de captura de movimiento e identificar patrones en la postura del usuario.

## Posturas humanas
Los trastornos musculoesqueléticos ocupacionales, en particular el dolor lumbar crónico (LBP, por sus siglas en inglés), son ubicuos debido a la sedestación estática prolongada o las posiciones no ergonómicas de la sedestación.
https://pubmed.ncbi.nlm.nih.gov/27868066/


## Estimación de la pose humana

La estimación de la pose humana es un subconjunto del campo más amplio de la visión artificial y el aprendizaje automático. Es el proceso mediante el cual las máquinas pueden identificar lo que está haciendo una persona en una escena determinada. Tiene como objetivo predecir las poses de las partes y articulaciones del cuerpo humano en imágenes o videos.

### Modelos para modelado del cuerpo humano

Hay tres tipos de modelos para el modelado del cuerpo humano:

* El modelo cinemático, basado en la pose del esqueleto, se utiliza para estimar y representar la estructura del cuerpo humano, articulaciones y sus relaciones en 2D y 3D.
* Modelo plano, o contornos, se utiliza para estimar y representar forma, apariencia y poses del cuerpo humano en 2D estadístico.
* Modelo volumétrico, o poses en 3D. Se utilizan para estimar la forma, articulado y poses del cuerpo humano en 3D estadístico.

### Descripción de la arquitectura del modelo

Los modelos de estimación de pose humana involucra:

* Enfoques "De abajo hacia arriba" o ascendente : las articulaciones del cuerpo se examinan primero una por una y luego se organizan para formar una pose única.
* Enfoques "De arriba hacia abajo"o descendente: primero ejecuta un detector de cuerpos y demarca los cuadros delimitadores para cada cuerpo antes de determinar las uniones del cuerpo dentro de los cuadros delimitadores.

Estos puntos claves o uniones serían las articulaciones: el codo, las rodillas, las muñecas, etc. Hay dos tipos de estimación de pose: pose múltiple y pose única. La estimación de pose única estima las poses de un solo objeto en una escena determinada, y la estimación de pose múltiple detectan poses para varios objetos.

Se ha demostrado que el aprendizaje profundo trajeron avances y rendimiento en tareas de estimación de posturas que superan a los métodos clásicos.

### Métodos Populares de Estimación de poses con aprendizaje profundo

* Método #1: OpenPose, es un enfoque ascendente
detección de múltiples personas en tiempo real de código abierto, con alta precisión en la detección de puntos clave del cuerpo, el pie, la mano y la cara.
* Método #2:High-Resolution Net (HRNet), Es una red neuronal utilizada en problemas de procesamiento de imágenes para encontrar lo que conocemos como puntos clave (articulaciones). Es útil para la detección de la postura humana en los deportes televisados por su capacidad de analizar representaciones de baja calidad.
* Método #3: Corte profundo, es enfoque ascendente, El modelo funciona detectando la cantidad de personas en una imagen y luego prediciendo las ubicaciones conjuntas para cada imagen.
* Método #4: Regional Multi-Person Pose Estimation (AlphaPose), implementa un enfoque descendente, aplicable para detectar poses de una o varias personas en imágenes o campos de video.
* Método #5: DeepPose, captura todas las articulaciones, articula una capa de agrupación, una capa de convolución y una capa totalmente conectada para formar parte de estas capas.
* Método #6: PoseNet, construida en tensorflow.js para ejecutarse en dispositivos livianos como el navegador o el dispositivo móvil. Por lo tanto, PoseNet se puede utilizar para estimar una sola pose o varias poses.
* Método #7: DensePose, tiene como objetivo mapear todos los píxeles humanos de una imagen RGB en la superficie 3D del cuerpo humano. DensePose también se puede utilizar para problemas de estimación de pose única y múltiple.
*

Con el conjunto de datos ***MS COCO*** puede detectarse 17 puntos clave diferentes (clases). Cada punto clave se anota con tres números (x,y,v), donde **x** e **y** marcan las coordenadas yv indica si el punto clave es visible.

Casos de uso y aplicaciones de estimación de pose

Fuente:

### Aplicaciones de Estimación de poses

La estimación de pose tiene aplicaciones en muchos campos

* En **actividad humana**
  * Aplicación para detectar gestos sentados Comunicación de cuerpo completo/lenguaje de señas (por ejemplo, señales de policías de tránsito)
  * Aplicaciones en el **ámbito sanitario** hay aplicaciones que pueden medir distonías musculares para estudiar la eficacia de un tratamiento. O aplicaciones que nos ayuden a realizar correctamente nuestros ejercicios de fisioterapia o detectar si una persona se ha caído o está enferma.
  * Aplicaciones en el **ámbito deportivo** es muy útil para detectar los movimientos de deportistas realizando alguna acción. Podemos hacer desde una aplicación que te enseñe a lanzar tiros libres hasta una que te indique cómo mejorar tu pedaleo en ciclismo así para apoyar el análisis de fútbol, ​​baloncesto y deportes.
  * Aplicaciones para analizar **técnicas de danza** (por ejemplo, en danzas de ballet)
  * Aplicación del **aprendizaje de posturas para trabajos corporales y sutilezas**.
  * Aplicaciones en el **ámbito de la seguridad**, podemos estudiar las poses de las personas para saber si están predispuestas a la violencia en grandes concentraciones. Las cámaras de un estadio deportivo podrían analizar la pose de la gente y mandar seguridad si detecta actividad sospechosa.
* En **Realidad Aumentada y Realidad Virtual**, estimación de poses interconectada con aplicaciones de realidad aumentada y virtual brinda a los usuarios una mejor experiencia en línea, programas de realidad aumentada para ser utilizados en combate. Estos programas tienen como objetivo ayudar a los soldados a distinguir entre tropas enemigas y amigas, así como mejorar la visión nocturna.
* En **Robots de entrenamiento con seguimiento de pose humana**, aplicaciónes de hacer que los robots aprendan ciertos oficios.
* En **Seguimiento de movimiento humano para consolas**, plicaciones dentro del juego, donde los sujetos humanos generan automáticamente e inyectan poses en el entorno del juego para una experiencia de juego interactiva.
  
En el ámbito del **entretenimiento** podemos diseñar juegos que se controlan con nuestra propia posición corporal.

¿Cómo obtengo un modelo de estimación de la pose? ¿Dónde puedo ver ejemplos?
Puedes empezar por aquí: <https://github.com/tensorflow/tfjs-models/tree/master/pose-detection>
<https://github.com/hpssjellis/tfjs-models-purejs-posenet>
<https://hpssjellis.github.io/tfjs-models-purejs-posenet/>

Fuente: <https://eniit.es/estimacion-de-la-pose-con-deep-learning/>

Repositorios de Python - MediaPipe - OpenCV
<https://www.youtube.com/watch?v=TpkMdHIXkik>
<https://omes-va.com/estimacion-postura-mediapipe-python/>

<https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/pose.py>

<https://iheanyiigboko.wordpress.com/2019/06/08/4-easy-ways-to-improve-your-posture/>

### Objetivo Personal
>
>Promover el bienestar humano a traves del *movimiento corporal*, afianzamiento las capacidades físicas, cognitivas y afectivas de la persona.
>
## Proyecto

### Objetivo del proyecto

Replicar los resultados de investigación "Clasificación y corrección de posturas
humanas en dispositivos móviles"
Fuente: <https://m.riunet.upv.es/bitstream/handle/10251/175049/Perez%20-%20Clasificacion%20y%20correccion%20de%20posturas%20humanas%20en%20dispositivos%20moviles.pdf?sequence=1&isAllowed=y>

### Problema a revolver
 >
 > En el **ámbito sanitario** Malas posturas

### Diseño y estrategia

* Detectar una persona
* Una cámara web standar de pc, celular que graba la escena
* aplicar el modelo a video
* modelo 3D
* Modelo de estimación de pose de TensorFlow
*

<https://www.argentina.gob.ar/inti/estudio-antropometrico-nacional-argentino>

---

## Diferentes estudios explorados para acotar los puntos anteriores

### Enfoque podría ser en los adultos
>
>La educación física es parte del proceso educativo de toda persona, centrada en el movimiento corporal con el fin de lograr un afianzamiento en las capacidades físicas, cognitivas y afectivas de la persona.
Fuente: <http://www.austriaco.edu.gt/?page_id=751>

>Cada semana, los adultos necesitan 150 minutos de actividad física de intensidad moderada y 2 días de actividad para fortalecer sus músculos, de acuerdo con las Recomendaciones de actividad física para estadounidenses actuales (enlace solo en inglés)
Fuente: <https://www.cdc.gov/physicalactivity/basics/spanish/Cuanta-actividad-fisica-necesitan-los-adultos.htm#:~:text=Cada%20semana%2C%20los%20adultos%20necesitan>,(enlace%20solo%20en%20ingl%C3%A9s).

### Tratamiento multidisciplinar del aparato locomotor

1. Recuperación Muscular
Si se descarta una enfermedad sistémica, será recomendable abordar las diferentes estructuras, comenzando generalmente por la recuperación muscular para evitar las tracciones de los músculos fibrosados sobre las demás estructuras.
2. Optimización deportiva
Al final, con la optimización deportiva el objetivo será mejorar el dolor, limitar el deterioro y recuperar la actividad al máximo.

Aquí nos ayudarán los suplementos y los planes de acondicionamiento deportivo, que mantendrá la biomecánica en el mejor estado posible y evitarán y/o minimizarán las recaídas.

* Fuente: <https://clinalgia.com/tratamientos-aparato-locomotor/>

### Biomecánica y ML, DL, CV entre otros

La visión artificial (computer vision) es una de las áreas en donde el aprendizaje profundo(Deep Learning) proporciona una mejora considerable para realizar un análisis en tiempo real de la biomecánica deportiva,  a través del análisis de video.

* Fuente: <https://www.linkedin.com/pulse/aplicaci%C3%B3n-de-deep-learning-en-tiro-con-arco-zarate-torres/?originalSubdomain=es>
* Repositorio: <https://github.com/CMU-Perceptual-Computing-Lab/openpose>

### A Random Forest Machine Learning Framework to Reduce Running Injuries in Young Triathletes

 Con el que hemos aprendido que cuando hacemos un estudio biomecánico lo primero que tenemos que observar es la cinemática 3D de la pelvis por su implicación directa en las lesiones de carrera, concretamente en un 98% de probabilidad de lesión.

* Fuente: <https://javimgramage.com/matematicas-y-biomecanica-aplicadas-al-rendimiento-en-carrera/>
* Paper: <https://www.mdpi.com/1424-8220/20/21/6388>

### Aplicación comercial de Biomecánica con inteligencia Artificial

Identifica patrones complejos, generando protocolos de exploración acorde a las variables que se presentan para ofrecer los posibles diagnósticos y tratamientos que más se aproximan a los resultados de la anamnesis y exploración.

La anamnesis es el proceso de la exploración clínica que se ejecuta mediante el interrogatorio para identificar personalmente al individuo, conocer sus dolencias actuales, obtener una retrospectiva de él y determinar los elementos familiares, ambientales y personales relevantes.

Al recoger los datos de la anamnesis, peso, estatura y actividad que realiza habitualmente, junto con el motivo de consulta y la localización del dolor, HIGEA calcula y acota todas las posibles patologías y lesiones relacionadas con estos datos. En este momento te propone diferentes exploraciones para terminar ofreciendo hasta 4 diagnósticos por % de aproximación, así como tratamientos y ejercicios terapéuticos.

* Fuente: <https://higeaonline.com/>

## Otras fuentes exploradas

<https://viso.ai/deep-learning/pose-estimation-ultimate-overview>
<https://kemtai.com/blog/the-complete-guide-to-human-pose-estimation>
<https://cmu-perceptual-computing-lab.github.io/openpose/web/html/doc/index.html>

## Datasets

<https://cocodataset.org/#download>

## Códigos en Repositorios

<https://github.com/Devashi-Choudhary/AI-Dance-based-on-Human-Pose-Estimation>
<https://github.com/AdiSuresh/dance-evaluator>
<https://github.com/Suddalakavya24/RealTime-Pose-Estimation>
<https://github.com/utkarsh-maheshwari/Dance-based-human-pose>
<https://github.com/yinghanlong/dance_pose_estimation>
<https://github.com/search?q=%22Dance%22+and+Pose+Estimation+Based&type=code>

El Aprendizaje profundo, subconjunto del aprendizaje automático no supervisado, utiliza red neuronal para identificar patrones en imagenes, videos, sonidos y demas formas de datos no estructurados. Uno de estos modelos, La estimación de pose humana es una forma de identificación de patrones que utiliza redes neuronales convulsionales profundas en visión artificial modernas.