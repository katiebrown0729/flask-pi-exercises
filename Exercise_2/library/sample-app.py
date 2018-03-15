from flask import Flask, render_template, request
from library import textanalytics as ta

app = Flask(__name__)


@app.route('/test')
def mainpage():
    name = 'Matie'
    return render_template('index.html', name=name)

"""
@app.route('/')
def hello_world():
    return 'hello world'
    """

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('forms/textanalytics_form.html')
    elif request.method == 'POST':
        kwargs = {
            'string1': request.form['string1'],
            'string2': request.form['string2'],
            'union': ta.union(request.form['string1'],request.form['string2']),
                }
        return render_template(
            'forms/textanalytics_form_results.html', **kwargs)