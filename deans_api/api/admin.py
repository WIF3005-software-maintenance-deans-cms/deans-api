from django.contrib import admin
from .models import Operator, Crisis, CrisisType, CrisisAssistance


admin.site.register(Operator)

class CrisisAdmin(admin.ModelAdmin):
    list_display = ('crisis_id', 'crisis_description','crisis_time','visible')
admin.site.register(Crisis, CrisisAdmin)

admin.site.register(CrisisType)
admin.site.register(CrisisAssistance)
