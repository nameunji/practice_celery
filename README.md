# Practice_Celery

## celery 반영 전
코드 : [e15de44](https://github.com/nameunji/practice_celery/commit/e15de44e93c6c90e1d954d223b7ac8c9c0087b22)  
해당 view가 실행되었을 때 메일 발송 + return 까지 약 8초정도 소요되었다.

## celery 반영 후
해당 view가 실행되었을 때 메일발송은 celery worker에게 넘겨주고 201을 바로 리턴하였다.



