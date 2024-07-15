# Proyecto final para Codo a Codo 2024

## Repositorio virtual


##### Crear repositorio
* Desde la terminal del VSCode, ejecutar el comando en la terminal bash.

    ```bash
    virtualenv venv
    ```

![alt text](img/image-1.png)

##### Activar el repositorio
* Para activar el repositorio y postetiormente instalar las librerias necesarias, ejecutar el siguiente comando en la terminal bash.

    ```bash
    source venv/Scripts/Activate
    ```

![alt text](img/image-2.png)

Una vez finalizado la creacion del entorno de trabajo y que este activado, continuamos con el repositorio.

### Clonar el repositorio

En la carpeta deseada ejecutar el comando
****
```bash
git clone https://github.com/alegaon/proyecto_final_G4.git
```

### Instalaciones desde Visual Studio Code

- Instalar librerias del proyecto

```bash
pip install -r requirements.txt
```

### Configurar variables de entorno
Para administrar la conexion de la base de datos y preservar la seguridad de la misma. Se debe crear dentro de la estructura del Backend un archivo, el cual administra las credenciales de la conexion a la base de datos PostgreSQL.

```bash
Crear un archivo sin nombre y de extencion *.env, como se muestra en la siguiente imagen.
```

![alt text](img/image-4.png)

Dentro del archivo se deben colocar losiguiente:

```bash
DB_HOST = 127.0.0.1
DB_PORT = 5432
DB_USERNAME = USER_database
DB_PASSWORD = PSW_database
DB_NAME = DB-NAME_database
```

### Correr Backend

Desde la consola, dentro de la carpeta del backend, ejecutar el comando.

```bash
python run.py
```

# Uso de Insomnia

### Importar archivo json

Para cargar los request de prueba, importar en Insomnia el archivo. Seleccionando la opcion Import del menu desplegable.

```bash
Insomnia_2024-07-12.json
```

![alt text](img/image.png)

Seleccionar la opcion Importar. Y cargar el archivo JSON. Luego correr las request POST para cargar al menos 4 datos en la base y poder ejecutar algunos GET, PUT y DELETE.

### Request de Insomnia

Vista de las request. Para poder precargar datos en postgresql, ejecutar los POST. De esta manera ya tendra cuatro registros operativos y funcionales en su base de datos.

Ademas tiene metodos de GET para consultar algunos de los registros, PUT para modificarlos y DEL para realizar borrado lógicos, los cuales se pueden reestablecer posteriormente.

![alt text](img/image-3.png)