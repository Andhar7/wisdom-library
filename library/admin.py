from django.contrib import admin
from .models import Author, Category, Book

# Register your models here.


class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    fields = ("title", "published_date")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "birth_date")
    search_fields = ("name",)
    inlines = [BookInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "created_at")
    list_filter = ("categories", "author")
    search_fields = ("title", "author__name")
    readonly_fields = ("created_at",)
