import requests

url = "https://assets.breatheco.de/apis/fake/sample/project1.php"
response = requests.get(url)
data = response.json()

print(data["name"])
# your code here