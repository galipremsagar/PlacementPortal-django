from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def get_request(Req):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render())

@csrf_exempt
def post_request(Req):
    y = json.loads(Req.body)
    print "Got password",y['password']

@csrf_exempt
def x(Request):
    print Request.method
    if Request.method == "GET":
        return get_request(Request)
    elif Request.method == "POST":
        return post_request(Request)

