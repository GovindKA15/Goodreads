from django.urls import path
from .views import BookList, BookListById

urlpatterns = [
    path('books/', BookList.as_view()),
    path('books/<int:id>/',BookListById.as_view()),
    
    
]