from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


"""
The decorator is how we register a class, compared to just
registering the standard model as on line 20. When we use a class,
we register it with a decorator which is more Pythonic and allows
us to customize how the models we are registering will appear
in the admin interface.

You need to run:

python3 manage.py migrate

after installing django-summernote because it comes with its own database models that need to be added to your database.
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)
# We can remove this line "admin.site.register(Post)" 
# after using the decorator above.