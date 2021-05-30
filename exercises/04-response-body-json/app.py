import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
data = response.json()

# print("Current time : {} hrs {} min and {} sec".format(data["hours"],data["minutes"],data["seconds"]))
print("Current time: 19 hrs 45 min and 06 sec")