from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from .models import Movie, Genre, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['label']
    save_on_top = True


class GenreAdmin(admin.ModelAdmin):
    search_fields = ['label']
    list_display = ['label']
    save_on_top = True


class MovieAdmin(admin.ModelAdmin):
    autocomplete_fields = ['genre']
    search_fields = ['title', 'imdb_id']
    readonly_fields = ['update_serial']
    list_display_links = ['title']
    list_filter = ['category',
                   ('genre', RelatedDropdownFilter),
                   'active']
    list_display = ['active',
                    'title',
                    'production_year',
                    'duration',
                    'category',
                    'created',
                    'modified']
    save_on_top = True


admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)

