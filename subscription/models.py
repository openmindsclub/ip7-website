from django.db import models

class Subscribe(models.Model):
	email = models.EmailField(unique=True)
	firstname = models.CharField(max_length=20)
	familyname = models.CharField(max_length=20)
	occupation = models.CharField(max_length=20)


	def __unicode__(self):
		return self.email;


