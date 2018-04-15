from flask import Flask, render_template, request
from library.real_pi import pi_led_contraption as PC
#from library.mock_pi import pi_led_contraption as PC

app = Flask(__name__)
print("Initializing the app...")
# led_contraption is an instance of pi_led_contraption. We need to make an instance of a class to call it.
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
        print("Individual POST")
        print(request.form)
        led_number = request.form["led_number"]
        action= request.form["led-state"]
        print(led_number)
        if(action=="on"):
           led_contraption.led_on(int(led_number))
        else:
            led_contraption.led_off(int(led_number))
    elif request.method == 'GET':
        print("GET")
    return render_template('individual.html')

@app.route('/group.html', methods=['POST', 'GET'])
def group():
    if request.method == 'POST':
        print("Group POST")
        print(request.form)
    return render_template('group.html')

@app.route('/patterns.html', methods=['POST', 'GET'])
def patterns():
    if request.method == 'POST':
        print("Patterns POST")
        print(request.form)
        action = request.form["Pattern"]
        if(action=="Race Up"):
            led_contraption.race_up()
        elif(action=="Race Down"):
            led_contraption.race_down()
        elif(action=="Dance"):
            led_contraption.dance()

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