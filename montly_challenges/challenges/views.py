from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Eat no meat for rhe entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day! ",
    "april": "1Eat no meat for rhe entire month!",
    "may": "2Walk for at least 20 minutes every day!",
    "june": "3Learn Django for at least 20 minutes every day! ",
    "july": "11Eat no meat for rhe entire month!",
    "august": "22Walk for at least 20 minutes every day!",
    "september": "4Learn Django for at least 20 minutes every day! ",
    "october": "111Eat no meat for rhe entire month!",
    "november": "222Walk for at least 20 minutes every day!",
    "desember": None,
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("you invalid")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
        
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
     
    
    
    
  