# Poses_CompVis_app
Contador de Poses sobre Computer Vision

Predice si un usuario levanta la mano derecha o levanta mano izquierda con modelo sklearn y mediapipe en una app tkinter.

Aquí aprendemos a:
  - Embeber un Modelo
  - Utilizar Mediapipe
  - Utilizar opencv
  - Lanzar Tkinter
  
  ## Configuración del entorno
  
* OpenCV: usará esta biblioteca para la visión por computadora y para realizar técnicas de procesamiento de imágenes en la imagen de entrada.
* MediaPipe: utilizará esta biblioteca para realizar la detección manual y el seguimiento de la imagen de entrada.
* imutils: usará esta biblioteca para cambiar el tamaño del cuadro de video de la entrada.
  ## Comandos para Construir y Lanzar app

  ### Considere crear un entorno
* `python -m venv venvpose`

Si estas en Windows con VsCode, dentro de carpeta app:
* `venvpose\Scripts\Activate.ps1`

Una vez activado el entorno, construir:
* `python install -r requirements.txt`

Lanzar app:
*  `python main.py`

<img alt='captura pose' src='https://raw.githubusercontent.com/hcgalvan/Humai-Certifica-AI/main/test/poses/images/app.png'>

<img alt='captura pose' src='https://raw.githubusercontent.com/hcgalvan/Humai-Certifica-AI/main/test/poses/images/entorno.png'>

**References** :
  - 