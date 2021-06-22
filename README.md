# Practice_Celery
  
<br> 

## celery 반영 전
코드 : [e15de44](https://github.com/nameunji/practice_celery/tree/e15de44e93c6c90e1d954d223b7ac8c9c0087b22)  
해당 view가 실행되었을 때 메일 발송 + return 까지 약 8초정도 소요되었다.  
  
<br>  
  
## celery 반영 후
코드 : [1ee7294](https://github.com/nameunji/practice_celery/tree/1ee72944d9d0878417d1ddc98fcf2268fa7506bc)
해당 view가 실행되었을 때 메일발송은 celery worker에게 넘겨주고 201을 바로 리턴하였다.  

<br>
  
## blog
https://velog.io/@nameunzz/Celery-Redis

