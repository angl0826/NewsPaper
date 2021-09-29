from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали товара
    path('add/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]