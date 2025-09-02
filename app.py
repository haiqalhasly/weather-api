import os
from flask import Flask,request, url_for, jsonify
import requests
from dotenv import load_dotenv
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Load the environment variables from .env file
load_dotenv()
# Access the environment variable 
api_key = os.environ.get('API_KEY')

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Weather!"


def get_weather(location):
    

@app.route('/<location>', methods = ['GET'])
def api_weather(location):

    weather_key = f"{location}_data"
    weather_data = redis_client.get(weather_key)

    if weather_data is None:
        print("No data in cache, retrieving from API")  
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={os.environ.get('WEATHER_API_KEY')}"
        print("requesting url...")
        response = requests.get(url)

        if response.status_code == 200:
            weather_output = response.json()
            weather_output = jsonify(weather_output)
            redis_client.set(weather_key, json.dumps(weather_data))
            return weather_output
        else:
            return 404
    else:
        print("data in cache, serving from Redis")
        weather_output = json.loads(weather_data)
        return weather_output
    
if __name__ == '__main__':
    app.run(debug=True)