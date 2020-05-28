import os
import requests
from flask import Flask, url_for, jsonify, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
	if request.method == 'POST':
		country = request.form['country']   
		res = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a11f01e092807127f0217f4d1e793939'.format(country)).json()
		if res.get('message') is None:
			icon = res['weather'][0]['icon']
			icon_png = ('http://openweathermap.org/img/w/{}.png').format(icon)
			weather_main = res['weather'][0]['main']
			weather_description = res['weather'][0]['description']
			temp = res['main']['temp']
			humidity = res['main']['humidity']
			wind_speed = res['wind']['speed']
			work = 'Success'
		else:
			message = res['message']
			work = 'Failed'
			return render_template('index.html', message = message, work = work)
			
		

		return render_template('index.html', country = country, icon = icon_png, weather_main = weather_main, description = weather_description,
		temp = temp, humidity = humidity, wind_speed = wind_speed, work = work)
	return render_template('index.html')


{'coord': {'lon': 8, 'lat': 10}, 
'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 
'base': 'stations', 
'main': {'temp': 73.67, 'feels_like': 78.04, 'temp_min': 73.67, 'temp_max': 73.67, 'pressure': 1012, 'humidity': 80, 'sea_level': 1012, 'grnd_level': 926}, 
'wind': {'speed': 3.29, 'deg': 167}, 
'clouds': {'all': 100}, 
'dt': 1590619138, 
'sys': {'country': 'NG', 'sunrise': 1590555955, 'sunset': 1590601489}, 
'timezone': 3600, 'id': 2328926, 'name': 'Nigeria', 'cod': 200}