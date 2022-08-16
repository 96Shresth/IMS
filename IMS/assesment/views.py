from pickle import PUT
from urllib import request, response
from django.shortcuts import render
from .models import incident, incident_no
from django.contrib.auth.models import User
from .seriealizers import ManagementSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,RetrieveUpdateAPIView,GenericAPIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.mixins import CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin,ListModelMixin
from django.http import HttpResponseRedirect
from .permission import Owner, PutClosed
from django.core.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter

class CreateApi(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = incident.objects.all()
    serializer_class = ManagementSerializer
    
    permission_classes=[Owner]

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


    # def get_serializer_context(self):
    #     return {
    #         'user_id':self.reporter_name.id
    #     }
    
    # def create(self, request, *args, **kwargs):
    #     response = super(CreateApi,self).create(request, *args, **kwargs)
    #     return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/myapi/<int:pk>/')

class RUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = incident.objects.all()
    serializer_class = ManagementSerializer
    
    permission_classes=[Owner,PutClosed]


    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



    # def save(self,*args,**kwargs):
    #     if request.method==PUT and self.incident_status=="closed":
    #         raise PermissionDenied()
    #     else:
    #         super()
    #     super(RUD,self).save(*args,**kwargs)

# class IncidentModelViewset(viewsets.ModelViewSet):
#     queryset = incident.objects.all()
#     serializer_class = ManagementSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[IsAuthenticated]



class List(ListAPIView):
    queryset = incident.objects.all()
    serializer_class = ManagementSerializer
    filter_backends = [SearchFilter]
    search_fields = ['incident_number']
    permission_classes = [IsAdminUser]


# class Create(CreateAPIView):
#     queryset = incident.objects.all()
#     serializer_class = ManagementSerializer

# class Retrive(RetrieveAPIView):
#     queryset = incident.objects.all()
#     serializer_class = ManagementSerializer

# class Update(UpdateAPIView):
#     queryset = incident.objects.all()
#     serializer_class = ManagementSerializer

# class RetriveUpdate(RetrieveUpdateAPIView):
#     queryset = incident.objects.all()
#     serializer_class = ManagementSerializer
