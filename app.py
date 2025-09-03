import os, requests, redis, json
from flask import Flask,request, url_for, jsonify
from dotenv import load_dotenv
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
@limiter.limit('10 per 3 hours')
def api_weather(location):

    weather_key = f"{location}_data"
    weather_data = redis_client.get(weather_key)


    if weather_data is None:
        print("No data in cache, retrieving from API")  
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={os.environ.get('WEATHER_API_KEY')}"
        print("requesting url...")
        response = requests.get(url)
        try:
            if response.status_code == 200:
                weather_output = response.json()
                current_conditions = weather_output['currentConditions'] 

                try:
                    redis_client.set(weather_key, json.dumps(current_conditions))
                    redis_client.expire(weather_key, timedelta(hours=12))

                except redis.RedisError as redis_error:
                    print(f"Redis error: {redis_error}")

                return jsonify(current_conditions)
        
        #HTTP requests error handling

            else:
                return f"Request failed with status: {response.status_code}", 500
            
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
        except requests.exceptions.ReadTimeout as errrt:
            print("Time out")
        except requests.exceptions.ConnectionError as conerr:
            print("Connection error")
        except requests.exceptions.RequestException as errex:
            print("Exception request")
        
    # Get in cache
    else:
        try:
            storedData = redis_client.get(weather_key)
            if storedData:
                print("data in cache, serving from Redis")
                weather_output = json.loads(weather_data)
                return jsonify(weather_output)
            
        except redis.RedisError as redis_error:
            print(f"Redis error: {redis_error}")

# Flask will always ask for the browser icon for some reason, this will ignore it  
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

    

if __name__ == '__main__':
    app.run(debug=True)