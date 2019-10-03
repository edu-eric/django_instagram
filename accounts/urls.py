from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/', views.delete_account, name="delete_account"),
    path('update/', views.update_account, name="update_account"),
    path('password/', views.update_password, name="update_password"),
    path('<int:user_id>/', views.follow, name="follow"),
]