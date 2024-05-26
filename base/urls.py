from django.urls import path
from . import views
app_name = 'basic_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addToTask, name='addTask'),
    path('edit/<str:pk>/', views.editTask, name='editTask'),
    path('delete/<str:pk>/', views.deleteTask, name='deleteTask'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]