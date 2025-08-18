## ejemplo de pipeline utilizando python y github


Una canalización o pipeline es una serie de etapas automatizadas que un desarrollador de software utiliza para entregar código nuevo. Este proceso, a menudo llamado Integración Continua/Despliegue Continuo (CI/CD), garantiza que el código sea probado, construido y desplegado de manera eficiente y confiable. 🤖

Ejemplo de Pipeline con Python y GitHub Actions
A continuación, te muestro un ejemplo sencillo de cómo configurar una pipeline CI/CD en un proyecto de Python usando GitHub Actions. Este pipeline se activará automáticamente cada vez que se haga un push o una pull request a la rama main.

1. Requisitos
Antes de empezar, necesitarás:

Un repositorio en GitHub.

Un proyecto de Python en ese repositorio.

Un archivo de requisitos (requirements.txt).

Algún test unitario, por ejemplo, usando la biblioteca unittest o pytest.

2. Estructura del proyecto
La estructura de tu proyecto de Python debería ser similar a esta:
```
mi_proyecto_python/
├── .github/
│   └── workflows/
│       └── python_ci.yml  # Aquí va el archivo de la pipeline
├── mi_app/
│   └── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```
3. Configuración de la Pipeline (Archivo python_ci.yml)
Crea el archivo .github/workflows/python_ci.yml y añade el siguiente código. Este archivo define la lógica del pipeline.

YAML
```
name: Python CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest tests/
```
4. Explicación de las Etapas
El archivo YAML se lee de la siguiente manera:

name: El nombre de tu pipeline, que aparecerá en la interfaz de GitHub Actions.

on: Define los eventos que activarán el pipeline. En este caso, un push o una pull_request a la rama main.

jobs: Un pipeline puede tener múltiples trabajos o jobs. Aquí solo tenemos uno llamado build.

runs-on: Indica el entorno en el que se ejecutará el trabajo. ubuntu-latest es una máquina virtual de Ubuntu.

steps: La lista de acciones a realizar, en orden.

actions/checkout@v3: Descarga el código de tu repositorio en la máquina virtual.

actions/setup-python@v4: Configura la versión de Python que vas a usar, en este caso, la 3.10.

Install dependencies: Instala las librerías necesarias del archivo requirements.txt.

Run tests: Ejecuta los tests unitarios. Aquí se asume que usas pytest y que tus tests están en el directorio tests/.

5. ¿Cómo funciona?
Haces cambios en tu código y los subes a GitHub con un git push.

GitHub detecta el push a la rama main.

GitHub Actions lee el archivo python_ci.yml y empieza a ejecutar el pipeline.

Cada step se ejecuta en la máquina virtual. Si un step falla (por ejemplo, si un test no pasa), el pipeline se detiene y te notifica.

Si todos los steps se ejecutan correctamente, la pipeline pasa con éxito, lo que te da la confianza de que tus cambios no han roto ninguna funcionalidad existente.

## ejemplo de main.py y test_main.py

Un pipeline es una serie de etapas automatizadas que un desarrollador de software utiliza para entregar código nuevo. Este proceso, a menudo llamado Integración Continua/Despliegue Continuo (CI/CD), garantiza que el código sea probado, construido y desplegado de manera eficiente y confiable. 🤖

Ejemplo de Pipeline con Python y GitHub Actions
A continuación, te muestro un ejemplo sencillo de cómo configurar una pipeline CI/CD en un proyecto de Python usando GitHub Actions. Este pipeline se activará automáticamente cada vez que se haga un push o una pull request a la rama main.

1. Requisitos
Antes de empezar, necesitarás:

Un repositorio en GitHub.

Un proyecto de Python en ese repositorio.

Un archivo de requisitos (requirements.txt).

Algún test unitario, por ejemplo, usando la biblioteca unittest o pytest.

2. Estructura del proyecto
La estructura de tu proyecto de Python debería ser similar a esta:
```
mi_proyecto_python/
├── .github/
│   └── workflows/
│       └── python_ci.yml  # Aquí va el archivo de la pipeline
├── mi_app/
│   └── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```
3. Configuración de la Pipeline (Archivo python_ci.yml)
Crea el archivo .github/workflows/python_ci.yml y añade el siguiente código. Este archivo define la lógica del pipeline.

YAML
```
name: Python CI Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest tests/
```
4. Explicación de las Etapas
El archivo YAML se lee de la siguiente manera:

name: El nombre de tu pipeline, que aparecerá en la interfaz de GitHub Actions.

on: Define los eventos que activarán el pipeline. En este caso, un push o una pull_request a la rama main.

jobs: Un pipeline puede tener múltiples trabajos o jobs. Aquí solo tenemos uno llamado build.

runs-on: Indica el entorno en el que se ejecutará el trabajo. ubuntu-latest es una máquina virtual de Ubuntu.

steps: La lista de acciones a realizar, en orden.

actions/checkout@v3: Descarga el código de tu repositorio en la máquina virtual.

actions/setup-python@v4: Configura la versión de Python que vas a usar, en este caso, la 3.10.

Install dependencies: Instala las librerías necesarias del archivo requirements.txt.

