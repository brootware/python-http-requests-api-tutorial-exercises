import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/project_list.php"
response = requests.get(url)
data = response.json()
print(data[1]["name"])