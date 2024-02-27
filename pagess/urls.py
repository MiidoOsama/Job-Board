from django.urls import path , include
from . import views 

app_name = 'pagess'
urlpatterns = [
    path('',views.candidates, name='candidates'),

]