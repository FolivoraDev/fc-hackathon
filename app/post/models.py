from django.db import models

# Create your models here.
from member.models import User


class Post(models.Model):
    """
    # 제목 title
    # 글쓴이 author(user)
        # 닉네임 nickname
        # 아이디 패스워드 id, pwd
    # 내용 content
    # 댓글 comment
        # 내용 content
        # 쓴 사람 author
        # 비밀 번호 pwd
        # 작성일 created_at
        # 수정일 updated_at
    # 작성일 created_at
    # 수정일 updated_at
    #후원댓글(댓글)  donation_comment(comment)
        # 후원액수 donation_price

    """

    title = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Comment(models.Model):
    """
    # 댓글 comment
        # 내용 content
        # 쓴 사람 author
        # 비밀 번호 pwd
        # 작성일 created_at
        # 수정일 updated_at
    """
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class DonationComment(Comment):
    donation_price = models.IntegerField()
