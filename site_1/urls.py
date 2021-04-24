"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from viewer.views import hello , MoviesView , MoviesViewTemplate , MoviesViewList, MovieCreateView , GenreCreateView, MovieUpdateView, MovieDeleteView, MovieDetailView


admin.autodiscover()
# admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<s0>/', hello, name="hello"),
    path('', MoviesViewList.as_view(), name="movies"), #class bassed view
    path('movie/create/', MovieCreateView.as_view(), name="movie_create"),
    path('genre/create/', GenreCreateView.as_view(), name="genre_create"),
    path('movie/update/<pk>/', MovieUpdateView.as_view(), name="movie_update"),
    path('movie/delete/<pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movie/detail/<pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('accounts/', include('accounts.urls', namespace='accounts'))
]
