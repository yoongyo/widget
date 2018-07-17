from django.contrib import admin
from .models import Post, Country
from .forms import CountryForm, PostForm

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    form = CountryForm


class PostAdmin(admin.ModelAdmin):
    list_display = []
    form = PostForm
admin.site.register(Post,PostAdmin)
