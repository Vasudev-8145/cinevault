
from django.urls import path

from film.views import UserCreateView,AdminCreateView
from film.views import MovieListView,MoviecreateView,MovieRetrieveUpdateDeleteView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    # route to admin create view
    path("admin/",AdminCreateView.as_view()),

    # route to user create view
    path("register/",UserCreateView.as_view()),

    # route to token authentication
    path("token/",ObtainAuthToken.as_view()),

    # route to movie list
    path("movie/all/",MovieListView.as_view()),

    # route to movie create view
    path("movie/add/",MoviecreateView.as_view()),

    # route to movie retrieve,update,delete view
    path("movie/<int:pk>/",MovieRetrieveUpdateDeleteView.as_view())
]