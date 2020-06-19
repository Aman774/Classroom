from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from classroom.models import UserClassQuestion,Class,Question
from django.contrib.auth.models import User
from classroom.serializers import  UserClassQuestionSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from helpers.permission import IsAdmin

# Create your views here.



def Success_response(obj):
    print("success")
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











#for adding classes and questions to users(students) using user_id,class_id and question_id

@api_view(["POST"])
@permission_classes([IsAdmin])
def addClasses(request):

    user = request.data["user_id"]

    schedule_class = request.data["class_id"]

    question =request.data["question_id"]

    user_instance= User.objects.get(id=user)
    schedule_class_instance=Class.objects.get(id=schedule_class)
    question_instance= Question.objects.get(id=question)


    if UserClassQuestion.objects.filter(user=user_instance,schedule_class=schedule_class_instance,question=question_instance).exists():
      return fail_response({"error":"already exist"})
    else:
         users_class_question_obj=UserClassQuestion.objects.create(user=user_instance,schedule_class=schedule_class_instance,question=question_instance)


    try:


        info = {
            "user_class_question": UserClassQuestionSerializer(users_class_question_obj).data}
        return Success_response(info)



    except Exception as e:
       fail_response({'error':str(e)})




#Top 3 scheduled classes will be shown in upcoming classes along with question
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_upcoming_classes(request):
     print(request.user)
     upcoming=[];

     if UserClassQuestion.objects.filter(user=request.user).exists():

         Classes = UserClassQuestion.objects.filter(user=request.user)
         length = Classes.count()


         if length > 3:
             length = 3

         for i in range(0, length):
             upcoming.append(UserClassQuestionSerializer(Classes[i]).data)

         return Response(upcoming, status.HTTP_200_OK)

     else:
         return fail_response({"error":"classes not found for user"})


