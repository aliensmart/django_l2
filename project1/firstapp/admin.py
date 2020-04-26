from django.contrib import admin
from firstapp.models import Topic, AccessRecord, Webpage

# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)