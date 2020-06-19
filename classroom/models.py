from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Class(models.Model):
    name = models.CharField(max_length=200)
    start_time=models.DateTimeField(default=now)
    end_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class Question(models.Model):
     Question_text = models.TextField(max_length=500)

     def __str__(self):
         return self.Question_text



class UserClassQuestion(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    schedule_class =models.ForeignKey(Class,on_delete=models.CASCADE)
    question =models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.schedule_class.name