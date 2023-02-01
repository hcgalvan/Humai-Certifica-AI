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


Fuente: https://viso.ai/deep-learning/pose-estimation-ultimate-overview/