from . import views
from django.urls import path


urlpatterns = [
    path("", views.post, name='posts'),
    path("add_post/", views.AddPost.as_view(),name='add_post'),

    ]