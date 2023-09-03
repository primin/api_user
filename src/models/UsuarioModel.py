from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():
    # Para listar todos los usuarios con GET
    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios = []
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT id_usuario,nombre,primer_apellido,segundo_apellido,cedula_identidad,fecha_nacimiento FROM usuarios ORDER BY nombre ASC')
                resultset = cursor.fetchall()
                
                for row in resultset:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
                    usuarios.append(usuario.to_JSON())
                    
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)
    
    # Para listar un solo usuario enviandole un parametro
    @classmethod
    def get_usuario(self,id):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id_usuario,nombre,primer_apellido,segundo_apellido,cedula_identidad,fecha_nacimiento FROM usuarios WHERE id_usuario= %s",(id,))
                row = cursor.fetchone()
                
                usuario = None
                if row != None:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
                    usuario = usuario.to_JSON()
                    
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)
    
    # Para Insertar usuarios
    @classmethod
    def add_usuario(self, usuario):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:

                cursor.execute("""INSERT INTO usuarios (id_usuario,nombre,primer_apellido,segundo_apellido,cedula_identidad,fecha_nacimiento) 
                               VALUES (%s, %s, %s, %s, %s, %s)""",(usuario.id_usuario,usuario.nombre, usuario.primer_apellido, usuario.segundo_apellido, usuario.cedula_identidad, usuario.fecha_nacimiento))
                affected_rows = cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    # Para Eliminar usuarios
    @classmethod
    def delete_usuario(self, usuario):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (usuario.id_usuario,))
                affected_rows = cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    # Para Actualizar datos de usuarios
    @classmethod
    def update_usuario(self, usuario):
        try:
            connection = get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuarios SET nombre=%s, primer_apellido=%s, segundo_apellido=%s, cedula_identidad=%s, fecha_nacimiento=%s 
                               WHERE id_usuario= %s""",(usuario.nombre, usuario.primer_apellido, usuario.segundo_apellido, usuario.cedula_identidad, usuario.fecha_nacimiento, usuario.id_usuario))

                affected_rows = cursor.rowcount
                connection.commit()
                    
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    # Para obtener el promedio de edad con GET
    @classmethod
    def get_usuariosPromedio(self):
        try:
            connection = get_connection()
            usuarios = []
            
            with connection.cursor() as cursor:
                cursor.execute('SELECT ROUND(AVG(EXTRACT(YEAR FROM AGE(NOW(), fecha_nacimiento))),2) AS promedio_edades FROM usuarios;')
                row = cursor.fetchone()

            connection.close()
            return row
        except Exception as ex:
            raise Exception(ex)
    
    # Para obtener los datos de la Api con GET
    @classmethod
    def get_api(self):
        try:
            connection = get_connection()
            usuarios = []
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre_api,version,'desarrolladoPor',email FROM datos_api WHERE estado='ACTIVO'")
                row = cursor.fetchone()
                
                usuario = None
                if row != None:
                    usuario = {'nameSystem': row[0],
                               'version': row[1],
                               'developer': row[2],
                               'email': row[3]
                              }
                    
            connection.close()
            return usuario
        
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)