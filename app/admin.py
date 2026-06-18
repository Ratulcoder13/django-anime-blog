from django.contrib import admin
from .models import BlogApp,UserFormModel,TopAnime,TopMovies



class BlogAppAdmin(admin.ModelAdmin):
    
    list_display =('title','category','author','status','is_featured')
    
    list_editable = ('status','is_featured')
    
    
    
admin.site.register(BlogApp,BlogAppAdmin)
admin.site.register(TopAnime)
admin.site.register(TopMovies)
admin.site.register(UserFormModel)

    
# Register your models here.
