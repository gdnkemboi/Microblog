import json
import requests
from flask_babel import _
from app import app

def translate(text, source_lang, dest_lang):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {
         'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': ''
    }

    r = requests.post(
        'https://api.cognitive.microsofttranslator.com'
        f'/translate?api-version=3.0&from={source_lang}&to={dest_lang}', headers=auth, json=[{'Text': text}]
    )