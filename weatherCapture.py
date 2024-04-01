import requests
from bs4 import BeautifulSoup

URL = "https://www.accuweather.com/en/us/mesa/85203/current-weather/331799"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")



webWeather = soup.find("div", class_="card-content")

for weatherInfo in webWeather:
    displayTemp = weatherInfo.find("h2", class_="display-temp")
    weatherPhrase = weatherInfo.find("h3", class_="phrase")
    print(displayTemp)
    print(weatherPhrase)

    print()