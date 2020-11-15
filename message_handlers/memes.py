# Picks a random post meme from subreddit
import requests
import logging

MEME_ENDPOINT = "https://meme-api.herokuapp.com/gimme/{}"

def send_random_meme(subreddit=""):
    try:
        res = requests.get(MEME_ENDPOINT.format(subreddit))
        url = res.json()['url']
        return url
    except Exception as error:
        logging.error(error)
        return "No meme found Ayaya :("

