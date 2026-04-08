from flask import Flask, render_template, request
import requests
import pycountry

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    response = requests.get(f"https://api.nationalize.io/?name={name}")
    data = response.json()
    countries = []
    for c in data['country']:
        try:
            full_name = pycountry.countries.get(alpha_2=c['country_id']).name
        except:
            full_name = c['country_id']
        countries.append({'name': full_name, 'probability': c['probability']})
    return render_template('results.html', name=data['name'], countries=countries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')