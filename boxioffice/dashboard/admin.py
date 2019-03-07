from django.contrib import admin
from .models import dashboard
# Register your models here.

class dashboardAdmin(admin.ModelAdmin):
	class Meta:
		model = dashboard
admin.site.register(dashboard,dashboardAdmin)
