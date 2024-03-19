from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_location', methods=['POST'])
def get_location():
    address = request.json.get('address_input')

    # Check if address is provided
    if not address:
        return jsonify({'error': 'Address is required'}), 400

    # Make a request to the API
    api_url = f"https://geocode.maps.co/search?q={address}"  
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch data from the API'}), 500

@app.route('/get_weather_data', methods=['POST'])
def get_weather_data():
    latitude = request.json.get('latitude_value')
    longitude = request.json.get('longitude_value')

    # Check if address is provided
    if not longitude and latitude:
        return jsonify({'error': 'Address is required'}), 400

    # Make a request to the API
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,apparent_temperature,precipitation_probability,precipitation,pressure_msl,cloudcover,visibility,windspeed_10m,winddirection_10m"
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch data from the API'}), 500


if __name__ == '__main__':
    app.run(debug=True)