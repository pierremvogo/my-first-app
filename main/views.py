from django.shortcuts import render
from .models import User,School

def index(request):
    context = (
        {}
    )
    return render(request, 'index.html', context)

