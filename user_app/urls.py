from django.conf.urls import url
from user_app import views

urlpatterns = [
    url(r'^list', views.users, name='users'),
    url(r'^add', views.add_user, name='add_user'),
]
