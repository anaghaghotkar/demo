from flask import Flask
app = Flask(__name__)

@app.route('/h1/<name>')
def hello_name(name):
    return 'Hello ' + name + ' welcome'

if __name__=='__main__':
        app.run(debug=True)
