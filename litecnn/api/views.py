from django.db.models import Q
from rest_framework import generics, permissions

from .serializers import ProductModelSerializer
from litecnn.models import Image



# This is the create API View

class UploadImageAPIView(generics.CreateAPIView):
	serializer_class = ProductModelSerializer

	def do_ocr(self):
		print("gff")
		
