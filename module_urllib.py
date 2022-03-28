# Import module
from urllib import request

# Read google main page using usrlopen()
target = request.urlopen("https://googl.com")
output = target.read()

# Print
print(output)