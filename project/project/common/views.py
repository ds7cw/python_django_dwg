from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'common/index-page.html', context)

def htmx_home(request):
    context = {}
    request.session["guess"] = ""  # Reset guess on page load
    return render(request, 'htmx/htmx-home.html', context)


def htmx_updated(request):

    letter = request.GET.get("letter", "")
    guess = request.session.get("guess", "")

    if len(guess) < 5:  # Ensure max length is 5
        guess += letter
        request.session["guess"] = guess
    
    return render(request, "htmx/htmx-updated.html", {"guess": guess})
