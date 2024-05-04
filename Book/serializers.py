from rest_framework import serializers

from .models import Books, Bookmarks, Score, Comment


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
    #comments = serializers.SerializerMethodField()
    class Meta:
        model = Books
        fields = ['title', 'abstract', 'comments_count', 'score_count', ]

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_score_count(self, obj):
        return obj.scores.count()

class BookMaarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = ['user_id', 'book_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'book_id', 'user_id']


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ['rate_number', 'book_id', 'user_id']
    """
    def get_comments(self, obj):
        return obj.comments()

    def get_score(self, obj):
        return obj.scores()
    

    def get_av_of_scores(self, obj):
        sum = 0
        scor = obj.score


        #sum = sum / obj.scores.count()
        return sum

    

    """