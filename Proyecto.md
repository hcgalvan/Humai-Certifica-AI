# Biomecánica: Análisis en tiempo real

 El propósito es resolver algunos de los siguientes problemas:
* *Malas posturas (Reconocerlos, educar y reentrenar)*
* Patologías y lesiones (Educar en ejercicios terapéuticos)
* Pérdida muscular ( Recuperar la musculatura)
* Dolor y deterioro muscular (Mejorar el dolor, limitar el deterioro y recuperar la actividad al máximo)

Por el tiempo que contamos, veo mayor viabilidad el primer punto.

---
### Ejemplos de uso de Estimación de la Pose
Es imposible enumerar todos los usos de esta tecnología, pero contaré algunos de los que más me gustan a mí o más curiosos me parecen.

* En el **ámbito deportivo** es muy útil para detectar los movimientos de deportistas realizando alguna acción. Podemos hacer desde una aplicación que te enseñe a lanzar tiros libres hasta una que te indique cómo mejorar tu pedaleo en ciclismo.
* En el **ámbito sanitario** hay aplicaciones que pueden medir distonías musculares para estudiar la eficacia de un tratamiento. O aplicaciones que nos ayuden a realizar correctamente nuestros ejercicios de fisioterapia.
* En el **ámbito de la seguridad**, podemos estudiar las poses de las personas para saber si están predispuestas a la violencia en grandes concentraciones. Las cámaras de un estadio deportivo podrían analizar la pose de la gente y mandar seguridad si detecta actividad sospechosa.
En el ámbito del **entretenimiento** podemos diseñar juegos que se controlan con nuestra propia posición corporal.

¿Cómo obtengo un modelo de estimación de la pose? ¿Dónde puedo ver ejemplos? 
Puedes empezar por aquí: https://github.com/tensorflow/tfjs-models/tree/master/pose-detection
https://github.com/hpssjellis/tfjs-models-purejs-posenet
https://hpssjellis.github.io/tfjs-models-purejs-posenet/

Fuente: https://eniit.es/estimacion-de-la-pose-con-deep-learning/

Repositorios de Python - MediaPipe - OpenCV
https://www.youtube.com/watch?v=TpkMdHIXkik
https://omes-va.com/estimacion-postura-mediapipe-python/

https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/pose.py



### Objetivo Personal
>Promover el bienestar humano a traves del *movimiento corporal*, afianzamiento las capacidades físicas, cognitivas y afectivas de la persona.
## Proyecto: 


### Objetivo del proyecto: 
Replicar los resultados de investigación "Clasificación y corrección de posturas
humanas en dispositivos móviles"
Fuente: https://m.riunet.upv.es/bitstream/handle/10251/175049/Perez%20-%20Clasificacion%20y%20correccion%20de%20posturas%20humanas%20en%20dispositivos%20moviles.pdf?sequence=1&isAllowed=y

### Problema a revolver
 > En el **ámbito sanitario** Malas posturas

### Diseño y estrategia 

* Detectar una persona
* Una cámara web standar de pc, celular que graba la escena
* aplicar el modelo a video
* modelo 3D
* Modelo de estimación de pose de TensorFlow
*
https://www.argentina.gob.ar/inti/estudio-antropometrico-nacional-argentino

---


## Diferentes estudios explorados para acotar los puntos anteriores.

### Enfoque podría ser en los adultos
>La educación física es parte del proceso educativo de toda persona, centrada en el movimiento corporal con el fin de lograr un afianzamiento en las capacidades físicas, cognitivas y afectivas de la persona.
Fuente: http://www.austriaco.edu.gt/?page_id=751

>Cada semana, los adultos necesitan 150 minutos de actividad física de intensidad moderada y 2 días de actividad para fortalecer sus músculos, de acuerdo con las Recomendaciones de actividad física para estadounidenses actuales (enlace solo en inglés)
Fuente: https://www.cdc.gov/physicalactivity/basics/spanish/Cuanta-actividad-fisica-necesitan-los-adultos.htm#:~:text=Cada%20semana%2C%20los%20adultos%20necesitan,(enlace%20solo%20en%20ingl%C3%A9s).


### Tratamiento multidisciplinar del aparato locomotor
3. Recuperación Muscular
Si se descarta una enfermedad sistémica, será recomendable abordar las diferentes estructuras, comenzando generalmente por la recuperación muscular para evitar las tracciones de los músculos fibrosados sobre las demás estructuras.
9. Optimización deportiva
Al final, con la optimización deportiva el objetivo será mejorar el dolor, limitar el deterioro y recuperar la actividad al máximo.

Aquí nos ayudarán los suplementos y los planes de acondicionamiento deportivo, que mantendrá la biomecánica en el mejor estado posible y evitarán y/o minimizarán las recaídas.
+ Fuente: https://clinalgia.com/tratamientos-aparato-locomotor/

### Biomecánica y ML, DL, CV entre otros
La visión artificial (computer vision) es una de las áreas en donde el aprendizaje profundo(Deep Learning) proporciona una mejora considerable para realizar un análisis en tiempo real de la biomecánica deportiva,  a través del análisis de video.
+ Fuente: https://www.linkedin.com/pulse/aplicaci%C3%B3n-de-deep-learning-en-tiro-con-arco-zarate-torres/?originalSubdomain=es
+ Repositorio: https://github.com/CMU-Perceptual-Computing-Lab/openpose

### A Random Forest Machine Learning Framework to Reduce Running Injuries in Young Triathletes
 Con el que hemos aprendido que cuando hacemos un estudio biomecánico lo primero que tenemos que observar es la cinemática 3D de la pelvis por su implicación directa en las lesiones de carrera, concretamente en un 98% de probabilidad de lesión.
+ Fuente: https://javimgramage.com/matematicas-y-biomecanica-aplicadas-al-rendimiento-en-carrera/
+ Paper: https://www.mdpi.com/1424-8220/20/21/6388

### Aplicación comercial de Biomecánica con inteligencia Artificial

Identifica patrones complejos, generando protocolos de exploración acorde a las variables que se presentan para ofrecer los posibles diagnósticos y tratamientos que más se aproximan a los resultados de la anamnesis y exploración.

La anamnesis es el proceso de la exploración clínica que se ejecuta mediante el interrogatorio para identificar personalmente al individuo, conocer sus dolencias actuales, obtener una retrospectiva de él y determinar los elementos familiares, ambientales y personales relevantes.

Al recoger los datos de la anamnesis, peso, estatura y actividad que realiza habitualmente, junto con el motivo de consulta y la localización del dolor, HIGEA calcula y acota todas las posibles patologías y lesiones relacionadas con estos datos. En este momento te propone diferentes exploraciones para terminar ofreciendo hasta 4 diagnósticos por % de aproximación, así como tratamientos y ejercicios terapéuticos.
+ Fuente: https://higeaonline.com/

