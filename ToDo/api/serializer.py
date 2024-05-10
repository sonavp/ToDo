from rest_framework import serializers
from reminder.models import Task,User

class Taskserializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Task
        fields="__all__"
        read_only_fields=['id','user','name']
        
        
class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','password']
        read_only_fields=['id']
        
        def create(self,validate_data):
            return User.objects.create_user(**validate_data)