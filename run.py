from flask import Flask
from flask_cors import CORS
from app.views import *
from app.database import *

app = Flask(__name__)

# Rutas
app.route('/', methods=['GET'])(index)

app.route('/api/especies', methods=['GET'])(get_especies)

app.route('/api/especies/<int:id_especie>', methods=['GET'])(get_especie)
app.route('/api/especies/activos', methods=['GET'])(get_active_especies)

app.route('/api/especie/create', methods=['POST'])(new_especie)

app.route('/api/especies/update/<int:id_especie>',
          methods=['PUT'])(update_article)
app.route('/api/especie/activo/<int:id_especie>',
          methods=['DELETE'])(active_article)

# Realizo una prueba de conexion a la base de datos
test_conn()
create_especies()

init_app(app)
CORS(app)


if __name__ == '__main__':
    app.run(debug=True)
