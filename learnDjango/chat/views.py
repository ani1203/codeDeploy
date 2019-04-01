# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):     # creating a index method to render the html page
    return render(request, 'chat/index.html', {})   # this method just render us to the index.html page


def room(request, room_name):   # creating the room function to render its html page
    # this will render to the html page
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })   # importing the mark-safe that is basically to pass in the json equivalent of this room name
