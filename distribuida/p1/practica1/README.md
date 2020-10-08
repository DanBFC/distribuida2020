# Servicio (Nginx con Python 3)

Este archivo contiene la información necesaria para construir las imagenes de docker e iniciar los contenedores

## Contenido de las imagenes

Se tienen imagenes de nginx como servidor http y flask como framekwork para utilizar python para trabajar con páginas web

## Instrucciones para construir la imagen y correr el contenedor

Previamente se requiere tener instalado `Docker CE`.
Abrir una terminal y dirigirse a la carpeta donde ha clonado este repositorio y ejecutar los comandos listados abajo.

### `docker-compose up --build`

Construye las imagenes correspondientes e inicia el contenedor, de esta forma es accesible el servicio definido en `run.py` en `localhost:80`.

## Instrucciones para detener el contenedor luego del primer inicio

Apretar `Ctrl + C` si se está en la aplicación o `docker-compose down` si está en el directorio raíz de la aplicación dentro de su computadora y no está en el prompt de la aplicación.

## Instrucciones para iniciar el contenedor en próximas ocasiones

Se pueden escribir algunos de los siguientes comandos.

### `docker-compose up`

Inicia el contenedor y además muestra un prompt con la salida del arranque del SO sostenido por el contenedor.

### `docker-compose up -d`

Inicia el contenedor pero corre en segundo plano por lo cual no hay ninguna salida visible.

## Instrucciones para cambiar el puerto de acceso a la aplicación

Ubicar la línea que contiene la palabra `ports` en el archivo `docker-compose.yml` y modificar el número a la izquierda de `:` por el puerto deseado, excluyendo claro el puerto `8080` que está siendo utilizado por `flask`  (Ej. `- ports 1080:80`, de esta forma sería accesible el servicio a través de `localhost:1080`), claramente luego volver a ejecutar `docker-compose up`, si estaba el contenedor corriendo entonces antes ejecutar `docker-compose down`.

## Instrucciones para modificar las rutinas que realiza nuestro servicio

Se deberá modificar el archivo `run.py` que está en `flask/src` y por supuesto debería despues volver a ejecutar `docker-compose up --build`.
