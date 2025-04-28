from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
month_challenges_dict={
   "january":"this is january",
   "february":"this is february",
   "march":"this is march",
   "april":"this is april",
   "may":"this is may",
   "june":"this is june",
   "july":"this is july",
   "august":"this is august",
   "september":"this is september",
   "october":"this is october", 
   "november":"this is november",
   "december":None
}

def month_challenges_by_number(request,month):
  months=list(month_challenges_dict.keys())
  if month<=12:
    redirect_month = months[month-1]
    print(redirect_month)
    redirect_path=reverse("abc", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
  else:
    return HttpResponse("<h1>please provide valid number</h1>")

def month_challenges(request,month):
  try:
    challenge_text=month_challenges_dict[month]
    print(challenge_text)
    return render(request,"challenges/challenge.html",{
      "month":month,
      "text":challenge_text
    })
  except:
    return HttpResponse("<h1>There is no challenge for this month</h1>")
  
def basicpage(request):
  list_Of_months=list(month_challenges_dict.keys())
  return render(request,"challenges/index.html",{
    "months":list_Of_months
  })