# X Simposio de Software Libre y Código Abierto de la Mixteca

Universidad Tecnológica de la Mixteca

10 y 11 de Octubre 2024

## Taller FastAPI - Construcción de API’s con Python

### Contenido del Taller

1. [Introducción](#introducción)

- [Características principales de FastAPI](#características-principales-de-fastapi)
- [Ventajas de FastAPI sobre Flask o Django](#ventajas-de-fastapi-sobre-flask-o-django)
- [Cuándo Elegir FastAPI](#cuándo-elegir-fastapi)

2. [Configuración ambiente de desarrollo](#configuración-ambiente-de-desarrollo)

- [Herramientas a utilizar](#herramientas-a-utilizar)
- [Initial configuration](#initial-configuration)

### Introducción

FastAPI es un framework moderno, rápido (de alto rendimiento), y fácil de usar para construir APIs con Python. Fue diseñado para ayudar a los desarrolladores a crear APIs robustas y escalables de forma rápida y con menos código, aprovechando la sintaxis moderna de Python y características como las anotaciones de tipo.

#### Características principales de FastAPI:

1. **Rendimiento Alto**: Utiliza Starlette y Pydantic, lo cual le permite alcanzar un rendimiento similar a frameworks como Node.js y Go. Está basado en estándares modernos como ASGI (Asynchronous Server Gateway Interface), lo cual lo hace extremadamente rápido y adecuado para sistemas concurrentes.
2. **Automatización y Documentación de APIs**: Una de las características más atractivas de FastAPI es su capacidad de generar automáticamente documentación interactiva y de alta calidad de las APIs. Usa OpenAPI y Swagger para proporcionar documentación interactiva, lo cual permite probar y explorar las funciones sin esfuerzo adicional.
3. **Basado en Tipos de Python**: FastAPI hace uso de las anotaciones de tipos de Python para definir los esquemas y las validaciones de las entradas y respuestas. Esto no solo facilita el desarrollo y la validación de datos, sino que también mejora la experiencia del desarrollador con sugerencias y verificaciones automáticas del tipo de datos.
4. **Asincronismo y Concurrente**: FastAPI es compatible con async y await, lo cual permite crear aplicaciones que manejen muchas peticiones simultáneamente de manera eficiente, ideal para servicios que necesitan alta concurrencia.
5. **Fácil de Usar y Aprender**: Gracias a su diseño intuitivo y su documentación completa, FastAPI es fácil de aprender para desarrolladores que ya están familiarizados con Python. Su curva de aprendizaje es más baja en comparación con otros frameworks, pero a la vez es lo suficientemente robusto para proyectos complejos.

##### Starlette

FastAPI utiliza Starlette como la base de su infraestructura de servidor web debido a sus capacidades asincrónicas y de alto rendimiento. Starlette proporciona a FastAPI muchas de sus características esenciales, tales como el manejo de solicitudes y respuestas HTTP, soporte para WebSockets, middlewares, y la capacidad de definir rutas. Gracias a Starlette, FastAPI hereda la capacidad de manejar múltiples conexiones simultáneas de manera eficiente.

Starlette es un componente esencial para cualquier aplicación moderna basada en Python que requiera alta capacidad de concurrencia y rendimiento. Su diseño modular y ligero permite construir desde aplicaciones web pequeñas hasta servicios complejos, y es la base sobre la que se apoya FastAPI para ofrecer todas sus funcionalidades de forma rápida y eficiente.

##### Casos de Uso:

- Creación de APIs RESTful para microservicios.
- Aplicaciones que necesitan integrar machine learning o procesamiento de datos de alta concurrencia.
- Aplicaciones web modernas que requieren procesamiento en tiempo real.

#### Ventajas de FastAPI sobre Flask o Django

**FastAPI**, **Flask** y **Django** son tres frameworks populares para desarrollar aplicaciones web y APIs con Python, pero tienen diferentes enfoques y características. A continuación, se presentan algunas ventajas que tiene **FastAPI** sobre **Flask** y **Django**:

##### 1. Alto Rendimiento y Asincronismo

**FastAPI** está diseñado para ser _rápido_ y eficiente. Utiliza `async` y `await` para implementar asincronismo, lo cual permite manejar un gran número de solicitudes simultáneas de manera eficiente. **Flask**, aunque puede manejar asincronismo mediante configuraciones adicionales, no está diseñado nativamente para este propósito, y **Django** también requiere bibliotecas adicionales (como `Django Channels`) para lograr una concurrencia similar.

**FastAPI** está basado en **Starlette** y **Pydantic**, lo que le permite alcanzar un rendimiento comparable al de Node.js y Go, haciéndolo ideal para aplicaciones que necesitan alta capacidad de procesamiento concurrente.

##### 2. Validación Automática de Datos y Documentación

**Validación automática de datos**: **FastAPI** utiliza **Pydantic** para la validación de datos basada en anotaciones de tipo, lo cual facilita la validación y el parsing de entradas sin esfuerzo adicional. En **Flask** y **Django**, la validación requiere de más trabajo manual o el uso de bibliotecas externas.

**Generación automática de documentación**: **FastAPI** genera automáticamente documentación interactiva utilizando **OpenAPI** y **Swagger**. Esto significa que, sin esfuerzo adicional, se obtiene una interfaz que permite explorar y probar las APIs. En comparación, en **Flask** y **Django** (con `Django REST Framework`), la documentación debe ser configurada con herramientas adicionales.

##### 3. Simplicidad y Tipos de Python

**Anotaciones de tipo**: **FastAPI** aprovecha al máximo las anotaciones de tipo de Python. Al definir parámetros de entrada y salida utilizando tipos, no solo se mejora la validación de los datos, sino que también se obtienen beneficios como la generación automática de documentación y un mejor soporte para herramientas de desarrollo (como autocompletado en editores de código).

**Flask** y **Django** no aprovechan las anotaciones de tipo de la misma manera, lo cual resulta en un desarrollo menos explícito y más propenso a errores en cuanto a la validación de datos.

##### 4. Fácil de Escalar y Modularidad

**FastAPI** permite una **estructura modular** similar a la de **Django** (usando routers para dividir la lógica de la aplicación), pero sin la complejidad que introduce la configuración inicial de **Django**. Esto facilita la creación de grandes aplicaciones organizadas en diferentes módulos y asegura un crecimiento limpio del proyecto.

En comparación con **Flask**, **FastAPI** proporciona un enfoque más moderno y organizado para manejar múltiples rutas y sub-aplicaciones, lo cual hace que el desarrollo y mantenimiento de proyectos grandes sea más sencillo.

##### 5. Mejor Experiencia del Desarrollador

**Productividad**: Gracias a características como la validación automática de datos y la documentación generada al vuelo, los desarrolladores pueden **iterar más rápidamente** al escribir y probar código. Esto se traduce en mayor productividad y menos errores.

**Herramientas modernas**: **FastAPI** se integra bien con características modernas de Python (como `async`/`await`) y tiene una excelente **experiencia de autocompletado** en editores como VSCode o PyCharm, lo cual facilita mucho el desarrollo. **Flask** y **Django** no se enfocan tanto en mejorar la experiencia del desarrollador a través de tipos y autocompletado.

##### 6. Más Ligero que Django

**Django** es un framework completo de desarrollo web, que incluye herramientas como ORM, sistema de autenticación, administración, entre otros. Esto es ideal para proyectos que necesitan una solución integral para el desarrollo de sitios web. Sin embargo, para APIs ligeras o microservicios, **Django** puede ser más pesado de lo necesario.

**FastAPI** es más **minimalista** y enfocado en la creación de APIs RESTful, lo que lo hace ideal para microservicios, servicios backend, o sistemas donde la ligereza y el rendimiento son esenciales.

##### 7. Soporte para WebSockets

**FastAPI** tiene soporte nativo para manejar **WebSockets**, lo cual es ideal para aplicaciones que necesitan comunicación en tiempo real, como chats o sistemas de notificación. **Flask** y **Django** también pueden manejar **WebSockets**, pero no de forma nativa y requieren bibliotecas adicionales.

##### 8. Menor Configuración para RESTful APIs

Mientras que **Django** puede desarrollar APIs a través de `Django REST Framework (DRF)`, la configuración es más compleja, y requiere un esfuerzo adicional para construir APIs comparado con **FastAPI**. **FastAPI** está diseñado específicamente para APIs RESTful, lo cual simplifica la creación y gestión de endpoints.

##### Comparativa de Uso:

- **Flask**: Ideal para aplicaciones pequeñas o para quienes prefieren un enfoque minimalista y desean un control absoluto sobre el framework. Sin embargo, requiere más esfuerzo manual para implementar cosas como validación de datos y documentación.
- **Django**: Ideal para aplicaciones completas con requerimientos de autenticación, ORM, y un conjunto amplio de herramientas integradas. Es muy útil para aplicaciones web completas, pero es más pesado para aplicaciones ligeras o microservicios.
- **FastAPI**: Enfocado en **APIs modernas**, alto rendimiento y facilidad de uso, con muchas características automáticas que hacen que el desarrollo de APIs sea rápido y efectivo. Es una excelente opción para construir microservicios y aplicaciones donde la validación y el rendimiento son fundamentales.

En resumen, **FastAPI** combina lo mejor del rendimiento, la simplicidad, y la automatización, haciéndolo una opción atractiva sobre **Flask** y **Django** para la creación de APIs rápidas, modernas y bien documentadas, especialmente en proyectos donde la eficiencia y la facilidad de desarrollo son esenciales.

#### Cuándo Elegir FastAPI

Elegir **FastAPI** como framework de desarrollo depende del tipo de aplicación que se desea construir, los requisitos del proyecto y las características propias de **FastAPI**. A continuación, se analizan los escenarios en los que se debería elegir y en los que no se debería elegir **FastAPI**.

##### 1. Necesidad de Altas Prestaciones y Concurrencia

- Si tu aplicación necesita manejar **altas cargas de solicitudes simultáneas**, como un servicio con muchos usuarios concurrentes o una API pública, **FastAPI** es una excelente elección gracias a su capacidad asincrónica y el alto rendimiento que ofrece basado en el estándar ASGI.

##### 2. Creación Rápida de APIs RESTful

- **FastAPI** está optimizado para la **creación de APIs RESTful**. Si tu proyecto consiste en desarrollar una API que interactúe con clientes móviles, aplicaciones web, o microservicios, **FastAPI** simplifica considerablemente la construcción, validación de datos, y documentación.

##### 3. Documentación Automática y Validación de Datos

- Si necesitas una **documentación automática** para tu API (utilizando OpenAPI/Swagger), **FastAPI** es una gran elección, ya que proporciona automáticamente documentación interactiva sin necesidad de configuraciones adicionales.

* **La validación de datos basada en tipos** es una característica clave de **FastAPI**. Si tu proyecto requiere que las entradas del usuario se validen de manera robusta y eficiente, la integración de **Pydantic** facilita mucho este proceso, proporcionando además una experiencia de desarrollo más segura y con menos errores.

##### 4. Proyectos Modernos y Requisitos Asíncronos

Si tu aplicación requiere el uso intensivo de funcionalidades modernas de Python como `async` y `await` para realizar operaciones asincrónicas (por ejemplo, consultas a bases de datos o llamadas a APIs externas), **FastAPI** es ideal, ya que soporta asincronismo de manera nativa.

##### 5. Microservicios y Arquitectura Basada en Servicios

**FastAPI** es una excelente opción para desarrollar **microservicios** dentro de una arquitectura más grande basada en servicios. Gracias a su rendimiento y a la facilidad para crear APIs bien documentadas, se adapta perfectamente a arquitecturas de microservicios.

##### 6. Simplicidad y Rapidez de Desarrollo

Si buscas una **curva de aprendizaje corta** y una **alta productividad** en el desarrollo, **FastAPI** es una excelente opción debido a su simplicidad, excelente documentación y uso de anotaciones de tipo, lo que facilita tanto el desarrollo como el mantenimiento del código.

##### 7. Integración con Machine Learning o IA

Si estás desarrollando servicios que integren modelos de **machine learning** o inteligencia artificial (IA), **FastAPI** se lleva muy bien con estas herramientas, ya que permite integrar fácilmente modelos, definir endpoints para inferencia y manejar respuestas de manera asincrónica.

### Configuración ambiente de desarrollo

#### Herramientas a utilizar

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Desktop](https://docs.docker.com/desktop/)

#### Initial configuration

1. Crear carpeta `backend`
2. Crear archivo `requirements.txt`, dentro de carpeta `backend`.

   El archivo `requirements.txt` en un proyecto de Python se utiliza para listar las dependencias del proyecto, es decir, los paquetes y bibliotecas necesarios para que el código funcione correctamente.

```
alembic
email-validator
fastapi==0.115.0
passlib[bcrypt]
psycopg2-binary
pydantic
pyjwt
python-multipart
sqlalchemy
uvicorn[standard]
```

- **alembic**:
  Alembic es una herramienta de migración de bases de datos para SQLAlchemy. Permite gestionar y aplicar cambios en la estructura de la base de datos (como crear, modificar o eliminar tablas y columnas) de manera controlada y versionada, facilitando la evolución de la base de datos junto con el código.

- **email-validator**:
  Este paquete se utiliza para validar direcciones de correo electrónico. Verifica que las direcciones de correo proporcionadas tengan un formato válido según los estándares y, opcionalmente, puede hacer verificaciones más avanzadas como consultar si el dominio del correo existe.
- **fastapi**:
  FastAPI es un framework moderno y de alto rendimiento para crear APIs web en Python. Es compatible con Python 3.7+ y está diseñado para ser fácil de usar y eficiente, con soporte integrado para validación de datos y generación automática de documentación. La versión especificada es la 0.115.0.
- **passlib**:
  Passlib es una biblioteca para manejar contraseñas de manera segura. Proporciona funciones para generar hashes seguros de contraseñas y para verificar contraseñas de manera que se protejan contra ataques como el hash cracking. Es común usarla cuando se necesitan almacenar contraseñas en bases de datos de forma segura.
- **psycopg2-binary**:
  Psycopg2 es el adaptador de PostgreSQL más popular para Python. psycopg2-binary es una versión que viene con binarios precompilados, lo que facilita su instalación sin necesidad de compilarlo. Se utiliza para interactuar con bases de datos PostgreSQL desde Python, permitiendo ejecutar consultas y operaciones sobre la base de datos.
- **pydantic**:
  Pydantic es una biblioteca para la validación de datos y la gestión de tipos en Python. FastAPI la utiliza para garantizar que los datos recibidos en las solicitudes (por ejemplo, en un API) tengan el formato y los tipos correctos. Pydantic asegura que los datos sean consistentes y proporciona mecanismos para manejar errores de validación.
- **sqlalchemy**:
  SQLAlchemy es un ORM (Object-Relational Mapping) que permite interactuar con bases de datos SQL de manera más sencilla, utilizando objetos Python en lugar de escribir consultas SQL directamente. Facilita la manipulación de datos en la base de datos de una manera orientada a objetos y permite construir y ejecutar consultas SQL de manera programática.
- **uvicorn**:
  Uvicorn es un servidor ASGI (Asynchronous Server Gateway Interface) ligero y rápido para Python. Es el servidor recomendado para correr aplicaciones hechas con FastAPI. El [standard] indica que se instalarán dependencias adicionales necesarias para el rendimiento y soporte completo de características estándar como WebSockets, HTTP/2 y mejoras de rendimiento.

3. Crear archivo `Dockerfile`, dentro de carpeta `backend`.

Este archivo Dockerfile es una receta que define cómo crear una imagen de Docker para una aplicación basada en FastAPI.

```
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

- `FROM python:3.11-slim`:
  Esta línea especifica la imagen base que se utilizará para construir la imagen de Docker. En este caso, se está utilizando una imagen oficial de Python versión 3.11 en su variante "slim" (una versión más ligera y optimizada en cuanto a tamaño). Esto permite ejecutar programas en Python 3.11 en el contenedor.
- `WORKDIR /app`:
  Define el directorio de trabajo dentro del contenedor, es decir, el lugar donde las siguientes instrucciones se ejecutarán. En este caso, se establece el directorio `/app`. Si el directorio no existe, Docker lo crea automáticamente. Este será el directorio donde se colocarán los archivos de la aplicación.
- `COPY requirements.txt .`:
  Esta instrucción copia el archivo `requirements.txt` desde el directorio local (de la máquina donde se está construyendo la imagen) al directorio de trabajo (/app) en el contenedor de Docker. El punto (.) al final indica el directorio actual en el contenedor.
- `RUN pip install --no-cache-dir -r requirements.txt`:
  Esta línea ejecuta un comando dentro del contenedor, específicamente, instala las dependencias listadas en el archivo `requirements.txt` usando `pip`. La opción `--no-cache-dir` se utiliza para evitar que `pip` almacene en caché los archivos descargados, lo que reduce el tamaño de la imagen final. Al instalar las dependencias dentro del contenedor, este ya tendrá todas las bibliotecas necesarias cuando la aplicación se ejecute.
- `COPY . .`:
  Copia todo el contenido del directorio actual de tu máquina (donde está el Dockerfile) al directorio `/app` dentro del contenedor. Esto incluye todo el código fuente de la aplicación. El primer `.` se refiere a tu directorio local y el segundo `.` al directorio de trabajo dentro del contenedor (`/app`).
- `CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]`:
  Esta es la instrucción que define el comando predeterminado que se ejecutará cuando el contenedor inicie. En este caso, se está utilizando Uvicorn para ejecutar la aplicación FastAPI.

  - `uvicorn`: Es el servidor ASGI que ejecutará la aplicación.
  - `app.main:app`: Especifica el punto de entrada de la aplicación FastAPI. Aquí, app.main se refiere al archivo main.py dentro de la carpeta app, y app es la instancia de FastAPI dentro de ese archivo.
  - `--host 0.0.0.0`: Esto permite que la aplicación sea accesible desde cualquier red (no solo desde localhost), lo que es necesario para que funcione dentro de Docker.
  - `--port 8000`: Define el puerto en el que la aplicación escuchará dentro del contenedor. En este caso, será el puerto 8000.
  - `--reload`: Activa el "modo de recarga automática", lo que significa que Uvicorn volverá a cargar la aplicación si detecta cambios en los archivos del código fuente. Esto es útil para desarrollo, pero generalmente no se usa en producción.

4. Crear archivo `.dockerignore`

El archivo .dockerignore es un archivo de configuración utilizado en proyectos que contienen un Dockerfile. Su principal objetivo es especificar qué archivos y directorios deben ser ignorados al construir una imagen de Docker. Funciona de manera similar a .gitignore en Git, donde defines una lista de archivos o carpetas que no deben ser incluidos en el proceso de construcción de la imagen.

```
# Ignorar archivos y directorios innecesarios
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
*.env

# Ignorar archivos de versiones y sistemas de control
.git/
.gitignore
Dockerfile
docker-compose.yml
```

5. Crear archivo `docker-compose.yml`

   Este archivo docker-compose.yml define los servicios que forman parte de una aplicación, en este caso una aplicación web que usa FastAPI y una base de datos PostgreSQL.

```
services:
  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydatabase
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U myuser -d mydatabase"]
      interval: 10s
      timeout: 5s
      retries: 5

  fastapi:
    build:
      context: backend
    ports:
      - "8000:8000"
    depends_on:
      db:
         condition: service_healthy
    environment:
      DATABASE_URL: postgresql://myuser:mypassword@db:5432/mydatabase
    volumes:
      - ./backend:/app

volumes:
  postgres_data:
```

- **services**:
  Esta sección define los servicios que Docker Compose va a orquestar. En este caso, los servicios son `db` (PostgreSQL) y `fastapi` (el backend de la aplicación web).

  - **db**:

    - `image: postgres`
      Se utiliza la última imagen oficial de PostgreSQL disponible en Docker Hub.
    - `environment`:
      Aquí se establecen las variables de entorno necesarias para que PostgreSQL funcione. Se definen:
      - `POSTGRES_USER`: El nombre de usuario de la base de datos.
      - `POSTGRES_PASSWORD`: La contraseña del usuario.
      - `POSTGRES_DB`: El nombre de la base de datos que se creará automáticamente al iniciar el servicio.
    - `volumes`:
      Monta un volumen llamado `postgres_data` en el directorio `/var/lib/postgresql/data` dentro del contenedor, que es donde PostgreSQL almacena sus datos. Esto asegura que los datos persistan incluso si el contenedor se elimina o reinicia.
    - `ports`:
      Mapea el puerto `5432` del contenedor al puerto `5432` del host, lo que significa que puedes conectarte a PostgreSQL desde tu máquina en `localhost:5432`.
    - `healthcheck`:
      Verifica el estado del servicio PostgreSQL con el comando `pg_isready`, que comprueba si la base de datos está lista para aceptar conexiones.
      - `test`: Ejecuta el comando para verificar la salud de la base de datos.
      - `interval`: La salud del servicio se verifica cada 10 segundos.
      - `timeout`: El test fallará si no recibe respuesta en 5 segundos.
      - `retries`: Si el test falla 5 veces consecutivas, el servicio se marcará como no saludable.

  - **fastapi**:
    - `build`:
      El servicio fastapi se construye utilizando un Dockerfile que se encuentra en el directorio backend. El contexto de construcción (context) se refiere a ese directorio.
    - `ports`:
      Mapea el puerto `8000` del contenedor al puerto `8000` del host, lo que significa que puedes acceder a la aplicación FastAPI en localhost:`8000`.
    - `depends_on`:
      Este servicio depende del servicio db (PostgreSQL). Aquí se especifica que `fastapi` solo se iniciará cuando el servicio `db` esté saludable, utilizando la condición `service_healthy`.
    - `environment`:
      Define la variable de entorno DATABASE_URL, que FastAPI utiliza para conectarse a la base de datos PostgreSQL. La URL de conexión incluye el usuario, la contraseña, el nombre de la base de datos y la dirección del servicio db (en este caso, el hostname es db, que se refiere al nombre del servicio PostgreSQL dentro de la red interna de Docker Compose).
    - `volumes`:
      Monta el directorio local ./backend en el contenedor, en la ruta /app. Esto permite que cualquier cambio que hagas en el código fuente de backend en tu máquina local se refleje automáticamente dentro del contenedor, lo cual es útil para el desarrollo.

6. Crear carpeta `app` dentro de `backend`
7. Crear archivo vacío `__init__.py` dentro de carpeta `app`
8. Crear archivo `main.py` dentro de carpeta `app`

```
from fastapi import FastAPI

app = FastAPI()
```

- `from fastapi import FastAPI`:
  - Esta línea importa la clase `FastAPI` desde el paquete `fastapi`.
  - La clase `FastAPI` es la pieza central del framework, y contiene todas las funcionalidades que necesitas para crear una aplicación, gestionar rutas (endpoints), manejar solicitudes y respuestas HTTP, entre otras cosas.
- `app = FastAPI()`:
  - Aquí se está creando una instancia de la clase `FastAPI` y asignando a la variable `app`.
  - Esta instancia (`app`) representa la aplicación que vas a construir. Es la base donde definirás las rutas (endpoints), la lógica de negocio, y configuraciones adicionales.
  - La instancia de `FastAPI` es la que orquesta cómo se deben manejar las solicitudes HTTP que reciba tu aplicación, desde rutas simples como `GET /` hasta operaciones más complejas.

9. Inicia la composición de contenedores Docker

```
docker compose up
```

10. Open http://localhost:8000/docs

### Initial concepts

#### main.py

**Importar FastAPI**: La línea `from fastapi import FastAPI` importa la clase FastAPI que se usará para crear la aplicación.

**Crear una Instancia de FastAPI**: `app = FastAPI()` inicializa la aplicación FastAPI.

#### Definir un Endpoint

Un **endpoint** es un punto específico de acceso dentro de una API (Interfaz de Programación de Aplicaciones) que permite a los clientes (como navegadores web o aplicaciones móviles) interactuar con el servidor. Es una **URL única** a la cual se puede realizar una solicitud para ejecutar una operación específica, como obtener datos, enviar datos, actualizar información o eliminarla.

En el contexto de una API, los endpoints representan las **diferentes funcionalidades** disponibles y están relacionados con una **ruta (URL)** y un **método HTTP**. Los métodos HTTP más comunes son:

- **GET**: Recupera datos del servidor.
- **POST**: Envía datos al servidor para crear algo nuevo.
- **PUT**: Actualiza datos existentes en el servidor.
- **DELETE**: Elimina datos en el servidor.

Continuando con el ejemplo agreguemos lo siguiente a nuestro archivo `main.py`

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"mensaje": "Hola Mundo"}
```

- **Ruta**: `/` es la URL que define el endpoint.
- **Método HTTP**: `GET`, especificado por el decorador `@app.get("/")`.
- **Funcionalidad**: La función `read_root()` maneja las solicitudes GET y devuelve el mensaje `{"mensaje": "Hola Mundo"}`.

#### Estrutura del proyecto

Hay libertad de estructurar el proyecto, pero para este curso usaremos esta forma.

```
/app
│
├── models
|   ├── __init__.py
│   └── user.py
├── routers
|   ├── __init__.py
│   └── users.py
├── schemas
|   ├── __init__.py
│   └── user.py
├── __init__.py
├── database.py
└── main.py
```

- `main.py`
  Este archivo es generalmente el punto de entrada de la aplicación. Aquí es donde normalmente se encuentra la instancia de FastAPI y donde se incluyen las rutas (routers) que importan las diferentes funcionalidades de la aplicación.
- `database.py`
  Aquí se gestiona la configuración de la base de datos. Suele contener la configuración de conexión a la base de datos (por ejemplo, usando SQLAlchemy o cualquier ORM).

  También es común ver la creación del motor de la base de datos (engine) y la sesión.

- `/models`
  Este directorio contiene las definiciones de modelos que representan las tablas en la base de datos, generalmente usando un ORM como SQLAlchemy.
- `/routers`
  Este directorio contiene los routers, que son módulos donde se agrupan las rutas o endpoints de la aplicación. Estos routers permiten que las rutas estén organizadas por funcionalidad, lo que ayuda a mantener el código ordenado y más fácil de escalar.
- `/schemas`
  Este directorio contiene los esquemas que definen la forma de los datos que se envían o reciben a través de las rutas de la API. Los esquemas son generalmente modelos de datos que validan las solicitudes y respuestas utilizando Pydantic.
- Archivos `__init__.py` permiten que cada directorio se trate como un paquete, facilitando la importación de módulos desde otros lugares del proyecto.

### Conectandose a Base de datos (PosgreSQL)

Archivo `database.py`

```
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
```

- `DATABASE_URL = os.environ.get("DATABASE_URL")`
  Aquí se obtiene el valor de la variable de entorno DATABASE_URL, que contiene la URL de conexión a la base de datos. Esta URL normalmente incluye el tipo de base de datos (por ejemplo, PostgreSQL o MySQL), el usuario, la contraseña, el host, el puerto y el nombre de la base de datos.

- `engine = create_engine(DATABASE_URL)`
  Se crea el motor de conexión a la base de datos usando la URL obtenida en la variable DATABASE_URL. El motor (engine) se encarga de gestionar la conexión y realizar las operaciones necesarias sobre la base de datos.

- `SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)`
  Aquí se configura el creador de sesiones con sessionmaker. Se utilizan algunos parámetros clave:

  - `autocommit=False`: Se desactiva el modo autocommit. Esto significa que los cambios en la base de datos no se aplicarán automáticamente después de cada operación. Tendrás que hacer `commit()` manualmente.
    `autoflush=False`: Se desactiva el autoflush, lo que evita que los cambios en la sesión se escriban automáticamente en la base de datos antes de hacer consultas. Esto permite un mejor control sobre cuándo se aplican los cambios.
    `bind=engine`: Se asocia este creador de sesiones al motor de la base de datos previamente creado (engine), de manera que todas las sesiones que se creen utilizarán esa conexión.

- `def get_db()`:
  Esta función es un generador que se utiliza para obtener una sesión de la base de datos cuando sea necesario. FastAPI, por ejemplo, usa esta función con `Depends()` para inyectar la sesión en las rutas.
  - `db = SessionLocal()`: Se crea una nueva instancia de sesión para interactuar con la base de datos.
  - `try: ... finally:`: Se utiliza un bloque try-finally para asegurarse de que la sesión siempre se cierre correctamente después de su uso, incluso si ocurre un error. El cierre de la sesión libera los recursos asociados a la conexión con la base de datos.
  - `yield db`: Entrega la sesión al código que la solicite.
  - `db.close()`: Cierra la sesión cuando se termina su uso.

Archivo `models/user.py`

```
from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
```

- `class User(Base):`:
  Se define la clase User, que representa la tabla users en la base de datos. Esta clase hereda de Base, lo que permite que SQLAlchemy la trate como un modelo de tabla.
- `__tablename__ = "users"`:
  Aquí se especifica explícitamente el nombre de la tabla en la base de datos, que será `users`. Esto le indica a SQLAlchemy que esta clase está asociada a una tabla llamada `users`.
  Si no especificas el nombre de la tabla, SQLAlchemy intentaría crear una tabla con el nombre de la clase en minúsculas (en este caso, `user`), pero con esta declaración se asegura que el nombre sea `users`.
- `id = Column(Integer, primary_key=True)`:
  - Define una columna llamada `id`, que será un entero (`Integer`).
  - `primary_key=True` indica que esta columna es la clave primaria de la tabla, lo que significa que su valor será único para cada fila y se utilizará para identificar cada registro.
- `username = Column(String, unique=True, index=True)`:
  - Define una columna llamada `username`, que será de tipo cadena de texto (`String`).
    - `unique=True`: Esto garantiza que no haya dos usuarios con el mismo nombre de usuario en la tabla. Los valores de esta columna deben ser únicos.
    - `index=True`: Se crea un índice en esta columna para acelerar las búsquedas que la incluyan, como cuando se busca un usuario por su nombre de usuario.
  - `email = Column(String, unique=True, index=True)`:
    - Similar a la columna `username`, se define una columna email de tipo cadena de texto (`String`).
    - Única e indexada.
  - `password = Column(String)`:
    - Define una columna llamada `password` de tipo cadena de texto (`String`). Esta columna almacenará la contraseña del usuario.
    - No tiene restricciones adicionales como unique o index, ya que no es necesario que las contraseñas sean únicas o se indexen.

#### Inicializar Base de datos usando alembic `alembic`

1. Ejecutar `docker ps` y localizar el nombre del contenedor, por ejemplo: `fastapi-taller-x_sslcam-fastapi-1`
2. Ejecutar en modo interactivo en el contenedor de fastapi el comando bash:

```
docker exec -it fastapi-taller-x_sslcam-fastapi-1 bash
```

3. Inicializar alembic

```
alembic init alembic
```

4. Abre el archivo `alembic.ini` y configura la conexión a tu base de datos en la sección `[alembic]`. Busca la línea que comienza con `sqlalchemy.url` y comentalo. Por ejemplo:

```
# sqlalchemy.url = driver://user:pass@localhost/dbname
```

5. Busca el archivo `env.py` e importa la url de la base de datos y el Base de `app.database`:

```
from app.database import DATABASE_URL, Base
```

6. Buca la línea `config = context.config` y agrega debajo lo siguiente:

```
config.set_main_option("sqlalchemy.url", DATABASE_URL)
```

7. Busca `target_metadata = None` y sustituyelo por el metada de `Base`:

```
target_metadata = Base.metadata
```

8. Importa el modelo `User` que definimos en `app.models.user`:

```
from app.models.user import User  # noqa: F401
```

9. Autogenera la revisión para la tabla de usuarios:

```
alembic revision --autogenerate -m "User table"
```

10. Revisar que en la carpeta `alembic/versions` se haya creado un archivo con dos métodos

    - `upgrade` crea la tabla usuarios
    - `downgrade` borra la tabla usuarios

11. Correr la migración

```
alembic upgrade head
```

#### Guardando en base de datos

Archivo `schemas/user.py`

```
from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserDetail(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(
        from_attributes=True
    )
```

- `class UserCreate(BaseModel):`:
  Esta clase representa el esquema de datos que se utilizará para crear un nuevo usuario. Es decir, los datos que se esperan cuando se crea un usuario nuevo.
  Esta clase se usará para validar que cuando un cliente envía datos para crear un usuario, se provean los tres campos obligatorios (username, email, password) y que el formato del correo electrónico sea correcto.
  - `username: str`: Define que el campo `username` es obligatorio y debe ser de tipo cadena de texto (`str`).
  - `email: EmailStr`: Define que el campo `email` es obligatorio y debe ser de tipo `EmailStr`, lo que asegura que Pydantic validará que el valor sea un correo electrónico válido.
  - `password: str`: Define que el campo `password` es obligatorio y debe ser de tipo cadena de texto (`str`).
- `class UserDetail(BaseModel):`:
  Esta clase representa el esquema de datos que se utilizará para detallar o devolver información de un usuario.
  - `id: int`: Define que el campo `id` es obligatorio y debe ser de tipo entero (`int`). Normalmente, este campo representa el identificador único de un usuario en la base de datos.
  - `username: str`: Define que el campo `username` es obligatorio y debe ser de tipo cadena de texto (`str`).
  - `email: EmailStr`: Define que el campo `email` es obligatorio y debe ser de tipo `EmailStr`, asegurando que sea un correo electrónico válido.

Archivo `routers/users.py`

```
from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session


from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserDetail

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()


@router.post("/users/", response_model=UserDetail)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    db_user = db.query(User).filter(
        User.username == user.username
    ).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    # Crear un nuevo usuario
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username, email=user.email,
                    password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```

- `pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")`: Configuración del contexto de hashing de contraseñas
- `router = APIRouter()`:
  Se crea una instancia de `APIRouter`, que actuará como un "mini-enrutador" para definir rutas relacionadas con los usuarios. Esto permite modularizar la aplicación y organizar las rutas por funcionalidad.
- Definición de la ruta para crear un usuario
  ```
  @router.post("/users/", response_model=UserDetail)
  def create_user(user: UserCreate, db: Session = Depends(get_db)):
  ```
  - `@router.post("/users/")`: Define una ruta HTTP `POST` en `/users/`, lo que indica que este endpoint será utilizado para crear un nuevo usuario.
  - `response_model=UserDetail`: Esto indica que la respuesta de esta ruta debe seguir el formato definido en el esquema `UserDetail`, es decir, se devolverá el `id`, `username` y `email` del usuario creado.
  - `user: UserCreate`: Este es el cuerpo de la solicitud (el payload). Se espera que los datos recibidos sigan el formato definido en el esquema `UserCreate` (con `username`, `email` y `password`).
  - `db: Session = Depends(get_db)`: Se inyecta una sesión de la base de datos utilizando la dependencia `get_db`

Agrega dentro de main el router de users

```
from fastapi import FastAPI

from app.routers import users

app = FastAPI()
app.include_router(users.router)


@app.get("/")
async def read_root():
    return {"mensaje": "Hola Mundo"}
```

- `from app.routers import users`:
  Esta línea importa un router que está definido en un módulo llamado `users` dentro del directorio `app.routers`.
  Los routers en FastAPI se utilizan para **modularizar** y **organizar** las rutas o endpoints de la aplicación. En este caso, se asume que el archivo `users.py` contiene un router con las rutas relacionadas a la funcionalidad de usuarios.

- `app.include_router(users.router)`:
  Esta línea incluye el router `users.router` en la aplicación principal.
  - `include_router()`: Es un método de FastAPI que permite agregar un conjunto de rutas definidas en un router a la aplicación principal. Esto permite **modularizar** las rutas por funcionalidades o áreas de la aplicación (en este caso, las rutas relacionadas con los usuarios están definidas en `users.router`).
  - `users.router`: Se refiere al router que se ha definido en el archivo `users.py` del módulo `app.routers`. Probablemente, este router contiene rutas como `/users/` para operaciones de usuarios (por ejemplo, creación de usuarios, actualización, etc.).

#### Leyendo de base de datos
