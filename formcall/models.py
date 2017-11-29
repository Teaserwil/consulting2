from django.db import models

# Create your models here.
class Formcall(models.Model):
	email = models.EmailField()
	name = models.CharField ( max_length = 128 )
	city = models.CharField ( max_length = 128 )
	number = models.CharField ( max_length = 20 )
	def __str__(self):
		return "%s %s %s %s" % ( self.name , self.email, self.city, self.number )
	
	class Meta:
		verbose_name = "Call"
		verbose_name_plural = "Calls"