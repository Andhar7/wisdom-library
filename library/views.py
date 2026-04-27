from django.shortcuts import redirect, render, get_object_or_404
from .models import Author, Book

# Create your views here.


def book_list(request):
    books = Book.objects.select_related("author").all()

    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, "library/book_list.html", {"book": book})


def book_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        author_id = request.POST["author_id"]
        author = get_object_or_404(Author, pk=author_id)

        Book.objects.create(title=title, author=author)

        return redirect("library:book_list")

    authors = Author.objects.all()

    return render(request, "library/book_create.html", {"authors": authors})
