from django.shortcuts import render
from django.http import JsonResponse


def sample_api_view(request):
    return JsonResponse({
        'message': 'Good response!'
    })
