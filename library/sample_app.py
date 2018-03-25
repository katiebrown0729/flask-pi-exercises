from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/index.htm')
def index_2():
    return render_template('index.htm')

@app.route('/individual.htm')
def individual():
    return render_template('individual.htm')

@app.route('/group.htm')
def group():
    return render_template('group.htm')

@app.route('/patterns.htm')
def patterns():
    return render_template('patterns.htm')


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