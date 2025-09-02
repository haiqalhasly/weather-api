import os
from flask import Flask,request, url_for, jsonify
import requests
from dotenv import load_dotenv


# Load the environment variables from .env file
load_dotenv()
# Access the environment variable 
api_key = os.environ.get('API_KEY')

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Weather!"


@app.route('/<location>', methods = ['GET'])
def api_weather(location):

    #fetch from api
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={os.environ.get('WEATHER_API_KEY')}"
    print("requesting url...")
    response = requests.get(url)

    if response.status_code == 200:
        events = response.json()
        return jsonify(events)
if __name__ == '__main__':
    app.run(debug=True)