from django.contrib import admin

# Register your models here.
from .models import Contact, myPost, blogComment

admin.site.register((Contact,  blogComment))

@admin.register(myPost)
class myPostAdmin(admin.ModelAdmin):
	class Media:
		js = ('js/injecter.js',)