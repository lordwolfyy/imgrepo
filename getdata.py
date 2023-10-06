import requests
def getapitoken():
    data = {
        'grant_type': 'client_credentials',
        'client_id': '14c69328e87c4505ad2552d97d449e49',
        'client_secret': '7001fa65b6404791abf5f674cf88bc3b',
    }

    r = requests.post('https://accounts.spotify.com/api/token', data=data)
    x = r.json()
    print(x['access_token'])
    return x['access_token']

def getsong(authtoken, id):
    headers = {
        'Authorization': f'Bearer {authtoken}',
    }
    response = requests.get(f'https://api.spotify.com/v1/tracks/{id}', headers=headers)
    x = response.json()
    author = x['artists'][0]['name']
    title = x['name']
    return author, title

r = getapitoken()