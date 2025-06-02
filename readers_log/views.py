from django.shortcuts import render

def index(request):
    """The home page for Readers Log."""
    return render(request, 'readers_log/index.html')