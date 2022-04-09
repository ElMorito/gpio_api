from flask import Flask
from flask import jsonify
import RPi.GPIO as GPIO

GRUEN = 17 #GPIO Nummer(!) NICHT die nummer vom durchzaehlen
ROT = 18 #GPIO Nummer(!) NICHT die nummer vom durchzaehlen
GELB = 27 #GPIO Nummer(!) NICHT die nummer vom durchzaehlen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(GRUEN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ROT, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GELB, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)
#Status ALLE
@app.route('/api/status')
def status_info():
    return jsonify(gruen=GPIO.input(GRUEN), gelb=GPIO.input(GELB), rot=GPIO.input(ROT))
# Toggle ALL
@app.route('/api/toggle/all')
def toggle_all():
    GPIO.output(GRUEN,not GPIO.input(GRUEN))
    GPIO.output(GELB,not GPIO.input(GELB))
    GPIO.output(ROT,not GPIO.input(ROT))
    return jsonify(gruen=GPIO.input(GRUEN), gelb=GPIO.input(GELB), rot=GPIO.input(ROT))
#ALL on
@app.route('/api/all_on')
def all_on():
    GPIO.output(GRUEN,GPIO.HIGH)
    GPIO.output(GELB,GPIO.HIGH)
    GPIO.output(ROT,GPIO.HIGH)
    return jsonify(gruen=GPIO.input(GRUEN), gelb=GPIO.input(GELB), rot=GPIO.input(ROT))
#ALL off
@app.route('/api/all_off')
def all_off():
    GPIO.output(GRUEN,GPIO.LOW)
    GPIO.output(GELB,GPIO.LOW)
    GPIO.output(ROT,GPIO.LOW)
    return jsonify(gruen=GPIO.input(GRUEN), gelb=GPIO.input(GELB), rot=GPIO.input(ROT))

# GRÜNES LICHT
@app.route('/api/gruen/on')
def gruen_on():
    GPIO.output(GRUEN,GPIO.HIGH)
    return jsonify(led=GPIO.input(GRUEN))

@app.route('/api/gruen/off')
def gruen_off():
    GPIO.output(GRUEN,GPIO.LOW)
    return jsonify(led=GPIO.input(GRUEN))

@app.route('/api/gruen/toggle')
def gruen_togggle():
    GPIO.output(GRUEN,not GPIO.input(GRUEN))
    return jsonify(led=GPIO.input(GRUEN))

@app.route('/api/gruen/status')
def gruen_status():
    return jsonify(led=GPIO.input(GRUEN))


# GELBES LICHT
@app.route('/api/gelb/on')
def gelb_on():
    GPIO.output(GELB,GPIO.HIGH)
    return jsonify(led=GPIO.input(GELB))

@app.route('/api/gelb/off')
def gelb_off():
    GPIO.output(GELB,GPIO.LOW)
    return jsonify(led=GPIO.input(GELB))

@app.route('/api/gelb/toggle')
def gelb_togggle():
    GPIO.output(GELB,not GPIO.input(GELB))
    return jsonify(led=GPIO.input(GELB))

@app.route('/api/gelb/status')
def gelb_status():
    return jsonify(led=GPIO.input(GELB))


# ROTES LICHT
@app.route('/api/rot/on')
def rot_on():
    GPIO.output(ROT,GPIO.HIGH)
    return jsonify(led=GPIO.input(ROT))

@app.route('/api/rot/off')
def rot_off():
    GPIO.output(ROT,GPIO.LOW)
    return jsonify(led=GPIO.input(ROT))

@app.route('/api/rot/toggle')
def rot_togggle():
    GPIO.output(ROT,not GPIO.input(ROT))
    return jsonify(led=GPIO.input(ROT))

@app.route('/api/rot/status')
def rot_status():
    return jsonify(led=GPIO.input(ROT))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")