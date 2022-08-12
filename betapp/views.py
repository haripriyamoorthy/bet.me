from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .api import odds_response,odds_json,sports_response
import random 
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.



def index(request):
    if request.method == "POST":
        serched = request.POST.get("search")
        sc = UpcommingMatchs.objects.filter(sports_name__contains=serched ,sports_title__contains=serched)
        return render(request,"index.html",{"result":sc,"data":odds_response.json()})
    else:
        return render(request,"index.html",{"data":odds_response.json()})
#this is used to check the user login details and accept or it will display the warning mgs 
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect("user")
            else:
                return HttpResponse("account not active")
        else:
            return HttpResponse("Invalid Login Details")
    else:
        return render(request,"login.html")
# this function is for logout function 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
# this is for register page checking or it will again redict to the register page 
def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfile(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            #return HttpResponseRedirect("register")
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfile()
    
    return render(request, 'register2.html', {'user_form': user_form, "profile_form": profile_form, "registered": registered})
    
   
# this all function where used for connect the html page 
def about(request):
    return render(request,"about.html")

def team(request):
    return render(request,"live.html",{"data":sports_response.json()})

def news(request):
    return render(request,"news.html")


def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")


def booking_page(request,text):
    if not request.user.is_authenticated:
        return redirect("login_user")
    booking = False
    if request.method == "POST":
        form = BookingForm(request.POST or None)
        if form.is_valid():
            form.save()
            booking = True
            return redirect("user")
        else:
            print(form.errors)
    else:
        form = BookingForm(initial={"price":random.randint(1,100),"upcomming_match":text})
        return render(request,"teamreg.html",{"form":form,"booking":booking})



