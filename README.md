# WEATHER API

An app to get current weather using API

## Features

Here's some features that are implemented in this app:

* Search weather using city
* Caching for faster data retrieval
* Limits each client to 10 requests every 3 hours

## Example Usage

Example uses of this app.

![Weather](weather_api.gif)

## Getting Started

### Prerequisites

* Python 3.1 or higher
* Flask
* Redis (Cloud or local instance)
* Visual Crossing Weather API Key
  
``` py
# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={os.environ.get('WEATHER_API_KEY')}
```

### Installation
1. Clone the repository (in the terminal of your ide)

```py
git clone https://github.com/haiqalhasly/github-api-cli.git
```
3. Create a virtual environment

```py
  python -m venv venv
```
5. Activate the virtual environment
   * On windows
    ```py
    venv\Scripts\activate
    ```

   * On macOS/Linux
    ```py
    source venv/bin/activate
    ```

7. Install dependencies
```py
  pip install -r requirements.txt
```
8. Create environments variable
 ```bash
  touch.env
```
9. Within the `env`, add following content:
```env
    API_KEY=your_api_key_here
    REDIS_URL=your_redis_url_here
    WEATHER_API_KEY=your_weather_api_key_here
```

## Usage

1. Run `app.py` in command line or F5 key to start the server
```bash
python app.py
```
2. Follow the `URL` or quit the server using `ctrl+click`

```bash
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
3. Change the parameter for whatever city you want
```py
# http://127.0.0.1:5000/<city>
# example : http://127.0.0.1:5000/KualaLumpur
```

## API Response Format
The tool processes JSON responses from the Visual Crossing Weather API API using this format.
```
{
  "cloudcover": 88.0,
  "conditions": "Rain, Partially cloudy",
  "datetime": "13:09:00",
  "datetimeEpoch": 1756901340,
  "dew": 60.8,
  "feelslike": 67.1,
  "humidity": 80.5,
  "icon": "rain",
  "moonphase": 0.36,
  "precip": 0.027,
  "precipprob": 100.0,
  "preciptype": [
    "rain"
  ],
  "pressure": 996.0,
  "snow": 0.0,
  "snowdepth": 0.0,
  "solarenergy": 0.2,
  "solarradiation": 66.0,
  "source": "obs",
  "stations": [
    "D5621",
    "F6665",
    "EGLC"
  ],
  "sunrise": "06:16:31",
  "sunriseEpoch": 1756876591,
  "sunset": "19:42:08",
  "sunsetEpoch": 1756924928,
  "temp": 67.1,
  "uvindex": 1.0,
  "visibility": 6.2,
  "winddir": 182.0,
  "windgust": 18.6,
  "windspeed": 6.7
}
```

## Things that I have learned:
This project is a good starter to learn HTTP requests, caching and environment variables. Here's what I have achieved :

* Weather Data Retrieval: Fetches current weather conditions for any location using the Visual Crossing Weather API.
* Caching with Redis: Stores weather data in Redis for 12 hours to reduce API calls and improve response times.
* Rate Limiting: Limits each client to 10 requests every 3 hours to prevent abuse.
* Environment Variable Support: Uses a .env file for secure configuration of API keys and Redis connection.
* RESTful API: Simple endpoints for easy integration with other applications.
* Error Handling: Handles HTTP and Redis errors gracefully.

## Project Page

This is project based on roadmap.sh backend development roadmap.
Checkout project instructions [here](https://roadmap.sh/projects/weather-api-wrapper-service)


## References

1. Flask
  * <https://medium.com/@nguyenkims/python-decorator-and-flask-3954dd186cda>
  * <https://www.geeksforgeeks.org/python/decorators-in-python>
  * <https://www.youtube.com/watch?v=zsYIw6RXjfM>
  * <https://coderivers.org/blog/how-to-create-an-api-in-python>
  * <https://blog.luisrei.com/articles/rest.html>

2. Environment variables
  * <https://medium.com/@alwinraju/%EF%B8%8F-storing-environment-variables-and-api-keys-in-python-475144b2f098#ca0f>
  
3. Caching using Redis
  * <https://redis.io/docs/latest/develop/get-started>
  * <https://www.youtube.com/watch?v=jgpVdJB2sKQ&t=35s>
  * <https://www.youtube.com/watch?v=_8lJ5lp8P0U>
  * <https://redis.io/docs/latest/develop/clients/redis-py>
  * <https://redis.io/docs/latest/commands>
  
4. Rate limiting
  * <https://pypi.org/project/Flask-Limiter>
  * <https://www.youtube.com/watch?v=vQleDvTM5xA>
     
5. HTTP exception handling
  * <https://www.geeksforgeeks.org/python/exception-handling-of-python-requests-module>
