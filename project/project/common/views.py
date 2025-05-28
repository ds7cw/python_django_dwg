from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'common/index-page.html', context)

def htmx_home(request):
    context = {}
    return render(request, 'htmx/htmx-home.html', context)

def htmx_updated(request):
    context = {}
    return render(request, 'htmx/htmx-updated.html', context)
