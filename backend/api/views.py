from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import Author


def test_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })


def gauthor_api(request, author_id):
    author = Author.objects.get(id=author_id)
    
    match request.method:
        case 'DELETE':
            author.delete()
            return JsonResponse({
                'message': 'Author deleted'
            })
        case 'PUT':
            # to do
            pass


def author_api(request):
    match request.method:
        case 'GET':
            return JsonResponse({
                'authors': [author.as_dict() for author in Author.objects.all()]
            })
        case 'POST':
            data = json.loads(request.body)
            author = Author.objects.create(
                name=data['name'],
                age=data['age'],
                active=data['active']
            )
            return JsonResponse(author.as_dict())

