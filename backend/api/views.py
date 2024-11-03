from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import Author


def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })


def author_api(request, author_id):
    author = Author.objects.get(id=author_id)
    print(f'author to be deleted is !!!! {author.as_dict()}')
    
    match request.method:
        case 'DELETE':
            author.delete()
            return JsonResponse({
                'message': 'Author deleted'
            })
        case 'PUT':
            data = json.loads(request.body)

            author.name = data['name']
            author.age = data['age']
            author.active = data['active']

            return JsonResponse(author.as_dict())


def authors_api(request):
    match request.method: 
        case 'POST':
            data = json.loads(request.body)
            author = Author.objects.create(
                name=data['name'],
                age=data['age'],
                active=data['active']
            )
            return JsonResponse(author.as_dict())
        
        case 'GET':
            return JsonResponse({
                        'authors': [author.as_dict() for author in Author.objects.all()]
                    })

