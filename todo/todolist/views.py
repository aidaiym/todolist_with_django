from django.shortcuts import render
from .models import Profile

def todolist(request):
    
    return render(request, 'blog/todolist.html')
# Create your views here.
