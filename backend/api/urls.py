"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import authors_api, author_api, books_api, book_api


urlpatterns = [
    # API entry points should be defined here
    path('authors/', authors_api, name='authors api'),
    path('authors/<int:author_id>/', author_api, name='author api'),
    path('books/', books_api, name='books api'),
    path('books/<int:book_id>/', book_api, name='book api'),
]
