from django.contrib import admin
from .models import Operator, Crisis, CrisisType

admin.site.register(Operator)
admin.site.register(Crisis)
admin.site.register(CrisisType)

