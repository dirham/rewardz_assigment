from django.http import JsonResponse
import requests

def search(term: str):
    try:
        params = {
                    'q': term,
                    'fields': 'key,title,author_name,editions,editions.key,editions.title,editions.language,cover_edition_key,number_of_pages,number_of_pages_median',
                    'limit': 10,
                }
        response = requests.get('https://openlibrary.org/search.json?',params=params)
        response.raise_for_status()
        data = response.json()  
        return JsonResponse(data)
    except requests.exceptions.RequestException as e:
        return JsonResponse(str(e))

    return JsonResponse(data)