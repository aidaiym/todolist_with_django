from django.shortcuts import render
from .models import Profile
def todoappView(request):
    profile = Profile.objects.fiter
    return render(request, 'blog/todolist.html', {'Profile':Profile})
# Create your views here.
