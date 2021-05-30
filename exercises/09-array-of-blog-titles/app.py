import requests

def get_titles():
    # your code here
    titles = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url).json()

    for i in response["posts"]:
        titles.append(i["title"])

    return titles


print(get_titles())