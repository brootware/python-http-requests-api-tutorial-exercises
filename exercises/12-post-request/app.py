import requests

# your code here
url = "https://assets.breatheco.de/apis/fake/sample/post.php"
myobj = {'hello' : 'world'}
postThis = requests.post(url, data = myobj)

print(postThis.text)
