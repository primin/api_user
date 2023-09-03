from flask import Flask

from config import config

# Routes
from routes import Usuario

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Página no encontrada</h1>",404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Usuario.main, url_prefix='/api/usuarios')
    
    # Error handlers
    app.register_error_handler(404,page_not_found)
    app.run()