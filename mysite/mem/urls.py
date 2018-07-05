from django.conf.urls import url
from mem import views

app_name = 'mem'

urlpatterns = [
    url(r'^data/', views.getdata, name='getdata'),
    url(r'^$', views.main, name='main'),
]
