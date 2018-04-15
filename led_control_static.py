import os

#from library import sample_app as app
from library.run_app import app

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 8080))
    print("About to start the app!")
    app.run(host=host, port=port)

