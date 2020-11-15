import requests

def check_valid_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        return True
    else:
        return False