from django.utils.timesince import timesince
from rest_framework import serializers

from litecnn.models import Image



class ProductModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = [
			'title',
			'image'
		] 

