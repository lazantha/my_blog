from django.db import models
from django.utils import timezone
#password=1234



class UserTable(models.Model):
	id=models.AutoField(primary_key=True)
	dp=models.FileField(null=True,blank=True)
	email=models.CharField(max_length=50,null=False)
	name=models.CharField(max_length=100)
	

class PostTable(models.Model):
	id=models.AutoField(primary_key=True)
	user_id=models.ForeignKey(UserTable, on_delete=models.CASCADE)
	topic=models.CharField(max_length=50)
	link=models.CharField(max_length=255)
	content=models.CharField(max_length=1000)
	created_at = models.DateTimeField(default=timezone.now)


