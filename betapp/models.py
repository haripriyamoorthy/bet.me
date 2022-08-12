from django.db import models
from django.contrib.auth.models import User

# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.



class game(models.Model):
    name = models.CharField(max_length=120)
    best_player = models.CharField(max_length=120)
    score = models.IntegerField()
    
    def __str__(self):
        return self.name
        

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_no = models.IntegerField()
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Players(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField(null=True)
    best_score = models.IntegerField()
    base_price = models.IntegerField()

    def __str__(self):
        return self.first_name


class UpcommingMatchs(models.Model):
    sports_name = models.CharField(max_length=120)
    sports_title = models.CharField(max_length=120)
    start_time = models.DateTimeField()
    home_team = models.CharField(max_length=120)
    away_team = models.CharField(max_length=120)
    

    def __str__(self):
        return self.sports_title

class BetBooking(models.Model):
    upcomming_match = models.CharField(max_length=120)
    user_id = models.ForeignKey(UserProfileInfo,on_delete=models.CASCADE)
    price = models.CharField(max_length=120)

    def __str__(self):
        return self.upcomming_match



    

    
    
    
    
    
    

    