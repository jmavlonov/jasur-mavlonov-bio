from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('contact-view/',views.contact_view,name='contact_view'),
      
]


