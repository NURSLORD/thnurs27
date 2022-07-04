from datetime import datetime

from django.conf import settings
from django.shortcuts import render, redirect

# Create your views here.
from post.models import Job, MyHistory, Email
from django.core.mail import send_mail


def set_main(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'thnurs27 Заявка',
            f'Dear Nursultan new message for you \nName: {name}\nEmail: {email}\nMessage: {message}\nДата отправки: {datetime.now()}',
            settings.EMAIL_HOST_USER,
            ['normosbekov@gmail.com', ]
        )
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
