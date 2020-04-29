from flask import Flask
from shield_components.actuadores import RGBApagar, RGBprender
from shield_components.sensores import obtenerSenial
app = Flask(__name__)

@app.route('/')
def index():
    return 'Esto será una GUI para chimalli'

@app.route('/sensores')
def sensores():
    analog_1 = obtenerSenial()
    return 'Valor del sensor {}'.format(analog_1)

@app.route('/prender_rgb')
def prenderRGB():
    RGBprender()
    return 'Rgb en funcionamiento'

@app.route('/apagar_rgb')
def apagarRGB():
    RGBApagar()
    return 'RGB Apagado'

if __name__ == '__main__':
    app.run(port=5000, env=True)