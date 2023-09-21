from django.db import models
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
	content=models.CharField(max_length=1000)

