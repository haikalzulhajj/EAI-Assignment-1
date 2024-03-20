from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Define API endpoints and keys
API_ENDPOINTS = {
    'LaLiga': {
        'url': 'https://laliga-standings.p.rapidapi.com/',
        'headers': {
            "X-RapidAPI-Key": "0c1987e45amsh7597114646015eep16cea2jsnac8c91ce1a50",
            "X-RapidAPI-Host": "laliga-standings.p.rapidapi.com"
        }
    },
    'Bundesliga': {
        'url': 'https://bundesliga-standings.p.rapidapi.com/',
        'headers': {
            "X-RapidAPI-Key": "0c1987e45amsh7597114646015eep16cea2jsnac8c91ce1a50",
            "X-RapidAPI-Host": "bundesliga-standings.p.rapidapi.com"
        }
    }
}

@app.route('/')
def root():
    return "Welcome to the football league standings!"

@app.route('/standings', methods=['GET', 'POST'])
def standings():
    selected_league = request.form.get('league', 'LaLiga')
    endpoint = API_ENDPOINTS[selected_league]
    response = requests.get(endpoint['url'], headers=endpoint['headers'])
    standings_data = response.json()
    return render_template('laliga.html', data=standings_data, selected_league=selected_league)

if __name__ == '__main__':
    app.run(debug=True)
