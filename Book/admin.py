from django.contrib import admin
from .models import Books, Bookmarks, Score, Comment
# Register your models here.

@admin.register(Bookmarks)
class BookmarksAdmin(admin.ModelAdmin):
    pass

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    pass

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

