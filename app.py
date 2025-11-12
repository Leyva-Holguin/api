from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
api  = "https://pokeapi.co/api/v2/pokemon/"

app = Flask(__name__)

app.secret_key = 'CORBATAS_VIDRIO_EN_CIELOS_DE_MIEL_UN_GOLEM_REFLEJADO_EN_EL_ALEPH'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=["POST"])
def buscar():
    error=None
    pokemon_name = request.form.get('name', '').strip().lower()
    if not pokemon_name:
        flash('Ingrese un pokemon', 'error')
        return redirect(url_for('index'))
    
    try:
        resp = requests.get(f"{api}{pokemon_name}")
        if resp.status_code == 200:
            pokemon_data = resp.json()
            pokemon_info= {              
                'name': pokemon_data['name'].title(),
                'id': pokemon_data['id'],
                'height': pokemon_data['height']/10,
                'weight': pokemon_data['weight']/10,
                'sprite': pokemon_data['sprites']['front_default'],
                'shiny': pokemon_data['sprites']['front_shiny'],
                'abilities':[a['ability']['name'].title() for a in pokemon_data['abilities']],
                'types': [t['type']['name'].title() for t in pokemon_data['types']],
            }
            return render_template('pokemon.html', pokemon=pokemon_info)
        else: 
            flash('Pokémon no encontrado', 'error')
            return redirect(url_for('index'))
    except requests.exceptions.RequestException as e:
        flash('Error al busacar el pokemon', 'error')
        return redirect(url_for('index'))

#@app.route('/api-data')
#def get_api_data():
#    response = request.get('https://pokeapi.co/api/v2')
#    data = response.json()
#    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)