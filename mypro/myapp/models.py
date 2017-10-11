from django.db import models
class data(models.Model):
  ProfilePicture=models.CharField(max_length=1000)
  Name=models.CharField(max_length=50)
  Email=models.CharField(max_length=50)
  Mobile=models.CharField(max_length=12)
  NationalId=models.CharField(max_length=14)
  University=models.CharField(max_length=50)
  Faculty=models.CharField(max_length=50)
  Major=models.CharField(max_length=50)
  Minor=models.CharField(max_length=50)
  ExpectedGraduationYear=models.CharField(max_length=4)

  def __str__(self):
      return self.Name



