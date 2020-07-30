import json

from django.views import View
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import Qna
from practice_celery.settings import DEFAULT_FROM_EMAIL


class QnaView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data["email"])
            Qna(
                name=data["name"],
                email=data["email"],
                content=data["content"]
            ).save()

            send_mail(
                subject='test',
                message=data["content"],
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=[data["email"]],
                fail_silently=False
            )
            return HttpResponse(status=201)
        except ValidationError:
            return JsonResponse({"message": "INVALID_EMAIL"}, status=400)