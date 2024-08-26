import requests

url = "https://ipinfo.io/161.185.160.93/geo"

response = requests.get(url)

print(response.json())