from django.contrib import admin
from irontask_back.models import *

class BenevoleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Benevole, BenevoleAdmin)

class TriathlonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Triathlon, TriathlonAdmin)

class TypeTriathlonAdmin(admin.ModelAdmin):
    pass
admin.site.register(TypeTriathlon, TypeTriathlonAdmin)