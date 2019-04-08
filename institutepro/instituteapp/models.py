from django.db import models

from django.db import models
from multiselectfield import MultiSelectField

class ContactData(models.Model):
       name=models.CharField(max_length=50)
       email=models.EmailField(max_length=50)
       mobile=models.IntegerField()
       COURSE_CHOICES=(
              ('python','python'),
              ('django','django'),
              ('ui','uitechonologies'),
              ('restapi','restapi'),
              ('flask','flask')
       )
       courses=MultiSelectField(max_length=100,choices=COURSE_CHOICES)
       LOCATION_CHOICES=(
              ('hyd','hyderabad'),
              ('bang','banglore'),
              ('che','chennai'),
       )
       locations=MultiSelectField(max_length=100,choices=LOCATION_CHOICES)

       SHIFT_CHOICES=(
              ('mrng','morning'),
              ('aftrn','afternoon'),
              ('evng','evening'),
              ('nyt','night')
       )
       shifts=MultiSelectField(max_length=100,choices=SHIFT_CHOICES)
class FeedbackData(models.Model):
       name=models.CharField(max_length=100)
       rating=models.IntegerField()
       date=models.DateField()
       feedback=models.TextField(max_length=600)
