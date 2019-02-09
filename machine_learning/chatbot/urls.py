from django.urls import path
from chatbot import views
from django.contrib.auth.views import LoginView,LogoutView


#URL list here
urlpatterns = [
path('',views.home,name = 'home'),
path('inference/',views.inference,name = 'inference'),
]
