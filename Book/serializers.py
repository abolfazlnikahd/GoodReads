from rest_framework import serializers

from .models import Books, Bookmarks, Rate


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'abstract']

class BookmarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = ['id', '']