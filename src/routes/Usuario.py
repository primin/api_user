from flask import Blueprint,jsonify, request
#import uuid
import uuid 
#Entities
from models.entities.Usuario import Usuario
# Models
from models.UsuarioModel import UsuarioModel

main = Blueprint('usuario_blueprint',__name__)

# Muestra toda la lista de usuarios
@main.route('/')
def get_usuarios():
    try:
        usuarios = UsuarioModel.get_usuarios()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 

# Muestra un solo usuario
@main.route('/<id>')
def get_usuario(id):
    try:
        usuario = UsuarioModel.get_usuario(id)
        if usuario!=None:
            return jsonify(usuario)
        else:
            return jsonify({"mensaje":"No se encontro la pelicula"}),404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 

# Para insertar registros de usuarios:
@main.route('/usuarios', methods=['POST'])
def add_usuario():
    try:
        nombre = request.json['nombre']
        primerApellido = request.json['primerApellido']
        segundoApellido = request.json['segundoApellido']
        cedulaIdentidad = request.json['cedulaIdentidad']
        fechaNacimiento = request.json['fechaNacimiento']
        id_usuario = uuid.uuid4()
        print(id_usuario)        
        usuario = Usuario(str(id_usuario), nombre, primerApellido, segundoApellido, cedulaIdentidad, fechaNacimiento)
        affected_rows = UsuarioModel.add_usuario(usuario)
        
        if affected_rows == 1:
            return jsonify(usuario.id_usuario)
        else:
            return jsonify({'message': "Error al guardar el registro"}), 500
        
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 
    
    # Para eliminar usuarios:
@main.route('/usuarios/<id>', methods=['DELETE'])
def delete_usuario(id):
    try:
        usuario = Usuario(id)

        affected_rows = UsuarioModel.delete_usuario(usuario)

        if affected_rows == 1:
            return jsonify(usuario.id_usuario)
        else:
            return jsonify({'message': "No se pudo eliminar al usuario"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Para actualizar datos de usuario:
@main.route('/usuarios/<id>', methods=['PUT'])
def update_usuario(id):
    try:
        nombre = request.json['nombre']
        primerApellido = request.json['primerApellido']
        segundoApellido = request.json['segundoApellido']
        cedulaIdentidad = request.json['cedulaIdentidad']
        fechaNacimiento = request.json['fechaNacimiento']       
        
        usuario = Usuario(id, nombre, primerApellido, segundoApellido, cedulaIdentidad, fechaNacimiento)
        
        affected_rows = UsuarioModel.update_usuario(usuario)
        
        if affected_rows == 1:
            return jsonify(usuario.id_usuario )
        else:
            return jsonify({'message': "Error al actualizar el registro"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 

# Permite obtener el promedio de edad de todos los usuarios registrados:
@main.route('/promedio-edad/')
def get_usuariosPromedio():
    try:
        usuarios = UsuarioModel.get_usuariosPromedio()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

# Permite obtener los datos de la Api
@main.route('/estado/')
def get_api():
    try:
        usuarios = UsuarioModel.get_api()
        return jsonify(usuarios)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500 
