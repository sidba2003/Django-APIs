from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import Author, Book


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


def book_api(request, book_id):
    book = Book.objects.get(id=book_id)

    match request.method:
        case 'DELETE':
            book.delete()
            return JsonResponse({'message': 'Book deleted'})
        case 'PUT':
            data = json.loads(request.body)
            book.title = data['title']
            book.description = data['description']
            book.published = data['published']
            book.save()

            # Update authors
            authors_ids = data.get('authors', [])
            authors = Author.objects.filter(id__in=authors_ids)
            book.author.set(authors)

            return JsonResponse(book.as_dict())


def books_api(request):
    match request.method: 
        case 'POST':
            data = json.loads(request.body)
            book = Book.objects.create(
                title=data['title'],
                description=data['description'],
                published=data['published']
            )
            # Set authors
            authors_ids = data.get('authors', [])
            authors = Author.objects.filter(id__in=authors_ids)
            book.author.set(authors)

            return JsonResponse(book.as_dict())
        case 'GET':
            books = [book.as_dict() for book in Book.objects.all()]
            return JsonResponse({'books': books})

