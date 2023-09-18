from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TrekDetail, Photo
from django.forms.models import model_to_dict
from django.conf import settings
from .forms import ContactUs
from django.template.loader import render_to_string
from email.message import EmailMessage
import smtplib


# Create your views here.
def details(request, param):

    trekDetails = model_to_dict(TrekDetail.objects.get(pk = param))
    # print(trekDetails.items())

    updatedTrekDetails = {}

    for key,x in trekDetails.items():
        
        if isinstance(x, str):
            tmp = x.splitlines()
            if len(tmp) > 1:
                updatedTrekDetails[key] = x.splitlines()
            else:
                updatedTrekDetails[key] = x
        else:
            updatedTrekDetails[key] = x

    try:
        updatedTrekDetails['image'] = settings.MEDIA_URL + str(Photo.objects.get(pk = updatedTrekDetails['imageFK']))
    except:
        updatedTrekDetails['image'] = ""

    return render(request, 'details.html', updatedTrekDetails)


def home(request):
    trekList = TrekDetail.objects.all()
    # print(trekList)

    updatedTrekList = []
    for x in trekList:
        tmp = model_to_dict(x)

        try:
            img = settings.MEDIA_URL + str(Photo.objects.get(pk = tmp['imageFK']))
        except:
            img = ""

        updatedTrekList.append({'pk':tmp['id'], 'value':[tmp['name'], tmp['price']], 'image': img})
    # print(updatedTrekList)

    form = ContactUs()
    # print(form) 

    return render(request, 'home.html', {'hi':updatedTrekList, 'form':form})


def accept(request):
    if request.method == "POST":
        contactUsForm = ContactUs(request.POST)

        # if contactUsForm.is_valid():
        #     print(contactUsForm)
    
    return JsonResponse({'message': "sucess"})


def sendmail(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        smtp = smtplib.SMTP_SSL('smtp.gmail.com',465)

        try:
            smtp.login(settings.MAIL_HOST_NAME, settings.MAIL_PASSWORD)
        except:
            return JsonResponse({'message':'fail'})
        
        print("login successfull")
        print(message)

        msg = EmailMessage()
        msg['Subject'] = f"Contacted by {name}"
        msg['From'] = settings.MAIL_HOST_NAME
        msg['To'] = settings.MAIL_HOST_NAME

        msg.set_content("Checking...")

        htmlToString = render_to_string('mail.html',{'name':name, 'email':email, 'message':message})
        msg.add_alternative(htmlToString, subtype = 'html')

        smtp.send_message(msg)

        # print("Email Sent Successfully")

        return JsonResponse({'message':'success'})
    

    return JsonResponse({'message':'fail'})