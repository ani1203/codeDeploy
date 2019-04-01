from django.urls import path, re_path
from .views import index, room

app_name = 'chat'   # giving the app name

urlpatterns = [
    path('', index, name='index'),     # giving path for the index method inside views
    re_path(r'^(?P<room_name>[^/]+)/$', room, name='room'),
]
