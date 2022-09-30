from datetime import datetime
import requests
from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.
from post.models import Job, MyHistory, Email


def set_main(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
         
        order = f'Dear Nursultan new message for you \nName: {name}\nEmail: {email}\nMessage: {message}\nДата отправки: {datetime.now()}'
        base_url = f'https://api.telegram.org/bot5421110622:AAGTrih1SWDeaAEnn2S6erFwFu7Q1hPob5s/sendMessage?chat_id=-716220787&text={order}'
        requests.get(base_url)

        
           
        redirect('home')

    job = Job.objects.all()
    his = MyHistory.objects.all()
    con = {
        'jobs': job,
        'histories': his,
        # 'first': MyHistory.objects.filter(date__lte='2014-01-01').last()
        'first': MyHistory.objects.all().filter(date__lte='2014-01-01')
    }

    return render(request, "index.html", con)
