from users.models import Profile
from rest_framework.views import APIView

from rest_framework.response import Response
from users.serializers import ProfileSerializer
from users.serializers import RegistrationSerializer

from users.serializers import  UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
import json

from django.contrib.auth.models import User



def Success_response(obj):
    content = {
                    'status': {
                        'isSuccess': True,
                        'code': "SUCCESS",
                        'message': "Success",
                    },
                }

    for key, value in obj.items():
         content['status'][key] = value
    return Response(content, status=status.HTTP_200_OK)


def fail_response(obj):
    content = {
                    'status': {
                        'isSuccess': False,
                        'code': "fail",
                        'message': "failed",
                    },
                }

    for key, value in obj.items():
         content['status'][key] = value
    return Response(content, status=status.HTTP_200_OK)




class LoginFun(APIView):
    def post(self,request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                email = request.data['email']
                password = request.data['password']
                try:
                    user_email_obj = User.objects.get(email__iexact=email)
                except Exception as e:
                    return fail_response({'error':str(e)})
                    user_email_obj = None




                if user_email_obj:
                    user_obj = authenticate(username=user_email_obj.username,password=password)

                    if user_obj:
                        token,create = Token.objects.get_or_create(user=user_obj)
                        profile_obj = Profile.objects.filter(user=user_obj).first()



                        ob = {
                        'token':token.key,
                        'profile':ProfileSerializer(profile_obj).data,

                        }
                        return Success_response(ob)
                    else:
                        return fail_response({'error':'password is wrong'})

                else:
                    return fail_response({'error':'user not found'})
            else:
                return fail_response({'error':serializer.errors})

        except Exception as e:
            return fail_response({'error':e})



class Registation(APIView):
    def post(self,request):
        try:
          serializer = RegistrationSerializer(data=request.data)
   
          if serializer.is_valid():
               email=request.data['email']
               first_name = request.data['first_name']

               last_name = request.data['last_name']
               age=request.data['age']
               city=request.data['city']
               grade=request.data['grade']
               board=request.data['board']
               phone = request.data['phone']
               password = request.data['password']
               
               
               try:
                   user_email_obj = User.objects.filter(username=email,email=email,first_name=first_name,last_name=last_name)
                   print (user_email_obj)
                   if user_email_obj:
                      return fail_response({'error':'user already exist'})
                   else:
                        user_obj = User.objects.create(username=email,email=email,first_name=first_name,last_name=last_name)
                        user_obj.set_password(password)
                        user_obj.save()
                        token = Token.objects.create(user=user_obj)
                        profile_obj = Profile.objects.create(user=user_obj,email=email,phone=phone,age=age,city=city,grade=grade,board=board)


                        objt = {
                        'profile':ProfileSerializer(profile_obj).data,
                        'Token':token.key,
                        }

                        return Success_response(objt)

               except Exception as e:

                    return fail_response({'error':str(e)})

          else:
                return fail_response({'error':str(serializer.errors)})

                
        except Exception as e:
             return fail_response({'error':e}) 

               
                
                
                


                
          


                







