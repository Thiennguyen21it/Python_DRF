from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer 
from rest_framework import generics,permissions
from .serializer import SignupSerializer
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer






# class GetAllUserApi(APIView):
#     def get(self,request,pk=None):
#          if pk is None:
#                   users = User.objects.all()
#                   mydata = GetAllUserSerializer(users,many=True)
#                   return Response(data=mydata.data,status=status.HTTP_200_OK)
#          else: 
#                   user = User.objects.get(id=pk)
#                   mydata = GetAllUserSerializer(user)
#                   return Response(data=mydata.data,status=status.HTTP_200_OK) 
          
#     def post(self,request):
#           mydata = UserSerializer(data=request.data)
#           if not mydata.is_valid():
#                 return Response("sai du lieu roi ",status=status.HTTP_400_BAD_REQUEST)
#           first_name = mydata.data["firts_name"]
#           last_name = mydata.data["last_name"]
#           user = User.objects.create(firts_name=first_name,last_name=last_name)
#           return Response(data = user.id,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#               user = User.objects.get(id=pk)
#               mydata = UserSerializer(data=request.data)
#               if not mydata.is_valid():
#                   return Response("sai du lieu roi ",status=status.HTTP_400_BAD_REQUEST)
#               first_name = mydata.data["firts_name"]
#               last_name = mydata.data["last_name"]
#               user.firts_name = first_name
#               user.last_name = last_name
#               user.save()
#               return Response(data = user.id,status=status.HTTP_200_OK)
#     def delete(self,request,pk):
#             user = User.objects.get(id=pk)
#             user.delete()
#             return Response(data = user.id,status=status.HTTP_200_OK)
            
      