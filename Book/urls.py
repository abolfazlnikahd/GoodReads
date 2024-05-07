from django.urls import path
from .views import BookListView, BookDetailView, BookMark, BookMarkDelete, BookReaction





urlpatterns = [
    path('', BookListView.as_view(), name='book-index'),
    path('<int:pk>/Reaction', BookReaction.as_view(), name='book-reaction'),
    path('<int:pk>/Bookmark/delete', BookMarkDelete.as_view(), name='book-mark-delete'),
    path('<int:pk>/Bookmark', BookMark.as_view(), name='book-mark'),
    path('<int:pk>/', BookDetailView.as_view()),

    #path('score/add/', )
]