import django.contrib.auth.models
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404

class Books(models.Model):
    title = models.CharField(max_length=32)
    abstract = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}-id : {self.pk}'

class Score(models.Model):
    rate_number = models.PositiveSmallIntegerField(null=True, validators=[MaxValueValidator(5), MinValueValidator(0)])
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='scores')
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book_id.pk)
class Comment(models.Model):
    comment = models.TextField(null=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey('auth.User', on_delete= models.CASCADE)
    def __str__(self):
        return str(self.book_id.pk)

class Bookmarks(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmarks')
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='bookmarks')

    def __str__(self):
        book = Books.objects.get(pk=self.book_id.pk)
        return f'{book.title}'