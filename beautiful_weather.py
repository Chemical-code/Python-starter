# Import module
from urllib import request
from bs4 import BeautifulSoup

# Read national weather using urlopen
target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup()
soup = BeautifulSoup(target, "html.parser")

# Find location tag
for location in soup.select("location"):
    # Print with inside city, wf, tmn, tmx tag
    print("City:", location.select_one("city").string)
    print("Weather:", location.select_one("wf").string)
    print("Min Temperature:", location.select_one("tmn").string)
    print("Max Temperature:", location.select_one("tmx").string)
    print()