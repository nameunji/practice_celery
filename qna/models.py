from django.db import models


class Qna(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_send = models.BooleanField(default=False)

    class Meta:
        db_table = 'qna'
