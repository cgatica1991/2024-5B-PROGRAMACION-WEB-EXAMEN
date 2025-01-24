from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta para el formulario de cálculo de compras (form1)
@app.route('/form1', methods=['GET', 'POST'])
def form1():
    nombre = None
    total_sin_descuento = 0
    descuento = 0
    total_con_descuento = 0

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_por_tarro = 9000
        total_sin_descuento = tarros * precio_por_tarro

        if edad < 18:
            descuento = 0
        elif 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        else:
            descuento = total_sin_descuento * 0.25

        total_con_descuento = total_sin_descuento - descuento

    return render_template('form1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento,
                           total_con_descuento=total_con_descuento)


# Ruta para el formulario de inicio de sesión (form2)
@app.route('/form2', methods=['GET', 'POST'])
def form2():
    message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Diccionario simple con usuarios y contraseñas
        users = {
            'juan': 'admin',
            'pepe': 'user'
        }

        # Verifica las credenciales
        if username in users and users[username] == password:
            if username == 'juan':
                message = "Bienvenido administrador juan"
            elif username == 'pepe':
                message = "Bienvenido usuario pepe"
        else:
            message = "Credenciales incorrectas, intenta de nuevo."

    return render_template('form2.html', message=message)


# Ruta raíz que muestra opciones para ambos formularios
@app.route('/')
def index():
    # Este podría dirigir a una página que ofrezca enlaces a los dos formularios
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
