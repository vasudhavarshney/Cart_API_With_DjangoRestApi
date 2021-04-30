from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import item,itemserializer

# Create your views here.
'''def cartpage(request):
	return render(request,"cart.html")'''
class itemlist(APIView):
	def get(self,request):
		items1=item.objects.all()
		serializer=itemserializer(items1,many=True)
		return Response(serializer.data)

	def post(self):
		pass
