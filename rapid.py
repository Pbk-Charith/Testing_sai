import requests

url = "https://linkedin-data-api.p.rapidapi.com/company-jobs"

# payload = {
# 	"companyIds": [5383240, 2382910],
# 	"page": 1
# }
# headers = {
# 	"x-rapidapi-key": "60afc02605mshab12b14c209bc06p1f1362jsn69570887ce1f",
# 	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

response = requests.post(url)

print(response.json())

