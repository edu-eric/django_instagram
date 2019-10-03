from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:post_id>/', views.detail, name="detail"),
    path('<int:post_id>/delete', views.delete, name="delete"),
    path('<int:post_id>/update', views.update, name="update"),
    path('<int:post_id>/comment/', views.create_comment, name="create_comment"),
    path('<int:post_id>/comment/<int:comment_id>/delete/', views.delete_comment, name="delete_comment"),
    path('<int:post_id>/like/<int:user_id>/', views.likeit, name="likeit"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)