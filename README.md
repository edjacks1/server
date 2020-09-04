## Pasos para ejecutar el proyecto


### 1. Entorno virtual

Situate en la raiz del proyecto.

El entorno virtual se situa fuera del proyecto. De tal manera que:

- proyecto
    - Carpetas
    - ...
    - README.md
    - requirements.txt
- venv

Crea el entorno virual fuera de la raiz:

`python3 -m venv ../venv`

Ahora se activa:

`source ../venv/bin/activate`

Una vez activado el entorno virtual, se instalan los requerimientos del sistema:

`pip install -r requirements.txt`

### 2. Antes de correr el proyecto, es necesario crear una base de datos en postgres

Para esto tienes que estar asegurado de tener postgres instalado en tu sistema.

Aqui puedes encontrar las instrucciones para los distintos sistemas operativos:
- https://www.postgresql.org/download/

Una vez instalado, ejecuta los siguientes comandos en la terminal para acceder a postgres:

`sudo su - postgres`

`psql`

Para crear la base de datos:

`CREATE DATABASE iieg2;`

Esto sera suficiente para que la configuracion del proyecto haga las migraciones de nuestra base de datos.

### 3. Inicializar el proyecto

Ahora toca inicializar la base de datos y correr las migraciones.

Nos movemos a la carpeta de la base de datos del proyecto:

`cd Database`

Ejecutamos los comandos que nos permiten crear la estructura en la db.

`python init.py db init`

`python init.py db migrate`

`python init.py db upgrade`

### 4. Correr el proyecto

Nos movemos a la carpeta de rutas:

`cd Router`

Corremos finalmente el proyecto:

`python routs.py`

### 5. Alimentar con datos

Para ingresar los datos, unicamente es necesario ingresar el archivo .csv de los accidentes automovilisticos por medio de la ruta /home. Los datos se insertan automaticamente.
