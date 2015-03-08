from django.contrib import admin
from .models import Subscribe

class Sub(admin.ModelAdmin):
	list_display = ('familyname','firstname','email')

admin.site.register(Subscribe,Sub)
