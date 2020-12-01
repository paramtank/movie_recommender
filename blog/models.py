from django.db import models
from datetime import datetime 

class Blog(models.Model):
    title = models.CharField(max_length = 100 ,verbose_name = 'Baslik Giriniz' , help_text = 'Baslik Bilgisi Burada Girilir' , blank=False , null=True, )
    icerik = models.TextField(max_length = 1000 , verbose_name = 'Icerik Giriniz',null=True , blank=False)
    created_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)



class userLiked(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username= models.CharField(max_length=100)
    liked_movie= models.CharField(max_length=100)



#class Comment(models.Model):
#    comment_id = models.IntegerField(primary_key=True)
#    username= models.CharField(max_length=100)
#    comment= models.TextField(max_length=500)


class friend(models.Model):
    friend_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    friend_username = models.CharField(max_length=100)

""" class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(default="Default Value")
    body = models.TextField(default="Comment Here")
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name) """
