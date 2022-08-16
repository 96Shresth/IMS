from dataclasses import fields
from pyexpat import model
from executing import Source
from rest_framework import serializers
from django.contrib.auth.models import User


from assesment.models import incident


class ManagementSerializer(serializers.ModelSerializer):

    
    # reporter_name = serializers.SerializerMethodField()
    
   
    class Meta:
        model=incident
        fields='__all__'
    # def save(self, **kwargs):
    #     user_id=self.context['user_id']
    #     incident=incident.objects.create(**self.validated_data,reporter_name_id=user_id)
    
    #def get_reporter_name(self,obj): 
        #return obj.reporter_name.username