# Descripción
Este proyecto propone un evaluador de posturas embebido en app de escritorio aplicado a la biomecánica deportiva

## Configuración del entorno
  
* OpenCV: biblioteca de visión por computadora  realiza técnicas de procesamiento de imágenes en la imagen de entrada.
* MediaPipe: biblioteca para realizar detección manual y el seguimiento de la imagen de entrada.
* imutils: usará esta biblioteca para cambiar el tamaño del cuadro de video de la entrada.

## Comandos para Construir y Lanzar app

### Considere crear un entorno
* `python -m venv venvpose`

Si estas en Windows con VsCode, dentro de carpeta app:
* `venvpose\Scripts\Activate.ps1`

Una vez activado el entorno, construir:
* `pip install -r requirements.txt`

Lanzar app:
*  `python main.py`

## Mapa a las distintas carpetas y archivos


<img alt='captura pose' src='https://raw.githubusercontent.com/hcgalvan/Humai-Certifica-AI/main/test/poses/images/app.png'>

<img alt='captura pose' src='https://raw.githubusercontent.com/hcgalvan/Humai-Certifica-AI/main/test/poses/images/entorno.png'>

