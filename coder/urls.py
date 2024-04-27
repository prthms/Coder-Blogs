from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='home'),
    path('blog/<str:slug>', views.getBlog, name='getBlog'),
    path('about', views.about, name='about'),
    path('search', views.searchBlog, name='searchBlog'),
    path('blogs-list', views.getBlogsList, name='getBlogsList'),
    path('contact', views.contact, name='contact'),
    path('signup', views.handleSignUp, name='handleSignUp'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('postComment', views.postComment, name='postComment'),
]
