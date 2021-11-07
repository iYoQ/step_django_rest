from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from books_rest.celery import app
from datetime import datetime

@app.task(bind=True)
def send_email(request):
    # send_mail(
    # 'Subject here',
    # 'Here is the message.',
    # 'iyoqpwnz@gmail.com',
    # ['iyoqpwnz@gmail.com'],
    # fail_silently=False,
    email = EmailMessage('Subject', 'Body', to=['iyoqpwnz7@gmail.com'])
    email.send()
# )

@app.task(bind=True)
def save_date():
    with open('dates.txt', 'a') as f:
        print(f'date: {datetime.now().date()}', file=f)