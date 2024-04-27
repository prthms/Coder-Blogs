from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	desc = models.CharField(max_length=300)
	phone = models.IntegerField(default=0)
	contact_date = models.DateField(default='')
	def __str__(self):
		return self.name

class myPost(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	slug = models.CharField(max_length=100)
	content = models.TextField()
	author = models.CharField(max_length=50)
	category = models.CharField(max_length=50)
	postDate = models.DateTimeField(max_length=40)
	postViews = models.IntegerField(default=0)
	thumbnail = models.ImageField(upload_to='blog/thumnail/',max_length=100,default='',null=True)
	def __str__(self):
		return self.title+" by "+self.author

class blogComment(models.Model):
	sno = models.AutoField(primary_key=True)
	comment = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(myPost, on_delete=models.CASCADE)
	parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
	commentTime = models.DateTimeField(default=now)


