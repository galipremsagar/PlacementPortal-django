from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def get_request(Req):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render())

def post_request(Req):
    pass

def x(Request):
    if Request.method == "GET":
        return get_request(Request)
    elif Request.method == "POST":
        return post_request(Request)

