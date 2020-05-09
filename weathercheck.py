# Erin O'Neill 
# EC500

# Pulling City Info and outputting 

import json
import requests


def lookforCity(cityName):
	# Insert the API key here - removed for github
	apiKey = "###" 
	currentWeather = "http://api.openweathermap.org/data/2.5/weather?"
	currentWeatherURL = currentWeather+ "appid="+ apiKey+ "&q="+ cityName
	currentWeatherOut = requests.get(currentWeatherURL).json()

	# now that we have current data lets get our forecast 
	forecastWeather = "http://api.openweathermap.org/data/2.5/forecast?"
	forecastWeatherURL = currentWeather+ "appid="+ apiKey+ "&q="+ cityName
	forecastWeatherOut = requests.get(forecastWeatherURL).json()

	return forecastWeatherOut, currentWeatherOut 


def outputInfo(forecastWeatherOut, currentWeatherOut):
	##first check that we have good data 
	if forecastWeatherOut["cod"] == "404" or currentWeatherOut["cod"] == "404":
		print("Error finding data, please check your city and country input")
		return 0
	else: 
	    ## now that we know our data is good output the data 
	    ## first the current weather 
	    currentTempK = currentWeatherOut['main']['temp']
	    ## this temp isn't useful to us, put it in c and f 
	    currentTempC = currentTempK - 273.15
	    currentTempF = (currentTempC)*(9/5)+32
	    currentFeelsLikeK = currentWeatherOut['main']['feels_like']
	    currentFeelsLikeC = currentFeelsLikeK - 273.15
	    currentFeelsLikeF = (currentFeelsLikeC)*(9/5)+32

	    ## other conditions 
	    currentHumidity = currentWeatherOut['main']['humidity']
	    currentDescription = currentWeatherOut['weather'][0]["description"]
	    print("----------------------------------------------")
	    print("The current temperature in this city is : %.00f degrees F" % (currentTempF))
	    print(" and feels like : %.00f degrees F" % (currentFeelsLikeF))
	    print("Which is : %.00f degrees C" % (currentTempC))
	    print(" and feels like : %.00f degrees C" % (currentFeelsLikeC))
	    print("The humidity is at : %f %" % (currentHumidity))
	    print("Overall the weather is : " % (currentDescription))

	    ## Now lets output the forecast - pick 10 data points away 
	    forecastDateTime = forecastWeatherOut['list'][10]["dt_txt"]
	    forecastTempK = forecastWeatherOut['list'][10]['main']['temp']
	    ## this temp isn't useful to us, put it in c and f 
	    forecastTempC = forecastTempK - 273.15
	    forecastTempF = (forecastTempC)*(9/5)+32
	    forecastFeelsLikeK = forecastWeatherOut['list'][10]['main']['feels_like']
	    forecastFeelsLikeC = forecastFeelsLikeK - 273.15
	    forecastFeelsLikeF = (forecastFeelsLikeC)*(9/5)+32

	    ## other conditions 
	    forecastHumidity = forecastWeatherOut['list'][10]['main']['humidity']
	    forecastDescription = forecastWeatherOut['list'][10]['weather'][0]["description"]

	    print("------------------------------------------------")
	    print("And for the forecast at %s : " % (forecastDateTime))
	    print("The forecast temperature in this city is : %.00f degrees F" % (forecastTempF))
	    print(" and feels like : %.00f degrees F" % (forecastFeelsLikeF))
	    print("Which is : %.00f degrees C" % (forecastTempC))
	    print(" and feels like : %.00f degrees C" % (forecastFeelsLikeC))
	    print("The humidity is at : %.00f %" %(forecastHumidity))
	    print("Overall the weather is : " % forecastDescription)

	    print("------------------------------------------------")
	    return 1

def main():
	print("Please input a city to check current and future weather in:")
	print("format should be City,CountryCode (2 character country code)")
	print(" example: Boston,US (note that there is nospace between the city and country ")
	cityName = str(raw_input())
	[forecastWeatherOut, currentWeatherOut] = lookforCity(cityName)
	didCollectInfo = outputInfo(forecastWeatherOut, currentWeatherOut)
	print("--------------------------------------------")


if __name__ == '__main__':
  main()