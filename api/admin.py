from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Option)
admin.site.register(Quiz)
