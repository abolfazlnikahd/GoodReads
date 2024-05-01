import django.contrib.auth.models
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=32)


class Rate(models.Model):
    rate_number = models.PositiveSmallIntegerField(null=True)
    comment = models.TextField(null=True)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='rates')
    user_id = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE)


class Bookmarks(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='bookmarks')
    user_id = models.ForeignKey(django.contrib.auth.models.User, on_delete=models.CASCADE, related_name='bookmarks')
