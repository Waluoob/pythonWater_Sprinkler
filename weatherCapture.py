import requests
# creating a variable for city my sprinkler system is located in
citydata = "Mesa, Arizona"

# prints the city location
print(citydata)

# pass the City name onto the url
url = 'https://wttr.in/{}'.format(citydata)

# gathers local weather data of city
res = requests.get(url)

print(res.text)
