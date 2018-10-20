from django.contrib import admin
from .models import Operator, Crisis, CrisisType, CrisisAssistance

admin.site.register(Operator)
admin.site.register(Crisis)
admin.site.register(CrisisType)
admin.site.register(CrisisAssistance)