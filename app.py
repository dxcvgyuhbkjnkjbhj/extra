from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

    from flask import Flask, render_template

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal
@app.route("/")
def index():
    return "¡Bienvenido a mi aplicación Flask!"

# Ruta para una página de agradecimiento
@app.route("/gracias")
def gracias():
    return "¡Gracias por visitar esta página!"

# Punto de entrada principal
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