Run tests: Ejecuta los tests unitarios. Aquí se asume que usas pytest y que tus tests están en el directorio tests/.

5. ¿Cómo funciona?
Haces cambios en tu código y los subes a GitHub con un git push.

GitHub detecta el push a la rama main.

GitHub Actions lee el archivo python_ci.yml y empieza a ejecutar el pipeline.

Cada step se ejecuta en la máquina virtual. Si un step falla (por ejemplo, si un test no pasa), el pipeline se detiene y te notifica.

Si todos los steps se ejecutan correctamente, la pipeline pasa con éxito, lo que te da la confianza de que tus cambios no han roto ninguna funcionalidad existente.

Ejemplo de main.py y test_main.py
Para que el pipeline funcione, necesitas tener código para probar. A continuación, tienes un ejemplo de un archivo main.py con una función simple y su correspondiente archivo de prueba test_main.py usando la biblioteca pytest.

main.py
Guarda este archivo en el directorio mi_app/.

Python
```
# mi_app/main.py

def sumar(a, b):
    """
    Esta función suma dos números.
    """
    return a + b

def restar(a, b):
    """
    Esta función resta dos números.
    """
    return a - b
```
test_main.py
Guarda este archivo en el directorio tests/.

Python
```
# tests/test_main.py

from mi_app.main import sumar, restar

def test_sumar_numeros_positivos():
    """
    Prueba que la función sumar funciona con números positivos.
    """
    assert sumar(2, 3) == 5

def test_sumar_numeros_negativos():
    """
    Prueba que la función sumar funciona con números negativos.
    """
    assert sumar(-1, -1) == -2

def test_restar():
    """
    Prueba que la función restar funciona correctamente.
    """
    assert restar(5, 2) == 3
    assert restar(10, 5) == 5

def test_restar_resultado_negativo():
    """
    Prueba que la función restar funciona con resultados negativos.
    """
    assert restar(2, 5) == -3
```
¿Qué hace este ejemplo?
El archivo main.py contiene dos funciones básicas: sumar y restar.

El archivo test_main.py contiene varias funciones de prueba que verifican el comportamiento de las funciones de main.py usando assert.

Cuando el pipeline de GitHub Actions llega a la etapa Run tests, ejecutará pytest tests/, que a su vez encontrará y ejecutará las funciones de prueba en test_main.py. Si todas las aserciones (assert) son verdaderas, la prueba pasa. Si alguna falla, el pipeline también falla.

Este flujo de trabajo simple asegura que cada vez que subes cambios a tu código, se comprueba automáticamente que las funciones principales de tu aplicación sigan funcionando como se espera.

## Ejemplo de requirements.txt para este ejercicio


Claro, para el ejemplo de pipeline que hemos visto, solo necesitas instalar la biblioteca pytest para poder ejecutar los tests.

requirements.txt
Crea este archivo en la raíz de tu proyecto con el siguiente contenido:

pytest
¿Qué hace este archivo?
El archivo requirements.txt es un estándar en proyectos de Python para listar las dependencias del proyecto. En el ejemplo del pipeline, la etapa Install dependencies ejecuta el siguiente comando:

pip install -r requirements.txt
Este comando le dice a pip que instale todas las bibliotecas que se encuentran listadas en el archivo requirements.txt. En este caso, instalará pytest, permitiendo que el siguiente paso del pipeline (pytest tests/) se ejecute sin problemas.


## como crear el archivo __init__.py


Un archivo __init__.py es una parte fundamental de los paquetes de Python. Su función principal es decirle a Python que un directorio que lo contiene debe ser tratado como un paquete o subpaquete.

En el contexto de tu proyecto, necesitarás este archivo en la carpeta mi_app/ para que los tests en tests/test_main.py puedan importar el código de mi_app/main.py. Sin él, Python no sabría cómo resolver la importación from mi_app.main import sumar, restar.

¿Cómo crearlo?
Simplemente crea un archivo vacío llamado __init__.py dentro del directorio mi_app/.
```
mi_proyecto_python/
├── .github/
│   └── workflows/
│       └── python_ci.yml
├── mi_app/
│   ├── __init__.py  # ¡Aquí está!
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md
```
Contenido del archivo
En muchos casos, el archivo __init__.py puede estar completamente vacío. Solo su presencia es suficiente para que Python lo reconozca como un paquete.

Sin embargo, también puedes usarlo para:

Inicializar el paquete: Puedes ejecutar código de inicialización cuando el paquete es importado.

Exponer funciones o clases: Puedes importar funciones o clases de otros módulos dentro del paquete para que sean accesibles directamente desde el paquete principal. Por ejemplo, en __init__.py podrías poner:

Python
```
# mi_app/__init__.py
from .main import sumar, restar
```
Con este cambio, podrías importar las funciones de forma más corta en test_main.py:

Python
```
# tests/test_main.py
from mi_app import sumar, restar
```
Para el ejemplo del pipeline, no necesitas agregar ningún contenido. Simplemente crear el archivo vacío en el lugar correcto es suficiente para que las importaciones funcionen y tu pipeline corra con éxito.
