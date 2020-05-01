from flask import Flask, render_template
from flask_socketio import SocketIO, send

import time

from shield_components.actuadores import RGBApagar, RGBprender
from shield_components.sensores import obtenerSenial

app = Flask(__name__)

#session
app.config['SECRET_KEY'] = 'LApalabraSecreta'

#socket
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'Esto será una GUI para chimalli'

@app.route('/dashboard', methods = ['POST', 'GET'])
def dashboard():
    return render_template('index.html')

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

@socketio.on('data')
def read_sensor():
    while True:
        data = obtenerSenial()
        send(data, broadcast = True)
        time.sleep(0.5)


if __name__ == '__main__':
    socketio.run(port=5000, env=True)