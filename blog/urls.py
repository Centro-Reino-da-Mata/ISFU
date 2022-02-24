from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, \
    DeletePostView, AddCategoryView, CategoryView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('articulo/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('articulo/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('articulo/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
]