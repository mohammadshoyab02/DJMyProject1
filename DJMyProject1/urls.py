"""DJMyProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.urls import path,re_path
from django.urls import re_path
from MyApp1 import views;


#from App1 import views;
#from App2 import views;

#multiple approaches and multiple-views
#approach1(specific content)
from App1.views import  f11;
from App2.views import  f22;
#approach2(alias)
from App1 import views as v11;
from App2 import views as v22;


urlpatterns = [
    path('admin/', admin.site.urls),
   # path('welcome4/',views.display),
   # path('hellow/',v1.show),
    #single app and multiple-views
   # path('mrng/',v1.f1),
    #path('aftr/',v1.f2),
    #path('evng/',v1.f3),
    #multiple-apps with multiple-views
    #approach1
    path('hello/',f11),
    path('datetime/',f22),
    #approach2
    path('hello/',v11.f11),
    path('datetime/',v22.f22),
    path('test/',views.display),
    re_path('^.*$',views.display),




]
