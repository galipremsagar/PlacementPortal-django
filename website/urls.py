from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.x,name='index'),
    url(r'^login/$',views.n,name='login')
]