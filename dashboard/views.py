from django.shortcuts import render
from . models import Books
from . forms import *
from django.contrib import messages


# Create your views here.
def home(request):
        return render(request, 'dashboard/home.html')
    
def notes(request):
        if request.method == 'POST':
            form = NotesForm(request.POST)
            if form.is_valid():
                notes = Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
                notes.save()
            messages.success(request,f"Notes added from {request.user.username} successfully!")
        else:
            form = NotesForm()
        notes = Notes.objects.filter(user=request.user)
        context = {'notes': notes, 'form': form}
        return render(request, 'dashboard/notes.html',context)

def books(request):
        books = Books.objects.filter(user=request.user)
        return render(request, 'dashboard/books.html')

def conversion(request):
        return render(request, 'dashboard/conversion.html')

def dictionary(request):
        return render(request, 'dashboard/dictionary.html')

def homework(request):
        return render(request, 'dashboard/homework.html')

def todo(request):
        return render(request, 'dashboard/todo.html')

def wiki(request):
        return render(request, 'dashboard/wiki.html')    

def youtube(request):
        return render(request, 'dashboard/youtube.html')
