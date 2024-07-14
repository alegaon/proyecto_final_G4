from app.database import get_db
import datetime


"""
nombre_vulgar, nombre_cientifico, lugar, descripcion, modalidades, epoca
"""


class Especies():
    def __init__(self, id=None, nombre_vulgar=None, nombre_cientifico=None, lugar=[], descripcion=None, modalidades=[], epoca=False, activo=True,
                 creado=datetime.datetime.now(), actualizado=datetime.datetime.now()
                 ):

        self.id = id
        self.nombre_vulgar = nombre_vulgar
        self.nombre_cientifico = nombre_cientifico
        self.lugar = lugar
        self.descripcion = descripcion
        self.modalidades = modalidades
        self.epoca = epoca
        self.activo = activo
        self.creado = creado
        self.actualizado = actualizado

    @staticmethod
    def __get_especies_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        articles = []
        for row in rows:
            articles.append(
                Especies(
                    id=row[0],
                    nombre_vulgar=row[1],
                    nombre_cientifico=row[2],
                    lugar=row[3],
                    descripcion=row[4],
                    modalidades=row[5],
                    epoca=row[6],
                    activo=row[7],
                    creado=row[8],
                    actualizado=row[9]
                )
            )
        cursor.close()
        return articles

    @staticmethod
    def get_especies():
        # Obtengo todos los especies de la base (activos e inactivos)
        return Especies.__get_especies_by_query(
            """
        SELECT * 
        FROM especies 
        ORDER BY creado DESC
        """
        )

    @staticmethod
    def get_active_especies():
        return Especies.__get_especies_by_query(
            """
        SELECT * 
        FROM especies  
        WHERE activo = true
        ORDER BY creado DESC
        """
        )

    @staticmethod
    def get_especie(id_especie):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM especies  WHERE id = %s", (id_especie,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return Especies(
                id=row[0],
                nombre_vulgar=row[1],
                nombre_cientifico=row[2],
                lugar=row[3],
                descripcion=row[4],
                modalidades=row[5],
                epoca=row[6],
                activo=row[7],
                creado=row[8],
                actualizado=row[9]
            )
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:  # Actualizar un especie que ya existe
            cursor.execute(
                """
                    UPDATE especies 
                    SET nombre_vulgar = %s, nombre_cientifico = %s, descripcion = %s, lugar = %s, modalidades = %s, epoca = %s,
                    activo = %s, actualizado = %s
                    WHERE id = %s
                """,
                (
                    self.nombre_vulgar, self.nombre_cientifico, self.descripcion, f'{{"{self.lugar}"}}', self.modalidades, self.epoca,
                    self.activo, self.actualizado, self.id
                )
            )
        # De lo contrario si no tiene un id_especie especificado, significa que es una nueva
        else:  # Crear un nuevo Articulo
            cursor.execute(
                """
                    INSERT INTO especies
                    (nombre_vulgar, nombre_cientifico, descripcion, lugar, modalidades, epoca, activo, creado, actualizado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    self.nombre_vulgar, self.nombre_cientifico, self.descripcion, self.lugar, self.modalidades, self.epoca,
                    self.activo, self.creado, self.actualizado
                )
            )
            # Obtengo el ultimo valor de id, y se lo asigno al id_especie
            self.id_especie = cursor.lastrowid
        db.commit()                 # Hago efectivos los cambio sen las tablas
        cursor.close()

    def delete(self):
        # En realidad no se borra el registrofisicamente de la base. Se pone el estado del activo en false y de esta forma queda inactivo
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE especies  SET activo = false, actualizado = %s WHERE id = %s", (datetime.datetime.today(), self.id,))
        db.commit()
        cursor.close()

    def serializer(self):
        return {
            'id': self.id,
            'nombre_vulgar': self.nombre_vulgar,
            'nombre_cientifico': self.nombre_cientifico,
            'descripcion': self.descripcion,
            'lugar': self.lugar,
            'modalidades': self.modalidades,
            'epoca': self.epoca,
            'activo': self.activo,
            'creado': self.creado,
            'actualizado': self.actualizado,
        }
