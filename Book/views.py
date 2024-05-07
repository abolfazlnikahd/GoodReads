from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Books, Bookmarks, Score, Comment
from .serializers import BookSerializer, BookDetailSerializer, CommentSerializer, ScoreSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


# Create your views here.

class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        bok = Books.objects.all()
        serializer = BookSerializer(bok, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        bok = get_object_or_404(Books, **{'pk': pk})

        serializer = BookDetailSerializer(bok)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookMark(APIView):
    def get(self, request, pk, *args, **kwargs):
        bok = get_object_or_404(Books, **{'pk': pk})
        user = get_object_or_404(User, id=request.user.id)
        a = Comment.objects.filter(book_id=pk, user_id=request.user.id).exists()
        b = Score.objects.filter(book_id=pk, user_id=request.user.id).exists()
        c = Bookmarks.objects.filter(book_id=pk, user_id=request.user).exists()
        if a or b or c:
            return Response({"msg":"first"}, status=status.HTTP_400_BAD_REQUEST)
        obj = Bookmarks(book_id=bok, user_id=user)
        obj.save()
        return Response({"msg": f"The book with ID number {pk} has been added to your bookmark"},
                        status=status.HTTP_201_CREATED)

    """def delete(self, request, pk, *args, **kwargs):
        obj = Bookmarks.objects.filter(book_id=pk, user_id=request.user.id)
        obj.delete()

        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)"""


class BookMarkDelete(APIView):
    def get(self, request, pk, *args, **kwargs):
        obj = Bookmarks.objects.filter(book_id=pk, user_id=get_object_or_404(User, id=request.user.id))
        obj.delete()
        return Response("deleted", status=status.HTTP_204_NO_CONTENT)

class BookReaction(APIView):
    def post(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Books, **{"pk":pk})
        data_key = [i for i in request.data.keys()]
        data = request.data
        data['book_id'] = book
        data['user_id'] = request.user
        if 'rate_number' in data_key and 'comment' in data_key:
            comment = data['comment']
            del data['comment']
            score = ScoreSerializer().create(data)
            score.save()
            data['comment'] = comment
            del data['rate_number']
            comment = CommentSerializer().create(data)
            comment.save()
            return Response(status=status.HTTP_200_OK)

        elif 'rate_number' in data_key:
            score = ScoreSerializer().create(data)
            score.save()

            return Response(status=status.HTTP_200_OK)

        elif 'comment' in data_key:
            comment = CommentSerializer().create(data)
            comment.save()
            return Response(status=status.HTTP_200_OK)

