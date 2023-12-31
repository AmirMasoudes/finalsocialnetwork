from django.urls import path
from . import views
from post import views
app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post/<int:post_id>/<slug:post_slug>/',views.PostDetailView.as_view(), name='post_detail'),
    path('post/delete/<int:post_id/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/delete/<int:post_id', views.PostUpdateViwe.as_view(),name='post_update'),
]