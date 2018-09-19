from django.conf.urls import url
from user_app import views

urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^add_user', views.add_user, name='add_user'),
]
