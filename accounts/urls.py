from django.urls import path , include
from . import views 

app_name = 'accounts'
urlpatterns = [
    path('signup',views.job_list, name='signup'),

]