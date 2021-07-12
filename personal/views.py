from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.shortcuts import render
from django.conf import settings

DEBUG = False

@login_required(login_url="user:login")
def dashboard(request):
	context = {}
	context['debug_mode'] = settings.DEBUG
	context['debug'] = DEBUG
	context['room_id'] = "1"
	return render(request, "dashboard.html", context)