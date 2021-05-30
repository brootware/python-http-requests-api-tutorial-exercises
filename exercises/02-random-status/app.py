import requests

response = requests.get("https://assets.breatheco.de/apis/fake/sample/random-status.php")
response = str(response.status_code)

if response == "404":
    print("The URL you asked is not found")
elif response == "503":
    print("Unavailable right now")
elif response == "200":
    print("Everything went perfect")
elif response == "400":
    print("Something is wrong on the request params")
else:
    print("Anything")