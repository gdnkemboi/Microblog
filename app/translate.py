import json
import requests
from flask_babel import _
from app import current_app

def translate(text, source_lang, dest_lang):
    if 'TRANSLATOR_KEY' not in current_app.config or not current_app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    url = "https://microsoft-translator-text.p.rapidapi.com/translate"

    querystring = {"to[0]": dest_lang,"api-version":"3.0","from": source_lang,"profanityAction":"NoAction","textType":"plain"}
    headers = {
        'content-type': 'application/json',
        'X-RapidAPI-Key': current_app.config['TRANSLATOR_KEY'],
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }

    r = requests.post(
        url, json=[{'Text': text}], headers=headers, params=querystring
    )

    if r.status_code != 200:
        return _('Error: The translation service failed.')
    return r.json()[0]['translations'][0]['text']