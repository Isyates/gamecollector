from django.contrib import admin
from .models import History, Game, Photo
# Register your models here.
admin.site.register(Game)
admin.site.register(History)
admin.site.register(Photo)