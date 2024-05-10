from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializer import Taskserializer,userserializer
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from reminder.models import Task


# Create your views here.
class Taskviewset(ViewSet):
    
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args, **kwargs):
        qs=Task.objects.all()
        serializers=Taskserializer(qs,many=True)
        return Response(data=serializers.data)
    
    def create(self,request,*args, **kwargs):
        serializer=Taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(data=serializer.data)
        
    
    def retrieve(self,request,*args, **kwargs):                #get the data of specific object
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=Taskserializer(qs)
        return Response(data=serializers.data)
    
    
    def destroy(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response()
    
    def update(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=Taskserializer(data=request.data,instance=qs)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)


class SignUpView(APIView):
    
    def post(self,request,*args, **kwargs):
        serializer=userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)