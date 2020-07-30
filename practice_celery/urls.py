from django.urls import path, include

urlpatterns = [
    path('qna', include('qna.urls'))
]
