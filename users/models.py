from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    age=models.IntegerField(null=False,blank=False)
    city=models.CharField(max_length=200)
    grade=models.CharField(max_length=200)
    board=models.CharField(max_length=200)
    phone = models.CharField(max_length=10,blank=True, null= True)
    email = models.EmailField(max_length=100,blank=False,null= False)
    


    def __str__(self):
    	return self.user.first_name





class Roles(models.Model):
    """
     Roles
    1. Admin
    2. Student
    """

    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name

class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)


    def __str__(self):
        return "{} {}".format(self.user, self.role)



