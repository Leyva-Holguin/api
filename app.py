from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify

api  = "https://pokeapi.co/api/v2/pokemon/"

app = Flask(__name__)

app.secret_key = 'CORBATAS_VIDRIO_EN_CIELOS_DE_MIEL_UN_GOLEM_REFLEJADO_EN_EL_ALEPH'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods="POST")
def buscar():
    pokemon = request.form.get('name', '').strip().lower()
    return render_template('pokemon.html')

#@app.route('/api-data')
#def get_api_data():
#    response = request.get('https://pokeapi.co/api/v2')
#    data = response.json()
#    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)