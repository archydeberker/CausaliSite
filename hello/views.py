from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})



def email_view(request):

    import os
    from postmark import PMMail
    from django.conf import settings

    message = PMMail(api_key = os.environ.get('POSTMARK_API_TOKEN'),
        subject = "Hello from Postmark",
        sender = "a@deberker.com",
        to = "a@deberker.com",
        text_body = "Hello",
        tag = "hello")


    message.send()

    return  HttpResponse('Email Sent Successfully')
