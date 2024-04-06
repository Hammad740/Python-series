import requests


def random_jokes():
    url = 'https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1'
    response = requests.get(url)
    data = response.json()
    if data['success'] == True and data['statusCode'] == 200 and 'data' in data:
        joke = data['data']['data'][2]['content']
        return joke
    else:
        raise Exception("Failed to connect")


try:
    joke = random_jokes()
    print(joke)
except Exception as e:
    print(e)

# //The response.json() method is a convenient way to parse the JSON-formatted content of a response from text into a Python dictionary (or list, depending on the structure of the JSON data). This conversion allows you to interact with the data by accessing elements with keys or indices, iterating through it, and so on, just as you would with any normal Python data structure.
