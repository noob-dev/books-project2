from django.http import HttpResponse
from django.urls import reverse
from .models import Book, Author, Category


def book_list(request):
    books = Book.objects.all()

    book_items = ''
    for book in books:
        book_items += f'<li><a href="{reverse("book_detail", args=[book.pk])}">{book.title}</a></li>'

    html = f"""
    <html>
    <head><title>Book List</title></head>
    <body>
        <h1>Books List</h1>
        <ul>
            {book_items}
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

    html = f"""
    <html>
    <head><title>{book.title}</title></head>
    <body>
        <h1>{book.title}</h1>
        <p><strong>Author:</strong> {book.author}</p>
        <p>{book.description}</p>
        <a href="{reverse("book_list")}">Back to book list</a>
    </body>
    </html>
    """
    return HttpResponse(html)



def category_list(request):
    categories = Category.objects.all()

    category_items = ''
    for category in categories:
        category_items += f'<li><a href="{reverse("category_detail", args=[category.pk])}">{category.name}</a></li>'

    html = f"""
    <html>
    <head><title>Category List</title></head>
    <body>
        <h1>Categories List</h1>
        <ul>
            {category_items}
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)


def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse("Category not found", status=404)

    books = Book.objects.filter(category=category)
    book_list = ''.join([f'<li>{book.title}</li>' for book in books])

    html = f"""
    <html>
    <head><title>{category.name}</title></head>
    <body>
        <h1>{category.name}</h1>
        <h2>Books in this category:</h2>
        <ul>
            {book_list}
        </ul>
        <a href="{reverse("category_list")}">Back to category list</a>
    </body>
    </html>
    """
    return HttpResponse(html)



def author_list(request):
    authors = Author.objects.all()

    author_items = ''
    for author in authors:
        author_items += f'<li><a href="{reverse("author_detail", args=[author.pk])}">{author.name}</a></li>'

    html = f"""
    <html>
    <head><title>Author List</title></head>
    <body>
        <h1>Authors List</h1>
        <ul>
            {author_items}
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html)


def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return HttpResponse("Author not found", status=404)

    books = Book.objects.filter(author=author)
    book_list = ''.join([f'<li>{book.title}</li>' for book in books])

    html = f"""
    <html>
    <head><title>{author.name}</title></head>
    <body>
        <h1>{author.name}</h1>
        <h2>Books by this author:</h2>
        <ul>
            {book_list}
        </ul>
        <a href="{reverse("author_list")}">Back to author list</a>
    </body>
    </html>
    """
    return HttpResponse(html)
