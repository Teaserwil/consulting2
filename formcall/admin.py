from django.contrib import admin
from . models import *
# Register your models here.
class FormcallAdmin (admin.ModelAdmin):
	list_display = [field.name for field in Formcall._meta.fields ]
	list_filter = ["name"]
	search_fields = ["name","email"]
	fields = ["email" , "name", "city", "number" ]
	
	class Meta:
		model = Formcall



admin.site.register(Formcall, FormcallAdmin)