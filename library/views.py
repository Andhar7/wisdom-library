from .forms import BookForm
from django.shortcuts import redirect, render, get_object_or_404
from .models import Book

# Create your views here.


def book_list(request):
    books = Book.objects.select_related("author").all()

    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, "library/book_detail.html", {"book": book})


def book_create(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect("library:book_list")

    return render(request, "library/book_create.html", {"form": form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()

        return redirect("library:book_detail", pk=book.pk)

    return render(request, "library/book_update.html", {"form": form, "book": book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("library:book_list")

    return render(request, "library/book_delete.html", {"book": book})
