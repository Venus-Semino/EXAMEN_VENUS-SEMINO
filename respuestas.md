### 1. Dos diferencias entre una API REST y un servidor GraphQL.
* Una API REST funciona estableciendo todo, es decir el cliente no puede hacer una propuesta que esté fuera de los parámetros que se establecieron, mientras que un servidor GraphQL, las peticiones se pueden hacer en base a lo que el cliente necesite solicitar.
* Otra diferencia es que GraphQL suele utilizar solo un método normalmente, mientras que un API REST puede utilizar los 4 métodos.

### 2. Una situación para usar REST y otra para usar GraphQL.
* REST se puede usar para cuando se tiene datos específicos y la empresa no es tan grande, una empresa pequeña.
* GraphQL se utiliza mayormente en empresas grandes, cuando el usuario solo necesita los datos sin tener que hacer varias peticiones o que le den de más datos de los que necesita.

### 3. Diferencia entre imagen y contenedor, y el papel del Dockerfile.
* Imagen es el entorno, sistema que va a tener el contenedor, mientras que el contenedor es donde va a contener la imagen como el proyecto.
* Dockerfile es un archivo en donde se construye la imagen del contenedor.

### 4. Para qué sirve Docker Compose y qué significa cada 8000 del mapeo.
* Docker Compose sirve como orquestador para ejecutar los distintos programas en los contenedores.
* En 8000:8000, el primer 8000 es el puerto expuesto en mi computadora, y el segundo 8000 es el puerto interno dentro del contenedor donde se ejecuta la aplicación.

### 5. Por qué MySQL y no una lista en memoria, y qué identifica la llave primaria.
* Si se utiliza una lista en memoria, los datos van a quedar en dónde se hizo el proyecto y no van a estar incluidos en el contenedor.
* La llave primaria es un identificador único e irrepetible para cada registro en la tabla.