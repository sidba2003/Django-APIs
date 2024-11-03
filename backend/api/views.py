from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

import json

from .models import Author, Book, Authorship


def author_api(request, author_id):
    """Handles GET, PUT, and DELETE requests for a single author."""
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return JsonResponse({'error': 'Author not found'}, status=404)
    
    if request.method == 'DELETE':
        author.delete()
        return JsonResponse({'message': 'Author deleted'})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        author.name = data['name']
        author.age = data['age']
        author.active = data['active']
        author.save()
        return JsonResponse(author.as_dict())
    elif request.method == 'GET':
        return JsonResponse(author.as_dict())
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def authors_api(request):
    """Handles GET and POST requests for authors."""
    if request.method == 'GET':
        authors = [author.as_dict() for author in Author.objects.all()]
        return JsonResponse({'authors': authors})
    elif request.method == 'POST':
        data = json.loads(request.body)
        author = Author.objects.create(
            name=data['name'],
            age=data['age'],
            active=data['active']
        )
        return JsonResponse(author.as_dict())
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def book_api(request, book_id):
    """Handles GET, PUT, and DELETE requests for a single book."""
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
    
    if request.method == 'DELETE':
        book.delete()
        return JsonResponse({'message': 'Book deleted'})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        book.title = data['title']
        book.description = data['description']
        book.published = data['published']
        book.save()

        # Clear existing authorships
        Authorship.objects.filter(book=book).delete()

        # Set new authors with is_lead_author
        authors_data = data.get('authors', [])
        for author_data in authors_data:
            author = Author.objects.get(id=author_data['id'])
            Authorship.objects.create(
                author=author,
                book=book,
                is_lead_author=author_data.get('is_lead_author', False)
            )
        return JsonResponse(book.as_dict())
    elif request.method == 'GET':
        return JsonResponse(book.as_dict())
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


def books_api(request):
    """Handles GET and POST requests for books."""
    if request.method == 'GET':
        books = [book.as_dict() for book in Book.objects.all()]
        return JsonResponse({'books': books})
    elif request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            description=data['description'],
            published=data['published']
        )
        # Set authors with is_lead_author
        authors_data = data.get('authors', [])
        for author_data in authors_data:
            author = Author.objects.get(id=author_data['id'])
            Authorship.objects.create(
                author=author,
                book=book,
                is_lead_author=author_data.get('is_lead_author', False)
            )
        return JsonResponse(book.as_dict())
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
