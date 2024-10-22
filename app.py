from flask import Flask
from app.routes import main_bp

app = Flask(__name__)

# Registrar las rutas
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
