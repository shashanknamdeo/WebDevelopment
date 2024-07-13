from django.shortcuts import render

from django.http import HttpResponse

import requests

import json

def home(request):
    """
    """
    return render(request, 'Home.html')


def getMeaningOfWord(word):
    """
    """
    if len(word) != 0:
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word
        r = requests.get(url)
        htmlContent = r.content
        my_json = htmlContent.decode('utf8') #.replace("'", '"')
        data = json.loads(my_json)
        meaning_json = json.dumps(data, indent=4, sort_keys=True)
        return meaning_json
    # 
    else:
        print('Empty-Word-String')


def search(request):
    """
    """
    if request.method == 'GET':
        request_dict = dict(request.GET)
        word = request_dict['SearchWord'][0]
        meaning_json = getMeaningOfWord(word=word)
        print(meaning_json)
        html = "<html><body>Word : %s</body></html>" %meaning_json
        return HttpResponse(html)