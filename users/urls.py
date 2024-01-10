from django.urls import path

from . import views

# localhost:8000/users/index/
# localhost:8000/users
# localhost:8000/

urlpatterns = [
    path('index/', views.index, name='users_main_view'),
    path('signup/', views.signup, name='users_signup_view'),
]