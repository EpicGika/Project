from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    # path('post_detail', views.post_detail, name='post_detail'),
]
