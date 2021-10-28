from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from books_rest.celery import app

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