# This script gives weather of the typed city
import re
import urllib.request

city=input("Enter your city")
url="http://www.weather-forecast.com/locations/"+city+"/forecasts/latest"

data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

m = re.search('span class="phrase">',data1)
start=m.start()+20

m=re.search('.</span></span></span></p><div class="forecast-cont"><div class="units-cont">',data1)
end=m.start()

print(data1[start:end])
