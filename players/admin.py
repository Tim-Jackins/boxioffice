from django.contrib import admin

# Register your models here.
from .models import Actor, Role

class ActorAdmin(admin.ModelAdmin):
	class Meta:
		model = Actor

admin.site.register(Actor, ActorAdmin)

class RoleAdmin(admin.ModelAdmin):
	class Meta:
		model = Role

admin.site.register(Role, RoleAdmin)
