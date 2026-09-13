from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def show(request):
    author = Author.objects.all()
    search = request.GET.get('search','')
    if search:
        author = author.filter(
            Q(name__icontains=search) |
            Q(last_name__icontains=search)
        )
    return render(request,'author.html',{'author' : author,'search' : search})

def creat(request):
    if request.method == 'POST':
        Author.objects.create(
            name = request.POST['name'],
            last_name = request.POST['last_name'],
            b_date = request.POST['b_date']
            
        )
        return redirect('author_author')
    return render(request,'create.html')
        

def creat_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title = request.POST['title'],
            author_id = request.POST['author'],
            pages = request.POST['pages'],
            price = request.POST['price'],
            description = request.POST['description']
        )
        return redirect('book_book')
    author = Author.objects.all()
    return render(request,'c_book.html',{'author' : author})


def show_book(request):
    book = Book.objects.select_related('author').all()
    search = request.GET.get('search','')
    if search:
        book = book.filter(
            Q(title__icontains=search) |
            Q(author__name__icontains=search) |
            Q(author__last_name__icontains=search) |
            Q(description__icontains=search)
        )
    return render(request,'book.html',{'book' : book,'search' : search})


def delete(request,id):
    book = get_object_or_404(Book,id =id)
    book.delete()
    return redirect('book_book')

def update(request,id):
    book = get_object_or_404(Book,id =id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author_id = request.POST['author']
        book.pages = request.POST['pages']
        book.price = request.POST['price']
        book.description = request.POST['description']
        book.save()
        return redirect('book_book')
    author = Author.objects.all()
    return render(request,'update.html',{'book' : book,'author' : author})
