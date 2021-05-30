import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"
response = requests.get(url)
code = str(response.status_code)
text = response.text


if "200" in code:
    print(text)
else:
    print("Something went wrong")