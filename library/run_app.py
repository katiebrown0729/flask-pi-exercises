from flask import Flask, render_template, request
from library.mock_pi import pi_led_contraption as PC

app = Flask(__name__)
print("Initializing the app...")
led_contraption = PC.PiLedContraption()

@app.route('/')
def index():
    print("Rendering /")
    return render_template('index.html')

@app.route('/index.html')
def index_2():
    return render_template('index.html')

@app.route('/individual.html', methods=['POST', 'GET'])
def individual():
    if request.method == 'POST':
        print("POST")
        print(request.form)
        led_number = request.form["led_number"]
        action= request.form["led-state"]
        print(led_number)
        if(action=="On"):
           led_contraption.led_on(int(led_number))
        else:
            led_contraption.led_off(int(led_number))
    elif request.method == 'GET':
        print("GET")
    return render_template('individual.html')

@app.route('/group.html')
def group():
    return render_template('group.html')

@app.route('/patterns.html')
def patterns():
    return render_template('patterns.html')


# @app.route('/', methods=['POST', 'GET'])
# def hello_world():
#     if request.method == 'GET':
#         return render_template('forms/textanalytics_form.html')
#     elif request.method == 'POST':
#         kwargs = {
#             'string1': request.form['string1'],
#             'string2': request.form['string2'],
#             'union': ta.union(request.form['string1'],request.form['string2']),
#                 }
#         return render_template(
#             'forms/textanalytics_form_results.html', **kwargs)