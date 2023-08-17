from django.db import models

# Create your models here.
# django모델을 상속받는 Post 클래스 정의
class Post(models.Model):
    # 문자열 저장하는 속성
    title = models.CharField(max_length=30)
    content = models.TextField()

    # 글이 쓰여진 시각, auto_now_add=True:현재시간 기록
    created_at = models.DateTimeField(auto_now_add=True)
    # 최근수정일
    update_at = models.DateTimeField(auto_now=True)

#     숫자코드 : num_stars=models.IntegerField()

