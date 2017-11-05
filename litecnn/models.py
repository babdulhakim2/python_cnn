from django.db import models

# Create your models here.



def upload_location(instance, filename):
	return "images/%s/%s" %(instance.title, filename)

class Image(models.Model):
	title = models.CharField(max_length=500)
	image = models.ImageField(blank=True, null=True, 
                              upload_to=upload_location)


	def __str__(self):
		return self.title