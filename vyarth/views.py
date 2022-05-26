from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from myapp.models import SubmitWaste,CollectWaste, Search
from . import forms
from geopy.geocoders import Nominatim
from geopy.distance import distance
from operator import itemgetter
from tabulate import tabulate
from django.core.mail import send_mail
from .forms import SearchForm
import folium
import geocoder
from django.conf import settings



class HomePage(TemplateView):
    template_name = "index.html" 

class Mainview(TemplateView):
    template_name = "works.html"

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

#class GenView(CreateView):
 #   model = SubmitWaste
  #  form_class= forms.SubmitWasteForm
   # success_url = reverse_lazy("home")
    #template_name = "SignupG.html"
    #success_url
    #template_name='thankyou.html'
def GenView(request):
    if request.method=='POST':
        #it is the orm Mapper For Creating a Database Table for and row for the user data .
        #it is the rendering objects for data 
        email=request.POST['email']
        fullname=request.POST['fullname']
        address=request.POST['address']
        zipcode=request.POST['zip-code']
        contact=request.POST['contact']
        typeofwaste=request.POST['Typeofwaste']
        print(typeofwaste)
        communityname=request.POST['communityname']
        quantity=request.POST['quantity']
        user=SubmitWaste(contact=contact,fullname=fullname,address=address,zipcode=zipcode,email=email,typeofwaste=typeofwaste,quantityofwaste=quantity,communityName=communityname)
        print(user)
        user.save()
        print(zipcode)
        string="Hi,Greetings from Vyarth !!We thank you for considering Vyarth Bekaar to Sweekar  as your waste remover. We have received your application. If you are interested to work we will connect to you soon, and your wastege will dispose. "
        send_mail(
                'vyarth Bekaar to Sweekar',
                string,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,

            )


        message="form Submitted, We will get in touch to you shortly!!"
        form = forms.SearchForm()
        
        address1 = Search.objects.all().last()
        location = geocoder.osm(zipcode)
        lat = location.lat
        print(lat)
        lng = location.lng
        point1=float(lat),float(lng)
        print(lng)
        
        
        location2=geocoder.osm(263660)
        lat1 = location2.lat
        lng1 = location2.lng
        lat = location.lat
        lng = location.lng
        point2=float(lat1),float(lng1)
        #km=distance(location,location2)
        m = folium.Map(location=[19, -12], zoom_start=2)
        folium.CircleMarker([lat, lng], tooltip='Click for more',
                  popup='country').add_to(m)
        
        folium.Marker([lat1, lng1], tooltip='Click for more',
                  popup='country').add_to(m)
        
        folium.PolyLine((point1,point2)).add_to(m)
        
        
        #client intiliazation on the  screen for dataset.
       
       
        

       
       
    # Get HTML Representation of Map Object
        m = m._repr_html_()
        context = {
            'm': m,
            'form': form,
        }
        return render(request, 'map.html', context)

    return render(request,'SignupG.html')
    
def signu_request(request):
    
    if request.method == 'POST':
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map')
    else:
        
        form = forms.SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    m = folium.Map(location=[19, -12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'map.html', context)
    
def login_request(request):
    title = "Login"
    form = forms.UserLoginForm(request.POST or None)
    context = {
        'form': form,
        'title': title,
    }
    print(context)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        login(request, user)
        # messages.info(request, f"You are now logged in  as {user}")
        return redirect('main')
    else:
        print(form.errors)
        # messages.error(request, 'Username or Password is Incorrect! ')
    return render(request, 'active.html', context=context)
#posting data with objects
def submit_waste(request):
    title = "Submit_Waste"
    if request.method == "POST":
        form = forms.SubmitWasteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = forms.SubmitWasteForm()

    context = {'form': form, 'title': title}
    return render(request, 'SignupG.html', context=context)



def signup_request(request):
    title = "Create Account"
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.RegistrationForm()

    context = {'form': form, 'title': title}
    return render(request, 'register.html', context=context)


class ColView(CreateView):
    model = CollectWaste
    form_class= forms.CollectWasteForm
    success_url = reverse_lazy("home")
    template_name = "SignupC.html"
    #success_url
    #template_name='thankyou.html'

class Sustain(TemplateView):
    template_name='sustain.html'
    
class Result(TemplateView):
    template_name='result.html'

class Waste(TemplateView):
    template_name='waste.html'
    
class Recycle(TemplateView):
    template_name='recycle.html'
class Organic(TemplateView):
    template_name='organic.html'

class Reduce(TemplateView):
    template_name='reduce.html'





geolocator = Nominatim(user_agent="myapp")
def new_view(request):
    if request.method=='POST':
        #email=request.POST['email']
        #fullname=request.POST['fullname']
        address=request.POST['address']
        zipcode=request.POST['zip-code']
        contact=request.POST['contact']
        typeofwaste=request.POST['Typeofwaste']
        communityname=request.POST['communityname']
        #quantity=request.POST['quantity']
        #user=CollectWaste(contact=contact,fullname=fullname,address=address,zipcode=zipcode,email=email,typeofwaste=typeofwaste,quantityofwaste=quantity,communityName=communityname)
        #print(user)
        #user.save()
        print(address)
        b=geolocator.geocode(zipcode)
        lat=b.latitude
        lon=b.longitude
        tup1=(lat,lon)
        print(lat,lon,"hello")
        #print(a)
        v=SubmitWaste.objects.filter(typeofwaste=typeofwaste).values_list()
        print(v)
        list1=[]
        rt=[]
        map=[]
        for i in v:
            temp=[]
            temp.append(i[4])
            temp.append(i[5])
            temp.append(i[1])
            map.append(i[7])
            
            rt.append(temp)
        dist=[]
        for ele in list1:
        
            tup2=(ele.latitude,ele.longitude)
            dist.append(distance.distance(tup1, tup2).km)
            print(dist)
            j=0
            for m in dist:
                rt[j].append(m)
        
            
        
        return render(request,'result.html',{'val':rt})


            #v=SubmitWaste.objects.filter(typeofwaste=a).values_list()
            #print(v)


        

        
    return render(request,'SignupC.html')

    
def mapurl(request):
    if request.method=='POST':
        #email=request.POST['email']
        #fullname=request.POST['fullname']
        address=request.POST['address']
        zipcode=request.POST['zip-code']
        contact=request.POST['contact']
        typeofwaste=request.POST['Typeofwaste']
        communityname=request.POST['communityname']
        print(address)
        b=geolocator.geocode(zipcode)
        lat=b.latitude
        lon=b.longitude
        tup1=(lat,lon)
        print(lat,lon,"hello")
        v=SubmitWaste.objects.filter(typeofwaste=typeofwaste).values_list()
        form = forms.SearchForm()
        map=[]
        for i in v:
            map.append(i[7])
        
        m = folium.Map(location=[19, -12], zoom_start=2)
        
        for i in range(len(map)):
            if(map[i]!=None):
                point=geolocator.geocode(map[i])
                x=point.latitude
                y=point.longitude
                folium.Marker([x, y], tooltip='Click for more',
                  popup='country').add_to(m)
        
        
        m = m._repr_html_()
        context = {
            'm': m,
            'form': form,
        }
        return render(request, 'map.html', context)
    
                
            
    return render(request,'SignupC.html')        
            
            
            
            
        
def send_data(request):
    form=forms.SubmitWasteForm()
    if request.method=='POST':
        value=request.POST["value"]
        v=SubmitWaste.objects.filter(email=email).values_list()

