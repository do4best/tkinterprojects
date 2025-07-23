from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    company={
        "title":"RAvi Scientific Traders",
        "CEO":"Faisal Sadique"
    }
    return render(request,"index.html",company)

