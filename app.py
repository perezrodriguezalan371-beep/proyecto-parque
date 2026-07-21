from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/leyendas')
def leyendas():
    return render_template('leyendas.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

if __name__ == '_main_':
    app.run(debug=True)