from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from models import Auth1
import json

# Create your views here.


@csrf_exempt
def get_request(Req):
    template = loader.get_template('website/index.html')

    return HttpResponse(template.render())

@csrf_exempt
def post_request(Req):
    y = json.loads(Req.body)
    print Req.COOKIES['sessionid']
    temp_pin = int(str(y['pin']))

    expected_pass = str(Auth1.objects.filter(pin_number=temp_pin)[0].password)

    if(expected_pass==str(y['password'])):
        print "CORRECT pass"
        correct_row = Auth1.objects.filter(pin_number=temp_pin)[0]
        correct_row.sessionKey = str(Req.COOKIES['sessionid'])
        correct_row.save()
        template = loader.get_template('website/login.html')
        res_body = {}
        res_body['redirect'] = 'login/'
        return JsonResponse(res_body)
    else:
        return HttpResponse(status=500)



def login_get(Req):
    template = loader.get_template('website/login.html')
    return HttpResponse(template.render())

@csrf_exempt
def n(Req):
    if Req.method == "GET":
        return login_get(Req)


@csrf_exempt
def x(Request):
    print Request.method
    if Request.method == "GET":
        return get_request(Request)
    elif Request.method == "POST":
        return post_request(Request)


