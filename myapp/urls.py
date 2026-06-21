"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('register/',views.submit_form,name="register"),
    
    # main different page air jonno 
    
    path('post/<int:id>/',views.post_detail,name="post_detail"),
    
    # url dia catagory name catch kora hobo like Anime,Movies
    path('category/<str:cat_name>/',views.category_view,name="category_page"),
    
    # for about url
    path('about/',views.about_view,name="about_page"),
    
    # for top anime url
    
    path('top-30-anime/',views.top_anime,name="top_anime"),
    
    # for top anime url
    
    path('top-movies/',views.top_movies,name="top_movies"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)