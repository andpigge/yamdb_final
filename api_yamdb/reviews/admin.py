from django.contrib import admin

from .models import Comment, CustomUser, Review, Title

admin.site.register(Review)
admin.site.register(Comment)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'email', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')


@admin.register(Title)
class TitleGenreAdmin(admin.ModelAdmin):
    """ Зарегистрировать поля произведений в админке. """
    list_display = (
        'pk',
        'name',
        'year',
        'description',
        'category'
    )

    list_editable = ('year',)
    search_fields = ('text',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'
