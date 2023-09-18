from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name='home'),
    path("details/<int:param>/", details, name='details'),
    path("accept/", accept, name='accept'),
    path("sendmail/", sendmail, name='sendmail')
]