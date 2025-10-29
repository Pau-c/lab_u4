### Compilación y ejecución de la aplicación

Cuando esté listo, inicie su aplicación ejecutando:
`docker compose up --build`.

Su aplicación estará disponible en http://localhost:8000.

### Despliegue de la aplicación en la nube

Primero, cree su imagen, por ejemplo: `docker build -t myapp .`.
Si su nube utiliza una arquitectura de CPU diferente a la de su 
máquina de desarrollo (por ejemplo, si usa una Mac M1 y su proveedor 
de nube es amd64), deberá crear la imagen para esa plataforma, por 
ejemplo: `docker build --platform=linux/amd64 -t myapp .`

Luego, súbala a su registro, por ejemplo: `docker push myregistry.com/myapp`.

Consulte la documentación [Introducción a Docker](https://docs.docker.com/go/get-started-sharing/) Documentación para obtener más detalles sobre la compilación y el despliegue.


### Referencias
* [Guía de Python de Docker](https://docs.docker.com/language/python/)