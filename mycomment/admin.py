from django.contrib import admin
from mycomment.models import head_comment, comment
# Register your models here.

admin.site.register(head_comment)
admin.site.register(comment)
