
from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.


def setcookie(request):
    response = render(request, "student/setcookie.html")
    # max_age=60 after 60sec  it will destoryed
    #  max_age and expires can not use together
    response.set_cookie('name', "rohan", expires=datetime.utcnow()+timedelta(days=2))  
    return response

def getcookie(request):
    # name = request.COOKIES['name']
    # or
    # name= request.COOKIES.get("name")       
        # or if we have no name no key so to avoid error we use default key
    # SET DEFAULT NAME AS GUEST
    name = request.COOKIES.get("name","GUEST")
    return render(request,"student/getcookie.html",{'name':name})

def delcookie(request):
    response = render(request,"student/delcookie.html")
    response.delete_cookie("name")
    return response
