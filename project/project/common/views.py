from django.http import JsonResponse
from django.shortcuts import render

MAGIC_WORD = "APPLE"  # Hardcoded magic word for testing


def index(request):
    context = {}
    return render(request, 'common/index-page.html', context)


def htmx_home(request):
    context = {}
    request.session["guess"] = ""  # Reset guess on page load
    return render(request, "htmx/htmx-home.html", {"guess": ""})


def htmx_updated(request):

    letter = request.GET.get("letter", "")
    guess = request.session.get("guess", "")

    if len(guess) < 5:
        guess += letter
        request.session["guess"] = guess
    return render(request, "htmx/htmx-updated.html", {"guess": guess})


def check_guess(request):
    guess = request.session.get("guess", "")

    if len(guess) < 5:
        return JsonResponse({"error": "Enter all 5 letters before checking!"})

    # Generate feedback for letter accuracy
    feedback = []
    for i, letter in enumerate(guess):
        if letter == MAGIC_WORD[i]:  # Exact match → Green
            feedback.append({"letter": letter, "color": "green"})
        elif letter in MAGIC_WORD:  # Present but incorrect position → Yellow
            feedback.append({"letter": letter, "color": "yellow"})
        else:  # Not in the magic word → Grey
            feedback.append({"letter": letter, "color": "grey"})

    return JsonResponse({"feedback": feedback})  # Return letter color info

