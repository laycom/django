from django.contrib import admin
from blogs.models import Blog, Tag, User

admin.site.register(Blog)
admin.site.register(User)
admin.site.register(Tag)
# Register your models here.
