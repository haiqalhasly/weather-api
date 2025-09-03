import os
from flask import Flask,request, url_for, jsonify
import requests
from dotenv import load_dotenv
import redis
import json
from datetime import timedelta
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Load the environment variables from .env file
load_dotenv()
# Access the environment variable 
api_key = os.environ.get('API_KEY')

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    storage_uri="redis://localhost:6379",)

@app.route('/')
def welcome():
    return "Welcome to Weather!"

@app.route('/<location>', methods = ['GET'])
@limiter.limit('10 per day')
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
            current_conditions = weather_output['currentConditions'] 

            redis_client.set(weather_key, json.dumps(current_conditions))
            redis_client.expire(weather_key, timedelta(hours=12))
            return jsonify(current_conditions)
        else:
            return 404
    else:
        print("data in cache, serving from Redis")
        weather_output = json.loads(weather_data)
        return jsonify(weather_output)

  # Flask will always ask for the browser icon for some reason, this will ignore it  
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

    

if __name__ == '__main__':
    app.run(debug=True)