import string
import random
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.utils.text import slugify
from .models import Room


# Create your views here.
@login_required
def index(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'chat/index.html', {'name': room.name, 'slug': room.slug})


@login_required
def create(request):
    if request.method == "POST":
        room_name = request.POST["room_name"]
        uid = str(''.join(random.choices(string.ascii_letters + string.digits, k=4)))
        room_slug = slugify(room_name + "_" + uid)
        room = Room.objects.create(name=room_name, slug=room_slug)
        return redirect(reverse('chat', kwargs={'slug': room.slug}))
    else:
        return render(request, 'chat/create.html')


@login_required
def join(request):
    if request.method == "POST":
        room_slug = request.POST["room_slug"]
        room = Room.objects.get(slug=room_slug)
        return redirect(reverse('chat', kwargs={'slug': room.slug}))
    else:
        return render(request, 'chat/join.html')
