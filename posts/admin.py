from django.contrib import admin

from .models import Posts


class PostsAdmin(admin.ModelAdmin):
	class Meta:
		model = Posts


admin.site.register(Posts,PostsAdmin)