from flask import Flask, render_template, request, redirect
import math
app = Flask(__name__)


class TrianguloRetangulo:
    def __init__(self, cateto1, cateto2, hipotenusa):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
        self.hipotenusa = hipotenusa


    def calcular(self):
        self.hipotenusa = math.sqrt((math.pow(self.cateto1, 2) + math.pow(self.cateto2, 2)))


msg_error = ""
msg_error_2 = ""
triangulo = TrianguloRetangulo("","","")


def is_number(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

@app.route('/')
def index():
    return render_template('index.html', msg=msg_error, resultado=triangulo, msg2=msg_error_2)

@app.route('/calcular', methods=['POST',])
def operacao():
    verifica = True
    cateto_1 = request.form['cateto1']
    cateto_2 = request.form['cateto2']
    if not is_number(cateto_1):
        global msg_error
        msg_error = "valor invalido"
        triangulo.cateto1= ""
        triangulo.hipotenusa = ""
        verifica = False

    else:
        triangulo.cateto1 = float(cateto_1)
    if not is_number(cateto_2):
        global msg_error_2
        msg_error_2 = "Valor invalido!"
        triangulo.cateto2 = ""
        triangulo.hipotenusa = ""
        verifica = False
    else:
            triangulo.cateto2=float(cateto_2)
    if verifica:
        triangulo.calcular()
    return redirect('/')

app.run(debug=True)