from flask import Flask, request

app = Flask(__name__)


# Página principal para elegir el ejercicio
@app.route('/')
def inicio():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Evaluación 3 - Python</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        body {
            background-color: #f5f5f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 80vh;
            padding: 20px;
        }
        h1 {
            color: #2d2d2d;
            margin-bottom: 30px;
            text-align: center;
            font-size: 24px;
            width: 100%;
        }
        h2 {
            color: #4a4a4a;
            margin-bottom: 40px;
            text-align: center;
            font-size: 18px;
            width: 100%;
        }
        .boton-ejercicio {
            width: 280px; /* Ancho suficiente para el texto completo */
            height: 60px; /* Alto cómodo */
            line-height: 60px; /* Centra el texto verticalmente */
            text-align: center;
            text-decoration: none;
            color: white;
            font-size: 18px;
            border-radius: 8px;
            margin: 15px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: block; /* Asegura que tome todo el ancho definido */
        }
        #btn-ej1 {
            background-color: #0059b3;
        }
        #btn-ej2 {
            background-color: #00a3a3;
        }
    </style>
</head>
<body>
    <h1>Evaluación 3 - Introducción a Python</h1>
    <h2>Selecciona el ejercicio que deseas realizar</h2>

    <a href="/ejercicio1" class="boton-ejercicio" id="btn-ej1">Ejercicio 1: Cálculo de Notas</a>
    <a href="/ejercicio2" class="boton-ejercicio" id="btn-ej2">Ejercicio 2: Nombre Más Largo</a>
</body>
</html>
    '''


# Página del Ejercicio 1 con su resultado
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado_notas = None
    promedio_notas = None
    asistencia = None

    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio_notas = round((nota1 + nota2 + nota3) / 3, 2)
        resultado_notas = "APROBADO 🎉" if asistencia >= 75 and promedio_notas >= 60 else "NO APROBADO ❌"

    return f'''
<!DOCTYPE html>
<html>
<head>
    <title>Ejercicio 1 - Cálculo de Notas</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        body {{
            background-color: #f5f5f5;
            padding: 30px;
        }}
        .contenedor-principal {{
            max-width: 500px;
            margin: 0 auto;
        }}
        h1 {{
            text-align: center;
            color: #0059b3;
            margin-bottom: 30px;
            font-size: 24px;
        }}
        .formulario {{
            background-color: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        label {{
            display: block;
            margin-top: 15px;
            color: #4a4a4a;
            font-size: 14px;
        }}
        input {{
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }}
        button {{
            width: 100%;
            margin-top: 20px;
            padding: 12px;
            border: none;
            border-radius: 4px;
            color: white;
            font-size: 16px;
            cursor: pointer;
            background-color: #0059b3;
        }}
        .resultado {{
            margin-top: 20px;
            padding: 15px;
            border-radius: 4px;
            text-align: center;
            font-weight: bold;
        }}
        .aprobado {{
            background-color: #d4edda;
            color: #155724;
        }}
        .no-aprobado {{
            background-color: #f8d7da;
            color: #721c24;
        }}
        .volver {{
            display: block;
            text-align: center;
            margin-top: 20px;
            color: #0059b3;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
        }}
    </style>
</head>
<body>
    <div class="contenedor-principal">
        <h1>Ejercicio 1: Cálculo de Notas</h1>

        <div class="formulario">
            <form method="POST">
                <label for="nota1">Nota 1 (0-100):</label>
                <input type="number" id="nota1" name="nota1" min="0" max="100" required>

                <label for="nota2">Nota 2 (0-100):</label>
                <input type="number" id="nota2" name="nota2" min="0" max="100" required>

                <label for="nota3">Nota 3 (0-100):</label>
                <input type="number" id="nota3" name="nota3" min="0" max="100" required>

                <label for="asistencia">Asistencia (%) (0-100):</label>
                <input type="number" id="asistencia" name="asistencia" min="0" max="100" required>

                <button type="submit">Calcular Resultado</button>
            </form>

            {f'<div class="resultado {"aprobado" if resultado_notas == "APROBADO 🎉" else "no-aprobado"}">Promedio: {promedio_notas} | Asistencia: {asistencia}%<br>Resultado: {resultado_notas}</div>' if resultado_notas else ''}

            <a href="/" class="volver">Volver a selección de ejercicios</a>
        </div>
    </div>
</body>
</html>
    '''


# Página del Ejercicio 2 con su resultado
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_largo = None

    if request.method == 'POST':
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()
        nombre_largo = max([nombre1, nombre2, nombre3], key=len)

    return f'''
<!DOCTYPE html>
<html>
<head>
    <title>Ejercicio 2 - Nombre Más Largo</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }}
        body {{
            background-color: #f5f5f5;
            padding: 30px;
        }}
        .contenedor-principal {{
            max-width: 500px;
            margin: 0 auto;
        }}
        h1 {{
            text-align: center;
            color: #00a3a3;
            margin-bottom: 30px;
            font-size: 24px;
        }}
        .formulario {{
            background-color: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        label {{
            display: block;
            margin-top: 15px;
            color: #4a4a4a;
            font-size: 14px;
        }}
        input {{
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
        }}
        button {{
            width: 100%;
            margin-top: 20px;
            padding: 12px;
            border: none;
            border-radius: 4px;
            color: white;
            font-size: 16px;
        }}
    </style>
</head>
<body>
    <div class="contenedor-principal">
        <h1>Ejercicio 2: Nombre con Más Caracteres</h1>

        <div class="formulario">
            <form method="POST">
                <label for="nombre1">Nombre 1:</label>
                <input type="text" id="nombre1" name="nombre1" required>

                <label for="nombre2">Nombre 2:</label>
                <input type="text" id="nombre2" name="nombre2" required>

                <label for="nombre3">Nombre 3:</label>
                <input type="text" id="nombre3" name="nombre3" required>

                <button type="submit" style="background-color: #00a3a3;">Encontrar Nombre Más Largo</button>
            </form>

            {f'<div style="margin-top:20px; padding:15px; border-radius:4px; text-align:center; font-weight:bold; background-color:#d1ecf1; color:#0c5460;">El nombre con más caracteres es:<br>{nombre_largo}</div>' if nombre_largo else ''}

            <a href="/" style="display:block; text-align:center; margin-top:20px; color:#00a3a3; text-decoration:none; font-weight:bold; font-size:16px;">Volver a selección de ejercicios</a>
        </div>
    </div>
</body>
</html>
    '''


if __name__ == '__main__':
    app.run(debug=True)