import requests

def get_categories():
    res = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(res.status_code)
    # print(res.text)
    print(type(res))

    categories = res.json()
    print(categories)
    print(type(categories))
    for category in categories:
        print(category["name"])

