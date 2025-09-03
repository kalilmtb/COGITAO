from flask import Flask, render_template

app = Flask(__name__)

# Página principal (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Página de login (teladelogin.html)
@app.route('/login')
def login():
    return render_template('teladelogin.html')

# Rotas para outras seções (exemplo)
@app.route('/tccs')
def tccs():
    return render_template('tccs.html')

@app.route('/ics')
def ics():
    return render_template('ics.html')

@app.route('/mestrado')
def mestrado():
    return render_template('mestrado.html')

@app.route('/doutorado')
def doutorado():
    return render_template('doutorado.html')


if __name__ == '__main__':
    app.run(debug=True)
