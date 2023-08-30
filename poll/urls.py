from django.urls import path, include
from .views import index, update_poll

urlpatterns = [
    path('', index, name="index"),
    path('<id>/update_poll', update_poll, name="update_poll"),

]



