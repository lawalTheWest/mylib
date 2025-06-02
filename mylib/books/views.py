from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    sort_by = request.GET.get('sort', 'title')
    books = Book.objects.all().order_by(sort_by)
    return render(request, 'books/book_list.html', {'books' : books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def download_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if not book.file:
        raise Http404("File not found.")
    response = FileResponse(book.file.open('rb'), as_attachment=True, filename=book.file.name.split('/')[-1])
    return response
