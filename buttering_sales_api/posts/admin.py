from django.contrib import admin
from .models import Posts, Categories, Tags, Comments

admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(Comments)  