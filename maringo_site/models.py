from django.db import models
#from networkx import constraint

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    next_of_kin = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    age = models.IntegerField()
    status = models.CharField(max_length=20)
    class Meta:
          constraints = [models.CheckConstraint(check=models.Q(age__gte=13) & models.Q(age__lt=35), name='Age is valid between 13 and 35')]

    def __str__(self):
            return self.name
    
