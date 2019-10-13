from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
	author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	title=models.CharField(max_length=254)	
	text=models.TextField(max_length=2544)
	create_date=models.DateTimeField(default=timezone.now)
	publish_date=models.DateTimeField(blank=True,null=True)
	
	def Publish(self):
		self.publish_date=timezone.now()
		self.save()
	
	def __str__(self):
		return self.title
