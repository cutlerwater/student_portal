from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('notes', views.notes, name="notes" ),
    path('books', views.books, name="books" ),
    path('conversion', views.conversion, name="conversion" ),
    path('dictionary', views.dictionary, name="dictionary" ),
    path('homework', views.homework, name="homework" ),
    path('todo', views.todo, name="todo" ),
    path('wiki', views.wiki, name="wiki" ),
    path('youtube', views.youtube, name="youtube" ),

]

