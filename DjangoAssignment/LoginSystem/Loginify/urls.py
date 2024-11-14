from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('users/', views.get_all_users, name='all_users'),
    path('users/<str:email>/', views.get_user, name='get_user'),
    path('users/update/<str:email>/', views.update_user, name='update_user'),
    path('users/delete/<str:email>/', views.delete_user, name='delete_user'),
]
