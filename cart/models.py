from django.db import models
from rest_framework import serializers

# Create your models here.
class item(models.Model):
	Id=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	price=models.IntegerField()

	def __str__(self):
		return self.name

class itemserializer(serializers.ModelSerializer):
	class Meta:
		fields='__all__'