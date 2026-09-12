from django.shortcuts import render,redirect
from .models import *

def show(request):
    author = Author.objects.all()
    return render(request,'author.html',{'author' : author})

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
            author = request.POST['author'],
            pages = request.POST['pages'],
            price = request.POST['price'],
            description = request.POST['description']
        )
        return redirect('book_book')
    return render(request,'c_book.html')


def show_book(request):
    book = Book.objects.all()
    return render(request,'book.html',{'book' : book})


def delete(request,id):
    book = Book.objects.get(id =id)
    book.delete()
    return redirect('book_book')

def update(request,id):
    book = Book.objects.get(id =id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.pages = request.POST['pages']
        book.price = request.POST['price']
        book.description = request.POST['description']
        book.save()
        return redirect('book_book')
    return render(request,'update.html',{'book' : book})
