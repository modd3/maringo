from . import views
from django.urls import path

app_name = 'maringo_site'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_register, name='signup'),
    path('member_register/', views.member_register, name='member_register'),
    path('all_members/', views.members, name='all_members'),
    ]