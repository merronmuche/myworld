from django.db import models

from django.db import models

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  age = models.IntegerField()

  def __str__(self):
        return self.firstname

