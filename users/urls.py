from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path('', views.users, name="users"),
    path('profile/<username>/', views.profile),
]
