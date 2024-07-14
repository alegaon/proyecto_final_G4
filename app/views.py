from flask import jsonify, request
from datetime import datetime
from app.model import Especies


def index():
    return jsonify(
        {
            'message': 'Servicio API Especies de Peces en la Argentina'
        }
    )


def get_especies():
    especies = []
    especies = Especies.get_especies()
    print(especies)
    if not especies:
        return jsonify({'message': 'Species not found'}), 404
    return jsonify([especie.serializer() for especie in especies])


def get_especie(id_especie):
    especie = Especies.get_especie(id_especie)
    if not especie:
        return jsonify({'message': 'Species not found'}), 404
    return jsonify(especie.serializer())


def get_active_especies():
    especies = Especies.get_active_especies()
    return jsonify([especie.serializer() for especie in especies])


def new_especie():
    data = request.json
    new_art = Especies(
        nombre_vulgar=data['nombre_vulgar'],
        nombre_cientifico=data['nombre_cientifico'],
        descripcion=data['descripcion'],
        lugar=data['lugar'],
        modalidades=data['modalidades'],
        epoca=data['epoca'],
        activo=True,
        # creado=data['creado'],
        # actualizado=data['actualizado']
    )
    new_art.save()
    return jsonify({'message': 'Species created successfully'}), 201


def update_article(id_especie):
    campos_update = ['nombre_vulgar', 'nombre_cientifico',
                     'lugar', 'descripcion', 'modalidades', 'epoca', 'activo']
    especie = Especies.get_especie(id_especie)
    if not especie:
        return jsonify({'message': 'Species not found'}), 404
    data = request.json
    # Si se envia un diccionario vacio, se retorna un mesaje.
    if not data:
        return jsonify({'message': 'Nothing to update.', 'id': id_especie}), 404
    # Corrobora que la Key del diccionario a actualizar fue enviada, sino la pasa por alto. De lo contrario se rompe el Update
    for campo in campos_update:
        if campo in data:
            setattr(especie, campo, data[campo])
    # este queda automatico, cada vez que se realice un Update, se actualiza la fecha automaticamente.
    print(f"Fecha: {especie.creado}")
    especie.actualizado = datetime.today()
    print(f"actualizado: {especie.actualizado}")
    especie.save()
    return jsonify({'message': 'Species updated succesfully', 'data': data, 'id': id_especie})


def active_article(id_especie):
    especie = Especies.get_especie(id_especie)
    if not especie:
        return jsonify({'message': 'Species not found'}), 404
    especie.delete()
    return jsonify({'message': 'Species deleted successfully'}), 200
