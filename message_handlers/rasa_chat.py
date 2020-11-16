import requests
import logging
import json

RASA_AI_ENDPOINT = "https://rasa-ai-chan.herokuapp.com/webhooks/rest/webhook"

def get_chat_message(message="Hi"):
    payload = {
        "message": message
    }

    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps(payload)

    try:
        response = requests.post(RASA_AI_ENDPOINT, data=payload, headers=headers)
        results = response.json()
        result = ""

        for answer in results:
            result += answer['text'] + "\n"
        
        return result


    except Exception as err:
        logging.error(err)
        return "UwU!"
    
