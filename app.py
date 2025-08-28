from flask import Flask,request, url_for, jsonify
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Weather!"


@app.route('/weather/<city>', methods = ['GET'])
def api_weather(city):
    weather_data = {
    'london': {'temperature': 18, 'weather': 'Cloudy', 'humidity': 80},
    'tokyo': {'temperature': 25, 'weather': 'Partly Cloudy', 'humidity': 70},
    'newyork': {'temperature': 22, 'weather': 'Sunny', 'humidity': 60}
}
    if city in weather_data:
        return jsonify(weather_data[city])
    else:
        return "not_found", 404

if __name__ == '__main__':
    app.run(debug=True)