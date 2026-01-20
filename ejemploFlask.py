# Importamos Flask desde el módulo flask
from flask import Flask

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Definimos una ruta (la página principal)
@app.route('/')
def pagina_principal():
    return "¡Hola! Mi aplicación Flask funciona correctamente 🚀"

# Ejecutamos la aplicación si el archivo se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)