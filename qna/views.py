import json

from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import Qna
from .tasks import task_send_email


class QnaView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            validate_email(data["email"])
            qna = Qna(
                name=data["name"],
                email=data["email"],
                content=data["content"]
            )
            qna.save()

            task_send_email.delay(data["content"], data["email"], qna.id)
            return HttpResponse(status=201)
        except ValidationError:
            return JsonResponse({"message": "INVALID_EMAIL"}, status=400)