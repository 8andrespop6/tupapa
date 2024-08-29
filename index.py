from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
    return render_template('respuesta.html', res=name, email=email)
    
    
@app.route('/musica')
def musica():
    return render_template('musica.html')

@app.route('/vermas')
def vermas():
    return render_template('vermas.html')

if __name__ == '__main__':
    app.run(debug=True)
