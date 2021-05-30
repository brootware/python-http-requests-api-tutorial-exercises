import requests

url = "https://assets.breatheco.de/apis/fake/sample/save-project-json.php"
headerData = {"content-type" : "application/json"}
myData = {
    "id" : 2323,
    "title" : "Very big project"
}

resp = requests.post(url , json = myData, headers = headerData)
print(resp.json())