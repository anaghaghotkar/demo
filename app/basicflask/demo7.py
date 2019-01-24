from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():

    dict = {' java ':23,' vb ':5,' Ai ':34}
    print (dict)
    return render_template('table.html',index = dict)

if __name__ == '__main__':
    app.run(debug = True)
