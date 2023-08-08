from django.db import models



class student(models.Model):
	created_time = models.DateTimeField(auto_now_add=True)
	pic = models.ImageField(upload_to='img/')
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	father_name = models.CharField(max_length=120)
	mother_name = models.CharField(max_length=120)
	grandfather = models.CharField(max_length=120)
	data_of_birth = models.DateTimeField()
	born_city = models.CharField(max_length=60)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

