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

## Instrucciones de uso:

Una vez ejecutado el comando `docker-compose up -d` debe ingresar en el navegador a la url [http://localhost:80/](http://localhost:80/).

Existe ya un usuario por default, para poder ingresar con este usuario los datos son los siguientes:

- `username: user`
- `password: password`

En caso que no se quiera acceder con el usuario default dar click en Registrar y llenar el formulario

## Integrantes:

- Enrique Francisco Soto Astorga No. Cuenta: 409009624

- Daniel Beltrán Hernández No. Cuenta: 310030067
