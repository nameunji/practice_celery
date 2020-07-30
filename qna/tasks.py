from django.core.mail import send_mail
from celery import shared_task

from practice_celery.settings import DEFAULT_FROM_EMAIL
from .models import Qna


@shared_task
def task_send_email(content, email, id):
    send_mail(
        subject='문의내용입니다.',
        message=content,
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False
    )
    qna = Qna.objects.get(id=id)
    qna.is_send = True
    qna.save()
    return None