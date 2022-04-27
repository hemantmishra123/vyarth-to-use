"""vyarth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^main/$",views.Mainview.as_view(), name="main"),
    url(r"^login/$",  views.login_request, name='login'),
    url(r"^logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"^signup/$",  views.signup_request, name="signup"),
    url(r"^gview/$", views.GenView, name="gview"),
    url(r"^cview/$", views.ColView.as_view(), name="cview"),
    url(r'^result/$',views.Result.as_view(),name='result'),
    url(r"^new_view/$", views.new_view, name="new_view"),
    url(r"^send_data/$", views.send_data, name="send_data"),
    url(r"^register/$", views.signup_request, name='signup'),
    url(r"^map/$", views.signu_request, name='map'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
