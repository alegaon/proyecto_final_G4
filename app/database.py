import os
import psycopg2
from flask import g
from dotenv import load_dotenv

# Cargo las variables de entorno provenientes del archivo .env
load_dotenv()


# Configuro la base de datos, partiendo de las variables de entorno cargadas en el sistema
DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT'),
}


def test_conn():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()


def create_especies():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS public.especies
        (
            id SERIAL PRIMARY KEY,
            nombre_vulgar character varying(50) NOT NULL,
            nombre_cientifico character varying(50) NOT NULL,
            lugar text[] NOT NULL,
            descripcion text ,
            modalidades text[] ,
            epoca character varying ,
            activo boolean,
            creado timestamp,
            actualizado timestamp
        )
        """
    )
    conn.commit()

    cur.close()
    print('Tabla especies creada')

# Funcion para estableer la conexion a la BD


def get_db():
    # Si 'db' no esta en el contexto global de Flas "g"
    if 'db' not in g:
        # Establezco una nueva conexion a la BD y la guardo en 'g'
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    # Retorno la conexion a la base de datos
    return g.db

# Funcion para cerrar la conexion a la BD


def close_db(e=None):
    # Elimino de "g" la conexion a la BD
    db = g.pop('db', None)
    # Si la conexion existe, la cierro
    if db is not None:
        db.close()

# Funcion para inicializar la aplicacion con el manejo de base de datos


def init_app(app):
    # registro 'close_db' para que se ejecute al final del contexto de la app
    app.teardown_appcontext(close_db)
