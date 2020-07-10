from django.urls import path,include
from . import views
from .views import HomePage,DetailedView,AddPost,EditPost,DeletePost

urlpatterns = [
    path('',HomePage.as_view(),name="home"),
    path('detail/<int:pk>',DetailedView.as_view(),name="detail"),
    path('add_post/',AddPost.as_view(),name="create"),
    path('detail/edit/<int:pk>',EditPost.as_view(),name="update"),
    path('detail/<int:pk>/delete',DeletePost.as_view(),name="delete"),
]
