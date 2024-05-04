from django.urls import path
from .views import BookListView, BookDetailView, BookMark, BookMarkDelete





urlpatterns = [
    path('', BookListView.as_view(), name='book-index'),
    path('<int:pk>/Bookmark/delete', BookMarkDelete.as_view(), name='book-mark-delete'),
    path('<int:pk>/Bookmark', BookMark.as_view(), name='book-mark'),
    path('<int:pk>/', BookDetailView.as_view()),

    #path('score/add/', )
]