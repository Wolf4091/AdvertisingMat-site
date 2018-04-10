# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.



"""start example views


def logout_view(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def create_user(request):
        if request.method == 'POST':

            firstname = str(request.POST["Firstname"])
            lastname = str(request.POST["Lastname"])
            address = str(request.POST["Address"])
            city = str(request.POST["City"])
            zip = str(request.POST["Zip"])
            email = str(request.POST["Email"])
            phone = str(request.POST["Phone"])
            username = str(request.POST["username"])
            password = str(request.POST["password"])
            application = str(request.POST["application"])
            imgloc = str(request.POST["Userimage"])
            try:
                user_information = UserInformation.objects.get(username=str(username))
                alert = " Alert!"
                respond = " Please Use a User That Doesn't Exist."
                context = {'alert':alert,'respond':respond}
                return JsonResponse(context)
            except:
                user_django = User()
                user_accounts = UserAccounts()
                user_django.username = username
                user_django.first_name = firstname
                user_django.last_name = lastname
                user_django.email = email
                user_django.set_password(password)
                user_information = UserInformation()
                user_information.username = username
                user_information.address = address
                user_information.city = city
                user_information.zip = zip
                user_information.email = email
                user_information.phone = phone
                user_information.application = application
                user_information.save()
                user_django.is_active = False
                user_django.save()
                userinfo = UserInformation.objects.get(username=username)
                local = UserImage.objects.get_or_create(user=userinfo)
                local.location = imgloc
                local.save()

            #send_email(email=email)
            user = authenticate(username=username, password=password)

            time.sleep(.5)
            return HttpResponse()


@csrf_exempt
def send_support_email(request):
    if request.method == 'POST':
        firstname = str(request.POST["Firstname"])
        lastname = str(request.POST["Lastname"])
        address = str(request.POST["Address"])
        city = str(request.POST["City"])
        zip = str(request.POST["Zip"])
        email = str(request.POST["Email"])
        phone = str(request.POST["Phone"])
        message = str(request.POST["contact"])
        send_spp_email(email=email, subject="Contact Form, iDevops", body=message)
        time.sleep(.5)
        return HttpResponse("Thank you for contacting us we will get back with you in 24 hours.")

@csrf_exempt
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse()
        
    else:
        alert = ' Alert!'
        respond = ' Username or password failed authentication.'
        context = {'respond':respond,'alert':alert}
        return JsonResponse(context)
        template = loader.get_template('login.html')
        context = {'installed': "no"}
        return HttpResponse(template.render(context, request))

@csrf_exempt
def index(request):
    if not request.user.is_authenticated:
        template = loader.get_template('login.html')
        context = {'installed': "no"}
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('login.html')
        context = {'installed': "no"}
        return HttpResponse(template.render(context, request))


End example Views"""
