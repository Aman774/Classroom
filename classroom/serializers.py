from rest_framework import serializers
from . import models

from django.contrib.auth.models import User




class UserClassQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserClassQuestion
        fields = '__all__'

    def to_representation(self, instance):
        data = super(UserClassQuestionSerializer, self).to_representation(instance)

        data["user"] = {
                "name": instance.user.first_name,

            }
        data["schedule_class"]={
                "name":instance.schedule_class.name
            }
        data["question"] = {
                "text": instance.question.Question_text
            }
        return data