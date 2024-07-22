from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def template_home():
    return render_template("home.html")

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad'])

        # Precio por tarro
        precio_tarro = 9000

        # Calcula el total sin descuento
        total_sin_descuento = precio_tarro * cantidad_tarros

        # Calcula el descuento según la edad
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0

        # Calcula el total a pagar
        total_a_pagar = total_sin_descuento - descuento

        return render_template('ejercicio_1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               descuento=descuento, total_a_pagar=total_a_pagar)

    else:
        return render_template('ejercicio_1.html')



usuarios = {
    "juan": "admin",
    "pepe": "user"
}


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            if usuario == "juan":
                mensaje = "Bienvenido administrador juan"
            else:
                mensaje = f"Bienvenido usuario {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio_2.html", mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)