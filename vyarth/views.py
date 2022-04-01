from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.models import SubmitWaste,CollectWaste
from . import forms
from geopy.geocoders import Nominatim
from geopy import distance
from operator import itemgetter
from tabulate import tabulate
from django.core.mail import send_mail

from django.conf import settings

class HomePage(TemplateView):
    template_name = "start.html" 

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class GenView(CreateView):
    model = SubmitWaste
    form_class= forms.SubmitWasteForm
    success_url = reverse_lazy("home")
    template_name = "SignupG.html"
    #success_url
    #template_name='thankyou.html'
def send_data(request):
    form=forms.SubmitWasteForm()
    if request.method=='POST':
        #it is the rendering objects for data 
        form=forms.SubmitWasteForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            print("hello wolrld")
        return render(request,'')
    return render(request,'SignupG.html',{'form':form})



class ColView(CreateView):
    model = CollectWaste
    form_class= forms.CollectWasteForm
    success_url = reverse_lazy("home")
    template_name = "SignupC.html"
    #success_url
    #template_name='thankyou.html'

class Result(TemplateView):
    template_name='result.html'

geolocator = Nominatim(user_agent="myapp")
def new_view(request):
    form=forms.CollectWasteForm()
    if request.method=='POST':
        form=forms.CollectWasteForm(request.POST)
        if form.is_valid():
            print("hello")

            #send this information to this email value 
            email=form.cleaned_data['email']
            dataset=SubmitWaste.objects.filter(email=email).values_list()
            l=len(dataset)
            if(l==0):

                message="your data is not registered with us"
            else:

                print(l)
            
                li=[]
                for i in dataset:
                    li.append(i[2])
                    li.append(i[4])
                    li.append(i[5])

                item=li[0]
                print(item)
                item2=li[1]
                print(item2)

                item3=li[2]
                print(item3)
                ptr="we have Recieved your information. our executive will visit you in next working days .please stay connect with us "
                string=ptr+item2
            

                send_mail(
                    'waste Mangment your data with us ',
                    string,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,

            )

                message="form Submitted, We will get in touch to you shortly!!"
            #v=SubmitWaste.objects.filter(typeofwaste=a).values_list()
            #print(v)

            return render(request,'thankyou.html',{'message':message})
    return render(request,'SignupC.html',{'form':form})

def send_data(request):
    form=forms.SubmitWasteForm()
    if request.method=='POST':
        value=request.POST["value"]
        v=SubmitWaste.objects.filter(email=email).values_list()

