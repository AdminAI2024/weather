from flask import Flask, render_template, jsonify
from address_scrper import extract_address
from weather_converter import get_address, get_weather_for_cities

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

# For cities
@app.route('/get_weather_cities', methods=['POST'])
def get_weather_cities():
    cities = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","NewHampshire","NewJersey","NewMexico","NewYork","NorthCarolina","NorthDakota","Ohio","Oklahoma","Oregon","Pennsylvania","RhodeIsland","SouthCarolina","SouthDakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","WestVirginia","Wisconsin","Wyoming"]
    weather_info = get_weather_for_cities(cities)
    if weather_info:
        return jsonify({'status': 'success', 'weather_info': weather_info})
    else:
        return jsonify({'status': 'error', 'message': 'Could not fetch weather data for cities'})

# For maps
@app.route('/get_weather', methods=['POST'])
def get_weather():
    address = extract_address()
    if address:
        weather_info = get_address(address)
        return jsonify({'status': 'success', 'address': address, 'weather_info': weather_info})
    else:
        return jsonify({'status': 'error', 'message': 'Could not extract address'})
if __name__ == '__main__':
    app.run(debug=True)
