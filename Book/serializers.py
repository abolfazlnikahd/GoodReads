from rest_framework import serializers, status
from django.shortcuts import  get_object_or_404
from rest_framework.response import Response

from .models import Books, Bookmarks, Score, Comment
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    book_marks = serializers.SerializerMethodField()
    class Meta:
        model = Books
        fields = ['id', 'title', 'abstract', 'book_marks']

    def get_book_marks(self, obj):
        return obj.bookmarks.count()




class BookDetailSerializer(serializers.ModelSerializer):
    """
    comments = serializers.SerializerMethodField()
    scores = serializers.SerializerMethodField()
    av_of_scores = serializers.SerializerMethodField()

    """
    comments_count = serializers.SerializerMethodField()
    score_count = serializers.SerializerMethodField()
    score_average = serializers.SerializerMethodField()
    score_rates = serializers.SerializerMethodField()

    #comments = serializers.SerializerMethodField()
    class Meta:
        model = Books
        fields = ['title', 'abstract', 'comments_count', 'score_count', 'score_average', "score_rates"]

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_score_count(self, obj):
        return obj.scores.count()

    def get_score_average(self, obj):
        if obj.scores.count() == 0:
            return obj.scores.count()
        sum = 0
        for score in obj.scores.all():
            sum += score.rate_number

        return sum / obj.scores.count()

    def get_score_rates(self, obj):
        score_1 = 0
        score_2 = 0
        score_3 = 0
        score_4 = 0
        score_5 = 0
        for score in obj.scores.all():
            if score.rate_number == 1:
                score_1 += 1
            elif score.rate_number == 2:
                score_2 += 1
            elif score.rate_number == 3:
                score_3 += 1
            elif score.rate_number == 4:
                score_4 += 1
            elif score.rate_number == 5:
                score_5 += 1
        return {"score_1": score_1, "score_2": score_2, "score_3": score_3, "score_4":score_4, "score_5": score_5}

class BookMaarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = ['user_id', 'book_id']

    def create(self, validated_data):
        return Bookmarks.objects.create(**validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'book_id', 'user_id']


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ['rate_number', 'book_id', 'user_id']


    def create(self, validated_data):
        bookmark = Bookmarks.objects.filter(book_id=validated_data['book_id'], user_id=validated_data['user_id'])
        if bookmark:
            for bok in bookmark:
                bok.delete()
        return Score(**validated_data)

    """def create(self, validated_data):
        super(ScoreSerializer, self).create(validated_data)
        obj = Bookmarks.objects.filter(user_id=validated_data['user_id'])
        for o in obj.all():
            o.delete()"""
