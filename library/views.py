from django.http import JsonResponse
from .models import Book

# Create your views here.


def book_list(request):
    books = Book.objects.select_related("author").all()
    data = [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author.name,
        }
        for book in books
    ]
    return JsonResponse({"books": data})
