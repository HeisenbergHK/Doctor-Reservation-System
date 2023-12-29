from django.shortcuts import render


def home_view(request):
    return render(request, 'django/home.html')

# Create your views here.
