import requests

def get_post_tags(post_id):
    # your code here
    tags = []
    url = "https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php"
    response = requests.get(url).json()

    for i in response["posts"]:
        if i["id"] == post_id:
            for n in i["tags"]:
                tags.append(n)
    
    return tags



print(get_post_tags(146))