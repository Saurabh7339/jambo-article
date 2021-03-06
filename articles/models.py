from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Articles(models.Model):
	title=models.CharField(max_length=100)
	slug=models.SlugField()
	body= models.TextField(max_length=1000)
	date=models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default='default.png',blank=True)
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    

	def __str__(self):
		return self.title


	def snippet(self):
		return self.body[:50]+'...'