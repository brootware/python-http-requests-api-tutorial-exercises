import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
response = requests.get(url).json()

print(response["posts"][0]["author"]["name"])